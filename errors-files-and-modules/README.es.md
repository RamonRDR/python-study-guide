<div align="center">

# Errores, Archivos y Módulos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta sección inicia la transición desde pequeños programas que trabajan solo en memoria hacia programas que deben afrontar fallos, datos persistentes y código organizado en varios archivos.

La Fase 7 comienza con el manejo de excepciones, continúa con la generación deliberada de excepciones, trabaja de forma segura con archivos y datos de texto estructurados y termina organizando código Python con imports, módulos y paquetes.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Nivel | Estado |
|---|---|---|---|
| [01. `try`, `except`, `else` y `finally`](01-try-except-else-finally/README.es.md) | Manejar fallos esperados en runtime manteniendo explícitas las rutas normal y de limpieza | Principiante a intermedio | Disponible |
| [02. Lanzar Excepciones y Excepciones Personalizadas](02-raise-and-custom-exceptions/README.es.md) | Señalar estados inválidos deliberadamente con `raise`, volver a lanzar o encadenar fallos de forma intencional e introducir excepciones personalizadas simples | Intermedio | Disponible |
| [03. `open()` y `with`](03-open-and-with/README.es.md) | Abrir, leer, escribir y añadir a archivos de texto gestionando recursos de forma segura con `with` | Principiante a intermedio | Disponible |
| [04. TXT, CSV y JSON](04-txt-csv-and-json/README.es.md) | Analizar, escribir, convertir y validar formatos comunes de datos textuales con herramientas específicas del formato | Intermedio | Disponible |
| [05. Imports, Módulos y Paquetes](05-imports-modules-and-packages/README.es.md) | Dividir código en archivos reutilizables, organizar paquetes regulares y comprender el contexto de importación y ejecución de Python | Intermedio | Disponible |

## Orientación de prerrequisitos

Antes de comenzar esta fase, conviene estar cómodo con:

- condiciones y lógica booleana;
- bucles;
- funciones, parámetros y valores retornados;
- conversión básica de tipos;
- lectura conceptual de tracebacks simples;
- la diferencia entre comentarios del código fuente y comportamiento en runtime.

La ruta completa para principiantes de las Fases 1–6 proporciona todas estas bases.

## Secuencia recomendada

Al seguir el currículo completo, estudia los capítulos en orden numérico:

```text
01. Manejar excepciones
        ↓
02. Lanzar excepciones deliberadamente
        ↓
03. Abrir y gestionar archivos
        ↓
04. Leer y escribir formatos comunes de datos
        ↓
05. Organizar código con módulos y paquetes
```

La secuencia es intencional. Antes de que un programa empiece a depender de archivos y varios módulos, debe tener un modelo claro de lo que ocurre cuando una operación no puede terminar normalmente.

## Objetivos de la sección

Al final de la Fase 7, deberías poder:

- distinguir el flujo de control normal del flujo provocado por excepciones;
- manejar excepciones específicas de runtime sin ocultar fallos no relacionados;
- usar `else` y `finally` deliberadamente;
- lanzar excepciones apropiadas cuando una función no puede cumplir su contrato;
- abrir, leer y escribir archivos usando patrones seguros de gestión de recursos;
- trabajar con texto simple, CSV y JSON a nivel introductorio;
- separar responsabilidades de parsing, validación, transformación y persistencia;
- importar código desde módulos y paquetes;
- explicar cómo archivos, excepciones, funciones y módulos se conectan en un pequeño programa real.

## Estado de la fase

La Fase 7 está completada. Termina la sección con [Organizar Código con Imports, Módulos y Paquetes](05-imports-modules-and-packages/README.es.md).

Los Capítulos 01–02 establecen manejo y señalización deliberada de excepciones. El Capítulo 03 añade un tiempo de vida seguro de archivos e I/O de texto. El Capítulo 04 añade límites de datos TXT, CSV y JSON. El Capítulo 05 cierra la fase con imports explícitos, módulos, paquetes regulares, `__name__`, main guard, contexto de búsqueda, imports relativos, `python -m` y diseño de dependencias.

## Estructura del directorio

```text
errors-files-and-modules/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-try-except-else-finally/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── parse_integer.py
│       ├── safe_divide.py
│       └── trace_try_else_finally.py
├── 02-raise-and-custom-exceptions/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── custom_exception.py
│       ├── exception_chaining.py
│       └── validate_score.py
├── 03-open-and-with/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── append_text.py
│       ├── handle_missing_file.py
│       └── write_and_read_text.py
├── 04-txt-csv-and-json/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── csv_records.py
│       ├── handle_invalid_json.py
│       ├── json_document.py
│       └── text_records.py
└── 05-imports-modules-and-packages/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── grade_tools.py
        ├── import_standard_library.py
        ├── main_guard.py
        ├── module_demo.py
        ├── package_demo.py
        └── study_tools/
            ├── __init__.py
            └── formatting.py
```

Los cinco directorios planificados de la Fase 7 ya están publicados.
