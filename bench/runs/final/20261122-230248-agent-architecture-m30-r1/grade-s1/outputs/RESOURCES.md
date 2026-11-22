# Agent architecture Resources

## Knowledge

- [Docs: "How tool use works" (Anthropic)](https://platform.claude.com/docs/agents-and-tools/tool-use/how-tool-use-works)
  Primary documentation on the tool-use contract, who runs a tool, and the agentic loop for client tools. Use for: what the model outputs when it calls a tool, what the program does with the result, why the model never sees a tool's code.
- [Docs: "Define tools" (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
  Primary documentation on tool definitions: name, description and input schema. Use for: how the model picks a tool from its description, and how to write a good tool description ("Best practices for tool definitions").
- [Article: "Building effective agents" (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)
  Essay on agents as models using tools in a loop, and on workflows versus agents. Use for: the definition of an agent, stopping conditions such as a maximum number of iterations, and later the workflow-versus-agent decision.

## Wisdom (Communities)

None chosen yet.

## Gaps

- A source on context windows, tokens and memory, needed for the next topic.
