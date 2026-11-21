# Plan: Context and memory in an agent

## Objectives
- O3: "Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory."
- Length: 10 min reading (about 1,500 words), plus demo and quiz time.
- Core:
  1. Context window = everything the model sees on one call (system prompt, tool definitions, message history, tool results, its own output); limited, and billed per token.
  2. Between steps: the program re-sends the growing history on each call; context grows with every loop turn.
  3. Bigger is not free or better: cost grows and recall degrades (context rot); trim, clear old tool results, or compact.
  4. Between sessions: nothing persists unless the program saves it; notes written by the agent and read back are memory.
  5. Retrieval: fetch only the relevant manual page into context instead of loading the whole manual.

## Where the learner starts
- Knows: model = text in, text out (record 0001); agent loop (record 0002).
- Not shown: tokens, what the context window limits, why it affects cost; whether each step is a separate model call (quiz 0001, ungraded).
- Style: hands-on first, big picture then zoom in, car examples, short paragraph then bullet procedure, peer tone.
- Mission link: the makerspace assistant answers from long manuals and remembers each student's training status.

## Material
- Context is "the set of tokens included when sampling from a large-language model" (Anthropic, Effective context engineering, intro).
- Context window = "all the text a language model can reference when generating a response, including the response itself"; a "working memory" (Claude docs, Context windows, "How the context window works").
- Each turn's input holds all previous history plus the new message; the output becomes part of the next input (same section). System prompt, messages, tool results, tool definitions and output all count.
- An agent in a loop "generates more and more data that could be relevant for the next turn", which must be cyclically refined (Anthropic post, "Context engineering vs. prompt engineering").
- Context rot: as tokens grow, recall degrades; "more context isn't automatically better" (Claude docs; Anthropic post, "Why context engineering is important": finite attention budget, a gradient not a cliff).
- Guiding principle: smallest possible set of high-signal tokens (Anthropic post, "The anatomy of effective context").
- Compaction: summarize a conversation nearing the limit and start a new window with the summary; clearing old tool results is the lightest form (Anthropic post, "Compaction"; Claude docs, "Manage context with compaction").
- Notes as memory: the agent "regularly writes notes persisted to memory outside of the context window", pulled back later; example: Claude playing Pokémon keeping tallies (Anthropic post, "Structured note-taking").
- Retrieval: up-front embedding retrieval versus just-in-time (keep lightweight identifiers such as file paths or queries, load on demand); hybrids exist (Anthropic post, "Context retrieval and agentic search").
- Augmented LLM = model plus retrieval, tools and memory; often one call with retrieval is enough (Building effective agents, "Building block: The augmented LLM").
- Window sizes differ by model (1M or 200k in the docs); overflow gives an error or stop reason (Claude docs). Do not cite one size as universal.
- Statelessness: the docs imply the client resends history but never say "stateless"; say "the program sends the history on each call".
- Car analogy: window = what is on the dashboard and in front of you now; notes = the service logbook in the garage; retrieval = opening one page of the repair manual rather than carrying the shelf.

## Misconceptions
- M3 (new): The model remembers earlier steps and earlier chats by itself. Tempting because chatbots feel continuous. Fix: each call sees only what the program sends (Claude docs). Not yet shown by the learner.
- M4 (new): A bigger window means everything in it is used well. Tempting because "fits" sounds like "uses". Fix: context rot and cost (Claude docs; Anthropic post).
- M5 (new): To answer from a long manual, put the whole manual in context. Tempting: simplest. Fix: costs tokens every step and degrades recall; retrieve the relevant page (Anthropic post).
- M6 (new): Memory between sessions is automatic or lives in the model. Fix: only what the program saves and reloads persists (Anthropic post, structured note-taking).

## Threads to earlier lessons
- No earlier lessons exist. Build on learning records 0001 (the model knows training plus the text it is given) and 0002 (the loop; the "Is the laser cutter free on Friday?" trace).
- Warm-up recall: (a) what the model itself outputs when it wants a tool; (b) what a model knows besides the text it is given.
- Extend the Friday laser-cutter trace by showing what is in context at each step.

## Diagnostic questions
- M3: A student chats Monday and returns Tuesday; with no extra code, does the assistant know Monday's chat? Right: no. Wrong: yes.
- M3: In step 3 of the loop, how does the model know step 2's result? Right: the program includes it in the input. Wrong: it remembers.
- M4: A 200k window holds a 150k-token manual; is recall of a torque value guaranteed? Right: no, context rot and cost. Wrong: yes, it fits.
- M5: Manuals total 3 million tokens; best design? Right: retrieve relevant pages. Wrong: use a bigger model.
- M6: What must the program do so the assistant knows a student passed laser training? Right: write it to a store and load it into context. Wrong: nothing.

## Sources
- https://www.anthropic.com/research/effective-context-engineering-for-ai-agents (primary; read)
- https://platform.claude.com/docs/en/build-with-claude/context-windows (read)
- https://www.anthropic.com/research/building-effective-agents (search result only; cited for the augmented-LLM sentence)
