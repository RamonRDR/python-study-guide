<div align="center">

# Organizing Code with Imports, Modules, and Packages

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Errors, Files, and Modules](../README.md) · [← Previous: Working with TXT, CSV, and JSON](../04-txt-csv-and-json/README.md)

As programs grow, keeping every function, constant, parser, and workflow in one file becomes harder to understand and maintain. Python's import system lets you divide code into **modules** and organize related modules into **packages**.

The goal of this chapter is not to memorize every detail of Python's import machinery. It is to build a reliable mental model for small and medium programs: where imported names come from, what code runs during an import, how packages organize modules, why execution context matters, and which habits keep dependencies understandable.

**Estimated study time:** 120–160 minutes.

**Python requirement:** Python 3.10 or newer. The import behavior taught here was checked against the official Python 3.14 tutorial, language reference, and command-line documentation.

## Learning objectives

By the end of this chapter, you should be able to:

- explain what a Python module is in ordinary source-code projects;
- distinguish a module object from the names imported into another module;
- use `import module`, `from module import name`, and `as` deliberately;
- explain why module-qualified access often improves clarity;
- describe what happens to top-level code when a module is imported;
- explain the beginner-level role of `sys.modules` in import caching;
- use `if __name__ == "__main__":` to separate importable definitions from direct execution;
- describe the purpose of `sys.path` without treating it as a list to patch casually;
- distinguish `ModuleNotFoundError` from the broader `ImportError` family;
- explain what a regular package is and what `__init__.py` does;
- use dotted package names and basic absolute imports;
- recognize relative imports and explain why execution context matters for them;
- use `python -m` when a module should run in its package/import context;
- distinguish an import package from an installable distribution package;
- avoid wildcard imports, accidental module-name collisions, import-time side effects, and simple circular-import designs;
- organize a small multi-file Python program with explicit dependencies.

## 1. Why split code across files?

A single file is useful while a program is small. As responsibilities accumulate, one file can become a crowded room where unrelated ideas compete for attention.

Modules create boundaries:

```text
input handling
      ↓
validation
      ↓
calculation
      ↓
formatting
```

Each responsibility can live in a file whose name communicates its purpose.

Splitting code is not automatically better. A three-line helper does not need its own module merely because Python supports modules. Create a boundary when it improves reuse, navigation, testing, ownership of a responsibility, or dependency clarity.

## 2. In ordinary Python source code, a `.py` file can be a module

The Python tutorial introduces a module as a file containing Python definitions and statements.

For example:

```text
study_tools.py
```

can contain:

```python
def build_label(topic: str, level: int) -> str:
    return f"{topic} | level {level}"
```

and another file can import that module.

This file-based model is the right starting point for learners. Python's full import system can also load modules implemented in other ways, including built-in and extension modules, so "module" is broader than "a `.py` file" in the complete language model.

## 3. `import module` binds the module name

Suppose `grade_tools.py` contains:

```python
def classify_score(score: int) -> str:
    if score >= 80:
        return "ready"
    return "review"
```

Another file can import it:

```python
import grade_tools

status = grade_tools.classify_score(84)
print(status)
```

The name `grade_tools` now refers to the imported module object in the importing module's namespace.

## 4. Module-qualified access makes the source of a name visible

With:

```python
import grade_tools
```

you call:

```python
grade_tools.classify_score(84)
```

That extra prefix is useful information. A reader can see immediately that `classify_score` comes from another module.

This is one reason `import module` is often a clear default when the module name is short and meaningful.

## 5. `from module import name` binds selected names directly

Python also allows:

```python
from grade_tools import classify_score

status = classify_score(84)
```

Here `classify_score` is bound directly in the importing module's namespace. The name `grade_tools` is not automatically bound by this statement.

The source module still has to be found and loaded. `from ... import ...` changes what names are bound in the importer; it does not bypass the import system.

## 6. `as` creates a deliberate local alias

A module can be imported under another local name:

```python
import statistics as stats

mean_score = stats.mean([80, 90, 100])
```

A selected name can also be aliased:

```python
from math import sqrt as square_root

print(square_root(81))
```

Use aliases when they are conventional or genuinely improve readability. Avoid cryptic aliases that make the code harder to search and understand.

## 7. Choose an import style by readability, not by shortest typing

Compare:

```python
import decimal

value = decimal.Decimal("0.1")
```

with:

```python
from decimal import Decimal

value = Decimal("0.1")
```

Both can be appropriate.

Questions that help:

- Is the module name useful context?
- Will several names come from the same module?
- Could a directly imported name collide with another local name?
- Is the shorter form already a strong convention in that ecosystem?

The shortest line is not always the clearest dependency.

## 8. Imports are executable statements

An import is not a text-copy operation. Python locates and loads a module, creates or obtains a module object, and executes the module's top-level code when initialization is required.

Consider a module containing:

```python
print("Loading helpers")


def build_message() -> str:
    return "Ready"
```

Importing that module can print `Loading helpers` during module initialization.

This is why top-level executable work should be intentional.

## 9. Module definitions are created by executing module code

A function definition is itself a statement. When a module is initialized, Python executes statements that bind names such as functions, classes, and constants in that module's namespace.

A useful simplified flow is:

```text
find module
    ↓
create/obtain module object
    ↓
execute initialization code if needed
    ↓
module namespace contains its definitions
```

This mental model explains why syntax errors, missing dependencies, and top-level exceptions can make an import fail.

## 10. Normal imports reuse modules through `sys.modules`

During a normal interpreter session, imported modules are cached in `sys.modules`.

That means repeated statements such as:

```python
import math
import math
```

do not normally re-execute the module's initialization from scratch each time.

This is a useful beginner model, not a rule that module code can never run again. Advanced operations such as explicit reloading or manually changing import state can alter that behavior.

## 11. Avoid using import-time side effects as hidden application flow

This is fragile:

```python
# settings.py
print("Connecting to something...")
```

because any code that imports `settings` now triggers that work.

Prefer definitions at module level and explicit execution through functions:

```python
def initialize_settings() -> None:
    print("Settings initialized")
```

The caller can then decide when that action belongs in the program flow.

Some modules legitimately perform small initialization during import. The design warning is about surprising, expensive, irreversible, or order-dependent work.

## 12. Every module has a `__name__`

A module can inspect its own global `__name__` value.

When a module is imported normally, `__name__` reflects its import name.

For example, inside `grade_tools.py` imported as `grade_tools`, the value is typically:

```text
grade_tools
```

When code is executed as the top-level program, Python gives that execution environment the name:

```text
__main__
```

## 13. The main guard separates definitions from direct execution

A common pattern is:

```python
def main() -> None:
    print("Program started")


if __name__ == "__main__":
    main()
```

If the file is executed as the main program, `main()` runs.

If the file is imported, the function is defined but the guarded call does not run.

## 14. Put reusable work in functions before the main guard

Prefer:

```python
def build_report() -> str:
    return "Study report"


def main() -> None:
    print(build_report())


if __name__ == "__main__":
    main()
```

over placing the whole application directly inside the guard.

Functions remain reusable and testable, while the guard answers only one question: should direct-entry behavior start now?

## 15. `__name__ == "__main__"` is not an import blocker

The guard does not prevent the file from being imported.

It prevents only the guarded block from running when the module is imported under another name.

Definitions above the guard still execute as module statements and become available in the module namespace.

## 16. Python needs search locations to find modules

When you write:

```python
import study_tools
```

Python must determine what `study_tools` refers to.

The complete import system supports several kinds of finders and loaders. At beginner level, the important idea is that Python searches import locations according to its import machinery and execution environment.

Those search locations are reflected in `sys.path` for ordinary path-based imports.

## 17. `sys.path` is a list of module search locations

You can inspect it:

```python
import sys

for location in sys.path:
    print(location)
```

Its exact contents depend on how Python was started, the environment, installation configuration, and other settings.

Do not memorize one universal `sys.path` order from a screenshot. Learn the concept: it tells path-based import machinery where modules and packages may be found.

## 18. Do not treat `sys.path.append(...)` as the normal fix for project structure

This may appear to solve an import quickly:

```python
import sys

sys.path.append("../somewhere")
```

but it makes imports depend on runtime path surgery and often hides an unclear project layout or execution command.

Prefer a coherent package structure, a suitable working/install environment, and an execution method that gives Python the intended import context.

There are advanced cases for customizing import paths, but casual `sys.path` mutation should not be the first design tool.

## 19. Module names can collide with other modules

Imagine creating a beginner file named:

```text
json.py
```

and then writing:

```python
import json
```

Depending on the search context, your local file may shadow the standard-library module you intended to import.

Avoid naming your files after standard-library modules or important dependencies used by the same project.

## 20. `ModuleNotFoundError` usually means the requested module could not be found

For example:

```python
import module_that_does_not_exist
```

normally raises `ModuleNotFoundError`.

`ModuleNotFoundError` is a subclass of `ImportError`.

The message and exact failing name matter because an import can find your first module and still fail while importing one of its dependencies.

## 21. `ImportError` is the broader import-related exception

A module may exist while a requested name does not:

```python
from math import name_that_does_not_exist
```

This raises an `ImportError` because `math` is available but the requested imported name is not.

Do not catch `ImportError` around a large block merely to make failures disappear. Catch import-related exceptions only when the program has a deliberate policy, such as a truly optional dependency with a documented fallback.

## 22. A package organizes modules under a dotted namespace

Packages let related modules use hierarchical names such as:

```text
study_tools.formatting
study_tools.validation
study_tools.reports
```

A package can contain modules and subpackages.

In Python's full import model, a package is a special kind of module that can contain submodules. The directory analogy is useful for ordinary source projects, but the language model is based on module/package objects rather than folders alone.

## 23. A regular package commonly uses `__init__.py`

A simple regular package might look like:

```text
study_tools/
├── __init__.py
├── formatting.py
└── validation.py
```

The presence of `__init__.py` makes this directory a regular package in the conventional file-system layout.

`__init__.py` may be empty. It may also define initialization behavior or intentionally expose selected names at the package level.

## 24. Namespace packages are an advanced exception to the `__init__.py` rule

Modern Python also supports **namespace packages**, which can exist without an `__init__.py` and can span multiple locations.

Therefore this statement is too broad:

```text
"Every Python package must have __init__.py."
```

For beginner projects, regular packages with `__init__.py` are usually the clearest starting point. Namespace packages can wait until a project genuinely needs their model.

## 25. `__init__.py` is code, so keep its behavior deliberate

This is valid:

```python
from .formatting import build_label

__all__ = ["build_label"]
```

Now the package can intentionally provide a convenient public name:

```python
from study_tools import build_label
```

But a large `__init__.py` full of expensive setup and surprising imports can make package behavior harder to understand.

Treat package initialization as part of your dependency design.

## 26. Dotted names express package hierarchy

This import:

```python
import study_tools.formatting
```

loads the submodule using its full dotted name.

You then access:

```python
study_tools.formatting.build_label("Modules", 2)
```

Another style is:

```python
from study_tools import formatting

print(formatting.build_label("Modules", 2))
```

Both make the package relationship explicit.

## 27. Import the narrowest stable interface that keeps intent clear

Suppose a package intentionally exposes `build_label` from `__init__.py`:

```python
from study_tools import build_label
```

That can be a clean package API.

If the package does not promise that public shortcut, importing the defining module may be more honest:

```python
from study_tools.formatting import build_label
```

The best choice depends on the interface the package documents, not on how many characters the import saves.

## 28. An import package is not the same thing as a distribution package

The word **package** is overloaded in Python conversations.

An **import package** is part of Python's module namespace, such as:

```text
study_tools
```

A **distribution package** is something installed and managed by packaging tools and may provide one or more import packages or modules.

The install name and import name can even differ.

This chapter teaches import packages. Packaging and publishing distributions are separate topics.

## 29. Absolute imports name the package path explicitly

Inside a project package, an absolute import can look like:

```python
from study_tools.formatting import build_label
```

It names the package from the top-level import namespace.

Absolute imports are often easy to search and understand because the dependency path is explicit.

## 30. Relative imports use leading dots inside packages

A module inside `study_tools` can import a sibling with:

```python
from .formatting import build_label
```

A leading dot refers to the current package. Additional dots can refer to parent package levels.

Relative imports are useful for internal package relationships, but they depend on Python knowing the module's package context.

## 31. Relative imports are not based on the current working directory

This is an important distinction.

A relative import such as:

```python
from .formatting import build_label
```

is resolved from the current module's package information, not by walking from whatever directory the terminal happens to be in.

That is why "I am standing in the right folder" is not a complete explanation for whether a relative import will work.

## 32. Directly executing a package module can remove the package context it expects

Suppose a module contains a relative import and is intended to live inside a package.

Running it by file path:

```text
python study_tools/cli.py
```

may execute it as the top-level `__main__` module rather than as `study_tools.cli`. A relative import can then fail because the expected parent package is not known.

When the module is designed to run in package context, `python -m` is often the correct tool.

## 33. `python -m` locates a module through the import system and executes it

For example:

```text
python -m study_tools.cli
```

Python locates `study_tools.cli` using the standard import mechanism and executes its contents as the `__main__` module.

This preserves the fact that the code belongs to the `study_tools` package while still making it the program entry point.

The command uses a **module name**, not a `.py` filename.

## 34. A package can define `__main__.py` for `python -m package_name`

If a package contains:

```text
study_tools/
├── __init__.py
├── __main__.py
└── formatting.py
```

then:

```text
python -m study_tools
```

executes `study_tools.__main__` as the main module.

This is useful when the package itself has a command-line entry behavior. A package does not gain that behavior merely because `__init__.py` exists.

## 35. Imports make dependencies visible

If `reports.py` imports `formatting.py`, then `reports` depends on `formatting`.

A useful dependency sketch is:

```text
cli
 ↓
reports
 ↓
formatting
```

Keeping dependency direction understandable helps prevent tangled modules where everything imports everything else.

## 36. Circular imports are often a design signal

A simple circular relationship looks like:

```text
module_a imports module_b
        ↑         ↓
        └─────────┘
```

Python may encounter one module while it is only partially initialized, producing missing-name errors or confusing behavior.

Common design fixes include:

- move shared definitions into a third module;
- pass values or callables as parameters instead of importing back upward;
- clarify which module owns a responsibility;
- reduce top-level work that depends on the other module being fully initialized.

Moving an import inside a function can sometimes break a cycle, but it may only hide the architectural problem. Understand the dependency before applying that workaround.

## 37. Imports inside functions are allowed, but top-level imports are the usual readable default

This is valid Python:

```python
def calculate_root(value: float) -> float:
    import math

    return math.sqrt(value)
```

Most ordinary dependencies are easier to see when imports appear near the top of the module.

Local imports can be deliberate for optional dependencies, delayed loading, or carefully understood cycles. Use them for a reason, not as a reflex.

## 38. Avoid wildcard imports in ordinary modules

This syntax exists:

```python
from math import *
```

but it makes the local namespace less explicit. A reader has to know which names the source exports, and new exported names can create collisions.

Prefer explicit imports:

```python
from math import pi, sqrt
```

`__all__` can influence what a wildcard import exposes, but it does not turn wildcard imports into the clearest default for application code.

## 39. Group imports for readability

A common readable organization is:

```python
import csv
import json

from study_tools import build_label
```

PEP 8 convention groups standard-library, third-party, and local application imports separately when those groups exist.

The deeper goal is visibility: a reader should be able to understand a module's main dependencies without hunting through unrelated code.

## 40. Practical example: import the standard library

```python
import math


number = 81
root = math.sqrt(number)

print(f"Square root: {root}")
```

Output:

```text
Square root: 9.0
```

Executable version: [`examples/import_standard_library.py`](examples/import_standard_library.py).

## 41. Practical example: import your own module

Helper module `grade_tools.py`:

```python
def classify_score(score: int) -> str:
    if score >= 80:
        return "ready"
    return "review"
```

Executable module `module_demo.py`:

```python
import grade_tools


score = 84
status = grade_tools.classify_score(score)

print(f"Score {score}: {status}")
```

Output:

```text
Score 84: ready
```

Executable version: [`examples/module_demo.py`](examples/module_demo.py). Supporting module: [`examples/grade_tools.py`](examples/grade_tools.py).

## 42. Practical example: import from a regular package

Package layout:

```text
examples/
├── package_demo.py
└── study_tools/
    ├── __init__.py
    └── formatting.py
```

`formatting.py` defines the reusable function:

```python
def build_label(topic: str, level: int) -> str:
    return f"{topic} | level {level}"
```

`__init__.py` intentionally exposes it at the package level:

```python
from .formatting import build_label

__all__ = ["build_label"]
```

The executable file imports the package API:

```python
from study_tools import build_label


print(build_label("Modules", 2))
```

Output:

```text
Modules | level 2
```

Executable version: [`examples/package_demo.py`](examples/package_demo.py). Supporting package: [`examples/study_tools/`](examples/study_tools/).

## 43. Practical example: main guard

```python
def main() -> None:
    print("Main guard executed")


if __name__ == "__main__":
    main()
```

Output when executed directly:

```text
Main guard executed
```

Executable version: [`examples/main_guard.py`](examples/main_guard.py).

## 44. Common mistake: naming a file after a dependency

Files such as these can create confusing shadows:

```text
json.py
csv.py
math.py
random.py
```

if the same project also expects the standard-library modules with those names.

Choose module names that represent your own responsibility and do not collide with dependencies you import.

## 45. Common mistake: hiding application startup inside an import

Avoid making this the program architecture:

```text
import app
    ↓
app immediately reads files, connects services, and starts loops
```

Prefer an explicit entry point:

```text
import definitions
    ↓
main() deliberately starts application behavior
```

Explicit startup is easier to test, reuse, and reason about.

## 46. Common mistake: assuming file execution and module execution are identical

These commands can create different import contexts:

```text
python path/to/tool.py
python -m package.tool
```

Both execute Python code, but `-m` locates a named module through the import system and executes it as `__main__`.

The difference matters especially for packages and relative imports.

## 47. Common mistake: using packages only to create deep folder trees

This is not automatically good design:

```text
app/core/services/helpers/utils/common/
```

A package hierarchy should communicate meaningful namespaces and responsibilities.

More nesting adds more import paths, navigation, and boundaries to understand. Create levels that earn their complexity.

## 48. A small project can grow in stages

Start simple:

```text
app.py
```

Then extract a real reusable responsibility:

```text
app.py
grade_tools.py
```

Then group related modules when the namespace becomes useful:

```text
app.py
study_tools/
├── __init__.py
├── grades.py
└── formatting.py
```

Structure should follow responsibilities, not a desire to look "enterprise" before the program needs it.

## 49. Exercise

Create a small package-based study application with this structure:

```text
study_app/
├── __init__.py
├── grading.py
└── formatting.py
run_study_app.py
```

Requirements:

1. In `grading.py`, create `classify_score(score: int) -> str` that returns `"ready"` for scores of at least 80 and `"review"` otherwise.
2. In `formatting.py`, create `format_result(topic: str, status: str) -> str`.
3. In `study_app/__init__.py`, keep initialization minimal. You may leave it empty or deliberately expose one documented package-level name.
4. In `run_study_app.py`, import the package functionality explicitly and print results for at least three fictional topics.
5. Put the executable behavior in a `main()` function.
6. Call `main()` only under `if __name__ == "__main__":`.
7. Do not mutate `sys.path`.
8. Do not use `from ... import *`.
9. Rename any file that would shadow a standard-library module you use.

Extra questions:

- Which names are bound by `import study_app.grading`?
- How would the local namespace differ with `from study_app.grading import classify_score`?
- What runs when `study_app.grading` is imported for the first time in a normal interpreter session?
- What does `__name__` contain in the directly executed entry file?
- Why can a relative import behave differently when a package module is executed by file path?
- When would `python -m package.module` be preferable?
- Why is a regular package's `__init__.py` allowed to be empty?

## 50. Review checklist

Before moving to the standard library phase, confirm that you can answer these without guessing:

- What is a module in an ordinary `.py`-based project?
- What name does `import grade_tools` bind?
- What changes with `from grade_tools import classify_score`?
- What does an `as` alias change?
- Can top-level code run during an import?
- What beginner-level role does `sys.modules` play?
- What is `__name__` when a file is the top-level program?
- What problem does the main guard solve?
- What does `sys.path` represent?
- Why can naming your file `json.py` cause trouble?
- How are `ModuleNotFoundError` and `ImportError` related?
- What makes a regular directory-based package recognizable in the conventional layout?
- Are namespace packages required to contain `__init__.py`?
- What do leading dots mean in a relative import?
- Why can `python -m package.module` be useful?
- What is the difference between an import package and a distribution package?
- Why are wildcard imports usually avoided?
- What can circular imports reveal about module design?

## 51. Quick reference

| Need | Pattern or idea |
|---|---|
| Import a module | `import module_name` |
| Access a module name | `module_name.item` |
| Import selected name | `from module_name import item` |
| Alias a module | `import module_name as alias` |
| Alias a selected name | `from module_name import item as alias` |
| Direct-entry guard | `if __name__ == "__main__":` |
| Module search locations | inspect `sys.path` |
| Normal import cache | `sys.modules` |
| Missing requested module | commonly `ModuleNotFoundError` |
| Broader import failure | `ImportError` |
| Conventional regular package marker | `__init__.py` |
| Import a package submodule | `import package.submodule` |
| Absolute package import | `from package.module import item` |
| Relative sibling import | `from .module import item` |
| Execute module by import name | `python -m package.module` |
| Execute package entry | `python -m package` with `package/__main__.py` |
| Avoid hidden namespace imports | prefer explicit names over `import *` |
| Avoid casual path surgery | do not use `sys.path` mutation as normal structure |

A useful dependency model is:

```text
entry point
    ↓ imports
coordinating modules
    ↓ imports
focused reusable modules
```

Aim for dependency direction that a learner can draw without creating a knot.

## Phase 7 complete

This chapter closes **Phase 7: Errors, Files, and Modules**.

The phase now connects failure handling, persistence boundaries, structured text data, and code organization:

```text
exceptions
    ↓
deliberate exception signaling
    ↓
safe file lifetime
    ↓
TXT / CSV / JSON data boundaries
    ↓
imports / modules / packages
```

You can now build a small program that fails deliberately when a contract is broken, handles expected external failures, persists text data safely, parses common formats, and separates reusable code across modules and packages.

## What comes next

**Phase 8: Standard Library** will build on the import model by exploring useful batteries that ship with Python, beginning with modules such as `pathlib` and `datetime` according to the project roadmap.

The important transition is:

```text
learn how imports organize dependencies
        ↓
use Python's standard-library modules deliberately
```

## Official references

- Python 3.14 tutorial, Modules: <https://docs.python.org/3.14/tutorial/modules.html>
- Python 3.14 language reference, The import system: <https://docs.python.org/3.14/reference/import.html>
- Python 3.14 language reference, The import statement: <https://docs.python.org/3.14/reference/simple_stmts.html#import>
- Python 3.14 command-line documentation, `-m`: <https://docs.python.org/3.14/using/cmdline.html#cmdoption-m>
- Python 3.14 `__main__` documentation: <https://docs.python.org/3.14/library/__main__.html>