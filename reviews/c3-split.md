# Reviews: c3-split

Your quick rounds while you split up the teach job, and then the major review of `c3-split`.
Add one subagent of the teach pipeline per round, so the run before it shows the lesson without it and the run after it shows the lesson with it.
The major review covers the lesson only, and its previous step is `c2-review`.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c2-review/20261120-214054-agent-architecture-m30-r1

**My thoughts:**

@reviews/c2-review.md: implement 
 - lesson-planner: provided a series of learning objectives, it considers the expected misconceptions and builds an outline for a complete lesson
 - lesson-writer: provided an outline of a lesson and the desired duration, it constructs a complete lesson - it calls on resource-finder and demo-dev agents

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-planner.md, tutor/.claude/skills/teach/SKILL.md
- Why: As the first of the two roles asked for, a lesson-planner subagent now takes the learning objectives and minutes, does the plan skill's preparation with each expected misconception and its correcting fact, and adds an outline of the complete lesson (the win, each section's objective, core idea, misconception, example, figure, practice check and word budget, and the demo slot) that the teach skill now writes from.

### Round 2

**Run:** bench/runs/_live/20261121-181658-agent-architecture-m30-r1

**My thoughts:**

ok, the lesson follows teh planner, but many of the graphics are poorly formatted. add the demo-dev subagent whose job is to create any graphics and demos for the lesson. Its products should be reviewed prior to be accepted for use in a lesson.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/demo-dev.md, tutor/.claude/skills/teach/SKILL.md, tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/agents/lesson-planner.md
- Why: To fix the poorly formatted graphics and have them reviewed before use, a demo-dev subagent now builds the demo and every figure in the outline as separate fragments laid out by numbered rules (label widths estimated and checked against their boxes, no overlaps or rotated text, one style), the lesson-reviewer gained a visuals review that redoes that layout check, and the teach skill pastes only visuals it accepted, after at most two passes, recorded in review-records/NNNN-visuals.md.

### Round 3

**Run:** bench/runs/_live/20261121-184822-agent-architecture-m30-r1

**My thoughts:**

The agents submitted 6 actions that were met with denial - this can be fixed by added reles to SKILL.md, address the analysis for denials 5 and 6:
Only two of the six denials are worth fixing, and they're the same command. The other four can be avoided with the tools the
  skill already has. The latest live run is 20261121-184822, and its teach scenario still finished (ok, one lesson in lessons/). I
  changed no files.

  Denials 5 and 6: the reviewer's measuring tool. This is the only real loss.
  python3 /tmp/p3-endf6tdp/.claude/tools/lesson_check.py /tmp/p3-endf6tdp/drafts/0001-context-and-memory.html
  - Your rule Bash(python3 .claude/tools/lesson_check.py:*) matches only the relative path. The reviewer added the scenario folder
    in front, so both passes estimated length by hand. The record says pass 1 was "about 4,900 words excluding the demo … 108% to
    116%".
  - Without a new rule (my recommendation): in lesson-reviewer.md, tell it to run the command exactly as written, with the
    relative path, and never put the workspace's folder in front of it. The bench starts every session at the workspace's root, so
    the relative form passes the rule you already have.
  - With a rule: Bash(python3 /tmp/p3-*/.claude/tools/lesson_check.py *) still allows only this one script. Two caveats:
    - I'm not certain Claude Code matches a * in the middle of a Bash rule, so a live run would have to confirm it.
    - The /tmp/p3- folder is what the bench used on your machine. On macOS the temporary folder is elsewhere, so the rule wouldn't
      carry over.

  Denials 1 to 4: no allow rule needed. A rule broad enough to let these through would have to allow python3, sed or loops in
  general.

  ┌─────┬───────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────┐
  │  #  │                    Command                    │                  How the skill finishes without it                  │
  ├─────┼───────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┤
  │ 1   │ for f in 0001-fig*.html; do … sed … head …;   │ Read or Grep the figure files. No allow rule can pass a loop like   │
  │     │ done                                          │ this anyway ("A variable in this command can't be checked").        │
  ├─────┼───────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┤
  │     │ python3 -I - <<'EOF' putting the template,    │ Read the fragments and paste them in with Write or Edit, which it   │
  │ 2   │ demo and figures together into                │ then did. It also tried to write outside the workspace.             │
  │     │ /tmp/p3_parts.py                              │                                                                     │
  ├─────┼───────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┤
  │     │                                               │ It wrote the same file with the Write tool right after, and the     │
  │ 3   │ mkdir -p assets && sed … > assets/lesson.css  │ lesson links it as ../assets/lesson.css. FORMATS.md allows that, so │
  │     │                                               │  nothing was lost.                                                  │
  ├─────┼───────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┤
  │     │ python3 -I -c "…print(len(t.split()))", a     │ Run python3 .claude/tools/lesson_check.py drafts/<file> with the    │
  │ 4   │ word count                                    │ relative path. It's already allowed and prints the visible words    │
  │     │                                               │ per section.                                                        │
  └─────┴───────────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────┘

  So for 1 to 4, a short rule in teach/SKILL.md would do it: look at files with Read, Glob and Grep, build the draft with Write
  and Edit, and use no shell command except lesson_check.py with its relative path.

**What changed:**

- Kind: other
- Files: tutor/.claude/agents/lesson-reviewer.md
- Why: To fix denials 5 and 6, where the lesson-reviewer called lesson_check.py by its absolute path and so missed the allow rule and measured the lesson by hand, it now runs the command only in the relative form the existing rule allows, cuts any folder off the draft's path, and retries once in that form before falling back to a hand estimate.

### Round 4

**Run:** bench/runs/_live/20261121-184822-agent-architecture-m30-r1

**My thoughts:**

The agents submitted 6 actions that were met with denial - this can be fixed by added reles to SKILL.md, address the analysis for denials 1 through 4:
Only two of the six denials are worth fixing, and they're the same command. The other four can be avoided with the tools the
  skill already has. The latest live run is 20261121-184822, and its teach scenario still finished (ok, one lesson in lessons/). I
  changed no files.

  Denials 5 and 6: the reviewer's measuring tool. This is the only real loss.
  python3 /tmp/p3-endf6tdp/.claude/tools/lesson_check.py /tmp/p3-endf6tdp/drafts/0001-context-and-memory.html
  - Your rule Bash(python3 .claude/tools/lesson_check.py:*) matches only the relative path. The reviewer added the scenario folder
    in front, so both passes estimated length by hand. The record says pass 1 was "about 4,900 words excluding the demo … 108% to
    116%".
  - Without a new rule (my recommendation): in lesson-reviewer.md, tell it to run the command exactly as written, with the
    relative path, and never put the workspace's folder in front of it. The bench starts every session at the workspace's root, so
    the relative form passes the rule you already have.
  - With a rule: Bash(python3 /tmp/p3-*/.claude/tools/lesson_check.py *) still allows only this one script. Two caveats:
    - I'm not certain Claude Code matches a * in the middle of a Bash rule, so a live run would have to confirm it.
    - The /tmp/p3- folder is what the bench used on your machine. On macOS the temporary folder is elsewhere, so the rule wouldn't
      carry over.

  Denials 1 to 4: no allow rule needed. A rule broad enough to let these through would have to allow python3, sed or loops in
  general.

  ┌─────┬───────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────┐
  │  #  │                    Command                    │                  How the skill finishes without it                  │
  ├─────┼───────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┤
  │ 1   │ for f in 0001-fig*.html; do … sed … head …;   │ Read or Grep the figure files. No allow rule can pass a loop like   │
  │     │ done                                          │ this anyway ("A variable in this command can't be checked").        │
  ├─────┼───────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┤
  │     │ python3 -I - <<'EOF' putting the template,    │ Read the fragments and paste them in with Write or Edit, which it   │
  │ 2   │ demo and figures together into                │ then did. It also tried to write outside the workspace.             │
  │     │ /tmp/p3_parts.py                              │                                                                     │
  ├─────┼───────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┤
  │     │                                               │ It wrote the same file with the Write tool right after, and the     │
  │ 3   │ mkdir -p assets && sed … > assets/lesson.css  │ lesson links it as ../assets/lesson.css. FORMATS.md allows that, so │
  │     │                                               │  nothing was lost.                                                  │
  ├─────┼───────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┤
  │     │ python3 -I -c "…print(len(t.split()))", a     │ Run python3 .claude/tools/lesson_check.py drafts/<file> with the    │
  │ 4   │ word count                                    │ relative path. It's already allowed and prints the visible words    │
  │     │                                               │ per section.                                                        │
  └─────┴───────────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────┘

  So for 1 to 4, a short rule in teach/SKILL.md would do it: look at files with Read, Glob and Grep, build the draft with Write
  and Edit, and use no shell command except lesson_check.py with its relative path.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/SKILL.md
- Why: To fix denials 1 to 4, where the main teach conversation used shell commands to look at files, assemble the page, extract the CSS and count words, the teach skill now has a Tools section: Read, Glob and Grep to look, Write and Edit to make and assemble files inside the workspace, and lesson_check.py with relative paths as its only shell command, for the word count.

### Round 5

**Run:** bench/runs/_live/20261121-184822-agent-architecture-m30-r1

**My thoughts:**

add a dedicated reviewer subagent rather relying on the teach agent skill. The reviewer should look at the product of each agent and have a chance to provide feedback for changes prior to giving it to the requester. Limit the feedback to two rounds.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/product-reviewer.md, tutor/.claude/agents/lesson-planner.md, tutor/.claude/agents/demo-dev.md, tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: So that a dedicated reviewer checks each agent's product before it goes back to the teach skill, a product-reviewer now reviews the lesson-planner's plan (budget, placement of every core idea and misconception, shape, figures, sources) and demo-dev's visuals (the layout, consistency, correctness and demo checks moved out of lesson-reviewer), and each of those agents starts it itself, fixes its findings, and stops after at most two passes.

## Major review

**Run:** bench/runs/c3-split/20261121-225109-agent-architecture-m30-r1

**Live tries:**

The tutor just did a good job of explaining the topic that I requested, informed me that it was not on the current quiz and asked if I would like to focus on that. It refused to score my incorrect answers as correct. But the review and response of my incorrect answers takes a least a minute, which seems longer than necessary.

### Lesson

#### Technical correctness and facts

Rating: 5

#### Pedagogy

Rating: 5

#### Alignment with the learning goal

Rating: 5

#### Overall quality

Rating: 5

### Compared with the previous step

The token usage did not increase dramatically, but the time to generate a lesson did go up a noticable amount. The figures and demos have more polish and less build issues. The overall structure of the lesson and content presented has not changed a significant amount, it still provides links to materials and uses figures and demos to aid understanding, but that has been the case since the skills were added early on.

### What the next step should fix

Maybe attempt to reduce the token usage by decreasing the review iterations. It seems like the plan itself is the longest created document, so maybe reducing the scope what what the planner is creating - maybe have it just create an outline with estimated time per section, key points of coverage. Right now, it basically creates an entire lessons worth of reading material. I think the reviewer is a worthwhile agent to maintain, the max reviews can be limited to 1 for each sub-agent, thought the final product should be allowed to recieve an second pass.
