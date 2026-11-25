# Debug a Negative Window

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.debug-negative-window` · **Difficulty:** Medium · 22 min

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
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)
- [01-manual-coding-and-debugging](../../../manual-programming-practices/01-manual-coding-and-debugging/README.md)

## Contract

Fix the supplied fixed-window algorithm. Given an integer list and valid size 1 <= size <= len(values), return the largest sum of exactly size consecutive elements. All-negative lists are valid. Preserve input and use a single rolling window.

Only the stated input domain is graded; return the specified value and exact types, without printing, external dependencies or changing mutable arguments. Do not use the reference during the independent attempt.

Reproduce the defect, trace the state, make a minimal fix, and rerun your cases.

Copy the starter to a personal practice directory. Python 3.13 is the baseline; browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def max_window_sum(values: list[int], size: int) -> int:
    total = 0
    for index in range(size):
        total += values[index]
    best = max(0, total)
    for index in range(size, len(values)):
        total += values[index] - values[index - size]
        best = max(best, total)
    return best
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[-4,-2,-3],2]` | `-5` |
| `[[4,-1,3,2],2]` | `5` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Run the starter on [-4, -2, -3] with size 2.

</details>

<details>
<summary>Hint 2</summary>

Zero is not the sum of any valid window in that case.

</details>

<details>
<summary>Hint 3</summary>

Initialize best with the first actual window sum, then update it as the window moves.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

Initializing best at zero invents a nonexistent window when every sum is negative. The first actual sum establishes a valid baseline.

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
