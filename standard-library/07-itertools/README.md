<div align="center">

# Engineering Lazy Iterator Pipelines with `itertools`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Standard Library](../README.md) · [← Previous chapter: Collections](../06-collections/README.md)

Earlier chapters introduced `for`, iterables, the basic iterable-versus-iterator distinction, and helpers such as `range()`, `enumerate()`, and `zip()`. This chapter goes further: it studies `itertools` as a toolkit for composing **lazy iterator pipelines** with explicit consumption, buffering, grouping, and combinatoric contracts.

The central question is:

```text
Can this transformation be expressed as a stream of values
without materializing every intermediate collection?
```

`itertools` is powerful because its functions return iterators. That can reduce intermediate memory use and make data-flow intent precise, but it also means consumption order matters.

**Estimated study time:** 170–220 minutes.

**Python requirement:** Python 3.10 or newer for the core material and executable examples. Version-sensitive sections identify `batched()` (3.12) and `batched(strict=...)` (3.13).

**Documentation baseline:** behavior and version notes were checked against the official Python 3.14 `itertools` documentation and Functional Programming HOWTO.

## Learning objectives

By the end of this chapter, you should be able to:

- explain why `itertools` is an iterator-algebra toolkit rather than a collection module;
- distinguish lazy pipeline construction from eager materialization;
- reason about one-shot iterator consumption;
- combine streams with `chain()` and `chain.from_iterable()`;
- batch finite input deliberately and understand `batched(strict=...)` version requirements;
- slice streams with `islice()` without assuming sequence semantics;
- compare neighboring elements with `pairwise()`;
- select elements with `compress()`, `filterfalse()`, `dropwhile()`, and `takewhile()`;
- build running state with `accumulate()`;
- apply pre-grouped argument tuples with `starmap()`;
- bound infinite iterators such as `count()`, `cycle()`, and `repeat()`;
- align unequal streams with `zip_longest()`;
- understand `tee()` buffering and thread-safety limitations;
- use `groupby()` for consecutive runs instead of SQL-style global grouping;
- estimate the growth of `product()`, `permutations()`, and combinations before consuming them;
- test iterator pipelines without accidentally hiding consumption bugs.

## 1. What this chapter adds after earlier iteration chapters

Earlier chapters already established:

```text
for item in iterable
range() -> numeric progression
enumerate() -> position + item
zip() -> parallel items
```

This chapter adds a more compositional model:

```text
source
  -> transform lazily
  -> select lazily
  -> combine lazily
  -> consume at an intentional boundary
```

The goal is not to replace readable loops. It is to recognize when a pipeline expresses the data flow more directly.

## 2. `itertools` functions build iterators

The official documentation describes the module as a set of fast, memory-efficient iterator building blocks.

```python
from itertools import islice

numbers = iter(range(100))
first_five = islice(numbers, 5)

print(type(first_five))
```

`islice()` does not return a list. It returns an iterator that produces values when consumed.

## 3. Lazy does not mean free

Laziness usually means work is deferred until iteration asks for a value.

```python
from itertools import chain

stream = chain([1, 2], [3, 4])
print(next(stream))
```

Only enough work is performed to provide the requested value.

But lazy pipelines can still:

- consume CPU;
- retain buffered values;
- hold references to objects;
- eventually materialize data at a consumer;
- become infinite.

"Lazy" describes evaluation timing, not zero cost.

## 4. Iterators are usually single-pass

```python
values = iter([10, 20, 30])

print(list(values))
print(list(values))
```

Output:

```text
[10, 20, 30]
[]
```

The first conversion exhausts the iterator. The second sees no remaining values.

This consumption model is central to `itertools`.

## 5. Choose the materialization boundary deliberately

A useful pipeline often stays lazy until the program needs a concrete result:

```python
from itertools import islice

stream = (number * number for number in range(1_000_000))
preview = list(islice(stream, 3))
print(preview)
```

Here, only the preview is materialized.

Materialize because the next operation needs a collection, not merely because `list(...)` is familiar.

## 6. Import the tools that communicate the pipeline

```python
from itertools import (
    accumulate,
    chain,
    combinations,
    groupby,
    islice,
    pairwise,
    product,
    tee,
    zip_longest,
)
```

Specific imports make the vocabulary of the pipeline visible.

# Part I: composing and shaping streams

## 7. `chain()` concatenates iterables lazily

```python
from itertools import chain

combined = chain(["a", "b"], ("c", "d"), "ef")
print(list(combined))
```

Output:

```text
['a', 'b', 'c', 'd', 'e', 'f']
```

`chain()` consumes the first iterable, then the next, and so on.

## 8. `chain()` is not a merge algorithm

`chain()` does not sort, deduplicate, align, or compare inputs.

```text
input A -> all values
input B -> all values
input C -> all values
```

If the real requirement is sorted merging or keyed reconciliation, choose a tool that models that contract instead.

## 9. `chain.from_iterable()` flattens one level

```python
from itertools import chain

pages = [[1, 2], [3], [4, 5]]
flattened = chain.from_iterable(pages)
print(list(flattened))
```

Output:

```text
[1, 2, 3, 4, 5]
```

It flattens one iterable-of-iterables level. It is not a recursive arbitrary-depth flattening function.

## 10. `chain.from_iterable()` keeps the outer source lazy

The outer iterable itself can be lazy:

```python
from itertools import chain

rows = ([number, number * 10] for number in range(3))
print(list(chain.from_iterable(rows)))
```

The next inner iterable is requested as the chain advances.

## 11. `batched()` creates non-overlapping tuples

Python 3.12 added `itertools.batched()`:

```python
from itertools import batched

print(list(batched("ABCDEFG", 3)))
```

On Python 3.12+ the result is:

```text
[('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
```

The final batch may be shorter than `n`.

## 12. `batched(strict=True)` makes full batches a contract

Python 3.13 added the `strict` parameter:

```python
from itertools import batched

print(list(batched([1, 2, 3, 4], 2, strict=True)))
```

If the final batch is incomplete, `strict=True` raises `ValueError`.

Use strict mode when incomplete data should be treated as invalid rather than as a valid smaller batch.

## 13. `batched()` consumes only enough for the next batch

The implementation is lazy with respect to the input. It requests enough values to fill the next tuple, yields it, and then continues.

That makes batching suitable for streams where building a complete list first would be unnecessary.

## 14. `islice()` slices iterables, not sequences

```python
from itertools import islice

stream = iter(range(20))
print(list(islice(stream, 2, 10, 3)))
```

Output:

```text
[2, 5, 8]
```

`islice()` expresses start, stop, and step over iteration.

## 15. `islice()` does not support negative indexes

Sequence slicing can work backward from the end because a sequence can know its length and support indexed access.

An arbitrary iterator may have no known end at all.

Therefore negative `start`, negative `stop`, and non-positive `step` values are not supported by `islice()`.

## 16. Slicing a stream advances the source

```python
from itertools import islice

source = iter([0, 1, 2, 3, 4, 5])
print(list(islice(source, 3)))
print(list(source))
```

Output:

```text
[0, 1, 2]
[3, 4, 5]
```

`islice()` does not copy the input iterator. It consumes from it.

## 17. A stepped `islice()` still consumes skipped values

If an input is an iterator, fully consuming an `islice()` advances the input according to the slice bounds even when not every traversed value is yielded.

This matters when another part of the program continues using the same underlying iterator afterward.

## 18. `pairwise()` exposes adjacent relationships

Python 3.10 added `pairwise()`:

```python
from itertools import pairwise

readings = [10, 15, 13, 18]
for previous, current in pairwise(readings):
    print(previous, current)
```

Output:

```text
10 15
15 13
13 18
```

It is ideal for transitions, deltas, edges, and adjacent comparisons.

## 19. `pairwise()` produces one fewer result

An input with `n` values yields `n - 1` pairs when `n >= 1`.

Inputs with fewer than two elements produce no pairs.

That boundary behavior should be part of tests when pair counts matter.

# Part II: selecting and stopping

## 20. `compress()` applies a Boolean selector stream

```python
from itertools import compress

names = ["Ana", "Bo", "Cy", "Di"]
selected = [True, False, True, False]
print(list(compress(names, selected)))
```

Output:

```text
['Ana', 'Cy']
```

The data and selector iterables advance together.

## 21. `compress()` stops when either input ends

A shorter selector stream truncates the result even if more data remains.

That is a zip-like alignment contract. Validate lengths separately if unequal lengths represent malformed input.

## 22. `filterfalse()` keeps predicate failures

```python
from itertools import filterfalse

numbers = [1, 2, 3, 4, 5]
print(list(filterfalse(lambda value: value % 2 == 0, numbers)))
```

Output:

```text
[1, 3, 5]
```

It is the inverse-selection counterpart to `filter()`.

## 23. `dropwhile()` changes behavior after the first failure

```python
from itertools import dropwhile

values = [1, 2, 5, 2, 1]
print(list(dropwhile(lambda value: value < 4, values)))
```

Output:

```text
[5, 2, 1]
```

After the predicate first becomes false, all remaining elements are yielded without further filtering.

## 24. `dropwhile()` is not `filterfalse()`

For the same predicate:

```text
dropwhile -> discard only the leading matching prefix
filterfalse -> test every element and keep every failure
```

The names encode different stream shapes.

## 25. `takewhile()` stops at the first failure

```python
from itertools import takewhile

values = [1, 2, 5, 2, 1]
print(list(takewhile(lambda value: value < 4, values)))
```

Output:

```text
[1, 2]
```

Unlike `filter()`, values after the first failure are never considered by `takewhile()`.

## 26. `takewhile()` consumes the first failing element

This is a subtle but important contract.

```python
from itertools import takewhile

source = iter([1, 2, 5, 6])
print(list(takewhile(lambda value: value < 4, source)))
print(list(source))
```

Output:

```text
[1, 2]
[6]
```

The failing `5` was consumed in order to discover that the prefix should stop.

# Part III: running state and argument application

## 27. `accumulate()` emits running results

```python
from itertools import accumulate

print(list(accumulate([2, 3, 4])))
```

Output:

```text
[2, 5, 9]
```

The default operation is addition.

## 28. `accumulate()` differs from `sum()` and `reduce()`

```text
accumulate -> every running result
sum        -> final additive total
reduce     -> final accumulated result
```

Choose according to whether intermediate states are part of the required output.

## 29. `accumulate()` accepts another binary function

```python
from itertools import accumulate

values = [3, 1, 5, 2]
print(list(accumulate(values, max)))
```

Output:

```text
[3, 3, 5, 5]
```

Running minima, maxima, products, balances, and state transitions can all fit the same contract.

## 30. `initial=` changes both state and output length

```python
from itertools import accumulate

print(list(accumulate([1, 2, 3], initial=10)))
```

Output:

```text
[10, 11, 13, 16]
```

With `initial`, the initial value itself is emitted first, so the output has one more element than the input.

## 31. The accumulation function receives state then element

Conceptually:

```text
new_state = function(previous_state, next_element)
```

This argument order matters when the function is not commutative.

## 32. `starmap()` unpacks argument tuples

```python
from itertools import starmap

arguments = [(2, 5), (3, 2), (10, 3)]
print(list(starmap(pow, arguments)))
```

Output:

```text
[32, 9, 1000]
```

It is useful when an iterable already contains argument tuples.

## 33. `map()` and `starmap()` model different input shapes

```text
map(function, a, b)       -> function(a_item, b_item)
starmap(function, tuples) -> function(*tuple_item)
```

Choose based on how arguments are represented upstream.

# Part IV: infinite iterators

## 34. Infinite iterators require a termination design

`count()`, `cycle()`, and `repeat()` can produce values indefinitely.

An infinite source is not inherently dangerous. An **unbounded consumer** is the problem.

Design the limit before consuming the stream.

## 35. `count()` creates an arithmetic progression

```python
from itertools import count, islice

numbers = count(10, 3)
print(list(islice(numbers, 5)))
```

Output:

```text
[10, 13, 16, 19, 22]
```

`count()` is useful when the progression itself should remain an iterator.

## 36. Floating-point `count()` can accumulate error

The official documentation notes that better floating-point accuracy can sometimes be achieved by deriving each value from an integer index:

```python
from itertools import count, islice

values = (0.1 * index for index in count())
print(list(islice(values, 4)))
```

For exact decimal business rules, the next chapter will introduce `decimal`.

## 37. `repeat()` supplies a constant stream

```python
from itertools import repeat

print(list(repeat("x", 3)))
```

Output:

```text
['x', 'x', 'x']
```

Without the second argument, repetition is infinite.

## 38. `repeat()` composes naturally with `map()`

```python
from itertools import repeat

print(list(map(pow, [2, 3, 4], repeat(2))))
```

Output:

```text
[4, 9, 16]
```

The repeated constant supplies the same exponent to every call.

## 39. `cycle()` repeats the input sequence indefinitely

```python
from itertools import cycle, islice

rotating = cycle(["A", "B", "C"])
print(list(islice(rotating, 7)))
```

Output:

```text
['A', 'B', 'C', 'A', 'B', 'C', 'A']
```

## 40. `cycle()` stores input values for later repeats

To repeat an arbitrary iterable, `cycle()` saves values as it encounters them.

Therefore its auxiliary memory can grow with the size of the original finite input.

Do not interpret "iterator" as "constant memory" automatically.

## 41. Bound infinite streams close to the source

A readable pattern is:

```python
from itertools import count, islice

limited = islice(count(1), 5)
print(list(limited))
```

Putting the bound near the infinite producer makes termination easier to audit.

# Part V: alignment and fan-out

## 42. `zip_longest()` aligns until the longest input ends

```python
from itertools import zip_longest

left = [1, 2, 3]
right = ["a"]
print(list(zip_longest(left, right, fillvalue="-")))
```

Output:

```text
[(1, 'a'), (2, '-'), (3, '-')]
```

This contrasts with normal `zip()`, which stops at the shortest iterable.

## 43. `zip_longest()` and `zip(strict=True)` represent different policies

```text
zip()                -> shortest wins
zip(strict=True)     -> unequal lengths are invalid
zip_longest()        -> longest wins; missing values are filled
```

Choose the policy that matches the data contract instead of repairing mismatches afterward.

## 44. An infinite input can make `zip_longest()` infinite

If any input can continue forever, `zip_longest()` can also continue forever.

Wrap the result with a limiting tool such as `islice()` when the consumer must be finite.

## 45. `tee()` creates independent iterator views

```python
from itertools import tee

source = iter([10, 20, 30])
left, right = tee(source, 2)

print(next(left))
print(list(right))
print(list(left))
```

Output:

```text
10
[10, 20, 30]
[20, 30]
```

Each returned iterator has its own logical position.

## 46. `tee()` independence requires buffering

If one branch runs ahead, `tee()` must retain values until slower branches consume them.

The memory cost therefore depends on how far the consumers diverge.

## 47. Prefer materialization when consumers are far apart

The official documentation notes that if one branch consumes most or all data before another branch starts, converting to a list can be faster than `tee()`.

`tee()` is valuable for coordinated streaming consumers, not automatically for every "use twice" requirement.

## 48. `tee()` iterators are not thread-safe

Simultaneous use of iterators returned by the same `tee()` call is not thread-safe and may raise `RuntimeError`.

Do not treat `tee()` as a concurrency primitive.

## 49. Avoid mixing the original iterator with its tee branches

After creating branches, keep consuming through the branches rather than continuing to use the original iterator in unrelated code.

A single ownership path makes buffering and consumption behavior much easier to reason about.

# Part VI: grouping consecutive runs

## 50. `groupby()` groups consecutive equal keys

```python
from itertools import groupby

values = ["A", "A", "B", "B", "A"]
for key, group in groupby(values):
    print(key, list(group))
```

Output:

```text
A ['A', 'A']
B ['B', 'B']
A ['A']
```

The final `A` starts a new group because it is not adjacent to the first `A` run.

## 51. `groupby()` is not SQL `GROUP BY`

SQL-style grouping usually collects all rows that share a key regardless of position.

`itertools.groupby()` starts a new group whenever the key changes.

Think **runs**, not global buckets.

## 52. Sort first when global-by-key grouping is intended

```python
from itertools import groupby
from operator import itemgetter

records = [("b", 2), ("a", 1), ("b", 3)]
records.sort(key=itemgetter(0))

for key, group in groupby(records, key=itemgetter(0)):
    print(key, list(group))
```

Sorting by the same key function brings equal keys together first.

## 53. Group iterators share the underlying source

The `group` returned by `groupby()` is itself an iterator over the shared input.

When the outer `groupby()` advances, a previous group may no longer be available.

Materialize a group if it must survive beyond the current outer iteration.

## 54. `groupby()` can express run-length encoding

```python
from itertools import groupby

values = "AAABBCCCCA"
runs = [(key, len(list(group))) for key, group in groupby(values)]
print(runs)
```

Output:

```text
[('A', 3), ('B', 2), ('C', 4), ('A', 1)]
```

This preserves run boundaries rather than collapsing all equal values.

# Part VII: combinatoric iterators

## 55. `product()` models a Cartesian product

```python
from itertools import product

print(list(product(["A", "B"], [1, 2])))
```

Output:

```text
[('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

It is equivalent in meaning to nested loops over each input pool.

## 56. `product()` consumes input pools before yielding combinations

Although `product()` returns an iterator, it first consumes each input iterable into in-memory pools.

Therefore it requires finite inputs and its input-side memory behavior is different from tools such as `chain()`.

## 57. `repeat=` multiplies product dimensions

```python
from itertools import product

print(list(product([0, 1], repeat=2)))
```

Output:

```text
[(0, 0), (0, 1), (1, 0), (1, 1)]
```

The number of results grows multiplicatively with each dimension.

## 58. `permutations()` models ordered selections

```python
from itertools import permutations

print(list(permutations("ABC", 2)))
```

Output:

```text
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

Order matters, and positions are not reused within one permutation.

## 59. Combinatoric uniqueness is positional

If equal values appear at different input positions, the tools still treat those positions as distinct choices.

Do not assume duplicate input values will automatically produce deduplicated output tuples.

## 60. `combinations()` ignores ordering of a chosen subset

```python
from itertools import combinations

print(list(combinations("ABC", 2)))
```

Output:

```text
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

`('B', 'A')` is not another combination because the same two positions have already been chosen.

## 61. `combinations_with_replacement()` allows position reuse

```python
from itertools import combinations_with_replacement

print(list(combinations_with_replacement("AB", 2)))
```

Output:

```text
[('A', 'A'), ('A', 'B'), ('B', 'B')]
```

This is useful when repeating a choice is allowed and order does not create a new result.

## 62. Estimate cardinality before consuming

Small inputs can produce large outputs quickly.

Useful formulas include:

```text
product sizes       -> multiply pool sizes
permutations(n, r)  -> n! / (n-r)!
combinations(n, r)  -> n! / (r! * (n-r)!)
```

Python's `math.perm()` and `math.comb()` can estimate two of these counts without generating the tuples.

## 63. An iterator can still represent an enormous computation

Returning values lazily prevents a giant result list from being created automatically, but it does not reduce the number of combinations that must be generated if you consume all of them.

Laziness protects intermediate storage, not algorithmic complexity.

# Part VIII: pipeline design

## 64. Compose left-to-right around a clear source

```python
from itertools import chain, islice

pages = [[1, 2], [3, 4], [5, 6]]
stream = chain.from_iterable(pages)
preview = islice(stream, 4)
print(list(preview))
```

Output:

```text
[1, 2, 3, 4]
```

Each stage answers one question: flatten, limit, consume.

## 65. Generator expressions and `itertools` complement each other

```python
from itertools import islice

squares = (number * number for number in range(100))
print(list(islice(squares, 5)))
```

Use generator expressions for simple custom expressions and `itertools` for reusable iteration patterns.

## 66. Do not compress every loop into a pipeline

A multi-step loop may be clearer when it contains:

- complex branching;
- several side effects;
- error handling per item;
- mutable state that deserves explicit names.

Pipeline style is a design option, not a code-golf requirement.

## 67. Name meaningful stages

Prefer:

```python
from itertools import chain, islice

rows = [[1, 2], [3], [4, 5]]
flattened = chain.from_iterable(rows)
preview = islice(flattened, 3)
print(list(preview))
```

over a deeply nested expression when intermediate names explain the model.

## 68. Document ownership of shared iterators

When multiple helpers consume the same iterator, make it clear which stage owns the next value.

Bugs involving `takewhile()`, `islice()`, `groupby()`, or `tee()` are often consumption bugs rather than arithmetic bugs.

## 69. Test partial consumption, not only final lists

A useful iterator test can inspect what remains:

```python
from itertools import islice

source = iter([1, 2, 3, 4])
assert list(islice(source, 2)) == [1, 2]
assert list(source) == [3, 4]
```

This verifies the consumption contract directly.

## 70. Bound infinite tests explicitly

Never write a test that tries to materialize an infinite iterator.

Use `islice()`, a finite `repeat(..., times)`, or another explicit stopping condition.

## 71. Four executable examples in this chapter

The `examples/` directory contains deterministic programs:

```text
lazy_pipeline.py
pairwise_deltas.py
groupby_runs.py
combinatoric_options.py
```

They are intentionally small enough for unattended CI and use Python 3.10-compatible `itertools` APIs.

## 72. Common mistakes

### Mistake 1: materializing every stage

```python
values = list(range(1_000_000))
```

when the consumer only needs a short prefix.

Better: preserve laziness until a concrete collection is needed.

### Mistake 2: reusing an exhausted iterator

A consumed iterator does not restart automatically.

### Mistake 3: expecting `groupby()` to collect non-adjacent equal keys

It groups consecutive runs.

### Mistake 4: forgetting that `takewhile()` consumes the failing value

That value is not available to a later consumer of the same source iterator.

### Mistake 5: assuming `tee()` duplicates data for free

Lagging branches cause buffering.

### Mistake 6: using an infinite iterator without a visible bound

The pipeline may never terminate.

### Mistake 7: treating lazy combinatorics as cheap combinatorics

The result count can still explode.

### Mistake 8: using `islice()` like ordinary sequence slicing

Negative indexes are unsupported and traversed elements are consumed.

## 73. Practical exercise

Build a small event-analysis pipeline.

Requirements:

1. Start with several pages of integer measurements, represented as a list of lists.
2. Flatten one level with `chain.from_iterable()`.
3. Use `islice()` to inspect only the first eight measurements.
4. Use `pairwise()` to calculate adjacent differences.
5. Classify each difference as `"up"`, `"down"`, or `"same"`.
6. Use `groupby()` to summarize consecutive classification runs.
7. Do not materialize the full flattened source before the preview boundary.

Bonus: explain which stages consume their input and where materialization occurs.

## 74. Quick reference

```text
chain(a, b, c)                  concatenate iterables
chain.from_iterable(rows)       flatten one level
batched(iterable, n)            non-overlapping batches [Python 3.12+]
batched(..., strict=True)       require complete batches [Python 3.13+]
islice(iterable, ...)           lazy positive slicing
pairwise(iterable)              adjacent pairs
compress(data, selectors)       Boolean-mask selection
filterfalse(predicate, items)   keep predicate failures
dropwhile(predicate, items)     drop leading matching prefix
takewhile(predicate, items)     keep leading matching prefix
accumulate(items, func)         running state
starmap(func, argument_tuples)  call func(*args)
count(start, step)              infinite arithmetic progression
cycle(iterable)                 repeat saved input indefinitely
repeat(value, times=None)       repeat one object
zip_longest(..., fillvalue=x)   align until longest input ends
tee(iterable, n)                fork logical iterator positions
groupby(iterable, key)          group consecutive equal keys
product(...)                    Cartesian product
permutations(items, r)          ordered selections
combinations(items, r)          unordered selections
combinations_with_replacement   unordered selections with reuse
```

## 75. Design checklist

Before adding an `itertools` stage, ask:

- Is the source finite or potentially infinite?
- Who owns consumption of this iterator?
- Is the stage lazy, buffered, or internally materializing input?
- Will another consumer need the values afterward?
- Does a boundary helper consume a sentinel or failing value?
- Should unequal input lengths truncate, fail, or fill?
- Is grouping consecutive or global?
- Can branch divergence make `tee()` expensive?
- How many combinatoric outputs can this request generate?
- Where should the pipeline become a concrete collection?
- Would an explicit loop be easier to understand?
- Am I depending on a version-specific API?

## 76. Connections to other Python concepts

`itertools` connects directly to topics already studied:

- **`for` loops and iteration:** every itertool ultimately participates in Python's iterator protocol.
- **`range()`, `enumerate()`, and `zip()`:** these built-ins are natural neighbors of iterator pipelines.
- **Functions:** predicates, key functions, and binary accumulation functions are passed as behavior.
- **Collections:** `chain()` streams through containers; `groupby()` exposes group iterators; combinatoric tools often pool finite inputs.
- **Generators:** generator expressions and itertools stages compose naturally without eager intermediate lists.
- **Algorithms:** laziness changes storage behavior but does not erase time complexity or combinatoric growth.
- **Testing:** iterator ownership and partial-consumption behavior are contracts worth asserting directly.
- **Upcoming `decimal`:** exact arithmetic becomes important when numeric iterator pipelines represent money or other precision-sensitive values.

## References

Primary references used for this chapter:

- [Python 3.14 documentation: `itertools` — Functions creating iterators for efficient looping](https://docs.python.org/3.14/library/itertools.html)
- [Python 3.14 Functional Programming HOWTO — Iterators, generators, and `itertools`](https://docs.python.org/3.14/howto/functional.html)
- [Python 3.14 built-in `zip()` documentation, including `strict=True`](https://docs.python.org/3.14/library/functions.html#zip)
- [Python 3.14 `math.comb()` and `math.perm()` documentation](https://docs.python.org/3.14/library/math.html#combinatorics)

## Next chapter

Continue with [Chapter 08: `decimal`](../08-decimal/README.md).

The next chapter moves from lazy iteration contracts to **numeric precision contracts**: decimal representation, contexts, rounding, traps, quantization, and exact arithmetic for values where binary floating-point behavior is not the desired model.
