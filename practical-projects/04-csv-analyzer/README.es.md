<div align="center">

# Proyecto 04 · Analizador CSV

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Proyectos Prácticos](../README.es.md)

Este es el cuarto proyecto de la **Fase 10: Proyectos Prácticos**. Se enfoca en fronteras CSV, schemas explícitos, conversión tipada de filas, validación por fila, fallos estructurales, agregación determinista y análisis comprobable sin depender de pandas.

**Tiempo estimado de estudio e implementación:** 180–240 minutos.

## Objetivos de aprendizaje

Al terminar este proyecto, deberías poder:

- definir un schema CSV exacto en lugar de asumir que cualquier tabla es aceptable;
- distinguir una estructura CSV malformada de datos inválidos en una fila;
- convertir campos de texto en valores `int`, `bool`, `date` y `Enum`;
- conservar filas válidas aunque otras fallen la validación;
- reportar varios problemas de campo para una sola fila rechazada;
- detectar identificadores duplicados entre filas aceptadas;
- mantener inmutables los resultados públicos del parser;
- agregar registros de forma determinista sin redondeo oculto de `float`;
- filtrar registros validados sin modificarlos;
- probar encabezados, entrada malformada, reglas de conversión, rechazos y resúmenes.

## 1. Resumen del proyecto

Construye un analizador CSV para un conjunto ficticio de incidentes.

El analizador debe:

1. exigir un schema exacto de encabezados;
2. leer archivos CSV UTF-8 con BOM UTF-8 opcional;
3. convertir filas de incidentes en registros tipados e inmutables;
4. recopilar problemas de validación por fila sin descartar todos los datos correctos;
5. rechazar valores `event_id` duplicados entre registros aceptados;
6. distinguir errores de schema/formato del documento de errores de datos por fila;
7. resumir registros válidos;
8. filtrar registros válidos por severidad, estado de resolución o servicio;
9. formatear un informe de texto determinista;
10. demostrar caminos de éxito y fallo con pruebas automatizadas.

## 2. Contrato del conjunto de datos

El encabezado obligatorio exacto es:

```text
event_id,service,severity,duration_minutes,resolved,occurred_on
```

Cada columna tiene un contrato diferente:

```text
event_id         -> entero ASCII positivo
service          -> texto legible no vacío, con espacios normalizados
severity         -> low | medium | high | critical
duration_minutes -> entero ASCII no negativo
resolved         -> true | false
occurred_on      -> fecha de calendario exacta YYYY-MM-DD
```

Todos los registros de ejemplo son ficticios.

## 3. Por qué el encabezado es estricto

CSV es solo un formato contenedor. Que un archivo sea CSV válido no significa que contenga la tabla esperada por el programa.

Estos son schemas diferentes:

```text
event_id,service,severity,duration_minutes,resolved,occurred_on
```

y:

```text
service,event_id,severity,duration_minutes,resolved,occurred_on
```

Este proyecto exige deliberadamente los nombres y el orden exactos definidos en `EXPECTED_HEADERS`.

Así, un cambio inesperado de schema queda visible en lugar de mapear datos incorrectamente en silencio.

## 4. Errores estructurales frente a errores de fila

El analizador separa dos niveles de fallo.

### Fallos a nivel de documento

Ejemplos:

- ausencia de fila de encabezado;
- nombres de encabezado duplicados;
- nombres u orden incorrectos;
- comillas malformadas rechazadas por el parser CSV de Python.

Estos casos lanzan `CsvSchemaError` o `CsvFormatError`, porque el documento no puede considerarse la tabla esperada.

### Fallos a nivel de fila

Ejemplos:

- `event_id` igual a cero;
- severidad igual a `urgent`;
- duración negativa;
- resolved igual a `yes`;
- fecha igual a `2026-02-30`;
- fila con valores extra o ausentes.

Estos casos generan un `RejectedRow`. Las demás filas válidas siguen disponibles para el análisis.

## 5. Conversión tipada

`csv.DictReader` devuelve valores de texto. El proyecto no deja todo como strings.

Una fila válida se transforma en:

```python
IncidentRecord(
    event_id=101,
    service="Payments",
    severity=Severity.HIGH,
    duration_minutes=45,
    resolved=True,
    occurred_on=date(2026, 8, 1),
)
```

Así, los errores de conversión quedan concentrados en la frontera de entrada y el resto del programa trabaja con tipos más fuertes.

## 6. Contratos de enteros

Dos helpers hacen explícita la intención numérica:

```python
parse_positive_integer(...)
parse_non_negative_integer(...)
```

`event_id` debe ser mayor que cero.

`duration_minutes` puede ser cero.

Los parsers aceptan únicamente dígitos decimales ASCII. Valores como `-1`, `1.5` y dígitos Unicode de ancho completo se rechazan bajo el contrato de este proyecto.

## 7. Normalización de servicio

Los nombres de servicio son datos orientados a presentación.

El analizador reduce espacios externos y repetidos:

```python
normalize_service("  Data   Sync ")
# "Data Sync"
```

Se conserva el uso de mayúsculas y minúsculas y se aplica un pequeño límite de longitud definido por el proyecto.

Para agrupación y filtro, la comparación de servicios no distingue mayúsculas y minúsculas, mientras el primer formato de presentación aceptado se conserva en el resumen.

## 8. Severidad como enum

La severidad usa:

```python
class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
```

La entrada no distingue mayúsculas y minúsculas, por lo que `HIGH`, `high` y ` High ` se convierten en `Severity.HIGH`.

Los valores desconocidos se rechazan en lugar de entrar al modelo como texto arbitrario.

## 9. Parsing Boolean estricto

La columna `resolved` acepta solo:

```text
true
false
```

ignorando espacios externos y capitalización.

Valores como `yes`, `1` o `truthy` se rechazan.

Esto evita inventar reglas sorprendentes de truthiness para datos externos.

## 10. Parsing estricto de fechas

Las fechas deben usar exactamente:

```text
YYYY-MM-DD
```

El parser comprueba tanto la forma como la validez del calendario.

Por lo tanto:

```text
2024-02-29 -> válido
2026-2-01  -> formato inválido
20260201   -> formato inválido
2026-02-30 -> fecha de calendario inválida
```

El resultado es un objeto real `datetime.date`, no una string con aspecto de fecha.

## 11. Registros válidos inmutables

`IncidentRecord` es una dataclass congelada con slots.

La validación también se ejecuta cuando se llama directamente al constructor, así que no se pueden omitir las reglas simplemente evitando el parser CSV.

El parser devuelve tuplas de registros en vez de exponer listas internas mutables.

## 12. Problemas a nivel de campo

Una sola fila incorrecta puede tener varios problemas independientes.

Por ejemplo:

```text
0, ,urgent,-2,yes,2026-02-30
```

genera problemas para:

```text
event_id
service
severity
duration_minutes
resolved
occurred_on
```

El proyecto recopila todos esos problemas de la fila lógica en lugar de detenerse en el primero.

## 13. Numeración de filas lógicas

`RejectedRow.row_number` identifica la fila lógica del CSV, considerando el encabezado como fila 1 y el primer registro de datos como fila 2.

Las líneas físicas completamente vacías son ignoradas por el lector CSV de Python.

Este proyecto usa numeración de registros lógicos y no promete números físicos exactos para cualquier combinación posible de campos CSV multilínea entre comillas.

## 14. Valores extra y ausentes

Una fila con más valores de los permitidos por el schema se rechaza con un problema `_row`.

Una fila con un campo final ausente pasa `None` al parser de ese campo y es rechazada por el contrato correspondiente.

Esto impide que datos truncados o desplazados parezcan válidos.

## 15. Identificadores duplicados

`event_id` debe ser único entre **filas válidas aceptadas**.

Si un `event_id=101` válido ya fue aceptado, una fila válida posterior con `event_id=101` será rechazada.

Una fila inválida anterior no reserva el ID. Por lo tanto, una fila válida posterior puede usar el mismo ID.

Esta regla convierte al conjunto aceptado en la fuente de unicidad.

## 16. Lectura de archivos y BOM UTF-8

`load_incident_csv(...)` abre archivos con:

```python
encoding="utf-8-sig"
newline=""
```

`utf-8-sig` acepta un archivo UTF-8 normal y elimina un BOM UTF-8 opcional al inicio.

`newline=""` sigue la orientación del módulo CSV de Python para que el propio parser controle los saltos de línea.

Los archivos inexistentes propagan `FileNotFoundError` intencionalmente.

## 17. Entradas por texto, stream y archivo

El proyecto expone tres fronteras de entrada:

```python
parse_incident_csv(stream)
parse_incident_csv_text(text)
load_incident_csv(path)
```

El comportamiento central de parsing permanece en `parse_incident_csv(...)`.

Esto separa I/O de archivo de la conversión de filas y facilita pruebas con `StringIO` o strings literales.

## 18. Resultado del parsing

Un parsing exitoso devuelve:

```python
CsvLoadResult(
    records=(...),
    rejected_rows=(...),
)
```

Las propiedades auxiliares ofrecen:

```text
valid_count
rejected_count
data_row_count
```

`data_row_count` cuenta filas lógicas aceptadas más rechazadas, sin incluir el encabezado.

## 19. Agregación determinista

`summarize_incidents(...)` calcula:

- total de registros válidos;
- cantidades resueltas y no resueltas;
- duración total;
- duración promedio con dos decimales;
- mayor duración;
- conteo para cada severidad;
- conteo por servicio.

Los conteos por servicio se ordenan sin distinguir mayúsculas y minúsculas para producir una salida estable.

Las severidades siempre siguen el orden del enum:

```text
low
medium
high
critical
```

## 20. Redondeo exacto del promedio

El promedio se devuelve como `Decimal` con dos decimales.

La implementación no depende del contexto global de `decimal` del llamador. Calcula centésimos enteros directamente y aplica redondeo half-up.

Por ejemplo, un promedio exacto de `0.375` se convierte en:

```text
0.38
```

Esto mantiene el informe determinista.

## 21. Análisis vacío

Un conjunto válido vacío todavía puede analizarse.

El resumen devuelve:

```text
total de registros: 0
duración promedio: 0.00
mayor duración: 0
conteos por servicio: vacío
todas las severidades: 0
```

No es necesario generar una excepción por división entre cero.

## 22. Invariantes del resumen

`IncidentSummary` valida su propio constructor público.

Entre otras comprobaciones:

- resueltos + no resueltos debe ser igual al total;
- la duración promedio debe corresponder a la duración total dividida por la cantidad de registros;
- la mayor duración no puede superar la duración total, y los resúmenes vacíos o de un solo registro aplican sus restricciones naturales de duración;
- los conteos de severidad deben contener cada valor del enum exactamente una vez;
- el total de severidades debe ser igual al total de registros;
- las claves de servicio deben ser únicas sin distinguir capitalización;
- los conteos de servicio deben estar ordenados de manera determinista;
- el total de conteos de servicio debe ser igual al total de registros.

Un resumen que se contradice es rechazado.

## 23. Filtros

`filter_incidents(...)` puede combinar criterios opcionales:

```python
filter_incidents(
    records,
    severity=Severity.HIGH,
    resolved=True,
    service="Payments",
)
```

La función devuelve una tupla y no modifica la colección original.

La comparación de servicio ignora mayúsculas y minúsculas después de aplicar la misma normalización de espacios utilizada por el modelo.

## 24. Informe de texto determinista

`format_analysis(...)` produce un informe estable estilo CLI:

```text
data rows: 6
valid: 4
rejected: 2
resolved: 3
unresolved: 1
total duration: 165
average duration: 41.25
longest duration: 90
```

La función también verifica que el resumen entregado corresponda a la misma cantidad de filas válidas del resultado de parsing.

## 25. Estructura del proyecto

```text
04-csv-analyzer/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── csv_analyzer.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_csv_analyzer.py
```

## 26. Ejecutar la demostración determinista

Desde la raíz del repositorio:

```bash
python practical-projects/04-csv-analyzer/demo.py
```

Salida esperada:

```text
data rows: 6
valid: 4
rejected: 2
resolved: 3
unresolved: 1
total duration: 165
average duration: 41.25
longest duration: 90
critical: 1
```

La demostración contiene intencionalmente dos filas inválidas para hacer visible el comportamiento de rechazo.

## 27. Ejecutar las pruebas del proyecto

```bash
python -m pytest -q practical-projects/04-csv-analyzer/tests
```

La suite inicial contiene **75 escenarios pytest** que cubren helpers de parsing, validación directa de modelos, fallos de schema, CSV malformado, problemas de campo por fila, IDs duplicados, BOM UTF-8, lectura de archivos, invariantes de agregación, filtros e informe determinista.

## 28. Caminos de fallo para inspeccionar manualmente

Prueba modificar los datos de la demo para incluir:

```text
orden incorrecto de encabezados
occurred_on ausente
séptimo valor extra
severity = urgent
resolved = yes
occurred_on = 2026-02-30
event_id válido duplicado
```

Observa qué problemas detienen el documento y cuáles rechazan solo una fila.

## 29. Nota de diseño: parsear en la frontera

El resto del analizador no debería preguntar repetidamente si `"45"` es un número o si `"true"` significa un Boolean.

Esas conversiones ocurren una sola vez en la frontera CSV.

Después de que una fila se convierte en `IncidentRecord`, las funciones posteriores pueden confiar en sus tipos e invariantes.

## 30. Nota de diseño: éxito parcial útil

Muchos flujos de importación deben decidir si una sola fila inválida debería destruir todas las filas válidas.

Este proyecto elige:

```text
estructura de documento inválida -> detener
datos de fila inválidos          -> rechazar fila y conservar válidas
```

No es la única política posible, pero es explícita, comprobable y útil para estudiar diseño de ingestión de datos.

## 31. Nota de diseño: biblioteca estándar antes de pandas

La Fase 9 ya presentó pandas. Este proyecto usa deliberadamente el módulo `csv` de Python.

El objetivo es exponer mecanismos que pandas suele ocultar:

- expectativas de schema;
- conversión de strings crudas;
- campos extra y ausentes;
- política de rechazo por fila;
- duplicidad de identificadores;
- registros de dominio inmutables.

Comprender estas fronteras facilita razonar sobre dataframes más adelante.

## 32. Lo que este proyecto no incluye intencionalmente

Esta versión no incluye:

- detección automática de delimitador;
- schemas arbitrarios definidos por el usuario;
- pandas;
- entrada Excel;
- persistencia en base de datos;
- datasets mayores que la memoria mediante streaming;
- procesamiento paralelo;
- corrección fuzzy de valores inválidos;
- gráficos o dashboards;
- interfaz gráfica.

Son extensiones posibles, pero diluirían la lección principal de ingestión y validación.

## 33. Desafío de extensión: schema configurable

Extrae las reglas de campo a especificaciones reutilizables de columnas.

Una versión futura podría definir:

```text
nombre de columna
obligatoria/opcional
parser
normalizador
valor predeterminado
regla de unicidad
```

Mantén simple el proyecto actual antes de generalizarlo.

## 34. Desafío de extensión: exportar rechazos

Escribe las filas lógicas rechazadas y sus mensajes de problema en un segundo archivo CSV.

Piensa cuidadosamente en:

- columnas estables;
- quoting;
- varios problemas por fila;
- si conservar o no los valores crudos;
- riesgos de formula injection en CSV si el archivo se abrirá en software de hojas de cálculo.

## 35. Desafío de extensión: filtros de fecha

Añade fechas inicial y final opcionales a `filter_incidents(...)`.

Define si los límites son inclusivos y prueba rangos inválidos, como una fecha inicial posterior a la fecha final.

## 36. Discusión de portafolio

Al presentar este proyecto, explica más que “lee archivos CSV”.

Puntos de ingeniería útiles incluyen:

- contratos exactos de schema;
- fallos estructurales frente a fallos de fila;
- conversión tipada en la frontera de datos;
- registros aceptados inmutables;
- diagnóstico de varios campos por fila rechazada;
- detección de duplicados entre filas válidas;
- agregación y redondeo deterministas;
- invariantes públicas del resumen;
- puntos de entrada comprobables por archivo, stream y texto;
- uso deliberado de la biblioteca estándar en vez de ocultar la ingestión detrás de pandas.

## 37. Checklist de revisión

Antes de considerar completa tu propia implementación, verifica:

- ¿Se revisan los nombres y el orden de encabezados antes de confiar en las filas?
- ¿Se rechazan encabezados duplicados?
- ¿Un CSV malformado lanza un error a nivel de documento?
- ¿Una fila incorrecta puede coexistir con filas válidas en el resultado?
- ¿Son visibles todos los problemas de campo de una fila rechazada?
- ¿Se detectan valores extra y ausentes?
- ¿Los `event_id` aceptados son únicos?
- ¿Una fila inválida evita reservar su ID?
- ¿Las fechas se convierten en objetos reales `date` después del parsing?
- ¿El parsing Boolean es explícito en lugar de basarse en truthiness?
- ¿Los conteos del resumen son internamente consistentes?
- ¿El redondeo del promedio es determinista?
- ¿Los filtros no modifican los datos originales?
- ¿Los ejemplos son ficticios y seguros para publicación?

## 38. Próximo proyecto

El Proyecto 04 añade ingestión CSV consciente de schema, validación por fila, conversión tipada, política de éxito parcial, filtros deterministas y agregación a la progresión de la Fase 10.

El siguiente proyecto planificado es el **Generador de Informes**, que cambiará el foco desde la ingestión de datos estructurados hacia la composición de salidas estructuradas e informes listos para presentación.
