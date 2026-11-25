# Detect a Duplicate

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.has-duplicate` · **Difficulty:** Medium · 18 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [05-sets-and-unique-values](../../../collections/05-sets-and-unique-values/README.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)

## Contract

Given an integer list, return True if any value occurs at two distinct positions, else False. Leave input unchanged. Aim for expected O(n) time using a set, not repeated full scans.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

Write pseudocode and implement independently before opening the reference.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def has_duplicate(values: list[int]) -> bool:
    raise NotImplementedError("Implement has_duplicate")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[]]` | `false` |
| `[[1]]` | `false` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Remember values seen in a set.

</details>

<details>
<summary>Hint 2</summary>

Check membership before adding a value.

</details>

<details>
<summary>Hint 3</summary>

If all values are new, return False after the loop.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

A hash set stores at most n distinct values and avoids scanning all earlier values for each element. Expected O(n) assumes ordinary hash behavior; output tests do not prove a time bound.

- Time: O(n) expected
- Auxiliary space: O(n)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.md) · [Exercise index](../../README.md)
