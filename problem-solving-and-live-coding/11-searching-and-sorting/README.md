# Searching and Sorting Challenges

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../10-functions-and-recursion/README.md) · [Module index](../README.md) · [Next →](../12-algorithms-and-complexity/README.md)
<!-- /chapter-navigation:top -->

Review linear search, binary search on sorted input and insertion sort. A binary insertion index need not be a matching position; it is the first position that can accept the value without breaking order.

Read the contract and linked prerequisite lessons, predict results, attempt the starter in a personal file, and check boundaries. Open hints progressively; compare the reference only after your attempt. No browser runner is provided.

### Two binary boundaries

On a sorted list, a half-open binary search can find the first value at least the target (discard through middle when value < target) or the first value strictly greater (discard through middle when value <= target). Both can return the length sentinel. For [1, 4, 4, 4, 9] and target 4, the boundaries are 1 and 4; the inclusive last index is 3. If the first boundary is outside the list or not equal to the target, it is absent. Two logarithmic searches remain logarithmic; no sorting or scan is necessary.

### Merge two sorted sequences

Keep a pointer to the next unconsumed item of each input. While both have items, append the smaller head (either on ties), advance only that pointer, then drain the remaining items of either sequence. For [1, 3] and [2, 3], the heads produce [1, 2, 3, 3]. The output prefix stays sorted and contains exactly consumed occurrences. Each pointer advances once per input item; the returned list is output space, with constant additional working storage. The technique is merging, not sorting arbitrary unsorted lists.

## Available challenges

- [First Matching Index](../../exercises/problem-solving/linear-first-index/README.md) · Easy · 12 min
- [Binary Insertion Index](../../exercises/problem-solving/binary-insertion-index/README.md) · Medium · 22 min
- [Descending Insertion Sort](../../exercises/problem-solving/descending-insertion-sort/README.md) · Medium · 25 min

- [Binary Target Range](../../exercises/problem-solving/binary-target-range/README.md) · Hard · 32 min
- [Merge Sorted Lists](../../exercises/problem-solving/merge-sorted-lists/README.md) · Hard · 30 min

<!-- chapter-navigation:bottom -->
[← Previous](../10-functions-and-recursion/README.md) · [Module index](../README.md) · [Next →](../12-algorithms-and-complexity/README.md)
<!-- /chapter-navigation:bottom -->
