# Algorithmic Complexity

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../02-constraints-and-edge-cases/README.md) · [Module index](../README.md) · [Next →](../04-recursion/README.md)
<!-- /chapter-navigation:top -->

**Prerequisites:** [for](../../program-flow/04-for-loops-and-iteration/README.md) · [while](../../program-flow/06-while-loops-and-state-driven-repetition/README.md) · [Collections](../../collections/06-choosing-the-right-collection/README.md)

## Goal

Compare how time and extra storage grow with input size (35–50 minutes).

## 1. Count work rather than seconds

Let n be the number of elements, assuming constant-cost primitive operations on fixed-size values. Big O describes an asymptotic upper bound on growth, not elapsed seconds or necessarily a tight bound. For these examples we give tight growth bounds (also expressible with Theta). Constants and lower-order terms do not change the asymptotic class. Worst-case, best-case and average-case assumptions must be named.

| Growth | Example |
| --- | --- |
| O(1) | Access one valid list index |
| O(log n) | Repeatedly halve a positive size |
| O(n) | Visit every element once |
| O(n log n) | n work at each of logarithmically many levels |
| O(n²) | Visit every ordered pair of n elements |

Two consecutive scans cost O(n), not O(n²). A nested loop need not be quadratic: count its actual iterations. For size 8, a halving loop 8 → 4 → 2 → 1 takes 3 steps, a full scan 8, and ordered pairs 64. See [operation counts](examples/operation_counts.py); doubling n doubles a scan, quadruples ordered pairs and adds roughly one halving step.

## 2. Space and trade-offs

Auxiliary space is additional working storage excluding input and, by stated convention here, required output. An accumulator has O(1) auxiliary space; a list copied from n values needs O(n) extra space. Recursive calls also use stack space. A hash table can reduce repeated scans to expected constant-time lookups under ordinary hashing assumptions, but stores additional entries and worst-case lookup can be linear. Python arbitrary-size integer arithmetic and string comparisons can depend on operand size; state the simplified model rather than claiming all operations are constant.

## 3. Use the right comparison

Do not choose a complex algorithm for a tiny input solely because of asymptotic growth; consider clarity, actual constraints, memory and correctness. Time measurements vary by hardware and are not proofs. Use operation counts and reasoning to compare growth.

## Practice

For n = 4, 8, 16, predict scan, pair and halving counts; run the example and explain why two independent scans are still O(n). Compare returning a count with creating a list of all matching values, distinguishing auxiliary and output space.

**Quick reference:** define n and assumptions, count iterations, identify worst case, account for auxiliary storage.

Run from the chapter directory (Python 3.13 baseline):

```bash
python examples/operation_counts.py
```

<!-- chapter-navigation:bottom -->
[← Previous](../02-constraints-and-edge-cases/README.md) · [Module index](../README.md) · [Next →](../04-recursion/README.md)
<!-- /chapter-navigation:bottom -->
