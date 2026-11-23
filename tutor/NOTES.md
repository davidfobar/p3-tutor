# Notes

## What the learner knows

- Knows forward and inverse kinematics as position maps (joint angles <-> hand pose), well enough to ask what Jacobians add.

## Misconceptions seen

- 2026-11-23: thought forward and inverse kinematics "do everything", so Jacobians seemed redundant. Corrected: FK/IK relate positions; the Jacobian relates velocities (and, transposed, forces to joint torques), and it is what most numerical IK solvers run on. Check later that they can say what J maps and why it changes with the arm's pose.
- 2026-11-23: on a stretched-out two-link arm they said "the hand can only get closer to the origin". That is right about reach (positions), but they thought in positions, not velocities: at that pose the hand can't move radially at all, in or out, only sideways, and J loses rank (det J = L1·L2·sin θ2 = 0). They didn't yet link the singularity to J being non-invertible.
