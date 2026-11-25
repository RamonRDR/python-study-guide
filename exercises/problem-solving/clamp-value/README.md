# Clamp a Value

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.clamp-value` · **Difficulty:** Easy · 10 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [02-if-elif-and-else](../../../program-flow/02-if-elif-and-else/README.md)

## Contract

Given integers with lower <= upper, return lower if value is below lower, upper if above upper, otherwise value. Equal bounds are valid.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

Write pseudocode and implement independently before opening the reference.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def clamp_value(value: int, lower: int, upper: int) -> int:
    raise NotImplementedError("Implement clamp_value")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[2,3,9]` | `3` |
| `[10,3,9]` | `9` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Compare the value to the lower bound.

</details>

<details>
<summary>Hint 2</summary>

Compare to the upper bound if needed.

</details>

<details>
<summary>Hint 3</summary>

Return the original value if neither condition holds.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

Separate early returns make each of the three mutually exclusive outcomes explicit.

- Time: O(1)
- Auxiliary space: O(1)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.md) · [Exercise index](../../README.md)
