# Plan: Context and Memory in the Makerspace Assistant

- Objective: O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
- Minutes: 60
- Win: Riley can decide what the makerspace assistant keeps in context, saves between sessions, and retrieves from a long manual, with a reason for each.
- Demo: 4: Watch a context window fill as an agent loop adds each step, and see what compaction or clearing frees.
- Next lesson: Sub-agents with clean contexts, and a cost-per-request budget for the assistant.

## Outline

### 1. Why the assistant needs a memory (O3, 3 min)
- The assistant must answer from long manuals and recall each student's training status between visits.
- Preview: what is in view now, what is carried forward, what is looked up.

### 2. Warm-up: the loop you already know (O3, 4 min)
- Recall from record 0002: action, result back, repeat; each result must go somewhere.
- Recall from record 0001: the model only sees text handed to it, nothing else.
- Misconception: the model remembers past chats -> nothing persists unless the program sends it again. [S2]

### 3. The context window (O3, 9 min)
- The context window is all the text the model can see when answering, its own reply included. [S2]
- Everything counts: system prompt, every message, tool results, documents, and tool definitions. [S2]
- A token is a chunk of text; limit and cost are both counted in tokens; windows reach up to 1M. [S2]
- Context rot: as tokens grow, recall and accuracy fall gradually, not at a cliff. [S1][S2]
- Figure: Context window as a fuel tank bar filling across loop steps, with segments for system prompt, tool definitions, messages, tool results.

### 4. What is kept between steps (O3, 9 min)
- Each turn, all previous history plus the new message is the input; the output joins the next input. [S2]
- So each tool result stays and grows the token count, which raises cost per step. [S2]
- Clearing old tool results is the lightest fix; compaction summarizes near the limit and restarts with the summary. [S1][S2]
- Misconception: a bigger window means keep everything -> curate; irrelevant text dilutes recall. [S1]

### 5. What is kept between sessions: notes as memory (O3, 9 min)
- A new session starts with an empty window; only what was saved outside it can return. [S2]
- Structured note-taking: the agent writes notes outside the window, such as NOTES.md or a to-do list, and reads them later. [S1]
- Example: an agent tracked progress across more than 1,000 steps using notes. [S1]
- Design state so recovery is fast when a new session starts. [S2]

### 6. Retrieval: finding the right page (O3, 9 min)
- Up-front retrieval surfaces relevant text before the model answers, often with embeddings. [S1]
- Just-in-time retrieval keeps light identifiers, such as file paths or queries, and loads data with tools when needed. [S1]
- Just-in-time is slower and needs good tools; a hybrid loads some context up front and searches on demand. [S1]
- Misconception: paste the whole manual into the prompt -> retrieve only the pages needed, for recall and cost. [S1][S2]
- Figure: Two paths from question to answer: up-front retrieval fills the window first; just-in-time has the model call a search tool in the loop.

### 7. Worked example: the makerspace assistant (O3, 11 min)
- Riley sorts a real request, "Can I book the laser cutter Friday?", into kept in context, saved as notes, and retrieved.
- Practice: decide where training status, the manual, and the booking result live, with a reason each.
- Practice: choose up-front, just-in-time, or hybrid retrieval for the manuals.
- Figure: Three-lane sketch (context, notes, manual store) with arrows for one request.

### 8. Summary (O3, 3 min)
- Context is limited working memory; notes carry across sessions; retrieval brings in only what is needed.

### 9. Go further (O3, 3 min)
- Read the context engineering article, then the memory tool and compaction pages. [S1][S2]

## Sources

- S1: Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- S2: Context windows, https://platform.claude.com/docs/en/build-with-claude/context-windows
