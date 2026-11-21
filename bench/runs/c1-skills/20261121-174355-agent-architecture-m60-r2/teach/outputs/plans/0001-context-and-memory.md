# Plan: Context and memory in an agent (what the model sees, what is kept, what is saved)

## Objectives
- **O3**: "Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory."
- Length: 60 min.
- Core:
  1. Context = the set of tokens given to the model on one call (system prompt, tool definitions, message history, tool results) plus its output; the window is the cap on it.
  2. Between steps: the loop's history is carried by the program, which resends it each call; it grows every step, so cost and quality are affected.
  3. Between sessions: nothing is kept unless the program saves it; memory is a store the app owns.
  4. Retrieval: fetch only the relevant page of a long manual into context, up front or just in time.
  5. Notes: the agent writes facts outside the window (file) and reads them back; compaction summarizes when the window fills.
- Win: Riley sketches what the makerspace assistant puts in context, saves per student, and retrieves from manuals.

## Where the learner starts
- Knows: model is text in/text out (record 0001); the agent loop (record 0002); Python, JSON, one web API.
- Has heard "token" and "context window" but cannot say what they limit or why they affect cost (NOTES.md). Tokens were never taught: teach briefly here.
- Not shown: that every step is a separate model call and that the program runs tools (quiz 0001 ungraded, two submissions, not graded). Do not build on them as shown; recap lightly.
- Preferences: hands-on first, big picture then zoom, sketches, car examples, short paragraph then bullet procedure, peer tone, direct.
- Mission: makerspace assistant answers from long manuals, remembers each student's training status, small budget.

## Material
Primary source: Anthropic Engineering, "Effective context engineering for AI agents" (A).
- Context is the set of tokens included when sampling from the model (A, "Context engineering vs. prompt engineering"). Context engineering is curating that set; aim for the smallest set of high-signal tokens (A).
- Context rot: recall falls as tokens grow; context is a finite resource with diminishing returns, an "attention budget" (A, "Why context engineering is important"). Docs agree: more context is not automatically better (C).
- Everything counts toward the window: system prompt, tool definitions, every message, tool results, and the output (C, "Context window"/"Tool results"). Each turn's history is preserved in full and the response becomes input next turn (C). Caching changes price, not whether tokens count (C, usage/caching).
- Overflow: input too long gives a 400 "prompt is too long" error; newer models may stop with stop_reason model_context_window_exceeded (C).
- Up-front retrieval (embedding search before the call) vs just-in-time: the agent keeps lightweight identifiers (paths, queries, links) and loads data with tools; "progressive disclosure"; slower and can waste context on dead ends; hybrid is common; "do the simplest thing that works" (A, "Context retrieval and agentic search").
- Claude Code example: CLAUDE.md loaded up front, glob and grep fetch files just in time (A).
- Compaction: summarize a conversation nearing the limit and start a new window with the summary; keep decisions, unresolved bugs; drop redundant tool outputs; risk of losing subtle details; lightest form is clearing old tool results (A, "Compaction").
- Structured note-taking: agent writes notes to memory outside the window and reads them later; to-do list, NOTES.md; Claude playing Pokémon keeps tallies and maps across resets (A, "Structured note-taking").
- Sub-agents: clean contexts, return 1,000-2,000-token summaries (A); mention only as a pointer, it is a later objective.
- Memory tool: client-side; the app runs view/create/str_replace/insert/delete/rename on a /memories store; persistence depends on the app's storage; context "might be reset at any moment" so save progress as you go (M). Security: validate paths against traversal; do not store sensitive data; cap size; expire old files (M, "Security").
- Adaptable figure: a bar growing each step as history, tool results and output add up (C turn diagram); worked example: count tokens in a 5-step run for the laser-cutter question.
- Demo idea (for /demo): a context-window "meter" where Riley steps through the assistant loop, sees what is resent each call, and toggles retrieval, compaction, notes.
- Car analogy candidates: the window is the workbench (only what is on the bench can be used); notes are the shop's job-card file; retrieval is fetching one page of the service manual rather than carrying the whole book.

## Misconceptions
- **M5** "The model remembers earlier steps/conversations by itself." Tempting because chatbots feel continuous. Fix: each call sees only what the program sends; history is resent (C); between sessions only what the app saves (M). Not yet shown by Riley; related quiz 0001 distractor M3 (automatic memory), ungraded.
- **M6** "A bigger context window solves memory and long manuals." Tempting because bigger sounds better. Fix: context rot, finite attention budget, cost per token (A, C).
- **M7** "Put the whole manual in the prompt." Fix: retrieve the relevant pages; keep the smallest high-signal set (A).
- **M8** "Memory means the model learns/changes (training)." Fix: memory is files the program stores and re-reads into context (M); training is out of scope (record 0001).
- **M9** "Compaction or notes are lossless." Fix: summaries can lose subtle critical details (A, "Compaction").
- **M10** "Tokens are words, and only my typed message counts." Fix: tool definitions, tool results and outputs count too (C).
- Existing ids: M1, M3, M4 appear in key 0001; check keys/0001.json before reuse. Learner-shown: none yet.

## Threads to earlier lessons
- No earlier lessons (lessons/ is empty). Build on record 0002 (the loop; Riley's traced laser-cutter request) and record 0001 (the model knows only training plus the text it is given).
- Running example: "Is the laser cutter free Friday?" extended with a training-status check and a manual lookup.
- Warm-up retrieval (recalls O1/O2): "In the loop, what is sent to the model at step 2?" and "Who runs the tool?"

## Diagnostic questions
- M5: "A student chats Monday, returns Thursday. With no extra code, what does the assistant know from Monday?" Right: nothing. Wrong: it remembers.
- M5: "At step 3 of a loop, what does the program send the model?" Right: system prompt, tools, and all earlier messages and results. Wrong: only the latest result.
- M6: "A model has a window 10x bigger. Does that remove the need to pick which manual pages to include?" Right: no (rot, cost). Wrong: yes.
- M7: "The laser cutter manual is 300 pages; the question is about focus height. Best approach?" Right: retrieve the relevant section. Wrong: paste it all.
- M8: "Where does the assistant's note 'Sam passed laser training' live?" Right: a file/DB the app owns, re-read into context. Wrong: inside the model.
- M9: "After compaction, the assistant forgets a student's allergy to a material. Why?" Right: the summary dropped it. Wrong: model glitch/no cause.
- M10: "List what takes up space in context on a step after one tool call." Right: incl. tool definitions and result. Wrong: only user message.

## Sources
- A: [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (read, via fetch)
- C: [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (read, via fetch)
- M: [Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (read, via fetch)
