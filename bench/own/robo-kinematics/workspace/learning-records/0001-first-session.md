# 0001 - First session

The learner can, given a serial arm, assign DH frames, compose the homogeneous transforms, and read off every joint axis zᵢ and every frame origin Oᵢ in the base frame. Build on this, and reteach it only if the warm-up below shows they can't.

The Jacobian lesson depends on this more than anything else:

Axis directions: column i needs joint i's axis, zᵢ₋₁, written in base coordinates. Learners get that from the third column of the rotation part of ⁰Tᵢ₋₁.
Moment arms: the vector from each joint to the endpoint, Oₙ − Oᵢ₋₁, is a difference of base-frame origins. Learners get the origins from the position part of ⁰Tᵢ.

A learner who can only produce the final end-effector pose ⁰Tₙ, but can't pull out the intermediate ⁰Tᵢ and their parts, will get stuck on the first column. A useful warm-up for the start of the lesson: have them list zᵢ and Oᵢ in base coordinates for a two-link arm. If they can't do that, the Jacobian derivation won't work for them yet.

The course uses the standard (distal) DH convention, as found in Paul and in Spong:

Joint i connects link i−1 to link i and acts about or along z_{i−1}.
Frame i sits at the distal end of link i, where the common normal between z_{i−1} and z_i meets z_i.
The link transform is ^{i−1}T_i = Trans(d_i along z_{i−1}) · Rot_z(θ_i) · Trans(a_i along x_i) · Rot_x(α_i).
The parameters:
α_i is the skew angle from z_{i−1} to z_i, measured about x_i.
d_i is the distance along z_{i−1}.
a_i is the distance along x_i.
θ_i is the angle about z_{i−1}.

The course allows one relaxation: x_i may point from z_i back to z_{i−1}. When it does, a_i and α_i change sign. Keep this in mind when grading, because a learner who flips x_i can get negative link lengths and still be correct.

This is the convention where the off-by-one misconception (joint i about z_i instead of z_{i−1}) applies. In the modified (Craig) convention, joint i really does act about z_i. A learner who has seen Craig elsewhere will make the off-by-one error confidently.
