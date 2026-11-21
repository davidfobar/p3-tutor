# Plan: Context and memory: what the assistant sees, keeps and looks up

## Objectives
- **O3**: "Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory."
- Length: 30 minutes. No quiz requested; the learner asks separately.
- Core ideas:
  1. The context window is everything the model is given for one call (system prompt, tool descriptions, the whole message history including tool results, and the output). It is working memory, not training data, and it is finite.
  2. Between steps: the model keeps nothing itself; the program re-sends the growing context at every step. Between sessions: nothing survives unless the program saves it.
  3. Bigger context is not free or perfect: more tokens cost more and recall gets worse (context rot), so keep the smallest set of high-signal tokens.
  4. Retrieval: find the right page of a long manual and put only that in context, just in time, via a tool.
  5. Notes as memory: the agent writes to files outside the window and reads them back later; the program does the storage.
- Learner's win: for the makerspace assistant, decide what stays in context, what is saved per student between visits, and how a manual page is found.

## Where the learner starts
- Knows (record 0001): model = text in, text out; knows only training plus the given text.
- Knows (record 0002): the agent loop; the result goes back to the model.
- Not shown: that every step is a separate call and that the program runs tools (quiz 0001, ungraded). State briefly, build on it, then check.
- Has heard "token" and "context window" but cannot say what they limit or why they affect cost. Introduce tokens in one paragraph, no ML.
- Comfortable with Python and JSON: show the context as a list of dicts.
- Preferences: hands-on first, big picture then zoom in, car analogies, short paragraph then bullet procedure, sketches, peer tone.

## Material
Core idea 1 (context window)
- The context window is all the text a model can reference when generating, including its own response; it is "working memory", distinct from the training data. Everything in the request counts: system prompt, every message including tool results, tool definitions; the turn's output counts too. [Context windows docs]
- Context is "the set of tokens included when sampling" from the model. [Anthropic context engineering, intro]
- Window sizes vary by model (e.g. 200k tokens for some, 1M for others); do not teach one number as general. [Context windows docs]

Core idea 2 (steps vs sessions)
- Message history and tool results accumulate each turn. [Anthropic, compaction section; Context windows docs]
- "Your context window might be reset at any moment", so anything not written to a memory file can be lost. [Memory tool docs]
- "Memory lives entirely in your application"; files in the application's store persist across sessions. [Memory tool docs]

Core idea 3 (limits)
- Context rot: as tokens grow, recall of information in the context decreases; a gradient, not a cliff. Context is a finite "attention budget" with diminishing returns; aim for the smallest set of high-signal tokens. [Anthropic, context vs prompt engineering section; Context windows docs]
- Cause, one line only: every token attends to every other, n² pairs. [Anthropic, same section]
- Cost: more tokens in the request means more to process; keep it qualitative (no pricing source; see RESOURCES.md Gaps).
- Compaction: summarize a near-full window and restart with the summary, keeping decisions and unresolved bugs and dropping redundant tool output; lightest form is clearing old raw tool results. [Anthropic, compaction]

Core idea 4 (retrieval)
- Pre-inference (embedding-based) retrieval puts relevant material in up front; just-in-time retrieval keeps lightweight identifiers (file paths, queries, links) and loads data with tools at runtime. [Anthropic, context retrieval and agentic search]
- Claude Code is a hybrid: CLAUDE.md dropped in up front, glob/grep fetch files on demand. Trade-off: runtime exploration is slower and needs good tool design. "Do the simplest thing that works." [same]
- Adaptable example: a manual index (page titles) in context plus a `read_page(manual, page)` tool.

Core idea 5 (notes)
- Structured note-taking: the agent writes notes outside the window and reads them back later (a to-do list, a NOTES.md). Pokémon example: "for the last 1,234 steps I've been training my Pokémon in Route 1, Pikachu has gained 8 levels toward the target of 10"; after context resets it reads its notes and continues. [Anthropic, structured note-taking]
- Memory tool: files under /memories; commands view, create, str_replace, insert, delete, rename; the model only requests the operation, the application executes it and returns a tool_result; Claude checks memory before starting. Use cases: project context across sessions, lessons from past interactions, a growing knowledge base. [Memory tool docs]
- Choosing: compaction for long back-and-forth, notes for work with clear milestones, sub-agents for parallel research (later lesson). [Anthropic, long-horizon section]

Figure and example ideas
- Context as a stack of messages growing each step, with a fill gauge.
- Car analogy: context window = the dashboard and the road in view right now; notes = the service logbook in the glovebox; retrieval = opening the shop manual to one page instead of strapping it to the dash.
- Makerspace: a student returns next week; training status is in a per-student notes file the program loads.

## Misconceptions
- **M3** (existing; quiz 0001 q1 distractor b): the assistant automatically remembers earlier conversations. Tempting because chatbots seem to. Fact: memory is not automatic; the application stores and reloads it. [Memory tool docs] Not yet shown by the learner (quiz ungraded).
- **M7**: the model itself keeps state between steps, so it "remembers" earlier tool results without being resent. Tempting from the chat experience. Fact: each step is a new call over the whole context the program sends. [Context windows docs] Related to M4 (quiz 0001).
- **M8**: a bigger context window removes the need to choose what to include. Tempting: "just paste everything". Fact: recall decreases as context grows and more tokens mean more to process; aim for the smallest high-signal set. [Anthropic, context rot]
- **M9**: notes or memory mean the model learns, i.e. its weights change. Tempting because "memory" and "learning" blur. Fact: notes are ordinary files the program stores and the model re-reads into context; the model is unchanged. [Memory tool docs, client-side execution]
- **M10**: retrieval means loading the whole manual into context, or that the model searches the manuals by itself. Fact: a tool run by the program fetches only the needed piece, just in time, or relevant pieces are chosen up front. [Anthropic, retrieval section]
- The learner has shown none of M7 to M10 yet.

## Threads to earlier lessons
- No lessons exist yet (`lessons/` is empty). Threads come from the records and quiz:
  - Record 0002: the "Is the laser cutter free on Friday?" trace. Extend it: show the context after each step, growing with the tool call and its result.
  - Record 0001: "the model knows only training plus the text it is given"; the context window is exactly that text, so notes and retrieval are ways to get the right text in.
  - Quiz 0001 q4: one model call per input supports M7.
- Warm-up (O1/O2): who runs a tool, the model or the program? What happens to the result after it runs?

## Diagnostic questions
For practice, not a quiz.
- M7: "In step 3 the model uses a calendar result from step 2. Where does it get it from?" Right: the program included it in call 3's input. Wrong: "it remembers it from the previous step."
- M3: "A student trained on the laser cutter Monday and returns Thursday to a new session. With no extra code, what does the assistant know about them?" Right: nothing; a new session starts with an empty context. Wrong: "it remembers their training."
- M8: "The manual is 400 pages and fits in the window. Is pasting it into every request the best design? One reason." Right: no; cost and recall drop. Wrong: "yes, it has everything it needs."
- M9: "After the agent writes a note to its memory file, what changed: the model or something else?" Right: a file in the program's storage. Wrong: "the model learned it."
- M10: "Which is retrieval for the manuals: (a) all manuals in the system prompt; (b) an index plus a tool that returns one page; (c) retrain the model on the manuals?" Right: b. Wrong: a or c.
- Design check: sort training status, today's chat, and the band-saw manual into keep in context / save between sessions / look up on demand.

## Sources
- [Anthropic Engineering: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (primary; read in full)
- [Claude Docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) (read)
- [Claude Docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (read)
