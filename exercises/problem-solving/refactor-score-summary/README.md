# Refactor Score Summary

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.refactor-score-summary` · **Difficulty:** Medium · 22 min

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
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.md)
- [06-pep8-and-readability](../../../comments-and-documentation/06-pep8-and-readability/README.md)
- [03-test-driven-development](../../../manual-programming-practices/03-test-driven-development/README.md)

## Contract

Refactor the working starter for integer scores 0–100. Return a dictionary with total, passed and failed counts; a score >= 60 passes. Keep input unchanged. Use descriptive names and one classification pass; review clarity manually.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

The starter already passes functional tests. Preserve behavior, make the requested structural change and inspect the diff. Output tests do not grade readability or algorithm choice.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def summarize_scores(scores: list[int]) -> dict[str, int]:
    a = 0
    for x in scores:
        if x >= 60:
            a += 1
    b = 0
    for x in scores:
        if x < 60:
            b += 1
    return {"total": len(scores), "passed": a, "failed": b}
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[]]` | `{"total":0,"passed":0,"failed":0}` |
| `[[59,60,61]]` | `{"total":3,"passed":2,"failed":1}` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Preserve the contract and write boundary tests around 60.

</details>

<details>
<summary>Hint 2</summary>

Count passing scores in one loop with a descriptive variable.

</details>

<details>
<summary>Hint 3</summary>

Compute failed as total minus passed; verify all original cases.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

Each score is either passing or failing, so failed is total minus passed. A single classification loop avoids repeated work. Tests check behavior, not readability.

- Time: O(n)
- Auxiliary space: O(1)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/14-refactoring-challenges/README.md) · [Exercise index](../../README.md)
