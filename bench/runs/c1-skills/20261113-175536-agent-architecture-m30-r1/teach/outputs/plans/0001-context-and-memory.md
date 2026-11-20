# Plan: Context and memory in an agent

## Objectives
- **O3**: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Core:
  1. The context window is everything the model sees on one call (system prompt, tool definitions, history, tool results, its own output); it is finite and counts in tokens.
  2. Between steps: the model keeps nothing; the program resends the growing history, so each step costs more and tool results pile up.
  3. More context is not better: context rot / attention budget; keep the smallest set of high-signal tokens.
  4. Between sessions: nothing is kept unless the program saves it; notes written to files (memory tool, NOTES.md pattern) and read back next session.
  5. Retrieval: chunk, embed, search, put only the top chunks in the prompt; exact-match (BM25) helps with identifiers like "TS-999"; small corpora can skip retrieval.
- Length: 30 minutes reading, plus demo and quiz time.

## Where the learner starts
- Knows (records 0001, 0002): model = text in, text out; agent loop (action, result, repeat).
- Has not shown: that every step is a separate model call (quiz 0001 tests it; ungraded); tokens and what the window limits; memory; retrieval.
- Python, JSON and dicts: fine for a hands-free list-of-messages picture.
- Mission: makerspace assistant answers from long machine manuals and remembers each student's training status between visits; small model budget.

## Material
- Context = "the set of tokens included when sampling from a large-language model"; context engineering curates it. (Anthropic, Effective context engineering, intro.)
- Context window = all text the model can reference when generating, including the response; works like "working memory"; "more context isn't automatically better" because of context rot. (Claude docs, Context windows, "How the context window works".)
- Each turn: input is all previous history plus the new message; the output becomes part of the next turn's input. (Same section.)
- Everything counts: system prompt, every message including tool results, tool definitions. (Same section.)
- Overflow: input too long gives a 400 "prompt is too long" error. (Context windows, "Context window overflow behavior".)
- Attention budget; recall decreases as tokens grow; a gradient, not a cliff; larger windows do not remove it. (Context engineering post, "Why context engineering is important".)
- Pre-loading vs just-in-time: keep lightweight identifiers (file paths), load with tools at runtime; hybrid; "do the simplest thing that works". (Post, "Context retrieval and agentic search".)
- Compaction: summarize and restart with the summary; tool-result clearing is a light form. (Post, "Compaction".)
- Structured note-taking: agent writes notes outside the context window and pulls them back later (NOTES.md, to-do lists). (Post, "Structured note-taking".)
- Sub-agents return 1,000-2,000-token summaries: pointer for the later lesson. (Post, "Sub-agent architectures".)
- Memory tool: file-based, client-side; Claude requests file operations under /memories and the app runs them; commands view, create, str_replace, insert, delete, rename; app must block path traversal; multisession pattern: progress log read first, updated before ending. (Claude docs, Memory tool.)
- RAG: split corpus into chunks (usually no more than a few hundred tokens), embed each, store in vector DB, embed the query, add the best chunks to the prompt. BM25 matches exact words, good for identifiers; example "Error code TS-999". Under 200,000 tokens (about 500 pages) put the whole knowledge base in the prompt, with prompt caching. Top-20 failure 5.7% baseline to 1.9% with contextual embeddings, contextual BM25 and reranking. (Anthropic, Contextual Retrieval.)
- Primary source: Anthropic's Effective context engineering for AI agents.

## Misconceptions
- **M3** (existing): the assistant automatically remembers earlier conversations. Tempting because chat apps seem to. Fix: the model keeps nothing; only what the program saves and puts back in the input. (Context windows doc; memory tool doc.) Evidence: not yet shown; was a distractor in quiz 0001 q1.
- **M7** (new): a bigger context window removes the need to manage context (put in everything). Fix: context rot, cost grows per call, attention budget. (Post.)
- **M8** (new): within one session the model itself remembers earlier steps. Fix: each call gets the whole history resent as input; if the program leaves something out, it is gone. (Context windows doc.)
- **M9** (new): retrieval means the model searches the manual itself / semantic search always finds the exact page. Fix: the program retrieves and pastes chunks; embeddings can miss exact identifiers; BM25 or hybrid. (Contextual Retrieval.)

## Threads to earlier lessons
- No earlier lessons. Records: 0002 loop trace "Is the laser cutter free on Friday?" is the running example; extend it so the learner sees the context at each step. Warm-up: O2 (agent loop): what happens to a tool result? Answer: goes back to the model as next input.

## Diagnostic questions
- M8: "Step 3 of the loop: what does the model call receive?" Right: the whole conversation so far. Wrong: only the latest tool result.
- M3: "A student returns next week. What does the assistant know about their training?" Right: only what the program stored and loaded. Wrong: it remembers.
- M7: "Window is large enough for all manuals. Why still retrieve?" Right: cost and focus. Wrong: no reason.
- M9: "Student asks about error E-417. Which search finds it?" Right: exact-match/hybrid. Wrong: embeddings always.

## Sources
- https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (read)
- https://platform.claude.com/docs/en/build-with-claude/context-windows (read)
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (read)
- https://anthropic.com/research/contextual-retrieval (read)
