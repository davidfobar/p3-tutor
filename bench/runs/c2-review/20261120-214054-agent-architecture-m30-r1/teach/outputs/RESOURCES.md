# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering, Sep 29, 2025)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on what goes in an agent's context, context rot, just-in-time retrieval, compaction, note-taking and sub-agents. Use for: anything about context and memory design.
- [Docs: Context windows (Claude Developer Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Defines the context window as the model's working memory, counting all input and output. Use for: what the window holds and why it fills up.
- [Docs: Memory tool (Claude Developer Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How file-based memory works: the model requests file operations, the application runs them and stores the files. Use for: what persists between sessions and who does the saving.

## Wisdom (Communities)

- None listed yet.

## Gaps

- A source on tokens and cost per request (needed for the budget constraint).
- A source on embedding-based retrieval over long documents (the manuals).
