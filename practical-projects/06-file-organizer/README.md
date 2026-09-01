<div align="center">

# Project 06 · File Organizer

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Practical Projects](../README.md)

> **Phase 10 · Practical Projects**

This project organizes direct child files into category folders while keeping discovery, planning, collision handling, and filesystem mutation explicit and testable.

## Learning objectives

By the end of this project, you should be able to:

- discover files with `pathlib` without recursively traversing a tree;
- classify filenames deterministically from case-insensitive suffix rules;
- model planned filesystem changes with immutable dataclasses;
- separate a non-mutating planning phase from a mutating execution phase;
- detect exact and case-insensitive destination collisions;
- choose an explicit collision policy instead of silently overwriting data;
- treat symlinks as a separate filesystem boundary;
- revalidate assumptions immediately before mutation;
- enforce exact destination no-replace behavior at the mutation step;
- verify source identity across time-of-check/time-of-use boundaries;
- preserve uncertain destination state instead of performing destructive rollback;
- test filesystem code safely with temporary directories.

## Problem

Imagine a fictional workspace containing files such as:

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

The important challenge is not merely calling a move function. The project must make destructive filesystem decisions visible before changing anything.

## Requirements

The implementation must:

1. accept an existing non-symlink source directory;
2. inspect only direct children of that directory;
3. ignore nested directories;
4. report direct-child symlinks separately instead of following them;
5. classify regular files by filename suffix;
6. preserve each filename exactly;
7. create destination folders only when needed;
8. produce deterministic ordering;
9. build an immutable plan before mutation;
10. reject invalid category paths, including symlinked category directories;
11. detect existing exact and case-insensitive destination collisions;
12. support explicit `ERROR` and `SKIP` collision policies during planning;
13. run a full preflight before any move;
14. never silently replace an exact destination that appears after preflight;
15. reject a planned source whose filesystem identity changes before commit;
16. never delete an unverified destination while handling a source-removal failure;
17. return a structured result after successful execution.

## Deliberate scope

The pipeline is:

```text
source directory
    -> direct-file discovery
    -> suffix classification
    -> collision-safe plan
    -> execution preflight
    -> required category folders
    -> identity-verified no-replace moves
```

This project intentionally does **not** include:

- recursive organization;
- MIME or content inspection;
- automatic duplicate renaming;
- hashing or deduplication;
- deletion;
- rollback transactions across the entire plan;
- filesystem watchers;
- GUI interaction;
- cloud storage;
- cross-filesystem organization.

Keeping these responsibilities out of scope makes the safety rules visible instead of burying them inside a general-purpose file manager.

## Categories

`FileCategory` defines five destinations:

| Category | Folder | Representative suffixes |
|---|---|---|
| Documents | `documents/` | `.txt`, `.md`, `.pdf`, `.docx` |
| Data | `data/` | `.csv`, `.json`, `.xml`, `.xlsx` |
| Images | `images/` | `.png`, `.jpg`, `.webp`, `.svg` |
| Archives | `archives/` | `.zip`, `.7z`, `.tar.gz`, `.tar.xz` |
| Other | `other/` | anything not matched above |

Matching is case-insensitive. Classification uses filenames only and does not open file contents.

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

The plan is immutable. Creating it does not create directories and does not move files.

### `OrganizationResult`

Records the exact planned destinations that were successfully moved.

## Discovery is intentionally shallow

`discover_files()` returns only direct regular-file children.

Nested directories are not traversed. This matters because recursive movement introduces additional questions:

- should the relative path be preserved?
- should category folders inside nested directories be revisited?
- how should duplicate names from different subdirectories be handled?

Those questions are useful, but they belong to a larger project.

## Planning before mutation

`plan_organization()` validates the directory, scans the files, classifies them, and calculates destinations without changing the filesystem.

That separation provides a useful engineering pattern:

```text
observe -> decide -> validate -> mutate
```

It is easier to test and review a proposed operation when the proposal exists as data before side effects begin.

## Collision policies

Two policies are explicit:

### `CollisionPolicy.ERROR`

Planning stops with `FileExistsError` when a destination name already exists.

Use this when every source file must have a conflict-free destination.

### `CollisionPolicy.SKIP`

Files whose destination collides are left in the source directory and listed in `skipped_collisions`.

Use this when safely organizing the non-conflicting subset is acceptable.

The policy is applied during planning. Execution still refuses new exact collisions that appear later.

## Case-insensitive collision checks

A directory may be case-sensitive on one operating system and case-insensitive on another.

The project therefore compares destination names with `casefold()` during planning and preflight. For example, these are treated as a logical collision:

```text
Report.TXT
report.txt
```

This keeps the plan portable across common filesystem behaviors.

## Symlink boundary

The organizer does not follow direct-child symlinks.

It also rejects:

- a source directory that is itself a symlink;
- a category folder implemented as a symlink.

On platforms with directory-descriptor support, execution pins the source and category directories with `O_DIRECTORY | O_NOFOLLOW` so a category path that becomes a symlink after preflight cannot redirect the mutation outside the workspace.

## Why preflight is not enough

A first implementation might do this:

```python
if not destination.exists():
    source.rename(destination)
```

That contains a time-of-check/time-of-use race. Another process can create the destination after the check but before the rename.

On POSIX, `rename()` is allowed to replace an existing destination. A planned source can also be replaced after preflight. Therefore execution must validate both destination availability and source identity at the mutation boundary.

## Exact no-replace mutation

The execution path uses a same-filesystem hard-link operation as its destination guard:

```text
1. capture source identity during preflight
2. revalidate that the source is still the same regular file
3. create the destination hard link without replacement
4. verify that the destination references the expected source identity
5. revalidate the source identity again
6. remove the original source path
```

Filesystem identity is represented by the `(device, inode)` pair returned by `stat`. This lets execution distinguish “the same filename” from “the same filesystem object.” A late symlink or regular-file replacement therefore aborts execution instead of being reported as a successful move.

`os.link()` does not replace an existing destination. Because every destination folder is inside the same source directory, source and destination are intentionally on the same filesystem for this project.

If creating the link fails, the source remains untouched. If removing the source fails after the destination has been created, the implementation deliberately **keeps the destination** and raises an error. It does not attempt an unconditional rollback unlink, because another process could have replaced that directory entry in the meantime. Preserving uncertain state is safer than deleting an object whose identity can no longer be proven.

This does not turn the whole multi-file plan into a transaction. It provides narrower guarantees: exact destinations are not silently overwritten, planned sources are revalidated by identity, and failure handling does not intentionally delete an unverified destination.

## Execution flow

`execute_plan()` performs:

1. type validation;
2. source-directory revalidation;
3. category-path revalidation;
4. capture of planned-source filesystem identities;
5. destination collision preflight;
6. creation/opening of only required category folders;
7. identity-verified exact no-replace moves;
8. construction of `OrganizationResult`.

A stale plan is therefore not trusted blindly.

## Determinism

Files and actions are sorted by a key based on:

```python
(path.name.casefold(), path.name)
```

This makes examples, tests, and review output stable instead of depending on filesystem iteration order.

## Running the demo

From the repository root:

```bash
python practical-projects/06-file-organizer/demo.py
```

The demo uses `TemporaryDirectory`, creates only fictional files, prints the planned moves, executes them, and shows the final workspace layout. It does not touch personal directories.

## Running the tests

Focused suite:

```bash
python -m pytest practical-projects/06-file-organizer/tests -q
```

The focused suite intentionally avoids embedding a fixed scenario count in this chapter because regression coverage grows as review findings are hardened.

Coverage includes:

- suffix classification;
- path validation;
- deterministic discovery;
- shallow scanning;
- symlink handling;
- immutable model invariants;
- exact and case-insensitive collisions;
- `ERROR` and `SKIP` policies;
- stale/missing sources;
- category-path changes;
- collision preflight;
- a destination created between preflight and mutation;
- a category path becoming a symlink during mutation;
- a planned source becoming a symlink during mutation;
- source-removal failure without destructive destination rollback;
- successful execution;
- preservation of unrelated destination files;
- empty plans.

## Failure paths worth studying

### Missing source directory

Raises `FileNotFoundError`.

### Source path is a regular file

Raises `NotADirectoryError`.

### Source directory is a symlink

Rejected before scanning.

### Category path is a file or symlink

Rejected before planning or execution.

### Destination exists during planning

Handled according to the selected collision policy.

### Destination appears after planning

Preflight raises `FileExistsError` before any move.

### Exact destination appears after preflight

The no-replace hard-link operation fails with `FileExistsError`; the newly created destination is preserved and the source remains in place.

### Planned source identity changes during execution

Execution raises instead of unlinking the changed source entry or reporting the move as successful.

### Source removal fails after destination creation

Execution raises and retains the destination. It deliberately avoids deleting a destination whose current identity cannot be proven safely during rollback.

## Common mistakes

### Moving while scanning

Mixing discovery and mutation makes partial failure difficult to reason about.

Prefer building a plan first.

### Using only `Path.exists()` before `rename()`

The check can become stale immediately, and POSIX rename semantics can replace the destination.

### Treating a filename as object identity

A directory entry can be replaced while keeping the same name. When concurrency matters, compare filesystem identity and file type at the mutation boundary.

### Rolling back by blindly deleting the destination

A rollback path is still a mutation path. If another actor can replace the destination entry, unconditional deletion can destroy unrelated data.

### Silently inventing new filenames

Renaming collisions to values such as `report_2.txt` hides a policy decision. This project keeps collision behavior explicit.

### Following symlinks accidentally

A friendly-looking path can point outside the intended workspace.

### Assuming directory iteration order

Filesystem iteration order is not an application-level ordering contract. Sort explicitly when deterministic behavior matters.

### Treating a successful preflight as a transaction

The filesystem can change after preflight. Revalidation narrows risk but does not make a multi-file operation transactional.

## Exercise

Extend the organizer with a **dry-run renderer** without changing execution behavior.

Requirements:

1. accept an `OrganizationPlan`;
2. return deterministic human-readable text;
3. show planned moves, skipped collisions, and ignored symlinks;
4. never access or mutate the filesystem;
5. add tests for empty and non-empty plans.

The purpose is to practice keeping presentation separate from domain and mutation logic.

## Extension challenges

After completing the exercise, consider:

- a configurable suffix-to-category mapping;
- a user-defined category enum alternative;
- a JSON plan export/import format with careful stale-plan validation;
- an operation journal;
- recursive discovery with explicit relative-path rules;
- checksum-based duplicate detection;
- a stronger platform-specific conditional source-removal primitive;
- a rollback strategy for partially executed plans.

Each extension introduces new invariants. Add the contract before adding the code.

## Portfolio discussion

A useful portfolio explanation is not “I wrote a script that moves files.”

A stronger explanation is:

> I designed a filesystem workflow with a non-mutating planning phase, deterministic classification, explicit collision policies, symlink boundaries, execution-time identity validation, exact no-replace destination protection, and conservative failure handling that never blindly deletes an unverified rollback target.

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
| Verify filesystem identity | `(st_dev, st_ino)` from `stat` |
| Enforce exact no-replace mutation | `os.link()` + verified source `unlink()` |

## What comes next

Project 05 generated files. Project 06 owns the next boundary: discovering and organizing files safely.

Project 07 will move upward again, combining validated domain records and explicit workflow states in a **fictional reconciliation workflow**.
