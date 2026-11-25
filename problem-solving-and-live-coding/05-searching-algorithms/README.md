# Searching Algorithms

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../04-recursion/README.md) · [Module index](../README.md) · [Next →](../06-sorting-algorithms/README.md)
<!-- /chapter-navigation:top -->

**Prerequisites:** [Lists](../../collections/01-list-creation-and-indexing/README.md) · [Loop control](../../program-flow/07-break-continue-and-loop-else/README.md) · [Complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)

## Goal

Select and implement linear and binary search under explicit contracts (35–50 minutes).

## 1. Linear search

Visit each item from left to right; return the index of the first target, or -1 if absent. Works on unsorted integer lists and preserves the input. With [8, 4, 4, 9] and target 4, the answer is 1. Empty input returns -1. Worst-case O(n) time, O(1) auxiliary space.

## 2. Binary search

Binary search needs a sorted ascending sequence with random access. Keep a half-open interval [left, right) that contains all still-possible positions. Initially left=0 and right=len(values). Compute mid = (left + right) // 2. If values[mid] is less than target, discard through mid by setting left = mid + 1; otherwise set right = mid. When equal bounds meet, left is the first possible insertion position. Verify it is within the list and equals target, or return -1. This variant finds the **first** match even with duplicates.

Trace [2, 4, 4, 7, 9] for target 4: interval [0,5), mid 2 (4) → [0,2); mid 1 (4) → [0,1); mid 0 (2) → [1,1); index 1. Every iteration shrinks the interval. Do not access values[len(values)].

## 3. Compare

The [example](examples/search.py) assumes integer lists and an ascending sorted input for binary search; it does not scan to validate sortedness, because that would cost O(n). Worst-case binary search takes O(log n) comparisons and O(1) auxiliary space; sorting an unsorted input just for one lookup may cost more than a scan. Built-ins such as `in` are useful when only membership matters.

## Practice

Trace a missing target smaller than all values and one larger than all values; test empty, single-item and duplicate lists. Implement both functions without reading the example, then compare. Explain why a binary search on an unsorted list is outside its contract.

**Quick reference:** linear scan for arbitrary order; binary search only with sorted data and a shrinking interval.

Run from the chapter directory (Python 3.13 baseline):

```bash
python examples/search.py
```

<!-- chapter-navigation:bottom -->
[← Previous](../04-recursion/README.md) · [Module index](../README.md) · [Next →](../06-sorting-algorithms/README.md)
<!-- /chapter-navigation:bottom -->
