# First Matching Index

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.linear-first-index` · **Difficulty:** Easy · 12 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.md)

## Contract

Given an unsorted integer list and target, return the first matching index or -1 if absent. Do not mutate the input or use list.index.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

Write pseudocode and implement independently before opening the reference.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def first_index(values: list[int], target: int) -> int:
    raise NotImplementedError("Implement first_index")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[],3]` | `-1` |
| `[[8,4,4,9],4]` | `1` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Use enumerate to get index and value.

</details>

<details>
<summary>Hint 2</summary>

Check the value against the target.

</details>

<details>
<summary>Hint 3</summary>

Return on first match; return -1 only after the scan.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

Scanning in index order makes the first match definitive. The missing result is different from index zero.

- Time: O(n)
- Auxiliary space: O(1)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.md) · [Exercise index](../../README.md)
