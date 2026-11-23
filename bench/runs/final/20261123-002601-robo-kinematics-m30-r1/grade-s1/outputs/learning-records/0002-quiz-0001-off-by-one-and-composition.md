# Composes transforms well; off-by-one on joint axes (M3) and row/column slip persist

On quiz 0001 the learner correctly gave the base-frame axes and origins for a two-link planar arm and chose the right intermediate transform for a 6-joint arm. They still wrote joint 2 about z₂ and O₂ (M3), though they used the correct index for joint 3 in q3, so the rule is unstable. They also read an axis from a row of the rotation block instead of a column.

**Evidence:** quiz 0001, submission s1, items q1, q2, q3.
**Implications:** Start the Jacobian lesson with a short drill on joint i about z_{i-1} and on reading zᵢ from columns of ⁰Rᵢ.
