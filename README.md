# 🧵 Threads Growth Engine

> **Universal, niche-agnostic organic growth system for AI coding agents and human creators on Threads.**

---

## ⚡ What is Threads Growth Engine?

`threads-growth-engine` is an autonomous skill that turns your AI agent into an elite Threads showrunner. It decouples platform mechanics, viral post deconstruction, and audience psychology from specific niche topics. 

Whether your niche is **software engineering, fitness, B2B sales, design, or crypto**, the skill adapts to your voice without leaking another creator's concepts.

---

## 🚀 Key Capabilities

1. **Zero-Config Workspace Auto-Discovery:**
   * The agent scans your existing project files (`README.md`, `about.md`, `positioning.md`, docs) to extract your author identity, niche, audience, and CTA.
   * If any information is missing, the agent asks **only 1–2 targeted questions** instead of forcing you to fill lengthy questionnaires.
   * Caches your profile in `THREADS_PROFILE.md` to prevent unnecessary token consumption.

2. **Smart Screenshot Triage & Viral Reverse-Engineering:**
   * Drop a screenshot, link, or text of any Threads post.
   * The agent automatically checks whether you already commented, whether it is a reply to you, or a thread continuation.
   * For fresh viral posts, it delivers 1-click comments immediately and automatically deconstructs the hook formula for *your* niche. For ongoing dialogues, it skips deconstruction and replies in context.

3. **1-Click Reactive Commenting (Early Follower Engine):**
   * Instant delivery of 3–4 high-impact comment angles (<500 characters): *Contrarian Frame*, *Hidden Nuance*, *Grounded Case*, and *Witty Mirror*.
   * Includes an inline **Reader Punch Check** rating so you can copy-paste and win the 15-minute viral window.

4. **High-Retention Anchor Threads:**
   * Crafts 5-post anchor threads using the proven viral sequence: *Scene/Hook → Mechanism → Action Steps → Debate Trigger*.
   * Strictly enforces character limits (`<= 500` chars per post) and clean visual formatting.

5. **Dual-Phase Quality Gate (Ruthless Reader Proxy):**
   * **Phase 1 (Technical & Anti-Slop):** Verifies zero AI cliches, length limits, and layout rules via the bundled zero-dependency Python linter `lint_threads.py`.
   * **Phase 2 (Cold Reader Proxy):** Simulates an impatient smartphone user with a 1.5-second attention span. Scores your hook (Thumb-stop), eliminates preaching, cuts 20–30% of dead text, and verifies the reply trigger.

---

## 📦 Installation & Setup

### Option 1: Install as an Agent Skill (Antigravity / Claude Code)

Clone this repository into your global or project skills directory:

```bash
# In your project root:
git clone https://github.com/voronin-s-dev/threads-growth-engine.git .agents/skills/threads-growth-engine

# Or into your global agent skills folder:
# Windows:
git clone https://github.com/voronin-s-dev/threads-growth-engine.git %USERPROFILE%\.gemini\config\skills\threads-growth-engine
# Mac/Linux:
git clone https://github.com/voronin-s-dev/threads-growth-engine.git ~/.gemini/config/skills/threads-growth-engine
```

### Option 2: Copy as a Project Module
Simply copy the `threads-growth-engine` folder into your project's skills or rules directory.

---

## 🛠️ How to Use (Workflows)

Once installed, your agent activates the skill automatically or when you ask:

### 1. Initialize Profile
```text
"Настрой мой профиль для Threads" or "/threads init"
```
*The agent will inspect your repository, summarize what it found, ask for any missing details, and save `THREADS_PROFILE.md`.*

### 2. Generate 1-Click Comments
```text
"Вот залетевший пост конкурента: [текст поста]. Напиши 3 варианта комментария от моего лица"
```
*The agent returns 3–4 punchy, verified comments under 500 characters with one recommended pick.*

### 3. Deconstruct a Viral Thread
```text
"Разбери этот тред и напиши аналогичный по структуре пост в моей нише: [текст или ссылка]"
```
*The agent breaks down the hook syntax and creates an original draft tailored to your expertise.*

### 4. Write an Anchor Thread
```text
"Напиши тред из 5 постов на тему [твоя идея]"
```
*The agent drafts the thread and runs it through both Phase 1 (technical linter) and Phase 2 (cold reader audit) before presenting it to you.*

---

## 📁 Repository Structure

```text
threads-growth-engine/
├── SKILL.md                            # Main agent skill definition & orchestration logic
├── README.md                           # Documentation & quickstart guide
├── rules/
│   ├── threads-algorithm.md            # Cadence, ranking factors & character limits
│   ├── auto-discovery-protocol.md      # Heuristics for scanning repo & gap resolution
│   ├── viral-deconstruction.md         # Formula reverse-engineering pipeline
│   ├── reactive-commenting.md          # 4-angle commenting strategies & speed rules
│   ├── reader-proxy-standard.md        # The 4 axes of the impatient feed reader
│   └── antislop-threads.md             # Banned AI cliches & human voice standards
├── templates/
│   ├── THREADS_PROFILE_TEMPLATE.md     # Reference schema for author profile
│   └── FEW_SHOT_STYLE_BANK_TEMPLATE.md # Template for storing deconstructed viral pairs
└── scripts/
    └── lint_threads.py                 # Standalone, zero-dependency Python 3 linter
```

---

## 🧪 Local Verification

Run the bundled linter directly in your terminal:

```bash
# Check any file:
python scripts/lint_threads.py path/to/thread.md

# Check inline text:
python scripts/lint_threads.py --text "Твой текст поста для проверки"
```

---

## 📄 License

MIT License. Free to use, adapt, and share.
