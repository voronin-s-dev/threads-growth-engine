# 🧐 Reader Proxy and Audience Critic Standard

> **Purpose:** Ruthless Phase 2 evaluation simulating an impatient mobile feed reader.

---

## 1. The Reader Persona

1. The simulated reader scrolls social feeds on a smartphone.
2. The reader maintains an initial attention span of 1.5 seconds.
3. The reader ignores academic lectures and abstract generalities.
4. The reader values personal relevance, clarity, and authentic voice.
5. The reader evaluates posts without prior knowledge of author frameworks.

---

## 2. Four Evaluation Axes

### Axis 1: Thumb-Stop Hook (Target: >= 8/10)
1. The opening sentence must stop the scroll immediately.
2. The opening line introduces an acute tension or recognizable scene.
3. The agent rejects rhetorical questions and generic topic labels.

### Axis 2: Tone and Preachiness Detector (Target: Zero Preaching)
1. The author writes as an equal peer.
2. The text eliminates condescending and didactic phrasing.
3. The author avoids imperative commands like 'do this' or 'stop that'.
4. The text avoids synthetic corporate or influencer cliches.

### Axis 3: Occam Brevity Cut (Target: 20% to 30% Text Reduction)
1. The agent identifies sentences that explain obvious conclusions.
2. The agent marks all redundant adjectives for deletion.
3. The draft must deliver identical impact with fewer total words.
4. The agent provides a trimmed draft version in the audit.

### Axis 4: Discussion Trigger (Target: High Reply Potential)
1. The ending line leaves open room for reader opinions.
2. The text avoids closed or self-satisfied conclusions.
3. The reader feels a natural urge to share personal experience.
4. The author avoids artificial survey questions.

---

## 3. Standard Audit Output Structure

The agent outputs the review in three distinct sections:

```markdown
### Phase 1: Technical & Anti-Slop Audit
- lint_threads.py status: [PASS / FAIL]
- Post character limits: [PASS / FAIL]

### Phase 2: Reader Proxy Verdict
- Thumb-Stop Hook: [Score / 10] — [Short verdict]
- Tone & Preachiness: [Score / 10] — [Short verdict]
- Brevity & Density: [Score / 10] — [Short verdict]
- Reply Trigger: [Score / 10] — [Short verdict]
- Reader Brutal Reaction: [1-2 sentences of raw reader impression]

### Actionable Cuts & Line Edits
- Removable lines: [List exact lines to delete]
- Recommended rewrite: [Trimmed version]
```
