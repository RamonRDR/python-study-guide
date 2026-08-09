# Roadmap de Python Study Guide

[🇺🇸 English](roadmap.en.md) · [🇧🇷 Português](roadmap.pt-BR.md) · [🇪🇸 Español](roadmap.es.md)

Este roadmap acompaña tanto la ruta educativa como la base del repositorio que la sostiene. La numeración de las fases representa la secuencia de aprendizaje prevista, pero el trabajo del repositorio puede anticipar secciones posteriores cuando eso ayude a establecer estándares útiles.

## Leyenda de estados

- **Completada:** el alcance planificado está disponible y revisado.
- **En progreso:** ya existe material útil, pero el alcance planificado todavía no está cerrado.
- **Planificada:** la fase todavía no ha comenzado como una sección completa de aprendizaje.

## Progreso actual

| Fase | Estado | Resultado actual |
|---|---|---|
| 0. Base del proyecto | Completada | Base disponible, auditada y oficialmente completada |
| 1. Fundamentos | Completada | Seis capítulos revisados cubren ejecución, entrada y salida, variables y nombres, tipos de datos incorporados, inspección de tipos y conversión de tipos |
| 2. Textos y números | Completada | Cuatro capítulos revisados cubren creación de strings, métodos comunes, comportamiento numérico y booleano, precisión de punto flotante y funciones numéricas incorporadas |
| 3. Colecciones | En progreso | Los Capítulos 01 a 05 cubren listas, tuplas, diccionarios, unicidad en conjuntos, pertenencia y relaciones fundamentales entre conjuntos |
| 4. Flujo del programa | Planificada | Contenido todavía no iniciado |
| 5. Funciones | Planificada | Contenido todavía no iniciado |
| 6. Comentarios, documentación y código limpio | Completada | Seis capítulos revisados están disponibles y la sección educativa piloto está oficialmente completada |
| 7. Errores, archivos y módulos | Planificada | Contenido todavía no iniciado |
| 8. Biblioteca estándar | Planificada | Contenido todavía no iniciado |
| 9. Bibliotecas externas | Planificada | Contenido todavía no iniciado |
| 10. Proyectos prácticos | Planificada | Contenido todavía no iniciado |

Las Fases 0, 1, 2 y 6 están completadas. La Fase 3 ahora está en progreso con sus cinco primeros capítulos de Colecciones disponibles, mientras la Fase 6 continúa proporcionando el modelo editorial y de calidad para las secciones posteriores.

## Fase 0: Base del proyecto

### Elementos completados

- [x] READMEs principales multilingües
- [x] Estructura inicial escalable
- [x] Guías de contribución multilingües
- [x] Plantillas de pull request e issues en GitHub
- [x] Estándares de la comunidad y orientaciones para reportes
- [x] Formato editorial coherente para los capítulos
- [x] Licencia MIT
- [x] Registros de autoría y mantenimiento
- [x] Flujo basado en pull requests y rama `main` protegida
- [x] Instrucciones del repositorio para colaboradores y agentes de IA
- [x] Guía de desarrollo responsable asistido por IA
- [x] Roadmap y documentación de la estructura en tres idiomas
- [x] Verificaciones automáticas para archivos Python, ejemplos aprobados, enlaces internos y estructura
- [x] Identidad visual original y recursos del repositorio
- [x] Auditoría final de navegación, terminología, accesibilidad y estado
- [x] Marcar oficialmente la Fase 0 como completada

### Seguimiento planificado y no bloqueante

- Refinar y reemplazar los recursos visuales con exportaciones de alta calidad después de completar el encuadre final del logotipo.

## Fase 1: Fundamentos

- [x] [Cómo Python ejecuta un programa](../fundamentals/01-how-python-runs-a-program/README.es.md)
- [x] [`print()` e `input()`](../fundamentals/02-print-and-input/README.es.md)
- [x] [Variables y nombres](../fundamentals/03-variables-and-naming/README.es.md)
- [x] [Tipos de datos incorporados](../fundamentals/04-built-in-data-types/README.es.md)
- [x] [`type()` e `isinstance()`](../fundamentals/05-type-and-isinstance/README.es.md)
- [x] [Conversión de tipos](../fundamentals/06-type-conversion/README.es.md)

## Fase 2: Textos y números

- [x] [Creación e indexación de strings](../strings-and-numbers/01-string-creation-and-indexing/README.es.md)
- [x] [Métodos comunes de strings](../strings-and-numbers/02-common-string-methods/README.es.md)
- [x] [`int`, `float` y `bool`](../strings-and-numbers/03-int-float-and-bool/README.es.md)
- [x] [Funciones numéricas incorporadas: `round()`, `abs()`, `min()`, `max()` y `sum()`](../strings-and-numbers/04-numeric-builtins/README.es.md)

## Fase 3: Colecciones

- [x] [Creación, indexación y slicing de listas](../collections/01-list-creation-and-indexing/README.es.md)
- [x] [Modificar listas y métodos comunes de listas](../collections/02-modifying-lists-and-methods/README.es.md)
- [x] [Tuplas e inmutabilidad](../collections/03-tuples-and-immutability/README.es.md)
- [x] [Diccionarios: claves y valores](../collections/04-dictionaries-keys-and-values/README.es.md)
- [x] [Conjuntos y valores únicos](../collections/05-sets-and-unique-values/README.es.md)
- [ ] Elegir la colección correcta

## Fase 4: Flujo del programa

- `if`, `elif` y `else`
- `for` y `while`
- `range()`, `enumerate()` y `zip()`
- `break`, `continue` y diseño de bucles

## Fase 5: Funciones

- `def`
- Parámetros y argumentos
- Valores de retorno
- Alcance
- Type hints
- Valores predeterminados
- `*args` y `**kwargs`
- Funciones trabajando juntas
- Flujo de datos entre funciones

## Fase 6: Comentarios, documentación y código limpio

Consulta la [ruta de aprendizaje de la sección](../comments-and-documentation/README.es.md).

- [x] Cuándo y por qué comentar
- [x] Cuándo no comentar
- [x] Comentarios útiles y perjudiciales
- [x] Docstrings
- [x] Nombres significativos y código autoexplicativo
- [x] `TODO`, `FIXME`, `NOTE` y marcadores relacionados
- [x] Comentarios frente a logging
- [x] PEP 8 y legibilidad

La Fase 6 está oficialmente completada y proporciona el modelo editorial y de calidad para las demás secciones de aprendizaje.

## Fase 7: Errores, archivos y módulos

- `try`, `except`, `else` y `finally`
- `raise` y excepciones personalizadas
- `open()` y `with`
- TXT, CSV y JSON
- Imports, módulos y paquetes

## Fase 8: Biblioteca estándar

- `pathlib`
- `datetime`
- `json`
- `csv`
- `logging`
- `collections`
- `itertools`
- `decimal`
- `os` y `shutil`

## Fase 9: Bibliotecas externas

- `pandas`
- `openpyxl`
- `requests`
- `pytest`

## Fase 10: Proyectos prácticos

- Calculadora de calificaciones
- Registro de usuarios
- Control de gastos
- Analizador de CSV
- Generador de informes
- Organizador de archivos
- Flujo ficticio de conciliación
- Flujo simulado de automatización
