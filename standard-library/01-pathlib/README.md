# Working with Filesystem Paths Using `pathlib`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

`pathlib` is the standard-library module for representing and manipulating filesystem paths as objects.

Earlier chapters used strings such as `"notes.txt"` and `"reports/data.csv"` when opening files. That works, but paths have structure: they contain directories, names, stems, suffixes, parents, and platform-specific separators. `pathlib` gives that structure a dedicated API.

For most everyday work, start with:

```python
from pathlib import Path
```

Then create `Path` objects and combine them instead of manually concatenating path strings.

## Learning goals

By the end of this chapter, you should be able to:

- explain what a `Path` object represents;
- create relative and absolute paths;
- combine path segments with `/`;
- inspect names, suffixes, parents, and parts;
- use `Path.cwd()` and `Path.home()` deliberately;
- create directories with `mkdir()`;
- read and write text through a path object;
- inspect whether a path currently points to a file or directory;
- iterate through directories with `iterdir()`;
- search with `glob()` and `rglob()`;
- transform path names with `with_name()` and `with_suffix()`;
- understand why existence checks do not guarantee that a later filesystem operation will succeed;
- distinguish `Path` from the pure path classes at a beginner level;
- avoid hard-coded path separators when portability matters.

## 1. What problem does `pathlib` solve?

A path is more than text.

Consider:

```text
reports/2026/summary.txt
```

That path has several meaningful pieces:

- `reports` is a directory segment;
- `2026` is another directory segment;
- `summary.txt` is the final name;
- `summary` is the stem;
- `.txt` is the suffix.

You could manipulate those pieces with string methods, but then your code must also understand path separators and operating-system conventions.

`pathlib` puts path-specific behavior behind path-specific objects.

```python
from pathlib import Path

report_path = Path("reports") / "2026" / "summary.txt"

print(report_path)
print(report_path.name)
print(report_path.stem)
print(report_path.suffix)
print(report_path.parent)
```

The exact separator shown by `print(report_path)` depends on the operating system. That is part of the point: your code expresses path structure instead of manually inserting `/` or `\\`.

## 2. `Path` is usually the class you want

The `pathlib` module contains several path classes.

For normal filesystem work, use `Path`:

```python
from pathlib import Path

config_path = Path("config") / "settings.json"
```

`Path` is a concrete path class. It can both manipulate path structure and perform filesystem operations such as reading a file, creating a directory, or checking what currently exists.

The module also contains pure path classes such as `PurePath`, `PurePosixPath`, and `PureWindowsPath`. Pure paths manipulate path syntax without touching the filesystem.

You normally do **not** need to choose `PosixPath` or `WindowsPath` directly. `Path` chooses the concrete path flavor appropriate for the running platform.

## 3. Creating paths

A path can be created from one string:

```python
from pathlib import Path

file_path = Path("notes.txt")
```

It can also be created from multiple segments:

```python
from pathlib import Path

file_path = Path("reports", "2026", "summary.txt")
```

Or you can combine path objects and segments with `/`:

```python
from pathlib import Path

reports_dir = Path("reports")
file_path = reports_dir / "2026" / "summary.txt"
```

The `/` operator here does not perform division. `Path` defines it as a convenient path-joining operation.

Prefer this:

```python
file_path = Path("reports") / "2026" / "summary.txt"
```

over manual separator construction such as:

```python
file_path = "reports/" + "2026/" + "summary.txt"
```

The `Path` version communicates intent and avoids embedding one platform's separator into the program.

## 4. Relative and absolute paths

A **relative path** is interpreted relative to some context, commonly the process's current working directory.

```python
from pathlib import Path

relative_path = Path("reports") / "summary.txt"

print(relative_path.is_absolute())
```

An **absolute path** identifies a location from the filesystem's root or drive context.

Do not assume that a relative path is relative to the Python source file. It is normally interpreted relative to the current working directory of the running process.

That distinction is one of the most common sources of "the file exists, but Python cannot find it" confusion.

## 5. Current working directory and home directory

`Path.cwd()` returns the current working directory:

```python
from pathlib import Path

current_dir = Path.cwd()
print(current_dir)
```

`Path.home()` returns the current user's home directory:

```python
from pathlib import Path

home_dir = Path.home()
print(home_dir)
```

These methods are useful when the program intentionally depends on those locations.

Do not use them merely to make a path "look absolute". First decide what the path is supposed to be relative to.

## 6. Inspecting path structure

`Path` exposes common path components as attributes.

```python
from pathlib import Path

path = Path("archive") / "report.final.csv"

print(path.name)
print(path.stem)
print(path.suffix)
print(path.suffixes)
print(path.parent)
print(path.parts)
```

Typical meanings:

| Attribute | Meaning |
|---|---|
| `.name` | final path component |
| `.stem` | final name without its last suffix |
| `.suffix` | last file suffix |
| `.suffixes` | list of suffixes |
| `.parent` | logical parent path |
| `.parents` | sequence of logical ancestors |
| `.parts` | tuple of path components |

A suffix is based on path syntax, not on the file's actual contents. A file named `table.csv` is not guaranteed to contain valid CSV just because its suffix is `.csv`.

## 7. Transforming names without string surgery

Use path methods when the operation is about path structure.

```python
from pathlib import Path

source = Path("exports") / "report.csv"

print(source.with_suffix(".json"))
print(source.with_name("summary.csv"))
```

`with_suffix()` returns a new path. It does not rename a file on disk.

Likewise, `with_name()` returns another path object with a different final name.

This distinction matters:

```text
construct or transform a Path object
        !=
perform a filesystem mutation
```

## 8. Reading and writing text

`Path.read_text()` and `Path.write_text()` are convenient wrappers for small text files.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    notes_dir = workspace / "notes"
    notes_dir.mkdir()

    notes_path = notes_dir / "pathlib.txt"
    notes_path.write_text("Paths are objects.\n", encoding="utf-8")

    print(notes_path.read_text(encoding="utf-8").strip())
```

Use an explicit encoding for text data when the file format or application contract expects one.

For portable project data, UTF-8 is usually a good explicit choice:

```python
text = path.read_text(encoding="utf-8")
```

and:

```python
path.write_text(text, encoding="utf-8")
```

### Important: `write_text()` replaces existing contents

`Path.write_text()` opens the target for writing. If the file already exists, its previous contents are replaced.

That makes this dangerous if the existing file must be preserved.

Use it only when replacement is intentional.

For append workflows or more specialized opening modes, use `open()` or `Path.open()` with an appropriate mode.

## 9. `Path.open()` and the built-in `open()`

A `Path` object can be passed directly to the built-in `open()` because it implements Python's path-like protocol.

```python
from pathlib import Path

path = Path("notes.txt")

with open(path, "r", encoding="utf-8") as file:
    text = file.read()
```

You can also call the path's own method:

```python
with path.open("r", encoding="utf-8") as file:
    text = file.read()
```

Both are valid. Choose one style consistently within a codebase.

## 10. Creating directories with `mkdir()`

`Path.mkdir()` creates a directory.

```python
from pathlib import Path

output_dir = Path("output")
output_dir.mkdir()
```

If missing parent directories should also be created:

```python
output_dir = Path("build") / "reports" / "daily"
output_dir.mkdir(parents=True)
```

If an already-existing directory is acceptable:

```python
output_dir.mkdir(parents=True, exist_ok=True)
```

Be precise about `exist_ok=True`: it says an existing directory at that path is acceptable. It does not turn every filesystem problem into success. Permission errors and incompatible existing objects can still fail.

## 11. Checking the filesystem

Common queries include:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    file_path = workspace / "lesson.txt"
    file_path.write_text("pathlib", encoding="utf-8")

    print(file_path.exists())
    print(file_path.is_file())
    print(workspace.is_dir())
```

The central methods are:

| Method | Question |
|---|---|
| `.exists()` | does this path currently exist? |
| `.is_file()` | does it currently refer to a regular file? |
| `.is_dir()` | does it currently refer to a directory? |
| `.is_symlink()` | is it a symbolic link? |

These methods report the result of the filesystem query at the time it runs, but a `False` result is not always proof that an entry is absent. In Python 3.14, boolean status methods such as `exists()`, `is_file()`, and `is_dir()` return `False` when an `OSError` prevents inspection. With the default `follow_symlinks=True`, `exists()` also returns `False` when a symbolic link's target is missing. If you need to distinguish missing, inaccessible, invalid, or another status failure, use `stat()` and handle its exception rather than relying on the boolean query alone.

These checks are therefore useful snapshots of what the query could establish, not authoritative guarantees about the filesystem. The operation you actually need to perform, and any exception it raises, remains the authoritative boundary.

## 12. A check is not a guarantee

This code looks cautious:

```python
if path.exists():
    text = path.read_text(encoding="utf-8")
```

But the filesystem can change between the check and the read. Permissions can change. Another process can remove or replace the file. A network filesystem can become unavailable.

So `exists()` is useful when the **current state itself** matters, but it should not be treated as a promise that the next operation cannot fail.

At an operation boundary, handle the exception that the operation itself can raise:

```python
from pathlib import Path

settings_path = Path("settings.json")

try:
    text = settings_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("Settings file is missing")
else:
    print(text)
```

This connects directly to Phase 7: filesystem APIs and exception handling are designed to work together.

## 13. Iterating over a directory

`iterdir()` yields the direct children of a directory.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)

    for name in ("gamma.txt", "alpha.txt", "beta.txt"):
        (workspace / name).write_text(name, encoding="utf-8")

    for path in sorted(workspace.iterdir()):
        print(path.name)
```

The filesystem does not promise a useful order. If deterministic order matters, sort explicitly.

This is especially important in:

- tests;
- generated reports;
- tutorials;
- reproducible automation.

`iterdir()` is not recursive. It sees only the direct children of that directory.

## 14. Searching with `glob()` and `rglob()`

`glob()` matches paths using a pattern relative to the current path.

```python
from pathlib import Path

for path in Path("src").glob("*.py"):
    print(path)
```

That searches only the matching level.

`rglob()` searches recursively:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source_dir = workspace / "src"
    nested_dir = source_dir / "tools"
    nested_dir.mkdir(parents=True)

    (source_dir / "app.py").write_text("print('app')\n", encoding="utf-8")
    (nested_dir / "helper.py").write_text("VALUE = 1\n", encoding="utf-8")
    (nested_dir / "notes.txt").write_text("notes\n", encoding="utf-8")

    for path in sorted(source_dir.rglob("*.py")):
        print(path.relative_to(workspace))
```

Again, results are not guaranteed to arrive in a particular order. Sort when order is part of the output contract.

Patterns can be powerful, but recursive searches such as `**` or `rglob()` can become expensive on large directory trees. Search as narrowly as the task allows.

## 15. Making a path relative to another path

`relative_to()` expresses one path relative to a known parent context:

```python
from pathlib import Path

workspace = Path("/project")
file_path = Path("/project/docs/guide.md")

print(file_path.relative_to(workspace))
```

Conceptually, the result is:

```text
docs/guide.md
```

`relative_to()` is a path relationship operation. It is not the same as asking the operating system for the current working directory.

It raises `ValueError` when the requested relationship cannot be formed under its rules.

## 16. Resolving paths

`resolve()` returns an absolute path while resolving `..` components and symbolic links according to the filesystem.

```python
from pathlib import Path

path = Path("docs") / ".." / "README.md"
resolved = path.resolve()

print(resolved)
```

Because `resolve()` can involve filesystem semantics, do not confuse it with simple string cleanup.

Use it when you actually need a resolved filesystem path, not automatically on every `Path`.

## 17. Pure paths

Pure path classes are useful when you want path semantics without filesystem access.

For example, code running on Linux can still reason about Windows path syntax:

```python
from pathlib import PureWindowsPath

windows_path = PureWindowsPath("C:/Users/Ana/Documents/report.txt")

print(windows_path.name)
print(windows_path.parent)
```

`PureWindowsPath` does not check whether that Windows path exists.

For ordinary application code that works with the local filesystem, `Path` remains the default starting point.

## 18. Cross-platform thinking

Avoid manually hard-coding separators when the path is meant to be portable.

Fragile:

```python
path = "reports\\2026\\summary.txt"
```

Better:

```python
from pathlib import Path

path = Path("reports") / "2026" / "summary.txt"
```

But "cross-platform" does not mean every path is meaningful on every platform. Drive letters, UNC paths, permissions, case sensitivity, symbolic-link behavior, reserved names, and filesystem rules can differ.

`pathlib` gives you the platform-aware abstraction. It does not erase the operating system.

## 19. `Path` objects work with many Python APIs

Modern Python APIs commonly accept path-like objects.

For example:

```python
from pathlib import Path
import json

path = Path("config.json")

with path.open("r", encoding="utf-8") as file:
    data = json.load(file)
```

This is one reason `pathlib` composes well with the earlier file and module chapters.

You do not normally need to convert every `Path` to `str`.

Convert to a string only when an external API specifically requires a string representation.

## 20. Common exceptions

Filesystem operations can still fail.

Common exceptions include:

| Exception | Typical situation |
|---|---|
| `FileNotFoundError` | a requested file or parent path is missing |
| `FileExistsError` | creation required absence, but an entry already exists |
| `PermissionError` | the operation is not permitted |
| `IsADirectoryError` | a file operation targets a directory |
| `NotADirectoryError` | a directory component is not actually a directory |
| `OSError` | broader operating-system or filesystem failures |

Catch the most specific exception you can actually handle.

Do not wrap every `Path` call in `except Exception:` just because filesystem operations can fail.

## 21. When to use `pathlib`

Use `pathlib` when:

- you are building paths from segments;
- you need names, stems, suffixes, or parent relationships;
- you are reading or writing files;
- you are creating directories;
- you are discovering files;
- you need portable path construction;
- you want path intent to be explicit in function interfaces.

For example:

```python
from pathlib import Path

def load_template(template_path: Path) -> str:
    return template_path.read_text(encoding="utf-8")
```

A type hint of `Path` can make a path-oriented contract clearer when your function intentionally expects a `Path` object.

Depending on the interface, accepting a broader path-like input can also be appropriate. That is an API-design decision, not a rule that every path parameter must use one exact type.

## 22. When not to force `pathlib`

Do not introduce path objects where there is no path problem to solve.

Also remember that some low-level or legacy APIs may still be designed around `os`, `os.path`, file descriptors, or raw strings.

Phase 8 will later cover `os` and `shutil`. Those modules are not "obsolete because `pathlib` exists". They overlap in some areas and serve different levels of the standard library.

## 23. Common mistakes

### Mistake 1: assuming relative means relative to the source file

```python
Path("data.json")
```

is normally interpreted from the process's current working directory.

### Mistake 2: checking `exists()` and assuming the next operation is guaranteed

Filesystem state can change between operations.

### Mistake 3: forgetting that `write_text()` replaces contents

If preserving existing data matters, choose the appropriate file-opening strategy.

### Mistake 4: manually concatenating separators

Prefer structural path composition.

### Mistake 5: assuming suffix equals format validation

`.json` in the name does not prove valid JSON.

### Mistake 6: relying on directory iteration order

Sort when deterministic ordering matters.

### Mistake 7: calling `resolve()` automatically everywhere

Resolve when you need resolution semantics.

### Mistake 8: converting every `Path` to `str`

Many Python APIs accept path-like objects directly.

## 24. Practical example

Imagine a small reporting program that creates a workspace, writes a report, then discovers generated text files.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    reports_dir = workspace / "reports"
    reports_dir.mkdir()

    report_path = reports_dir / "summary.txt"
    report_path.write_text("status=ready\n", encoding="utf-8")

    for path in sorted(reports_dir.glob("*.txt")):
        print(path.name, path.read_text(encoding="utf-8").strip())
```

The important design idea is not merely shorter syntax.

The program uses one path abstraction consistently for:

```text
construct
    ↓
create
    ↓
write
    ↓
discover
    ↓
read
```

That makes filesystem intent visible from end to end.

## 25. Exercise

Create a program using `TemporaryDirectory` and `Path` that:

1. creates a directory named `study`;
2. creates `notes` and `archive` inside it;
3. writes two `.txt` files inside `notes`;
4. lists the direct children of `notes` in sorted order;
5. finds every `.txt` file below `study` recursively;
6. prints each discovered path relative to `study`;
7. reads one file using UTF-8;
8. does not leave permanent files behind.

Then answer:

- Which paths are relative?
- Which operations in this exercise actually access or modify the filesystem, and which are only structural path operations such as path composition or `relative_to()`?
- Why would checking `.exists()` first not guarantee that `.read_text()` succeeds later?
- When would `PureWindowsPath` be useful instead of `Path`?

## 26. Review checklist

Before moving on, make sure you can explain:

- what a `Path` object represents;
- why `/` is useful for path composition;
- relative versus absolute paths;
- current working directory versus source-file location;
- `.name`, `.stem`, `.suffix`, `.parent`, and `.parts`;
- `read_text()` and `write_text()`;
- `mkdir(parents=True, exist_ok=True)`;
- `.exists()`, `.is_file()`, and `.is_dir()`;
- why checks are not guarantees;
- `iterdir()`, `glob()`, and `rglob()`;
- why deterministic output may require `sorted()`;
- `with_name()` and `with_suffix()`;
- the purpose of `resolve()`;
- the difference between `Path` and pure paths;
- why `pathlib` complements rather than replaces all of `os` and `shutil`.

## Quick reference

```python
from pathlib import Path

path = Path("reports") / "summary.txt"

path.name
path.stem
path.suffix
path.parent
path.parts

Path.cwd()
Path.home()

path.exists()
path.is_file()
path.is_dir()

path.read_text(encoding="utf-8")
path.write_text("text\n", encoding="utf-8")

directory.mkdir(parents=True, exist_ok=True)

list(directory.iterdir())
list(directory.glob("*.txt"))
list(directory.rglob("*.txt"))

path.with_name("other.txt")
path.with_suffix(".json")
path.resolve()
```

## Runnable examples

- [`examples/path_parts.py`](examples/path_parts.py)
- [`examples/text_workspace.py`](examples/text_workspace.py)
- [`examples/discover_python_files.py`](examples/discover_python_files.py)
- [`examples/inspect_paths.py`](examples/inspect_paths.py)

These examples are deterministic and use either path-only operations or temporary directories so they do not leave persistent files behind.

## Next chapter

Continue with **[Chapter 02: `datetime` and Time Calculations](../02-datetime/README.md)**, where the standard library adds explicit objects for dates, times, durations, parsing, formatting, and date arithmetic.

## Official references

- [Python 3.14 `pathlib` - object-oriented filesystem paths](https://docs.python.org/3.14/library/pathlib.html)
- [Python 3.14 `os.PathLike` and `os.fspath()`](https://docs.python.org/3.14/library/os.html#os.PathLike)
- [Python 3.14 built-in `open()`](https://docs.python.org/3.14/library/functions.html#open)
