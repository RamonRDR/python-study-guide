# Vowel Counter

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.vowel-counter` · **Difficulty:** Easy · **Estimated time:** 10 min

## Prerequisites

- [Strings and character access](../../../strings-and-numbers/01-string-creation-and-indexing/README.md)
- [String membership and normalization](../../../strings-and-numbers/02-common-string-methods/README.md)
- [Membership and Boolean conditions](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.md)
- [Iteration with for](../../../program-flow/04-for-loops-and-iteration/README.md)
- [Function definition](../../../functions/01-defining-and-calling-functions/README.md)
- [Parameters](../../../functions/02-parameters-and-arguments/README.md)
- [Return values](../../../functions/03-return-values/README.md)
- [Type hints](../../../functions/05-type-hints/README.md)
- [Accumulator and decomposition](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [Boundary tests](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [Complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)

## Goal

Implement count_vowels(text) and return the number of ASCII vowels A, E, I, O, U (uppercase or lowercase) in the input string. Count repeated occurrences; ignore every other character.

- Input is a Python str, including empty strings; other input types are outside the contract.
- Only the ten literal ASCII characters aeiouAEIOU count. Accented letters, y/Y, digits, punctuation, whitespace and other Unicode characters do not count.
- Return an int, not a string, Boolean or printed output. No external dependencies or input/output operations are needed.

Try independently first. Copy the starter to a personal practice directory; do not edit the repository reference solution. Python 3.13 is the baseline; the exercise uses only the standard language. Browser execution has not been verified. The public tests and solutions are visible, not secret.

[Starter](starter.py) · [Machine-readable record](exercise.json)

```python
def count_vowels(text: str) -> int:
    raise NotImplementedError("Implement count_vowels")
```

## Examples

| Input | Expected | Reason |
| --- | ---: | --- |
| `"Hello, World!"` | 3 | e, o and o count. |
| `"AEIOU"` | 5 | All five uppercase vowels count. |
| `""` | 0 | No characters to count. |
| `"Aéİu🙂"` | 2 | Only A and u count. |

## Progressive hints

<details>
<summary>Hint 1</summary>

What value should the counter have before reading any character?

</details>

<details>
<summary>Hint 2</summary>

Iterate over the original string with for; use a membership test against the literal ASCII vowel string.

</details>

<details>
<summary>Hint 3</summary>

Increment only on a match, then return the counter after the loop.

</details>

## Reference and explanation

<details>
<summary>Reveal after your attempt</summary>

[Reference solution](solution.py)

Start at zero. For each original character, increment once if it belongs to aeiouAEIOU. Return the accumulated count after the loop. This counts duplicates and handles uppercase without Unicode case conversion. Converting the entire string with lower() can turn U+0130 (İ) into an ASCII i plus a combining mark, changing the specified contract. Returning inside the loop would ignore later characters.

- Time: O(n), one pass over n Python string characters; membership in a fixed ten-character string is bounded.
- Space: O(1) auxiliary variables in the usual fixed-cost model; the counter uses O(log n) bits if arbitrary integer bit storage is counted.

</details>

## Validation

Test your own file manually by calling count_vowels with the inputs above and comparing returned integers. Add at least two new cases before looking at the reference. The repository command below, run from the root, verifies the reference and known incorrect implementations, not your personal file. It does not run arbitrary student code.

```bash
python -m unittest discover -s tests -p "test_problem_solving_pilot.py"
```

[Test source](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.md) · [Exercise index](../../README.md)
