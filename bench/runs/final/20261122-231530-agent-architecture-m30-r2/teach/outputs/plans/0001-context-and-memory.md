# Plan: What the Assistant Sees, Keeps and Looks Up

- Objective: O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Minutes: 30
- Win: Riley can say what goes in the makerspace assistant's context, what it saves between sessions, and how it finds a manual page.
- Demo: 3: Watch a context window fill up step by step and choose what to drop, summarize or save.
- Next lesson: Choosing chunk size and ranking methods in depth; token costs in dollars.

## Outline

### 1. Why the assistant needs a memory plan (O3, 2 min)
- The assistant must answer from long manuals and remember each student's training status between visits.
- Like a mechanic's bench: only so many tools fit within reach.

### 2. Warm-up: the loop, revisited (O1, 3 min)
- Riley traced "Is the laser cutter free on Friday?" through the loop; each step is a separate model call.
- Each call receives the text so far; that text is the context.

### 3. The context window and what stays between steps (O3, 7 min)
- Context is a finite resource: each added token draws on an attention budget. [S1]
- Context rot: recall of earlier content declines as the window grows, in all models. [S1]
- Each loop turn adds data; old raw tool results can be cleared, and near the limit a summary starts a new window (compaction). [S1]
- Misconception: more text in context always helps -> more tokens dilute attention, so keep the smallest high-signal set. [S1]
- Figure: window as a bar filling across loop steps, with tool results, summary and cleared parts marked.

### 4. Memory between sessions: notes (O3, 5 min)
- The window is gone when the session ends; the agent writes notes to storage outside it and reloads them later. [S1]
- Example: a NOTES.md-style file, or a per-student record of training status.
- Misconception: the model remembers past visits by itself -> only what is written down and reloaded is remembered. [S1]

### 5. Retrieval: finding the right manual page (O3, 6 min)
- Under 200,000 tokens (about 500 pages), the whole knowledge base can go in the prompt. [S2]
- Larger sets use retrieval: split into chunks of a few hundred tokens, fetch the relevant ones. [S2]
- Embeddings find meaning; BM25 finds exact terms like an error code "TS-999"; combine both. [S2]
- Agents can also keep references and load content just in time, trading speed for a lean context. [S1]
- Figure: manual split into chunks, a question matching top chunks that enter the window.

### 6. Worked example with practice (O3, 4 min)
- Walk one request: a student asks to book the laser cutter and which setting suits 3 mm acrylic.
- Practice: sort each item into context now, notes between sessions, or retrieved on demand.

### 7. Summary (O3, 1.5 min)
- Context is limited and curated; notes persist; retrieval brings in only what is needed.

### 8. Go further (O3, 1.5 min)
- Contextual retrieval cut top-20 failures from 5.7% to 2.9% with BM25 and embeddings combined. [S2]
- Sub-agents return condensed summaries of often 1,000 to 2,000 tokens. [S1]

## Sources

- S1: Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- S2: Introducing Contextual Retrieval, https://www.anthropic.com/news/contextual-retrieval
