# Recursive Integer Power

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.recursive-power` · **Difficulty:** Medium · 20 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [03-int-float-and-bool](../../../strings-and-numbers/03-int-float-and-bool/README.md)
- [04-recursion](../../../problem-solving-and-live-coding/04-recursion/README.md)

## Contract

Given an integer base from -10 to 10 and an exponent from 0 to 10, compute base raised to exponent by recursive multiplication, without ** or pow. Define exponent zero as 1, including 0**0.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

Write pseudocode and implement independently before opening the reference.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def integer_power(base: int, exponent: int) -> int:
    raise NotImplementedError("Implement integer_power")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[2,3]` | `8` |
| `[0,0]` | `1` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Use the exponent as the decreasing argument.

</details>

<details>
<summary>Hint 2</summary>

When exponent equals zero, return one.

</details>

<details>
<summary>Hint 3</summary>

Multiply the base by the result for exponent minus one.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

The recursive step reduces the exponent, not the base; negative bases work naturally because each step multiplies by the original base.

- Time: O(e)
- Auxiliary space: O(e)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.md) · [Exercise index](../../README.md)
