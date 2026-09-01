<div align="center">

# Project 06 · File Organizer

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Practical Projects](../README.md)

> **Phase 10 · Practical Projects**

This project organizes direct child files into category folders while keeping discovery, planning, collision handling, and filesystem mutation explicit and testable.

## Learning objectives

By the end of this project, you should be able to:

- discover direct files with `pathlib` without recursive traversal;
- classify filenames deterministically with case-insensitive suffix rules;
- model planned filesystem changes with immutable dataclasses;
- separate a non-mutating planning phase from a mutating execution phase;
- detect exact and case-insensitive destination collisions;
- choose explicit collision policies instead of silently overwriting data;
- treat symlinks and special files as filesystem boundaries;
- reason about time-of-check/time-of-use races;
- compare filesystem objects by `(device, inode)` identity;
- anchor directories with file descriptors on Linux;
- pin sources without blocking on late FIFO replacements;
- use atomic no-replace rename semantics at the final exact-name commit boundary;
- distinguish logical casefold collision checks from exact-name atomic guarantees;
- preserve uncertain state instead of blindly deleting entries during recovery;
- test filesystem code safely with temporary directories.

## Problem

Imagine a fictional workspace containing:

```text
workspace/
├── notes.txt
├── rows.csv
├── photo.png
├── backup.tar.gz
└── script.py
```

The organizer should produce:

```text
workspace/
├── documents/
│   └── notes.txt
├── data/
│   └── rows.csv
├── images/
│   └── photo.png
├── archives/
│   └── backup.tar.gz
└── other/
    └── script.py
```

The important challenge is not merely moving files. The project makes filesystem decisions visible before mutation and refuses to claim safety guarantees the current platform cannot enforce.

## Requirements

The implementation must:

1. accept an existing non-symlink source directory;
2. inspect only direct children;
3. ignore nested directories;
4. report direct-child symlinks separately instead of following them;
5. classify regular files by filename suffix;
6. preserve filenames exactly;
7. create destination folders only when required;
8. produce deterministic ordering;
9. build an immutable plan before mutation;
10. reject invalid category paths, including symlinked category directories;
11. detect exact and case-insensitive destination collisions during planning/preflight;
12. support explicit `ERROR` and `SKIP` planning policies;
13. run a complete execution preflight;
14. bind each source filesystem identity when execution begins, not during planning;
15. never silently replace an exact destination;
16. recheck casefold-equivalent destination names immediately before commit;
17. reject source changes after execution-time identity binding and reject stale root/category assumptions;
18. never blindly unlink a staging or rollback entry whose identity may have changed;
19. return a structured result only after the planned destination is verified.

## Deliberate scope

The pipeline is:

```text
source directory
    -> direct-file discovery
    -> suffix classification
    -> collision-safe plan
    -> execution preflight
    -> anchored category folders
    -> source claim
    -> mutation-time casefold recheck
    -> atomic exact-name no-replace destination commit
```

This project intentionally excludes:

- recursive organization;
- MIME or content inspection;
- automatic duplicate renaming;
- hashing or deduplication;
- deletion as a user-facing feature;
- whole-plan rollback transactions;
- filesystem watchers;
- GUI interaction;
- cloud storage;
- cross-filesystem moves.

Keeping these responsibilities out of scope makes the safety rules easier to inspect.

## Categories

`FileCategory` defines five destinations:

| Category | Folder | Representative suffixes |
|---|---|---|
| Documents | `documents/` | `.txt`, `.md`, `.pdf`, `.docx` |
| Data | `data/` | `.csv`, `.json`, `.xml`, `.xlsx` |
| Images | `images/` | `.png`, `.jpg`, `.webp`, `.svg` |
| Archives | `archives/` | `.zip`, `.7z`, `.tar.gz`, `.tar.xz` |
| Other | `other/` | anything not matched above |

Matching is case-insensitive. Classification uses filenames only and never opens file contents.

## Core models

### `MoveAction`

Represents one planned move:

```text
source file -> category destination
```

Its invariants require absolute paths, the same source/destination filename, and a destination folder matching the selected category.

### `OrganizationPlan`

Stores:

- the absolute source directory;
- sorted `MoveAction` values;
- files skipped because of collisions;
- ignored direct-child symlinks.

The plan is immutable. Creating it does not create directories and does not move files. It records **pathname/category intent**, not an open descriptor or durable snapshot of the filesystem object behind each pathname. If a regular file is replaced at the same planned pathname before `execute_plan()` begins binding sources, the replacement is the current object selected by that pathname intent. Strong object identity starts at execution-time pinning.

### `OrganizationResult`

Records the exact planned destinations returned after successful execution.

## Discovery is intentionally shallow

`discover_files()` returns direct regular-file children only.

Recursive movement introduces additional contracts for relative paths, nested category folders, and duplicate names across directories. Those belong to a larger project.

## Planning before mutation

`plan_organization()` validates the workspace, scans direct files, classifies them, and calculates destinations without changing the filesystem.

```text
observe -> decide -> validate -> mutate
```

The proposal exists as data before side effects begin, which makes review and testing easier. This separation deliberately does **not** promise that a pathname still names the identical filesystem object observed during planning; retaining that guarantee would require keeping live source descriptors inside the plan. Execution instead binds the current regular object at each planned pathname before any category creation or source mutation.

## Collision policies

### `CollisionPolicy.ERROR`

Planning raises `FileExistsError` when a destination name already exists.

### `CollisionPolicy.SKIP`

Conflicting source files remain in the source directory and are listed in `skipped_collisions`.

Execution rechecks collisions after planning. Exact-name existence is enforced atomically at the final Linux commit; casefold-equivalent names are rechecked immediately before that commit.

## Case-insensitive collision checks

Filesystems differ in case sensitivity. The organizer therefore compares logical destination names using `casefold()`.

```text
Report.TXT
report.txt
```

These names are treated as a logical collision during planning, preflight, and the mutation-time recheck even on a case-sensitive filesystem.

There is an important boundary: on a case-sensitive filesystem, the kernel primitive `RENAME_NOREPLACE` protects only the **exact destination name**. A non-cooperating external process could still create a different casefold-equivalent name in the tiny interval after the final casefold scan. The project therefore does not claim atomic case-insensitive uniqueness where the filesystem does not provide it.

## Symlink and directory-anchor boundaries

The organizer does not follow direct-child symlinks. It rejects a source directory or category folder that is a symlink. On Windows, source directories and category folders that are NTFS junctions are rejected too: `is_dir()` follows a junction, so accepting one could redirect discovery or a planned move outside the workspace.

On the secure Linux path, the source root and required category directories are opened with `O_DIRECTORY | O_NOFOLLOW`. Their `(device, inode)` identities are repeatedly compared with the paths that should still reach them.

This matters because a directory file descriptor remains attached to the same directory even if another process renames that directory. Descriptor pinning prevents symlink redirection, while anchor validation prevents execution from silently continuing inside a directory that is no longer reachable at the planned path.

## Why preflight is not enough

A naive implementation might do:

```python
if not destination.exists():
    source.rename(destination)
```

That check can become stale immediately. Another process may create the destination or replace a source or directory after validation.

Preflight reduces the number of unsafe states, but concurrency-sensitive guarantees must also exist at the mutation boundary.

## Filesystem identity

The implementation represents identity with:

```text
(st_dev, st_ino)
```

The filename `notes.txt` is a directory entry. It is not the identity of the underlying filesystem object.

Planning records pathname intent rather than source-object identity. Therefore a regular file replaced at the same pathname **before execution-time pinning** is accepted as the current object selected by the plan. During secure Linux execution, source identity is accepted **only after the current source has been opened** with `O_NOFOLLOW | O_NONBLOCK` when `O_NONBLOCK` is available. The following `fstat()` derives `(device, inode)` from that already-open descriptor, and every planned source descriptor stays open until the plan finishes. An accepted inode that is later unlinked therefore cannot be freed and immediately reused while execution still depends on its identity. The nonblocking flag also prevents a late FIFO replacement from hanging `open()`. Descriptor pinning stabilizes object identity, not file contents; concurrent writes to the same inode are outside this project's snapshot guarantees.

## Fixed-length staging names

The secure Linux path temporarily claims the public source entry under an internal name:

```text
.fo-stage-<32 hexadecimal characters>
```

The stage name has fixed length and never embeds the original filename. A valid long filename therefore cannot make the internal name exceed a typical filesystem `NAME_MAX` limit.

## Atomic no-replace commit on Linux

The secure Linux path uses `renameat2(..., RENAME_NOREPLACE)` through pinned directory descriptors.

Conceptually:

```text
1. validate paths and collision preflight
2. open and anchor the source root
3. open the current regular file at every planned pathname and accept identity from `fstat()` on that pinned descriptor
4. keep all accepted source descriptors open through plan completion
5. open and anchor required category directories
6. claim source name -> short internal stage with no-replace semantics
7. verify stage identity and directory anchors
8. rescan the pinned category for a casefold-equivalent destination
9. atomically rename stage -> exact destination with RENAME_NOREPLACE
10. verify destination identity and anchors
11. report success
```

`RENAME_NOREPLACE` makes **exact destination-name** existence part of the atomic filesystem operation. There is no separate `exists()` check followed by a replacing rename. The preceding casefold scan catches logical collisions visible at that boundary, but it is intentionally documented as a recheck rather than an atomic case-insensitive lock.

The normal secure path does **not** finalize a move by calling `unlink()` on the staging name. This avoids transferring the same check-to-unlink race from the public source name to an internal name.

## Conservative recovery

Concurrency errors can leave uncertain state. Recovery therefore favors preservation over destructive cleanup.

If execution has already claimed the source into a staging entry and later detects an unsafe condition, it may create a no-replace hard link back to the original source name when possible. It does not blindly delete the staging entry.

A staging pathname is not an inode lock. If the final rename consumes a replacement entry and destination identity verification detects the mismatch, execution leaves the unrelated destination intact and, before closing the still-pinned source file descriptor, copies the planned source bytes into an exclusive `.fo-recovery-*` regular file. This preserves recoverable data without claiming that the original inode survived the race.

Safe Linux execution therefore deliberately requires read access to each planned regular file. Readability is validated before category directories are created and again when the source inode is pinned for mutation; permission failures are reported as `PermissionError`, not as a false source-identity change.

This can intentionally leave an internal recovery entry in unusual race/failure scenarios. The `.fo-stage-*` and `.fo-recovery-*` prefixes are reserved internal namespaces and are excluded from later discovery so recovery evidence is not accidentally reorganized. That is preferable to deleting or reclassifying uncertain data whose current identity cannot be proven.

The whole multi-file plan is not transactional.

## Platform contract

The implementation is explicit about platform guarantees:

- **Linux:** secure descriptor-anchored execution uses `renameat2(RENAME_NOREPLACE)` when available, with atomic no-replace protection for the exact destination name and mutation-time casefold rechecks;
- **Windows:** the guarded portable path relies on Windows `os.rename()` refusing an existing destination and performs best-effort casefold, redirect, and identity checks. It does **not** claim the descriptor-pinned adversarial race resistance of the Linux path;
- **other POSIX platforms:** execution raises `NotImplementedError` when the project cannot enforce the required no-replace semantics safely.

A safety-oriented example should fail honestly instead of silently downgrading its contract.

## Execution flow

`execute_plan()` performs:

1. plan type validation;
2. source-directory revalidation;
3. category-path revalidation;
4. destination collision preflight;
5. platform capability selection;
6. Linux: bind the current regular file at every planned pathname by pinning it before accepting identity and before category mutation;
7. anchored directory setup;
8. source claim;
9. mutation-time casefold collision recheck;
10. atomic exact-name no-replace commit;
11. destination/anchor verification;
12. `OrganizationResult` construction.

## Determinism

Files and actions are sorted by:

```python
(path.name.casefold(), path.name)
```

This keeps examples, tests, and review output stable.

## Running the demo

From the repository root:

```bash
python practical-projects/06-file-organizer/demo.py
```

The demo uses `TemporaryDirectory`, creates fictional files only, prints the plan, executes it, and shows the resulting folders.

## Running the tests

Focused suite:

```bash
python -m pytest practical-projects/06-file-organizer/tests -q
```

The chapter intentionally avoids a fixed test count because review-driven regression coverage evolves.

Coverage includes:

- suffix classification;
- deterministic shallow discovery;
- symlink handling;
- immutable model invariants;
- exact and case-insensitive collisions;
- `ERROR` and `SKIP` policies;
- stale and missing sources;
- late exact destinations;
- late casefold-equivalent destinations before final commit;
- late source symlink/file/FIFO replacement;
- nonblocking source pinning;
- category symlink and rename races;
- source-root rename races;
- fixed-length staging names;
- staging finalization without `unlink()`;
- destination identity verification;
- successful execution and empty plans.

## Failure paths worth studying

### Missing source directory

Raises `FileNotFoundError`.

### Source path is a regular file

Raises `NotADirectoryError`.

### Source directory is a symlink

Rejected before scanning.

### Category path is a file or symlink

Rejected before planning or execution.

### Destination appears after planning

Preflight and the mutation-time casefold recheck raise `FileExistsError` for collisions they observe. The final Linux `RENAME_NOREPLACE` atomically rejects an exact-name destination that appears at the commit boundary.

### Planned source becomes a FIFO or another special file

The Linux source pin uses nonblocking open flags, then `fstat()` rejects the replacement as non-regular instead of hanging execution.

### Planned source changes

Execution raises instead of treating the replacement as the planned file.

### Source root or category directory is renamed/replaced

Anchor verification raises instead of returning a path that no longer identifies the committed destination.

### Atomic no-replace primitive is unavailable

The unsupported platform path raises rather than weakening the safety contract silently.

## Common mistakes

### Moving while scanning

Mixing discovery and mutation makes partial failure difficult to reason about. Build a plan first.

### Treating a filename as object identity

Directory entries can be replaced while preserving the same name. Use filesystem identity when the distinction matters.

### Opening a possibly replaced path in blocking mode

`O_NOFOLLOW` rejects symlinks but does not stop a FIFO from blocking a read-only `open()`. Use nonblocking pinning before validating the file type.

### Assuming a casefold scan is an atomic lock

A user-space directory scan can detect logical case-insensitive collisions, but on a case-sensitive filesystem it cannot make a later differently cased name impossible. Keep the atomic guarantee scoped to the exact name enforced by the kernel primitive.

### Checking immediately before `unlink()`

A check-to-unlink window still exists. When deletion identity matters, restructure the operation instead of adding another check.

### Assuming an open directory descriptor still has the same pathname

A descriptor follows the directory inode through rename. Verify its anchor against the planned path.

### Embedding the full source filename in a staging name

Valid source names may already be near `NAME_MAX`. Keep internal names bounded independently.

### Blind cleanup after a race

Cleanup is mutation too. Preserve uncertain entries rather than deleting something that may belong to another actor.

### Treating preflight as a transaction

The filesystem can change afterward. A multi-file plan remains a sequence of individually guarded commits.

## Exercise

Extend the organizer with a **dry-run renderer** without changing execution behavior.

Requirements:

1. accept an `OrganizationPlan`;
2. return deterministic human-readable text;
3. show planned moves, skipped collisions, and ignored symlinks;
4. never access or mutate the filesystem;
5. add tests for empty and non-empty plans.

## Extension challenges

Consider:

- configurable suffix mappings;
- user-defined categories;
- JSON plan export/import with stale-plan validation;
- operation journaling;
- recursive discovery with explicit relative-path rules;
- checksum-based duplicate detection;
- richer recovery/audit tooling for preserved staging entries;
- a transactional design for a different problem domain.

Each extension introduces new invariants. Define the contract before adding code.

## Portfolio discussion

A useful explanation is not “I wrote a script that moves files.”

A stronger version is:

> I designed a filesystem workflow with deterministic planning, explicit collision policies, symlink/special-file boundaries, inode-based identity checks, descriptor-anchored directories, bounded staging names, mutation-time casefold rechecks, and an atomic Linux exact-name no-replace commit using `renameat2(RENAME_NOREPLACE)`. Failure handling preserves uncertain state instead of blindly deleting entries.

That communicates engineering decisions, not just API usage.

## Quick reference

| Task | Function/type |
|---|---|
| Classify a filename | `classify_path()` |
| Discover direct regular files | `discover_files()` |
| Build a safe proposal | `plan_organization()` |
| Choose collision behavior | `CollisionPolicy` |
| Describe one move | `MoveAction` |
| Hold the immutable plan | `OrganizationPlan` |
| Execute the plan | `execute_plan()` |
| Hold successful destinations | `OrganizationResult` |
| Identify filesystem objects | `(st_dev, st_ino)` |
| Logical casefold recheck | pinned-directory `listdir()` |
| Secure Linux exact-name commit | `renameat2(RENAME_NOREPLACE)` |

## What comes next

Project 05 generated files. Project 06 owns the next boundary: discovering and organizing files safely.

Project 07 moves upward again, combining validated domain records and explicit workflow states in a **fictional reconciliation workflow**.