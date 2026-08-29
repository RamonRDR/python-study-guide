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

The project foundation and **Phases 1–8 are complete**. **Phase 9: External Libraries is in progress** with three reviewed-track chapters: [`pandas`](external-libraries/01-pandas/README.md), targeting pandas 3.0.x, [`openpyxl`](external-libraries/02-openpyxl/README.md), targeting openpyxl 3.1.x, and [`requests`](external-libraries/03-requests/README.md), targeting Requests 2.34.x.

The phase now covers tabular-data transformation, Excel workbook automation, and HTTP/API consumption. Repository CI installs the explicit third-party contract in [`requirements-external.txt`](requirements-external.txt) before running approved examples.

The next planned Phase 9 chapter is `pytest`. See the [External Libraries index](external-libraries/README.md), [roadmap](docs/roadmap.en.md), or [full learning path](docs/learning-path.en.md) for current status.

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