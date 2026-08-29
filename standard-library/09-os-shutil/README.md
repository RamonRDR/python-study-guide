<div align="center">

# Engineering OS and Filesystem Operations with `os` and `shutil`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Standard Library](../README.md) · [← Previous: `decimal`](../08-decimal/README.md)

The earlier `pathlib` chapter introduced path objects as the default high-level way to represent and manipulate filesystem paths. This chapter goes lower and wider.

The `os` module exposes operating-system interfaces such as process environment state, current working directory, directory scanning, file metadata, renaming, directory traversal, permission-related capabilities, and lower-level path operations. The `shutil` module builds higher-level file and directory operations on top of those primitives, including copying, moving, recursive deletion, archive handling, executable discovery, and disk-usage inspection.

The goal is not to replace `pathlib`. It is to understand the contracts that appear when a program crosses the operating-system boundary.

**Estimated study time:** 220–300 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain the different roles of `pathlib`, `os`, `os.path`, and `shutil`;
- read and modify process environment variables deliberately;
- explain why current working directory is shared process state;
- use `os.PathLike` and `os.fspath()` at filesystem API boundaries;
- distinguish path separators from `PATH` separators;
- create directories safely with `mkdir()` and `makedirs()`;
- choose between `listdir()` and `scandir()`;
- use `DirEntry` metadata without assuming it stays fresh forever;
- inspect file metadata with `stat()`;
- remove files and empty directories with the correct primitive;
- distinguish `rename()` from replacement-oriented `replace()`;
- traverse directory trees with `walk()` and prune recursion safely;
- understand the risk of following symbolic links during recursive traversal;
- recognize advanced `dir_fd` and capability-detection APIs without assuming universal platform support;
- distinguish `copyfile()`, `copy()`, and `copy2()`;
- copy directory trees with explicit merge, ignore, and symlink policies;
- move files and directories while understanding same-filesystem and fallback behavior;
- use `rmtree()` only behind a carefully validated destructive-operation boundary;
- explain why metadata preservation is never a blanket guarantee;
- inspect disk usage and resolve executables through `PATH`;
- create and unpack archives with an explicit trust policy;
- use exceptions instead of pre-check races when performing filesystem I/O;
- make filesystem processing deterministic when directory enumeration order is unspecified;
- design safe, reviewable file-management workflows.

## 1. `os` is a bridge to operating-system services

`os` contains interfaces for many categories of operating-system behavior. This chapter focuses on the parts most relevant to portable application code:

```text
process environment
current working directory
filesystem paths
files and directories
metadata
directory traversal
filesystem capabilities
```

The module also exposes process-management and platform-specific APIs. Those are real parts of `os`, but they are intentionally outside this chapter's scope.

## 2. `shutil` operates at a higher filesystem level

`shutil` provides operations over files and collections of files:

```text
copy one file
copy a directory tree
move files or trees
remove directory trees
inspect disk usage
find executables
create and unpack archives
```

A useful mental model is:

```text
pathlib  -> model paths and perform convenient path-oriented operations
os       -> operating-system primitives and lower-level filesystem interfaces
shutil   -> high-level file and directory workflows
```

## 3. Do not treat the three modules as competitors

They overlap because they solve neighboring problems.

For ordinary path composition and inspection, `pathlib.Path` is often the clearest interface. `os` remains important when you need environment state, directory descriptors, byte paths, capability sets, or lower-level APIs. `shutil` remains useful for recursive copying, recursive deletion, archive operations, disk usage, and executable discovery.

Python 3.14 also added high-level `Path.copy()`, `Path.copy_into()`, `Path.move()`, and `Path.move_into()`. That increases overlap, but it does not make `os` or `shutil` obsolete.

## 4. Many filesystem APIs accept path-like objects

Since the path protocol was introduced, many `os` and `shutil` functions accept objects implementing `os.PathLike`.

```python
import os
from pathlib import Path


path = Path("reports") / "summary.txt"
print(os.fspath(path))
```

`Path` objects can therefore cross directly into many lower-level APIs without manual conversion to strings.

## 5. `os.fspath()` exposes the filesystem representation

```python
import os
from pathlib import Path


path = Path("data") / "input.csv"
raw_path = os.fspath(path)
print(type(raw_path).__name__)
```

For a normal `Path`, the result is a string.

Use `os.fspath()` when an API boundary genuinely requires the low-level `str` or `bytes` representation. Do not scatter conversions through code that can already accept path-like objects.

## 6. `os.PathLike` is a protocol, not a concrete path model

A path-like object implements `__fspath__()` and returns either `str` or `bytes`.

```python
import os


class ReportPath:
    def __fspath__(self):
        return "reports/output.txt"


print(os.fspath(ReportPath()))
```

In application code, `pathlib.Path` is usually preferable to inventing custom path classes. The protocol matters mainly because it explains interoperability between filesystem APIs.

## 7. `str` paths are usually the portable default

Many `os` functions support both `str` and `bytes` paths. Byte paths are useful in specialized low-level situations, especially on Unix, but they carry encoding complexity.

Prefer Unicode strings and `Path` objects unless the program has a specific reason to preserve raw filesystem bytes.

## 8. `fsencode()` and `fsdecode()` are explicit encoding boundaries

```python
import os


encoded = os.fsencode("notes.txt")
decoded = os.fsdecode(encoded)

print(decoded)
```

These functions use Python's configured filesystem encoding and error handler.

They are boundary tools, not a recommendation to convert all paths to bytes.

## 9. `os.name` is coarse platform information

```python
import os


print(os.name)
```

Common values include `"posix"` and `"nt"`.

Do not build broad platform branches when feature detection would be more precise. The exact operating system may matter less than whether a specific operation supports `dir_fd`, symbolic-link handling, or another capability.

## 10. The current working directory is process state

```python
import os


current = os.getcwd()
print(type(current).__name__)
```

Relative paths are interpreted against the process's current working directory.

That means a relative path is not self-contained. Its meaning depends on ambient state.

## 11. `os.chdir()` changes that ambient state

```python
import os


original = os.getcwd()
# os.chdir("another-directory")
# work happens relative to the new current directory
# os.chdir(original)
```

Changing the working directory affects later relative-path operations in the process. In concurrent or reusable code, hidden working-directory mutation can make behavior difficult to reason about.

Prefer absolute paths or explicit base paths when possible.

## 12. Restoring the working directory does not erase concurrency risk

A `try/finally` restoration pattern prevents one class of bug:

```python
import os


original = os.getcwd()
try:
    pass
    # os.chdir(target)
finally:
    os.chdir(original)
```

But while the directory is changed, other code in the same process can still observe that state. Scoped restoration is useful, but it is not isolation.

## 13. `os.environ` models the process environment

`os.environ` is a mutable mapping of environment-variable names to string values.

```python
import os


mode = os.environ.get("APP_MODE", "development")
print(mode)
```

Environment variables are often configuration boundaries. Treat them as external input rather than as trusted constants.

## 14. `os.getenv()` is convenient for defaulted reads

```python
import os


timeout_text = os.getenv("APP_TIMEOUT", "30")
print(timeout_text)
```

The result is still text. Convert and validate it according to the application contract.

```python
import os


timeout = int(os.getenv("APP_TIMEOUT", "30"))
```

A missing variable and an invalid variable are different conditions. A default only solves the missing-value case.

## 15. Modify `os.environ` instead of calling `putenv()` directly

```python
import os


KEY = "APP_MODE"
previous_value = os.environ.get(KEY)

try:
    os.environ[KEY] = "test"
    print(os.getenv(KEY))
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value
```

The example restores any pre-existing value, so running it in a REPL, notebook, or other long-lived process does not erase the caller's environment state.

Assignments to `os.environ` update the process environment through the appropriate platform mechanism.

Direct `os.putenv()` calls do not update the Python `os.environ` mapping, so modifying the mapping is normally the clearer contract.

## 16. Environment changes do not rewrite the parent process

A Python process can modify its own environment and the environment inherited by child processes it creates later. It cannot retroactively change the environment mapping of the shell or parent process that launched it.

Think of environment inheritance as downstream process configuration, not shared mutable storage between unrelated processes.

## 17. Environment values are strings

```python
import os


KEY = "WORKER_COUNT"
previous_value = os.environ.get(KEY)

try:
    os.environ[KEY] = "4"
    worker_count = int(os.environ[KEY])
    print(worker_count + 1)
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value
```

The same restoration rule applies when an environment value is temporarily changed only to demonstrate parsing.

Use explicit parsing for integers, booleans, lists, paths, URLs, and other structured configuration.

## 18. `os.environ` is a cached mapping

The mapping is captured when `os` is imported, normally during interpreter startup. Changes made through `os.environ` remain synchronized, but environment modifications performed outside that mapping may not be visible automatically.

That distinction matters mainly in advanced embedding or native-integration scenarios.

## 19. `os.reload_environ()` is new in Python 3.14

Python 3.14 adds:

```python
import os


# os.reload_environ()
```

It refreshes `os.environ` and `os.environb` from the current process environment.

The official documentation warns that `os.reload_environ()` is **not thread-safe**. Do not use it casually in a process where other threads may read or modify environment state concurrently.

## 20. `os.sep` and `os.pathsep` solve different problems

```python
import os


print(repr(os.sep))
print(repr(os.pathsep))
```

`os.sep` is the pathname-component separator, such as `/` or `\`.

`os.pathsep` separates entries in path-list environment variables such as `PATH`, commonly `:` on POSIX and `;` on Windows.

Confusing them is a classic portability bug.

## 21. Prefer path-aware composition over manual separators

Avoid:

```python
base = "reports"
filename = "summary.txt"
path = base + "/" + filename
```

Prefer `Path` or, when working in a procedural `os.path` interface, `os.path.join()`:

```python
import os


path = os.path.join("reports", "summary.txt")
print(path)
```

The separator is a platform concern, not a string-concatenation rule.

## 22. `os.path` remains a useful low-level path toolkit

Common functions include:

```text
os.path.join()
os.path.basename()
os.path.dirname()
os.path.splitext()
os.path.abspath()
os.path.realpath()
os.path.exists()
os.path.isfile()
os.path.isdir()
```

Use `pathlib` when object-oriented path code is clearer. Use `os.path` when working with existing string-path APIs, byte paths, or low-level code where its procedural style is natural.

## 23. Normalization is not one universal operation

`abspath()`, `realpath()`, and lexical path manipulation answer different questions. Symbolic links can make apparently simple cleanup of `..` segments semantically important.

Do not normalize a path merely to make it look prettier. Decide whether you need a lexical path, an absolute path, or resolution through filesystem links.

## 24. Create one directory with `os.mkdir()`

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "reports")
    os.mkdir(path)
    print(os.path.isdir(path))
```

`mkdir()` creates one directory level. Missing parents cause an error.

## 25. Create missing parent directories with `os.makedirs()`

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "year", "month", "reports")
    os.makedirs(path)
    print(os.path.isdir(path))
```

`makedirs()` recursively creates intermediate directories as needed.

## 26. `exist_ok=True` expresses idempotent directory creation

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "output")
    os.makedirs(path, exist_ok=True)
    os.makedirs(path, exist_ok=True)
    print(os.path.isdir(path))
```

Use this when an existing directory is an acceptable precondition. Do not use it when pre-existence should be treated as a conflict.

## 27. `os.listdir()` returns names in arbitrary order

```python
import os


names = os.listdir(".")
print(type(names).__name__)
```

The API does not promise sorted results.

When output, tests, archives, manifests, or processing order must be deterministic, sort explicitly:

```python
import os


for name in sorted(os.listdir(".")):
    pass
```

## 28. `os.scandir()` yields richer directory entries

```python
import os


with os.scandir(".") as entries:
    for entry in entries:
        if entry.is_file():
            pass
```

`scandir()` yields `os.DirEntry` objects that can expose file type and metadata efficiently. Code that needs those attributes can avoid repeated path lookups compared with a `listdir()` plus separate `stat()` calls.

## 29. Use the `scandir()` iterator as a context manager

```python
import os


with os.scandir(".") as entries:
    first_names = sorted(entry.name for entry in entries)[:3]

print(type(first_names).__name__)
```

The context manager ensures directory-scanning resources are closed promptly even when iteration ends early.

## 30. `DirEntry` metadata may be cached

A `DirEntry` can cache information obtained from the operating system.

That is good for a short directory scan. It is not a promise that the object remains a live view forever.

If metadata may have changed since the scan, call `os.stat(entry.path)` again instead of treating an old `DirEntry` as current truth.

## 31. `os.stat()` returns structured filesystem metadata

```python
import os
from tempfile import NamedTemporaryFile


with NamedTemporaryFile() as temp_file:
    info = os.stat(temp_file.name)
    print(info.st_size)
```

Useful fields include file size and several timestamps. Their exact meaning and availability can vary by platform and filesystem.

## 32. Prefer nanosecond timestamp fields when exact integer precision matters

`stat_result` exposes nanosecond variants such as `st_mtime_ns` where supported.

```python
import os
from tempfile import NamedTemporaryFile


with NamedTemporaryFile() as temp_file:
    info = os.stat(temp_file.name)
    print(isinstance(info.st_mtime_ns, int))
```

Floating-point timestamp fields are convenient, but integer nanoseconds avoid an unnecessary binary floating-point representation step.

## 33. Do not interpret `st_ctime` as universal creation time

Timestamp semantics differ across platforms. Historically, `st_ctime` has represented metadata-change time on Unix and creation-related information on Windows.

When creation or birth time is a requirement, check the specific platform fields and documentation instead of assigning one universal meaning to `ctime`.

## 34. Remove a file with `os.remove()` or `os.unlink()`

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "temporary.txt"
    path.write_text("temporary", encoding="utf-8")
    os.remove(path)
    print(path.exists())
```

For ordinary filesystem paths, `os.remove()` and `os.unlink()` are aliases with the same behavior.

## 35. `os.rmdir()` removes only an empty directory

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    child = Path(temp_dir) / "empty"
    child.mkdir()
    os.rmdir(child)
    print(child.exists())
```

That restriction is useful. Recursive deletion is a much larger operation and belongs behind a more explicit API such as `shutil.rmtree()`.

## 36. `os.rename()` does not have identical overwrite behavior everywhere

```python
import os


# os.rename(source, destination)
```

Renaming is affected by operating-system rules, destination type, and filesystem boundaries. Replacement behavior for an existing destination differs between platforms.

If overwriting an existing destination is part of the contract, use an API whose replacement semantics express that intent.

## 37. `os.replace()` expresses replacement intent

```python
import os


# os.replace(source, destination)
```

If the destination is an existing file and permissions allow replacement, `replace()` is designed to replace it without requiring a separate delete step.

The operation can fail across filesystems. On POSIX, a successful rename-style replacement is required to be atomic.

## 38. Avoid check-then-act races

This pattern is fragile:

```python
import os


path = "report.txt"
if os.path.exists(path):
    pass
    # open(path)
```

The filesystem can change between the check and the operation.

Prefer performing the operation and handling the relevant exception:

```python
try:
    with open("report.txt", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    content = ""
```

This is an example of EAFP: easier to ask forgiveness than permission.

## 39. `os.access()` is not a general preflight authorization test

`os.access()` has specialized uses, including real-ID permission checks on Unix.

Do not use it as a universal "can I safely open this file?" pre-check. The official documentation warns that check-then-open creates a race window, and network filesystems may have permission semantics beyond the local permission-bit model.

## 40. `os.walk()` traverses a directory tree

```python
import os


for root, dirnames, filenames in os.walk("."):
    print(root, len(dirnames), len(filenames))
    break
```

Each iteration yields:

```text
(root path, child directory names, child file names)
```

The child lists contain names, not complete paths.

## 41. Top-down walking allows recursion pruning

When `topdown=True`, modify `dirnames` in place to control which directories are visited:

```python
import os


for root, dirnames, filenames in os.walk(".", topdown=True):
    dirnames[:] = [name for name in dirnames if name != "__pycache__"]
```

Assigning a new local list without modifying `dirnames` would not prune the walk.

## 42. Sort directory names when traversal order matters

```python
import os


for root, dirnames, filenames in os.walk("."):
    dirnames.sort()
    filenames.sort()
```

Directory enumeration order is not a deterministic contract. Sort when downstream behavior depends on order.

## 43. Following directory symlinks can create cycles

By default, `os.walk()` does not follow symbolic links that resolve to directories.

If `followlinks=True`, a link can point back to an ancestor and create unbounded recursion. `os.walk()` does not automatically remember every directory it has already visited.

Following links should therefore be a deliberate graph-traversal decision, not a convenience flag.

## 44. `onerror` makes traversal failure policy explicit

```python
import os


def handle_error(error: OSError) -> None:
    print(type(error).__name__)


for _ in os.walk(".", onerror=handle_error):
    break
```

Without `onerror`, scanning errors are ignored by `walk()`. A callback can report the error and continue, or re-raise it to abort.

## 45. `os.fwalk()` adds a directory file descriptor

`fwalk()` yields:

```text
(dirpath, dirnames, filenames, dirfd)
```

The descriptor enables operations relative to the currently visited directory without rebuilding full paths.

This is an advanced tool. The yielded file descriptor is only valid until the next iteration step unless duplicated.

## 46. `dir_fd` support is capability-dependent

Several `os` APIs can operate relative to an open directory descriptor.

Do not assume that every platform supports every `dir_fd` combination. Python exposes capability sets such as:

```python
import os


print(isinstance(os.supports_dir_fd, set))
print(isinstance(os.supports_follow_symlinks, set))
```

Feature detection is better than pretending every operating system exposes identical filesystem primitives.

## 47. Symbolic-link behavior needs an explicit policy

Many filesystem APIs accept `follow_symlinks` or equivalent options.

The choice changes whether an operation targets:

```text
the symbolic link itself
or
the object referenced by the link
```

That distinction can affect metadata, deletion boundaries, security, and portability.

## 48. Use `shutil.copyfile()` for file contents only

```python
import shutil


# shutil.copyfile("source.txt", "destination.txt")
```

`copyfile()` copies file data to a complete destination filename. It does not promise metadata preservation.

If source and destination identify the same file, `SameFileError` is raised.

## 49. `shutil.copy()` also copies permission mode

```python
import shutil


# shutil.copy("source.txt", "backup/")
```

`copy()` can accept a destination directory. In addition to file data, it copies the permission mode.

It does not attempt the broader metadata preservation of `copy2()`.

## 50. `shutil.copy2()` attempts broader metadata preservation

```python
import shutil


# shutil.copy2("source.txt", "destination.txt")
```

`copy2()` uses `copystat()` to attempt to preserve metadata such as permission bits, access time, modification time, flags, and some extended attributes where supported.

The word **attempts** matters.

## 51. No `shutil` copy is a complete metadata clone

The official documentation explicitly warns that high-level copy functions cannot preserve every kind of metadata on every platform.

Examples of metadata that may not be preserved include ownership, ACLs, resource forks, or alternate data streams depending on the operating system.

If exact filesystem metadata replication is a requirement, verify the target platform and use tools designed for that contract.

## 52. `follow_symlinks` changes copy semantics

With a symlink source:

```text
follow_symlinks=True  -> copy the referenced object's contents
follow_symlinks=False -> recreate a symbolic link where supported
```

Do not choose the flag after the code is written. Decide whether links are topology or indirection in the data model first.

## 53. `copymode()` and `copystat()` separate metadata operations

```python
import shutil


# shutil.copymode(source, destination)
# shutil.copystat(source, destination)
```

`copymode()` copies permission bits.

`copystat()` attempts a broader set of metadata without copying file contents, owner, or group.

These helpers are useful when data copying and metadata copying are separate workflow steps.

## 54. `shutil.copytree()` copies a directory tree

```python
import shutil


# shutil.copytree(source_dir, destination_dir)
```

By default, `copytree()` recursively creates the destination tree and uses `copy2()` for individual files.

A recursive copy is a workflow, not one file operation. Define destination-existence, symlink, ignore, and error policies deliberately.

## 55. `dirs_exist_ok` controls destination merging

```python
import shutil


# shutil.copytree(source, destination, dirs_exist_ok=True)
```

When `False`, the default, an existing destination directory is a conflict.

When `True`, existing directories may be reused and corresponding destination files can be overwritten.

That switch can turn a "create backup" operation into a "merge into existing tree" operation, so name and document the policy clearly.

## 56. `ignore_patterns()` creates a reusable copy filter

```python
import shutil


ignore = shutil.ignore_patterns("*.tmp", "__pycache__")
# shutil.copytree(source, destination, ignore=ignore)
```

Ignore patterns apply recursively by name within each directory visited by `copytree()`.

Treat ignored data as part of the backup or deployment contract. A pattern that silently omits required files is still a correctness bug.

## 57. `copytree()` can aggregate multi-file errors

A recursive copy may encounter more than one failure. `shutil.Error` can contain multiple `(source, destination, exception)` tuples collected during the operation.

When reliability matters, do not reduce a multi-file failure to a single generic "copy failed" message. Preserve enough context to diagnose which paths failed.

## 58. `shutil.move()` handles files and directory trees

```python
import shutil


# final_path = shutil.move(source, destination)
```

If the destination is an existing directory, the source is normally moved inside it.

The exact destination contract should be explicit in code because "move to this path" and "move inside this directory" are different operations.

## 59. Moving may become copy-then-delete

`shutil.move()` prefers a rename-style operation when possible. When that cannot be used, such as across filesystems, it can fall back to copying and then removing the source.

That means a move is not universally one atomic metadata operation.

For workflows that require atomic replacement, same-filesystem guarantees and an API such as `os.replace()` may be more appropriate.

## 60. Recursive deletion deserves a hard boundary

```python
import shutil


# shutil.rmtree(target_directory)
```

`rmtree()` deletes an entire directory tree.

Before calling it in real software, validate the target from trusted state. A path typo, empty configuration value, incorrect base directory, or symlink boundary mistake can transform cleanup into data loss.

## 61. Prefer positive target validation before destructive operations

A destructive workflow can validate that the resolved target belongs under an expected workspace before deletion.

```python
from pathlib import Path


workspace = Path("build").resolve()
target = (workspace / "temporary").resolve()

if target.parent != workspace:
    raise ValueError("unexpected cleanup target")
```

This example is intentionally strict. Real nested-workspace policies may need `Path.is_relative_to()` or another explicit containment rule.

Validation reduces accidental scope errors, but filesystem races and symlink behavior still require careful design in hostile environments.

## 62. `rmtree()` has platform-dependent symlink-attack resistance

On platforms with the required file-descriptor-based APIs, Python uses a symlink-attack-resistant `rmtree()` implementation by default.

You can inspect:

```python
import shutil


print(isinstance(shutil.rmtree.avoids_symlink_attacks, bool))
```

A security-sensitive application should not assume that every supported platform provides the same protection.

## 63. `onexc` is the modern `rmtree()` error callback

Python 3.12 added `onexc` and deprecated the older `onerror` callback.

```python
import shutil


def handle_remove_error(function, path, exception):
    print(type(exception).__name__)


# shutil.rmtree(target, onexc=handle_remove_error)
```

The callback can inspect the operation, path, and exception. Exceptions raised by the callback propagate.

## 64. `rmtree()` changed missing-file handling in Python 3.13

Since Python 3.13, `rmtree()` ignores `FileNotFoundError` for entries below the top-level target while the traversal is in progress.

A missing top-level path still matters.

This makes concurrent disappearance of nested entries less disruptive without turning an absent requested root into silent success.

## 65. `shutil.disk_usage()` reports filesystem capacity

```python
import shutil


usage = shutil.disk_usage(".")
print(hasattr(usage, "free"))
```

The named tuple contains total, used, and free byte counts.

The actual values are environment-dependent. Do not hard-code them into tests or documentation examples.

## 66. `shutil.which()` resolves executables through a search path

```python
import shutil


python_path = shutil.which("python")
print(python_path is None or isinstance(python_path, str))
```

By default, `which()` consults the process `PATH` environment variable and uses `os.pathsep` to interpret its directory list.

The exact result is environment-dependent, so application code must handle `None`.

## 67. `copyfileobj()` copies between open file-like objects

```python
import io
import shutil


source = io.StringIO("alpha\nbeta\n")
destination = io.StringIO()
shutil.copyfileobj(source, destination)
print(destination.getvalue())
```

This works at the stream level instead of accepting filesystem path names.

For real buffered file objects, `copyfileobj()` does not guarantee that the destination has been flushed when it returns. Flush or close before another consumer must observe the copied data.

## 68. High-level copy functions may use fast system calls

Since Python 3.8, several `shutil` copy operations may use platform-specific fast-copy syscalls internally.

The optimization is an implementation detail behind the same public API. Do not duplicate a manual read/write loop merely to assume it will be faster.

Python 3.14 expanded some of these platform optimizations, including additional copy-on-write or server-side-copy possibilities on supported systems.

## 69. `make_archive()` creates a packaged tree

```python
import shutil


# archive_path = shutil.make_archive("backup", "zip", root_dir="workspace")
```

The returned path includes the archive extension selected by the format.

Archive creation is different from a byte-for-byte filesystem clone. Metadata and format capabilities vary.

## 70. Archive extraction is a trust boundary

```python
import shutil


# shutil.unpack_archive("backup.zip", "restored")
```

Never treat extraction from an untrusted archive as a harmless copy operation.

Archive entries can attempt to influence target paths, links, permissions, or other filesystem behavior. Python 3.14's built-in extraction defaults block the most dangerous path cases, but the official documentation still recommends inspection and an explicit trust policy.

## 71. Tar extraction filters became safer by default in Python 3.14

For tar-based formats, `shutil.unpack_archive()` passes extraction filtering to the underlying tar implementation. The `"data"` filter is the default starting in Python 3.14.

```python
import shutil


# shutil.unpack_archive("backup.tar", "restored", filter="data")
```

ZIP extraction does not accept that `filter` argument.

A safer default reduces risk. It does not make arbitrary untrusted archives automatically safe for every application.

## 72. Filesystem exceptions are part of the design

Common exceptions include:

```text
FileNotFoundError
FileExistsError
PermissionError
NotADirectoryError
IsADirectoryError
OSError
shutil.SameFileError
shutil.SpecialFileError
shutil.Error
```

Catch the narrowest exception that represents an expected branch in the workflow. Let unexpected failures remain visible.

## 73. A practical environment contract

```python
import os


KEY = "PYTHON_STUDY_GUIDE_MODE"
MISSING_KEY = "PYTHON_STUDY_GUIDE_MISSING"
previous_value = os.environ.get(KEY)
previous_missing = os.environ.pop(MISSING_KEY, None)

try:
    os.environ[KEY] = "practice"
    print(f"configured: {os.getenv(KEY)}")
    print(f"fallback: {os.getenv(MISSING_KEY, 'default')}")
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value

    if previous_missing is not None:
        os.environ[MISSING_KEY] = previous_missing
```

```text
configured: practice
fallback: default
```

The example modifies only its own process environment and restores any pre-existing value.

## 74. A practical deterministic directory scan

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    (workspace / "alpha.txt").write_text("alpha\n", encoding="utf-8")
    (workspace / "data").mkdir()
    (workspace / "data" / "values.txt").write_text("1\n2\n", encoding="utf-8")

    with os.scandir(workspace) as entries:
        for entry in sorted(entries, key=lambda item: item.name):
            kind = "dir" if entry.is_dir() else "file"
            print(f"{entry.name}: {kind}")
```

```text
alpha.txt: file
data: dir
```

The important detail is the explicit sort. `scandir()` itself does not promise directory order.

## 75. A practical walk with pruning

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    (workspace / "src").mkdir()
    (workspace / "src" / "app.py").write_text("print('ready')\n", encoding="utf-8")
    (workspace / "cache").mkdir()
    (workspace / "cache" / "ignored.bin").write_bytes(b"ignored")

    for root, dirnames, filenames in os.walk(workspace, topdown=True):
        dirnames[:] = sorted(name for name in dirnames if name != "cache")
        filenames.sort()

        relative_root = Path(root).relative_to(workspace)
        label = "." if relative_root == Path(".") else relative_root.as_posix()
        print(f"{label}: {filenames}")
```

```text
.: []
src: ['app.py']
```

The `cache` directory is removed from `dirnames` before recursion reaches it.

## 76. A practical copy-tree and move workflow

```python
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source = workspace / "source"
    destination = workspace / "backup"
    archive = workspace / "archive"

    (source / "reports").mkdir(parents=True)
    (source / "reports" / "summary.txt").write_text("ready\n", encoding="utf-8")
    (source / "scratch.tmp").write_text("temporary\n", encoding="utf-8")

    shutil.copytree(source, destination, ignore=shutil.ignore_patterns("*.tmp"))
    archive.mkdir()
    moved_path = Path(shutil.move(destination / "reports" / "summary.txt", archive))

    copied_names = sorted(path.name for path in destination.iterdir())
    print(f"backup entries: {copied_names}")
    print(f"moved file: {moved_path.name}")
    print(f"content: {moved_path.read_text(encoding='utf-8').strip()}")
```

```text
backup entries: ['reports']
moved file: summary.txt
content: ready
```

The ignored temporary file never enters the copied tree, and the returned move path is treated as data rather than guessed.

## 77. Common mistakes

### Mistake: manual path separators

```python
path = "reports/" + "summary.txt"
```

Prefer `Path` or `os.path.join()`.

### Mistake: changing working directory inside a reusable helper

A hidden `os.chdir()` can change the meaning of relative paths in unrelated code.

### Mistake: treating environment strings as already validated configuration

```python
import os


workers = os.getenv("WORKERS", "4")
# workers + 1  # TypeError
```

Parse the external text into the required type and validate its range.

### Mistake: relying on directory enumeration order

`listdir()`, `scandir()`, and filesystem traversal should not be assumed to return alphabetical order.

### Mistake: using `os.access()` before `open()` as a safety guarantee

The path can change between check and use. Attempt the I/O and handle its exception.

### Mistake: saying `copy2()` copies everything

It attempts more metadata than `copy()`, but metadata guarantees remain platform-dependent.

### Mistake: using `dirs_exist_ok=True` without realizing it merges

That flag can overwrite files in an existing destination tree.

### Mistake: enabling `followlinks=True` without cycle handling

A symlink to an ancestor can produce unbounded traversal.

### Mistake: calling `rmtree()` on a path assembled from unchecked external input

Recursive deletion should operate on a validated target under a trusted base.

### Mistake: extracting untrusted archives directly into a sensitive directory

Archive extraction is an input-validation and filesystem-security boundary.

## 78. Decision table

| Requirement | Prefer |
|---|---|
| model and compose paths | `pathlib.Path` |
| procedural low-level path manipulation | `os.path` |
| read process environment | `os.environ` / `os.getenv()` |
| convert a path-like object to `str` or `bytes` | `os.fspath()` |
| create one directory | `os.mkdir()` |
| create parent directories recursively | `os.makedirs()` |
| list only names | `os.listdir()` |
| scan names plus file-type or metadata hints | `os.scandir()` |
| inspect metadata | `os.stat()` |
| remove one file | `os.remove()` / `os.unlink()` |
| remove one empty directory | `os.rmdir()` |
| replace a destination by rename semantics | `os.replace()` |
| traverse a directory tree | `os.walk()` |
| copy file contents only | `shutil.copyfile()` |
| copy file plus permission mode | `shutil.copy()` |
| attempt broader metadata preservation | `shutil.copy2()` |
| copy a directory tree | `shutil.copytree()` |
| move a file or tree | `shutil.move()` |
| recursively remove a directory tree | `shutil.rmtree()` with strict target validation |
| inspect capacity | `shutil.disk_usage()` |
| resolve an executable | `shutil.which()` |
| create an archive | `shutil.make_archive()` |
| unpack a trusted or validated archive | `shutil.unpack_archive()` |

## 79. Quick reference

```text
os.getcwd()
os.chdir(path)

os.environ["KEY"]
os.environ.get("KEY")
os.getenv("KEY", default)
os.reload_environ()                 # Python 3.14+, not thread-safe

os.fspath(path)
os.fsencode(path)
os.fsdecode(path)
os.sep
os.pathsep
os.path.join(...)
os.path.abspath(path)
os.path.realpath(path)

os.mkdir(path)
os.makedirs(path, exist_ok=True)
os.listdir(path)
os.scandir(path)
os.stat(path)
os.remove(path)
os.unlink(path)
os.rmdir(path)
os.rename(src, dst)
os.replace(src, dst)
os.walk(path)
os.fwalk(path)

os.supports_dir_fd
os.supports_follow_symlinks
os.supports_fd

shutil.copyfile(src, dst)
shutil.copy(src, dst)
shutil.copy2(src, dst)
shutil.copymode(src, dst)
shutil.copystat(src, dst)
shutil.copytree(src, dst)
shutil.ignore_patterns(...)
shutil.move(src, dst)
shutil.rmtree(path)
shutil.disk_usage(path)
shutil.which(command)
shutil.copyfileobj(source, destination)
shutil.make_archive(...)
shutil.unpack_archive(...)
```

## 80. Design checklist

Before a filesystem workflow crosses into `os` or `shutil`, ask:

- Is `Path` enough for the path-modeling part?
- Is the input path trusted, validated, or externally supplied?
- Does the operation depend on the current working directory?
- Could I make the base path explicit instead?
- Is environment text converted and validated before use?
- Does deterministic output require sorting directory entries?
- Am I holding `DirEntry` data longer than its freshness assumptions allow?
- Could the filesystem change between a pre-check and the real operation?
- Should I attempt the operation and handle an exception instead?
- Is the destination allowed to exist already?
- Is overwrite or replacement intentional?
- Could source and destination be on different filesystems?
- What is the symbolic-link policy?
- Could traversal follow a cycle?
- Does recursive copy merge with an existing tree?
- Which metadata must actually be preserved?
- Is recursive deletion restricted to a positively validated base?
- Is the archive trusted, inspected, or extracted into an isolated location?
- Does the target platform support the advanced capability I plan to use?
- Is a Python-version-specific behavior documented?
- Have destructive paths been tested with temporary directories first?

## 81. Exercise

Build a fictional workspace backup utility with these requirements:

1. Read the source and destination base directories from function arguments, not from `chdir()`.
2. Accept an optional environment variable `BACKUP_MODE` with a documented default.
3. Validate that the mode is one of a small allowed set.
4. Scan the source tree recursively.
5. Skip directories named `cache` and `__pycache__` by pruning `dirnames` in a top-down `os.walk()`.
6. Sort directories and files before producing a manifest.
7. Refuse to copy when the source directory does not exist.
8. Copy the tree with `shutil.copytree()` and an explicit ignore policy for `*.tmp`.
9. Decide whether an existing destination is an error or a merge and document the choice.
10. Return a summary containing copied file count and destination path.
11. Do not recursively delete anything unless the target is proven to be inside a dedicated temporary workspace.
12. Catch only expected filesystem exceptions and let unexpected errors remain visible.

Extension challenges:

- add a dry-run mode that lists planned actions without mutating the filesystem;
- record file sizes with `os.stat()`;
- resolve an optional external compressor with `shutil.which()` and handle `None`;
- create a ZIP archive with `shutil.make_archive()`;
- write tests using `tempfile.TemporaryDirectory()` so no real user files are touched;
- document how symbolic links should be handled.

## 82. Connections to earlier Python concepts

`os` and `shutil` connect many earlier topics:

- **Files and context managers:** filesystem operations still depend on correct resource lifetime.
- **Exceptions:** `OSError` subclasses are normal control boundaries for expected I/O failures.
- **`pathlib`:** path objects compose naturally with path-like-aware `os` and `shutil` APIs.
- **Strings:** environment variables and many path boundaries arrive as text.
- **Collections:** `os.environ` is mapping-like, `walk()` yields lists, and traversal often builds manifests.
- **Functions:** safe file operations benefit from small helpers with explicit source, destination, and policy parameters.
- **Logging:** recursive copy, move, and cleanup workflows are natural places for structured operational evidence.
- **`datetime`:** file metadata contains timestamps whose platform semantics must be interpreted carefully.
- **`json` and `csv`:** filesystem utilities often discover, move, or archive files that are then parsed under separate data-format contracts.
- **`itertools`:** large file lists may be processed lazily after discovery, but the underlying filesystem can still change while iteration proceeds.
- **`decimal`:** `st_*_ns` integer timestamps illustrate again that representation choice is part of a data contract.

## References

Primary references used for this chapter:

- [Python 3.14 documentation: `os` - Miscellaneous operating system interfaces](https://docs.python.org/3.14/library/os.html)
- [Python 3.14 documentation: `shutil` - High-level file operations](https://docs.python.org/3.14/library/shutil.html)
- [Python 3.14 documentation: `pathlib` - Object-oriented filesystem paths](https://docs.python.org/3.14/library/pathlib.html)
- [Python 3.14 documentation: `os.path` - Common pathname manipulations](https://docs.python.org/3.14/library/os.path.html)
- [Python glossary: EAFP](https://docs.python.org/3.14/glossary.html#term-EAFP)

## Phase 8 complete

This chapter closes **Phase 8: Standard Library**.

The phase started with object-oriented path modeling in `pathlib` and progressed through date/time contracts, structured data formats, logging, specialized collections, lazy iteration, decimal arithmetic, and finally the operating-system boundary itself.

Continue with **Phase 9: External Libraries**: [`pandas` — Working with Tabular Data](../../external-libraries/01-pandas/README.md).
