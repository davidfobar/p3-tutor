# Agent architecture Resources

## Knowledge

- [Docs: "How tool use works" (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
  Official explanation of the tool-use contract, where tools run, and the agentic loop. Use for: who runs a tool, what the model outputs, how the loop repeats and exits, what the model receives about a tool.
- [Docs: "Define tools" (Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
  Official guide to tool schemas (name, description, input schema) and how to write descriptions. Use for: what the model is given about each tool and how to write a good tool description.

## Gaps

- No source yet for stopping conditions such as step limits, or for memory between sessions.
