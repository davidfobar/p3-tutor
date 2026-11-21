# Agent architecture Resources

## Knowledge

- [Docs: "How tool use works" (Claude Platform docs)](https://platform.claude.com/docs/agents-and-tools/tool-use/how-tool-use-works)
  Primary documentation of the tool-use contract: the model emits a structured request and the application runs the tool. Sections: "The tool-use contract", "The agentic loop (client tools)", "The server-side loop". Use for: who runs a tool, how results go back to the model, the loop and its stop conditions.
- [Article: "Building effective agents" (Anthropic)](https://www.anthropic.com/research/building-effective-agents)
  Defines agents versus workflows and describes agents as LLMs using tools based on environmental feedback in a loop. Section "Agents" (under "Building blocks, workflows, and agents") mentions stopping conditions such as a maximum number of iterations. Use for: choosing between a fixed workflow and an agent, and stopping conditions.
- [Docs: "Define tools" (Claude Platform docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
  Sections "Specifying client tools" and "Best practices for tool definitions": name, description and input schema, and why detailed descriptions matter. Use for: writing tool descriptions and how the model uses them.

## Wisdom (Communities)

None yet.
