# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering, Sep 2025)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite resource, context rot, just-in-time retrieval, compaction, note-taking, sub-agents. Use for: what to keep in context, retrieval, notes as memory.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how it grows each turn, overflow, usage and caching. Use for: tokens, window size, cost per step.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A file-based memory the application stores and the model reads and writes through tool calls. Use for: what is saved between sessions and how, and its risks.

## Wisdom (Communities)

- None chosen yet.

## Gaps

- A source on retrieval over long documents (chunking, embeddings, search) for the machine manuals.
