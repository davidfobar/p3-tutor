# Notes

## What the learner wants
- 2026-11-13: Wants to write their own AI agents for learning and research tasks (changed from "use agents"). See `MISSION.md`.
- Background (from PREFERENCES.md): first-year engineering student, learns hands-on first, relates to car examples.

## What they know
- Says they understand the agent loop (self-reported; see record 0003). Quiz 0001 shows it is partial: they know the tool round trip (q2) but counted tool runs as model calls (q5); see record 0005.
- Quiz 0001 (diagnostic, 3/6): has the tool round trip (O2), knows a research agent needs search and fetch (O4), and picks a workflow when the steps are fixed (O6).
- Not yet: the API is stateless and the conversation must be resent on every call (O1, M1, record 0004); one model call per reply, however many tools it asks for (O3); a citation holds up only if the page states the claim (O5, showed M5).
- Quiz 0002 (O1, 1/5, 2026-11-22): has max_tokens as a ceiling (q2). Not yet: key in the environment rather than the code (q1); replies saved and resent as assistant turns (q3, q5, M9; record 0006); reply.content is a list of blocks (q4, confused with stop_reason). M1 may be easing: did not pick it this time.
- Suggested first lesson: O1, one model call from code, with them resending the history themselves.
- Programming background: knows Python (stated 2026-11-13). Write build lessons in Python.

- 2026-11-13: asked how guardrails are placed on agents; got a chat overview (instructions, tool choice, checks in code before a tool runs, loop limits, checking output). Good material for the O2/O3 lessons.
- 2026-11-22: said they don't understand the limits of context windows; got a chat overview (what counts, hard limit, context rot, what to do) and a check question on fitting pages into a window, not yet answered. Understanding not yet shown. Build on it in O3/O4. Quiz 0002 is ungraded, so the example used one research request, not a growing chat (too close to its q3 and q5).

## Working notes
- Build objectives in order: (1) one model call from code; (2) a tool: define it, run it when asked, return the result; (3) the loop in code with a stop condition; (4) a research agent that searches, reads and cites; (5) testing it and checking its citations; (6) when to build a workflow instead.
- Before teaching API details, read current API docs (claude-api skill or official docs), not memory.

## Objective ids (from the build order above)
- O1: one model call from code. O2: a tool (define, run when asked, return the result). O3: the loop in code with a stop condition.
- O4: a research agent that searches, reads and cites. O5: testing it and checking its citations. O6: when to build a workflow instead.

## Misconception ids
- M1: the model API remembers earlier calls, so you need not resend the conversation.
- M2: the model provider runs a tool you defined in your own program.
- M3: once your program runs the tool, the turn is over; the result need not go back to the model.
- M4: a model can cite sources reliably from memory, without reading them.
- M5: a citation holds up if its link works or the site is reputable, without checking the page says the claim.
- M6: an agent is the better build even when the steps are fixed and known in advance.
- M7: the reply's content is the answer as a string (it is a list of blocks).
- M8: max_tokens sets the reply's length, so the model writes about that much (it is only a ceiling).
- M9: only the model can write "assistant" turns, so the history the program sends holds only user messages.

## Quizzes
- 2026-11-13: quiz 0001, a diagnostic across O1-O6 (one item each), given before any lesson.
- 2026-11-13: lesson 0001 (O1, one model call from Python, 15 min, hands-on demo with a stand-in for the API) and its quiz 0002 (5 items).
- 2026-11-22: quiz 0002 taken in chat (s2, 1/5), grades in `grades/0002-s2.json`. They asked for correct answers to be recorded for misses: submission left as given, answers stated in the feedback. Answers now seen, so recheck O1 with a new quiz.
