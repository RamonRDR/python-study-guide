# Estructura del Proyecto

[🇺🇸 English](project-structure.en.md) · [🇧🇷 Português](project-structure.pt-BR.md) · [🇪🇸 Español](project-structure.es.md)

Este documento describe la estructura actualmente versionada en el repositorio. Los directorios planificados no se presentan como secciones educativas completadas.

## Mapa actual del repositorio

```text
python-study-guide/
├── .github/
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
├── collections/
├── docs/
├── exercises/
├── external-libraries/
├── functions/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-defining-and-calling-functions/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── define_and_call.py
│   │       ├── execution_order.py
│   │       └── repeated_calls.py
│   ├── 02-parameters-and-arguments/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   └── examples/
│   │       ├── book_details.py
│   │       ├── greet_people.py
│   │       └── score_status.py
│   └── 03-return-values/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       └── examples/
│           ├── calculate_total.py
│           ├── classify_score.py
│           └── find_first_even.py
├── fundamentals/
├── practical-projects/
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

Las secciones educativas completadas tienen sus propios índices de capítulos y directorios de ejemplos. El árbol de Funciones aparece detallado porque la Fase 5 se está desarrollando capítulo por capítulo.

## Guía de directorios

- `.github/`: configuración de colaboración y GitHub Actions.
- `assets/`: identidad visual del proyecto y orientaciones de uso.
- `comments-and-documentation/`: ruta completa de la Fase 6.
- `collections/`: ruta completa de la Fase 3.
- `docs/`: rutas de aprendizaje, roadmaps, documentación de estructura, documentos localizados y orientaciones de desarrollo responsable.
- `exercises/`: actividades prácticas enfocadas.
- `external-libraries/`: futuras guías de paquetes de terceros.
- `functions/`: Fase 5 en progreso. Los Capítulos 01–03 cubren definición y llamada de funciones, parámetros y argumentos, valores de retorno, `None`, retornos por rama y anticipados, resultados en tupla, `print()` frente a `return` y seguimiento completo de entrada y salida.
- `fundamentals/`: ruta completa de la Fase 1.
- `practical-projects/`: futuros proyectos integrados.
- `program-flow/`: ruta completa de la Fase 4.
- `scripts/`: herramientas de calidad del repositorio sin dependencias externas.
- `standard-library/`: futuras guías de la biblioteca estándar.
- `strings-and-numbers/`: ruta completa de la Fase 2.
- `tests/`: pruebas de regresión de las herramientas de calidad y, más adelante, del código educativo.

## Regla de directorios de capítulos

Cada capítulo contiene un `README.md` canónico en inglés, READMEs localizados en portugués de Brasil y español y un directorio `examples/` cuando los ejemplos ejecutables mejoran el tema.

## Convenciones de nombres e idiomas

Las rutas del repositorio y los identificadores de código utilizan inglés. Las explicaciones se ofrecen en inglés, portugués de Brasil y español.

## Regla de mantenimiento

Un pull request que cree, mueva o elimine rutas importantes debe actualizar estos documentos de estructura en el mismo cambio. Los ejemplos aprobados para ejecución automática también deben registrarse en `scripts/example_manifest.txt`.
