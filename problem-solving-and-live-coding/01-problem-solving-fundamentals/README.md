# Problem-Solving Fundamentals

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../../manual-programming-practices/04-professional-workflow/README.md) · [Module index](../README.md) · [Next →](../02-constraints-and-edge-cases/README.md)
<!-- /chapter-navigation:top -->

**Prerequisites:** [Program Flow](../../program-flow/08-choosing-and-combining-program-flow/README.md) · [Functions](../../functions/08-functions-working-together/README.md) · [SDD](../../manual-programming-practices/02-specification-driven-development/README.md)

## Goal

Learn to turn a request into a small, testable program before opening the editor (25–35 minutes).

## 1. Read, restate and model

A fictional reading club records whole minutes spent studying each day. Given a list of nonnegative integers, return the total of days that reached a goal of 20 minutes. Here “total” means **sum of minutes**, not number of days. Empty input gives zero; the original list stays unchanged. Ask about an ambiguous requirement before coding. For `[12, 20, 25]`, the qualifying values are 20 and 25, so the answer is 45.

## 2. Decompose and trace

Break the task into identifying a qualifying value, accumulating qualifying minutes, and returning the result. Write language-independent pseudocode: start total at zero; for each minute value, if it is at least the goal, add it; return total after iteration. A trace of the example is 0 → 0 → 20 → 45. The accumulator represents the sum of qualifying values processed so far. Use a loop rather than three hard-coded indices; use a function rather than printing inside the loop so callers can test the return value.

## 3. Implement and verify

The shared example uses a configurable goal, default 20. Try writing it first; then compare with the [example](examples/study_minutes.py). The contract assumes nonnegative integer inputs and goal; no extra validation is required. Test empty input, exactly the threshold, no matching values, and repeated values. If returning too early produces 0, trace the indentation and move the return outside the loop.

## Practice

Change the fictional requirement: return the **number** of qualifying days, not the minutes. Write two hand-calculated examples, pseudocode and a function before consulting a solution. Explain why the two contracts differ. For the original example, the new answer is 2.

**Quick reference:** contract → examples → decomposition → trace → code → tests → explanation.

Run from the chapter directory (Python 3.13 baseline):

```bash
python examples/study_minutes.py
```

<!-- chapter-navigation:bottom -->
[← Previous](../../manual-programming-practices/04-professional-workflow/README.md) · [Module index](../README.md) · [Next →](../02-constraints-and-edge-cases/README.md)
<!-- /chapter-navigation:bottom -->
