<div align="center">

# Biblioteca Estándar

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Python incluye una biblioteca estándar amplia. Estos módulos resuelven problemas comunes sin requerir instalación de terceros, pero cada herramienta mantiene sus propios contratos, trade-offs y modos de fallo.

La Fase 8 parte del modelo de imports aprendido en la Fase 7 y estudia un conjunto enfocado de módulos frecuentes en programas Python reales.

## Ruta de aprendizaje

| Capítulo | Foco principal | Nivel | Estado |
|---|---|---|---|
| [01. `pathlib`](01-pathlib/README.es.md) | Representar, componer, inspeccionar, crear, leer y descubrir rutas del sistema de archivos con objetos específicos para rutas | Intermedio | Disponible |
| [02. `datetime`](02-datetime/README.es.md) | Trabajar con fechas, horas, duraciones, parsing, formato, conciencia de timezone y aritmética | Intermedio | Disponible |
| [03. `json`](03-json/README.es.md) | Controlar contratos de serialización y decodificación, comportamiento numérico estricto, hooks, valores personalizados, nombres duplicados y salida determinista | Intermedio | Disponible |
| [04. `csv`](04-csv/README.es.md) | Controlar dialectos, quoting, escaping, forma de filas, sniffing y contratos de texto tabular | Intermedio | Disponible |
| [05. `logging`](05-logging/README.es.md) | Diseñar jerarquía de loggers, configuración, registros contextuales, entrega mediante colas, concurrencia y contratos de logging en runtime | Intermedio | Disponible |
| [06. `collections`](06-collections/README.es.md) | Usar contenedores especializados, capas de mappings, registros de tupla, reordenación, wrappers e interfaces de colección mediante contratos explícitos de operación | Intermedio | Disponible |
| 07. `itertools` | Construir pipelines eficientes de iteradores con herramientas reutilizables | Intermedio | Planificado |
| 08. `decimal` | Realizar aritmética decimal exacta con redondeo y contexto explícitos | Intermedio | Planificado |
| 09. `os` y `shutil` | Trabajar con entorno, operaciones de filesystem de nivel más bajo, copia, movimiento y árboles de directorios | Intermedio | Planificado |

## Prerrequisitos

Antes de comenzar esta fase conviene dominar:

- funciones y valores de retorno;
- colecciones e iteración;
- excepciones;
- archivos y context managers;
- imports, módulos y paquetes.

La ruta completa de las Fases 1-7 proporciona esas bases.

## Secuencia recomendada

Al seguir el currículo completo, estudia en orden:

```text
01. Modelar rutas con pathlib
        ↓
02. Modelar fechas y duraciones con datetime
        ↓
03. Profundizar JSON
        ↓
04. Profundizar CSV
        ↓
05. Configurar logging en runtime
        ↓
06. Usar colecciones especializadas
        ↓
07. Componer pipelines de iteradores
        ↓
08. Usar aritmética decimal exacta
        ↓
09. Trabajar con utilidades de OS y filesystem
```

El orden es intencional. Empieza con trabajo familiar de archivos y continúa por tiempo, formatos de datos, diagnóstico, contenedores, iteración, precisión numérica y utilidades de sistema de nivel más bajo.

## Objetivos de la sección

Al final de la Fase 8 deberías poder:

- elegir herramientas de la biblioteca estándar en lugar de reinventar infraestructura común;
- leer la documentación oficial de módulos con mayor confianza;
- entender que el nombre de un módulo no es un contrato completo de uso;
- combinar módulos de la biblioteca estándar con funciones, excepciones, archivos y paquetes;
- reconocer APIs superpuestas y elegir según la intención;
- preservar comportamiento determinista cuando orden y entorno pueden variar;
- escribir programas pequeños que dependan solo de Python y su biblioteca estándar.

## Estado de la fase

La Fase 8 está en progreso. El Capítulo 01 introduce [`pathlib`](01-pathlib/README.es.md), el Capítulo 02 añade [`datetime`](02-datetime/README.es.md), el Capítulo 03 profundiza [`json`](03-json/README.es.md), el Capítulo 04 profundiza [`csv`](04-csv/README.es.md), el Capítulo 05 profundiza [`logging`](05-logging/README.es.md) y el Capítulo 06 añade [`collections`](06-collections/README.es.md) con contratos de `Counter`, `defaultdict`, `deque`, `namedtuple`, `ChainMap`, `OrderedDict`, wrappers de extensión e interfaces de `collections.abc`. El próximo capítulo planificado es `itertools`.

Los Capítulos 03, 04, 05 y 06 profundizan temas que aparecieron anteriormente en el currículo. Sus apariciones previas enseñaron formatos de archivo, diseño de logging o modelos de colecciones integradas; en esta fase estudiamos los módulos de la biblioteca estándar, sus APIs y sus trade-offs.

## Estructura del directorio

```text
standard-library/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-pathlib/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── discover_python_files.py
│       ├── inspect_paths.py
│       ├── path_parts.py
│       └── text_workspace.py
├── 02-datetime/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── date_arithmetic.py
│       ├── duration_seconds.py
│       ├── parse_and_format.py
│       └── utc_conversion.py
├── 03-json/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── decimal_decode.py
│       ├── deterministic_json.py
│       ├── reject_duplicate_keys.py
│       └── strict_numbers.py
├── 04-csv/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── dialect_round_trip.py
│       ├── quote_none_escape.py
│       ├── sniff_delimiter.py
│       └── validate_dict_rows.py
├── 05-logging/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── context_filter.py
│       ├── dict_config_routing.py
│       ├── queue_listener.py
│       └── stacklevel_helper.py
└── 06-collections/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── bounded_deque.py
        ├── chainmap_config.py
        ├── counter_inventory.py
        └── defaultdict_grouping.py
```

Se añadirán nuevos directorios de capítulos a medida que avance la fase.
