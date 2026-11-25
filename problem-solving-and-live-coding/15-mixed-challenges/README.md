# Mixed Challenges

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../14-refactoring-challenges/README.md) · [Module index](../README.md) · [Next →](../16-timed-live-coding/README.md)
<!-- /chapter-navigation:top -->

Combine earlier concepts rather than guessing a new algorithm. Restate the contract, decide on data structures and tie-breaking, and trace a small example before coding.

Read the contract and linked prerequisite lessons, predict results, attempt the starter in a personal file, and check boundaries. Open hints progressively; compare the reference only after your attempt. No browser runner is provided.

### Reconciliation as a composition

Separate a reconciliation into aggregation, ordered unique keys and comparison. For each input row, unpack label and quantity; sum quantities in a dictionary specific to that input. Maintain a separate seen set and ordered list while scanning expected rows before actual rows. Then visit labels in that order, obtain missing totals with get(label, 0), and emit a difference row only when totals differ. For expected [["a", 2], ["a", 3]] and actual [["a", 4]], the expected total is 5, actual 4, delta -1. Comparing before aggregation would misclassify duplicate records. The pipeline combines previously taught frequency maps, order preservation and accumulators; no sorting or external data is required.

## Available challenges

- [Total Length of Short Labels](../../exercises/problem-solving/total-short-lengths/README.md) · Easy · 15 min
- [Most Frequent Label](../../exercises/problem-solving/most-frequent-label/README.md) · Medium · 25 min

- [Reconcile Inventory Records](../../exercises/problem-solving/inventory-reconciliation/README.md) · Hard · 40 min

<!-- chapter-navigation:bottom -->
[← Previous](../14-refactoring-challenges/README.md) · [Module index](../README.md) · [Next →](../16-timed-live-coding/README.md)
<!-- /chapter-navigation:bottom -->
