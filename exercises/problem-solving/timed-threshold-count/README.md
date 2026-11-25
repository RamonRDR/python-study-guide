# Timed: Threshold Count

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.timed-threshold-count` · **Difficulty:** Easy · 10 min

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
- [01-conditions-comparisons-and-boolean-logic](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.md)
- [16-timed-live-coding](../../../problem-solving-and-live-coding/16-timed-live-coding/README.md)

## Contract

Return the number of integer values greater than or equal to threshold. Preserve the list; empty input returns zero. Count repeated occurrences, not distinct values.

Only stated input domains are graded. Return exact types and values; do not print, mutate inputs or add dependencies. Algorithm choices and complexity require manual review; functional tests cannot prove them.

Use a personal timer. Work independently, no hints, reference or AI during the first attempt. At the limit record progress, stop the clock, then finish and compare. Timing is self-reported, not graded by CI.

Copy the starter to a personal practice directory; Python 3.13 is the baseline. Browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def count_at_least(values: list[int], threshold: int) -> int:
    raise NotImplementedError("Implement count_at_least")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[],2]` | `0` |
| `[[2,2,3,1],2]` | `3` |
| `[[-3,-2,0],-2]` | `2` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Initialize a counter before iteration.

</details>

<details>
<summary>Hint 2</summary>

Use an inclusive comparison.

</details>

<details>
<summary>Hint 3</summary>

Return after processing the entire list.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

The counter counts exactly the qualifying elements already processed. An inclusive comparison handles equality and the empty loop leaves zero.

- Time: O(n)
- Auxiliary space: O(1)

Fixed-cost model for bounded integer operations and bounded-length labels, expected hash behavior when applicable. n/m are input lengths (for nested lists n counts all visited items and list nodes), k distinct keys, h nesting depth. Required output excluded from auxiliary space; recursion uses O(h) frames.

</details>

## Validation

Check your own calls manually and add boundary cases. From the repository root, the command below tests trusted references and known incorrect implementations, not your personal code. Public solutions are inspectable; no AI grading.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/16-timed-live-coding/README.md) · [Exercise index](../../README.md)
