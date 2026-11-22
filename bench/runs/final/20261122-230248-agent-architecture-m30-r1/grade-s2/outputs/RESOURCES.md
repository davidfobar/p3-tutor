# Agent architecture Resources

## Knowledge

- [Article: "Building effective agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/building-effective-agents)
  Primary source on what an agent is, workflows versus agents, and when to use each. Use for: the agent loop (section "Agents"), stopping conditions such as a maximum number of iterations, and workflow-versus-agent decisions.
- [Docs: "Define tools" (Claude API docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
  Official reference on tool definitions. Use for: what a tool definition holds (name, description, input schema), how to write descriptions the model can choose from ("Best practices for tool definitions"), and what the model outputs when it uses a tool ("Model responses with tools").

- [Docs: "Handle tool calls" (Claude API docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)
  Official steps for what the program does when the model requests a tool. Use for: the program running the tool, sending the result back as a tool_result, and repeating the loop (section "Handling results from client tools").

## Wisdom (Communities)

## Gaps

- No community source chosen yet.
- No source read yet on context windows, tokens and cost, memory, or retrieval (needed for the next mission step).
