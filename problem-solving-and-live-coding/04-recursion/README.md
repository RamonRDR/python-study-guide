# Recursion

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../03-algorithmic-complexity/README.md) · [Module index](../README.md) · [Next →](../05-searching-algorithms/README.md)
<!-- /chapter-navigation:top -->

**Prerequisites:** [Return values](../../functions/03-return-values/README.md) · [Scope](../../functions/04-scope/README.md) · [Functions](../../functions/08-functions-working-together/README.md) · [Complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)

## Goal

Understand self-calls, base cases, progress and the call stack (35–45 minutes).

## 1. A smaller instance of the same problem

Recursion solves a problem by calling the same function on a smaller instance. The base case returns without another call; the recursive step must move toward it. To sum integers 1 through n, use sum(0) = 0 and sum(n) = n + sum(n - 1) for positive n. Each call has its own local variables; earlier calls wait for later results.

For n = 3: calls descend 3 → 2 → 1 → 0. Returns unwind 0 → 1 → 3 → 6. A missing base case, or calling with n + 1, fails to terminate for positive n.

## 2. Python implementation

The [example](examples/recursive_sum.py) accepts exact integers from 0 to 100. It rejects values outside the domain before recursing and uses a private helper so validation is not repeated. The limit is a teaching constraint, not a guarantee for every possible Python stack configuration. Python limits recursion depth and may raise RecursionError; do not increase the limit just to solve a linear problem. An iterative accumulator avoids recursive stack growth.

Under the fixed-cost arithmetic model, both versions take O(n) time; the recursive version uses O(n) auxiliary stack space, and the iterative version O(1). A closed-form formula can avoid iteration, but the goal here is understanding recursive structure.

## Practice

Trace n = 4 using a table of pending calls and returned values. Implement a recursive countdown function that returns the count of steps to zero for n in 0–100. Test 0 and 1, then compare with a loop. Explain why the decreasing argument proves progress, and why validating negative inputs matters.

**Quick reference:** base case + smaller input + combine returns; count stack frames as auxiliary space.

Run from the chapter directory (Python 3.13 baseline):

```bash
python examples/recursive_sum.py
```

<!-- chapter-navigation:bottom -->
[← Previous](../03-algorithmic-complexity/README.md) · [Module index](../README.md) · [Next →](../05-searching-algorithms/README.md)
<!-- /chapter-navigation:bottom -->
