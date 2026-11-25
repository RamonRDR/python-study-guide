# Data Structures and Algorithms Review

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../03-python-fundamentals-review/README.md) · [Module index](../README.md) · [Next →](../05-classes-and-objects/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [collections/01-list-creation-and-indexing](../../collections/01-list-creation-and-indexing/README.md)
- [collections/03-tuples-and-immutability](../../collections/03-tuples-and-immutability/README.md)
- [collections/04-dictionaries-keys-and-values](../../collections/04-dictionaries-keys-and-values/README.md)
- [collections/05-sets-and-unique-values](../../collections/05-sets-and-unique-values/README.md)
- [collections/06-choosing-the-right-collection](../../collections/06-choosing-the-right-collection/README.md)
- [problem-solving-and-live-coding/03-algorithmic-complexity](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [problem-solving-and-live-coding/04-recursion](../../problem-solving-and-live-coding/04-recursion/README.md)
- [problem-solving-and-live-coding/05-searching-algorithms](../../problem-solving-and-live-coding/05-searching-algorithms/README.md)
- [problem-solving-and-live-coding/06-sorting-algorithms](../../problem-solving-and-live-coding/06-sorting-algorithms/README.md)
- [problem-solving-and-live-coding/07-problem-solving-patterns](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)
- [problem-solving-and-live-coding/08-strings-and-numbers](../../problem-solving-and-live-coding/08-strings-and-numbers/README.md)

## Choose by the contract

A list models order and repetition; a tuple fixes its positions; a dictionary associates hashable keys with values; a set represents unique hashable members. A tuple can contain mutable objects and is not always hashable. Choose the structure by behavior, not by a memorized ranking.

For duplicate detection, a set of seen hashable values can avoid a nested scan. Under usual average-case hashing assumptions, a scan takes O(n) time and up to O(n) auxiliary space. Do not promise constant worst-case dictionary/set access. Linear search works on unsorted input; binary search needs ordered data and a valid invariant. Recursion needs a base case and progress toward it; include call-stack space. Explain sorting trade-offs using the Phase 11 lessons, not only the name of an algorithm.

## Practice with existing challenges

Use the original Phase 11 challenge bank: `has-duplicate` for membership, `binary-target-range` for boundaries, and `longest-distinct-substring` for variable windows. Study the corresponding instruction first. For each, state constraints, choose a structure, explain time/space with assumptions, test edge cases, then compare with its reference.

**Quick reference:** contract → representation → algorithm → complexity → tests.

Existing challenges: [has-duplicate](../../exercises/problem-solving/has-duplicate/README.md) · [binary-target-range](../../exercises/problem-solving/binary-target-range/README.md) · [longest-distinct-substring](../../exercises/problem-solving/longest-distinct-substring/README.md)

<!-- chapter-navigation:bottom -->
[← Previous](../03-python-fundamentals-review/README.md) · [Module index](../README.md) · [Next →](../05-classes-and-objects/README.md)
<!-- /chapter-navigation:bottom -->
