# Visuals review record, lesson 0001

One pass, five findings, all fixed.

1. fig1, layout: legend text at 16, should be 18. Changed the three legend labels to 18 (widths in the table already assumed 18).
2. demo, layout: legend text at 16, should be 18. Changed the three legend labels to 18; ticks stay at 16 as notes.
3. fig1, correct to the material: title said every bar has a tool-results part, but bar 1 has none. Reworded the title.
4. demo, works: readout gave only the newest item's size, disagreeing with prompt 1 (400 tokens). Added `lastAdded` (what the last step added) and used it in the readout.
5. demo, works: prompt 3 could not be tried with the controls. Replaced it with a prompt the controls can do, and added to the clear note that the program can run the tool again.

Declined: none.
Figures not accepted: none (all four accepted).
