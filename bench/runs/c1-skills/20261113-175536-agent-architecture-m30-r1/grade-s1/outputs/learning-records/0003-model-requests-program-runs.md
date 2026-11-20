# The learner believes the model runs the tools itself (M4) and remembers across sessions (M3)

On quiz 0001 (submission s1) Riley chose the option where the model opens the booking system itself, and counted one model call for a three-tool run because "the model runs the 3 tools itself". Riley also wrote that the model "remembers on its own" earlier sessions. Riley does know that the model picks tools from their descriptions, and that a step limit stops a stuck loop.

**Evidence:** quiz 0001, submission s1, items q2, q4 and q6 (correct on q1 and q3).

**Implications:** Teach that the model only outputs a request and the program runs the tool and calls the model again, so each step is a separate model call. Teach it with a hands-on trace before the memory topic, since memory is also something the program puts back into the input. Submission s2 can show whether this has been fixed.
