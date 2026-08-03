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
│   │   └── translation-improvement.yml
│   └── pull_request_template.md
├── .gitignore
├── AGENTS.md
├── AUTHORS.md
├── AUTHORS.pt-BR.md
├── AUTHORS.es.md
├── CONTRIBUTING.md
├── CONTRIBUTING.pt-BR.md
├── CONTRIBUTING.es.md
├── LICENSE
├── README.md
├── README.pt-BR.md
├── README.es.md
├── assets/
│   └── README.md
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
├── standard-library/
│   └── README.md
└── tests/
    └── README.md
```

## Guía de los archivos raíz

- `.gitignore`: evita que se versionen artefactos locales de Python y otros archivos generados.
- `AGENTS.md`: reúne las instrucciones generales del repositorio para colaboradores y agentes de IA.
- `AUTHORS...`: registra, en los tres idiomas, la autoría, el mantenimiento y el reconocimiento de las contribuciones.
- `CONTRIBUTING...`: describe el flujo de contribución y las expectativas de calidad en los tres idiomas.
- `LICENSE`: contiene la Licencia MIT aplicada al repositorio.
- `README...`: funciona como punto de entrada multilingüe del proyecto.

## Guía de directorios

- `.github/`: configuración de colaboración de GitHub. La plantilla de pull request solicita alcance, validación, alineación entre idiomas, declaración de asistencia por IA, verificaciones de privacidad y notas para la revisión. Los formularios de issue separan reportes de errores, sugerencias de contenido y mejoras de traducción, mientras que `config.yml` desactiva las issues en blanco sin estructura para colaboradores y dirige a la guía de contribución.
- `assets/`: política y futuro espacio para logotipos, banners, diagramas, capturas de pantalla e imágenes de presentación originales.
- `comments-and-documentation/`: ruta sobre comentarios, docstrings, nombres, marcadores de tareas, decisiones de logging, PEP 8 y código legible. El primer capítulo está disponible en `01-comments/`.
- `docs/`: roadmaps, arquitectura del proyecto, políticas y documentos multilingües de referencia. El directorio `ai-assisted-development/` explica el uso responsable de ChatGPT y Codex en el flujo del proyecto.
- `exercises/`: futuras actividades prácticas relacionadas con los capítulos.
- `external-libraries/`: futuras guías sobre paquetes de terceros instalados por separado.
- `functions/`: futura ruta sobre creación de funciones, parámetros, argumentos, retornos, alcance, type hints y colaboración entre funciones.
- `fundamentals/`: futura ruta sobre variables, tipos de datos, entrada, salida, strings, números, colecciones y control de flujo.
- `practical-projects/`: futuros proyectos pequeños que combinarán varios conceptos.
- `standard-library/`: futuras guías sobre módulos distribuidos con Python.
- `tests/`: pruebas automatizadas para los ejemplos ejecutables y proyectos a medida que se añadan.

## Convenciones de nombres e idiomas

Los directorios, nombres de archivos, variables, funciones, clases y demás identificadores de código usan inglés. Los documentos explicativos se ofrecen en inglés, portugués de Brasil y español.

El inglés se representa mediante el `README.md` predeterminado cuando el documento es un punto de entrada principal de GitHub. Los documentos dentro de `docs/` pueden utilizar los sufijos explícitos `.en.md`, `.pt-BR.md` y `.es.md`.

Las plantillas de colaboración de GitHub utilizan inglés como idioma predeterminado del repositorio y permiten explícitamente que los envíos se escriban en inglés, portugués de Brasil o español.

## Regla de mantenimiento

Un pull request que mueva, cree o elimine rutas importantes deberá actualizar esta estructura en el mismo cambio. Los directorios de capítulos planificados deberán añadirse solamente cuando contengan material útil, y no como placeholders vacíos.
