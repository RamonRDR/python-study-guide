# Most Frequent Label

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.most-frequent-label` · **Difficulty:** Medium · 25 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)

## Contract

Return the exact label with the highest total frequency. If tied, choose the label that first appeared in the original list. Empty input returns None; empty string is a valid label. Preserve input and aim for expected linear time.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

Write pseudocode and implement independently before opening the reference.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def most_frequent_label(labels: list[str]) -> str | None:
    raise NotImplementedError("Implement most_frequent_label")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[]]` | `null` |
| `[["b","a","a","b"]]` | `"b"` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Build the final frequency map before choosing a winner.

</details>

<details>
<summary>Hint 2</summary>

Scan the original labels again, comparing their final counts.

</details>

<details>
<summary>Hint 3</summary>

Replace the winner only on strictly greater frequency, not equal frequency.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

A complete frequency pass followed by a left-to-right selection respects ties by first appearance. Strict improvement preserves the earlier winner.

- Time: O(n) expected
- Auxiliary space: O(k)

Complexity uses the fixed-cost model for bounded integer operations and string labels of bounded length; n is input length, m the second input length, k distinct values, d decimal digits, e exponent, as applicable. Output storage is excluded from auxiliary space. Hash-based times are expected, not worst-case bounds.

</details>

## Validation

Check your own calls manually using the stated cases and add at least two boundary cases. The following command at repository root tests only trusted reference and known incorrect implementations, not your own file. Public answers are inspectable; no AI grading is used.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/15-mixed-challenges/README.md) · [Exercise index](../../README.md)
