# Estructura del Proyecto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento describe la estructura actualmente versionada en el repositorio. Los directorios planificados no se muestran como si ya existieran.

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
├── requirements-external.txt
├── SECURITY.md
├── SUPPORT.md
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
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-expense-tracker/
│   ├── 02-grade-calculator/
│   ├── 03-user-registration/
│   ├── 04-csv-analyzer/
│   ├── 05-report-generator/
│   └── 06-file-organizer/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       ├── demo.py
│       ├── file_organizer.py
│       └── tests/
│           ├── conftest.py
│           ├── test_atomic_move.py
│           └── test_file_organizer.py
├── program-flow/
├── scripts/
│   ├── check_internal_links.py
│   ├── example_manifest.txt
│   ├── run_examples.py
│   └── validate_repository_structure.py
├── standard-library/
├── strings-and-numbers/
└── tests/
```

El mapa anterior resume las rutas de primer nivel y expande el área de la Fase 10 que cambia en este pull request. Los capítulos internos de las fases anteriores permanecen documentados por sus índices de sección y rutas de aprendizaje.

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
- `comments-and-documentation/`: ruta completa de la Fase 6, con capítulos revisados en inglés, portugués de Brasil y español y ejemplos ejecutables seguros.
- `collections/`: ruta completa de la Fase 3 sobre listas, tuplas, diccionarios, conjuntos y elección de colecciones.
- `docs/`: rutas completas de aprendizaje, roadmaps, estructura del proyecto, documentos localizados, políticas y guía de desarrollo responsable asistido por IA.
- `errors-files-and-modules/`: ruta completa de la Fase 7 sobre excepciones, archivos, formatos TXT/CSV/JSON, imports, módulos y paquetes.
- `exercises/`: actividades prácticas relacionadas con los capítulos.
- `external-libraries/`: ruta completa de la Fase 9 para pandas, openpyxl, Requests y pytest, con ejemplos deterministas y contrato explícito de dependencias.
- `functions/`: ruta completa de la Fase 5 sobre definición, parámetros, retornos, alcance, type hints, defaults, `*args`, `**kwargs`, composición y flujo de datos.
- `fundamentals/`: ruta completa de la Fase 1 sobre ejecución, entrada/salida, variables, tipos e conversión.
- `practical-projects/`: espacio de la Fase 10. Los Proyectos 01–05 están completados y el Proyecto 06 Organizador de Archivos está en progreso. El Proyecto 06 añade descubrimiento superficial determinista, planificación inmutable, políticas de colisión, fronteras de symlink, identidad `(device, inode)`, directorios raíz/categoría anclados, nombres de staging acotados, commit atómico no-replace en Linux con `renameat2(RENAME_NOREPLACE)`, demo determinista y pruebas de regresión enfocadas.
- `program-flow/`: ruta completa de la Fase 4 sobre condiciones, branching, pattern matching, loops y herramientas de iteración.
- `scripts/`: herramientas de mantenimiento sin dependencias externas utilizadas localmente y por GitHub Actions.
- `standard-library/`: ruta completa de la Fase 8 sobre `pathlib`, `datetime`, JSON, CSV, logging, collections, itertools, decimal y `os`/`shutil`.
- `strings-and-numbers/`: ruta completa de la Fase 2 sobre strings, números, booleanos, precisión y funciones numéricas incorporadas.
- `tests/`: pruebas de regresión de las herramientas de calidad y del contenido educativo cuando corresponda.

## Regla de los directorios de capítulos

Cada capítulo de aprendizaje contiene:

- un `README.md` canónico en inglés;
- READMEs localizados en portugués de Brasil y español;
- un directorio `examples/` cuando los ejemplos ejecutables mejoran el tema;
- solamente material completo y revisable, sin placeholders vacíos.

Los proyectos prácticos pueden añadir módulos de implementación, `demo.py` y una carpeta `tests/` cuando el proyecto necesita una superficie ejecutable y cobertura automatizada propia.

## Convenciones de nombres e idiomas

Los directorios, archivos, variables, funciones, clases y demás identificadores utilizan inglés. Los documentos explicativos se ofrecen en inglés, portugués de Brasil y español.

El inglés utiliza archivos canónicos reconocidos automáticamente por GitHub. Las versiones en portugués de Brasil y español de los documentos principales se almacenan en `docs/localized/`. Los capítulos mantienen los READMEs localizados junto a la versión en inglés para facilitar la navegación.

## Regla de mantenimiento

Un pull request que mueva, cree o elimine rutas importantes debe actualizar esta estructura en el mismo cambio. Los nuevos ejemplos ejecutables también deben revisarse para ejecución automática y registrarse en `scripts/example_manifest.txt` cuando se aprueben para CI.
