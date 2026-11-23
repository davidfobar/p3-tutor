# Plan: What the assistant sees, and what it remembers

- Objective: O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Minutes: 30
- Win: Riley can say what goes in the makerspace assistant's context, what it saves between sessions, and how it finds a manual page.
- Next lesson: Sub-agents and splitting work across agents; chunking and search details for long manuals.

## Outline

### 1. Why the assistant must remember (O3, 2 min)
- The assistant answers from long manuals and must know each student's training status between visits.
- Context is the tokens included when the model is sampled. [S1]

### 2. Warm-up: one loop, many calls (O3, 3 min)
- Recall the laser cutter trace: each step is a separate model call, so what does each call see?
- Figure: the loop from record 0002 with the context growing at each step.

### 3. The context window is a limited budget (O3, 6 min)
- Context is everything sent in each call: instructions, tool descriptions, history, tool results. [S1]
- Recall accuracy falls as the window fills ("context rot"), gradually and in all models. [S1]
- Context size affects cost per request, which matters for the sponsor's budget.
- Misconception: the model remembers earlier steps by itself -> it only sees what is resent each call. [S1]
- Figure: a cargo-load analogy beside a window filling with manual text.

### 4. Within a session: what to keep between steps (O3, 5 min)
- Compaction summarizes a nearly full conversation and restarts a fresh window with the summary. [S1]
- Clearing old tool results is one of the lightest forms of compaction. [S1]
- Figure: a window near full, a summary, then a fresh window starting with that summary.

### 5. Between sessions: notes as memory (O3, 5 min)
- Notes are written outside the window to persistent storage, such as a NOTES.md file, then read back later. [S1]
- Misconception: a bigger window is memory -> the window does not outlast the session; saved notes do. [S1]
- Figure: two visits by one student, with a training-status record saved at the end of the first.

### 6. Retrieval: finding the right manual page (O3, 4 min)
- Keep lightweight identifiers, such as file paths or stored queries, and load content at runtime with tools. [S1]
- Loading data just in time, instead of pasting whole manuals into context, keeps the window small. [S1]
- Figure: the assistant holding a list of manual file paths, calling a tool that loads one page into the window.

### 7. Worked example and practice (O3, 3 min)
- Decide for three makerspace items: keep in context, save as a note, or retrieve on demand.

### 8. Summary and go further (O3, 2 min)
- Three places information lives: window, notes, retrievable store.
- Go further: read S1 on sub-agents, which return summaries of about 1,000 to 2,000 tokens. [S1]

## Sources

- S1: Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
