# Cheat sheet: context and memory in an agent

Sources: [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), [Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool).

## Definitions
- **Context window**: all the text the model can reference when it writes a reply, including the reply. Working memory, not training data.
- **Counts toward it**: system prompt, tool definitions, every message including tool results, and the output.
- **Token**: a chunk of text, often a word or part of a word; the window's size is measured in tokens.
- **Context rot**: recall of information in the window gets worse as the window fills; a gradient, not a cliff.
- **Retrieval**: fetch the right piece of a big store and put only that in the window.
- **Notes (agentic memory)**: files outside the window that the agent writes and later reads back.

## Where information lives
| Kind | Lives in | Example |
|---|---|---|
| Needed now, small, ends with the session | Window | Today's chat |
| Must outlive the session, small | Notes file, loaded at start | Training status |
| Large, one piece at a time | Looked up on demand | Machine manuals |

## Procedure: decide where an item goes
- How long must it live? One session: window. Longer: saved file.
- How big is it? Large: look it up, one piece at a time.
- Does it change often? Fetch it live with a tool.

## Rules to remember
- Each model call is sent the whole window again; the model keeps no state of its own.
- A new session starts empty unless the program saves and reloads something.
- The program runs retrieval and the file operations; the model only asks.
- Saving a note does not change the model.
- Put in the smallest set of high-signal text.
