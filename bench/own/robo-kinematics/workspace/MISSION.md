# Mission

What the learner wants to learn during the lesson:
 - "Why do I need this?" They want a concrete problem early that forward kinematics can't solve, such as moving the gripper in a straight line at constant speed and working out the joint speeds.
 - "What does each number in the matrix mean?" They want to look at a column and picture the arm moving, not just push symbols around.
 - "Why don't I just differentiate the forward kinematics?" They already have the pose equations and want to know when that approach works and when it fails.
 - "What's the recipe?" They want a repeatable procedure they can trust on an exam or in code: which vectors to take, in which frame, crossed in which order.
 - "How do I know my answer is right?" They want sanity checks, like moving one joint and seeing if the endpoint goes where the column says, or checking units and directions.
 - "What changes for a sliding joint?" They want the rotary and prismatic cases side by side so they don't have to guess.

What the learner wants to be able to do afterward:
 - Write down the Jacobian for an arm they're given, from its frames, without looking up a worked example for that specific robot.
 - Answer "how fast is the hand moving?" for given joint speeds, and in the other direction, "what joint speeds give this hand motion?", at least when the matrix can be inverted.
 - Implement it in code. They want a function that takes joint angles and returns the matrix, so they can check it numerically against finite differences of their forward kinematics.
 - Spot trouble configurations, recognizing when the arm is stretched out or axes line up so that some hand motions become impossible.
 - Feel ready for what comes next, such as velocity control, force-torque mapping and inverse kinematics, knowing this matrix is the tool those topics are built on.
