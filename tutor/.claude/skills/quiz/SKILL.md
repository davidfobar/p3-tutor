---
name: quiz
description: Write a quiz and its answer key for the learner in this workspace, using only multiple-choice items and small problems with one checkable numeric answer, never free-text items; also give a quiz in the chat and collect the learner's answers. Use it whenever the learner asks for a quiz or to be tested.
argument-hint: "What should the quiz cover, and how many questions?"
---

# Quiz

You write quizzes and their answer keys for the learner in this workspace.
A quiz is retrieval practice that also shows you and the learner where they stand.
Each item tests one thing that matters for the objective, at the learner's level, with exactly one answer that a script can check without judgment.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
A request that says what to do gets done now, without stopping to ask first.
Put any question you have for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## The rule this skill exists for

Every item is either `mcq` or `numeric`. **Never write a `short` item**, even though `FORMATS.md` allows the type.
The learner does not want free-text answers judged by a model: every answer must be one an exact comparison can check, an option id or a number.

When an idea seems to call for a written answer ("explain why", "name one thing", "is the teammate right?"), turn it into one of these instead:

- an `mcq` whose options are the plausible explanations, judgments or names, with the wrong ones built on real misconceptions;
- a `numeric` problem: a small concrete case where applying the idea produces a count, a quantity or a result the learner computes.

## Read first

Read `FORMATS.md` (the exact shape of `quizzes/NNNN.json` and `keys/NNNN.json`), `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/`.
Then read the lessons on the objective in `lessons/`, and the earlier quizzes and grades for the misconceptions this learner has shown and their ids. Never read, list or search `keys/`: a guard blocks it.
Use Read, Glob and Grep to look around, Write to create files and the Agent tool for the review loop; work only inside this workspace and never write anything under `.claude/`.

## Steps

1. **Pin down the quiz:** the objective or objectives it covers and their ids, as the next section says, and the number of items asked for (five when none is given).
   Reuse an objective id the workspace already has for the same objective, and never invent a new id for something that has one.
2. **Find each objective's core:** the handful of ideas a learner must get right to have met it, from its lessons or, when there are none, from a high-trust source you search for and read.
   Cover the core first, and skip trivia and phrasing a lesson happened to use.
   When the objective has not been taught yet, write the quiz as a check of the objective itself, at the level its wording states, and say in your message that the quiz is ahead of the lessons.
3. **Write the items**, as the sections below describe, and give each one the id of the objective it serves.
4. **Check it** (below), and rewrite any item that fails.
5. **Write the first draft**, with NNNN the next free number in `quizzes/`: the quiz to `drafts/NNNN-quiz-v1.json` and its key to `drafts/NNNN-key-v1.json`, in exactly the shapes `FORMATS.md` shows for `quizzes/NNNN.json` and `keys/NNNN.json`.
6. **Run the review loop** (below).
7. **Write the final files once**, with the Write tool, copying the last draft's content: the quiz to `quizzes/NNNN.json` and its key to `keys/NNNN.json`; never copy them with a shell command, and never read or edit them again after writing them.
   Never change an existing quiz or key; a quiz that needs fixing becomes a new quiz.
8. **Finish** with a short message: the quiz's path, what it covers and how many items it has, and never any answer.

## The review loop

Your draft is read by the `quiz-reviewer` subagent, a fresh reader with a checklist, before the learner sees it; it checks above all that every objective and its core are assessed, and that a learner with the basics passes while only one who has mastered the objective gets every item right.

- **Drafts go in `drafts/`, never in `quizzes/` or `keys/`.** Each pass that revises writes a new pair, `-v2.json`, `-v3.json`.
- **Start a pass** with the Agent tool, `subagent_type` `quiz-reviewer`, and a task message that gives the learner's request (the objective or objectives with their ids and wording, and the number of items) and the paths of the draft quiz and draft key, and, from the second pass on, lists the previous pass's findings to confirm.
  Do not hand it your tier labels, your list of core ideas or your reasoning: it judges coverage and difficulty itself, the way the learner will meet the quiz.
- **Wait for the reviewer's report** before you revise or finish; never end the session while a review is running.
- **Revise:** fix every finding in a new draft, then run "Check before you finish" on it again. You may decline a finding only when you are sure it is wrong, and then say why in the record.
- **The cap is two passes.** Stop as soon as a report says `FINDINGS: 0`. After the second report, fix what it found in one last draft without reviewing again.
- **Write the record** `review-records/NNNN-quiz.md`: how many passes ran, the reviewer's core list and tier for each item in the last pass, each pass's findings in one line each (check number, item, what), what you changed for each, and any finding you declined with why. Never put an answer in the record.

## One objective or several

- **The request names one objective** (by id or by its wording): every item serves that objective, and the quiz's `objective` is its id.
- **The request names no single objective** (such as "quiz me", "test me on what we've done", or a review quiz): span at least three objectives, and all of them when the number of items allows.
  - Take the objectives and their ids from `MISSION.md`, `NOTES.md`, the learning records, the lessons and earlier quizzes.
  - Choose first the objectives the learner has studied, in lessons, learning records or earlier quizzes; add an objective they have not studied only to reach three, at the level its wording states, and say in your message which objective is ahead of the lessons.
  - Give each chosen objective at least one item, and spread the rest so no objective has more than half the quiz.
  - The three tiers below apply to the quiz as a whole: put the basic items across the objectives, and choose the challenging item from an objective the learner has studied.
  - The quiz's `objective` is the id of the objective with the most items; when two tie, the one the learner studied most recently.
- **The request names two objectives:** cover both, and add a third the learner has studied when the number of items allows.

## Choosing item types

- `mcq` when the wrong answers are predictable: each distractor is a misconception or a typical error, so a wrong pick tells you something.
  It suits both kinds of item below: recognizing a definition or a basic fact, and applying the idea to a concrete case (which design fits, what happens next, which change fixes it).
- `numeric` for a simple problem: a short scenario with every number given, where using the idea correctly leads to one number, such as a count of steps, calls or items, a total, a ratio or a time.
  Keep the arithmetic easy; the item tests the idea, not the calculation.
  Prefer whole-number answers, and say the unit in the stem and in `unit`, and the precision you expect when the answer is not whole.
- Include at least one `numeric` item when the objective allows a quantity; otherwise all items are `mcq`.

## Difficulty

A learner who has the basics should pass, and only a learner who can also handle one hard question should get every item right.
Plan the quiz in three tiers before you write any item:

- **Basic:** enough items that getting only these right is a pass, at least 60% of the quiz rounded up (3 of 4 or 5, 4 of 6, 5 of 7 or 8).
  Each checks one piece of the objective's core directly: what a term means, which example matches a definition, a basic fact or a one-step use of a rule.
  A learner who read the lesson and remembers its core gets these right without a long chain of reasoning, and no distractor in them is a trap that only an expert would avoid.
- **Challenging:** exactly one item, the only one that should separate a learner who has mastered the objective from one who has the basics.
  It asks them to apply the idea in a less familiar case, to combine two parts of the core, or to tell apart two close ideas, and it still needs only what they were taught.
- **Moderate:** every remaining item, if there are any: applying one idea to a concrete case that resembles what the lesson showed.
  These should be within reach of a learner with the basics who thinks carefully; do not let any of them become a second challenging item.

Mix the order, but do not open the quiz with the challenging item.
No item should need knowledge the learner was never given, and no basic item should be made hard by its wording instead of its idea.

## Writing stems

- One question per item, complete on its own: a learner who knows the idea can answer it without the lesson open.
- Plain, exact wording, with no double negatives, no "all of the above" or "none of the above", and no trick wording.
- When the stem asks for the "best" or "most" of something, say best for what.
- Give every number, unit and condition the answer depends on, and for a `numeric` item, say exactly what to count, so two careful readers count the same things.
- Make sure no item gives away another item's answer, and none repeats a practice question from a lesson.
- Use examples the learner relates to, as `PREFERENCES.md` says, when they fit the objective without distorting it.

## Writing options (`mcq`)

- Three to five options, usually four, with ids `a`, `b`, `c`, `d`.
- Every option plausible to someone holding the misconception it encodes; no joke options.
- All options about the same length, with the same grammar and level of detail, so the right one never stands out.
- Vary which position holds the correct answer across items, and give nothing away by formatting or order.
- Exactly one option is correct; check that no distractor is also defensible.

## Writing the key

- `answer`: the option id for `mcq`, or a JSON number in the item's unit for `numeric`.
- `tolerance`: for every `numeric` item, the absolute tolerance its precision implies: 0 for a count, 0.5 for an answer rounded to a whole number, 0.05 for one decimal place.
- `rationale`: why the answer is right, in one or two sentences, and what a typical wrong answer shows; for a `numeric` item, show the working in one line.
- `distractors`: each wrong option that encodes a misconception, mapped to that misconception's id; reuse the ids the workspace already has.
- No `accepted` field, since there are no `short` items.

## Check before you finish

- Confirm that no item in the quiz has `"type": "short"`; rewrite any that does as `mcq` or `numeric`.
- Label each item basic, moderate or challenging for yourself, and confirm the counts: the basic items alone reach 60% of the quiz, and exactly one item is challenging.
  If a basic item turned out to need several steps of reasoning, simplify it; if a second item turned out as hard as the challenging one, make it easier.
- Answer every item yourself from its stem alone, without looking at your key, and compare.
  Rewrite any item where you hesitate, where a careful expert could argue for a second option, or where a `numeric` item could reasonably be counted two ways.
- Check that every item serves one of the quiz's objectives and carries that objective's id, and, when the request named no single objective, that at least three objectives have an item; then check that the quiz file holds no answers, and that the key has the same item ids in the same order.

## Giving a quiz in the chat

When the learner wants to take a quiz in a live session, show its title and each item's stem, options and unit, and never anything from `keys/`.
Collect their answers, write them exactly as given to the next `submissions/sN.json` as `FORMATS.md` shows, and then have it graded: use the `/grade` skill when this workspace has one, and the `/teach` skill's grade job otherwise.

---

Adapted from the shipped teach skill's `references/QUIZZES.md`, itself adapted from the `teach` skill in mattpocock/skills (MIT License, copyright (c) 2026 Matt Pocock); the full notice is in `THIRD-PARTY.md` at the root of the template repo.
