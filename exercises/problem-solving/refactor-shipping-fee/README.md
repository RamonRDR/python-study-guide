# Refactor Shipping Fee

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.refactor-shipping-fee` · **Difficulty:** Easy · 15 min

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
- [02-if-elif-and-else](../../../program-flow/02-if-elif-and-else/README.md)
- [06-pep8-and-readability](../../../comments-and-documentation/06-pep8-and-readability/README.md)
- [03-test-driven-development](../../../manual-programming-practices/03-test-driven-development/README.md)

## Contract

Refactor the working starter without changing behavior. For nonnegative order totals in fictional units, shipping is free at total >= 100 or for members; otherwise it costs 12. Use one clear combined condition and avoid duplicate returns.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

The starter already passes functional tests. Preserve behavior, make the requested structural change and inspect the diff. Output tests do not grade readability or algorithm choice.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def shipping_fee(total: int, member: bool) -> int:
    if total >= 100:
        return 0
    if member:
        return 0
    return 12
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[99,false]` | `12` |
| `[100,false]` | `0` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Write boundary cases before editing.

</details>

<details>
<summary>Hint 2</summary>

Identify which two branches return the same value.

</details>

<details>
<summary>Hint 3</summary>

Combine the conditions with or; retain the fallback fee.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

The two free-shipping conditions form an inclusive OR. Consolidating them preserves output and makes the business rule visible.

- Time: O(1)
- Auxiliary space: O(1)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/14-refactoring-challenges/README.md) · [Exercise index](../../README.md)
