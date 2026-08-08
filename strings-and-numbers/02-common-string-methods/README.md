# Common String Methods

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Back to the section index](../README.md) · [← Previous chapter: String creation and indexing](../01-string-creation-and-indexing/README.md)

The previous chapter taught you how to create strings and read their positions and ranges. This chapter adds a new idea: strings also provide **methods**, reusable operations that can inspect text or produce a string result without mutating the original value.

You will learn a focused set of methods that appear constantly in real programs. The goal is not to memorize the entire `str` API. It is to understand the method-call pattern, recognize common text tasks, and choose an operation whose behavior matches your intention.

## Chapter information

| Item | Value |
|---|---|
| Phase | 2 — Strings and numbers |
| Chapter | 02 |
| Level | Beginner |
| Prerequisite | Chapter 01 — String creation and indexing |
| Main type | `str` |
| Main idea | Call common string methods deliberately while respecting immutability |

## Learning objectives

By the end of this chapter, you should be able to:

- explain what a string method is;
- call methods with dot notation;
- distinguish the original string from a method result;
- normalize case with `lower()` and `upper()`;
- remove surrounding whitespace with `strip()`;
- remove exact prefixes and suffixes with `removeprefix()` and `removesuffix()`;
- replace text with `replace()`;
- test beginnings and endings with `startswith()` and `endswith()`;
- locate and count substrings with `find()` and `count()`;
- split text into parts with `split()`;
- join strings with `join()`;
- combine a few methods without hiding the program's intention.

## 1. What is a method?

A **method** is a function-like operation associated with an object.

A string value knows how to perform string-specific operations. You ask it to perform one with **dot notation**:

```python
language = "Python"

print(language.upper())
```

```text
PYTHON
```

The dot connects the value on the left to a method provided by its type.

```text
value.method(arguments)
```

Some methods take no arguments. Others need information between the parentheses.

## 2. Methods belong to values, not variable names

The variable name is not what owns the method. The string value does.

These calls are both valid:

```python
language = "Python"

print(language.lower())
print("Practice".lower())
```

```text
python
practice
```

A name is simply one way to refer to a value. This connects directly to the Phase 1 distinction between names and values.

## 3. String methods do not edit the original string in place

Strings are immutable. A method such as `lower()` produces a result, but it does not rewrite the existing string value.

```python
language = "Python"

lowercase_language = language.lower()

print(language)
print(lowercase_language)
```

```text
Python
python
```

If you need to keep the result, assign it to a name.

```python
language = "Python"
language = language.lower()

print(language)
```

```text
python
```

That is reassignment. The original string was not mutated.

## 4. `lower()` and `upper()` change letter case in the result

Use `lower()` when you need a lowercase result:

```python
message = "Python Practice"

print(message.lower())
```

```text
python practice
```

Use `upper()` when you need an uppercase result:

```python
message = "Python Practice"

print(message.upper())
```

```text
PYTHON PRACTICE
```

Case conversion is useful for display and for some normalization tasks.

Do not assume that case conversion validates meaning. `"YES".lower()` becomes `"yes"`, but your program still needs rules for deciding what `"yes"` means.

## 5. Normalize before comparing when case should not matter

Suppose two pieces of text should be treated the same regardless of capitalization.

```python
expected = "python"
received = "PyThOn"

print(received.lower() == expected)
```

```text
True
```

This is a common beginner pattern.

For more advanced internationalized caseless matching, Python also provides `casefold()`. That distinction is intentionally postponed here so this chapter can stay focused on the most common beginner operations.

## 6. `strip()` removes surrounding whitespace by default

User input and external text often contain spaces or line breaks around the meaningful content.

```python
raw_name = "   Python   "

clean_name = raw_name.strip()

print("[" + raw_name + "]")
print("[" + clean_name + "]")
```

```text
[   Python   ]
[Python]
```

With no argument, `strip()` removes leading and trailing whitespace.

It does **not** remove whitespace from the middle:

```python
text = "  Python Study Guide  "

print(text.strip())
```

```text
Python Study Guide
```

## 7. `strip(chars)` treats `chars` as a set of removable characters

This detail matters.

```python
text = "...Python..."

print(text.strip("."))
```

```text
Python
```

When an argument is provided, `strip()` removes combinations of those characters from both ends. It is not an "exact prefix" or "exact suffix" remover.

That means this style can be misleading:

```python
filename = "report.txt"

print(filename.strip(".txt"))
```

The argument is treated as removable characters, not as the exact suffix `".txt"`.

When your intention is to remove one exact prefix or suffix, use the methods designed for that job.

## 8. `removeprefix()` and `removesuffix()` remove exact text

**Compatibility note:** `str.removeprefix()` and `str.removesuffix()` were added in Python 3.9. The examples in this section therefore require Python 3.9 or newer. In Python 3.8 or earlier, these methods are unavailable and calling them raises `AttributeError`.

Use `removeprefix()` for a known prefix:

```python
resource = "draft-report"

print(resource.removeprefix("draft-"))
```

```text
report
```

Use `removesuffix()` for a known suffix:

```python
filename = "report.txt"

print(filename.removesuffix(".txt"))
```

```text
report
```

If the exact prefix or suffix is absent, the textual value is preserved.

These methods express intention more accurately than trying to imitate prefix or suffix removal with `strip()`.

## 9. `replace()` substitutes occurrences

`replace(old, new)` produces a result in which occurrences of `old` are replaced by `new`.

```python
sentence = "Python is clear. Python is practical."

print(sentence.replace("Python", "Code"))
```

```text
Code is clear. Code is practical.
```

You can limit the number of replacements with a third argument:

```python
sentence = "one one one"

print(sentence.replace("one", "two", 1))
```

```text
two one one
```

`replace()` performs textual substitution. It does not understand words, grammar, file formats, or business meaning unless your program adds those rules.

## 10. Use `in` when you only need to know whether text exists

The membership operator is often the clearest way to ask whether a substring is present.

```python
message = "Learn Python step by step"

print("Python" in message)
print("Java" in message)
```

```text
True
False
```

This is not a method, but it belongs beside string-search methods because it is usually the best tool for a simple presence check.

## 11. `startswith()` and `endswith()` express boundary checks

Use `startswith()` when the beginning matters:

```python
filename = "report-2026.csv"

print(filename.startswith("report-"))
```

```text
True
```

Use `endswith()` when the ending matters:

```python
filename = "report-2026.csv"

print(filename.endswith(".csv"))
```

```text
True
```

These methods return Boolean values, which connects string work to `bool` from Phase 1.

## 12. `find()` returns the first matching position or `-1`

Use `find()` when you need the position of a substring.

```python
message = "Learn Python"

print(message.find("Python"))
print(message.find("Java"))
```

```text
6
-1
```

A found substring returns its lowest matching index. A missing substring returns `-1`.

If you only need to know whether the substring exists, prefer `in` because its result communicates the question directly.

## 13. `find()` and `index()` are similar but fail differently

Strings also provide `index()`.

```python
message = "Learn Python"

print(message.index("Python"))
```

```text
6
```

The important difference appears when the substring is missing:

- `find()` returns `-1`;
- `index()` raises `ValueError`.

For beginner code, choose based on the behavior your program actually needs. Do not use `index()` merely because its name sounds more familiar.

## 14. `count()` counts non-overlapping occurrences

Use `count()` when you need the number of occurrences.

```python
text = "banana"

print(text.count("a"))
print(text.count("na"))
```

```text
3
2
```

The count is based on non-overlapping matches.

A count of zero means the substring was not found.

## 15. `split()` separates text into a list of strings

With no explicit separator, `split()` separates on runs of whitespace.

```python
text = "Python   makes   text readable"

words = text.split()

print(words)
```

```text
['Python', 'makes', 'text', 'readable']
```

The result is a **list** of strings.

Lists receive their own full section later in the guide. For now, you only need to recognize that `split()` can turn one string into an ordered collection of string parts.

## 16. `split(separator)` uses an explicit delimiter

When you provide a separator, Python splits on that exact separator string.

```python
record = "python|beginner|active"

parts = record.split("|")

print(parts)
```

```text
['python', 'beginner', 'active']
```

This is different from the whitespace behavior of `split()` with no argument.

Explicit separators can also produce empty string items:

```python
record = "a||b"

print(record.split("|"))
```

```text
['a', '', 'b']
```

That empty item is information: there was nothing between two separators.

## 17. Empty text behaves differently with default and explicit splitting

Compare these two calls:

```python
text = ""

print(text.split())
print(text.split(","))
```

```text
[]
['']
```

With no separator, an empty or whitespace-only string produces an empty list.

With an explicit separator, an empty string produces a list containing one empty string because there was one field and no separator occurrence.

This small distinction becomes important when processing delimited data.

## 18. `join()` combines strings with a separator

`join()` often looks backward at first.

```python
words = ["Python", "Study", "Guide"]

print(" ".join(words))
print("-".join(words))
```

```text
Python Study Guide
Python-Study-Guide
```

The string **before the dot** is the separator.

A useful way to read this is:

```text
separator.join(strings)
```

The separator asks to be placed between the string items.

## 19. `join()` requires string items

This works:

```python
parts = ["chapter", "02", "methods"]

print("/".join(parts))
```

```text
chapter/02/methods
```

But `join()` does not automatically convert arbitrary values to text. If the collection contains non-string items, Python raises `TypeError`.

That design prevents silent conversions from hiding mistakes. Convert values deliberately when text is truly the desired representation.

## 20. Splitting and joining are complementary ideas

You can split text into parts and later join those string parts with another separator.

```python
path_text = "docs/guides/python"

parts = path_text.split("/")
rebuilt = " > ".join(parts)

print(parts)
print(rebuilt)
```

```text
['docs', 'guides', 'python']
docs > guides > python
```

The list is a temporary representation of the pieces. `join()` creates the final text result.

## 21. Methods can be chained

Because many string methods return string results, another string method can sometimes be called immediately on that result.

```python
raw_title = "  Python Guide  "

normalized_title = raw_title.strip().lower().replace(" ", "-")

print(normalized_title)
```

```text
python-guide
```

The calls are evaluated from left to right:

```text
raw_title
    -> strip()
    -> lower()
    -> replace(" ", "-")
```

Chaining is convenient when each step remains obvious.

## 22. Do not turn method chains into puzzles

A shorter expression is not automatically clearer.

This is readable:

```python
raw_title = "  Python Guide  "
clean_title = raw_title.strip()
lowercase_title = clean_title.lower()
normalized_title = lowercase_title.replace(" ", "-")

print(normalized_title)
```

```text
python-guide
```

Named intermediate values are useful when:

- a transformation needs explanation;
- you want to inspect a step;
- the chain is becoming long;
- different steps represent different intentions.

Clarity is more valuable than squeezing every transformation onto one line.

## 23. Practical example: normalize a label

```python
raw_title = "  Python Study Guide  "

clean_title = raw_title.strip()
normalized_title = clean_title.lower().replace(" ", "-")

print("Raw:", "[" + raw_title + "]")
print("Clean:", clean_title)
print("Normalized:", normalized_title)
print("Starts with python:", clean_title.lower().startswith("python"))
print("Word count:", len(clean_title.split()))
```

```text
Raw: [  Python Study Guide  ]
Clean: Python Study Guide
Normalized: python-study-guide
Starts with python: True
Word count: 3
```

This combines cleanup, case normalization, replacement, a boundary check, and splitting without changing the original input in place.

## 24. Practical example: split and rebuild path-like text

```python
path_text = "docs/guides/python"

parts = path_text.split("/")

print("Parts:", parts)
print("Joined:", " > ".join(parts))
print("First separator:", path_text.find("/"))
print("Slash count:", path_text.count("/"))
print("Ends with python:", path_text.endswith("python"))
```

```text
Parts: ['docs', 'guides', 'python']
Joined: docs > guides > python
First separator: 4
Slash count: 2
Ends with python: True
```

This is intentionally plain text, not filesystem logic. A later standard-library chapter will introduce `pathlib` for real filesystem paths.

## 25. Common mistakes

### Forgetting parentheses

A method call needs parentheses:

```python
language = "Python"

print(language.lower())
```

Without `()`, you are referring to the method itself rather than calling it.

### Expecting a method to mutate the string

```python
language = "Python"
language.lower()

print(language)
```

```text
Python
```

Store or reassign the result when you need it.

### Using `strip()` as an exact prefix or suffix remover

`strip(chars)` removes characters from both ends according to a character set. Use `removeprefix()` or `removesuffix()` for exact boundary text.

### Using `find()` as a Boolean directly

A found substring may be at index `0`, and `0` is falsey. A missing substring produces `-1`, and `-1` is truthy.

So this is a poor presence test:

```python
text = "Python"

print(bool(text.find("Python")))
print(bool(text.find("Java")))
```

```text
False
True
```

Use `"Python" in text` when the question is simply whether the substring exists.

### Forgetting that explicit `split()` separators preserve empty fields

`"a||b".split("|")` contains an empty string between the two separators. Do not discard that fact unless your data rules say it is safe.

### Calling `join()` on the collection instead of the separator

The pattern is:

```text
separator.join(strings)
```

not `strings.join(separator)`.

## 26. Connections to earlier concepts

This chapter combines several ideas already studied:

- string values are instances of `str`;
- strings are immutable;
- method results can be assigned to variables;
- `bool` results appear in `startswith()` and `endswith()`;
- indexes appear in `find()`;
- `len()` can measure the list returned by `split()`;
- type conversion remains explicit when non-string values must become text.

It also previews later topics:

- lists will explain the object returned by `split()` in depth;
- conditionals will act on Boolean search results;
- loops will process many string parts;
- files and CSV data will require careful splitting or structured parsers;
- `pathlib` will replace manual string tricks for real filesystem paths.

## 27. Exercise: clean and inspect a text value

Create `text_methods_practice.py` with:

```python
raw_text = "  Python,practice,python  "
```

Produce and print:

1. the original text surrounded by brackets;
2. the text after `strip()`;
3. a lowercase version;
4. the number of lowercase `"python"` occurrences after normalization;
5. a version where commas are replaced by `" | "`;
6. whether the cleaned text starts with `"Python"`;
7. whether it ends with `"python"`;
8. the list produced by splitting on commas;
9. the same parts joined with `" -> "`.

A possible output shape is:

```text
Original: [  Python,practice,python  ]
Clean: Python,practice,python
Lowercase: python,practice,python
Python count: 2
Replaced: Python | practice | python
Starts with Python: True
Ends with python: True
Parts: ['Python', 'practice', 'python']
Joined: Python -> practice -> python
```

Try to solve each transformation independently before compressing any steps into a method chain.

## 28. Self-check

Make sure you can answer:

1. What does the dot mean in `text.lower()`?
2. Why does `text.lower()` not modify `text` in place?
3. What does `strip()` remove when called without arguments?
4. Why is `strip(".txt")` not the same idea as `removesuffix(".txt")`?
5. When is `in` clearer than `find()`?
6. What does `find()` return when no match exists?
7. What does `count()` measure?
8. What type does `split()` return?
9. Why can `split("|")` produce empty string items?
10. Which object provides the separator in `" - ".join(parts)`?
11. Why can a long method chain reduce readability?
12. What should you do when `join()` receives values that are not strings?

## 29. Quick reference

| Goal | Operation | Example result |
|---|---|---|
| Lowercase | `text.lower()` | `"Py".lower()` → `"py"` |
| Uppercase | `text.upper()` | `"Py".upper()` → `"PY"` |
| Trim surrounding whitespace | `text.strip()` | `"  Py  ".strip()` → `"Py"` |
| Remove exact prefix | `text.removeprefix(prefix)` | `"pre-item".removeprefix("pre-")` → `"item"` |
| Remove exact suffix | `text.removesuffix(suffix)` | `"file.txt".removesuffix(".txt")` → `"file"` |
| Replace text | `text.replace(old, new)` | `"a-b".replace("-", "/")` → `"a/b"` |
| Check presence | `sub in text` | `"Py" in "Python"` → `True` |
| Check beginning | `text.startswith(prefix)` | `"Python".startswith("Py")` → `True` |
| Check ending | `text.endswith(suffix)` | `"a.py".endswith(".py")` → `True` |
| Find first position | `text.find(sub)` | `"Python".find("th")` → `2` |
| Count occurrences | `text.count(sub)` | `"banana".count("a")` → `3` |
| Split on whitespace | `text.split()` | `"a  b".split()` → `['a', 'b']` |
| Split on delimiter | `text.split(sep)` | `"a|b".split("|")` → `['a', 'b']` |
| Join strings | `sep.join(strings)` | `"-".join(["a", "b"])` → `"a-b"` |

## 30. Repository examples

Run the deterministic examples:

```bash
python strings-and-numbers/02-common-string-methods/examples/normalize_text.py
python strings-and-numbers/02-common-string-methods/examples/split_and_join.py
```

Then run the repository checks:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 31. What comes next

You can now transform, inspect, split, and join text while keeping string immutability in mind.

The next chapter changes focus from text to numeric and logical values: **`int`, `float`, and `bool` in greater depth**.

## Official references

- [Python Built-in Types — Text Sequence Type `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python Built-in Types — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Built-in Types — Text and Binary Sequence Type Methods Summary](https://docs.python.org/3/library/stdtypes.html#text-and-binary-sequence-type-methods-summary)
- [What’s New In Python 3.9 — New String Methods to Remove Prefixes and Suffixes](https://docs.python.org/3/whatsnew/3.9.html#new-string-methods-to-remove-prefixes-and-suffixes)

[← Back to the section index](../README.md)
