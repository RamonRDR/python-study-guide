<div align="center">

# Comentarios, Documentación y Legibilidad

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta sección enseña cómo hacer que el código Python sea más fácil de comprender, explicar, mantener y observar. La secuencia comienza con comentarios y continúa con docstrings, nombres, marcadores de tareas, decisiones sobre logging y legibilidad según PEP 8.

## Ruta de aprendizaje

| Capítulo | Enfoque principal | Nivel | Estado |
|---|---|---|---|
| [01. Comentarios](01-comments/README.es.md) | Explicar decisiones y contextos no evidentes sin narrar el código | Principiante | Disponible |
| [02. Docstrings](02-docstrings/README.es.md) | Documentar módulos, funciones, clases y métodos | Principiante | Disponible |
| [03. Nombres significativos](03-meaningful-names/README.es.md) | Hacer que el código exprese intención mediante nombres claros y pequeñas abstracciones | Principiante | Disponible |
| [04. Marcadores de tareas](04-task-markers/README.es.md) | Utilizar `TODO`, `FIXME`, `NOTE` y convenciones relacionadas con responsabilidad | Principiante a intermedio | Disponible |
| 05. Comentarios frente a logging | Separar las explicaciones del código fuente de la observación durante la ejecución | Intermedio | Planificado |
| 06. PEP 8 y legibilidad | Aplicar orientaciones de estilo comprendiendo sus objetivos y límites | Principiante a intermedio | Planificado |

## Orientación sobre requisitos previos

- **01. Comentarios:** no tiene un requisito previo formal. La familiaridad básica con variables y condicionales ayuda, pero no es obligatoria.
- **02. Docstrings:** se recomienda una familiaridad básica con funciones. Los ejemplos de módulos, clases y métodos también pueden comprenderse conceptualmente antes de estudiar esos temas en profundidad.
- **03. Nombres significativos:** se recomienda una familiaridad básica con variables y funciones.
- **04. Marcadores de tareas:** se recomienda completar el capítulo de comentarios. La familiaridad con issues y control de versiones ayuda.
- **05. Comentarios frente a logging:** se recomienda completar el capítulo de comentarios. Los conocimientos básicos sobre ejecución de programas y excepciones serán útiles.
- **06. PEP 8 y legibilidad:** se recomienda conocer la sintaxis básica de Python y completar los capítulos de comentarios y nombres significativos.

Los requisitos previos planificados podrán ajustarse cuando se escriba cada capítulo. El tiempo estimado de estudio se publicará solamente después de que el capítulo tenga contenido completo y revisable.

## Secuencia recomendada

Estudia los capítulos en orden numérico. Después de comprender sus requisitos previos, cada capítulo también puede consultarse de forma independiente.

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
- registrar tareas técnicas con suficiente contexto para que continúen siendo útiles;
- decidir cuándo la información de ejecución pertenece al logging;
- aplicar las recomendaciones de PEP 8 con criterio, sin tratarlas como sintaxis de Python;
- revisar código considerando claridad, exactitud, privacidad y facilidad de mantenimiento.

## Capítulo actual

Después de estudiar [Comentarios en Python](01-comments/README.es.md), [Docstrings en Python](02-docstrings/README.es.md) y [Nombres Significativos y Código Autoexplicativo](03-meaningful-names/README.es.md), continúa con [Marcadores de Tareas y Seguimiento Técnico](04-task-markers/README.es.md). Todos los capítulos disponibles incluyen explicaciones multilingües, ejemplos ejecutables, un ejercicio y un resumen de consulta rápida.

## Estructura del directorio

```text
comments-and-documentation/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-comments/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── business_rule_comments.py
│       ├── unnecessary_comments.py
│       └── useful_comments.py
├── 02-docstrings/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── class_docstrings.py
│       ├── function_docstrings.py
│       └── inspect_docstrings.py
├── 03-meaningful-names/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── booleans_and_units.py
│       ├── refactor_for_intent.py
│       └── vague_and_clear_names.py
└── 04-task-markers/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── actionable_markers.py
        ├── scan_markers.py
        └── temporary_workaround.py
```

Los directorios de los próximos capítulos se añadirán cuando sus contenidos completos estén preparados. Evitamos placeholders vacíos para que cada directorio de capítulo versionado contenga material útil.
