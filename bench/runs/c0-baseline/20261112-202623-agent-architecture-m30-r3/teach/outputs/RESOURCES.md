# Agent Architecture Resources

## Knowledge

- [Anthropic: Effective context engineering for AI agents](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite budget, context rot, just-in-time retrieval, compaction, note-taking, sub-agents. Use for: what to keep in context and how to keep it small.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How the window fills turn by turn and what counts toward it. Use for: exact behavior of the window and token accounting.
- [Anthropic: Contextual Retrieval](https://anthropic.com/research/contextual-retrieval)
  Chunking with added context, embeddings plus keyword search, reranking. Use for: designing the manual search.
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
  The augmented LLM (retrieval, tools, memory), workflows versus agents. Use for: architecture choices and the workflow-versus-agent lesson.

## Wisdom (Communities)

- [Anthropic community page](https://www.claude.com/community)
  Lists a developer Discord. Use for: asking how others handle memory and chunking.

## Gaps

- A beginner-level, hands-on source for calling a model from Python (Riley has not done it yet).
