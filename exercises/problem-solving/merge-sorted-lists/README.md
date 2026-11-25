# Merge Sorted Lists

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.merge-sorted-lists` · **Difficulty:** Hard · 30 min

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
- [06-while-loops-and-state-driven-repetition](../../../program-flow/06-while-loops-and-state-driven-repetition/README.md)
- [06-sorting-algorithms](../../../problem-solving-and-live-coding/06-sorting-algorithms/README.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)
- [11-searching-and-sorting](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.md)

## Contract

Given two ascending sorted integer lists, return a new ascending list containing every occurrence from both inputs. Preserve both inputs and duplicates; use a two-pointer merge in O(n+m), not sorting the concatenation.

Only stated input domains are graded. Return exact types and values; do not print, mutate inputs or add dependencies. Algorithm choices and complexity require manual review; functional tests cannot prove them.

Copy the starter to a personal practice directory; Python 3.13 is the baseline. Browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    raise NotImplementedError("Implement merge_sorted")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[],[]]` | `[]` |
| `[[1,3],[2,4]]` | `[1,2,3,4]` |
| `[[1,1],[1,2]]` | `[1,1,1,2]` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Keep a pointer to the first unconsumed element of each list.

</details>

<details>
<summary>Hint 2</summary>

Append the smaller current element and advance only its pointer.

</details>

<details>
<summary>Hint 3</summary>

When one list is exhausted, append the remaining elements of the other.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

The output prefix is always sorted and contains exactly the consumed elements. Selecting the smaller head preserves order; draining the remainder preserves multiplicities. Each input position advances once.

- Time: O(n+m)
- Auxiliary space: O(1)

Fixed-cost model for bounded integer operations and bounded-length labels, expected hash behavior when applicable. n/m are input lengths (for nested lists n counts all visited items and list nodes), k distinct keys, h nesting depth. Required output excluded from auxiliary space; recursion uses O(h) frames.

</details>

## Validation

Check your own calls manually and add boundary cases. From the repository root, the command below tests trusted references and known incorrect implementations, not your personal code. Public solutions are inspectable; no AI grading.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.md) · [Exercise index](../../README.md)
