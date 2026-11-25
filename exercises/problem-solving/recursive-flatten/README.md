# Flatten Nested Lists

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.recursive-flatten` · **Difficulty:** Hard · 35 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.md)
- [02-modifying-lists-and-methods](../../../collections/02-modifying-lists-and-methods/README.md)
- [05-type-and-isinstance](../../../fundamentals/05-type-and-isinstance/README.md)
- [04-recursion](../../../problem-solving-and-live-coding/04-recursion/README.md)
- [09-data-flow-between-functions](../../../functions/09-data-flow-between-functions/README.md)
- [10-functions-and-recursion](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.md)
- [04-scope](../../../functions/04-scope/README.md)
- [08-functions-working-together](../../../functions/08-functions-working-together/README.md)

## Contract

Given a finite nested list containing only integers and lists, with at most 10 nested list levels below the outer list, return a new flat list of integers in left-to-right depth-first order. Preserve duplicates and input. Use recursion; no cycles or shared mutable references are provided.

Only stated input domains are graded. Return exact types and values; do not print, mutate inputs or add dependencies. Algorithm choices and complexity require manual review; functional tests cannot prove them.

Copy the starter to a personal practice directory; Python 3.13 is the baseline. Browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def flatten(values: list) -> list[int]:
    raise NotImplementedError("Implement flatten")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[]]` | `[]` |
| `[[1,[2,[3]],4]]` | `[1,2,3,4]` |
| `[[[[]],[],[0]]]` | `[0]` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Use one result list shared by a recursive helper.

</details>

<details>
<summary>Hint 2</summary>

For each item, distinguish a list from an integer.

</details>

<details>
<summary>Hint 3</summary>

Visit a nested list immediately; append an integer directly.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

A helper traverses every list in order and appends each leaf integer once. Empty lists add nothing. Sharing one output accumulator avoids repeated copying; stack depth is the nesting depth.

- Time: O(n)
- Auxiliary space: O(h)

Fixed-cost model for bounded integer operations and bounded-length labels, expected hash behavior when applicable. n/m are input lengths (for nested lists n counts all visited items and list nodes), k distinct keys, h nesting depth. Required output excluded from auxiliary space; recursion uses O(h) frames.

</details>

## Validation

Check your own calls manually and add boundary cases. From the repository root, the command below tests trusted references and known incorrect implementations, not your personal code. Public solutions are inspectable; no AI grading.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.md) · [Exercise index](../../README.md)
