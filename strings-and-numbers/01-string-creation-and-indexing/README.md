<div align="center">

# String Creation and Indexing

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to the section index](../README.md)

Phase 1 taught you that ordinary text values use the `str` type. This first chapter of Phase 2 goes deeper: it shows how to create strings and how to read individual positions and ranges from them.

A Python string is an immutable sequence of Unicode code points. For a beginner, a useful mental model is simpler: a string is an ordered text value whose positions can be read, but not replaced in place.

## Chapter information

| Item | Details |
|---|---|
| Level | Beginner |
| Prerequisites | Complete Phase 1: Fundamentals |
| Estimated study time | 70 to 90 minutes |
| Main concepts | `str`, string literals, `len()`, indexing, negative indexes, slicing, immutability, `IndexError` |

## Learning objectives

By the end of this chapter, you should be able to:

- create strings with single, double, and triple quotes;
- explain what source-code quotes do and do not become part of the value;
- use common escape sequences when needed;
- measure a string with `len()`;
- read positions with positive and negative indexes;
- explain why the first index is `0`;
- read ranges with slices;
- explain why a slice excludes its stop boundary;
- distinguish an invalid direct index from a broad valid slice;
- explain string immutability;
- recognize that indexing a string returns another `str`.

## 1. Strings are ordered text values

You have already used strings throughout the guide:

```python
course_name = "Python Study Guide"
current_topic = "Strings"
```

Order matters. `"Python"` and `"nohtyP"` contain the same letters, but they are different strings because their items appear in a different sequence.

That ordered structure makes indexing possible.

```text
Text:   P y t h o n
Index:  0 1 2 3 4 5
```

Each position has an integer index. The first position is `0`.

## 2. Creating string literals

A string literal is source-code notation that creates a string value.

Single quotes and double quotes both create ordinary strings:

```python
single_quoted = 'Python'
double_quoted = "Python"

print(single_quoted == double_quoted)
```

```text
True
```

For ordinary strings, quote choice does not change the resulting text. Choose the form that keeps the source readable.

```python
message = "Python's syntax can be readable."
quotation = 'She said "practice".'
```

The quote marks that delimit the literal are syntax. They are not normally part of the resulting value.

## 3. Escapes inside a literal

A backslash can introduce an escape sequence when the text needs a character that would otherwise be awkward to write.

```python
message = "She said \"practice\"."
two_lines = "first line\nsecond line"

print(message)
print(two_lines)
```

```text
She said "practice".
first line
second line
```

Useful early escape sequences include:

- `\n` for a newline;
- `\t` for a tab;
- `\\` for a literal backslash;
- `\"` for a double quote;
- `\'` for a single quote.

Do not memorize every escape at once. Use them when a real value needs them.

## 4. Triple-quoted strings

Matching triple single quotes or triple double quotes can span multiple physical lines.

```python
message = """Study
understand
practice"""

print(message)
```

```text
Study
understand
practice
```

The line breaks are part of the string value.

Triple-quoted strings also appear in docstrings, but a triple-quoted string is not automatically a docstring. Its role depends on where it appears in the program.

## 5. The empty string

A string may contain no code points at all.

```python
empty_text = ""

print(len(empty_text))
```

```text
0
```

The empty string is still a valid `str`. It is not the same thing as `None`.

## 6. Measuring a string with `len()`

`len()` returns the number of items in a sequence. For strings, it returns the number of Unicode code points.

```python
language = "Python"
topic = "Python strings"

print(len(language))
print(len(topic))
```

```text
6
14
```

Spaces count because they are part of the string.

For everyday beginner examples, `len(text)` is a good way to reason about how many indexed positions the string exposes.

### Unicode precision note

Python strings are Unicode text. `len()` counts Unicode code points, not bytes. Some visible symbols can be represented by multiple code points, so the number of visual symbols and `len()` are not guaranteed to match in every writing system or emoji sequence.

You do not need Unicode segmentation algorithms for this chapter. The key idea is that Python text is not modeled as raw bytes.

## 7. Positive indexing starts at zero

Square brackets read one position from a string.

```python
language = "Python"

print(language[0])
print(language[1])
print(language[5])
```

```text
P
y
n
```

For a non-empty string of length `n`, valid positive indexes run from `0` through `n - 1`.

```text
len("Python") == 6
valid indexes: 0 1 2 3 4 5
```

Index `6` is already outside the string.

## 8. Why the first index is zero

It helps to think of an index as an offset from the beginning.

```text
P y t h o n
^
0 positions away from the beginning
```

The item at index `0` is zero positions away from the start. The item at index `1` is one position away.

Python uses this zero-based convention for many sequence types, not only strings.

## 9. Negative indexes count from the end

Negative indexes let you read positions relative to the end.

```python
language = "Python"

print(language[-1])
print(language[-2])
print(language[-6])
```

```text
n
o
P
```

```text
Text:       P  y  t  h  o  n
Positive:   0  1  2  3  4  5
Negative:  -6 -5 -4 -3 -2 -1
```

`-1` is the last item, `-2` is the item before it, and so on.

## 10. Indexing returns another string

Python does not have a separate built-in character type.

```python
language = "Python"
first_item = language[0]

print(first_item)
print(type(first_item))
print(len(first_item))
```

```text
P
<class 'str'>
1
```

An indexed text item is simply a `str` of length `1`.

## 11. Invalid direct indexes raise `IndexError`

A direct index asks for one exact position. If that position does not exist, Python raises `IndexError`.

```python
language = "Python"

print(language[6])
```

```text
IndexError: string index out of range
```

The full traceback also contains file and line information. The important part here is the exception type and message.

An empty string has no valid direct index at all.

## 12. Slicing reads a range

Indexing reads one item. Slicing reads a range and returns a string result without mutating the original string.

Basic syntax:

```text
text[start:stop]
```

The `start` boundary is included. The `stop` boundary is excluded.

```python
language = "Python"

print(language[0:3])
```

```text
Pyt
```

Indexes `0`, `1`, and `2` are included. Index `3` marks where the slice stops.

## 13. Why the stop boundary is excluded

Exclusive stop boundaries make adjacent ranges fit together cleanly.

```python
language = "Python"

prefix = language[0:3]
suffix = language[3:6]

print(prefix)
print(suffix)
print(prefix + suffix)
```

```text
Pyt
hon
Python
```

The boundary `3` ends the first slice and begins the second one.

With the default unit step, when `0 <= start <= stop <= len(text)`, the slice length is `stop - start`.

## 14. Omitting slice boundaries

Omit `start` to begin at the start of the string:

```python
language = "Python"

print(language[:3])
print(language[3:])
print(language[:])
```

```text
Pyt
hon
Python
```

Omitting `stop` continues to the end. Omitting both returns the full text value as a slice.

Because strings are immutable, a full slice is usually unnecessary merely to protect the original value.

## 15. Negative indexes in slices

Slice boundaries may also be negative.

```python
filename = "notes.txt"

print(filename[:-4])
print(filename[-3:])
```

```text
notes
txt
```

This can be useful when a boundary is naturally described from the end.

Keep readability in mind. A shorter expression is not automatically a clearer expression.

## 16. Slices tolerate broad boundaries

A direct index outside the string raises `IndexError`, but a slice may extend beyond the available range.

```python
language = "Python"

print(language[:100])
print(language[100:])
```

```text
Python

```

The first slice returns all available text. The second returns the empty string.

```text
language[100]   -> one exact missing position -> IndexError
language[:100] -> available range             -> valid string
```

## 17. A first look at slice steps

Slices can have a third component:

```text
text[start:stop:step]
```

The step controls how positions are visited.

```python
language = "Python"

print(language[::2])
```

```text
Pto
```

This visits indexes `0`, `2`, and `4`.

You do not need advanced slice puzzles at this stage. Start-and-stop slices are more important for readable beginner code.

## 18. Strings are immutable

An immutable string cannot have one of its positions replaced in place after creation.

```python
language = "Python"
language[0] = "J"
```

```text
TypeError: 'str' object does not support item assignment
```

To produce different text, create another string value.

```python
language = "Python"
updated_language = "J" + language[1:]

print(language)
print(updated_language)
```

```text
Python
Jython
```

The next chapter introduces string methods that often express text transformations more clearly.

## 19. Reassignment is not mutation

A variable name can be rebound to another string.

```python
topic = "indexing"
topic = "slicing"

print(topic)
```

```text
slicing
```

The name now refers to a different string value. The original string was not edited in place.

This connects directly to the Phase 1 distinction between names and values.

## 20. Practical example: fixed-position text

When a format genuinely has fixed positions, indexing and slicing can separate its parts.

```python
record_code = "PY-2048"

category = record_code[:2]
separator = record_code[2]
number_text = record_code[3:]

print("Category:", category)
print("Separator:", separator)
print("Number text:", number_text)
```

```text
Category: PY
Separator: -
Number text: 2048
```

This is appropriate only when the position rules are stable and understood. Fixed indexes become fragile when input formats can vary.

## 21. Practical example: inspect a short text

```python
label = "practice"

print("Length:", len(label))
print("First:", label[0])
print("Last:", label[-1])
print("First four:", label[:4])
print("Remaining:", label[4:])
```

```text
Length: 8
First: p
Last: e
First four: prac
Remaining: tice
```

This combines the chapter's main tools without introducing string methods yet.

## 22. Common mistakes

### Treating index `1` as the first position

```python
language = "Python"
print(language[1])
```

This prints `y`, not `P`. The first index is `0`.

### Using `len(text)` as a valid index

```python
language = "Python"
print(language[len(language)])
```

`len(language)` is `6`, but the last valid positive index is `5`. For the last item, `language[-1]` is clearer.

### Expecting the slice stop to be included

`language[0:3]` produces `"Pyt"`, not `"Pyth"`.

### Confusing reassignment with mutation

Rebinding a name is valid. Assigning to `text[0]` attempts to mutate a string and raises `TypeError`.

### Indexing text that may be empty

A direct index requires the requested position to exist. Later chapters on conditionals will show how to guard such assumptions dynamically.

### Using fixed positions for variable formats

Only use fixed indexes when the data format actually guarantees those positions.

## 23. Connections to earlier concepts

This chapter builds directly on Phase 1:

- variables give names to string values;
- `type()` can confirm that indexed results are `str` values;
- `len()` returns an integer;
- indexes are integers;
- slices return string results without mutating the original;
- `print()` remains useful while inspecting results.

It also prepares later topics:

- string methods transform and search text;
- lists and tuples also support indexing and slicing;
- loops can visit sequence items repeatedly;
- conditionals can protect assumptions about empty text;
- files and external data often arrive as strings that need interpretation.

## 24. Exercise: build a text inspector

Create `text_inspector.py` with this starting value:

```python
text = "Python practice"
```

Print:

1. the complete text;
2. its length;
3. its first item;
4. its last item;
5. the first six items;
6. the second word using a slice;
7. every second item using a slice step;
8. the type of the first indexed item.

A possible output shape is:

```text
Text: Python practice
Length: 15
First: P
Last: e
First six: Python
Second word: practice
Every second: Pto rcie
Indexed type: <class 'str'>
```

Try to write the expressions yourself before comparing them with the repository examples.

### Stretch goal

Create a fixed fictional code such as `"AB-2048"` and separate the two-letter prefix, the hyphen, and the numeric text with indexes and slices.

Do not convert the numeric text yet. The goal is text positions.

## 25. Self-check

Make sure you can answer:

1. What type represents ordinary text in Python?
2. What is the first valid index of a non-empty string?
3. What does `-1` mean?
4. Why is `text[len(text)]` outside the valid range?
5. What is the difference between indexing and slicing?
6. Is the stop boundary included in a slice?
7. What happens when a direct index is outside the string?
8. Why can a broad slice succeed where a broad direct index fails?
9. What does string immutability prevent?
10. Does indexing produce a separate character type?

## 26. Quick reference

| Goal | Syntax | Example |
|---|---|---|
| Create text | quotes | `name = "Python"` |
| Empty string | empty quotes | `text = ""` |
| Measure text | `len(text)` | `len("Python")` → `6` |
| First item | `text[0]` | `"Python"[0]` → `"P"` |
| Last item | `text[-1]` | `"Python"[-1]` → `"n"` |
| Read a range | `text[start:stop]` | `"Python"[0:3]` → `"Pyt"` |
| From the start | `text[:stop]` | `"Python"[:3]` → `"Pyt"` |
| To the end | `text[start:]` | `"Python"[3:]` → `"hon"` |
| Use a step | `text[start:stop:step]` | `"Python"[::2]` → `"Pto"` |
| Invalid direct index | exact missing position | raises `IndexError` |
| Replace an item | not supported | raises `TypeError` |

## 27. Repository examples

Run the deterministic examples:

```bash
python strings-and-numbers/01-string-creation-and-indexing/examples/string_basics.py
python strings-and-numbers/01-string-creation-and-indexing/examples/fixed_position_text.py
```

Then run the repository checks:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 28. What comes next

You can now create strings, measure them, read exact positions, read ranges, and explain why a string cannot be edited item by item.

The next chapter moves from positions to behavior: **common string methods** for tasks such as changing case, trimming whitespace, searching, replacing, splitting, and joining text.

## Official references

- [Python Language Reference — String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)
- [Python Built-in Types — Text Sequence Type `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python Built-in Types — Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Built-in Functions — `len()`](https://docs.python.org/3/library/functions.html#len)

[← Back to the section index](../README.md)
