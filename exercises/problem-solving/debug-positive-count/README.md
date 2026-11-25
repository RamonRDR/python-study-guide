# Debug the Positive Counter

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.debug-positive-count` · **Difficulty:** Easy · 12 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [01-conditions-comparisons-and-boolean-logic](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.md)
- [01-manual-coding-and-debugging](../../../manual-programming-practices/01-manual-coding-and-debugging/README.md)

## Contract

Fix the supplied implementation so it returns the number of strictly positive integers in a list. Zero is not positive. Preserve input; return zero for empty lists.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

Reproduce the defect, trace the state, make a minimal fix, and rerun your cases.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def count_positive(values: list[int]) -> int:
    count = 0
    for value in values:
        if value >= 0:
            count += 1
    return count
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[]]` | `0` |
| `[[0]]` | `0` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Reproduce the bug with a one-element list containing zero.

</details>

<details>
<summary>Hint 2</summary>

Trace the condition for negative, zero and positive values.

</details>

<details>
<summary>Hint 3</summary>

Change the comparison so only strictly positive values increment the count.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

The original includes zero due to >=. A minimal change to > matches the specification; a zero-only regression case distinguishes both implementations.

- Time: O(n)
- Auxiliary space: O(1)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/13-debugging-challenges/README.md) · [Exercise index](../../README.md)
