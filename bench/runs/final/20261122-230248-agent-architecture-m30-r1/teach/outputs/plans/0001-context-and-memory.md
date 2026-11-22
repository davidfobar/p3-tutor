# Plan: What the assistant sees and what it remembers

- Objective: O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Minutes: 30
- Win: Riley can say what goes in the makerspace assistant's context, what it saves between visits, and how it finds a manual page.
- Demo: 3: Add steps and manual pages to a context window and watch it fill and crowd out what matters.
- Next lesson: Token counts and cost per request; choosing between workflow and agent.

## Outline

### 1. Why the assistant must remember (O3, 2 min)
- The assistant answers from long manuals and must know each student's training status next visit.
- Like a car: the engine runs now, the logbook records past service.

### 2. Warm-up: the loop revisited (O3, 2.5 min)
- Recall the laser cutter Friday trace and its loop steps.
- Lead into what the model sees at step three.

### 3. The context window (O3, 5 min)
- Context is everything the model sees on a call: instructions, history, tool results. [S1]
- Context is a finite resource with diminishing returns; every token should earn its place. [S1]
- Misconception: more in context is always better -> recall of earlier content gets worse as context grows ("context rot"). [S1]
- Figure: A window as a bar filling across loop steps, with tool results as the biggest blocks.

### 4. Kept between steps, and between sessions (O3, 5 min)
- Between steps, the program resends history and tool results; the model itself holds nothing. [S1]
- Compaction: summarize near the limit and restart with the summary; clearing old tool results is a light form. [S1]
- Misconception: the model remembers the last visit -> a new session starts empty unless something is saved and reloaded. [S1]
- Figure: Two sessions side by side; the second starts empty unless a saved note is loaded, and compaction shrinks history into a summary.

### 5. Retrieval and notes as memory (O3, 5.5 min)
- Retrieval brings in only relevant pages on demand, not the whole manual. [S2]
- Just-in-time: keep lightweight references such as file paths, load details when needed; this is slower and needs guidance. [S1]
- Structured notes: the agent writes notes outside the window and reloads them later. [S1]
- Figure: Manual and notes file outside the window, with arrows loading chosen pieces in.

### 6. Worked example: a returning student (O3, 6 min)
- Design the context for "Can I book the 3D printer?" for a student whose training is saved.
- Decide per item: keep in context, save as note, or retrieve from the manual.
- Practice: Riley sorts five items and defends one choice.

### 7. Summary (O3, 2 min)
- Context is the working desk; notes and retrieval are the filing cabinet.

### 8. Go further (O3, 2 min)
- Read the context engineering article's sections on compaction and notes. [S1]

## Sources

- S1: Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- S2: Building effective agents, https://www.anthropic.com/engineering/building-effective-agents
