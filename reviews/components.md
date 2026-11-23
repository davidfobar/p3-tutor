# Components

One entry for every skill and every subagent you built, from `c1-skills` to `final`, including the ones you dropped, even one you took out again before any snapshot.
The heading is the skill's folder name or the subagent's `name` from its frontmatter, and `reviews/README.md` says what each field holds.
Replace the empty entry at the bottom with your first component, and copy it for each one after that.
Claude Code may fill in Kind, Step added, and With and without; Purpose, Review and Kept in final are yours.

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: to build quizes
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: required to implement
- Kept in final: yes

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: to grade quizes
- With and without: reviews/c1-skills.md, Round 4 (without) and Round 5 (with)
- Review: required to implement
- Kept in final: yes

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: provide an interactive conversation for the learner
- With and without: reviews/c1-skills.md, Round 5 (without) and Round 6 (with)
- Review: required to implement
- Kept in final: yes

### plan

- Kind: skill
- Step added: c1-skills
- Purpose: Before writing a lesson, the plan should be constructed
- With and without: reviews/c1-skills.md, Round 6 (without) and Round 7 (with)
- Review: it is what I would do as a teacher, build a lesson outline then the lesson
- Kept in final: yes

### demo

- Kind: skill
- Step added: c1-skills
- Purpose: to focus on creating a well scoped demo
- With and without: reviews/c1-skills.md, Round 7 (without) and Round 8 (with)
- Review: the demo is what differentated every lesson
- Kept in final: yes

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: to build the lesson for the learner
- With and without: reviews/c1-skills.md, Round 8 (without) and Round 9 (with)
- Review: required to implement
- Kept in final: yes

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: to review answers and provide feedback
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: required to implement
- Kept in final: yes

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: to review the difficulty of quizes and provide feedback
- With and without: reviews/c2-review.md, Round 2 (without) and Round 3 (with)
- Review: required to implement
- Kept in final: yes

### lesson-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: to look at the lesson, and provide feedback
- With and without: reviews/c2-review.md, Round 3 (without) and Round 4 (with)
- Review: required to implement
- Kept in final: yes

### lesson-planner

- Kind: subagent
- Step added: c3-split
- Purpose: reduce the scope of the planner to produce a crisp lesson outline
- With and without: reviews/c3-split.md, Round 1 (without) and Round 2 (with)
- Review: required to implement
- Kept in final: yes

### demo-dev

- Kind: subagent
- Step added: c3-split
- Purpose: take the demo skill and provide it to an agent
- With and without: reviews/c3-split.md, Round 2 (without) and Round 3 (with)
- Review: it was worthwhile
- Kept in final: yes

### product-reviewer

- Kind: subagent
- Step added: c3-split
- Purpose: be a single point of review tasks
- With and without: reviews/c3-split.md, Round 5 (without) and Round 6 (with)
- Review: reduced token usage
- Kept in final: yes

### grader

- Kind: subagent
- Step added: final
- Purpose: I was not clear on what this on was built for, but it was required
- With and without: reviews/final.md, Round 3 (without) and Round 4 (with)
- Review: required to implement
- Kept in final: yes
