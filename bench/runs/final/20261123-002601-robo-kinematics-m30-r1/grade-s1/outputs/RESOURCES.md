# Robot Arm Jacobian Resources

## Knowledge

- [Article: "Denavit–Hartenberg parameters" (Wikipedia)](https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters)
  Covers the DH convention, with the sections "Four parameters" and "Denavit–Hartenberg matrix". Use for: which axis a joint rotates about (the previous frame's z-axis, z_{i-1}) and how link transforms are built.
- [Article: "Transformation matrix" (Wikipedia)](https://en.wikipedia.org/wiki/Transformation_matrix)
  Use for: why the columns of a transformation matrix are the images of the basis vectors, in the section "Finding the matrix of a transformation".

## Wisdom (Communities)

## Gaps

- No source yet found that states directly that the columns of the rotation block of a robot transform ⁰Tᵢ are frame i's axes in base coordinates.
