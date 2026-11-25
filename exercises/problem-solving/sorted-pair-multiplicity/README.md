# Count Target Pairs with Duplicates

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.sorted-pair-multiplicity` · **Difficulty:** Hard · 40 min

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
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.md)
- [12-algorithms-and-complexity](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.md)

## Contract

Given an ascending sorted integer list, count index pairs i < j whose values sum to target. Equal values at different indices are distinct occurrences; preserve input. Use grouped two pointers in O(n) time and constant auxiliary space.

Only stated input domains are graded. Return exact types and values; do not print, mutate inputs or add dependencies. Algorithm choices and complexity require manual review; functional tests cannot prove them.

Copy the starter to a personal practice directory; Python 3.13 is the baseline. Browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def count_target_pairs(values: list[int], target: int) -> int:
    raise NotImplementedError("Implement count_target_pairs")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[],4]` | `0` |
| `[[1,1,3,3,3],4]` | `6` |
| `[[2,2,2,2],4]` | `6` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Compare the two boundary values' sum to target.

</details>

<details>
<summary>Hint 2</summary>

On equality with distinct boundary values, count each run of equal values and multiply the counts.

</details>

<details>
<summary>Hint 3</summary>

If both boundary values are equal, all remaining positions have that value: add k(k-1)//2 and stop.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

Sortedness allows discarding an impossible boundary. When distinct matching groups have sizes a and b, all a*b cross-group pairs count. When both boundaries are equal, every pair of the remaining k positions counts once. Each pointer advances monotonically.

- Time: O(n)
- Auxiliary space: O(1)

Fixed-cost model for bounded integer operations and bounded-length labels, expected hash behavior when applicable. n/m are input lengths (for nested lists n counts all visited items and list nodes), k distinct keys, h nesting depth. Required output excluded from auxiliary space; recursion uses O(h) frames.

</details>

## Validation

Check your own calls manually and add boundary cases. From the repository root, the command below tests trusted references and known incorrect implementations, not your personal code. Public solutions are inspectable; no AI grading.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.md) · [Exercise index](../../README.md)
