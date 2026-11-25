# Longest Distinct Substring

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.longest-distinct-substring` · **Difficulty:** Hard · 35 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [01-string-creation-and-indexing](../../../strings-and-numbers/01-string-creation-and-indexing/README.md)
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)
- [08-strings-and-numbers](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.md)

## Contract

Return the length of the longest contiguous substring containing no repeated exact characters. Empty input returns 0. Compare original Python characters, not normalized text. Aim for expected linear time.

Only stated input domains are graded. Return exact types and values; do not print, mutate inputs or add dependencies. Algorithm choices and complexity require manual review; functional tests cannot prove them.

Copy the starter to a personal practice directory; Python 3.13 is the baseline. Browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def longest_distinct_length(text: str) -> int:
    raise NotImplementedError("Implement longest_distinct_length")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[""]` | `0` |
| `["abba"]` | `2` |
| `["abcabcbb"]` | `3` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Track the last position of each character.

</details>

<details>
<summary>Hint 2</summary>

If a repeated character lies inside the current window, move the left boundary past its last occurrence.

</details>

<details>
<summary>Hint 3</summary>

Never move left backwards; update best length after recording the current position.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

The current window contains unique characters. A repeated character invalidates only positions through its previous occurrence inside that window. max(left, previous + 1) preserves monotonic progress. Each right endpoint is visited once.

- Time: O(n) expected
- Auxiliary space: O(k)

Fixed-cost model for bounded integer operations and bounded-length labels, expected hash behavior when applicable. n/m are input lengths (for nested lists n counts all visited items and list nodes), k distinct keys, h nesting depth. Required output excluded from auxiliary space; recursion uses O(h) frames.

</details>

## Validation

Check your own calls manually and add boundary cases. From the repository root, the command below tests trusted references and known incorrect implementations, not your personal code. Public solutions are inspectable; no AI grading.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.md) · [Exercise index](../../README.md)
