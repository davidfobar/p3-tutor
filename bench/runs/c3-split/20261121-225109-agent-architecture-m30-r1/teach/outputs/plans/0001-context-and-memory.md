# Plan: Context and memory in an agent

Lesson number 0001 (`lessons/` is empty), slug `context-and-memory`. Learning records 0001 and 0002 exist, but they are not lessons.

## Objectives

- **O3:** "Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory."
- Requested length: 30 minutes (4,500 words at 150 per minute). No quiz was requested, so the lesson has no quiz minutes.

Core ideas (the handful the learner must get right):

- **C1. The context window.** It is everything the model is given for one call: system prompt, tool definitions, all messages, tool results and the model's own output. It is finite and measured in tokens. More in it is not better: accuracy and recall fall as it fills (context rot).
- **C2. Kept between steps.** The model keeps nothing between calls. The program resends the whole history every step, so the context grows with each tool result and each step costs more. Old tool results can be cleared, and a long history can be compacted into a summary.
- **C3. Kept between sessions: notes as memory.** When a session ends the context is gone. Only what the program saved survives. Memory is notes (files or a database) that the agent writes and the program stores, then reads back at the start of the next session. What to save is a design choice.
- **C4. Retrieval.** A manual too long or too costly to paste in every time stays outside the context. It is split into chunks and indexed, and only the best few chunks for this question are put into the context. The agent can do this through a search tool, just in time.
- **Not core this lesson:** sub-agents as a context tool (lesson on multi-agent systems), embeddings maths, prompt caching details, vector database choice.

## Where the learner starts

- **Knows (record 0001):** a model turns text in into text out, token by token. It knows only its training plus the text it is given, so "tools, context and memory all come down to what the model is given as input". This is the floor for O3.
- **Knows (record 0002):** the agent loop. The model asks for an action, the action runs, the result comes back, and this repeats. Riley traced "Is the laser cutter free on Friday?" on paper.
- **Not yet checked (record 0002, NOTES):** that every step is a separate model call, and that the program runs the tools. Quiz 0001 tests this, but it is ungraded (NOTES). C2 rests on this, so the lesson re-teaches it in a sentence and does not assume it.
- **Does not know (NOTES):** what a token or the context window limits, and why they affect cost. Never called a model from code. Has met no memory or retrieval.
- **Mission link:** the assistant must answer from long machine manuals and remember each student's training status between visits. Success item 3 is "decide what the assistant keeps in its context, what it saves between sessions, and how it finds the right page in a long manual". That is these three ideas, one each. The budget is small, so cost per request matters.
- **Preferences:** hands-on first and theory second, big picture then zoom in, a picture with each sentence, a short paragraph then a bulleted procedure, direct specific feedback, peer tone, cars as the example domain. This lesson is at most one-third car examples.

## Material

Primary source: Anthropic, "Effective context engineering for AI agents" (E). Others: Anthropic docs "Context windows" (CW), "Using the Messages API" (MA), "Memory tool" (MT), and Anthropic "Contextual Retrieval" (CR). All five were read for this plan.

### C1. The context window

- Context is "the set of tokens included when sampling from a large-language model". (E, "Context engineering vs. prompt engineering")
- The context window is all the text the model can reference when generating a response, including the response itself. It is a "working memory", different from the training corpus. (CW, "How the context window works")
- Everything in the request counts: the system prompt, every message including tool results, images and documents, and the tool definitions. The output the model generates counts too. (CW, "How the context window works")
- Size depends on the model. Many current models have up to 1M tokens. Others have 200k. (CW, "Context window sizes by model")
- A bigger window does not mean more is better: as token count grows, accuracy and recall degrade, called context rot. (CW, "How the context window works"; E, "Why it matters: context rot and the attention budget")
- The model has an "attention budget" and each new token draws it down. Degradation is gradual, not a cliff. (E, same section)
- The aim is "the smallest possible set of high-signal tokens" that makes the outcome likely. (E, "Anatomy of effective context")
- A token is a piece of text the model reads or writes (record 0001 mentions tokens). The lesson gives no token-to-word ratio, because none was sourced.

### C2. Kept between steps

- The Messages API is stateless: you always send the full conversational history. (MA, "Multiple conversational turns")
- Each turn's input is all previous history plus the new message. The output becomes part of the next turn's input. (CW, "How the context window works")
- Tool results go back as `tool_result` messages, so they join the history and count toward the window. (CW, same section; MT, "How it works")
- Tokens kept from earlier turns are billed as input tokens on later requests, "like the rest of the conversation history". (CW, "The context window with thinking")
- Caching changes what you pay for cached tokens, not whether they occupy the window. (CW, "Manage context with compaction")
- Context engineering repeats with every model call, since agents generate new data each turn. (E, "Context engineering vs. prompt engineering")
- Clearing old tool results is the lightest form of trimming. Compaction summarises a conversation near its limit and continues in a new window with the summary. Tune for recall first, then precision. (E, "Long-horizon tasks"; CW, "Manage context with compaction")
- In a chat interface, the app may manage the window itself, for example first in, first out. That is the product's doing, not the model's. (CW, footnote to the diagram)

### C3. Kept between sessions: notes as memory

- Nothing survives a new session unless the program stores it. Anthropic's memory tool "lets Claude store and retrieve information across conversations in a directory of memory files". (MT, intro)
- The memory tool is client-side: the model requests file operations (view, create, str_replace, insert, delete, rename), and the application runs them against storage the developer controls. (MT, "How it works")
- The model checks its memory directory before starting a task, saves what it learns under `/memories`, and reads it back later. (MT, "How it works")
- Structured note-taking (agentic memory) means the agent writes notes outside the context window and reloads them later. Examples are a to-do list and a NOTES.md file. (E, "Long-horizon tasks")
- Memory supports just-in-time retrieval: it keeps the active context focused on the current task instead of loading everything. (MT, intro)
- The multisession pattern: a progress log and a checklist written at the end of each session, read at the start of the next. (MT, "Multisession software development pattern")
- Memory expiration, size caps and keeping sensitive data out are the developer's job. (MT, "Security considerations")
- Memory pairs with compaction: compaction shrinks the active context, and memory keeps what must survive summarising. (MT, "Using with compaction")
- The context window is separate from the training data. Nothing written to memory changes the model. (CW, "How the context window works"; record 0001)

### C4. Retrieval

- Basic RAG: split the documents into small segments, turn each into a vector that captures meaning, store the vectors in a database that supports similarity search, and at query time find the closest segments and add them to the prompt. (CR, "A primer on RAG: scaling to larger knowledge bases")
- Under about 200,000 tokens (about 500 pages), Anthropic says you can skip RAG and put the whole knowledge base in the prompt. (CR, tip at the start). Context rot and cost still argue for selecting.
- Chunks can lose context. A chunk that does not say which company it concerns is hard to retrieve or use. (CR, "Introducing Contextual Retrieval")
- A stronger pipeline uses BM25 for exact-match search and embeddings for meaning, then merges the results. Adding context to each chunk cut the failure rate of finding the right chunk in the top 20 from 5.7% to 3.7%, and to 2.9% with BM25 added. These are Anthropic's own measurements. (CR, "Introducing Contextual Retrieval")
- Just-in-time retrieval: the agent keeps light references (file paths, queries, links) and loads content with tools at run time. File names, folders and timestamps help it judge relevance. (E, "Context retrieval and agentic search")
- The trade-off: run-time exploration is slower and needs guidance, so a hybrid works. Preload some context, then explore as needed. (E, same section)
- Retrieval results arrive as tool results, so they go back into the context (C2) and count against the window.

### Adaptable examples

- **Memory tool exchange (MT, "Example: How memory tool calls work"):** the model views `/memories`, the app returns the listing, the model views one file, the app returns it. Adapt it to a student's training-status file.
- **The context-window diagram (CW, "How the context window works"):** turns accumulate until the limit. Redraw it as an SVG for the makerspace loop.
- **Laser-cutter trace (record 0002):** reuse it as the running example for context growth. Booking-calendar and manual search results get added to the history.
- **RAG four steps (CR primer):** redraw as a pipeline figure.
- All numbers in a demo (token counts per step) are illustrative and labelled so. No source gives makerspace figures.

## Misconceptions

None is shown by this learner yet. Quiz 0001 is ungraded and there are no grades, so no evidence exists. M1 and M4 are likely, given the 0001 evidence that the learner uses chatbots, which seem to remember. The workspace has no earlier misconception ids, so M1 to M6 are new.

| Id | Wrong belief | Why tempting | Correcting fact and source | Shown by this learner? |
|---|---|---|---|---|
| M1 | The model itself remembers the conversation so far, so each step only needs the new message. | Chat apps feel continuous, and the loop in record 0002 reads like one ongoing thought. | The API is stateless: the program resends the full history on every call. (MA, "Multiple conversational turns"; CW, "How the context window works") | Not yet; check with Q3. Record 0002 notes "every step is a separate model call" is unchecked. |
| M2 | A bigger context window means you can put everything in, and more context is always better. | Window sizes sound huge (up to 1M tokens), and more information seems safer. | Accuracy and recall degrade as tokens grow (context rot), and the goal is the smallest set of high-signal tokens. Resent tokens are also billed as input every step. (CW, "How the context window works"; E, "Why it matters"; CW, "The context window with thinking") | Not yet; NOTES says the learner cannot say what the window limits or why it affects cost. |
| M3 | The context is just what the student typed, or just the conversation. | In chat the visible text is the user's message and the reply. | Everything counts: system prompt, tool definitions, every message including tool results, and the model's own output. (CW, "How the context window works") | Not yet; check with Q1. |
| M4 | Memory means the model learns from conversations, so it changes the model. | Chatbots say "I'll remember that". Record 0001 shows the learner sees the model as shaped by training. | The model's training is fixed. Memory here is files the program saves and loads into the next context. The memory tool is client-side. (MT, "How it works"; CW, "How the context window works") | Not yet; check with Q5. |
| M5 | Memory should save everything: keep the whole transcript and reload it next time. | It sounds safest and loses nothing. | Reloading it refills the window (M2) and costs tokens. Notes are curated: a progress log of what is done and what comes next, and the rest is dropped. Compaction keeps the essentials. (E, "Long-horizon tasks"; MT, "Multisession software development pattern") | Not yet; check with Q6. |
| M6 | Retrieval finds the page by matching the words typed, so the question must use the manual's own wording. Or the model has read the whole manual. | A search box works on keywords. "Retrieval" sounds like the model looking things up in everything it has seen. | Embeddings match by meaning and BM25 by exact words, and good pipelines use both. Only the few top chunks reach the model. A chunk alone can lose context. (CR, primer and "Introducing Contextual Retrieval") | Not yet; check with Q7. |

## Threads to earlier lessons

There are no earlier lessons (`lessons/` is empty, and there are no cheat sheets, quizzes or grades). The threads come from the learning records and the mission instead.

- **Record 0002, the loop:** the "Is the laser cutter free on Friday?" trace becomes the running example. The warm-up asks the learner to name the steps. Section 4 then shows that each loop pass is one more model call with a longer history.
- **Record 0001, the floor:** the model knows only its training plus the text it is given. C1 states it as "the window is that given text". M4's fix comes from the same floor.
- **Record 0001, implication:** tokens were "only in passing". C1 introduces them in one plain sentence and ties them to cost.
- **Mission, makerspace assistant:** the three running cases are the manual (retrieval), the booking calendar (a tool result that fills context), and each student's training status (memory between visits).
- **Warm-up retrieval questions:** (a) "Name the four things that happen in one pass of the agent loop." (b) "Why can a chatbot state an outdated fact confidently?" (record 0001). Both are recall, answers revealed on demand.

## Diagnostic questions

Not quiz items. The lesson uses them as practice checks, or the teach skill can swap in fresh questions.

1. **Q1 (M3).** "A student asks the assistant one short question. List everything that is in the context for the first model call." Right: system prompt, tool definitions, the question, and then the model's output once it is generated. Wrong: "just the question" or "the question and the manual".
2. **Q2 (M2).** "The model has a 1M-token window. Your manuals total about 300k tokens. Is pasting all of them into every request a good design? Give two reasons for or against." Right: no, because accuracy falls as the context fills (context rot) and the tokens are billed as input every call. Wrong: "yes, it fits, so nothing is lost".
3. **Q3 (M1).** "The assistant's loop makes 4 model calls for one booking request. On call 4, does the model receive the student's original question again? How do you know?" Right: yes, the program resends the whole history every call, since the API is stateless. Wrong: "no, it already has it from call 1".
4. **Q4 (M1, M2).** "A calendar tool returns 3,000 tokens on every step of a 6-step loop. Roughly how many tokens of calendar results does call 6 carry, and what could you do?" Right: call 6 carries the 5 earlier results, about 15,000 tokens, if none are cleared (a result joins the history only after its call, so the sixth first appears in call 7); clear old tool results or compact. Wrong: "3,000, only the latest". The demo uses the same convention: the bar at step n counts the results of steps 1 to n-1.
5. **Q5 (M4).** "A student finishes laser-cutter training on Monday. On Wednesday a new session starts. Where does the assistant learn that, and what makes it learn it?" Right: from a stored record the program loaded into the context, and the model itself learned nothing. Wrong: "the model remembers from Monday" or "it was trained on that".
6. **Q6 (M5).** "To remember a student, a teammate proposes saving the whole transcript of every visit and loading it all next time. Name two problems and say what to save instead." Right: it fills the window, costs tokens and buries the signal (context rot). Save a short curated record such as training status, equipment cleared and open issues. Wrong: "no problem, more memory is better".
7. **Q7 (M6).** "A student asks 'why does my cut come out burnt?' The manual's section is titled 'Power and speed settings for wood'. Will retrieval fail because the words differ? What if the question was about an error code 'E42'?" Right: meaning-based embeddings can link the two. Exact codes like E42 are what keyword matching (BM25) is for, so use both. Wrong: "it must contain the same words" or "the model reads the whole manual and finds it".

## Outline

- **The win:** By the end of this lesson you can explain what the makerspace assistant keeps in its context window, what it saves between sessions, and how it finds the right page in a long manual.
- **The mission tie:** Success item 3 in `MISSION.md` asks Riley to decide what the assistant keeps in context, what it saves between sessions and how it finds the right manual page, and this lesson builds that decision on a model of how each one works and what it costs.
- **Budget:** 30 min × 150 = 4,500 words; sections sum to 4,500.

| # | Section heading | Objective | Core idea | Misconception met | Example | Figure | Practice check | Words | Minutes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Opening: what the assistant must remember | O3 | - (frames C1 to C4) | - | The makerspace assistant and a student's Monday training, Wednesday visit (MISSION.md). | - | A prediction: "Where will the assistant keep a student's training status?" Answer on demand at once: "in a file the program saves and reloads next session; section 5 shows how". | 225 | 1.5 |
| 2 | Warm-up: the loop and the model's floor | O3 (recalls the earlier work in learning records 0001 and 0002; the workspace states no ids for them) | Recall for C1 to C2 | - | Laser-cutter trace (record 0002). | - | Two recall questions from the thread list, answers on demand. | 225 | 1.5 |
| 3 | The context window: everything the model sees in one call | O3 | C1 | M2, M3 | Car workbench analogy: only what is on the bench is in reach (the learner's brake-pad story, PREFERENCES.md). The manual's cost is shown with a first layout of the laser-cutter request. | Stacked bar of one call's context: system prompt, tools, history, tool results, output, with a limit line and a "rot" gradient near the limit. | Q1, then Q2. | 750 | 5 |
| 4 | Between steps: the program resends everything | O3 | C2 | M1 | Laser-cutter trace (record 0002) with a calendar result added each step. Illustrative token numbers. | Per step, the history bar grows; marks where clearing and compaction cut it. This is the demo's figure. | Q3, then Q4. | 750 | 5 |
| 5 | Between sessions: notes as memory | O3 | C3 | M4, M5 | Student training status file in `/memories`, using the memory tool exchange (MT) adapted. A car service logbook analogy (PREFERENCES.md), kept to one sentence. | Two sessions side by side with a notes file between them. The context empties at session end and the file survives. | Q5, then Q6. | 675 | 4.5 |
| 6 | Retrieval: finding the right page in a long manual | O3 | C4 | M6 | Makerspace manual question about a burnt cut and an error code (CR primer). A car service manual index analogy in one sentence. | Pipeline: manual to chunks to vectors and keyword index to top chunks to context. | Q7, then a short "what comes back" check with the pipeline. | 750 | 5 |
| 7 | Worked example, then your turn: design the assistant's memory | O3 | C1 to C4 together | - | Worked: one request, "Can I use the laser cutter Friday, and what power for 3 mm acrylic?", placing each item in context, memory or retrieval, with token costs (illustrative). Faded: the same for a new request, "Book the 3D printer and remind me what I still need for training". | The worked example is a three-column table (keep in context, save in memory, retrieve on demand). | The faded task, steps faded one by one, solution on demand. | 750 | 5 |
| 8 | Summary | O3 | C1 to C4 | - | The three-column table, compressed. | - | Prompt to explain in their own words where each of three things lives, with a model answer on demand. | 225 | 1.5 |
| 9 | Go further | O3 | - | - | The primary source (E) and two or three cited sources; the multi-agent lesson as the next step. | - | A choice: "which source answers your next design-review question?", with the answer in one line. | 150 | 1 |

Words sum: 225 + 225 + 750 + 750 + 675 + 750 + 750 + 225 + 150 = 4,500. Minutes sum: 1.5 + 1.5 + 5 + 5 + 4.5 + 5 + 5 + 1.5 + 1 = 30.

Example domain: the learner's car examples appear in sections 3, 5 and 6 (three of nine sections), each as one sentence. All other sections use the makerspace assistant.

- **The demo slot:** Section 4, under its own heading. It lets the learner see C2 and M1: step through the laser-cutter loop and watch a "tokens sent this call" bar grow with every step, because the whole history is resent. They can toggle "clear old tool results" and "compact" to see the bar drop, and a running "total tokens billed" counter shows why cost grows faster than the number of steps. Reserve 150 visible words for it inside the section's 750. The numbers are illustrative and labelled so. The demo-dev subagent builds the demo and every figure in the Figure column (sections 3 to 7).
- **Sources per section:**
  - 1 Opening: none beyond the mission.
  - 2 Warm-up: records 0001 and 0002.
  - 3: CW "How the context window works", "Context window sizes by model" and "The context window with thinking" (billing); E "Why it matters: context rot and the attention budget" and "Anatomy of effective context".
  - 4: MA "Multiple conversational turns"; CW "How the context window works", "The context window with thinking" (billing) and "Manage context with compaction"; E "Long-horizon tasks".
  - 5: CW "How the context window works" (the window is separate from training); MT intro, "How it works", "Multisession software development pattern", "Security considerations" and "Using with compaction"; E "Long-horizon tasks" (structured note-taking).
  - 6: CR "A primer on RAG" and "Introducing Contextual Retrieval"; E "Context retrieval and agentic search".
  - 7: all of the above, for the facts it reuses.
  - 8: no new facts.
  - 9: E as the primary source; CW, MT and CR as the others.
- **If the objective does not fit:** it fits as scoped. The core is the four ideas above. Left for later lessons: sub-agents as a context tool (the multi-agent lesson), writing the retrieval index in code, and prompt caching. If the lesson runs long, shorten section 7's faded task rather than any core idea.

## Sources

- Anthropic Engineering, "Effective context engineering for AI agents", https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (primary source; read)
- Anthropic docs, "Context windows", https://platform.claude.com/docs/en/build-with-claude/context-windows (read)
- Anthropic docs, "Using the Messages API", https://platform.claude.com/docs/en/build-with-claude/working-with-messages (read)
- Anthropic docs, "Memory tool", https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (read)
- Anthropic Engineering, "Contextual Retrieval", https://www.anthropic.com/engineering/contextual-retrieval (read)
