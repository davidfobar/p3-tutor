---
name: grade
description: Grade the learner's answers to a quiz in this workspace by handing them to the grader subagent - a verdict, a misconception id and feedback for every item, with each piece of feedback pointing the learner to the exact place in their lessons or sources where the idea is taught - then record what the grades show. Use it whenever the learner asks for a submission or a set of answers to be graded or marked.
argument-hint: "Which submission or answers should I grade?"
---

# Grade

You get the learner's answers graded and tell them the result.
You do not grade: the answer key is closed to this conversation, so the `grader` subagent reads it, grades, has the grades reviewed and writes every file.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
A request that says what to do gets done now, without stopping to ask first.
Put any question you have for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## Steps

1. **Find the submission.** Use the one the request names, or the newest in `submissions/` that has no file in `grades/` (use Glob).
   When the learner gave a complete set of answers in the chat instead, write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows; never complete or correct an answer.
   With no answers to grade, say so, and stop.
2. **Start the grader** with the Agent tool, `subagent_type` `grader`, and a task message that gives only the submission's path, the quiz's number and the learner's request in their own words.
   Do not read ahead for it: it reads the quiz, the key, the learner's files and the teaching material itself.
   For several submissions, start one grader at a time.
3. **Wait for its report** before you go on; never end the session while it is running, and write nothing meanwhile.
4. **Read the grades file** it names.
5. **Finish in the chat**, in the style `PREFERENCES.md` asks for: each item's verdict, the summary, and the next step with where to reread.
   Take it all from the grades file; add no answer, verdict or explanation of your own.

## What stays out of this conversation

- Never read, list or search `keys/`, and never ask a subagent what a key says.
- Never start `grade-reviewer` yourself: its report discusses the key, so only the grader starts it.
- Never grade, or change a grades file, yourself.
  When the grader cannot be started, reports that it did not grade, or leaves no grades file, start it once more if the cause looks temporary; otherwise tell the learner plainly that the answers are not graded yet, and why.

---

Adapted from the shipped teach skill's `references/GRADING.md`, itself adapted from the `teach` skill in mattpocock/skills (MIT License, copyright (c) 2026 Matt Pocock); the full notice is in `THIRD-PARTY.md` at the root of the template repo.
