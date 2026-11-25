# Binary Target Range

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.binary-target-range` · **Difficulty:** Hard · 32 min

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
- [06-while-loops-and-state-driven-repetition](../../../program-flow/06-while-loops-and-state-driven-repetition/README.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.md)
- [11-searching-and-sorting](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.md)

## Contract

Given an ascending sorted integer list, return [first, last] inclusive indices of the target, or [-1, -1] if absent. Use two binary boundary searches, not a linear scan; preserve input. Sortedness is guaranteed.

Only stated input domains are graded. Return exact types and values; do not print, mutate inputs or add dependencies. Algorithm choices and complexity require manual review; functional tests cannot prove them.

Copy the starter to a personal practice directory; Python 3.13 is the baseline. Browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def target_range(values: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement target_range")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[],3]` | `[-1,-1]` |
| `[[2,4,4,4,7],4]` | `[1,3]` |
| `[[1,1,1],1]` | `[0,2]` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Find the first position whose value is at least target.

</details>

<details>
<summary>Hint 2</summary>

If it is absent or beyond the list, return the missing pair.

</details>

<details>
<summary>Hint 3</summary>

Find the first position whose value is strictly greater; subtract one for the last match.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

The two half-open searches find the boundaries of the contiguous block of equal values. The right boundary is exclusive. Checking the left boundary prevents reporting a nonexistent target.

- Time: O(log n)
- Auxiliary space: O(1)

Fixed-cost model for bounded integer operations and bounded-length labels, expected hash behavior when applicable. n/m are input lengths (for nested lists n counts all visited items and list nodes), k distinct keys, h nesting depth. Required output excluded from auxiliary space; recursion uses O(h) frames.

</details>

## Validation

Check your own calls manually and add boundary cases. From the repository root, the command below tests trusted references and known incorrect implementations, not your personal code. Public solutions are inspectable; no AI grading.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.md) · [Exercise index](../../README.md)
