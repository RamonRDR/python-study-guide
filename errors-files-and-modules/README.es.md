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
| 04. TXT, CSV y JSON | Trabajar con formatos comunes de datos basados en texto y sus límites | Intermedio | Planificado |
| 05. Imports, Módulos y Paquetes | Dividir código en archivos reutilizables y comprender el modelo de importación de Python | Intermedio | Planificado |

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

## Capítulo actual

Continúa con [Abrir Archivos de Forma Segura con `open()` y `with`](03-open-and-with/README.es.md).

Los Capítulos 01–02 establecen manejo y señalización deliberada de excepciones. El Capítulo 03 añade apertura de archivos de texto, encoding explícito, modos de archivo, lectura, escritura, append, errores de archivo específicos y limpieza gestionada por contexto. El próximo capítulo planificado es **TXT, CSV y JSON**.

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
└── 03-open-and-with/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── append_text.py
        ├── handle_missing_file.py
        └── write_and_read_text.py
```

Los directorios de capítulos planificados se añaden únicamente cuando su contenido se publica realmente.
