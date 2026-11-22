---
name: plan
description: Outline a lesson before it is written - its sections, the estimated minutes of each, the key points each covers, the few sources behind them, and where a figure goes - and save it as a short plan. It writes no lesson material. Use it before writing any lesson, or when the learner asks to plan what to learn next.
argument-hint: "Which objective or topic should the next lesson cover, and how long?"
---

# Plan

You outline the next lesson for the learner in this workspace: what each section covers and how long it takes.
The outline is all you write about the lesson.
The teach skill writes the explanations, examples, practice and figures, so do not prepare those for it.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
When another skill, such as `/teach`, has you read this file instead of running it, the request is that skill's request.
A request that says what to do gets done now, without stopping to ask first.

## What to read

- `MISSION.md`, `PREFERENCES.md`, `NOTES.md`, the files in `learning-records/`, and `RESOURCES.md` if it exists.
- The file names in `lessons/`, for the next number, and the objective and headings of an earlier lesson only when this one builds on it.
- At most three web pages with WebFetch, high-trust ones, starting from those in `RESOURCES.md`; search only when you do not know of one.

Read nothing else: not `keys/`, `quizzes/`, `submissions/`, `FORMATS.md` or the teach skill's guides.
Work only inside this workspace and never write anything under `.claude/`.

## The objective and the length

- Use the objective, with its id, and the minutes the request gives; never invent a new id for an objective that has one.
- With no objective, choose the next one the learner can reach with a little help, from the mission, the notes and the records.
- With no length, use the one `PREFERENCES.md` implies, or 15 minutes.

## The plan

Write it to `plans/NNNN-<slug>.md`, with the number and slug the lesson will take, in exactly this shape and with nothing added:

```
# Plan: <lesson title>

- Objective: <id>: <its wording>
- Minutes: <requested reading minutes>
- Win: <what the learner can do by the end, in one sentence>
- Next lesson: <what did not fit, only when something did not>

## Outline

### 1. <section heading> (<objective id>, <minutes> min)
- <key point> [S1]
- Misconception: <wrong belief> -> <what is true> [S2]
- Figure: <what it shows, with any number it needs>

## Sources

- S1: <title>, <URL>
```

- **Sections:** an opening that ties to the mission, a warm-up that recalls what the learner has shown, one section per core idea, a worked example with practice, a summary, and go further.
- **Minutes:** estimated reading time, to the half minute, adding up to the requested minutes.
- **Key points:** at most four a section, each one line of at most 20 words: the point to cover, with its source and any number the lesson must get right. Take them from the pages you read, never from memory.
- **Misconceptions:** only the most likely one for a section, as one of its key points, with no id; add "(shown)" when the notes or records say this learner holds it.
- **Figures:** a `Figure:` line only in a section where a picture beats words.
- **Size:** at most 250 words plus 15 for each requested minute, so about 700 for a 30-minute lesson. Cut detail to fit, never a core idea.
- **Not in the plan:** explanations, lists of facts, examples worked out, questions, answers, word budgets, tables, or notes about your choices.

Add each new source to `RESOURCES.md` under `## Knowledge`, as `- [<title>](<URL>)` with one line below it on what it covers, ending `Use for: <when to reach for it>.`

## Finish

When another skill ran you, return to it with the plan's path.
When the learner asked for the plan, end with a short message: the plan's path, the objectives it covers, and that they can ask for the lesson whenever they are ready.

## Check before you finish

- The minutes add up, every core idea has a section, and every key point that states a fact names a source you read.
- The plan has only the parts shown above and is within its size.
