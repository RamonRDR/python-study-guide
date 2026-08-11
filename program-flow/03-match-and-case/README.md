<div align="center">

# `match` and `case`: Structural Pattern Matching

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Program Flow](../README.md) · [← Previous: `if`, `elif`, and `else`](../02-if-elif-and-else/README.md)

An `if` statement asks whether a condition is truthy. A `match` statement asks whether a value **fits a pattern**.

That difference starts small with literal values and becomes more useful when the value has structure, such as a tuple or dictionary.

**Estimated study time:** 110–140 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain what structural pattern matching means;
- recognize that `match` and `case` were added in Python 3.10;
- distinguish pattern matching from ordinary Boolean conditions;
- match literal values with `case`;
- use `_` as a wildcard fallback;
- combine alternatives with an OR pattern using `|`;
- explain why `case 1 | 2 | 3:` and `case 1, 2, 3:` mean different things;
- explain why a bare name such as `case value:` captures instead of comparing with an existing variable;
- extract values from sequence patterns;
- match selected keys in mapping patterns;
- use a guard to add a Boolean condition after a successful pattern match;
- choose between `if` and `match` according to intent;
- avoid depending on class patterns before classes are introduced later in the guide.

## 1. What structural pattern matching is

Structural pattern matching compares one subject value against one or more patterns.

The basic mental model is:

```text
subject value
    ↓
try the first case pattern
    ↓
match succeeds or fails
    ↓
if needed, try the next case
```

A pattern can describe more than one exact value. It can also describe the **shape** of data and capture parts of that data into names.

Python added the `match` statement in version 3.10.

## 2. Basic syntax

A `match` statement contains a subject expression followed by one or more `case` blocks:

```python
match subject:
    case pattern_a:
        statement
    case pattern_b:
        statement
```

Python evaluates the subject and tries the case patterns in order.

When a pattern succeeds, its block runs. Normally, later case blocks are not tried after a case is selected.

There is no automatic fallthrough from one selected case into the next one.

## 3. Start with literal patterns

The simplest pattern matches a literal value:

```python
status = "ready"

match status:
    case "ready":
        print("Ready to begin")
    case "paused":
        print("Waiting")
```

Output:

```text
Ready to begin
```

The subject is `status`.

The patterns are the string literals `"ready"` and `"paused"`.

Because the first pattern succeeds, Python executes that block.

## 4. Add a wildcard fallback with `_`

The underscore `_` is the wildcard pattern.

It succeeds without binding the subject to a name:

```python
status = "offline"

match status:
    case "ready":
        print("Ready to begin")
    case "paused":
        print("Waiting")
    case _:
        print("Unknown status")
```

Output:

```text
Unknown status
```

This role is similar to a final fallback branch, but it is still a pattern, not an `else` clause.

Because `_` matches anything, an unguarded wildcard case belongs last.

## 5. Case order matters

Patterns are tried from top to bottom.

Put more specific cases before a broad fallback:

```python
command = "stop"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
```

Output:

```text
Stopping
```

Once `"stop"` matches, the wildcard case is not selected.

## 6. One `case` can accept several alternatives

Use `|` to create an OR pattern:

```python
command = "resume"

match command:
    case "start" | "resume":
        print("Running")
    case "pause":
        print("Paused")
    case _:
        print("Unknown command")
```

Output:

```text
Running
```

Read this as:

```text
match "start" OR "resume"
```

The vertical bar belongs to pattern syntax here.

## 7. `case 1 | 2 | 3` is not `case 1, 2, 3`

This is an important distinction.

To match one of three integer values, use an OR pattern:

```python
option = 2

match option:
    case 1 | 2 | 3:
        print("Known option")
    case _:
        print("Unknown option")
```

Output:

```text
Known option
```

But this syntax means something different:

```python
case 1, 2, 3:
```

It describes a **sequence pattern** containing three positions.

It can match a subject such as:

```python
coordinates = (1, 2, 3)

match coordinates:
    case 1, 2, 3:
        print("Exact sequence")
    case _:
        print("Different sequence")
```

Output:

```text
Exact sequence
```

So remember:

```text
1 | 2 | 3  = alternatives
1, 2, 3    = sequence structure
```

## 8. `match` is more than a traditional switch

At first, literal cases can look similar to `switch` statements found in some languages.

That comparison is useful only as a starting point.

Python patterns can also:

- describe sequence structure;
- describe mapping structure;
- capture matched components into names;
- combine patterns;
- use guards after a successful structural match.

That structural behavior is the reason the feature is called **structural pattern matching**.

## 9. `match` and `case` are soft keywords

`match` and `case` are soft keywords.

They have special meaning in the grammatical contexts that form a match statement, but they are not reserved everywhere as ordinary keywords are.

For beginner code, the practical recommendation is simple: still prefer descriptive names that do not reuse `match` or `case` unnecessarily.

That avoids visual confusion even when a particular use would be syntactically allowed.

## 10. Capture patterns

A name inside a pattern can capture part of the subject.

Consider a tuple that represents an event:

```python
event = ("move", 4, -2)

match event:
    case ("move", x, y):
        print(x)
        print(y)
```

Output:

```text
4
-2
```

The literal `"move"` must match the first item.

The names `x` and `y` capture the second and third items.

After the selected case succeeds, those names contain the matched values.

## 11. A bare name does not compare with an existing variable

This is one of the most important beginner traps in pattern matching.

Suppose you already have:

```python
expected = "ready"
status = "paused"
```

This does **not** mean "compare status with expected":

```python
match status:
    case expected:
        print(expected)
```

Here `expected` is a capture pattern. It captures the subject value.

That means a plain name pattern is not the normal way to compare against a variable that already exists.

For values known directly in the code, use literal patterns such as:

```python
case "ready":
```

When your real intent is an arbitrary Boolean comparison against runtime values, an `if` statement is often clearer.

## 12. Why an irrefutable capture must be last

A plain capture pattern succeeds for any subject it can receive.

For example:

```python
match status:
    case captured:
        print(captured)
```

This case is irrefutable: without a guard, it always succeeds.

An unguarded irrefutable case cannot be followed by another case block because those later cases could never be selected.

The wildcard `_` is also irrefutable, but unlike a capture name it does not bind the subject.

## 13. Sequence patterns

Sequence patterns let you describe positions inside sequence-like data.

For example:

```python
point = (3, 7)

match point:
    case (x, y):
        print(f"x={x}, y={y}")
```

Output:

```text
x=3, y=7
```

Both positions are captured.

A fixed-length sequence pattern requires the expected number of elements.

## 14. Combine literals and captures in a sequence

Patterns become more descriptive when some positions are fixed and others are captured:

```python
event = ("message", "Hello")

match event:
    case ("move", x, y):
        print(f"Move to {x}, {y}")
    case ("message", text):
        print(text)
    case _:
        print("Unknown event")
```

Output:

```text
Hello
```

This is more than comparing the whole tuple for equality.

The pattern checks structure and extracts the relevant component at the same time.

## 15. Lists and tuples can fit sequence patterns

Sequence pattern syntax describes a sequence structure, not necessarily one exact display syntax of the subject.

For example:

```python
point = [8, 5]

match point:
    case (x, y):
        print(f"Point: {x}, {y}")
```

Output:

```text
Point: 8, 5
```

A list subject can satisfy this two-item sequence pattern.

Do not read parentheses in a pattern as "the subject must be a tuple".

## 16. Strings are not treated as sequence patterns here

Although strings are sequences in many Python operations, sequence patterns intentionally do not treat `str`, `bytes`, or `bytearray` as sequence subjects.

Match text using literal patterns or other appropriate logic instead of expecting character-by-character sequence pattern matching.

For example:

```python
word = "go"

match word:
    case "go":
        print("Go")
    case _:
        print("Other word")
```

Output:

```text
Go
```

## 17. Starred sequence patterns

A starred pattern can capture a variable-length middle or remainder:

```python
values = [10, 20, 30, 40]

match values:
    case [first, *middle, last]:
        print(first)
        print(middle)
        print(last)
```

Output:

```text
10
[20, 30]
40
```

The starred capture receives a list containing the unmatched middle items.

Use this when the variable-length structure is part of the meaning of the data, not merely as a clever way to unpack everything.

## 18. Mapping patterns

Mapping patterns let you match selected keys in mapping-like data.

A dictionary is the most familiar example:

```python
request = {
    "action": "open",
    "resource": "chapter",
}

match request:
    case {"action": "open", "resource": resource}:
        print(resource)
    case _:
        print("Unsupported request")
```

Output:

```text
chapter
```

The `"action"` key must have the literal value `"open"`.

The value associated with `"resource"` is captured into `resource`.

## 19. Mapping patterns do not require the mapping to have only those keys

A mapping pattern can match even when the subject has additional keys not mentioned by the pattern:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "theme": "dark",
}

match request:
    case {"action": "open", "resource": resource}:
        print(resource)
```

Output:

```text
chapter
```

The extra `"theme"` key does not prevent this pattern from succeeding.

This differs from a fixed-length sequence pattern, where the number of positions is significant unless a starred pattern is used.

## 20. Capture remaining mapping items with `**rest`

When the remaining keys matter, a double-star capture can collect them:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "theme": "dark",
}

match request:
    case {"action": "open", **rest}:
        print(rest)
```

Output:

```text
{'resource': 'chapter', 'theme': 'dark'}
```

The capture receives a dictionary containing the unmatched mapping items.

## 21. Guards add a condition after a pattern succeeds

A case can include an `if` guard:

```python
request = {
    "action": "open",
    "level": 3,
}

match request:
    case {"action": "open", "level": level} if level >= 2:
        print("Advanced access")
    case {"action": "open"}:
        print("Basic access")
```

Output:

```text
Advanced access
```

The order is:

```text
pattern succeeds
    ↓
evaluate the guard
    ↓
if the guard is truthy, select the case
otherwise try the next case
```

Guards connect this chapter directly to the Boolean logic and `if` concepts learned earlier.

## 22. A guard is not part of the structural pattern

Keep the two jobs separate in your mental model:

```text
pattern = does the value have the required form?
guard   = does an additional condition hold?
```

For example:

```python
record = ("score", 82)

match record:
    case ("score", value) if value >= 70:
        print("Passing score")
    case ("score", value):
        print("Score below threshold")
```

Output:

```text
Passing score
```

The tuple structure matches first. The numeric threshold is then checked by the guard.

## 23. `match` versus `if`

Neither tool replaces the other.

Use `if` when the main idea is an arbitrary Boolean condition:

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

Use `match` when the main idea is selecting behavior according to a value's pattern or structure:

```python
event = ("click", 10, 20)

match event:
    case ("click", x, y):
        print(f"Click at {x}, {y}")
    case _:
        print("Other event")
```

Ask which idea better describes the problem.

## 24. When a simple `if` can be clearer

Do not use `match` merely because it is newer syntax.

For one straightforward comparison, this is clear:

```python
if temperature > 30:
    print("Hot day")
```

Turning every small condition into pattern matching can add ceremony without adding meaning.

Prefer the construct that makes the decision easiest to understand.

## 25. When `match` becomes especially expressive

`match` becomes useful when several cases share a structured vocabulary.

Examples include fictional data such as:

```text
("move", x, y)
("message", text)
("quit",)
```

or mappings such as:

```text
{"action": "open", "resource": ...}
{"action": "close", "resource": ...}
```

The pattern itself documents the expected shape while selecting the behavior.

## 26. Common mistake: expecting fallthrough

Python selects the first case whose pattern succeeds and whose guard, if present, is truthy.

It does not automatically continue into the next case block afterward.

You do not need a `break` at the end of every case.

That is different from the behavior of some traditional switch constructs in other languages.

## 27. Common mistake: using commas for alternatives

Wrong mental model:

```python
case 1, 2, 3:
```

That is not "1 or 2 or 3".

For alternatives, write:

```python
case 1 | 2 | 3:
```

Use commas when you genuinely mean sequence structure.

## 28. Common mistake: using a bare variable name as a constant

This pattern captures:

```python
case expected:
```

It does not normally mean "compare against the current value stored in `expected`".

For beginner code, prefer:

- literal patterns when the alternatives are literal values;
- an `if` condition when comparing against runtime variables;
- more advanced value-pattern techniques only after their supporting concepts are understood.

## 29. Common mistake: placing `_` too early

This structure is conceptually wrong because the wildcard would make later alternatives unreachable:

```python
match command:
    case _:
        print("Anything")
    case "start":
        print("Start")
```

Put broad fallback patterns last.

## 30. Common mistake: forcing deeply complex patterns

Patterns can become sophisticated, but beginner code does not benefit from turning one case into a puzzle.

If a pattern mixes too many nested structures, captures, OR alternatives, and guards, consider whether smaller decisions would communicate the intent better.

Readable code remains the goal.

## 31. Scope boundary: class patterns come later

Structural pattern matching can also work with class patterns.

This guide does not require them here because classes have not yet been introduced in the beginner sequence.

For now, this chapter stays within concepts already available:

- literals;
- lists and tuples;
- dictionaries;
- names and assignment;
- Boolean conditions;
- Boolean conditions used as guards.

Class patterns can be revisited after object-oriented concepts are part of the learner's toolkit.

## 32. Worked example: literal choices

The file [`examples/literal_and_or_patterns.py`](examples/literal_and_or_patterns.py) contains:

```python
command = "pause"

match command:
    case "start" | "resume":
        message = "Session running"
    case "pause":
        message = "Session paused"
    case "stop":
        message = "Session stopped"
    case _:
        message = "Unknown command"

print(message)
```

Expected output:

```text
Session paused
```

Notice that `"start" | "resume"` groups two literal alternatives into one case.

## 33. Worked example: sequence structure

The file [`examples/sequence_patterns.py`](examples/sequence_patterns.py) contains:

```python
event = ("move", 4, -2)

match event:
    case ("move", x, y):
        print(f"Move to: {x}, {y}")
    case ("message", text):
        print(f"Message: {text}")
    case _:
        print("Unknown event")
```

Expected output:

```text
Move to: 4, -2
```

The first item identifies the event type. The remaining items are captured as data.

## 34. Worked example: mapping pattern plus guard

The file [`examples/mapping_patterns_and_guards.py`](examples/mapping_patterns_and_guards.py) contains:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "level": 2,
    "theme": "dark",
}

match request:
    case {"action": "open", "resource": resource, "level": level} if level >= 2:
        print(f"Open advanced resource: {resource}")
    case {"action": "open", "resource": resource}:
        print(f"Open resource: {resource}")
    case _:
        print("Unsupported request")
```

Expected output:

```text
Open advanced resource: chapter
```

The mapping contains an extra `"theme"` key, but the first pattern can still match because mapping patterns do not require the subject to contain only the listed keys.

## 35. Exercise

Create a variable named `event` containing one of these fictional values:

```python
("login", "Mina")
("logout", "Mina")
("move", 3, 8)
("unknown",)
```

Write one `match` statement that:

1. captures and prints the name for `("login", name)`;
2. captures and prints the name for `("logout", name)`;
3. captures and prints both coordinates for `("move", x, y)`;
4. uses `_` for anything else.

Then add a second small example where an integer variable named `option` accepts `1`, `2`, or `3` in a single case using `|`.

Do not use `for`, `while`, functions, exceptions, or comprehensions yet.

## 36. Exercise extension

Create this dictionary:

```python
request = {
    "action": "download",
    "file": "guide.pdf",
    "size_mb": 8,
}
```

Use a mapping pattern and guard so that:

- a download with `size_mb <= 10` prints `"Small download"`;
- another download request prints `"Large download"`;
- any other action reaches `_`.

Keep the example deterministic and non-interactive.

## 37. Review checklist

Before moving on, confirm that you can explain each statement without running the code:

- [ ] `match` evaluates a subject and compares it with patterns.
- [ ] cases are considered in order.
- [ ] only the first selected case block runs.
- [ ] `_` is a wildcard and does not bind a name.
- [ ] `|` creates pattern alternatives.
- [ ] commas can describe sequence structure rather than alternatives.
- [ ] a bare capture name is not a normal constant comparison.
- [ ] sequence patterns can extract positional components.
- [ ] mapping patterns can extract values by keys.
- [ ] extra mapping keys do not automatically prevent a match.
- [ ] a guard adds a Boolean condition after structural matching succeeds.
- [ ] `if` remains useful for arbitrary Boolean decisions.
- [ ] class patterns are intentionally deferred in this learning path.

## 38. Quick reference

| Need | Typical form |
|---|---|
| Match one literal | `case "start":` |
| Match several alternatives | `case "start" | "resume":` |
| Fallback | `case _:` |
| Match a two-item sequence | `case (x, y):` |
| Match a tagged sequence | `case ("move", x, y):` |
| Capture a variable-length remainder | `case [first, *rest]:` |
| Match selected mapping keys | `case {"action": "open", "resource": resource}:` |
| Capture extra mapping items | `case {"action": "open", **rest}:` |
| Add a condition | `case pattern if condition:` |
| Arbitrary Boolean decision | often `if condition:` |

Remember the progression:

**subject → pattern → optional captures → optional guard → selected block**

## Next step

The next chapter is **`for` Loops and Iteration**.

You now know how Python can select behavior from conditions and from data patterns. Next, the guide moves from **selection** to **repetition**, using `for` to process items from an iterable one at a time.

## Official references

- [Python 3.13 language reference: The `match` statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-match-statement)
- [Python 3.13 tutorial: `match` Statements](https://docs.python.org/3.13/tutorial/controlflow.html#match-statements)
- [PEP 634: Structural Pattern Matching — Specification](https://peps.python.org/pep-0634/)
- [PEP 636: Structural Pattern Matching — Tutorial](https://peps.python.org/pep-0636/)
