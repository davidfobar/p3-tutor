# Visuals review record, lesson 0001

One pass by product-reviewer, 4 findings. No figure was rejected.

## Findings and changes

1. Demo, layout (V1): in the starting state the drawing left empty bands over 40 units in a 640 x 440 frame. Changed: added a dotted reach circle (the most the hand can reach) as always-drawn content, set the viewBox to 640 x 360 with joint 1 at (320,180), scaled the arm (70 per unit) and arrows (28 per unit/s) so every mark stays within 168 of joint 1, and redid the initial and fullest rows of the layout check from real poses.
2. Demo, shows the outline (V4): the hand never moved, so the learner could not check a column by moving one joint. Changed: added "Nudge joint 1/2 by +0.15 rad" toggle buttons that draw a dashed ghost hand and read out the real hand displacement beside 0.15 x the column; prompt 1 now asks about the ghost hand.
3. Demo, legend (V4): the red dashed wrong-arm arrow had no legend entry. Changed: added "Wrong: link 1 only" and renamed the muted entry "Grey dashed: arm, joint 1 to hand"; prompt 3 now says "grey dashed arm".
4. Demo, works (V5): arrows shorter than 10 units vanished while the readout showed nonzero values. Changed: an arrow is now hidden only when its rate is 0; when it is too short to draw (under 8 units), the readout line says "[arrow too short to draw]".

## Declined

None.

## Figures not accepted

None. Figures 1 and 2 had no findings.
