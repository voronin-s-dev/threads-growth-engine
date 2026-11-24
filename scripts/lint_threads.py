#!/usr/bin/env python3
"""Zero-dependency linter for Threads posts and comments.

Validates:
1. Strict 500-character limit per post/comment.
2. Anti-slop rules (banned AI cliches, preachiness, fake engagement bait).
3. Paragraph layout and readability.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_POST_CHARS = 500

BANNED_OPENINGS = [
    (r"^(?:in today'?s (?:fast-paced )?world|in a world where)", "Generic AI opening ('In today's world...')"),
    (r"^(?:let'?s dive in|let'?s break it down)", "Generic AI transition ('Let's dive in...')"),
    (r"^here is the ultimate guide to", "Generic guide cliché ('Here is the ultimate guide...')"),
    (r"^ever wondered why", "Rhetorical question hook ('Ever wondered why...')"),
    (r"^в современном мире", "Шаблонное ИИ-вступление ('В современном мире...')"),
    (r"^давайте разберем(?:ся)?", "Шаблонное вступление ('Давайте разберемся...')"),
    (r"^мало кто задумывается(?:, но)?", "ИИ-клише ('Мало кто задумывается...')"),
    (r"^вы когда-нибудь замечали", "Шаблонный риторический вопрос ('Вы когда-нибудь замечали...')"),
]

BANNED_PATTERNS = [
    # It's not X, it's Y reveals
    (r"(?:это|дело) не в [^\n.,]+,\s*(?:а|дело) в", "Паттерн разоблачения 'дело не в X, а в Y'"),
    (r"it'?s not (?:about )?[^\n.,]+,\s*it'?s (?:about )?", "Pattern 'it's not X, it's Y'"),
    # Preachy coaching imperatives
    (r"(?:перестаньте|прекратите) [^\n.,]+ (?:и начните|раз и навсегда)", "Менторский приказ ('Перестаньте...')"),
    (r"запомните раз и навсегда", "Менторское клише ('Запомните раз и навсегда')"),
    (r"вы обязаны [^\n.,]+", "Директивный тон ('Вы обязаны...')"),
    (r"you must stop [^\n.,]+ once and for all", "Preachy imperative ('You must stop...')"),
    # Cheap SMM engagement bait
    (r"(?:согласны\?|а как вы думаете\?)\s*(?:напишите|делитесь) в комментариях", "Синтетический СММ-вопрос в комментариях"),
    (r"agree\?\s*(?:let me know|share|tell me) in (?:the )?comments", "Synthetic engagement bait ('Agree? Share in comments')"),
    (r"сохраня(?:й|йте),? чтоб(?:ы)? не потерять", "Инфобизнесовое клише ('Сохраняй чтобы не потерять')"),
    (r"save this (?:post )?so you don'?t lose it", "Engagement cliché ('Save this so you don't lose it')"),
]


def split_into_posts(text: str) -> list[str]:
    """Split thread text by common markers (---, ### Post N, 1/N)."""
    # Remove YAML frontmatter if present
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    
    # Split by horizontal rule separator
    if "\n---\n" in text:
        parts = [p.strip() for p in text.split("\n---\n") if p.strip()]
        return parts

    # Split by markdown headers like '### Post 1', '## 1.', '1/5'
    header_split = re.split(r"\n(?=#{1,4}\s*(?:Пост|Post|\d+[\.\/\)]|\d+\s*[-–]))", text)
    if len(header_split) > 1:
        return [p.strip() for p in header_split if p.strip()]

    return [text.strip()]


def clean_post_for_length(post: str) -> str:
    """Clean markdown headings from length check if they are structural metadata."""
    # Strip leading markdown title line like '### Post 1'
    cleaned = re.sub(r"^#{1,4}\s+[^\n]+\n+", "", post).strip()
    return cleaned if cleaned else post


def lint_single_post(post: str, post_index: int = 1) -> list[str]:
    """Run deterministic checks on a single post or comment."""
    errors: list[str] = []
    cleaned_text = clean_post_for_length(post)
    char_count = len(cleaned_text)

    # 1. Character limit check
    if char_count > MAX_POST_CHARS:
        errors.append(
            f"[Post {post_index}] Превышен лимит длины: {char_count}/{MAX_POST_CHARS} знаков "
            f"(сократите на {char_count - MAX_POST_CHARS} симв.)"
        )

    # 2. Banned opening lines
    first_line = cleaned_text.strip().split("\n")[0].lower() if cleaned_text else ""
    for pattern, desc in BANNED_OPENINGS:
        if re.search(pattern, first_line, re.IGNORECASE):
            errors.append(f"[Post {post_index}] Запрещенный зачин: {desc}")

    # 3. Banned structural patterns
    for pattern, desc in BANNED_PATTERNS:
        match = re.search(pattern, cleaned_text, re.IGNORECASE)
        if match:
            matched_phrase = match.group(0)
            errors.append(f"[Post {post_index}] Нарушение тона: {desc} -> '{matched_phrase}'")

    # 4. Wall of text check (paragraph > 400 chars without line break)
    paragraphs = [p.strip() for p in cleaned_text.split("\n\n") if p.strip()]
    for p_idx, p in enumerate(paragraphs, 1):
        if len(p) > 380 and not any(p.startswith(bullet) for bullet in ("-", "*", "•", "1.", "2.")):
            errors.append(
                f"[Post {post_index}, Абзац {p_idx}] Слишком плотный абзац ({len(p)} симв.). "
                "Разбейте на 2-3 коротких предложения."
            )

    return errors


def lint_content(content: str) -> list[str]:
    """Lint entire file or thread."""
    posts = split_into_posts(content)
    all_errors: list[str] = []

    for idx, post in enumerate(posts, 1):
        post_errors = lint_single_post(post, post_index=idx)
        all_errors.extend(post_errors)

        # Check for link in Post 1 if it is a multi-post thread
        if idx == 1 and len(posts) > 1:
            if re.search(r"https?://|t\.me/|bit\.ly/", post):
                all_errors.append(
                    "[Post 1] Ссылка в первом посте треда снижает охваты алгоритмом. "
                    "Перенесите ссылку в био профиля или в финальный пост."
                )

    return all_errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint Threads posts for length and anti-slop rules.")
    parser.add_argument("path", nargs="?", help="Path to markdown or text file to lint.")
    parser.add_argument("--text", type=str, help="Direct text string to lint.")
    args = parser.parse_args()

    if args.text:
        content = args.text
        source_name = "Inline text"
    elif args.path:
        path = Path(args.path)
        if not path.is_file():
            print(f"❌ Ошибка: файл '{path}' не найден.", file=sys.stderr)
            return 1
        content = path.read_text(encoding="utf-8")
        source_name = path.name
    else:
        parser.print_help()
        return 1

    errors = lint_content(content)

    if errors:
        print(f"\n❌ Ошибки линтера в '{source_name}':")
        for err in errors:
            print(f"  • {err}")
        print(f"\nИтого нарушений: {len(errors)}")
        return 1

    posts = split_into_posts(content)
    print(f"\n✅ PASS: '{source_name}' успешно прошел все проверки ({len(posts)} пост(ов)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
