# Plan: Context and memory in an agent

## Objectives
- **O3**: "Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory."
- Core:
  1. The context window is everything the model sees in one call (system prompt, tool definitions, messages, tool results, plus its output); it is finite and costs tokens.
  2. Between steps: the loop's history lives in the context and is resent each call, so it grows.
  3. Between sessions: nothing persists unless the program saves it outside the context (notes, files, database) and loads it back.
  4. Retrieval: fetch only the relevant page from a long manual into context, instead of loading it all.
  5. Notes as memory, and compaction when the context fills.
- Length: 10 minutes (about 1,500 visible words, demo included).

## Where the learner starts
- Knows: model is text in, text out (record 0001); agent loop at high level (record 0002); Python, JSON.
- Not shown: what a token or context window is, why they affect cost, retrieval, memory. Quiz 0001 not graded; whether Riley knows each step is a separate model call is unchecked, and this lesson rests on it.
- Prefers: hands-on first, big picture then zoom, sketches, cars as examples, short paragraph then bullets, peer tone.

## Material
- Context = "the set of tokens included when sampling from a large-language model". Source: Anthropic context engineering post, intro / "Context engineering vs. prompt engineering".
- Context window = all text the model can reference when responding, including the response; each turn's input holds all previous history plus the new message. Source: Claude docs, Context windows, intro and "turn by turn" section.
- What counts toward it: system prompt, every message incl. tool results, tool definitions, and the output. Source: Claude docs, Context windows.
- Overflow: input too large gets a 400 "prompt is too long" error. Source: Claude docs, Context windows.
- The docs do not say outright that the API stores nothing; they imply the caller sends the history. Teach it as "the program sends the history each call" and cite only the implication; do not overstate.
- Context rot: more tokens means lower recall accuracy; an "attention budget"; a gradient, not a cliff. Sources: context engineering post, "Why context engineering is important..."; docs "More context isn't automatically better".
- Aim for the smallest set of high-signal tokens. Source: context engineering post.
- Compaction: summarize a conversation nearing the limit and start a new window with the summary. Claude Code keeps decisions and unresolved bugs, drops redundant tool output. Source: post, "Compaction".
- Tool result clearing is a light form of compaction. Source: post.
- Structured note-taking: the agent writes notes outside the context window and pulls them back later (to-do list, NOTES.md). Source: post, "Structured note-taking".
- Retrieval: pre-loaded (embedding-based, before inference) vs just-in-time (keep lightweight identifiers such as file paths and load on demand); just-in-time is slower; hybrid is common; "do the simplest thing that works". Source: post, "Context retrieval and agentic search".
- Sub-agents return a condensed summary (often 1,000-2,000 tokens). Source: post, "Sub-agent architectures"; preview only, belongs to a later objective.
- Possible demo: a simulated agent where the learner steps through calls and watches the context token meter grow, then a "new session" button that empties it unless notes were saved.
- Car analogy: context is the workbench, notes are the service logbook in the glovebox, retrieval is looking up one page in the shop manual.

## Misconceptions
- M3 (new): The model remembers earlier conversations or steps by itself. Tempting because chatbots feel continuous. Fix: the program resends the history in the context; a new session starts empty. Source: Claude docs, Context windows. Not yet shown.
- M4 (new): A bigger context window means put in everything (the whole manual). Tempting because it fits. Fix: more context is not automatically better (context rot), and every token costs. Source: docs "More context isn't automatically better"; post. Quiz 0001 q1 had a "larger context window" distractor, so watch for this.
- M5 (new): Notes or memory are inside the model, or happen automatically. Fix: the program writes them to storage outside the context and loads them back. Source: post, "Structured note-taking".
- M6 (new): Retrieval means the model knows where the answer is. Fix: the program or a tool selects pages and puts them into context; the model sees only what is loaded. Source: post, retrieval section.

## Threads to earlier lessons
- No earlier lessons exist. Build on records 0001 (the model knows only training plus given text) and 0002 (loop, "Is the laser cutter free on Friday?").
- Extend the Friday laser cutter trace: show what is in context at each step.
- Retrieval question at the start: in the agent loop, what does the model receive after a tool runs? (the tool result, added to its input).

## Diagnostic questions
- M3: "A student closes the chat and returns tomorrow. With no extra code, does the assistant know their name?" Right: no. Wrong: yes, the model remembers.
- M3: "In a 5-step loop, is step 5 a fresh call that sees steps 1-4?" Right: separate call, history resent. Wrong: the model carries it internally.
- M4: "Your manual is 300 pages and fits in the window. Best to paste it all in every request?" Right: no, cost and recall; retrieve the relevant page. Wrong: yes, fits so fine.
- M5: "Where does the student's training status live between visits?" Right: a database or file the program reads and writes. Wrong: in the model.
- M6: "Who decides which manual page enters context?" Right: the program or a tool call. Wrong: the model just knows.

## Sources
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), read.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), read.
