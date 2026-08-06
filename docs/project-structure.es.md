# Estructura del Proyecto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento describe la estructura actualmente versionada en el repositorio. Los directorios planificados no se presentan como si ya existieran.

## Mapa actual del repositorio

```text
python-study-guide/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   └── quality-checks.yml
│   └── pull_request_template.md
├── AGENTS.md
├── AUTHORS.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── assets/
├── comments-and-documentation/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-comments/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── business_rule_comments.py
│   │       ├── unnecessary_comments.py
│   │       └── useful_comments.py
│   ├── 02-docstrings/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── class_docstrings.py
│   │       ├── function_docstrings.py
│   │       └── inspect_docstrings.py
│   ├── 03-meaningful-names/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── booleans_and_units.py
│   │       ├── refactor_for_intent.py
│   │       └── vague_and_clear_names.py
│   └── 04-task-markers/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── actionable_markers.py
│           ├── scan_markers.py
│           └── temporary_workaround.py
├── docs/
│   ├── ai-assisted-development/
│   ├── localized/
│   ├── project-structure.en.md
│   ├── project-structure.pt-BR.md
│   ├── project-structure.es.md
│   ├── roadmap.en.md
│   ├── roadmap.pt-BR.md
│   └── roadmap.es.md
├── exercises/
├── external-libraries/
├── functions/
├── fundamentals/
├── practical-projects/
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
└── tests/
```

## Guía de los archivos raíz

- `AGENTS.md`: instrucciones generales del repositorio para colaboradores y agentes de IA.
- `AUTHORS.md`: registro canónico de autoría, mantenimiento y reconocimiento de contribuciones.
- `CODE_OF_CONDUCT.md`: política de conducta de la comunidad e informes privados reconocida por GitHub.
- `CONTRIBUTING.md`: flujo de contribución y expectativas de calidad.
- `LICENSE`: Licencia MIT aplicada al repositorio.
- `README.md`: punto de entrada canónico en inglés.
- `SECURITY.md`: alcance de seguridad y política de reporte privado de vulnerabilidades.
- `SUPPORT.md`: orientación sobre canales y límites del soporte.

## Guía de directorios

- `.github/`: configuración de colaboración, formularios de issue, plantilla de pull request y workflow de GitHub Actions.
- `assets/`: identidad visual original, recursos exportados, composiciones editables, paleta, accesibilidad y reglas de uso.
- `comments-and-documentation/`: ruta de la Fase 6. Hay capítulos completos sobre comentarios, docstrings, nombres significativos y marcadores de tareas, cada uno en inglés, portugués de Brasil y español, con ejemplos ejecutables seguros.
- `docs/`: roadmaps, arquitectura del proyecto, documentos localizados, políticas y guía de desarrollo responsable asistido por IA.
- `exercises/`: actividades prácticas relacionadas con los capítulos.
- `external-libraries/`: futuras guías sobre paquetes de terceros.
- `functions/`: futura ruta sobre funciones, parámetros, retornos, alcance y type hints.
- `fundamentals/`: futura ruta sobre variables, tipos, entrada, salida, textos, números, colecciones y control de flujo.
- `practical-projects/`: futuros proyectos pequeños que combinarán varios conceptos.
- `scripts/`: herramientas de mantenimiento sin dependencias externas utilizadas localmente y por GitHub Actions.
- `standard-library/`: futuras guías sobre módulos distribuidos con Python.
- `tests/`: pruebas de regresión de las herramientas de calidad y, más adelante, del contenido educativo.

## Regla de los directorios de capítulos

Cada capítulo de aprendizaje contiene:

- un `README.md` canónico en inglés;
- READMEs localizados en portugués de Brasil y español;
- un directorio `examples/` cuando los ejemplos ejecutables mejoran el tema;
- solamente material completo y revisable, sin placeholders vacíos.

## Convenciones de nombres e idiomas

Los directorios, archivos, variables, funciones, clases y demás identificadores utilizan inglés. Los documentos explicativos se ofrecen en inglés, portugués de Brasil y español.

El inglés utiliza archivos canónicos reconocidos automáticamente por GitHub. Las versiones en portugués de Brasil y español de los documentos principales se almacenan en `docs/localized/`. Los capítulos mantienen los READMEs localizados junto a la versión en inglés para facilitar la navegación.

## Regla de mantenimiento

Un pull request que mueva, cree o elimine rutas importantes debe actualizar esta estructura en el mismo cambio. Los nuevos ejemplos ejecutables también deben revisarse para ejecución automática y registrarse en `scripts/example_manifest.txt` cuando se aprueben para CI.
