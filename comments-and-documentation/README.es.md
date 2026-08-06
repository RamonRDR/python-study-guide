<div align="center">

# Comentarios, Documentación y Legibilidad

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta sección enseña cómo hacer que el código Python sea más fácil de comprender, explicar, mantener y observar. Es la sección educativa piloto completada de Python Study Guide.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Nivel | Estado |
|---|---|---|---|
| [01. Comentarios](01-comments/README.es.md) | Explicar decisiones y contextos no evidentes sin narrar el código | Principiante | Disponible |
| [02. Docstrings](02-docstrings/README.es.md) | Documentar módulos, funciones, clases y métodos | Principiante | Disponible |
| [03. Nombres significativos](03-meaningful-names/README.es.md) | Expresar intención mediante nombres claros y pequeñas abstracciones | Principiante | Disponible |
| [04. Marcadores de tareas](04-task-markers/README.es.md) | Utilizar `TODO`, `FIXME`, `NOTE` y convenciones relacionadas con responsabilidad | Principiante a intermedio | Disponible |
| [05. Comentarios frente a logging](05-comments-vs-logging/README.es.md) | Separar las explicaciones del código fuente de la observación en ejecución | Intermedio | Disponible |
| [06. PEP 8 y legibilidad](06-pep8-and-readability/README.es.md) | Aplicar orientaciones de estilo comprendiendo sus objetivos y límites | Principiante a intermedio | Disponible |

## Orientación sobre requisitos previos

- **01. Comentarios:** no tiene un requisito previo formal. La familiaridad básica con variables y condicionales ayuda, pero no es obligatoria.
- **02. Docstrings:** se recomienda una familiaridad básica con funciones. Los ejemplos de módulos, clases y métodos también pueden comprenderse conceptualmente antes de estudiar esos temas en profundidad.
- **03. Nombres significativos:** se recomienda una familiaridad básica con variables y funciones.
- **04. Marcadores de tareas:** se recomienda completar el capítulo de comentarios. La familiaridad con issues y control de versiones ayuda.
- **05. Comentarios frente a logging:** se recomienda completar el capítulo de comentarios. Los conocimientos básicos sobre ejecución de programas y excepciones serán útiles.
- **06. PEP 8 y legibilidad:** se recomienda conocer la sintaxis básica de Python y completar los capítulos de comentarios y nombres significativos.

Estudia los capítulos en orden numérico al seguir la ruta completa. Cada capítulo también puede consultarse de forma independiente después de comprender sus requisitos.

```text
01. Comentarios
        ↓
02. Docstrings
        ↓
03. Nombres significativos
        ↓
04. Marcadores de tareas
        ↓
05. Comentarios frente a logging
        ↓
06. PEP 8 y legibilidad
```

## Objetivos de la sección

Al completar esta ruta, deberías ser capaz de:

- diferenciar comentarios, docstrings, documentación, type hints y logs;
- explicar decisiones sin repetir código evidente;
- elegir nombres que revelen intención, unidades, estado y responsabilidad;
- registrar tareas técnicas con contexto suficiente para que sigan siendo útiles;
- decidir cuándo la información de ejecución pertenece al logging;
- aplicar las recomendaciones de PEP 8 con criterio, sin tratarlas como sintaxis;
- revisar código considerando claridad, exactitud, privacidad y facilidad de mantenimiento.

## Capítulo actual

Completa la ruta con [PEP 8 y Legibilidad en Python](06-pep8-and-readability/README.es.md). Todos los capítulos incluyen explicaciones multilingües, ejemplos ejecutables, ejercicio, lista de revisión y resumen de consulta rápida.

## Estructura del directorio

```text
comments-and-documentation/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-comments/
├── 02-docstrings/
├── 03-meaningful-names/
├── 04-task-markers/
├── 05-comments-vs-logging/
└── 06-pep8-and-readability/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── imports_and_names.py
        ├── readable_layout.py
        └── refactor_for_readability.py
```
