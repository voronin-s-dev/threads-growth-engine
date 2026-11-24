# 🔍 Workspace Auto-Discovery Protocol

> **Purpose:** Autonomous extraction of user positioning from existing workspace files.

---

## 1. File Discovery Sequence

1. The agent inspects the workspace root for documentation files.
2. The agent reads `README.md`, `ABOUT.md`, `BIO.md`, `AUTHOR.md`, and `POSITIONING.md`.
3. The agent inspects `docs/`, `knowledge/`, `brand/`, and `marketing/` directories.
4. The agent checks existing product descriptions, landing page copy, and bot configurations.

---

## 2. Five Core Anchors

The agent extracts five mandatory fields:
1. **Author Identity:** Who is writing, their professional role, and primary background.
2. **Niche and Core Pillars:** Three to four primary topics covered in the profile.
3. **Target Audience:** Who the content serves, their struggles, and their goals.
4. **Tone and Taboos:** Desired communication style and explicitly forbidden topics.
5. **Target Action (CTA):** Next step for readers, such as profile links or direct messages.

---

## 3. Interactive Gap Resolution

1. If all five anchors exist, the agent presents a concise confirmation summary:
   - "I analyzed your workspace files. Here is your profile summary: [Summary]. Do you confirm?"
2. If any anchor is missing, the agent asks only for the missing information.
3. The agent limits questions to a maximum of two targeted prompts.
4. The agent writes the finalized configuration into `THREADS_PROFILE.md`.
5. The agent uses `THREADS_PROFILE.md` as the permanent source of truth.
