# Plan: What the assistant sees and remembers

- Objective: O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Minutes: 10
- Win: Riley can say what the assistant holds in context each step, what it saves between visits, and how it finds a manual page.
- Demo: 3: Step through a booking request and watch context, tokens and cost grow each step.
- Next lesson: Compaction and sub-agents in depth; workflow versus agent.

## Outline

### 1. Why the assistant must forget and remember (O3, 0.5 min)
- Ties to mission: long manuals, training status, small budget

### 2. Warm-up: the loop you traced (O3, 1 min)
- Recall the Friday laser cutter trace; each step is a separate model call [S2]

### 3. The context window (O3, 2.5 min)
- Context is all text the model can reference, including its response: working memory [S2]
- Counts: system prompt, messages, tool results, tool definitions [S2]
- Misconception: the model remembers earlier steps -> it sees only what is resent each call [S2]
- Each call resends history as input tokens, so long tool results are billed again every later step [S2]
- Figure: fuel-tank bar filling across steps, segments for prompt, tools, results

### 4. Kept between steps and between sessions (O3, 1.5 min)
- Within a session, previous turns are preserved completely and resent [S2]
- A new session starts empty unless something is saved outside the window [S1]
- Compaction: summarize a nearly full context and restart with the summary [S1]

### 5. Retrieval and notes as memory (O3, 1.5 min)
- Just-in-time retrieval: keep references, load the manual page with a tool when needed [S1]
- Structured notes: the agent writes notes outside the window and reloads them later [S1]
- Figure: car analogy: manual on shelf, notes card on dash, window as dashboard

### 6. Worked example and practice (O3, 2 min)
- Decide for the makerspace assistant what stays in context, what is saved, what is retrieved

### 7. Summary (O3, 0.5 min)
- The window is working memory; notes and retrieval are storage [S1]

### 8. Go further (O3, 0.5 min)
- Context rot: more tokens, worse recall [S1]; sub-agents with clean windows [S1]

## Sources

- S1: Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- S2: Context windows, https://platform.claude.com/docs/en/build-with-claude/context-windows
