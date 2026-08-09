<div align="center">

# Collections

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

This section is Phase 3 of the main Python Study Guide learning sequence. It builds on strings and numbers by teaching how several related values can be organized into collections before program flow introduces repeated iteration and branching.

## Learning path

| Chapter | Main focus | Level | Status |
|---|---|---|---|
| [01. List creation, indexing, and slicing](01-list-creation-and-indexing/README.md) | Create ordered collections and read individual items and ranges | Beginner | Available |
| [02. Modifying lists and common list methods](02-modifying-lists-and-methods/README.md) | Change list contents deliberately and understand mutation | Beginner | Available |
| [03. Tuples and immutability](03-tuples-and-immutability/README.md) | Use immutable sequences and compare them with lists | Beginner | Available |
| [04. Dictionaries: keys and values](04-dictionaries-keys-and-values/README.md) | Organize values by meaningful keys instead of positions | Beginner | Available |
| 05. Sets and unique values | Work with unique items and set-style membership operations | Beginner | Planned |
| 06. Choosing the right collection | Compare lists, tuples, dictionaries, and sets by intent | Beginner | Planned |

## Why this order?

The path grows one idea at a time:

```text
one value
    ↓
ordered group of values
    ↓
changing an ordered group
    ↓
immutable ordered group
    ↓
key -> value relationships
    ↓
unique-value collections
    ↓
choose by intent
```

Lists come first because their indexing and slicing reuse the sequence model from Phase 2. Mutation is separated into a second chapter so a beginner can understand the shape of a list before learning all the ways it can change.

Tuples then make mutability versus immutability explicit. Dictionaries introduce a larger conceptual shift from numeric positions to keys. Sets come after that because they are collections whose main model is not positional indexing. The final chapter brings the four choices together.

## Prerequisite guidance

- **01. List creation, indexing, and slicing:** complete Phases 1 and 2 first. You should understand variables, common built-in types, `len()`, integer indexes, string slicing, Boolean values, and common numeric built-ins.
- **02. Modifying lists and common list methods:** complete Chapter 01 first so list mutation is learned on top of a stable sequence model.
- **03. Tuples and immutability:** complete the two list chapters first so the contrast between mutable and immutable sequences has a concrete reference point.
- **04. Dictionaries: keys and values:** complete the sequence chapters first. This chapter changes the lookup model from positions to keys.
- **05. Sets and unique values:** complete the dictionary chapter first. Sets remove positional lookup and focus on unique membership.
- **06. Choosing the right collection:** complete the previous five chapters so the comparison is based on concepts you have already practiced.

Study the chapters in numerical order when following the complete path.

## Section goals

By the end of Phase 3, you should be able to:

- create and read lists confidently;
- modify lists deliberately and recognize in-place changes;
- explain the difference between mutable lists and immutable tuples;
- store and retrieve values with dictionary keys;
- use sets when uniqueness and membership are central;
- recognize which collection types are positional and which are not;
- choose a collection according to the relationship between the values rather than syntax familiarity;
- enter Phase 4 ready to use loops and conditionals with collections you already understand.

## Scope boundary

Phase 3 focuses on collection structure and basic operations.

It intentionally does **not** teach:

- `for` or `while` loops;
- list, dictionary, or set comprehensions;
- `enumerate()` or `zip()`;
- advanced sorting callbacks;
- custom collection classes.

Those ideas become easier after the learner first understands what the collections contain and how each collection organizes its values.

## Section status

Phase 3 is **in progress**. Chapters 01 through 04 are available in English, Brazilian Portuguese, and Spanish. Chapters 05 and 06 remain planned and will be added as complete, reviewable chapters rather than empty placeholders.

## Current directory structure

```text
collections/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-list-creation-and-indexing/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── list_basics.py
│       └── list_slicing.py
├── 02-modifying-lists-and-methods/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── list_copying.py
│       ├── list_methods.py
│       └── list_mutation.py
├── 03-tuples-and-immutability/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── tuple_basics.py
│       ├── tuple_mutable_item.py
│       └── tuple_unpacking.py
└── 04-dictionaries-keys-and-values/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── dictionary_basics.py
        ├── dictionary_mutation.py
        └── dictionary_views.py
```
