# Visuals review, lesson 0001

Findings (2):
- Demo, correctness (V3): STORY_ON[1] said the calendar result is resent at call 2, but it first arrives then; the resend is of the request. Changed the text to "The request is resent, and the calendar result (1,200 tokens) arrives with it. The model asks to book."
- Demo, works (V5): draw() put the messages segment at x = 20 + 400 * SCALE (100), over the tools block. Changed it to 20 + FIXED * SCALE (220), which matches the layout check.

Declined: none.
Layout (V1), consistency (V2), outline (V4): no findings.
Figures not accepted: none (both accepted).
