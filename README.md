<div align="center">

# Python Study Guide 🐍

### Study. Understand. Practice.

<img src="assets/banner.png" alt="Python Study Guide visual identity with a geometric serpent, code braces, an open book, and connected learning nodes." width="100%">

[🇺🇸 English](README.md) · [🇧🇷 Português](docs/localized/README.pt-BR.md) · [🇪🇸 Español](docs/localized/README.es.md)

</div>

A multilingual, practical guide for studying Python, understanding how its parts connect, and applying them through clear examples.

This project is designed both as a learning path and as a quick-reference library. Instead of presenting isolated commands, each topic explains what a resource does, why it exists, when to use it, when to avoid it, and how it works with other parts of Python.

## Why is the code written in English?

Folder names, file names, variables, functions, classes, and other identifiers are written in English. This helps learners become familiar with conventions commonly found in libraries, technical documentation, and international software projects.

The explanations are available in English, Brazilian Portuguese, and Spanish.

## How to study

Each chapter follows a consistent structure:

1. What it is
2. Why it exists
3. Syntax and conventions
4. When to use it
5. When to avoid it
6. How it connects to other resources
7. Basic and practical examples
8. Common mistakes
9. Exercise
10. Review checklist
11. Quick-reference summary

## Learning roadmap

The guide grows from Python fundamentals to functions, documentation, error handling, files, the standard library, external libraries, testing, and practical projects.

- [Full learning path: direct links to every published chapter](docs/learning-path.en.md)
- [Roadmap in English](docs/roadmap.en.md)
- [Roadmap em Português](docs/roadmap.pt-BR.md)
- [Roadmap en Español](docs/roadmap.es.md)

## Project structure

```text
python-study-guide/
├── assets/
├── comments-and-documentation/
├── collections/
├── docs/
├── errors-files-and-modules/
├── exercises/
├── external-libraries/
├── functions/
├── fundamentals/
├── practical-projects/
├── program-flow/
├── scripts/
├── standard-library/
├── strings-and-numbers/
└── tests/
```

Detailed explanations:

- [Project structure in English](docs/project-structure.en.md)
- [Estrutura do projeto em Português](docs/project-structure.pt-BR.md)
- [Estructura del proyecto en Español](docs/project-structure.es.md)

## Current status

The project foundation is complete. Phase 0 established the multilingual documentation, contribution workflow, collaboration templates, community standards, authorship, licensing, AI governance, automated quality checks, original visual identity, scalable repository structure, and final foundation audit.

The project foundation and seven complete educational sections are available, and [Phase 8: Standard Library](standard-library/README.md) is now in progress with [Chapter 01: `pathlib`](standard-library/01-pathlib/README.md), [Chapter 02: `datetime`](standard-library/02-datetime/README.md), [Chapter 03: `json`](standard-library/03-json/README.md), [Chapter 04: `csv`](standard-library/04-csv/README.md), and [Chapter 05: `logging`](standard-library/05-logging/README.md). [Phase 7: Errors, Files, and Modules](errors-files-and-modules/README.md) is complete with five reviewed chapters. [Phase 1: Fundamentals](fundamentals/README.md) provides six reviewed beginner chapters. Phase 6 contains six reviewed learning chapters:

- [Comments in Python](comments-and-documentation/01-comments/README.md)
- [Docstrings in Python](comments-and-documentation/02-docstrings/README.md)
- [Meaningful Names and Self-Explanatory Code](comments-and-documentation/03-meaningful-names/README.md)
- [Task Markers and Technical Follow-up](comments-and-documentation/04-task-markers/README.md)
- [Comments versus Logging in Python](comments-and-documentation/05-comments-vs-logging/README.md)
- [PEP 8 and Readability in Python](comments-and-documentation/06-pep8-and-readability/README.md)

Phases 1, 2, 3, 4, 5, 6, and 7 are complete. Phase 8 is in progress with [Working with Filesystem Paths Using `pathlib`](standard-library/01-pathlib/README.md), [Working with Dates and Time Calculations Using `datetime`](standard-library/02-datetime/README.md), [Controlling JSON Serialization and Decoding Contracts](standard-library/03-json/README.md), [Controlling CSV Dialects and Tabular Text Contracts](standard-library/04-csv/README.md), and [Engineering Logging Pipelines and Runtime Context Contracts](standard-library/05-logging/README.md). Together they add path-aware filesystem work, explicit date/time modeling, deeper JSON contracts for deterministic output and strict decoding, deeper CSV contracts for dialects and tabular-text boundaries, and deeper logging contracts for hierarchy, configuration, contextual records, queue-based delivery, concurrency, and operational safety. Phase 7 contains five reviewed chapters: exception handling; deliberate raising and custom exceptions; safe file handling with `open()` and `with`; [Working with TXT, CSV, and JSON](errors-files-and-modules/04-txt-csv-and-json/README.md); and [Organizing Code with Imports, Modules, and Packages](errors-files-and-modules/05-imports-modules-and-packages/README.md), which closes the phase with explicit module imports, regular package structure, the main guard, import search context, absolute and relative imports, `python -m`, and dependency design. Phase 5: Functions contains nine reviewed chapters: [Defining and Calling Functions](functions/01-defining-and-calling-functions/README.md), [Parameters and Arguments](functions/02-parameters-and-arguments/README.md), [Return Values](functions/03-return-values/README.md), [Scope](functions/04-scope/README.md), [Type Hints](functions/05-type-hints/README.md), [Default Values](functions/06-default-values/README.md), [`*args` and `**kwargs`](functions/07-args-and-kwargs/README.md), [Functions Working Together](functions/08-functions-working-together/README.md), and [Data Flow Between Functions](functions/09-data-flow-between-functions/README.md). Together they establish function definition and calling, required input flow, returned results, local and global scope, typed interfaces, safe optional inputs, intentionally flexible positional and keyword argument collection, composition through helpers and coordinators, and explicit caller-to-parameter-to-return data flow including rebinding versus mutation. Phase 4 remains complete with eight reviewed Program Flow chapters, ending with [Choosing and Combining Program Flow](program-flow/08-choosing-and-combining-program-flow/README.md). Phase 3 contains six reviewed Collections chapters, ending with [Choosing the Right Collection](collections/06-choosing-the-right-collection/README.md). Phase 2 remains complete with four reviewed chapters, ending with [Numeric Built-ins](strings-and-numbers/04-numeric-builtins/README.md). See the [roadmap](docs/roadmap.en.md) or the [full learning path](docs/learning-path.en.md) for the current curriculum status and direct chapter links.

## Visual identity

The project emblem connects Python, code, learning, and relationships between concepts through a geometric serpent, braces, an open book, and connected nodes.

See the [visual identity guide](assets/README.md) for available assets, palette, meaning, accessibility guidance, and usage rules.

## AI-assisted development

This project uses AI tools, including ChatGPT and Codex, to support planning, research, drafting, translation, review, and repository maintenance.

AI output is not accepted automatically. Every change must be understood, verified, and reviewed by the maintainer before it is incorporated into the `main` branch.

Repository-wide working instructions for AI agents and contributors are recorded in [AGENTS.md](AGENTS.md). Read the [AI-assisted development guide](docs/ai-assisted-development/README.en.md) for the responsible workflow.

## Authorship and maintenance

Python Study Guide was created and is maintained by [Ramon Estevez Rodriguez](https://github.com/RamonRDR).

Community contributions remain credited through commit metadata, Git history, and pull requests. Read the [project authorship record](AUTHORS.md) for the complete attribution policy.

## Community and support

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). The [Support Guide](SUPPORT.md) explains where different questions and requests belong. Potential vulnerabilities must follow the private process in the [Security Policy](SECURITY.md).

## Contributing

Contributions, corrections, examples, and translation improvements are welcome. Read the contribution guide in [English](CONTRIBUTING.md), [Portuguese](docs/localized/CONTRIBUTING.pt-BR.md), or [Spanish](docs/localized/CONTRIBUTING.es.md) before opening a pull request.

## License

This project is available under the [MIT License](LICENSE).