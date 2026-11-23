# Plan: From Joint Rates to Hand Speed

- Objective: O2: Find the endpoint velocity from the joint rates.
- Minutes: 30
- Win: Build the Jacobian of a given arm from its frames, then compute endpoint velocity from joint rates and check one column by moving one joint.
- Demo: 3: Turn one joint at a time and watch the endpoint move along that joint's column.
- Next lesson: Inverting the Jacobian for joint rates, force-torque mapping, and a full singularity analysis.

## Outline

### 1. A straight line at constant speed (O2, 2.5 min)
- Forward kinematics gives poses, not speeds; an arm sealing a car door seam needs joint speeds for constant hand speed.
- V = J·q̇ maps joint rates to hand velocity; this is what resolved-rate control uses [S1]

### 2. Warm-up: pull out zᵢ₋₁ and Oᵢ (O2, 3 min)
- Axes come from the third column of the rotation part of the frame transform, in base coordinates [S1]
- Origins come from the position part of ⁰Tᵢ; moment arm is Oₙ − Oᵢ₋₁ [S1]
- Misconception: every axis is (0, 0, 1) -> that is only true in its own frame; cross in base coordinates [S1] (shown)

### 3. One joint at a time (O2, 5.5 min)
- Column i is the endpoint motion for a unit rate at joint i, others frozen [S1]
- Since v = ω × r, a rotary column's linear part is axis × (arm to endpoint) [S1]
- Misconception: differentiate the pose row by row -> only the linear rows; angular velocity is not the derivative of Euler angles [S1] (shown)
- Figure: Two-link arm with the endpoint velocity arrow for each joint, perpendicular to its moment arm.

### 4. The recipe: rotary and prismatic side by side (O2, 5 min)
- Rotary column: linear zᵢ₋₁ × (Oₙ − Oᵢ₋₁), angular zᵢ₋₁ [S1]
- Prismatic column: linear zᵢ₋₁, angular zero [S1]
- Cross-product order is axis first; the arm runs from joint i to the endpoint, not along link i [S1] (shown)
- Misconception: column i depends only on θᵢ -> it depends on earlier joints through axes and later joints through arms (shown)

### 5. Reference point, zero blocks, trouble spots (O2, 3.5 min)
- Moving the reference point from wrist to tool tip changes only the linear part [S1]
- Joints whose axes pass through the reference point have zero linear columns, as in the Scheinman wrist [S1]
- Singularity: columns become dependent, so the stretched two-link arm cannot move along its length [S1]
- Figure: Two-link arm stretched straight, with both column arrows pointing the same way, perpendicular to the arm.

### 6. Worked example with practice (O2, 6 min)
- Planar two-link arm: build the columns, compute hand velocity for given rates.
- Check with one-joint motion, units and direction; then a prismatic-rotary arm like a car-wash gantry.
- Sanity check against finite differences of forward kinematics, as in code.

### 7. Summary (O2, 2 min)
- Recipe checklist: axes, origins, arm, cross, stack, multiply, check.

### 8. Go further (O2, 2.5 min)
- Near a singularity small hand motions need huge joint rates, which previews inverse velocity control [S1]

## Sources

- S1: Introduction to Robotics, Lecture 7 (Stanford CS223A), https://see.stanford.edu/materials/aiircs223a/transcripts/IntroductionToRobotics-Lecture07.html
