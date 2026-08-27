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
| 3. Colecciones | Completada | Seis capítulos revisados cubren listas, tuplas, diccionarios, conjuntos y elección de colección según la intención |
| 4. Flujo del programa | Completada | Ocho capítulos revisados cubren condiciones, ramificaciones, coincidencia de patrones estructurales, `for`, ayudas de iteración, `while`, control de bucles y elección y combinación de herramientas de flujo según la intención |
| 5. Funciones | Completada | Nueve capítulos revisados cubren `def`, llamadas, entradas obligatorias, valores retornados, alcance, type hints, valores predeterminados seguros, argumentos flexibles, composición de funciones y flujo explícito de datos |
| 6. Comentarios, documentación y código limpio | Completada | Seis capítulos revisados están disponibles y la sección educativa piloto está oficialmente completada |
| 7. Errores, archivos y módulos | En progreso | Los Capítulos 01–04 cubren manejo de excepciones, señalización deliberada, I/O seguro de archivos y formatos TXT/CSV/JSON |
| 8. Biblioteca estándar | Planificada | Contenido todavía no iniciado |
| 9. Bibliotecas externas | Planificada | Contenido todavía no iniciado |
| 10. Proyectos prácticos | Planificada | Contenido todavía no iniciado |

Las Fases 0, 1, 2, 3, 4, 5 y 6 están completadas. La Fase 7 está en progreso con manejo de excepciones, señalización deliberada, I/O seguro de archivos y límites de formatos TXT/CSV/JSON ya disponibles. El último capítulo planificado de la Fase 7 es **Imports, módulos y paquetes**. La Fase 6 continúa proporcionando el modelo editorial y de calidad para las secciones posteriores.

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
- [x] [Modificar listas y métodos comunes](../collections/02-modifying-lists-and-methods/README.es.md)
- [x] [Tuplas e inmutabilidad](../collections/03-tuples-and-immutability/README.es.md)
- [x] [Diccionarios: claves y valores](../collections/04-dictionaries-keys-and-values/README.es.md)
- [x] [Conjuntos y valores únicos](../collections/05-sets-and-unique-values/README.es.md)
- [x] [Elegir la colección adecuada](../collections/06-choosing-the-right-collection/README.es.md)

## Fase 4: Flujo del programa

Consulta la [ruta de aprendizaje de la sección](../program-flow/README.es.md).

- [x] [Condiciones, comparaciones y lógica booleana](../program-flow/01-conditions-comparisons-and-boolean-logic/README.es.md)
- [x] [`if`, `elif` y `else`](../program-flow/02-if-elif-and-else/README.es.md)
- [x] [`match` y `case`: coincidencia de patrones estructurales](../program-flow/03-match-and-case/README.es.md)
- [x] [Bucles `for` e iteración](../program-flow/04-for-loops-and-iteration/README.es.md)
- [x] [`range()`, `enumerate()` y `zip()`](../program-flow/05-range-enumerate-and-zip/README.es.md)
- [x] [Bucles `while` y repetición guiada por estado](../program-flow/06-while-loops-and-state-driven-repetition/README.es.md)
- [x] [`break`, `continue` y `else` de bucles](../program-flow/07-break-continue-and-loop-else/README.es.md)
- [x] [Elegir y combinar el flujo del programa](../program-flow/08-choosing-and-combining-program-flow/README.es.md)

La Fase 4 construye intencionalmente condiciones confiables primero, las usa para ramificaciones condicionales, introduce coincidencia de patrones estructurales, avanza hacia la repetición con `for`, añade ayudas para progresiones numéricas, posiciones e iteración paralela, introduce repetición guiada por estado con `while`, añade control deliberado de bucles con `break`, `continue` y `else` de bucle y cierra enseñando cómo elegir y combinar esas herramientas según la intención. Los Capítulos 01–08 están completados y la Fase 4 está oficialmente completada.

## Fase 5: Funciones

Consulta la [ruta de aprendizaje de la sección](../functions/README.es.md).

- [x] [Definir y llamar funciones](../functions/01-defining-and-calling-functions/README.es.md)
- [x] [Parámetros y argumentos](../functions/02-parameters-and-arguments/README.es.md)
- [x] [Valores de retorno](../functions/03-return-values/README.es.md)
- [x] [Alcance](../functions/04-scope/README.es.md)
- [x] [Type hints](../functions/05-type-hints/README.es.md)
- [x] [Valores predeterminados](../functions/06-default-values/README.es.md)
- [x] [`*args` y `**kwargs`](../functions/07-args-and-kwargs/README.es.md)
- [x] [Funciones trabajando juntas](../functions/08-functions-working-together/README.es.md)
- [x] [Flujo de datos entre funciones](../functions/09-data-flow-between-functions/README.es.md)

La Fase 5 está completada. El Capítulo 01 establece `def`, llamadas, reutilización, orden de ejecución, nombres, `pass`, `None` implícito y la conexión con el flujo del programa. El Capítulo 02 añade parámetros obligatorios, argumentos posicionales y por palabra clave básicos, expresiones como argumentos, errores de llamada y seguimiento del flujo de entrada. El Capítulo 03 añade `return`, resultados reutilizables, retornos por rama y anticipados, `None` y retornos en tupla. El Capítulo 04 añade nombres locales y globales, namespaces locales por llamada, búsqueda, sombreado, `NameError`, `UnboundLocalError` y uso cauteloso de `global`. El Capítulo 05 añade anotaciones de parámetros y retorno, hints de tipos incorporados y colecciones, `-> None`, `str | None`, metadatos de anotaciones y la diferencia entre información estática de tipos, validación en runtime y conversión. El Capítulo 06 añade valores predeterminados, reemplazos posicionales y por palabra clave selectivos, evaluación al definir la función, la trampa de valores mutables y el patrón seguro con `None` para crear objetos mutables nuevos. El Capítulo 07 añade recolección de cantidades variables de argumentos posicionales y por palabra clave con `*args` y `**kwargs`, comportamiento de tupla y diccionario dentro de la función, firmas mixtas simples, type hints básicos para los valores recogidos y la distinción entre recolección en la definición y desempaquetado posterior en la llamada. El Capítulo 08 compone funciones auxiliares y coordinadoras, pasa resultados retornados entre pasos, mantiene explícitas las dependencias mediante parámetros y retornos, combina funciones con condiciones y bucles, distingue cálculo reutilizable de presentación e introduce grafos simples de llamadas. El Capítulo 09 cierra la fase siguiendo el flujo llamador-parámetro-retorno, los vínculos locales de parámetros, reasignación frente a mutación, resultados en tupla y `None`, pipelines explícitos, transformaciones de colecciones y la diferencia entre grafos de llamadas y seguimientos de flujo de datos.

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

Consulta la [ruta de aprendizaje de la sección](../errors-files-and-modules/README.es.md).

- [x] [`try`, `except`, `else` y `finally`](../errors-files-and-modules/01-try-except-else-finally/README.es.md)
- [x] [`raise` y excepciones personalizadas](../errors-files-and-modules/02-raise-and-custom-exceptions/README.es.md)
- [x] [`open()` y `with`](../errors-files-and-modules/03-open-and-with/README.es.md)
- [x] [TXT, CSV y JSON](../errors-files-and-modules/04-txt-csv-and-json/README.es.md)
- [ ] Imports, módulos y paquetes

La Fase 7 está en progreso. Los Capítulos 01–02 establecen manejo y señalización deliberada de excepciones. El Capítulo 03 añade I/O seguro de archivos y gestión de recursos. El Capítulo 04 añade contratos TXT, parsing y escritura de CSV y JSON, conversión explícita de tipos y límites entre parsing y validación. El próximo capítulo planificado es **Imports, módulos y paquetes**.

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

Cada proyecto debe incluir:

- requisitos;
- notas de diseño;
- implementación;
- explicación;
- ideas de pruebas;
- desafíos de ampliación;
- discusión de portafolio.

## Criterios continuos de calidad

Cada fase debe preservar:

- precisión técnica;
- consistencia multilingüe;
- ejemplos originales y seguros para publicación;
- datos seguros desde el punto de vista de la privacidad;
- ejemplos ejecutables de Python cuando corresponda;
- integridad de la navegación interna;
- atención a PEP 8;
- documentación de cambios estructurales relevantes;
- transparencia sobre dependencias y supuestos de versión.

El roadmap evolucionará a medida que el proyecto crezca, pero los cambios deben preservar la progresión desde los conceptos iniciales hasta el trabajo práctico integrado.
