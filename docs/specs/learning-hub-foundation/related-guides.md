# Related guide integration register

[🇺🇸 English](related-guides.md) · [🇧🇷 Português](related-guides.pt-BR.md) · [🇪🇸 Español](related-guides.es.md)

Status: planned, not published. The maintainer approved independent, reciprocal guides. Python Study Guide owns Python-specific onboarding and workflow examples; the future Git Study Guide owns language-neutral Git, GitHub/GitLab and CI/CD depth. No external guide is required to complete Python. The proposed repository slug is `git-study-guide`; do not publish a URL until the repository and the target lesson exist.

| Python-side source | Future Git-side topic | State |
| --- | --- | --- |
| `README.md` | Guide introduction | Pending publication |
| `getting-started/README.md` | Git installation and basic workflow | Pending publication |
| `getting-started/04-virtual-environments/README.md` | Ignore rules and generated environments | Pending publication |
| `getting-started/05-packages-and-dependencies/README.md` | Dependency files and reproducibility | Pending publication |
| `getting-started/06-git-and-version-control/README.md` | Git fundamentals, remotes, safe recovery | Pending publication |
| Future Sprint 04 location | Professional branch/PR/test/review workflow | Pending publication |
| `CONTRIBUTING.md` | Contributor workflow | Pending publication |
| `docs/ai-assisted-development/README.en.md` | AI-assisted review and CI | Pending publication |
| `docs/roadmap.en.md` | Cross-guide roadmap | Pending publication |
| Future consumer contract | Independent manifest and related-guide navigation | Pending publication |

When the Git guide is published, inspect actual paths and locale selectors before adding links. Update EN/PT-BR/ES together in a focused PR in each repository, point each source to the matching language, verify destinations and reciprocal links, run CI and request review. Keep the Python lesson self-contained. Record commit/tag evidence of the published targets. For Sprint 08, consider optional related-guide metadata only after the independent schemas are available; do not change the existing schema or runtime contract prematurely.
