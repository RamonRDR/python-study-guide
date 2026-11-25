# Timed Live Coding

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../15-mixed-challenges/README.md) · [Module index](../README.md) · [Next →](../../technical-interview-preparation/01-understanding-technical-interviews/README.md)
<!-- /chapter-navigation:top -->

## Prepare before starting

Review [problem-solving fundamentals](../01-problem-solving-fundamentals/README.md), [boundary cases](../02-constraints-and-edge-cases/README.md), [complexity](../03-algorithmic-complexity/README.md) and [patterns](../07-problem-solving-patterns/README.md). Use a personal timer and local Python 3.13; no browser runner is supplied. Practice one exercise at a time. Read the prompt and permitted tools; no AI, hints or solutions during the first attempt. You may run your own code and tests. Do not sacrifice clarity or correctness for speed.

## Two practice schedules

| Activity | 10 min | 20 min |
| --- | ---: | ---: |
| Read and clarify contract, examples | 2 | 3 |
| Plan and trace | 2 | 4 |
| Implement | 4 | 9 |
| Test and explain | 2 | 4 |

If blocked, say which assumption you need or write the smallest testable step. At the limit record the state (not started, partial, complete), elapsed time and known failed cases; stop the clock. Then finish without time pressure, reveal hints/reference and retry later. Time is self-reported, not a grade or job-readiness measure.

## Contiguous runs

Counting all qualifying items differs from counting a contiguous run. Track the current run length and the maximum. Extend the current counter on a qualifying value; reset it on a failure. For qualification >= 2 and [2, 3, 0, 2], run lengths are 1, 2, 0, 1; best 2. The current value describes the qualifying suffix, not a total count. This combines an accumulator and a condition, with constant auxiliary variables.

## Self-assessment after each attempt

Record one point for each criterion met: clear contract/edge cases, justified plan, correct behavior on your own cases, readable implementation, and explanation of time/space. Use 0–5 only for personal feedback; no automated scoring of explanations or elapsed time. Record one improvement and the next practice action.

## Available challenges

- [Timed: Threshold Count](../../exercises/problem-solving/timed-threshold-count/README.md) · Easy · 10 min
- [Timed: Longest Qualifying Streak](../../exercises/problem-solving/timed-longest-streak/README.md) · Medium · 20 min

<!-- chapter-navigation:bottom -->
[← Previous](../15-mixed-challenges/README.md) · [Module index](../README.md) · [Next →](../../technical-interview-preparation/01-understanding-technical-interviews/README.md)
<!-- /chapter-navigation:bottom -->
