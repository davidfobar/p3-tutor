# Plan: Context and memory in the makerspace assistant

- Objective: O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Minutes: 10
- Win: Riley can say what the assistant keeps in context, what it saves between visits, and how it finds a manual page.
- Demo: 4: Fill the window step by step, then clear or summarize to make room.
- Next lesson: Cost per request and token budgeting.

## Outline

### 1. Why the assistant must remember (O3, 0.5 min)
- Assistant must answer from long manuals and recall each student's training status [S1]

### 2. Warm-up: the loop revisited (O3, 0.5 min)
- Each loop step is a separate model call, so the model needs the story so far [S2]

### 3. The context window (O3, 2 min)
- Window is all text the model can reference, including its own response [S2]
- Counts system prompt, messages, tool results and tool definitions [S2]
- More context is not better: accuracy and recall degrade, called context rot [S2][S1]
- Misconception: the model remembers earlier chats by itself -> it only sees what is in the window [S2]
- Figure: static fuel-gauge with segments for instructions, tools, history and results

### 4. What is kept between steps (O3, 1.5 min)
- Earlier turns are preserved and sent again as input each turn [S2]
- Old tool results are the lightest thing to clear [S1]
- Compaction summarizes a near-full conversation and restarts with the summary [S1]

### 5. What is kept between sessions: notes (O3, 1.5 min)
- Structured note-taking: agent writes notes outside the window and rereads them later [S1]
- Misconception: a bigger window replaces memory -> notes outlast any window [S1]
- Figure: two sessions with empty windows, a notes file session 1 writes and session 2 reads

### 6. Retrieval: finding the right manual page (O3, 1.5 min)
- Keep lightweight identifiers, such as file paths, and load content when needed [S1]
- Trade-off: loading at runtime is slower than precomputed retrieval [S1]
- Figure: car service manual index, one page pulled into the window

### 7. Worked example and practice (O3, 1.5 min)
- Sort items for the booking request: keep, clear, save as note, retrieve [S1]

### 8. Summary (O3, 0.5 min)
- Window is working memory; notes and retrieval are storage [S2][S1]

### 9. Go further (O3, 0.5 min)
- Read the context engineering article [S1]

## Sources

- S1: Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- S2: Context windows, https://platform.claude.com/docs/en/build-with-claude/context-windows
