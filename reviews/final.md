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

**Run:** bench/runs/final/20261122-231530-agent-architecture-m30-r2

**Live tries:**

I did a learning session with the final model on robot kinematics. It was useful, and even created a good demo.

### Lesson

#### Technical correctness and facts

Rating: 5

#### Pedagogy

Rating: 5

#### Alignment with the learning goal

Rating: 5

#### Overall quality

Rating: 5

### Quiz

#### Difficulty

Rating: 4

#### Coverage of the lesson's core

Rating: 4

#### Wording and possible misreadings

Rating: 5

#### Writing quality

Rating: 5

#### Alignment with the learning goal

Rating: 5

### Feedback

#### Useful

Rating: 4

#### Explains enough

Rating: 4

#### Personalized to how I like things explained

Rating: 4

### Tutor

#### Guardrails

Rating: 5

#### Personalization

Rating: 4

### Compared with the previous step

The token usage is up, but the final products are more polished. I do think that if this were a real tool, the token usage to build lessons is reasonable, but the live tutor session feels too slow, likely because of the additoinal reviews taking place.

### What I would do next

I would start from an empty directory, and have each subagent do a better job of distilling their products in an attempt to reduce the token usage for the final products. I would maintain the reviewer agent/role, but would change their scope so that only one distilled output is reviewed at a time, again in attempt to reduce token usage.

## Learning sessions

### Session 1

**Date:** 23NOV2026

**Topic:** robo-kinematics

The tutor was helpful. It offers to build demos/lessons but does not just assume that it should. It asks questions to attempt to identify misconceptions. When asked to make a quick demo (viewable in a browser) it took a long time, but produced a very useful demo for the topic being discussed.

## Test topics

### robo-kinematics

The baseline contained two graphics with little value, the only links in the lesson were at the end, it did include some code which is useful.
The final system took 3x longer and consumed 5x tokens. The demo is great, and is needed for material like this. There are still a limited number of links, but I think that is likely because source reference material is not provided.
