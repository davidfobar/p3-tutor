# Review record: lesson 0001 (context and memory, O3)

Passes: 2. The reviewer could not run a shell measurement in either pass (Bash denied), so reading times are the reviewer's hand estimates: pass 1 about 3,500 words (about 23 min, 0.78 of target); pass 2 about 4,600 words (about 30.5 min, 1.02). I did not re-measure after the final fixes.

## Pass 1 (24 findings, grouped)
- A1 Pokémon "favorite" and "rule of thumb" overstated the source: reworded to "one example they give" and "matches each technique to a kind of task", as bullets.
- A4 Figure 1 title and labels disagreed; demo readout hid that the reply adds tokens; whole-manual mode left notes unreachable; prompt 3 did not say to switch back: relabelled, added the reply count, added a message, added "Switch back to the index first".
- B5, C10 Too many undefined terms (embedding-based, CLAUDE.md, glob, grep, sampling, n², system prompt, tool descriptions, memory commands, "agentic memory"): cut or defined in a clause.
- B5 "Your turn" had no immediate feedback: added a button check on the calendar.
- B6 Missing figures for retrieval and for notes across sessions; Figure 2 arrows one-way: added Figures 3 and 4, made arrows two-way.
- B7 M7 never named in a box: added a box.
- B8 Car analogy in four sections: kept in two.
- D11 Cost paragraph and retrieval procedure unlinked: labelled as the lesson's own reasoning, plus a link to the context window docs.
- D12, D13 Length 0.78 of target, section times summed to 29: added a laser cutter call trace, a token-cost worked example, a decision procedure, a design review checklist, a third warm-up question; times re-set to sum to 30.
- D14 M8 box repeated the paragraph and the check: trimmed. Memory commands and technique matching turned into bullets.

## Pass 2 (7 findings)
- A3 Whole-manual design priced with three calls though it needs two: rewrote step 5 (two calls, 122,840 tokens, about 20 times).
- B5 System prompt and tool descriptions defined in one place with other terms: turned the two dfn terms into one plain sentence. Embedding-based cut to a clause.
- C10 "first lesson" with no earlier lesson: now points to learning record 0001.
- D11 Pokémon paragraph had no link: added.
- D14 "Two questions" with three boxes: now "Three questions".
- B5 term density in the retrieval section: reduced as above; I did not cut further.

Declined: none.
