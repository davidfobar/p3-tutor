# Report

This file is written by `p3 report --write` (p3 0.2.0, 2026-11-20 17:23 UTC). Do not edit it by hand: it is written again whenever new runs are scored.

## Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.68 (0.65-0.69) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.44 (0.33-0.50) |
| `c1-skills` | 1 | 1.00 | 0 | 0.73 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.67 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 562.0k (460.9k-668.3k) | 27.6k (24.7k-31.7k) | 2.6 (2.5-2.7) | 1 (0-2) | 0.56 (0.54-0.61) |
| `c1-skills` | 1 | 1.51M | 47.5k | 4.5 | 3 | 0.89 |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 134.8k (132.9k-136.9k) | 4.9k (4.5k-5.2k) | 0.6 (0.6-0.7) | 0 | 0.17 (0.17-0.18) |
| `c1-skills` | 1 | 136.2k | 6.2k | 0.8 | 0 | 0.19 |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 257.7k (233.5k-270.9k) | 6.6k (6.4k-6.7k) | 0.8 (0.7-0.8) | 0 | 0.32 (0.31-0.32) |
| `c1-skills` | 1 | 460.0k | 12.4k | 1.4 | 0 | 0.41 |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 587.2k (546.5k-627.2k) | 10.3k (9.5k-11.2k) | 1.5 (1.4-1.5) | 0 | 0.70 (0.69-0.71) |
| `c1-skills` | 1 | 752.6k | 12.3k | 1.6 | 1 | 0.58 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.54M (1.50M-1.62M) | 49.5k (47.0k-53.6k) | 5.4 (5.2-5.6) | 1 (0-2) | 1.76 (1.73-1.78) |
| `c1-skills` | 1 | 2.86M | 78.4k | 8.2 | 4 | 2.08 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 5 | - | - | - |
| Lesson | Pedagogy | 4 | - | - | - |
| Lesson | Alignment with the learning goal | 5 | - | - | - |
| Lesson | Overall quality | 3 | - | - | - |
| Quiz | Difficulty | 5 | - | - | - |
| Quiz | Coverage of the lesson's core | 5 | - | - | - |
| Quiz | Wording and possible misreadings | 5 | - | - | - |
| Quiz | Writing quality | 5 | - | - | - |
| Quiz | Alignment with the learning goal | 5 | - | - | - |
| Feedback | Useful | 4 | - | - | - |
| Feedback | Explains enough | 3 | - | - | - |
| Feedback | Personalized to how I like things explained | 4 | - | - | - |
| Tutor | Guardrails | 5 | - | - | - |
| Tutor | Personalization | 4 | - | - | - |
