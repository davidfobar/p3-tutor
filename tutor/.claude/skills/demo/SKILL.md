---
name: demo
description: Build the hands-on demo for a planned lesson - either an interactive graphic the learner plays with in the lesson page, or a short series of commands or code the learner runs themselves - from the lesson's plan, as a self-contained piece the lesson embeds. Use it after the plan skill and before the lesson is written, or when the learner asks for a demo or a hands-on exercise.
argument-hint: "Which plan or topic should the demo be for?"
---

# Demo

You build the one hands-on demo at the center of the next lesson, so the learner touches or sees the idea before, or while, they read about it.
The demo is one of two kinds: an **interactive graphic** in the lesson page, or a **hands-on exercise**, a series of commands or code the learner types and runs.
You build the demo only; the teach skill writes the lesson around it and places it.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
When another skill, such as `/teach`, has you read this file instead of running it, the request is that skill's request.
A request that says what to do gets done now, without stopping to ask first.

## Read first

Read the lesson's plan, the newest file in `plans/` unless the request names another; it gives the objectives and their core, where the learner starts, the material, the misconceptions and the threads to earlier lessons.
When there is no plan, read `MISSION.md`, `NOTES.md` and the learning records, and work from the request's objective.
Read `PREFERENCES.md` (the examples the learner relates to, and how they like to learn), `MISSION.md` for what they will build or do with this, and `.claude/skills/teach/references/lesson-template.html` for the lesson's CSS variables and classes.
Use Read, Glob and Grep to look around and Write to create files; work only inside this workspace and never write anything under `.claude/`.

## 1. Choose the idea and the kind

- Pick the one core idea from the plan that most needs to be seen or done to be understood: a mechanism, a process with steps, a quantity that changes, or a misconception the plan lists that a demo can break.
- Choose the kind:
  - **Interactive graphic** when the idea is a mechanism, a flow or a trade-off the learner can explore by changing something and watching what happens: a slider, a button that steps through a process, a toggle between two designs.
  - **Hands-on exercise** when the objective is something the learner will do themselves with code or a tool, the mission says they will build it, and `MISSION.md` or `NOTES.md` says they have what it needs (a language they know, a tool installed).
  - When both fit, choose the one `PREFERENCES.md` points to; when unsure, choose the interactive graphic, because it needs nothing installed.
- Write down, in one sentence, what the learner should notice or be able to do after the demo; everything in it serves that sentence.

## 2a. An interactive graphic

- One self-contained HTML fragment: a `<section class="demo">` that holds its own inline SVG, a `<style>` whose rules all start with `.demo`, and a `<script>` in plain JavaScript, with no library and nothing loaded from the web.
- Use the template's CSS variables for colors, so the demo works in light and dark mode, and keep it legible at phone width.
- The learner changes one or two things (a slider, a step button, a toggle), and the graphic and a short readout change with them; show what is happening in words beside the picture.
- Make it correct to the material: every number, label and behavior must match the plan's facts and sources, simplified but never wrong.
- When the plan lists a misconception the demo can break, include a moment where the learner can try the wrong belief and see it fail.
- Accessible: every control a real `<button>` or `<input>` with a label, usable from the keyboard, and the SVG with a `<title>`.
- Under the graphic, two or three short prompts ("Double this value. Before you move the slider, what do you expect to happen to that one?") that make the learner predict, then try.
- Wrap the script so nothing leaks to the page: an IIFE, with every element looked up inside the demo's own section.

## 2b. A hands-on exercise

- One self-contained HTML fragment, a `<section class="demo">`, that walks the learner through three to six steps, each with:
  - what to do and why, in a sentence or two;
  - the exact command or code, in a `<pre><code>` block they can copy;
  - what they should see, the expected output or result, so they can check themselves.
- Use only what the learner has or can get free in a minute; prefer the standard library and nothing that needs an account, a paid key or a download of more than a few megabytes.
  When the idea needs a paid service (such as a model API), build the exercise so it runs without one, for example with a stand-in function that returns a fixed reply, and say how the real call would replace it.
- Keep each code block short, under about 25 lines, and build it up step by step instead of handing over a finished program.
- The last step changes something on purpose (a value, a missing piece, a broken input) and asks the learner to predict what happens before they run it.
- You cannot run the code here, so check it by reading it line by line as an interpreter would: names defined before use, correct syntax, and outputs that match what you wrote under "what they should see".

## 3. Write the demo

Write it to `demos/NNNN-<slug>.html`, with the number and slug of the lesson it belongs to (the plan's).
Start the file with an HTML comment that says: the kind, the core idea, the one sentence of what the learner should notice or do, which section of the lesson it belongs in, and about how many minutes it takes.
Then the `<section class="demo">` fragment itself, ready to paste into the lesson as it is: no `<html>`, `<head>` or `<body>`.

## Finish

When another skill ran you, return to it with the demo's path.
When the learner asked for the demo, end with a short message: the demo's path, what it shows, and that the next lesson will use it.

## Check before you finish

- The fragment loads nothing from the web, its CSS rules all start with `.demo`, and its script touches nothing outside its own section.
- Every fact, number and behavior in it matches the plan's material.
- An interactive graphic works from the keyboard and has its prediction prompts; a hands-on exercise gives the expected result for every step.
