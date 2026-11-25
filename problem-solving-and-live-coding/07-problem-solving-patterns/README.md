# Problem-Solving Patterns

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../06-sorting-algorithms/README.md) · [Module index](../README.md)
<!-- /chapter-navigation:top -->

**Prerequisites:** [Dictionaries](../../collections/04-dictionaries-keys-and-values/README.md) · [Sets](../../collections/05-sets-and-unique-values/README.md) · [Complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)

## Goal

Recognize reusable patterns and select them according to the contract (40–55 minutes).

## 1. Accumulator and frequency map

An accumulator summarizes processed values in a variable (for example a sum). A frequency map stores counts per distinct key. For ["a", "b", "a"], update a dictionary using `counts.get(item, 0) + 1`; result {"a": 2, "b": 1}. Counts grow as you traverse; an empty list gives an empty dictionary. Expected O(n) time under normal hash behavior and O(k) storage for k distinct keys (the required output in this example). For membership alone, a set may be sufficient. Do not use a set to count occurrences because it discards duplicates.

## 2. Two pointers

For an ascending sorted integer list, decide whether two **different indices** sum to a target. Start left at 0 and right at len(values)-1. If their sum is too small, move left rightward; if too large, move right leftward; equality succeeds. Stop when left >= right. Sortedness justifies discarding a boundary: when the smallest plus largest is too small, that smallest cannot pair with any remaining value. [1, 3, 6, 8], target 9, succeeds at 1+8. [4], target 8, fails. O(n) time and O(1) auxiliary space, assuming sortedness without validation.

## 3. Fixed sliding window

To find the maximum sum of k consecutive integers (1 <= k <= len(values)), sum the first k values once; for each move, subtract the outgoing value and add the incoming one. Track the best sum. For [4, -1, 3, 2], k=2, sums are 3, 2, 5; result 5. Start best at the first sum, not zero, because all values may be negative. The shared implementation computes the first sum with a loop rather than a slice; O(n) time and O(1) auxiliary space. The example requires an exact integer k and raises TypeError for wrong types or ValueError for a size outside the permitted range. A fixed window is not an arbitrary subset, nor does this lesson claim that variable-window rules work for negative values.

## Practice

Trace each pattern with the examples above. Before opening the [shared example](examples/patterns.py), implement a frequency map for a list of labels, then test duplicates and empty input. Try an absent pair and a two-value duplicate pair; test a window with all-negative values and k equal to input length. Explain why a brute-force solution can be a useful correctness baseline before optimization.

**Quick reference:** accumulator for summaries; map for counts; two pointers when sortedness supports elimination; fixed window for adjacent ranges.

Run from the chapter directory (Python 3.13 baseline):

```bash
python examples/patterns.py
```

<!-- chapter-navigation:bottom -->
[← Previous](../06-sorting-algorithms/README.md) · [Module index](../README.md)
<!-- /chapter-navigation:bottom -->
