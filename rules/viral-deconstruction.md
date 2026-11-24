# 🔬 Viral Post Deconstruction Pipeline

> **Purpose:** Reverse-engineering viral posts into repeatable structural templates for any niche.

---

## 1. Triage and Trigger Rules

1. The agent runs triage on every incoming post or screenshot before deconstruction.
2. The agent verifies three conditions:
   - The user has not commented on the post yet.
   - The post is not a reply to the user's own comment.
   - The post is not a continuation of a thread already processed in the session.
3. If any condition fails, the agent skips deconstruction and delivers a contextual reply only.
4. If all three conditions pass, the agent runs deconstruction automatically after delivering 1-click comments.

---

## 2. Deconstruction Principles

1. Every viral post succeeds through structural tension rather than isolated domain facts.
2. The agent isolates the underlying syntax from the specific subject matter.
3. The agent transposes proven structures into the user niche defined in `THREADS_PROFILE.md`.
4. The agent never copies source text verbatim.

---

## 3. Four Analysis Layers

The agent deconstructs every target post into four layers:
1. **Hook Syntax:** The opening sentence pattern (contrast, counter-intuitive fact, or recognized scene).
2. **Psychological Tension:** The emotional or cognitive friction that keeps the user reading.
3. **Core Argument Engine:** How the author transitions from problem to mechanism to resolution.
4. **Discussion Trigger:** The specific phrasing that forces comments or debate.

---

## 4. Transposition Workflow

1. The agent extracts the structural formula:
   - Example Formula: `[Recognizable common mistake] + [Hidden actual cause] + [Counter-intuitive rule]`.
2. The agent fills the formula with domain concepts from `THREADS_PROFILE.md`.
3. The agent generates a complete response thread or standalone post.
4. The agent saves the pair into `FEW_SHOT_STYLE_BANK.md`.
