# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c1-skills/20261113-175536-agent-architecture-m30-r1

**My thoughts:**

Grade should get the first reviewer. I want the feedback to provide better references to source material to help students study.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grade-reviewer.md, tutor/.claude/skills/grade/SKILL.md
- Why: To get better references to source material, a grade-reviewer now opens every pointer in the drafted feedback and flags any that names no section, lands on a page that does not teach the item's idea, or sends different ideas to the same page; the grade skill drafts in drafts/, revises at most twice, and writes review-records/NNNN-sN-grade.md.

### Round 2

**Run:** bench/runs/_live/20261120-174736-agent-architecture-m30-r1

**My thoughts:**

The review flagged multiple issues that were corrected before being send to the student- it provided better answers and links to resources. The quiz skill needs a reviewer that ensures that all of specified learning objectives are assessed, and that it is easy for a student to pass, but challenging to get all answers correct. 

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: To make sure every learning objective is assessed and the quiz is easy to pass but hard to ace, a quiz-reviewer now maps each draft item to an objective and a core idea, solves each item from its stem alone to sort it into a difficulty tier, and flags any objective or core idea left untested, basic items below 60%, or not exactly one real challenging item; the quiz skill drafts in drafts/, revises at most twice, and writes review-records/NNNN-quiz.md.

### Round 3

**Run:** bench/runs/_live/20261120-201933-agent-architecture-m30-r1

**My thoughts:**

The quiz became very challenging, but still easy to pass, which is good for stratifying students grades. The reviewer flagged questions that were too similar, and influenced MC answer choices to better test master of definitions. Now the teach skill requires a reviewer to ensure the demos function as intended and that the target time is close enough. Additionally, the teach skill should not call the quiz skill, quizes should be made independent unless the lesson plans calls for an integrated quiz.

**What Changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md, tutor/.claude/tools/lesson_check.py, tutor/.claude/settings.json
- Why: To make sure demos work as intended and the lesson's time is close to its target, a lesson-reviewer runs a measuring script (reading time per section, demo script syntax and lookups), traces the demo's controls and prompts, and reviews correctness, pedagogy, alignment and overall quality separately; the teach skill now drafts in drafts/, revises at most twice with edits, and writes lessons/ once and review-records/NNNN-teach.md.

### Round 4

**Run:** bench/runs/_live/20261120-204446-agent-architecture-m30-r1

**My thoughts:**

The lesson has better structure, but still needs the quiz skill to be removed for all lesson plans - it should remain accesible if the lesson plan calls for it. 

**What Changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/SKILL.md, tutor/.claude/skills/teach/references/LESSONS.md, tutor/.claude/skills/teach/references/lesson-template.html
- Why: So that quizzes are made independently, the teach skill no longer runs /quiz after a lesson unless the plan or the learner's request calls for a quiz with it, and the lesson's header and closing leave out quiz minutes and instead tell the learner to ask for a quiz when they want one.


## Major review

**Run:** bench/runs/c2-review/20261120-214054-agent-architecture-m30-r1

**Live tries:**

### Lesson

#### Technical correctness and facts

Rating: 5

#### Pedagogy

Rating: 5

#### Alignment with the learning goal

Rating: 5

#### Overall quality

Rating: 5

I felt that the lesson approached the topic from multiple angles to help reinforce topics covered. It is clear that the reviews assisted in identifying issues to refine the demos and toy problem questions. The lesson plan is robust.

### Quiz

#### Difficulty

Rating: 5

#### Coverage of the lesson's core

Rating: 5

#### Wording and possible misreadings

Rating: 5

#### Writing quality

Rating: 5

#### Alignment with the learning goal

Rating: 5

### Feedback

#### Useful

Rating: 5

#### Explains enough

Rating: 5

#### Personalized to how I like things explained

Rating: 3

I am not sure how to grade this - the tutor strayed from using car analogies but I think it was for the better as the lesson initiates with the auto concept and then transititions into the actual topic, which I think is valid, but I think quiz feedback could return to the analogies to help explain.

### Compared with the previous step

Token usage is up, but the created products still do not take very long and are clearly better.

### What the next step should fix

The teach agent has been improved by splitting tasks into dedicated skills and providing reviewers, but we can do better by aligning the skills with dedicated agents who perform smaller tasks and iterate before including the next more costly step along the way. There should be the following agents:
 - resource-finder: given a topic, it searches for an appropriate website link to use within the lesson
 - lesson-planner: provided a series of learning objectives, it considers the expected misconceptions and builds an outline for a complete lesson
 - lesson-writer: provided an outline of a lesson and the desired duration, it constructs a complete lesson - it calls on resource-finder and demo-dev agents
 - demo-dev: provided a specific topic and learning goal of a demo, it builds a figure or demo for the lesson
 - lesson-reviewer: has review tasks for each of the above 4 agents, it provides actionable feedback to improve the student experience

