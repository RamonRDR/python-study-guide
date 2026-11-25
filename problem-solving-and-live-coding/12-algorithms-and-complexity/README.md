# Algorithms and Complexity Challenges

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../11-searching-and-sorting/README.md) · [Module index](../README.md) · [Next →](../13-debugging-challenges/README.md)
<!-- /chapter-navigation:top -->

Compare operation counts and storage before choosing a solution. For n positions there are n(n-1) ordered pairs of different positions, twice the unordered count; use the given arithmetic identity. For duplicate detection, contrast a repeated scan with a set. Functional tests do not prove asymptotic bounds.

Read the contract and linked prerequisite lessons, predict results, attempt the starter in a personal file, and check boundaries. Open hints progressively; compare the reference only after your attempt. No browser runner is provided.

### Count multiplicities, not just matching values

The earlier two-pointer pattern finds whether a pair exists. To count every index pair in sorted input, discard a boundary if its sum is too small or too large. On an exact match with different boundary values, count the consecutive occurrences of each value from its end and multiply: two 1s and three 3s form six pairs summing to 4. Consume both groups. If the two boundary values are equal, sortedness means every remaining value is equal. For k remaining indices, count k(k-1)//2 and stop. Four 2s yield six pairs, not two. Each pointer advances monotonically, so the total scanning work is linear even with nested run-counting loops. No input copy is required.

## Available challenges

- [Count Unordered Pairs](../../exercises/problem-solving/unordered-pair-count/README.md) · Easy · 12 min
- [Detect a Duplicate](../../exercises/problem-solving/has-duplicate/README.md) · Medium · 18 min

- [Count Target Pairs with Duplicates](../../exercises/problem-solving/sorted-pair-multiplicity/README.md) · Hard · 40 min

<!-- chapter-navigation:bottom -->
[← Previous](../11-searching-and-sorting/README.md) · [Module index](../README.md) · [Next →](../13-debugging-challenges/README.md)
<!-- /chapter-navigation:bottom -->
