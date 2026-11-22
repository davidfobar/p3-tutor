# Notes

What the learner already knows:
 - Forward kinematics. They can attach DH frames to a serial arm, write link transforms, and multiply them to get the endpoint pose. They can read off joint axis directions zᵢ and frame origins Oᵢ in base coordinates.
 - Vector tools. They can take cross products, use the right-hand rule, and change the frame a vector is expressed in with a rotation matrix.
 - Rigid-body velocity. They know the relation v = ω × r for a point on a rotating body. They know that angular velocities of bodies in series add as vectors.
 - Linear algebra and calculus. They can do matrix-vector products and the chain rule. They have met partial derivatives of vector functions, and probably the term "Jacobian" in a calculus setting.
 - Joint types. They know that a rotary joint rotates about its axis and a prismatic joint translates along it.

What they don't know yet:
 - How to turn joint rates into an endpoint linear and angular velocity with one matrix, without differentiating the full forward-kinematics expression.
 - The geometric construction: each column is the endpoint motion caused by a unit rate at that one joint, with all other joints held still.
 - How the column differs between a rotary joint (cross product of axis and moment arm, plus the axis itself) and a prismatic joint (axis direction, zero angular part).
 - That the result depends on which point is called the "endpoint." Moving the reference point from the wrist to the tool tip changes the linear part but not the angular part.
 - How arm geometry produces structure in the matrix, such as zero blocks when several axes pass through one point.

Where they tend to get stuck:
 - Treating angular velocity as the derivative of an orientation. They expect every row to be ∂(pose)/∂θ. They try to differentiate roll-pitch-yaw or Euler angles and either get stuck or get a different matrix.
 - Using the wrong moment arm. They use the vector along link i instead of the vector from joint i's axis all the way to the endpoint. This gives the right answer for the last joint only, so the error can go unnoticed on a two-link example.
 - Mixing coordinate frames. They write each joint axis as (0, 0, 1) because that is how it looks in its own local frame, then cross it with a vector expressed in base coordinates.
 - Assuming one column belongs to one joint. They expect column i to depend on θᵢ alone. They are surprised that it depends on every joint, through the axis direction (earlier joints) and the moment arm (later joints).
 - Getting the cross-product order or sign wrong. They write r × z instead of z × r and get the velocity pointing the wrong way. Sketching the arm and checking one column by intuition catches this.
 - Carrying over the rotary formula to prismatic joints. They apply the cross product to a prismatic joint, or give the joint a nonzero angular contribution.
 - Seeing no reason to care. The derivation can feel like extra algebra on top of forward kinematics until they see what it is for: resolved-rate control, singularities, and mapping forces to torques. One motivating example at he start of the lesson helps.
