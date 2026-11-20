# Knows the tool round trip, but counts tool runs as model calls

This is partial evidence on the loop they said they understand (record 0003).
They know the program runs the tool and sends the result back to the model, but on a trace with three tools requested in one reply they counted 5 model calls (the tool runs) instead of 4 (one per reply).
The loop lesson (O3) should have them trace the calls one reply at a time, including a reply that asks for several tools at once, rather than skip the loop as already known.

**Evidence:** quiz 0001, submission s1, items q2 (correct) and q5 (answered 5).
