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
15. return a structured result after successful execution.

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

## Symlink and directory-anchor boundaries

The organizer does not follow direct-child symlinks.

It also rejects:

- a source directory that is itself a symlink;
- a category folder implemented as a symlink;
- a category directory that is renamed or replaced after its directory descriptor is opened.

On platforms with secure directory-descriptor support, the implementation compares the pinned category descriptor identity with the current named child of the source root before and after mutation. A detached category directory therefore cannot silently receive a file while execution reports the original planned path.

## Why preflight is not enough

A first implementation might do this:

```python
if not destination.exists():
    source.rename(destination)
```

That contains a time-of-check/time-of-use race. Another process can create the destination after the check but before the rename.

On POSIX, `rename()` is allowed to replace an existing destination. That means a supposedly safe organizer could destroy newly created destination data.

The same principle applies to source removal: checking a source inode and then calling `unlink()` leaves a small window in which another process could replace that directory entry.

## Exact no-replace mutation

The execution path uses a same-filesystem hard link as the destination mutation guard:

```text
1. verify source and category identities
2. create the destination hard link without replacement
3. verify the destination and category anchor
4. atomically rename the source entry to a unique internal staging name
5. verify that the staged entry is still the planned inode
6. remove only that internal staged name
7. verify the category anchor again before reporting success
```

`os.link()` does not replace an existing destination. The staging rename avoids deleting the public source pathname after a separate identity check: if another actor replaces the source before the atomic rename, the unexpected entry is detected and preserved instead of being blindly unlinked.

Category directory descriptors are also revalidated against the named category path. If the category is renamed or replaced during execution, the operation raises instead of reporting a destination path that no longer points to the pinned directory.

This does not turn the whole multi-file plan into a transaction. It provides narrower guarantees around no-replace destination creation, source-entry identity, and category-path anchoring.

## Execution flow

`execute_plan()` performs:

1. type validation;
2. source-directory revalidation;
3. category-path revalidation;
4. planned-source identity capture;
5. destination collision preflight;
6. creation/opening of required category folders;
7. category-anchor verification;
8. exact no-replace destination linking;
9. atomic source staging and staged-identity verification;
10. final category-anchor verification;
11. construction of `OrganizationResult`.

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
- category symlink and rename races;
- source replacement between verification and final removal;
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

### Source entry changes during commit

The source pathname is atomically staged and the staged inode is verified. An unexpected replacement is preserved and the move raises instead of deleting the replacement.

### Category directory moves after it is opened

The pinned descriptor and the currently named category path no longer match, so execution raises instead of returning a false planned destination.

## Common mistakes

### Moving while scanning

Mixing discovery and mutation makes partial failure difficult to reason about.

Prefer building a plan first.

### Using only `Path.exists()` before `rename()`

The check can become stale immediately, and POSIX rename semantics can replace the destination.

### Checking an inode immediately before `unlink()`

That still leaves a check-to-unlink race. If source identity matters, restructure the commit so the public pathname is detached atomically before removing an internal staged name.

### Assuming an open directory descriptor still has the same pathname

A descriptor remains attached to an inode even after that directory is renamed. Verify that the descriptor still matches the category child currently reachable from the planned root.

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
- a rollback strategy for partially executed plans.

Each extension introduces new invariants. Add the contract before adding the code.

## Portfolio discussion

A useful portfolio explanation is not “I wrote a script that moves files.”

A stronger explanation is:

> I designed a filesystem workflow with a non-mutating planning phase, deterministic classification, explicit collision policies, symlink boundaries, execution-time identity checks, category-path anchoring, and exact no-replace destination protection. Source removal uses an atomic staging step so a late pathname replacement is not blindly unlinked.

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
| Enforce exact no-replace mutation | `os.link()` + atomic source staging |

## What comes next

Project 05 generated files. Project 06 owns the next boundary: discovering and organizing files safely.

Project 07 will move upward again, combining validated domain records and explicit workflow states in a **fictional reconciliation workflow**.
