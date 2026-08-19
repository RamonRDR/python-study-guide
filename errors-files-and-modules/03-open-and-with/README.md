<div align="center">

# Opening Files Safely with `open()` and `with`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Errors, Files, and Modules](../README.md) · [← Previous: Raising and Custom Exceptions](../02-raise-and-custom-exceptions/README.md)

Programs often need data to survive after the process ends. A text file can store notes, configuration, exports, logs, or intermediate results that a later execution can read again.

Python's built-in `open()` function creates a **file object** connected to a file or another file-like resource. The `with` statement gives that resource a clear lifetime so it is closed even when the block exits because of an exception.

This chapter focuses on **plain text files and safe resource management**. Chapter 04 will build on this foundation with TXT, CSV, and JSON as data formats.

**Estimated study time:** 100–130 minutes.

**Python requirement:** Python 3.10 or newer. The file-handling behavior taught here was verified against the official Python 3.14 documentation.

## Learning goals

By the end of this chapter, you should be able to:

- explain what `open()` returns and why a file object is a resource that should be closed;
- open text files with explicit modes and an explicit encoding;
- explain the practical differences among `r`, `w`, `a`, and `x`;
- read a complete small file, one line, or lines incrementally;
- write and append text while controlling newline characters deliberately;
- use `with` so a file is closed on normal and exceptional exit paths;
- connect `with` to the cleanup role previously seen with `finally`;
- handle common file exceptions at an appropriate boundary;
- explain why relative paths depend on the current working directory;
- avoid accidental truncation, encoding surprises, and unnecessary whole-file reads;
- distinguish text mode from binary mode at a beginner-friendly level;
- choose a safe basic pattern for common file tasks.

## 1. Files introduce persistence

Variables live in memory while a Python process is running. When the process ends, ordinary local variables disappear.

A file gives a program a place to store data outside that process:

```text
program memory
     ↓ write
text file on storage
     ↓ read later
another program execution
```

That persistence is useful, but it also introduces new failure possibilities: a path may not exist, permission may be denied, text may use an unexpected encoding, or a program may open an existing file in a destructive mode.

## 2. `open()` returns a file object

A common text-mode call looks like this:

```python
file = open("notes.txt", "r", encoding="utf-8")
```

`open()` does not return the file's text directly. It returns a **file object** that provides operations such as `read()`, iteration, `write()`, and `close()`.

The object also tracks state such as whether it is open and where the current read or write position is.

## 3. The simplified `open()` model

The complete built-in function has more parameters, but a strong beginner model is:

```python
open(file, mode="r", encoding=None)
```

For text files, think about three questions before opening anything:

1. **Which path?**
2. **What operation is intended: read, replace, append, or create-only?**
3. **Which text encoding does the file use?**

Making those choices explicit is safer than treating `open()` as a magical "get file contents" operation.

## 4. Mode `r`: read an existing file

`"r"` means read text. It is also the default mode when the mode argument is omitted.

```python
file = open("notes.txt", "r", encoding="utf-8")
```

The target must exist. If it does not, `open()` raises `FileNotFoundError`.

Being explicit with `"r"` is often useful in educational and application code because the intended operation is immediately visible.

## 5. Mode `w`: write and replace

`"w"` opens a text file for writing.

```python
file = open("notes.txt", "w", encoding="utf-8")
```

If the file does not exist, it is created. If it already exists, its previous contents are **truncated** before new data is written.

That destructive behavior makes mode selection a correctness decision, not a cosmetic detail.

```text
existing file + "w"
        ↓
old contents removed
        ↓
new writes become the contents
```

## 6. Mode `a`: append to the end

`"a"` opens for appending. New writes are added at the end instead of replacing the existing contents.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Files\n")
```

If the file does not exist, append mode creates it.

Append is useful when the previous contents should remain intact and each new write belongs after them.

## 7. Mode `x`: create only if the file is new

`"x"` requests exclusive creation.

```python
with open("notes.txt", "x", encoding="utf-8") as file:
    file.write("First version\n")
```

If the path already exists, Python raises `FileExistsError` instead of replacing it.

Use this when accidentally overwriting an existing file would be an error.

## 8. Choose the mode by intent

A compact decision table:

| Intent | Typical mode | Existing file |
|---|---|---|
| Read | `r` | kept |
| Replace contents | `w` | truncated |
| Add at the end | `a` | kept |
| Create only when absent | `x` | raises `FileExistsError` |

There are combinations such as `r+`, `w+`, and `a+` for reading and writing with the same file object. They are valid, but they also combine positioning and mode rules that beginners rarely need.

Prefer the simplest mode that matches the actual job.

## 9. Text mode needs an encoding decision

Text files store bytes, while Python strings contain Unicode text. An **encoding** defines how those two representations map to each other.

```text
str in Python
    ↓ encode
bytes in file
    ↓ decode
str in Python
```

If `encoding` is omitted, `open()` uses a default that depends on the runtime environment. That can make the same source code behave differently on different systems.

When the format is known to be UTF-8, state it explicitly:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

## 10. Why `with` is the normal file pattern

A file object uses an operating-system resource. It should be closed when the program finishes using it.

The manual pattern works:

```python
file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

But there is a problem: if an exception occurs between `open()` and `close()`, the final call may never execute.

The usual solution is `with`:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

When execution leaves the `with` block, the file's context-manager protocol performs the required exit work and closes the file.

## 11. `with` connects directly to `finally`

Chapter 01 introduced `finally` for cleanup. A context manager packages that cleanup pattern behind a reusable protocol.

Conceptually:

```text
acquire resource
      ↓
run block
      ↓
release resource
```

Even if the block raises an exception, the context manager is given a chance to perform its exit work before the exception continues outward.

For ordinary file objects, that means the file is closed. `with` does **not** mean "ignore file errors"; it means "manage the resource lifetime reliably.

## 12. The file is closed after the block

The name assigned by `as file` still exists after the block, but the underlying file object is closed:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(file.closed)
```

Output:

```text
True
```

Trying to perform normal I/O on that closed file object raises `ValueError`.

Do not design code that expects to keep using the file outside its `with` block. Move the data you need into ordinary Python objects instead.

## 13. Read a small file with `read()`

`read()` without a size argument reads from the current position to the end of the file.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

This is simple and appropriate for a file that is known to be small.

For a very large or unbounded file, reading everything at once can use unnecessary memory. In that case, process the file incrementally.

## 14. `read(size)` advances the current position

A positive size asks for at most that many characters in text mode:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first = file.read(5)
    second = file.read(5)
```

The second call continues from where the first call stopped. File reads are stateful.

At end-of-file, another text-mode `read()` returns an empty string.

This position model becomes important whenever multiple reads are performed through the same file object.

## 15. Read one line with `readline()`

`readline()` reads one line at a time:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
```

When a line ends with a newline in the file, that `\n` is normally part of the returned string.

At end-of-file, `readline()` returns `""`.

A blank line containing only a newline is `"\n"`, which is different from end-of-file.

## 16. Iterate over the file for line-oriented work

For ordinary line-by-line processing, iterate over the file object:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

This avoids first building a list containing every line and is the preferred simple pattern for incremental line processing.

The file object is an iterable. The loop consumes lines from its current position.

## 17. Be deliberate when removing newline characters

A tempting pattern is:

```python
clean = line.strip()
```

But `strip()` removes leading and trailing whitespace, not only the newline. That may change meaningful data.

If the only intended change is removing a trailing newline character, be more specific:

```python
clean = line.rstrip("\n")
```

Whether other whitespace should be removed is a data-format decision, not a universal file rule.

## 18. `readlines()` builds a list

`readlines()` returns the remaining lines as a list:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

This can be convenient when the complete set of lines is small and you truly need list operations afterward.

Do not use it automatically. If each line can be processed independently, iterating over the file keeps the memory model simpler and more scalable.

## 19. Write text with `write()`

In text mode, `write()` expects a string:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Functions\n")
    file.write("Exceptions\n")
```

`write()` does **not** add a newline automatically. If the file should contain line breaks, include them explicitly.

The method returns the number of characters written in text mode:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    count = file.write("Python\n")

print(count)
```

## 20. Convert non-string values before text writes

Text-mode `write()` does not format arbitrary Python objects for you:

```python
score = 92

with open("score.txt", "w", encoding="utf-8") as file:
    file.write(str(score))
```

An f-string is often clearer when labels or formatting are needed:

```python
with open("score.txt", "w", encoding="utf-8") as file:
    file.write(f"score={score}\n")
```

Chapter 04 will introduce structured formats that provide better conventions for storing more complex data.

## 21. `writelines()` does not invent separators

`writelines()` writes strings from an iterable, but it does not add newline characters between them:

```python
lines = ["Functions\n", "Exceptions\n", "Files\n"]

with open("notes.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

If the strings do not already contain separators, the result will run together.

For beginners, repeated `write()` calls are often easier to inspect until the exact data shape is clear.

## 22. Relative paths depend on the current working directory

A path such as:

```python
open("data/notes.txt", "r", encoding="utf-8")
```

is **relative**. Python resolves it from the process's current working directory, which is not guaranteed to be the same directory that contains the `.py` file.

That explains a common beginner surprise:

```text
same source code
+ different working directory
= different resolved path
```

Later chapters will introduce `pathlib`, which provides a richer path API. For now, always know which directory your process is running from when using relative paths.

## 23. Absolute paths identify a location from a filesystem root

An absolute path does not depend on the current working directory in the same way. Its exact syntax is platform-specific.

Hard-coding an absolute path from one computer into reusable source code is usually a portability problem.

Prefer to receive paths through configuration, arguments, or a path-building strategy appropriate to the program rather than embedding one developer's machine layout in the code.

## 24. Common file exceptions

File operations can raise several useful exception types:

| Exception | Typical meaning |
|---|---|
| `FileNotFoundError` | a required path does not exist |
| `FileExistsError` | exclusive creation targeted an existing path |
| `PermissionError` | the operation is not permitted |
| `IsADirectoryError` | a file operation targeted a directory |
| `UnicodeDecodeError` | bytes could not be decoded with the selected text encoding |
| `OSError` | broader operating-system I/O failures |

These are signals, not instructions to catch everything. Handle an exception only where the program has a meaningful response.

## 25. Place `try` around the boundary you can handle

If a missing optional file has a clear fallback, catch that specific failure:

```python
try:
    with open("preferences.txt", "r", encoding="utf-8") as file:
        preferences = file.read()
except FileNotFoundError:
    preferences = ""
```

The `with` still handles closing whenever opening succeeds.

A broad `except OSError:` may be appropriate when several operating-system failures truly have the same policy, but it should not be used merely to make all file problems disappear.

## 26. If the body fails, cleanup happens before propagation

Consider:

```python
with open("scores.txt", "r", encoding="utf-8") as file:
    score = int(file.readline())
```

If the line contains invalid integer text, `int()` raises `ValueError`.

The file context manager performs its exit work as the block is left, and the exception continues outward unless some surrounding code handles it.

That is the key composition:

```text
open succeeds
    ↓
body raises
    ↓
file is closed
    ↓
exception propagates
```

## 27. Separate file access from data interpretation when useful

A useful design is to let one function read text and another interpret it:

```python
def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def parse_score(text: str) -> int:
    score = int(text)
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score
```

Now file failures and content-validation failures are conceptually distinct.

That separation becomes especially useful in Chapter 04 when parsing structured data.

## 28. Validate before destructive writes when practical

Because `"w"` truncates an existing file when it is opened, validate data that can be validated **before** opening the destination in write mode.

Prefer this order:

```text
build or validate output data
        ↓
open destination with "w"
        ↓
write validated text
```

over opening the destination first and only then discovering that the data is invalid.

This does not make writing atomic or protect against every possible failure, but it reduces one avoidable class of accidental data loss.

## 29. Text mode and binary mode are different interfaces

Text mode is the default and works with `str`.

Binary mode adds `"b"` to the mode and works with `bytes`:

```python
with open("image.bin", "rb") as file:
    data = file.read()
```

In binary mode, text encoding is not used because Python is not converting between `str` and file bytes.

This chapter concentrates on text mode. Use binary mode when the data format is fundamentally bytes, such as many images, archives, or protocol payloads.

## 30. Do not pass `encoding` in binary mode

This combination is conceptually wrong:

```python
open("data.bin", "rb", encoding="utf-8")
```

Binary mode exposes bytes directly, so an encoding parameter is not part of that interface.

Choose one model:

```text
text mode  → str + encoding
binary mode → bytes
```

## 31. Multiple context managers can share one `with`

Python can manage more than one context in a single statement:

```python
with (
    open("input.txt", "r", encoding="utf-8") as source,
    open("output.txt", "w", encoding="utf-8") as destination,
):
    destination.write(source.read())
```

Both resources receive their corresponding exit handling.

For a beginner, nested or multi-item `with` statements are most useful when the operation genuinely needs both resources at the same time. Do not open files earlier or keep them open longer than necessary.

## 32. Practical example: write, then read

The first runnable example creates a temporary directory only so the repository test can exercise real file I/O without leaving generated files behind.

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "topics.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Functions\n")
        file.write("Exceptions\n")
        file.write("Files\n")

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))
```

Output:

```text
Functions
Exceptions
Files
```

The `tempfile` and `os.path` helpers are housekeeping for the executable example. The chapter's learning target is the two `with open(...)` blocks.

Runnable version: [`examples/write_and_read_text.py`](examples/write_and_read_text.py).

## 33. Practical example: append without replacing

The second example makes the difference between `"w"` and `"a"` visible:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "history.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Chapter 01\n")

    with open(path, "a", encoding="utf-8") as file:
        file.write("Chapter 02\n")
        file.write("Chapter 03\n")

    with open(path, "r", encoding="utf-8") as file:
        print(file.read(), end="")
```

Output:

```text
Chapter 01
Chapter 02
Chapter 03
```

Runnable version: [`examples/append_text.py`](examples/append_text.py).

## 34. Practical example: handle a missing optional file

The third example connects file access to the exception model from Chapters 01 and 02:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "optional.txt")

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = "default settings"

    print(content)
```

Output:

```text
default settings
```

The fallback is meaningful because this file is explicitly optional. A required file would normally need a different policy.

Runnable version: [`examples/handle_missing_file.py`](examples/handle_missing_file.py).

## 35. Common mistake: opening with `w` when you meant `a`

This replaces previous contents:

```python
with open("history.txt", "w", encoding="utf-8") as file:
    file.write("new entry\n")
```

If the intent was to preserve the old history and add one entry, use `"a"`.

Before every write-capable `open()`, ask whether existing contents should be replaced, preserved, or protected from overwrite.

## 36. Common mistake: forgetting the encoding

This relies on the environment's default text encoding:

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

If the file format is defined as UTF-8, say so:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Explicit encoding makes intent visible and avoids a major source of cross-platform surprises.

## 37. Common mistake: manual close with an exception gap

This has a cleanup gap:

```python
file = open("scores.txt", "r", encoding="utf-8")
score = int(file.readline())
file.close()
```

If `int()` raises, `close()` is skipped.

Prefer:

```python
with open("scores.txt", "r", encoding="utf-8") as file:
    score = int(file.readline())
```

Now resource cleanup is tied to the block's lifetime.

## 38. Common mistake: catching every file problem as if it were the same

Avoid collapsing unrelated failures without a reason:

```python
try:
    with open("settings.txt", "r", encoding="utf-8") as file:
        settings = file.read()
except Exception:
    settings = ""
```

This can hide programming errors and unexpected failures.

Choose a specific exception when the recovery policy is specific. If several `OSError` subclasses genuinely have the same policy, document that broader decision.

## 39. Common mistake: using `read()` automatically for every file

Whole-file reading is convenient, not universally optimal.

If the task is "process each line independently", this is often better:

```python
with open("events.txt", "r", encoding="utf-8") as file:
    for line in file:
        process(line)
```

than first loading all lines into one giant string.

Choose the reading strategy from the size and processing model of the data.

## 40. Paths from users are an input boundary

If a program accepts a path from a user, API request, configuration file, or command-line argument, that path is input.

A write-capable operation can modify or create data at the resolved location.

Applications with security or data-protection requirements should validate or constrain allowed locations according to their own policy. The exact policy depends on the program and is beyond this beginner chapter.

The general lesson is simple: **a path is not harmless metadata when the program will read from or write to it.**

## 41. When not to use raw text files as the whole data model

Plain text is excellent for simple content, but manually inventing separators and parsing rules becomes fragile as data gains structure.

For example:

```text
name|score|date|notes
```

raises questions about escaping `|`, missing fields, types, and embedded newlines.

Chapter 04 introduces TXT, CSV, and JSON so format choice can match the shape of the data instead of forcing every problem into ad-hoc text parsing.

## 42. Exercise

Create a small program called `study_notes.py` with these requirements:

1. Start with three topic names in a list.
2. Open `study_notes.txt` with `"w"` and `encoding="utf-8"`.
3. Write one topic per line.
4. Reopen the file with `"a"` and add one more topic.
5. Reopen it with `"r"` and iterate over the lines.
6. Print each topic without an extra blank line.
7. Use `with` for every file operation.
8. Explain in a comment why `"w"` is appropriate for the first open and `"a"` for the second.

Stretch questions:

- What would happen if the first mode were `"x"` and the file already existed?
- Which exception would you expect if you tried to read a missing file?
- Why might `read()` be a poor choice if the file could contain millions of lines?

## 43. Review checklist

Before moving on, make sure you can answer these without guessing:

- What does `open()` return?
- Why is `with open(...)` safer than a manual `open()` / `close()` pair?
- What does `"w"` do to an existing file?
- How is `"a"` different?
- When does `"x"` raise `FileExistsError`?
- Why should UTF-8 often be written as `encoding="utf-8"` explicitly?
- What does `read()` return at end-of-file in text mode?
- Why can iterating over a file be preferable to `readlines()`?
- Does `write()` add `\n` automatically?
- What happens to the file when an exception leaves the `with` body?
- From which directory is a relative path resolved?
- What is the basic difference between text mode and binary mode?

## 44. Quick reference

| Need | Pattern |
|---|---|
| Read UTF-8 text | `with open(path, "r", encoding="utf-8") as file:` |
| Replace UTF-8 text | `with open(path, "w", encoding="utf-8") as file:` |
| Append UTF-8 text | `with open(path, "a", encoding="utf-8") as file:` |
| Create only if absent | `with open(path, "x", encoding="utf-8") as file:` |
| Read all remaining text | `file.read()` |
| Read one line | `file.readline()` |
| Process lines incrementally | `for line in file:` |
| Write text | `file.write(text)` |
| Remove only trailing `\n` | `line.rstrip("\n")` |
| Missing required path | `FileNotFoundError` |
| Existing path with `x` | `FileExistsError` |
| General OS I/O category | `OSError` |
| Binary read | `with open(path, "rb") as file:` |

Default beginner pattern:

```python
with open(path, "r", encoding="utf-8") as file:
    content = file.read()
```

Choose the mode according to intent, specify a known text encoding, keep the file lifetime narrow, and catch only failures for which the surrounding code has a real policy.

## What comes next

Chapter 03 establishes safe text-file access and resource lifetime. The next chapter, **TXT, CSV, and JSON**, will focus on how data is represented inside files and which parser or writer should own each format boundary.

```text
exceptions
    ↓
deliberate raising
    ↓
safe file lifetime with open() + with
    ↓
TXT / CSV / JSON formats
    ↓
modules and packages
```

## Official references

- Python 3.14 built-in `open()` documentation: <https://docs.python.org/3.14/library/functions.html#open>
- Python 3.14 tutorial, Reading and Writing Files: <https://docs.python.org/3.14/tutorial/inputoutput.html#reading-and-writing-files>
- Python 3.14 language reference, `with` statement: <https://docs.python.org/3.14/reference/compound_stmts.html#the-with-statement>
- Python 3.14 `io` documentation, Text Encoding: <https://docs.python.org/3.14/library/io.html#text-encoding>
