# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261113-155118-agent-architecture-m30-r1

**My thoughts:**

When reviewing the latest produced quiz, I noticed that two questions are short answer - I only want multiple choice questions or simple problems with verifiable answers, I do not want an agent grading a short answer question. 

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md, tutor/CLAUDE.md
- Why: Quizzes were still written by /teach, whose guide encourages `short` items (q4 and q6 in this run); a quiz skill of its own allows only `mcq` items and `numeric` problems with a checkable answer and turns any would-be written answer into one of those, as these thoughts ask, and tutor/CLAUDE.md now sends quiz requests to it.

### Round 2

**Run:** bench/runs/_live/20261113-163907-agent-architecture-m30-r1

**My thoughts:**

Students should be able to get a passing grade from showcasing basic knowledge (such as simple definition questions), it should be challenging for a student to get 100%, but only because one of the questions is challenging. 

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: The quiz skill aimed mostly at apply-level items with one or two stretch items; it now plans three tiers, enough basic definition-and-fact items that they alone are a pass (at least 60%), exactly one challenging item, and moderate items for the rest, as these thoughts ask.

### Round 3

**Run:** bench/runs/_live/20261113-164333-agent-architecture-m30-r1

**My thoughts:**

The quiz should span at least 3 learning objectives - all if possible.  

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: The quiz skill kept every item on one objective; it now spans at least three objectives, and all of them when the number of items allows, whenever a request names no single objective, as these thoughts ask, while a request that names one objective (as the bench's does) still gets a quiz on that objective only.

### Round 4

**Run:** bench/runs/_live/20261113-155118-agent-architecture-m30-r1

**My thoughts:**

The grade skill should be a standalone skill and provide better feedback to the learner in the form of referencing them to the source material that the information can be found in. Feedback should encourage referencing teaching material whenever possible.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md, tutor/CLAUDE.md
- Why: Grading still ran inside /teach, whose feedback never pointed back to the material (its s1 feedback in Round 1's run, bench/runs/_live/20261113-155118-agent-architecture-m30-r1, names no lesson or source); a grade skill of its own first maps each item to the lesson section, cheat sheet or source that teaches it and ends every item's feedback and the summary with a precise pointer to reread, as these thoughts ask, and tutor/CLAUDE.md now sends grade requests to it.

### Round 5

**Run:** bench/runs/_live/20261113-170710-agent-architecture-m30-r1

**My thoughts:**

The tutor should be a standalone skill and does not need to deny the request about helping on the quiz - rather, the tutor should simply restate the learning objectives covered by the quiz, and refer the students back to the source learning material. If the question is not related to the quiz, then the tutor can address it directly.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md, tutor/CLAUDE.md
- Why: Tutoring still ran inside /teach, which met quiz questions with a refusal and option-by-option coaching (tutor-p01 and tutor-p02 in this run); a tutor skill of its own answers a question about an ungraded quiz by restating the objectives the quiz covers and pointing to the lesson section or source for each, without a refusal or the answer, and answers any other question directly, as these thoughts ask, and tutor/CLAUDE.md now sends chat questions to it.

### Round 6

**Run:** bench/runs/_live/20261113-171826-agent-architecture-m30-r1

**My thoughts:**

The teach skill should leverage a seperate independent plan skill. The plan skill should identify what learning objectives are to be covered, parse the course material specific to those objectives and identify common misoncetpions for the topic. The plan skill should also review previous lessons to understand where consistent threads can be used to link previous material to new material for the students. The plan skill should also identify questions that can help assess student misconceptions. None of this is the actual development of the lesson material, just the preperation stage.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/plan/SKILL.md, tutor/.claude/skills/teach/SKILL.md
- Why: /teach pinned down the objective and searched for sources inside the same pass that wrote the lesson; a plan skill of its own now prepares each lesson first (the objectives and their core, the material digested with its sources, the common misconceptions, the threads to earlier lessons, and diagnostic questions for each misconception) and saves it to plans/ without writing any lesson material, as these thoughts ask, and /teach now runs it first and builds the lesson from the plan.

### Round 7

**Run:** bench/runs/_live/20261113-172705-agent-architecture-m30-r1

**My thoughts:**

Following the plan skill, a demo skill should be executed that builds a demo that should be used within the actual lesson. The demo should either be a interactive graphic, or a series of commands/code that the learner should implement to get hands on experience with the material.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/demo/SKILL.md, tutor/.claude/skills/teach/SKILL.md
- Why: /teach went from the plan straight to writing the lesson, with no step that built something hands-on; a demo skill of its own now runs after the plan and builds one demo from it, either an interactive graphic or a series of commands or code the learner runs, as a fragment saved to demos/, as these thoughts ask, and /teach now runs it after the plan and embeds the demo in the lesson where its idea is introduced.

### Round 8

**Run:** bench/runs/_live/20261113-173658-agent-architecture-m30-r1

**My thoughts:**

The demo integration was good - to be clear, it should be focused on the most likely to be a misconception. Now the teach skill needs to be refreshed - remove items related to other direct skill (demo, grade, plan, quiz, tutor) since they are now standalone skills. Each header should include a label of which learning objective the section is focused on. hyperlinks to reference material should be used as much as possible. Provide estimated times for quizes and demos so that they combine with the estimated time for reading as well.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/SKILL.md, tutor/.claude/skills/teach/references/LESSONS.md, tutor/.claude/skills/teach/references/lesson-template.html, tutor/.claude/skills/teach/references/QUIZZES.md (removed), tutor/.claude/skills/teach/references/GRADING.md (removed), tutor/.claude/skills/teach/references/TUTORING.md (removed)
- Why: /teach still carried the quiz, grade and tutor jobs and their guides, and its lessons had no objective labels or time beyond reading; teach is rewritten to write lessons only, running /plan, /demo and then /quiz for the lesson's quiz, with every section heading labeled by its objective, every fact linked to its source, and the header showing reading, demo and quiz minutes and their total, as these thoughts ask (focusing the demo on the likeliest misconception is left for a later round).

## Major review

**Run:** bench/runs/c1-skills/20261113-175536-agent-architecture-m30-r1

**Live tries:**

While using the tutor, I was provided a quiz that was meant to expose my misunderstandings. For the questions that I got wrong, I was provided links to resources to help clarify and spend more time on. The tutor then asked clarifying questions in order to prepare the demo/lesson. I was able to see the teach plan call on both of my plan and demo skills as it prepared the content for me. Overall, the experince was fine, aside from the response time between interactions. I think to make this a realistic tool, less content needs to be generated by the agent at runtime. The generated lesson and demo were ok, I would have preferred to see more hyperlinks to reference material.

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

Rating: 4

I asked it to relate to cars when possible, that caused everything to be described in terms of cars, which is too much.

### Compared with the previous step

The current lessons are better in that they provide links and an actionable demo. I feel like the lesson is more organized, hopefully due to the plan skill. However, lesson planning took a very long time. I think the tutor performed as expected, but provided too many references to cars - there needs to be a balance.

### What the next step should fix

Try to reduce the learner wait time, and reduce the amount of car references to the learner.
