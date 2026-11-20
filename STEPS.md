# P3: what to do, in order

**Due:** Tue Nov 24, 11:59 pm. **Section:** 598E (so the length study is required).
**Status on Fri Nov 13:** setup and the baseline runs are done. **Your next step is Step 3 (preferences).**
**Check your position at any time:** run `uv run p3 next`. Its stage numbers match the step numbers below. Ignore its `Read: guide/...` line, because that site was deleted.

## The project in one paragraph

You start from a working tutor and improve it in four fixed versions:
**c1** (four skills) → **c2** (+ reviewer subagents) → **c3** (+ the lesson job split across subagents) → **final** (what was worth keeping, plus a guard).
After each version you measure two things: did it get better (your written review plus automatic scores), and what did it cost (tokens and time)?
The tutor itself isn't graded. Your evidence about which additions were worth their cost is.

## Who does what

- **You** write every review, rating, `PREFERENCES.md`, `EVAL.md`, `PREREG.md`, both test topics, and make every blind pick. These are graded as *your* judgment, so an AI must not write them.
- **The Builder** (plain `claude` in this folder) edits the tutor files under `tutor/` and records what it changed. You can ignore the "Guide" agent; this file replaces it.
- **A plain terminal** (no Claude running in it) runs full bench runs. They take 6 to 60+ minutes and must not die when a Claude window closes.

## The loop you repeat in Steps 4, 5 and 7

This is the core of the project, so here it is once:

1. **Run the tutor as it currently stands:** `uv run p3 bench --config live --quick` (5 sessions), or `--only teach` (1 session) when you're only changing one job. Output lands in `bench/runs/_live/`.
2. **Read what it made.** In `reviews/<step>.md`, under the next Round, fill in **Run:** (the run folder) and **My thoughts:** (did the last change help? what's good, what's bad, what should change? quote it).
3. **Tell the Builder:** `Act on Round N of reviews/<step>.md`. It makes **one** change and fills in "What changed".
4. Repeat. To add a round, copy the last one with its `TODO` lines.

**Why one change per round:** the run before a round is "without the component" and the run after is "with it". That's the evidence the inventory and graders ask for.

When the step is done, finish it like this (same every time):

- **Snapshot** it: `uv run p3 snapshot <step>`. This freezes the version. Never overwrite a snapshot that already has runs.
- **Full run** in a plain terminal: `uv run p3 bench --config <step>`.
- **Major review** in `reviews/<step>.md`: rate every criterion 1 to 5, each with evidence (quotes, item ids like `q3`, probe ids like `p04`).
- **EVAL.md section:** paste the tables from `uv run p3 report --configs <previous>,<step>`, then write what the step gained and what it cost.
- **Inventory:** tell the Builder to "add entries to reviews/components.md for the new components". You then write each one's **Purpose** and **Review**.
- **Commit and push** `configs/`, `bench/runs/`, `reviews/`, `EVAL.md`.

**How reviews are graded (30 pts, the biggest single part):** specific evidence; ratings your text justifies; feedback someone could act on ("q2 never says *better for what*", not "could be clearer"); and a visible trail from review → change → whether it helped. A change that made things worse is a fine result if the trail shows it.

---

## Steps

### ☑ 1. Setup · ☑ 2. Baseline: done

### ☑ 3. Write `tutor/PREFERENCES.md` (≈30 min)
**Do:** replace the default text under each of the 5 headings with how *you* actually like to learn: explanations, examples you relate to, length and density, feedback style, tone. Commit.
**Why:** the tutor reads this before every job. It's what makes the lessons yours, and your reviews and blind picks judge the tutor against it.

### ☐ 4. Step 1: `c1-skills`, four skills (≥4 rounds)
**Do:** use the loop above. One round per skill: write `tutor/.claude/skills/{teach,tutor,quiz,grade}/SKILL.md` (rewriting `teach` counts as one). **598E needs 6 skills**, so add your 2 extra skills here too, one round each. No subagents in this step: `p3 check` fails if one appears.
Major review covers **all four jobs** (lesson, quiz, feedback, tutor). EVAL section 2. Compare against `c0-baseline`.
**Why:** this tests whether specialised skills beat one do-everything skill. Be very specific in the major review, because its findings become the checklists for Step 5's reviewers.

### ☐ 5. Step 2: `c2-review`, review loops (≥3 rounds)
**Do:** with the loop, add reviewer **subagents** (files in `tutor/.claude/agents/`) for **teach, quiz and grade**, one per round. The `tutor` job gets none. Each reviewer checks the same criteria you use in your major reviews, each criterion separately: lesson 4, quiz 5, feedback 3. Build their checklists from your c1 major review. Cap the number of revision passes.
Major review covers **lesson, quiz, feedback**. EVAL section 3. Compare against `c1-skills`.
**Why:** this tests whether a second agent checking the work pays for the extra tokens. A reviewer that always says "looks good" is worth nothing.

### ☐ 6. Length study, part 1 (598E; can start as soon as `c1-skills` is snapshotted)
**Do:**
1. Write sections 1 to 4 of `PREREG.md` (your prediction, the smallest difference that matters, the measures, the analysis). **Commit and push it before any length-study run.**
2. In a plain terminal, run 9 teach-only runs:
   `uv run p3 bench --config c1-skills --only teach --minutes 10 --repeats 3`, then the same with `--minutes 30` and `--minutes 60`.

**Why:** the study asks whether a single agent gets worse faster than a split pipeline as lessons get longer. Committing your prediction first proves you didn't fit it to the results; git timestamps are the proof. These runs only need `c1-skills`, so get them out of the way now.

### ☐ 7. Step 3: `c3-split`, split the teach job (≥2 rounds)
**Do:** with the loop, split **only** the lesson-writing job across subagents you design (for example planner, writer, figure designer, references finder), one per round.
Major review covers **the lesson only**. EVAL section 4. Compare against `c2-review`.
**Why:** this tests whether a pipeline of specialists writes better lessons than one agent, and at what cost.
**598E minimum:** 8 subagents in total across all snapshots. Count what you have before you snapshot this step.

### ☐ 8. Two test topics (≈1.75 h each, no runs needed)
**Do:** one topic from another Mines course you took, and one life skill.
1. `uv run p3 new-topic <id>` for each.
2. Replace every `TODO` in `bench/own/<id>/` with your own words. Don't copy course material: the repo is public.
3. Re-run `uv run p3 check` until both topics pass.
4. **Commit and push before running anything on them.**

The life-skill topic must include a probe that tests that the tutor refuses personal financial, medical or legal advice. Your 3 learning sessions in Step 9 happen on one of these topics, so choose one where there's something you still want to learn.
**Why:** you tuned the tutor on one topic only. Fresh topics show whether the improvement is real or just fitted to that topic. A good task to do while full runs are going.

### ☐ 9. `final` (the most parts; start its runs early because they're slow)
**Do, in order:**
1. **Decide what stays.** Drop any component that didn't pay off. Dropping one with evidence is a *good* result; its inventory entry stays, marked `Kept in final: no, because…`.
2. **Guard:** have the Builder add a `PreToolUse` hook in `tutor/.claude/settings.json` that blocks the main conversation from reading `keys/`, while letting a **grader subagent** read them (grading moves into that subagent). Record it as a round in `reviews/final.md`. The facts it has to get right are in "Guard facts" below.
3. **Guard tests:** write `tests/test_guard.py`, which feeds sample inputs to the hook script and checks what it blocks and allows. Then do one `--config live` run and confirm in its trace that the hook actually fired.
4. `uv run p3 snapshot final`, then **commit `tutor/`**.
5. **Start the runs** in a plain terminal, in any order:
   - `uv run p3 bench --config final --repeats 3`
   - **Ablation:** remove one component from `tutor/`, `uv run p3 snapshot final-minus-<name>`, run it once, then `git restore tutor/`
   - Test topics: `uv run p3 bench --config c0-baseline --topic <id>` and `--config final --topic <id>`, for **both** topics (4 runs)
   - Length study: the same 9 teach-only runs as Step 6, with `--config final`
6. **3 learning sessions** while the runs go (with `tutor/` restored): `cd tutor && claude` and actually learn something on one test topic. Write each one up in `reviews/final.md`.
7. **Major review of `final`** (all four jobs). **Commit it before Step 10.**

**Why:** three repeats separate a real difference from run-to-run noise. The guard stops a tutor from handing out answers. The ablation shows whether one specific component matters.
**Cost warning:** a 598E `final` can use 10 to 15M tokens per full run, done 3 times, plus everything else. Check `/usage` first and spread the work over several days.

#### Guard facts (kept from the deleted guide page)
- **Where it goes:** the hook goes in `tutor/.claude/settings.json`. Its script goes under `tutor/.claude/hooks/`. Hooks in a subagent's frontmatter silently don't run in the bench, and `settings.local.json` never reaches the bench.
- **Telling the grader apart:** the hook gets JSON on stdin with `tool_name` and `tool_input`. Inside a subagent the JSON also has `agent_type` (the subagent's `name`). In the main conversation it doesn't, so block when `agent_type` is missing and allow when it's `grader`.
- **Only exit code 2 blocks.** A crash or a missing script lets the call through, so a broken guard looks the same as no guard. Add `"onFailure": "block"` next to `"type"` and `"command"`.
- **Path:** reference the script from the project root, using `python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/keys_guard.py"` on Linux, with forward slashes.
- **Matcher:** `Read|Grep|Glob|Bash|PowerShell`. A Read-only guard is beaten by `cat keys/0001.json`.
- **Don't use a permission deny rule:** it also blocks the grader, and a hook can't undo a deny. Leave the existing `Agent(p3-guide)` deny in `tutor/.claude/settings.json` alone; it's part of the baseline config.
- **Test cases to cover (EVAL §7 asks for them):** block the main conversation via Read, Grep, Glob, `cat`, and PowerShell `Get-Content` on `keys/`. Allow the grader's Read of `keys/`. Allow normal reads like `quizzes/0001.json`, `MISSION.md`, and `ls lessons`.
- **Trace check:** `uv run p3 bench --config live --only grade-s1`, then ask Claude to list every tool call in that run's `trace.jsonl.gz` that touched `keys/`. Keep the run id for EVAL §7.
- **Side effects:** grading must move into the grader subagent, or `grade_verdict_agreement` drops. The quiz skill must write its key once (draft in `drafts/`) and never read it back. The guard probably won't change `tutor_leaks`, because the baseline never read the keys, so don't claim it did.

### ☐ 10. Blind comparisons (≈1 h, no tokens)
**Do:** run these yourself and make every pick yourself. Never open `bench/compare/*.key.json` before the reveal.
- `uv run p3 compare c0-baseline final --job teach`, then `quiz`, `grade` and `tutor`
- Length study: `uv run p3 compare c1-skills final --job teach --teach-only --minutes 10`, then `30` and `60`
- After each one: `uv run p3 compare --reveal <session-id>`. Commit both files it writes.

**Why:** you built `final` and expect it to win, so labels would bias you. Committing your open review first lets you check your bias honestly.

### ☐ 11. Write-up
- `reviews/final.md` → **Test topics**: an open review of c0-baseline vs final on each topic.
- `reviews/components.md`: every component has Purpose, Review and Kept in final.
- `PREREG.md` section 5: the outcome.
- `EVAL.md`: all 13 sections. The ones not covered above:
  - **§10 judge check:** label 10 of the auto-judge's decisions yourself *before* looking at its verdicts, then report how often you agreed.
  - **§11:** one change that didn't pay off.
  - **§12:** the trade-offs across the whole ladder, from `uv run p3 report --configs c0-baseline,c1-skills,c2-review,c3-split,final`.

**Why:** the write-up is where you make your claims and back each one with the measurements.

### ☐ 12. Hand in
`uv run p3 check --final` passes, then push. Record a **5 to 10 min video** (50 pts): your architecture, one review that changed the tutor, the blind reveal, one cost table, what paid off and what didn't, and one real challenge. Post the repo URL and video in the Canvas P3 discussion.

---

## Suggested schedule (you're about a week behind the instructor's pace)

| Days | Work |
|---|---|
| Fri 13 to Sat 14 | Step 3; Step 4 rounds, snapshot, full run, major review |
| Sun 15 | Step 6 (commit PREREG, start the 9 runs); begin Step 5; write test topics while runs go |
| Mon 16 to Tue 17 | Finish Step 5; Step 7 |
| Wed 18 | Step 9 parts 1 to 5: get every `final` run started |
| Thu 19 to Sun 22 | Learning sessions, final major review, Step 10, inventory |
| Mon 23 to Tue 24 | EVAL.md, video, hand in |

## Rules that cost points if broken

- Don't edit `bench/` (except `bench/own/`), `p3/`, or `tutor/FORMATS.md`. They're hash-checked.
- Don't edit `configs/`, `bench/runs/` or `bench/compare/` by hand, and don't delete runs you don't like.
- Don't write anything in the tutor that recognises the shared-topic questions by their text.
- Nothing private in the repo (it's public), including in learning-session files.
- Stuck? Paste the exact error into a Claude session, or take it to office hours (Tue/Thu 9 to 10 and 2 to 3, CTLM 246L).
