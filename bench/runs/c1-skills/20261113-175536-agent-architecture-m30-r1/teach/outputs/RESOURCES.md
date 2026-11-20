# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context, attention budget, just-in-time retrieval, compaction, note-taking, sub-agents. Use for: what to keep in context and what to save outside it.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How tokens accumulate over turns, what counts, overflow. Use for: exact behavior of the window.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based, client-side memory across sessions. Use for: how notes between sessions work.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://anthropic.com/research/contextual-retrieval)
  Chunks, embeddings, BM25, when to skip retrieval. Use for: finding the right page in a long manual.

## Wisdom (Communities)

## Gaps
- No community vetted yet for testing agent designs.
