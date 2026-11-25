# Sorting Algorithms

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../05-searching-algorithms/README.md) · [Module index](../README.md) · [Next →](../07-problem-solving-patterns/README.md)
<!-- /chapter-navigation:top -->

**Prerequisites:** [List methods](../../collections/02-modifying-lists-and-methods/README.md) · [range](../../program-flow/05-range-enumerate-and-zip/README.md) · [Complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)

## Goal

Understand three elementary sorting algorithms and their trade-offs (45–60 minutes).

## 1. What sorting promises

Given a list of integers, return a new ascending list containing exactly the original values, including duplicates. The caller's list must remain unchanged. Sorting is not removing duplicates. Copy the list once before modifying it; the copy is the required output.

## 2. Bubble sort

Compare adjacent values and swap if left > right. After a full pass the largest remaining value is at its final end position. Reduce the unsorted boundary and stop early if no swap occurs. [3, 1, 2] becomes [1, 3, 2], then [1, 2, 3]. A stable sort keeps the relative order of equal-key items; swapping only strict inversions makes this variant stable.

## 3. Selection sort

At each index, scan the remaining suffix for its minimum index and swap that value into the current position. The prefix is then sorted and final. [3, 1, 2] → [1, 3, 2] → [1, 2, 3]. The usual swap-based variant is not stable: equal-key records may cross. It still scans each suffix even when already sorted.

## 4. Insertion sort

Treat the first item as a sorted prefix. Save the next value, shift larger prefix items one position right, and insert the saved value in the gap. [3, 1, 2] → [1, 3, 2] → [1, 2, 3]. Shift only strictly greater values to preserve stability. Each pass expands the sorted prefix.

| Variant | Best time | Worst time | Stable |
| --- | --- | --- | --- |
| Bubble (early exit) | O(n) | O(n²) | Yes |
| Selection | O(n²) | O(n²) | No |
| Insertion | O(n) | O(n²) | Yes |

All three use O(1) auxiliary space excluding the O(n) required returned copy. With the copy counted as additional allocation, total additional storage is O(n). These educational algorithms are not default production recommendations. Python `sorted(values)` returns a new list, while `values.sort()` mutates the list; both are stable. Prefer built-ins for ordinary application sorting.

## Practice

Trace each algorithm by hand for [4, 2, 2, 1]. Predict behavior on empty, sorted and reverse-sorted input; implement one before opening the [shared example](examples/sort.py). Check sortedness, multiplicities and unchanged input. Explain why a test that checks order alone might accept a solution that drops duplicates.

**Quick reference:** bubble moves adjacent inversions, selection chooses a minimum, insertion expands a sorted prefix.

Run from the chapter directory (Python 3.13 baseline):

```bash
python examples/sort.py
```

<!-- chapter-navigation:bottom -->
[← Previous](../05-searching-algorithms/README.md) · [Module index](../README.md) · [Next →](../07-problem-solving-patterns/README.md)
<!-- /chapter-navigation:bottom -->
