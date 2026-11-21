---
name: grade
description: Grade the learner's answers to a quiz in this workspace - a verdict, a misconception id and feedback for every item, with each piece of feedback pointing the learner to the exact place in their lessons or sources where the idea is taught - then record what the grades show. Use it whenever the learner asks for a submission or a set of answers to be graded or marked.
argument-hint: "Which submission or answers should I grade?"
---

# Grade

You grade the learner's answers to a quiz in this workspace.
Grading gives the learner a verdict on each answer and feedback that helps them learn, and every piece of feedback sends them back to the teaching material where the idea lives, so they can reread it and fix their own understanding.
It is also your best evidence of what they know, so it feeds the learning records.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
When the learner gives a complete set of answers in the chat instead of a submission file, write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows, and grade that.
A request that says what to do gets done now, without stopping to ask first.
Put any question you have for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## Read first

Read `FORMATS.md` (the exact shape of `grades/NNNN-sN.json`), `PREFERENCES.md` (how this learner likes feedback), `MISSION.md`, `NOTES.md` and every file in `learning-records/`.
Then read the quiz, its key and the submission.
Use Read, Glob and Grep to look around, Write to create files and the Agent tool for the review loop; work only inside this workspace and never write anything under `.claude/`.

## Find the teaching material first

Before you grade, build a short map from each item to the place where its idea is taught, because every item's feedback will point there.
Look, in this order, and use the first that covers the idea:

1. **Lessons** in `lessons/` on the quiz's objectives (their `p3-objective` meta tag says which): note the file and the heading of the section that teaches the idea, exactly as the heading reads.
2. **Cheat sheets** in `cheatsheets/`: the file and the heading or entry.
3. **Sources** in `RESOURCES.md`, and any source a lesson cites: the title, the URL, and the section or heading when the source has one.
4. **A new source**, only when none of the above covers an item's idea: search the web once for the uncovered ideas together, read the best high-trust source, and note its title, URL and the section that covers each idea.
   Add it to `RESOURCES.md` in the format in `.claude/skills/teach/references/RESOURCES-FORMAT.md`.

Never point to a file, heading or section you have not seen, and never make up a URL.
If nothing covers an item even after the search, say so in the summary instead of inventing a pointer.

## Verdicts

- Judge what the response means, not how it is worded: it is `correct` when it means what the key's answer means, even if it is oddly worded, misspelled, or reached by a valid route the key did not expect.
- The key's `accepted` list gives examples of correct wordings, not the only ones.
- It is `partial` when part of it is right: the right method with an arithmetic slip or the wrong unit, one half of a two-part idea, or the right answer with a stated reason that is wrong.
- It is `wrong` when it misses the idea, contradicts it, or is blank.
- For `mcq`, compare the option the learner chose with the key; if they wrote out an option's text instead of its id, match it to its option.
- For `numeric`, the number is right when it is within the key's tolerance (1% of the answer when the key gives none), after converting any unit the learner stated; a reason the learner gives with it is still judged by the rules above.
- If you are sure the key itself is wrong, grade against what is actually correct, and say so in the summary.

## Misconceptions

- Name a misconception id when the response shows that misconception: for `mcq`, the key's `distractors` entry for the chosen option; for other items, the misconception the learner's answer or reasoning shows, from the ids the workspace already uses (the keys' distractors and rationales, `NOTES.md`, the learning records).
- Use `null` for a correct response, a slip, a blank, or a wrong answer that shows no known misconception, and never invent an id.

## Feedback

Write each item's feedback to the learner, in the style `PREFERENCES.md` asks for: direct, specific, and saying exactly where the answer went wrong and why.

- **Correct:** say so, and add the one insight that makes it stick or links it to the next idea; for an unusual route, say why it works.
- **Partial:** say what was right, exactly what was off, and how to fix it.
- **Wrong:** name exactly where the answer went wrong and the right idea, with why it holds, in plain words; when a misconception is behind it, name the wrong belief plainly and say why it is tempting, without blame.
  Point at the first mistake and the idea behind it rather than walking through a full worked solution, so the learner can fix the rest from the material.
- **The pointer:** end every item's feedback with one sentence that sends the learner to the material from your map, naming the place precisely enough to find it in seconds, such as: `Reread "Who runs the tool" in lessons/0003-tool-calling.html.` or `See the "Stopping conditions" section of <source title> (<URL>).`
  For a wrong or partial answer, say what to look for when they reread it; for a correct one, offer it as where to go deeper.
  Leave the pointer out only when your map has nothing for that item.
- Keep each item's feedback to two to four sentences plus the pointer, unless the learner wants more.
- The `summary` says what the learner has down, the one thing to work on next, and a concrete next step that names the section or sections to reread before trying again.

## The review loop

Your draft is read by the `grade-reviewer` subagent, a fresh reader with a checklist, before the learner sees it; it checks above all that every pointer sends the learner to a specific place that really teaches the idea.

- **Drafts go in `drafts/`, never in `grades/`.** Name them `drafts/NNNN-sN-grades-v1.json`, `-v2.json` and so on, in the same JSON shape as the final file.
- **Start a pass** with the Agent tool, `subagent_type` `grade-reviewer`, and a task message that names the draft's path, the quiz's, the key's and the submission's, and, from the second pass on, lists the previous pass's findings to confirm.
  Do not hand it your map, your reasoning or what you meant: it reads the draft the way the learner will.
- **Wait for the reviewer's report** before you revise or finish; never end the session while a review is running.
- **Revise:** fix every finding in a new draft. Before you use a title, URL or heading the reviewer gives you, check it yourself if it is not in your map. You may decline a finding only when you are sure it is wrong, and then say why in the record.
- **The cap is two passes.** Stop as soon as a report says `FINDINGS: 0`. After the second report, fix what it found in one last draft without reviewing again.
- **Then write the final file once** with the Write tool to `grades/NNNN-sN.json`, copying the last draft's content; never copy it with a shell command.
- **Write the record** `review-records/NNNN-sN-grade.md`: how many passes ran, each pass's findings in one line each (check number, item, what), what you changed for each, and any finding you declined with why.

## Steps

1. Read what the section "Read first" lists, and build the map of teaching material.
2. Grade every item, including unanswered ones: a verdict, the misconception if the response shows one, and feedback with its pointer.
3. Write the first draft, `drafts/NNNN-sN-grades-v1.json`, exactly as `FORMATS.md` shows for a grades file.
4. Run the review loop above, and when it ends write `grades/NNNN-sN.json`, named after the quiz and the submission, and the loop's record.
5. Write a learning record when the grades are evidence: real understanding of something non-trivial, or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`.
6. Update `NOTES.md` with what the learner knows and does not yet know.
7. Finish in the chat with the summary and the next step, including where to reread; write every file before this message, never after it.

## Check before you finish

- The grades file has one entry per quiz item, with the same ids in the same order, and no feedback is empty.
- Every item whose idea your map covers ends with a pointer, and every pointer names a file, heading, title or URL you or the reviewer actually saw.
- No feedback is vague ("you're close", "check your work"): each one says what was right or wrong and why.
- `grades/` holds only the final file, and the record is in `review-records/`.

---

Adapted from the shipped teach skill's `references/GRADING.md`, itself adapted from the `teach` skill in mattpocock/skills (MIT License, copyright (c) 2026 Matt Pocock); the full notice is in `THIRD-PARTY.md` at the root of the template repo.
