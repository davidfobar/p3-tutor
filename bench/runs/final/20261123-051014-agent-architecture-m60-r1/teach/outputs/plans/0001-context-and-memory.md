# Plan: What the assistant sees and what it remembers

- Objective: O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Minutes: 60
- Win: Riley can decide, for the makerspace assistant, what stays in context, what is saved between sessions, and how it finds a manual page.
- Demo: 4: Run a booking request step by step, watch the context fill, then clear old tool results.
- Next lesson: Writing tool descriptions, and when to split work across several agents.

## Outline

### 1. Why the assistant must remember a student (O3, 3 min)
- The assistant answers from long manuals and must recall each student's training status between visits.
- Cost per request depends on what is sent to the model each step [S2].

### 2. Warm-up: the loop, one call per step (O3, 4 min)
- Recall the Friday laser cutter trace from the agent loop.
- Misconception: the model runs tools itself -> the program runs each tool; every step is a separate model call [S2].

### 3. The context window (O3, 10 min)
- The context window is all text the model can reference when answering, including its reply [S2].
- Everything counts: system prompt, every message, tool results, tool definitions [S2].
- Each turn sends all earlier history again, so context and cost grow with each step [S2].
- Misconception: a bigger window means better answers -> accuracy and recall degrade as tokens grow, called context rot [S1][S2].
- Figure: A bar filling across five loop steps, with tool results as the largest slices.

### 4. What is kept between steps (O3, 8 min)
- Within one run the history is kept whole, until the window nears its limit [S2].
- Compaction summarizes a long conversation and starts a new window from the summary [S1].
- Clearing old tool results is the lightest way to free space [S1].
- Figure: A full window, then cleared of old tool results, then compacted into a summary.

### 5. Between sessions: notes as memory (O3, 10 min)
- A new session starts with an empty window; nothing carries over unless saved outside it [S2].
- Structured note-taking: the agent writes notes outside the window and reads them back later, such as a NOTES.md [S1].
- Keep notes small and well organized so recovery at session start is fast [S2].
- Misconception: the model learns from past chats -> only saved notes carry over; the model itself is unchanged [S2].
- Figure: Two sessions with a notes file between them, holding a student's training status.

### 6. Retrieval: finding the right manual page (O3, 10 min)
- Retrieval adds only relevant material to the prompt; manuals are split into chunks of a few hundred tokens [S3].
- Embeddings match meaning but can miss exact identifiers; keyword search (BM25) catches them, so combine both [S3].
- Reranking: retrieve about 150 chunks, pass the top 20 to the model [S3].
- Just-in-time retrieval keeps light references and loads content with tools when needed [S1].
- Figure: A manual split into chunks, about 150 retrieved, the top 20 passed to the model.

### 7. Worked example: the makerspace context plan (O3, 9 min)
- Riley sorts items into three places: always in context, retrieved on demand, saved between sessions.
- Items: tool definitions, laser cutter manual, student's training status, calendar results, booking history.
- Aside: under about 200,000 tokens (roughly 500 pages), the whole knowledge base can go in the prompt [S3].
- Riley estimates which choice cuts tokens per request.

### 8. Summary (O3, 3 min)
- Context is a limited, costly working memory; notes and retrieval extend it.

### 9. Go further (O3, 3 min)
- Sub-agents use clean windows and return summaries of 1,000 to 2,000 tokens [S1].
- Reading: the context engineering article [S1].

## Sources

- S1: Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- S2: Context windows, https://platform.claude.com/docs/en/build-with-claude/context-windows
- S3: Introducing Contextual Retrieval, https://www.anthropic.com/news/contextual-retrieval
