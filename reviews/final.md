# Reviews: final

Your review of `final`: optional quick rounds, its major review, your three learning sessions, and your review of the two test topics.
Quick rounds are optional here; use one for each component that `final` adds, such as a grader subagent, so its inventory entry has its with and without.
`p3 check` ignores an optional round you leave untouched.
The major review covers all four jobs on one of the three runs of `final`, and its previous step is `c3-split`; for the quiz and the feedback, which `c3-split` did not review, compare with `c2-review`, and for the tutor with `c1-skills`.
Its live tries are your three learning sessions, all on one of your two test topics, written up under Learning sessions below, so its Live tries line points at them.
Hold the sessions on `tutor/` as you snapshotted `final`, and note what they make you want to change instead of changing it.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1 (optional)

**Run:** bench/runs/_live/20261122-180533-agent-architecture-m30-r1

**My thoughts:**

The content of the lesson had minimal impact from the reduced reviews, token usage was 4.53M, up from 3.7M. I expected it to decrease with fewer reviews. This could just be noise from a single run. Provide a reduced scope for the planner agent. I recorded thoughts on how to change it at the end of c3.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/plan/SKILL.md, tutor/.claude/agents/lesson-planner.md, tutor/.claude/agents/product-reviewer.md, tutor/.claude/agents/demo-dev.md, tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/demo/SKILL.md, tutor/.claude/skills/teach/SKILL.md
- Why: To reduce the planner's scope as the round and the end of c3-split ask, the plan skill now makes only a size-capped outline of minutes, key points and sources per section from at most three web pages, and the agents that write, review or use the plan now work from that outline.

### Round 2 (optional)

**Run:** bench/runs/_live/20261122-184436-agent-architecture-m30-r1

**My thoughts:**

token usage went down dramatically without any apparant loss in quality.

Add a guard, a PreToolUse hook in tutor/.claude/settings.json that blocks keys/ for everyone except the grade-reviewer subagent and a future subagent named grader, with its tests in tests/test_guard.py

**What changed:**

- Kind: other
- Files: tutor/.claude/hooks/keys_guard.py, tutor/.claude/settings.json, tutor/.claude/skills/quiz/SKILL.md, tests/test_guard.py
- Why: As the round asks, a PreToolUse hook now keeps keys/ from being read by everyone except the grade-reviewer and grader subagents, with its tests, while the main conversation may still create a new key so that the quiz skill, which no longer reads earlier keys, keeps working.

### Round 3 (optional)

**Run:** bench/runs/_live/20261122-191516-agent-architecture-m30-r1

**My thoughts:**

The grader sub-agent needs to be implemented as specified in guide/12-final.html

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grader.md, tutor/.claude/skills/grade/SKILL.md, tutor/.claude/agents/grade-reviewer.md
- Why: To implement the grader as the round and guide/12-final.html specify, a grader subagent now reads the key, grades and runs the grade-reviewer itself, while the grade skill only starts it, waits for its report and reads the finished grades, so neither the key nor the reviewer's report on it comes into the main conversation.

## Major review

**Run:** bench/runs/final/TODO

**Live tries:**

TODO: one line that points at your three learning sessions under Learning sessions below, and names anything else you tried with `final`.

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Quiz

#### Difficulty

Rating: TODO

TODO

#### Coverage of the lesson's core

Rating: TODO

TODO

#### Wording and possible misreadings

Rating: TODO

TODO

#### Writing quality

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

### Feedback

#### Useful

Rating: TODO

TODO

#### Explains enough

Rating: TODO

TODO

#### Personalized to how I like things explained

Rating: TODO

TODO

### Tutor

#### Guardrails

Rating: TODO

TODO

#### Personalization

Rating: TODO

TODO

### Compared with the previous step

TODO

### What I would do next

TODO

## Learning sessions

### Session 1

**Date:** TODO

**Topic:** TODO

TODO

### Session 2

**Date:** TODO

**Topic:** TODO

TODO

### Session 3

**Date:** TODO

**Topic:** TODO

TODO

## Test topics

### TODO: your first test topic's id

TODO

### TODO: your second test topic's id

TODO
