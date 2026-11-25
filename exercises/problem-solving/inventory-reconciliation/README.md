# Reconcile Inventory Records

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.inventory-reconciliation` · **Difficulty:** Hard · 40 min

## Prerequisites

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.md)
- [03-return-values](../../../functions/03-return-values/README.md)
- [05-type-hints](../../../functions/05-type-hints/README.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.md)
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.md)
- [02-modifying-lists-and-methods](../../../collections/02-modifying-lists-and-methods/README.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.md)
- [09-data-flow-between-functions](../../../functions/09-data-flow-between-functions/README.md)
- [15-mixed-challenges](../../../problem-solving-and-live-coding/15-mixed-challenges/README.md)

- [05-sets-and-unique-values](../../../collections/05-sets-and-unique-values/README.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.md)
- [03-tuples-and-immutability](../../../collections/03-tuples-and-immutability/README.md)

## Contract

Each input is a list of [label, quantity] rows, with exact string labels and nonnegative integer quantities. Aggregate duplicates separately, then return rows [label, expected_total, actual_total, actual_total - expected_total] only for labels with unequal totals. Order rows by first appearance in expected followed by first appearance of labels exclusive to actual. Missing quantities are zero; preserve inputs.

Only stated input domains are graded. Return exact types and values; do not print, mutate inputs or add dependencies. Algorithm choices and complexity require manual review; functional tests cannot prove them.

Copy the starter to a personal practice directory; Python 3.13 is the baseline. Browser execution is unverified.

[Starter](starter.py) · [Record](exercise.json)

```python
def reconcile(expected: list[list], actual: list[list]) -> list[list]:
    raise NotImplementedError("Implement reconcile")
```

## Examples (positional arguments)

| Arguments (JSON) | Expected (JSON) |
| --- | --- |
| `[[],[]]` | `[]` |
| `[[["a",2],["a",3]],[["a",4]]]` | `[["a",5,4,-1]]` |
| `[[["b",2],["a",1]],[["a",1],["c",3]]]` | `[["b",2,0,-2],["c",0,3,3]]` |

## Progressive hints

<details>
<summary>Hint 1</summary>

Build two independent dictionaries of totals.

</details>

<details>
<summary>Hint 2</summary>

Build the ordered unique label sequence across both inputs.

</details>

<details>
<summary>Hint 3</summary>

Compare totals with zero defaults and append only nonzero differences.

</details>

## Reference and explanation

<details>
<summary>Reveal after attempting</summary>

[Reference solution](solution.py)

Separate aggregation from ordering and comparison. The seen set prevents duplicate output rows; preserving first appearance does not require sorting. A zero default makes absent labels and explicitly zero quantities equivalent.

- Time: O(n+m) expected
- Auxiliary space: O(k)

Fixed-cost model for bounded integer operations and bounded-length labels, expected hash behavior when applicable. n/m are input lengths (for nested lists n counts all visited items and list nodes), k distinct keys, h nesting depth. Required output excluded from auxiliary space; recursion uses O(h) frames.

</details>

## Validation

Check your own calls manually and add boundary cases. From the repository root, the command below tests trusted references and known incorrect implementations, not your personal code. Public solutions are inspectable; no AI grading.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Test fixture](test_solution.py) · [Back to chapter](../../../problem-solving-and-live-coding/15-mixed-challenges/README.md) · [Exercise index](../../README.md)
