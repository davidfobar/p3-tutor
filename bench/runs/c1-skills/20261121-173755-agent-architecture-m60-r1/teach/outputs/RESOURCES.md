# Agent architecture Resources

## Knowledge

- [Anthropic Engineering: "Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite budget, context rot, compaction, note-taking, sub-agents, just-in-time retrieval. Use for: what to keep in context and how long tasks survive.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What the window holds, how history accumulates each turn, overflow, compaction. Use for: how context grows and what it costs.
- [Claude docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based memory that lives outside the window, handled by your code, with security notes. Use for: saving things between sessions.
- [Anthropic Engineering: "Contextual Retrieval"](https://www.anthropic.com/engineering/contextual-retrieval)
  RAG basics, embeddings versus BM25, chunks that lose context, measured failure rates. Use for: finding the right page in a long manual.

## Wisdom (Communities)

None chosen yet.

## Gaps

- A community where students building small agents compare designs.
