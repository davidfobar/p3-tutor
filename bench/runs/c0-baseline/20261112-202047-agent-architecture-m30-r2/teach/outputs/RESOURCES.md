# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on what goes into an agent's context: attention budget, compaction, structured note-taking, just-in-time retrieval, sub-agents. Use for: any decision about context, memory and cost.
- [Docs: "Context windows" (Claude docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official description of the context window as working memory and how input and output count. Use for: current window sizes and limit behaviour.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al., 2024)](https://huggingface.co/papers/2307.03172)
  Shows accuracy falls when relevant text is in the middle of a long input. Use for: arguing against stuffing the context.

## Wisdom (Communities)

- Local: the makerspace staff who answer students' questions today
  Use for: a real test set of questions for the retrieval tool.

## Gaps

- A high-trust, moderated community for agent builders; to find in a later lesson.
- A source on retrieval methods (chunking, keyword versus meaning-based search) for the next lesson on finding the right page.
