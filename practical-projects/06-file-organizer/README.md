<div align="center">

# File Organizer

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to Practical Projects](../README.md)

Project 06 turns filesystem concepts from Phase 8 into a small but deliberate organization workflow. The goal is not to build a desktop file manager. The goal is to practice discovery, classification, planning, collision handling, symlink boundaries, and safe mutation as separate engineering concerns.

## What you will practice

By the end of this project, you should be able to:

- discover direct regular-file children with `pathlib`;
- classify files by normalized suffix rules;
- model planned filesystem operations as immutable data;
- separate observation and planning from mutation;
- handle exact and case-insensitive destination collisions explicitly;
- ignore or reject symlinks at trust boundaries;
- revalidate a plan immediately before execution;
- prevent exact destination replacement during the mutation itself;
- pin POSIX source/category directories with no-follow directory descriptors so late symlinks cannot redirect moves;
- test filesystem race conditions with `pytest`, `tmp_path`, and monkeypatching;
- run a deterministic file workflow without touching personal directories.

## Project files

```text
06-file-organizer/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── demo.py
├── file_organizer.py
└── tests/
    ├── conftest.py
    ├── test_atomic_move.py
    └── test_file_organizer.py
```

## Requirements

The organizer must:

1. accept one source directory;
2. inspect only direct children;
3. classify regular files into explicit categories;
4. preserve original filenames;
5. build an immutable organization plan before changing the filesystem;
6. detect destination collisions case-insensitively during planning;
7. support explicit `ERROR` and `SKIP` collision policies;
8. reject source/category directory symlinks at validation boundaries;
9. ignore direct-child file symlinks instead of following them;
10. revalidate planned sources and destinations before mutation;
11. create only category directories actually required by the plan;
12. never replace an exact destination that appears after planning;
13. prevent late category symlinks from redirecting POSIX mutations outside the workspace;
14. return an immutable execution result;
15. remain deterministic for the same directory state.

## Workflow

```text
source directory
    -> direct-file discovery
    -> suffix classification
    -> collision-safe plan
    -> execution preflight
    -> required category folders
    -> no-follow directory pinning when supported
    -> no-replace moves
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

On platforms that support secure directory file descriptors, execution goes further: the source directory and each required category directory are opened with `O_DIRECTORY | O_NOFOLLOW`, and mutation happens relative to those pinned descriptors. A category path that becomes a symlink after preflight is therefore rejected before use, while a path changed after the real directory is opened cannot redirect the move through that symlink.

On platforms without those descriptor primitives, the portable fallback rechecks the category path immediately after creation and before each move. The POSIX descriptor path provides the stronger race-resistant boundary demonstrated by the dedicated regression test.

## Why preflight is not enough

A first implementation might do this:

```python
if not destination.exists():
    source.rename(destination)
```

That contains a time-of-check/time-of-use race. Another process can create the destination after the check but before the rename.

On POSIX, `rename()` is allowed to replace an existing destination. That means a supposedly safe organizer could destroy newly created destination data.

A similar race exists for category directories: a real directory can be absent during preflight and a symlink can appear before mutation. Checking the path again is useful, but on POSIX the stronger defense is to open the intended directory without following symlinks and perform the mutation through that descriptor.

## Exact no-replace mutation

The execution path therefore uses a same-filesystem hard-link operation as its mutation guard:

```text
1. create destination hard link
2. fail atomically if that exact destination already exists
3. remove the original source path
```

`os.link()` does not replace an existing destination. Because every destination folder is inside the same source directory, source and destination are intentionally on the same filesystem for this project.

When directory-descriptor support is available, the link uses `src_dir_fd` and `dst_dir_fd`, with `follow_symlinks=False`, so the operation is anchored to pinned source/category directories instead of resolving a late category symlink through a pathname.

If the link cannot be created, the source remains untouched. If removing the source fails after the link was created, the implementation attempts to remove the destination link before propagating the failure.

This does not turn the whole multi-file plan into a transaction. It solves narrower and important guarantees: an exact destination is never silently overwritten by the mutation primitive, and a late POSIX category symlink cannot redirect the move outside the planned workspace.

## Execution flow

`execute_plan()` performs:

1. type validation;
2. source-directory revalidation;
3. category-path revalidation;
4. planned-source revalidation;
5. destination collision preflight;
6. creation/opening of only required category folders;
7. no-follow directory pinning on supported platforms;
8. each exact no-replace move;
9. construction of `OrganizationResult`.

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

The current focused suite contains **58 pytest scenarios**.

Coverage includes:

- suffix classification;
- compound archive suffixes;
- invalid path-like inputs;
- shallow deterministic discovery;
- source-directory validation;
- symlink discovery behavior;
- immutable model invariants;
- exact and casefold collisions;
- both collision policies;
- empty plans;
- stale/missing sources;
- category path replacement;
- destination creation after planning;
- exact destination creation between preflight and mutation;
- category symlink creation between preflight and mutation;
- successful moves;
- preservation of unrelated existing files.

## Failure paths worth understanding

### Missing source directory

Fails before planning.

### Source directory is a file

Fails with `NotADirectoryError`.

### Category path is a regular file

Planning/execution refuses to treat it as a folder.

### Category path is a symlink

The organizer rejects it. On POSIX-capable execution, a symlink introduced after preflight is also blocked by no-follow directory opening.

### Destination already exists

`ERROR` stops planning; `SKIP` records the source without moving it.

### Destination appears after planning

Preflight refuses the stale plan.

### Destination appears after preflight

The no-replace hard-link operation raises instead of overwriting the late destination.

### Category symlink appears after preflight

The POSIX secure path refuses to open the category with `O_NOFOLLOW`, so the source remains in place and the external symlink target is not written.

### Planned source disappears or becomes a symlink

Execution refuses the plan before normal mutation begins.

## Common mistakes

### Moving files while discovering them

This mixes observation and mutation, making partial failure harder to reason about.

Prefer building a plan first.

### Using only `destination.exists()` before `rename()`

That check cannot prevent a destination from appearing immediately afterward.

Use a mutation primitive that itself refuses replacement.

### Trusting a category pathname after preflight

A late symlink can change what that pathname means.

On POSIX-capable systems, open the intended directory with no-follow semantics and perform mutations relative to the pinned descriptor.

### Automatically renaming duplicates

A suffix like `(1)` may look convenient, but it silently changes identity and belongs to a separate policy.

Keep the collision policy explicit.

### Following symlinks by accident

Filesystem helpers often follow symlinks unless you deliberately define a boundary.

Decide whether links are data, aliases, or forbidden paths before mutation.

## Exercise

Extend the planning layer with a new category named `CODE` for `.py`, `.js`, `.ts`, and `.sql` files.

Requirements:

1. add the enum member;
2. update classification rules;
3. preserve deterministic ordering;
4. add focused tests;
5. do not change collision or symlink behavior.

Then explain why classification belongs before execution rather than inside the move loop.

## Extension challenges

After the base contract is clear, try one at a time:

- a dry-run renderer that prints the plan without executing it;
- user-supplied extension/category mappings with validation;
- a result summary grouped by category;
- explicit rollback for earlier moves when a later move fails;
- a platform capability report explaining which no-follow protections are available;
- an opt-in recursive planner with preserved relative paths.

Each extension introduces a new responsibility. Keep it explicit rather than silently changing the current contract.

## Portfolio discussion

This project is useful in a portfolio because the interesting part is not the five destination folders. It is the safety reasoning around side effects.

You can discuss:

- why planning is separated from execution;
- why collisions are policies instead of accidental behavior;
- why casefold checks improve portability;
- why symlinks define a trust boundary;
- why preflight alone cannot close a TOCTOU race;
- why `rename()` was replaced with a no-replace hard-link strategy;
- why POSIX directory descriptors and `O_NOFOLLOW` close the late-category-symlink redirect found during review;
- why the project stays intentionally shallow and same-filesystem;
- how tests simulate filesystem changes between planning, preflight, and mutation.

Those are engineering decisions, not merely syntax demonstrations.

## Quick reference

```python
from file_organizer import (
    CollisionPolicy,
    FileCategory,
    classify_path,
    discover_files,
    execute_plan,
    plan_organization,
)

category = classify_path("report.PDF")
files = discover_files("workspace")
plan = plan_organization("workspace", collision_policy=CollisionPolicy.ERROR)
result = execute_plan(plan)
```

The central lesson is simple: **filesystem automation should make its plan and safety boundaries explicit before it mutates anything.**
