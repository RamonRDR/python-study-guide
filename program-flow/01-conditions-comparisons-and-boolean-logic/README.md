<div align="center">

# Conditions, Comparisons, and Boolean Logic

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Program Flow](../README.md) · [← Previous phase: Choosing the Right Collection](../../collections/06-choosing-the-right-collection/README.md) · [Next: `if`, `elif`, and `else` →](../02-if-elif-and-else/README.md)

Conditions are the questions a program can evaluate before it decides what should happen next.

You already met pieces of this idea in earlier phases. Comparisons such as `score >= 70` produce Boolean values, membership tests such as `"lists" in topics` answer whether a value is present, and `bool()` shows how Python interprets many values as true or false.

This chapter connects those pieces before introducing `if`. The goal is to understand the expressions that later control decisions and loops.

**Estimated study time:** 100–125 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- use value comparisons such as `==`, `!=`, `<`, `<=`, `>`, and `>=`;
- distinguish assignment with `=` from comparison with `==`;
- read and write chained comparisons;
- use `in` and `not in` with strings and collections;
- explain why dictionary membership tests keys by default;
- distinguish value equality from object identity;
- use `is None` and `is not None` appropriately;
- recognize common false values and use `bool()` to inspect truth values;
- combine conditions with `and`, `or`, and `not`;
- explain short-circuit evaluation;
- remember that `and` and `or` can return operands rather than `True` or `False`;
- use parentheses when they make Boolean expressions easier to read;
- prepare clear conditions for the next chapter on `if`, `elif`, and `else`.

## 1. A condition is an expression interpreted for truth

A **condition** is an expression whose result Python can interpret as true or false.

A comparison is one common source of a condition:

```python
score = 82

print(score >= 70)
```

```text
True
```

The expression `score >= 70` asks a question about two values. The result is a Boolean value.

In the next chapter, conditions will control which block of code runs. For now, keep the condition separate from the decision statement itself.

## 2. Comparisons produce truth values

Python provides six familiar value-comparison operators:

| Operator | Meaning |
|---|---|
| `==` | equal |
| `!=` | not equal |
| `<` | less than |
| `<=` | less than or equal |
| `>` | greater than |
| `>=` | greater than or equal |

Example:

```python
score = 82

print(score == 82)
print(score != 90)
print(score < 100)
print(score >= 70)
```

```text
True
True
True
True
```

Comparisons normally produce `True` or `False`.

## 3. `=` assigns; `==` compares

These symbols look similar but do different jobs.

Assignment stores or rebinds a value:

```python
score = 82
```

Comparison asks whether two values are equal:

```python
print(score == 82)
```

```text
True
```

A useful reading habit is:

- `=` → **store or bind**
- `==` → **ask whether values are equal**

This distinction becomes especially important when conditions appear inside control-flow statements.

## 4. Equality and ordering are different questions

Equality asks whether values compare as equal.

Ordering asks whether one value comes before, after, below, or above another according to the rules supported by those types.

For numbers:

```python
print(10 == 10.0)
print(10 < 12.5)
```

```text
True
True
```

Python numeric types can often compare across compatible numeric types.

That does **not** mean every pair of types supports ordering.

For example:

```python
print(10 < "12")
```

raises a `TypeError` because Python does not define that ordering between `int` and `str`.

```text
TypeError
```

The exact traceback contains file and line information. The important point here is that ordering comparisons require types whose comparison rules support that operation.

## 5. Chained comparisons express intervals clearly

Python allows comparisons to be chained:

```python
age = 28

print(18 <= age < 65)
```

```text
True
```

For this example, the idea is equivalent to asking both of these questions:

```python
age = 28

print(age >= 18 and age < 65)
```

```text
True
```

The chained form is often easier to read for intervals.

Python evaluates each expression in a comparison chain at most once. That detail matters more when expressions become complex; the beginner takeaway is that chained comparisons are a real Python feature, not shorthand produced by rewriting the source text.

## 6. Comparison chains do not imply every possible comparison

Consider:

```python
value = 5

print(1 < value < 10)
```

```text
True
```

This means:

- `1 < value`
- and `value < 10`

It does not introduce any extra comparison between `1` and `10`.

Keep the chain focused on the relationship you actually mean.

## 7. Membership tests ask whether a value is present

You already used `in` while studying collections.

```python
topics = ["strings", "numbers", "collections"]

print("collections" in topics)
print("loops" in topics)
```

```text
True
False
```

`in` asks whether membership is present.

`not in` asks the opposite:

```python
topics = ["strings", "numbers", "collections"]

print("loops" not in topics)
```

```text
True
```

Both forms produce Boolean results.

## 8. Membership works with strings too

For strings, membership checks whether one string occurs inside another:

```python
message = "study python"

print("python" in message)
print("java" not in message)
```

```text
True
True
```

Even though strings and lists are different types, both support meaningful membership tests.

## 9. Dictionary membership checks keys by default

A dictionary models key-value relationships.

```python
profile = {"name": "Ava", "level": "beginner"}

print("name" in profile)
print("Ava" in profile)
```

```text
True
False
```

`"name" in profile` checks whether `"name"` is a key.

It does not search dictionary values by default.

If your question is specifically about values, make that intent visible:

```python
profile = {"name": "Ava", "level": "beginner"}

print("Ava" in profile.values())
```

```text
True
```

## 10. Equality and identity are not the same concept

`==` compares values according to a type's equality rules.

`is` asks whether two references point to the **same object**.

These questions can produce different answers:

```python
first = [1, 2]
second = [1, 2]

print(first == second)
print(first is second)
```

```text
True
False
```

The lists contain equal values, but they are separate list objects.

For ordinary value comparison, use `==` and `!=`.

Do not replace value equality with `is` just because a small example appears to work.

## 11. Use identity comparison for `None`

`None` is a singleton value used to represent the absence of a normal value in many Python APIs and programs.

PEP 8 recommends identity comparison for singletons such as `None`:

```python
result = None

print(result is None)
print(result is not None)
```

```text
True
False
```

Use:

```python
result is None
```

rather than:

```python
result == None
```

The second expression can produce a Boolean result, but `is None` communicates the intended identity check and follows the standard style guidance.

## 12. Truth-value testing goes beyond literal `True` and `False`

Python can interpret many objects as true or false in a Boolean context.

Most built-in values considered false include:

- `False`;
- `None`;
- numeric zero such as `0` and `0.0`;
- empty strings;
- empty lists and tuples;
- empty dictionaries;
- empty sets.

Example:

```python
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(None))
```

```text
False
False
False
False
False
False
```

This behavior is called **truth-value testing**.

## 13. Nonempty collections are usually truthy

Compare empty and nonempty values:

```python
print(bool("Python"))
print(bool(["lists"]))
print(bool({"topic": "python"}))
print(bool({"python"}))
```

```text
True
True
True
True
```

For the built-in collections introduced so far, emptiness is therefore a useful Boolean distinction.

Do not confuse truthiness with a claim about the meaning of the contained data. A nonempty list is truthy even if its only item is `False`:

```python
print(bool([False]))
```

```text
True
```

The list itself is nonempty.

## 14. `bool()` makes the truth interpretation explicit

`bool()` converts a value to `True` or `False` according to its truth-value rules.

```python
value = []

print(bool(value))
print(type(bool(value)))
```

```text
False
<class 'bool'>
```

This is useful while learning and debugging.

Later, conditions can usually use the value directly without wrapping every expression in `bool()`.

## 15. `and` requires the left side to be truthy before evaluating the right side

With Boolean operands:

```python
has_ticket = True
venue_open = True

print(has_ticket and venue_open)
```

```text
True
```

If either requirement is false, the combined truth result is false:

```python
has_ticket = True
venue_open = False

print(has_ticket and venue_open)
```

```text
False
```

Read `and` as requiring both conditions to succeed when the operands are Boolean conditions.

## 16. `or` accepts the first truthy alternative

With Boolean operands:

```python
has_permission = False
is_admin = True

print(has_permission or is_admin)
```

```text
True
```

If at least one Boolean condition is true, the expression is true.

This makes `or` useful for alternatives.

## 17. `not` reverses truth interpretation and returns a Boolean

`not` produces a real Boolean result:

```python
is_blocked = False

print(not is_blocked)
print(not "")
print(not "Python")
```

```text
True
True
False
```

`not` asks for the opposite truth value.

It always produces `True` or `False`.

## 18. `and` and `or` do not always return `bool`

This is one of the most important details in this chapter.

`and` and `or` use truth-value testing, but they return one of their operands.

Example with `or`:

```python
display_name = "" or "Guest"

print(display_name)
print(type(display_name))
```

```text
Guest
<class 'str'>
```

The empty string is falsy, so `or` evaluates and returns `"Guest"`.

Example with `and`:

```python
result = "Python" and 3

print(result)
print(type(result))
```

```text
3
<class 'int'>
```

The first operand is truthy, so `and` evaluates and returns the second operand.

When both operands are actual Boolean conditions, the result often looks like an ordinary `True` or `False`. Do not generalize that appearance into a rule that `and` and `or` always return `bool`.

## 19. Boolean operators short-circuit

Python does not always evaluate every operand.

For `and`:

- if the left operand is falsy, that value is returned and the right operand is not evaluated;
- otherwise, the right operand is evaluated and returned.

For `or`:

- if the left operand is truthy, that value is returned and the right operand is not evaluated;
- otherwise, the right operand is evaluated and returned.

This is called **short-circuit evaluation**.

A small example shows why it matters:

```python
denominator = 0

safe_check = denominator != 0 and 10 / denominator > 2

print(safe_check)
```

```text
False
```

`denominator != 0` is `False`, so Python does not evaluate `10 / denominator > 2`. The division-by-zero expression is never reached.

Short-circuit behavior can make conditions safer and clearer, but do not hide important side effects inside Boolean expressions merely to exploit evaluation order.

## 20. Combine comparisons into meaningful Boolean expressions

Boolean operators become especially useful when their operands are comparisons.

```python
score = 82
is_active = True

eligible = score >= 70 and is_active

print(eligible)
```

```text
True
```

Another example:

```python
temperature = 28

needs_attention = temperature < 5 or temperature > 35

print(needs_attention)
```

```text
False
```

Try to name variables according to the question the expression answers.

## 21. Precedence affects how Boolean expressions are grouped

Among the operators in this chapter:

1. comparisons such as `>=`, `==`, `in`, and `is` bind more tightly than Boolean operators;
2. `not` binds more tightly than `and`;
3. `and` binds more tightly than `or`.

Therefore:

```python
print(True or False and False)
```

```text
True
```

Python groups the `and` part before the `or` part.

Even when you know the precedence rules, parentheses can make intent easier to see:

```python
print(True or (False and False))
```

```text
True
```

Prefer readability over showing that you memorized the precedence table.

## 22. Parentheses can document the intended groups

Consider:

```python
score = 82
has_project = False
has_certificate = True

eligible = score >= 70 and (has_project or has_certificate)

print(eligible)
```

```text
True
```

The parentheses make the alternatives visually explicit.

They are not decorative when they help a reader understand the logical groups.

## 23. Do not substitute bitwise operators for Boolean logic

Python also has operators such as `&`, `|`, and `^`.

Those are primarily **bitwise operators** for integer-style bit operations and can have specialized meanings for other types.

For ordinary logical conditions, use:

- `and`;
- `or`;
- `not`.

Do not learn `&` and `|` as alternate spellings for `and` and `or`.

## 24. Practical example: comparison results

The file [`examples/comparison_results.py`](examples/comparison_results.py) contains:

```python
age = 28
minimum_age = 18
maximum_age = 65
topics = ["strings", "numbers", "collections"]
profile = {"name": "Ava", "level": "beginner"}

print("At least 18:", age >= minimum_age)
print("Under 65:", age < maximum_age)
print("Inside interval:", minimum_age <= age < maximum_age)
print("Collections available:", "collections" in topics)
print("Name key exists:", "name" in profile)
print("Email key missing:", "email" not in profile)
```

Expected output:

```text
At least 18: True
Under 65: True
Inside interval: True
Collections available: True
Name key exists: True
Email key missing: True
```

This example combines value comparison, a chained interval, collection membership, and dictionary-key membership without introducing control-flow statements yet.

## 25. Practical example: Boolean logic and short-circuiting

The file [`examples/boolean_logic.py`](examples/boolean_logic.py) contains:

```python
has_ticket = True
venue_open = True
is_blocked = False
denominator = 0

can_enter = has_ticket and venue_open and not is_blocked
needs_attention = not has_ticket or is_blocked
safe_ratio_check = denominator != 0 and 10 / denominator > 2
display_name = "" or "Guest"

print("Can enter:", can_enter)
print("Needs attention:", needs_attention)
print("Safe ratio check:", safe_ratio_check)
print("Display name:", display_name)
```

Expected output:

```text
Can enter: True
Needs attention: False
Safe ratio check: False
Display name: Guest
```

Notice that the same example contains both Boolean conditions and the operand-return behavior of `or`.

## 26. Practical example: inspecting truth values

The file [`examples/truth_values.py`](examples/truth_values.py) contains:

```python
print("Empty string:", bool(""))
print("Text:", bool("Python"))
print("Zero:", bool(0))
print("Nonzero:", bool(-3))
print("None:", bool(None))
print("Empty list:", bool([]))
print("Filled list:", bool(["python"]))
print("Empty dictionary:", bool({}))
print("Filled dictionary:", bool({"topic": "python"}))
print("Empty set:", bool(set()))
print("Filled set:", bool({"python"}))
```

Expected output:

```text
Empty string: False
Text: True
Zero: False
Nonzero: True
None: False
Empty list: False
Filled list: True
Empty dictionary: False
Filled dictionary: True
Empty set: False
Filled set: True
```

The values are intentionally drawn from concepts already introduced in earlier phases.

## 27. Common mistakes

### Mistake 1: confusing assignment and equality

```python
score = 82
print(score == 82)
```

`=` performs assignment. `==` performs equality comparison.

### Mistake 2: using `is` for ordinary value equality

Avoid treating this as a replacement for value comparison:

```python
first = [1, 2]
second = [1, 2]

print(first is second)
```

```text
False
```

Use `==` when the question is whether the values compare as equal.

### Mistake 3: expecting `and` and `or` to always return Boolean values

```python
print("" or "fallback")
print("Python" and 5)
```

```text
fallback
5
```

They return operands according to truth-value testing.

### Mistake 4: assuming text that says `"False"` is falsy

```python
print(bool("False"))
```

```text
True
```

The string is nonempty.

### Mistake 5: forgetting that dictionary membership checks keys

```python
profile = {"name": "Ava"}

print("name" in profile)
print("Ava" in profile)
```

```text
True
False
```

### Mistake 6: making precedence do unnecessary mental work

This is valid:

```python
ready = True or False and False
```

But when real conditions become longer, use parentheses if they make the intended groups easier to recognize.

### Mistake 7: comparing incompatible values with ordering operators

```python
print(10 < "12")
```

This raises `TypeError`.

Convert or model the data appropriately rather than expecting every pair of types to have an ordering relationship.

## 28. Exercise: build a study-readiness condition set

Create a file named `study_readiness.py`.

Start with:

```python
completed_topics = ["strings", "numbers", "collections"]
score = 82
is_active = True
optional_note = ""
```

Without using `if`, `elif`, `else`, `for`, or `while`, create and print expressions that answer these questions:

1. Is `score` at least `70`?
2. Is `score` inside the interval from `70` through `100`, inclusive?
3. Is `"collections"` present in `completed_topics`?
4. Is `"loops"` absent from `completed_topics`?
5. Are both the minimum score requirement and `is_active` true?
6. Is `optional_note` truthy?
7. What value does `optional_note or "No note"` produce?

One possible implementation is:

```python
completed_topics = ["strings", "numbers", "collections"]
score = 82
is_active = True
optional_note = ""

minimum_reached = score >= 70
inside_expected_range = 70 <= score <= 100
has_collections = "collections" in completed_topics
loops_not_started = "loops" not in completed_topics
ready = minimum_reached and is_active
has_note = bool(optional_note)
display_note = optional_note or "No note"

print("Minimum reached:", minimum_reached)
print("Inside expected range:", inside_expected_range)
print("Has collections:", has_collections)
print("Loops not started:", loops_not_started)
print("Ready:", ready)
print("Has note:", has_note)
print("Display note:", display_note)
```

Expected output:

```text
Minimum reached: True
Inside expected range: True
Has collections: True
Loops not started: True
Ready: True
Has note: False
Display note: No note
```

The exercise deliberately stops before `if`. The goal is to make the condition itself trustworthy first.

## 29. Review checklist

Before moving on, make sure you can explain:

- [ ] the difference between `=` and `==`;
- [ ] what each of the six value-comparison operators asks;
- [ ] why `18 <= age < 65` is useful;
- [ ] what `in` and `not in` test;
- [ ] what dictionary membership checks by default;
- [ ] the difference between `==` and `is`;
- [ ] why `is None` is preferred;
- [ ] which common built-in values are falsy;
- [ ] what `bool()` does;
- [ ] how `and`, `or`, and `not` behave;
- [ ] why `and` and `or` can return non-Boolean operands;
- [ ] what short-circuit evaluation means;
- [ ] why parentheses can improve condition readability.

## 30. Quick reference

| Need | Typical form |
|---|---|
| Equal values | `a == b` |
| Different values | `a != b` |
| Ordering | `a < b`, `a <= b`, `a > b`, `a >= b` |
| Interval | `lower <= value <= upper` |
| Membership | `item in collection` |
| Absence | `item not in collection` |
| Identity with `None` | `value is None` |
| Negated `None` identity | `value is not None` |
| Require both conditions | `condition_a and condition_b` |
| Accept either condition | `condition_a or condition_b` |
| Reverse truth value | `not value` |
| Inspect truth value explicitly | `bool(value)` |

Remember:

```text
comparison -> truth value -> Boolean combination -> future decision
```

This chapter built the left side of that bridge. The next chapter adds the decision statement.

## Next step

The next chapter is **`if`, `elif`, and `else`**.

There, these conditions stop being values that you only print and start controlling which code Python executes.

## Official references

- [Python 3.13 built-in types: Truth Value Testing and Boolean Operations](https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing)
- [Python 3.13 language reference: Comparisons](https://docs.python.org/3.13/reference/expressions.html#comparisons)
- [PEP 8: Programming Recommendations](https://peps.python.org/pep-0008/#programming-recommendations)