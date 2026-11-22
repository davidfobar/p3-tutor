# Riley sees the model requests tools and the program runs them, but not yet that loops need a stop

On quiz 0001 (second attempt, submission s2), Riley picked out the loop as what makes an agent, identified the model's output as a structured tool request, counted four model calls for a three-tool request, and explained that the tool result goes back as the model's next input.
Still open: Riley chose "it will eventually fix the bug" for a looping agent (M6, an agent needs no stopping condition), says tools are chosen "by the name" rather than by their whole descriptions, and in q4 wrote that the model "runs" the tools, which is loose wording around M4.

**Evidence:** quiz 0001, submission s2, items q1, q2, q4, q5 correct; q3 wrong (M6); q6 partial.

**Implications:** Before building on the loop, cover stopping conditions and tool descriptions, and check later that Riley says "requests" and not "runs" for the model.
