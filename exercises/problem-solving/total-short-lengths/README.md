# Total Length of Short Labels

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.total-short-lengths` · **Difficulty:** Easy · 15 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [01-string-creation-and-indexing](../../../strings-and-numbers/01-string-creation-and-indexing/README.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.md)
- [01-conditions-comparisons-and-boolean-logic](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.md)

## Contract

Given exact strings and a nonnegative integer limit, return the sum of lengths of labels whose Python len is <= limit. Include repeated labels; empty labels contribute zero. Preserve input.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

Write pseudocode and implement independently before opening the reference.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def total_short_lengths(labels: list[str], limit: int) -> int:
    raise NotImplementedError("Implement total_short_lengths")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[["a","ab","abcd"],2]` | `3` |
| `[[],2]` | `0` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Separate determining a label's length from adding it.

</details>

<details>
<summary>Hint 2</summary>

Only add when the length is at most the limit.

</details>

<details>
<summary>Hint 3</summary>

Return the sum, not the number of qualifying labels.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

Compute each length once, compare it to the inclusive bound and accumulate lengths. This combines iteration, condition and a numeric accumulator.

- Time: O(n)
- Auxiliary space: O(1)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/15-mixed-challenges/README.md) · [Exercise index](../../README.md)
