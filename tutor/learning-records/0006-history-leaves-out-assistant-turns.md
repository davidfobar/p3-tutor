# Leaves the model's replies out of the history as assistant turns

On quiz 0002 the learner filed the model's answer as a "user" turn and counted 30 input tokens for a third call, which matches the questions without the replies (M9).
They no longer chose "the API already holds it", so M1 (record 0004) may be easing, but they can't yet build the history correctly, and O3's loop depends on that.

**Evidence:** quiz 0002, submission s2, items q3 (a) and q5 (30); 1 of 5 overall, with q2 (max_tokens is a ceiling) correct.

**Implications:** before O2 or O3, have them build and print a messages list by hand, then check with a new O1 quiz; quiz 0002's answers have been shown.
