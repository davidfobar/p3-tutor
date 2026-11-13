---
name: plan
description: Prepare a lesson before it is written - pin down the learning objectives it covers, gather and digest the material for them from the workspace and high-trust sources, list the common misconceptions, find the threads that link it to earlier lessons, and draft questions that reveal those misconceptions - and save it all as a lesson plan. It writes no lesson material itself. Use it before writing any lesson, or when the learner asks to plan what to learn next.
argument-hint: "Which objective or topic should the next lesson cover, and how long?"
---

# Plan

You prepare the next lesson for the learner in this workspace.
Your output is a lesson plan, the preparation a teacher does before writing: what the lesson must cover, what the material says, what the learner is likely to get wrong, how it connects to what they already learned, and how to find out what they misunderstand.
You do not write the lesson, its prose, its HTML, its figures or its quiz; the teach skill does that from your plan.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
When another skill, such as `/teach`, has you read this file instead of running it, the request is that skill's request.
A request that says what to do gets done now, without stopping to ask first.

## Read first

Read `FORMATS.md`, `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/`.
Then read the titles and objectives (the `p3-objective` meta tag) of every lesson in `lessons/`, and what exists of `cheatsheets/`, `RESOURCES.md`, `GLOSSARY.md`, and the earlier quizzes, keys and grades.
Use Read, Glob and Grep to look around, WebSearch and WebFetch for sources, and Write to create files; work only inside this workspace and never write anything under `.claude/`.

## Steps

### 1. The objectives

- Name the objective or objectives the lesson covers, with their ids and their wording as the request or the workspace states them; reuse an id the workspace already has, and never invent a new id for something that has one.
- When the request names no objective, choose the most relevant next one from the mission, `NOTES.md` and the learning records: one the learner can reach with a little help, that builds only on what they have shown.
- Break each objective into its core: the handful of ideas a learner must get right to have met it.
- Note the requested length in minutes, or the one `PREFERENCES.md` implies, or 15 when neither says.
- Note where the learner starts: what the records and `NOTES.md` say they already know that the objective needs, and what it needs that they have not shown.

### 2. The material

- Start from what the workspace already has on these objectives: earlier lessons, cheat sheets and the sources in `RESOURCES.md`.
- Search the web for high-trust sources on exactly these objectives (official documentation, textbooks, papers, recognised experts), read the best two or three, and choose the single best one as the lesson's primary source.
  Never rely on your own memory for a fact the lesson will teach.
- For each core idea, write the key facts in a sentence or two each, in your own words, with the source and the section they come from, so the teach skill can cite them without searching again.
- Note any worked example, figure or number in a source that the lesson could adapt, with where it is.
- Add the sources to `RESOURCES.md` in the format in `.claude/skills/teach/references/RESOURCES-FORMAT.md`.

### 3. The misconceptions

- List the common misconceptions for these objectives: first those the workspace already records (the keys' `distractors` and rationales, the grades, `NOTES.md`, the learning records), then those the sources or teachers of this topic commonly warn about.
- For each one: its id (the workspace's id when it has one, otherwise the next free `M` number), the wrong belief in one sentence, why it is tempting, and the fact that corrects it, with its source.
- Mark the ones this learner has actually shown, and with what evidence (for example "grades 0001-s1, q2").

### 4. The threads to earlier lessons

- Read the earlier lessons that touch these objectives or the ideas they build on.
- List the threads the new lesson can pick up: a running example, an analogy, a term, a figure or a scenario an earlier lesson used, with the lesson file and section, and how the new idea extends it.
- Name the one or two earlier ideas worth a quick retrieval question at the start of the lesson, because the new material rests on them.
- When there are no earlier lessons, say so, and list instead what the learner's records and mission give to build on.

### 5. The diagnostic questions

- For each misconception, write one or two questions that would reveal it: questions a learner holding the misconception would answer in a recognisably wrong way.
- For each question: the misconception it targets, the right answer in a few words, and what the typical wrong answer looks like.
- These are for the lesson's practice and checks; they are not a quiz, and the teach skill keeps its quiz items different from them.

### 6. Write the plan

Write it to `plans/NNNN-<slug>.md`, where `NNNN` and the slug are those the lesson will take: the next number in `lessons/` and a slug for its objective.
Use these headings, in this order: `# Plan: <lesson title>`, `## Objectives`, `## Where the learner starts`, `## Material`, `## Misconceptions`, `## Threads to earlier lessons`, `## Diagnostic questions`, `## Sources`.
Keep it to notes and short sentences, not lesson prose; it is for the teacher, not the learner.

## Finish

When another skill ran you, return to it with the plan's path.
When the learner asked for the plan, end with a short message: the plan's path, the objectives it covers, and that they can ask for the lesson whenever they are ready.

## Check before you finish

- Every fact in `## Material` names its source and section, and every source is one you actually read.
- Every misconception has an id, a correcting fact and at least one diagnostic question.
- The plan holds no lesson prose, HTML or quiz items.
