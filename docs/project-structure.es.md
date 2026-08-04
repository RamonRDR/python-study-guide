# Estructura del Proyecto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento describe la estructura actualmente versionada en el repositorio. Los directorios planificados no se presentan como si ya existieran.

## Mapa actual del repositorio

```text
python-study-guide/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.yml
│   │   ├── config.yml
│   │   ├── content-suggestion.yml
│   │   ├── learning-question.yml
│   │   ├── private-contact-request.yml
│   │   └── translation-improvement.yml
│   ├── workflows/
│   │   └── quality-checks.yml
│   └── pull_request_template.md
├── .gitignore
├── AGENTS.md
├── AUTHORS.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── assets/
│   ├── README.md
│   ├── banner.png
│   ├── banner.svg
│   ├── logo-mark.png
│   ├── logo.png
│   ├── repository-preview.png
│   └── repository-preview.svg
├── comments-and-documentation/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── 01-comments/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── business_rule_comments.py
│           ├── unnecessary_comments.py
│           └── useful_comments.py
├── docs/
│   ├── ai-assisted-development/
│   │   ├── README.en.md
│   │   ├── README.pt-BR.md
│   │   └── README.es.md
│   ├── localized/
│   │   ├── AUTHORS.pt-BR.md
│   │   ├── AUTHORS.es.md
│   │   ├── CODE_OF_CONDUCT.pt-BR.md
│   │   ├── CODE_OF_CONDUCT.es.md
│   │   ├── CONTRIBUTING.pt-BR.md
│   │   ├── CONTRIBUTING.es.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── SECURITY.pt-BR.md
│   │   ├── SECURITY.es.md
│   │   ├── SUPPORT.pt-BR.md
│   │   └── SUPPORT.es.md
│   ├── project-structure.en.md
│   ├── project-structure.pt-BR.md
│   ├── project-structure.es.md
│   ├── roadmap.en.md
│   ├── roadmap.pt-BR.md
│   └── roadmap.es.md
├── exercises/
│   └── README.md
├── external-libraries/
│   └── README.md
├── functions/
│   └── README.md
├── fundamentals/
│   └── README.md
├── practical-projects/
│   └── README.md
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
│   └── README.md
└── tests/
    ├── README.md
    └── test_check_internal_links.py
```

## Guía de los archivos raíz

- `.gitignore`: evita que se versionen artefactos locales de Python y otros archivos generados.
- `AGENTS.md`: reúne instrucciones generales del repositorio para colaboradores y agentes de IA.
- `AUTHORS.md`: registro canónico en inglés sobre autoría, mantenimiento y reconocimiento de contribuciones.
- `CODE_OF_CONDUCT.md`: política canónica en inglés sobre conducta e informes privados, reconocida por GitHub.
- `CONTRIBUTING.md`: flujo canónico en inglés para contribuciones y expectativas de calidad, reconocido por GitHub.
- `LICENSE`: contiene la Licencia MIT aplicada al repositorio.
- `README.md`: punto de entrada canónico en inglés reconocido por GitHub.
- `SECURITY.md`: política canónica en inglés sobre seguridad e informes privados de vulnerabilidades, reconocida por GitHub.
- `SUPPORT.md`: orientación canónica en inglés sobre canales y límites del soporte del proyecto.

## Guía de directorios

- `.github/`: configuración de colaboración y automatización de GitHub. La plantilla de pull request solicita alcance, validación, alineación entre idiomas, declaración de asistencia por IA, verificaciones de privacidad y notas para la revisión. Los formularios de issue separan reportes de errores, sugerencias de contenido, preguntas de aprendizaje, mejoras de traducción y solicitudes seguras de un canal privado. `config.yml` desactiva las issues en blanco sin estructura y dirige a las orientaciones de contribución, seguridad y conducta. El workflow `quality-checks.yml` compila archivos Python, ejecuta pruebas de regresión de las herramientas de calidad y ejemplos aprobados, verifica rutas internas en Markdown y valida la estructura del repositorio en pull requests y envíos a `main`.
- `assets/`: identidad visual original del proyecto, con archivos PNG finales para el banner, logotipo principal transparente, símbolo compacto y vista previa del repositorio. El directorio también contiene composiciones SVG editables que incorporan arte raster y, por ello, no son infinitamente escalables, además de la documentación de la paleta, significados, orientaciones de accesibilidad y reglas de uso.
- `comments-and-documentation/`: ruta sobre comentarios, docstrings, nombres, marcadores de tareas, decisiones de logging, PEP 8 y código legible. El primer capítulo está disponible en `01-comments/`.
- `docs/`: roadmaps, arquitectura del proyecto, políticas y documentos multilingües de referencia. El directorio `ai-assisted-development/` explica el uso responsable de ChatGPT y Codex en el flujo del proyecto. El directorio `localized/` contiene las versiones en portugués de Brasil y español de los documentos principales del proyecto, autoría, contribución, conducta, seguridad y soporte. Mantener solamente los archivos canónicos en inglés en la raíz evita una detección ambigua de las pestañas automáticas de GitHub sin reducir la navegación multilingüe.
- `exercises/`: futuras actividades prácticas relacionadas con los capítulos.
- `external-libraries/`: futuras guías sobre paquetes de terceros instalados por separado.
- `functions/`: futura ruta sobre creación de funciones, parámetros, argumentos, retornos, alcance, type hints y colaboración entre funciones.
- `fundamentals/`: futura ruta sobre variables, tipos de datos, entrada, salida, strings, números, colecciones y control de flujo.
- `practical-projects/`: futuros proyectos pequeños que combinarán varios conceptos.
- `scripts/`: herramientas de mantenimiento sin dependencias externas, utilizadas localmente y por GitHub Actions para ejecutar ejemplos aprobados, verificar enlaces internos y validar la estructura del repositorio.
- `standard-library/`: futuras guías sobre módulos distribuidos con Python.
- `tests/`: pruebas de regresión de las herramientas de calidad del repositorio y, más adelante, pruebas automatizadas de los ejemplos educativos y proyectos prácticos.

## Convenciones de nombres e idiomas

Los directorios, nombres de archivos, variables, funciones, clases y demás identificadores de código usan inglés. Los documentos explicativos se ofrecen en inglés, portugués de Brasil y español.

El inglés utiliza los archivos canónicos de la raíz reconocidos automáticamente por GitHub. Las versiones en portugués de Brasil y español de esos documentos se almacenan en `docs/localized/`. Las secciones de aprendizaje pueden mantener sus READMEs traducidos junto al capítulo en inglés cuando eso mejore la navegación.

## Regla de mantenimiento

Un pull request que mueva, cree o elimine rutas importantes deberá actualizar esta estructura en el mismo cambio. Los directorios de capítulos planificados deberán añadirse solamente cuando contengan material útil, y no como placeholders vacíos.
