# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite resource, context rot, compaction, note-taking and just-in-time retrieval. Use for: what to keep in context, what to save, how agents find information.
- [Docs: "Context windows" (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how turns accumulate, and trimming with compaction. Use for: context window facts and cost of long histories.
- [Docs: "Using the Messages API" (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
  Shows that the API is stateless and the full history is resent. Use for: what is kept between steps.
- [Docs: "Memory tool" (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side file memory across sessions and the multisession pattern. Use for: memory between sessions.
- [Article: "Contextual Retrieval" (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  RAG primer, chunking, embeddings plus BM25, and reported gains. Use for: finding the right page in a long manual.

## Wisdom (Communities)

None listed yet; no community was opened this session.

## Gaps

- A high-trust, moderated community for agent builders to test designs in.
- A sourced plain-language definition of a token and its link to cost, for the next lesson.
