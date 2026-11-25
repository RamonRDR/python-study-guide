# Functions and Recursion Challenges

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../09-collections/README.md) · [Module index](../README.md) · [Next →](../11-searching-and-sorting/README.md)
<!-- /chapter-navigation:top -->

Review parameters, returns and recursive base cases. Factorial multiplies positive integers up to n; integer power multiplies the same base repeatedly. Zero has an explicitly specified base result of one in both tasks.

Read the contract and linked prerequisite lessons, predict results, attempt the starter in a personal file, and check boundaries. Open hints progressively; compare the reference only after your attempt. No browser runner is provided.

### Recursive traversal of nested lists

A nested list is a finite hierarchy: each element is either an integer leaf or another list. In the recursive helper, loop over elements; append an integer to a shared result, or recursively visit a list before continuing with the next element. An empty list naturally returns after zero iterations. Use isinstance(item, list) to distinguish list nodes, and pass the same accumulator to the helper or define the helper inside the function so it can append to that list. In [1, [2, [3]], 4], visit 1, then descend into [2, [3]], append 2 and 3, return, then append 4. Do not append a whole nested list or concatenate copies at every depth. Assume finite acyclic input with bounded nesting. The call stack grows with depth, not with the number of leaves.

## Available challenges

- [Clamp a Value](../../exercises/problem-solving/clamp-value/README.md) · Easy · 10 min
- [Recursive Factorial](../../exercises/problem-solving/recursive-factorial/README.md) · Medium · 18 min
- [Recursive Integer Power](../../exercises/problem-solving/recursive-power/README.md) · Medium · 20 min

- [Flatten Nested Lists](../../exercises/problem-solving/recursive-flatten/README.md) · Hard · 35 min

<!-- chapter-navigation:bottom -->
[← Previous](../09-collections/README.md) · [Module index](../README.md) · [Next →](../11-searching-and-sorting/README.md)
<!-- /chapter-navigation:bottom -->
