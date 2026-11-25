# Timed: Longest Qualifying Streak

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.timed-longest-streak` · **Difficulty:** Medium · 20 min

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
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)
- [16-timed-live-coding](../../../problem-solving-and-live-coding/16-timed-live-coding/README.md)

## Contract

Return the longest contiguous run of integer values greater than or equal to threshold. Empty input or no qualifying values returns zero. A value below threshold breaks the run; preserve input.

Only stated input domains are graded. Return exact types and values; do not print, mutate inputs or add dependencies. Algorithm choices and complexity require manual review; functional tests cannot prove them.

Use a personal timer. Work independently, no hints, reference or AI during the first attempt. At the limit record progress, stop the clock, then finish and compare. Timing is self-reported, not graded by CI.

Copy the starter to a personal practice directory; Python 3.13 is the baseline. Browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def longest_streak(values: list[int], threshold: int) -> int:
    raise NotImplementedError("Implement longest_streak")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[],2]` | `0` |
| `[[2,2,0,3,4,2],2]` | `3` |
| `[[0,0],1]` | `0` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Keep the current run length and the best run length separately.

</details>

<details>
<summary>Hint 2</summary>

Reset the current length to zero on a failing value.

</details>

<details>
<summary>Hint 3</summary>

Update best after extending a run; do not add disconnected runs.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

The current counter describes the qualifying suffix ending at the current position. Resetting on a failure preserves contiguity. Tracking the maximum handles a run at the beginning, middle or end.

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
