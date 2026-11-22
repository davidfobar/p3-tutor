# Riley holds the loop and stopping condition but not who runs tools or that memory is not automatic

Riley recognised the agent loop as what makes a system an agent and chose a step limit as the safeguard against a repeating agent. Riley also knows the model picks a tool from its name and description. Still open: Riley believes the model runs the tools itself (M4), so counted one model call for a three-tool request, and believes the model remembers earlier sessions on its own (M3).

**Evidence:** quiz 0001, submission s1, items q1, q3, q6 (understood) and q2, q4, q6 (misconceptions).

**Implications:** Before context and memory, re-teach that the program runs each tool and that every step is a separate model call. Memory is the next topic, and M3 needs correcting there: the model sees only what the program sends on each call.
