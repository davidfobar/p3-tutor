# Language models do not remember earlier conversations on their own

Riley believed a model automatically remembers what each student said last week, so the makerspace assistant would recall it unaided. I corrected this: the model only sees the text sent in the current request, so anything remembered across sessions must be saved by the assistant's code and put back into the context.
Not yet confirmed that the correction landed; check with a question when memory comes up in the next lesson.

**Evidence:** chat message at the start of the context-and-memory session.
**Implications:** Teach the context window, and what to save between sessions, starting from this misconception.
