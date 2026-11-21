# Plan: Context and memory in an agent

## Objectives
- **O3**: "Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory."
- Length: 60 minutes reading (requested).
- Core:
  1. The model keeps nothing between calls; the program resends the whole context each step (M9).
  2. The context window holds everything (system prompt, tool definitions, messages, tool results), is limited, and costs tokens on every call.
  3. A fuller window is not a better one: context rot; keep context lean (clear old tool results, compact, sub-agents).
  4. Between sessions nothing persists unless the program stores it: notes/memory files read at the start of the next session (M3).
  5. Retrieval finds the right page in a long manual: chunk, embed, search, add to prompt; keyword search (BM25) for exact terms; a small manual may fit whole; just-in-time vs up front.
- Win: for the makerspace assistant, decide what goes in context, what is saved between sessions and how it finds a manual page.

## Where the learner starts
- Knows the agent loop (record 0002) and what a model does (0001); Python; has heard "token" and "context window" but cannot say what they limit or why they affect cost (NOTES.md).
- Has not met memory or retrieval. Quiz 0001 not yet graded, so "program runs tools / each step is a separate call" is unconfirmed: re-teach through the stateless-call idea.
- Prefers hands-on first, big picture then zoom, car examples, short paragraph then bullet procedure, direct feedback, peer tone.

## Material
- Context window = all the text the model can reference when generating, including its response; a "working memory", distinct from training data. Each turn resends all previous history as input; output becomes part of the next input. System prompt, messages, tool results and tool definitions all count. (Context windows doc, "How the context window works".)
- More context is not automatically better: accuracy and recall degrade as tokens grow, "context rot". (Context windows doc, intro; Context engineering post, "Context engineering vs. prompt engineering".)
- Overflow: input too large gives a 400 "prompt is too long" error; on newer models generation can stop with `model_context_window_exceeded`. (Context windows doc, "Context window overflow behavior".)
- Compaction summarizes earlier conversation so it can continue; tool result clearing drops old tool results. Prompt caching changes cost, not capacity: cached prefixes still occupy the window. (Context windows doc, "Manage context with compaction"; context engineering post, "Compaction".)
- Finite attention budget; goal is the smallest set of high-signal tokens; compaction keeps decisions, unresolved bugs, drops redundant tool output; note-taking outside the window (NOTES.md, to-do list); Pokemon example with tallies over thousands of steps and reads notes after context resets; sub-agents return 1,000-2,000-token summaries; just-in-time vs up-front retrieval and the hybrid. (Context engineering post.)
- Memory tool: client-side, directory of files under /memories, commands view/create/str_replace/insert/delete/rename; program implements storage; Claude checks the directory first; "Your context window might be reset at any moment". Cautions: path traversal, sensitive information, file size, expiration. (Memory tool doc.)
- RAG: chunk (a few hundred tokens), embed, vector search, append top chunks to prompt. Under 200,000 tokens (about 500 pages) just include the whole knowledge base. Embeddings miss exact matches (e.g. "Error code TS-999"), BM25 finds them; combine. A chunk can lack context ("revenue grew by 3%" without naming the company); contextual retrieval prepends 50-100 tokens. Failure rate (top-20) 5.7% -> 3.7% -> 2.9% -> 1.9% (with reranking). (Contextual retrieval post.)

## Misconceptions
- **M3** (workspace key 0001): the assistant automatically remembers earlier conversations. Tempting: chatbots feel continuous. Fix: each session starts empty; only what the program stores and loads exists (Memory tool doc). Not yet shown by learner.
- **M9** (new): the model itself holds state between steps. Tempting: the conversation feels continuous. Fix: each call gets the full history resent (Context windows doc).
- **M7** (new): a bigger window / more context is always better, so put the whole manual in. Fix: context rot, cost on every call (Context windows doc; engineering post).
- **M8** (new): semantic search always finds the right page. Tempting: "it understands meaning". Fix: embeddings can miss exact identifiers; add BM25; chunks can lack context (Contextual retrieval post).
- M1 (longer prompt is what matters) appears in key 0001; touch only lightly.

## Threads to earlier lessons
- No earlier lessons. Use records: 0002 trace "Is the laser cutter free on Friday?" (extend it: what does the model see at each call?); quiz 0001 q4 (count of model calls) as warm-up retrieval.
- Warm-up: why must the program send the tool result back to the model (O1); how many model calls for three tools.

## Diagnostic questions
- M9: "Between call 2 and call 3, where is the calendar result?" Right: in the resent input; wrong: "the model remembers it".
- M3: "Tomorrow the student returns; the assistant never wrote anything down. What does it know about their training?" Right: nothing; wrong: it remembers.
- M7: "Manual is 6,000 tokens; every call resends it. Total input over 3 calls?" Right: it is paid every call; wrong: once.
- M8: "Search 'Error E-47' returns generic troubleshooting." Right: add keyword search; wrong: bigger embedding model only.

## Sources
- https://platform.claude.com/docs/en/build-with-claude/context-windows (read)
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (read)
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (read; primary)
- https://www.anthropic.com/engineering/contextual-retrieval (read)
