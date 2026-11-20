# Plan: One model call from Python

## Objectives

- **O1: one model call from code.** Mission wording: "Write a program that calls a language model and uses its reply."
- Core:
  1. Setup: install the `anthropic` SDK; the SDK reads the key from the `ANTHROPIC_API_KEY` environment variable, so the key never sits in the script.
  2. The call: `client.messages.create(model=..., max_tokens=..., messages=[...])`; `messages` is a list of `{"role", "content"}` dicts.
  3. The reply: a Message object; the text is in `message.content`, a list of blocks, each with a `type` (take the `"text"` blocks); plus `stop_reason` and `usage`.
  4. Stateless: each call stands alone; to continue a conversation, the program appends the model's reply as an `"assistant"` turn and the new `"user"` turn, and sends the whole list again.
  5. `max_tokens` is a ceiling, not a target; a reply cut off shows `stop_reason == "max_tokens"`.
- Length: none requested, PREFERENCES.md implies none: 15 minutes (~2,250 visible words). Say they can ask for longer.

## Where the learner starts

- Knows Python (NOTES.md). First-year engineering student; car examples; hands-on first; short paragraph for the why, then bullets for procedures.
- Has shown: the tool round trip (quiz 0001 q2), research agent needs search + fetch (q3), workflow vs agent (q4).
- Has not shown: statelessness (q1 chose c, M1, record 0004); counts tool runs as model calls (q5, record 0005), which rests on "one call = one reply", a core idea here.
- Unknown: whether they have an API key or a Python venv set up. The demo should work with or without a key (offer a no-key path).

## Material

- **Install and key.** Venv, then `pip install anthropic`; set the key with `export ANTHROPIC_API_KEY="your-api-key-here"`; "The SDKs and CLI read your key from `ANTHROPIC_API_KEY`". Source: Get started with Claude, "Before you begin" and "Call the API" (Python tab: "Create a project and install the SDK", "Create your code", "Run your code").
- **Minimal call.** `client = anthropic.Anthropic()`, then `client.messages.create(model=..., max_tokens=1000, messages=[{"role": "user", "content": "..."}])`, then loop `for block in message.content: if block.type == "text": print(block.text)`. Source: Get started with Claude, "Call the API".
- **Required parameters.** `model`, `max_tokens`, `messages` are the ones not marked optional in the reference. Source: Messages API reference (body parameters). Teach as "the three you always pass".
- **Response shape.** Example: `id`, `type: "message"`, `role: "assistant"`, `content: [{"type": "text", "text": "Hello!"}]`, `model`, `stop_reason: "end_turn"`, `stop_sequence`, `usage: {input_tokens: 12, output_tokens: 6}`. Source: Using the Messages API, "Basic request and response". Adaptable as a labelled figure.
- **Stateless.** Verbatim: "The Messages API is stateless, which means that you always send the full conversational history to the API." Source: Using the Messages API, "Multiple conversational turns". Its example list: user "Hello, Claude" / assistant "Hello!" / user "Can you describe LLMs to me?". Adapt to a car example.
- **Alternating turns.** "Our models are trained to operate on alternating `user` and `assistant` conversational turns"; consecutive same-role turns are combined into one. Source: Messages API reference.
- **max_tokens.** "The maximum number of tokens to generate before stopping." and "only specifies the absolute maximum number of tokens to generate." Source: Messages API reference. `stop_reason` values verified: `"end_turn"`, `"max_tokens"` (Using the Messages API). Mention `"tool_use"` only as a forward thread (seen on the tool use page, "How tool use works").
- **System prompt.** Top-level `system` parameter, not a message in the list. Source: Messages API reference. Mention briefly only.
- **Model ids.** `claude-haiku-5-5` (cheapest, fine for practice), `claude-sonnet-5-5`, `claude-opus-5-5`. Source: Models overview, comparison table "Claude API ID". The docs' examples use `claude-opus-5-5`; the lesson can use `claude-haiku-5-5` to keep practice cheap.

## Misconceptions

- **M1 (shown: grades 0001-s1, q1; record 0004).** The API remembers earlier calls (by key or session). Tempting: chat apps feel continuous. Fix: the API is stateless; the app resends the history (Using the Messages API, "Multiple conversational turns").
- **M7 (new).** `message.content` is the reply as a string. Tempting: in the request, `content` is a string. Fix: in the response it is a list of typed blocks; take `block.text` from blocks with `type == "text"` (Get started; Using the Messages API, "Basic request and response").
- **M8 (new).** `max_tokens` sets the length of the reply, so the model writes about that much. Tempting: the name sounds like a target. Fix: it is a ceiling; replies usually stop earlier with `end_turn`, and hitting it cuts the reply off with `stop_reason "max_tokens"` (Messages API reference).
- **M9 (new).** Only the model can write `"assistant"` turns, so the history the program sends contains only user messages. Tempting: "assistant" sounds like the model's territory. Fix: the program writes the model's earlier replies into the list as `"assistant"` turns itself, alternating with user turns (Using the Messages API, "Multiple conversational turns"; reference on alternation).

## Threads to earlier lessons

- No earlier lessons. Threads from quiz 0001: q1 used "Explain how a torque converter works" then "Make it shorter"; the lesson can pick that exact scenario up and now run it in code (without revealing the quiz key beyond what the grade feedback already said).
- Thread forward: q5's "one model call per reply" becomes concrete here: count calls in the multi-turn example; the tool loop (O2, O3) later appends `tool_result` turns the same way.
- Warm-up retrieval: from the grade feedback, "what does your program send back after running a tool?" (q2, which they got right), so the lesson starts from strength and links to "the program carries the conversation".
- Analogy (car): a service counter with no records: every visit you bring the full work order and repair history, or the mechanic starts from zero.

## Diagnostic questions

- **M1.** "Second call sends only `[{'role':'user','content':'Make it shorter'}]`. What does the model reply about?" Right: it has no idea what "it" is; asks or guesses. Wrong: shortens the torque converter answer.
- **M1.** "Count the dicts in `messages` on the 3rd call of a chat where each call adds one exchange." Right: 5 (u, a, u, a, u). Wrong: 1.
- **M7.** "`print(message.content)` shows what?" Right: a list of block objects. Wrong: just the reply text.
- **M8.** "max_tokens=1000 and the question is 'What's 2+2?' How long is the reply?" Right: a few tokens, stop_reason end_turn. Wrong: ~1000 tokens.
- **M8.** "Reply ends mid-sentence; what do you check?" Right: stop_reason == "max_tokens". Wrong: retry / model broke.
- **M9.** "To ask a follow-up, which role do you give the model's earlier reply in your list?" Right: "assistant". Wrong: leave it out / "user".

## Sources

- Primary: [Get started with Claude](https://platform.claude.com/docs/en/get-started): "Before you begin", "Call the API".
- [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages): "Basic request and response", "Multiple conversational turns".
- [Messages API reference](https://platform.claude.com/docs/en/api/messages): parameters `model`, `max_tokens`, `messages`, `system`; alternation.
- [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview): model ids.
- [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview): "How tool use works" (forward thread only).
