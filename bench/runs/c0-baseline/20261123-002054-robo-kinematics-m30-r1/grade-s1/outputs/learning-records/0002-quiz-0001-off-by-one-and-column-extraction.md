# Planar-arm axes and origins are solid; joint indexing (M3) and column-vs-row extraction need work

On quiz 0001 (submission s1), Steve correctly gave the base-frame axes and origins of a two-link planar arm, and chose ⁰T₂ for joint 3's axis. They still answered "z₂, O₂" for joint 2 in q1 (M3, the off-by-one: joint i acts about z_{i−1}), and read ⁰z₂ from the third row of the rotation block instead of the third column.
Before the Jacobian lesson, rehearse "joint i uses z_{i−1} and O_{i−1}" and "columns of ⁰R are the frame's axes in base coordinates".

**Evidence:** quiz 0001, submission s1, items q1 (wrong, M3), q2 (correct), q3 (partial).
**Implications:** q1 and q3 are inconsistent: q3 used z₂ for joint 3 correctly, so the M3 error may be a convention slip rather than a fixed belief. Check it again with a short retrieval question.
