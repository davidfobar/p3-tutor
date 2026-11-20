# AI Agents Resources

## Knowledge

- [Article: "Building effective agents" (Anthropic Engineering, Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents)
  Defines agents vs workflows, names the common workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) and the agent loop. Use for: core definitions and when an agent is worth its cost. The page notes some tooling has changed since publication.

- [Docs: "Tool use with Claude" (Anthropic, Claude platform docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
  Official reference for giving Claude tools: client tools run in your application, Claude signals stop_reason "tool_use", and your code sends a tool_result back in a new request. Use for: the tool round trip (O2) and, through its code example, how the messages list is resent on every call (O1).

- [Docs: "Get started with Claude" (Anthropic, Claude platform docs)](https://platform.claude.com/docs/en/get-started)
  The official quickstart: install the Python SDK, set ANTHROPIC_API_KEY, make a first messages.create call and print the text blocks. Use for: the first model call from code (O1).
- [Docs: "Using the Messages API" (Anthropic, Claude platform docs)](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
  The request and response shapes and multi-turn conversations; states that the API is stateless. Use for: response fields and resending the history (O1).
- [Docs: "Messages" API reference (Anthropic)](https://platform.claude.com/docs/en/api/messages)
  Every parameter of messages.create (model, max_tokens, messages, system) and the response fields. Use for: exact parameter meanings; it is very long, so search it.
- [Docs: "Models overview" (Anthropic)](https://platform.claude.com/docs/en/about-claude/models/overview)
  Current model ids and how they compare. Use for: picking the model string to pass.

## Gaps
- A hands-on, build-it-yourself source for a first small agent.
- A source on checking an agent's citations: that the cited page actually states the claim (O5).
