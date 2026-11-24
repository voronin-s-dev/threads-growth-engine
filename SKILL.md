---
name: threads-growth-engine
description: Universal Threads growth system for AI agents. Autonomously extracts project context, deconstructs viral competitor threads, generates 1-click reactive comments, writes high-retention anchor threads, and audits drafts via a cold-reader proxy.
---

# 🧵 Threads Growth Engine: Autonomous Operating System

> **Purpose:** Universal, niche-agnostic growth system for organic audience acquisition on the Threads platform.

---

## 1. Protocol 1: Zero-Config Project Auto-Discovery

The agent initializes the user profile through autonomous workspace inspection.

### Step 1: Passive Workspace Scan
1. The agent searches the root workspace and subdirectories for context files.
2. The agent reads `README.md`, `ABOUT.md`, `BIO.md`, `AUTHOR.md`, `POSITIONING.md`, and `AGENTS.md`.
3. The agent searches folders named `docs/`, `knowledge/`, `brand/`, and `marketing/`.
4. The agent extracts five core anchors:
   - **Anchor 1: Author Identity.** Professional title, status, and background.
   - **Anchor 2: Niche and Core Pillars.** Three to four primary topics.
   - **Anchor 3: Target Audience.** Reader demographics, pain points, and desire states.
   - **Anchor 4: Tone and Taboos.** Voice style, forbidden terminology, and banned claims.
   - **Anchor 5: Target Action (CTA).** Profile link, direct message trigger, or engagement goal.

### Step 2: Gap Analysis and Targeted Interview
1. The agent checks if any of the five anchors are missing.
2. If all five anchors are present, the agent presents a four-line summary for user confirmation.
3. If any anchor is missing, the agent asks only targeted questions to fill the specific missing gaps.
4. The agent never asks the user to fill existing information.

### Step 3: Profile Persistence
1. The agent saves the confirmed profile to `THREADS_PROFILE.md` in the project root.
2. All subsequent workflows read `THREADS_PROFILE.md` directly.
3. The agent avoids rescanning the workspace on future executions.

---

## 2. Protocol 2: Viral Post Reverse-Engineering

The agent deconstructs external viral posts to build customized niche templates.

### Workflow:
1. The user provides a viral post text or reference link.
2. The agent isolates the first sentence and extracts the structural hook formula.
3. The agent identifies the psychological tension driving audience engagement.
4. The agent extracts the comment trigger located in the closing lines.
5. The agent transposes the structural formula into the user's specific niche from `THREADS_PROFILE.md`.
6. The agent appends the raw post and transposed formula to `FEW_SHOT_STYLE_BANK.md`.
7. The agent preserves structural syntax while replacing all original domain concepts.

---

## 3. Protocol 3: 1-Click Reactive Commenting

The agent generates rapid reply comments for incoming viral threads.

### Speed and Execution Rules:
1. The agent delivers comments immediately to preserve the viral reaction window.
2. The agent never runs multi-turn critique subagents on comments.
3. Every comment must stay strictly under 500 characters.
4. The agent verifies length using `len(text) <= 500` before output.
5. The agent delivers three to four distinct comment options in isolated code blocks:
   - **Option 1: Contrarian Frame.** Questions the core premise with a respectful alternative view.
   - **Option 2: Hidden Nuance.** Adds a non-obvious practical detail or edge case.
   - **Option 3: Grounded Experience.** Shares a compact, relatable personal scene.
   - **Option 4: Witty Mirror.** Reflects the paradox with dry relatable humor.
6. The agent marks one option as `(Recommended)`.
7. The agent appends a one-line reader impact rating below each option.

---

## 4. Protocol 4: High-Retention Anchor Thread Writing

The agent crafts five-post anchor threads following the proven viral architecture.

### Thread Structure:
1. **Post 1 (Hook and Scene):**
   - Contains the core keyword in the first two lines.
   - Grounds the problem in a recognizable physical scene or dialogue.
   - States an acute paradox without revealing the solution.
   - Ends with an open tension requiring reader to expand the thread.
2. **Post 2 (Hidden Mechanism):**
   - Explains the underlying psychological, technical, or systemic cause.
   - Eliminates generic motivational slogans.
3. **Posts 3 and 4 (Actionable Shift):**
   - Delivers one to two concrete, testable micro-actions.
   - Uses bullet points only for executable steps.
4. **Post 5 (Resolution and Discussion Trigger):**
   - Delivers a memorable synthesis insight.
   - Includes an open discussion question that provokes debate or shared experience.
   - Integrates the subtle profile CTA defined in `THREADS_PROFILE.md`.

### Formatting Constraints:
1. Every individual post must remain under 500 characters.
2. Paragraphs contain two to three compact sentences.
3. The agent rejects single-line sentences separated by blank lines.
4. The agent rejects external links in Post 1.

---

## 5. Protocol 5: Dual-Phase Quality Gate

Every thread draft must pass two deterministic verification gates before publishing.

### Phase 1: Technical & Anti-Slop Gate
1. The agent runs `py scripts/lint_threads.py <file>` or checks text in-memory.
2. The agent enforces zero occurrences of banned AI cliches.
3. The agent validates character limits on every individual post.
4. Status must be 100% clean PASS.

### Phase 2: Reader Proxy Gate (Cold Audience Simulation)
The agent simulates an impatient user scrolling a smartphone feed with a 1.5-second attention span.
The agent scores the draft on four strict criteria:
1. **Thumb-Stop:** Does the opening line force an instant scroll pause? (Target: >= 8/10).
2. **Tone Check:** Does the voice sound like an equal peer? Text contains zero preachiness.
3. **Brevity Cut:** The agent cuts 20% to 30% of unnecessary explanatory text.
4. **Discussion Trigger:** Does the ending provoke replies or counter-arguments?

The agent outputs the trimmed, finalized text alongside the structured audit scores.
