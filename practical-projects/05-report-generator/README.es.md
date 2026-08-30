<div align="center">

# Proyecto 05 · Generador de Informes

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Proyectos Prácticos](../README.es.md)

Este es el quinto proyecto de la **Fase 10: Proyectos Prácticos**. Se centra en transformar registros de dominio ya validados en un pipeline confiable de informes: ventanas explícitas de período, agregación determinista, resúmenes independientes de la presentación, múltiples renderizadores y salida segura a archivos de texto.

**Tiempo estimado de estudio e implementación:** 180–240 minutos.

## Objetivos de aprendizaje

Al finalizar este proyecto, deberías poder:

- modelar datos de origen con registros inmutables y validados;
- definir explícitamente una ventana inclusiva para el informe;
- rechazar identificadores duplicados antes de agregar datos;
- separar los registros de origen de los incluidos en el período;
- calcular métricas de estado, duración, porcentaje y agrupación por equipo de forma determinista;
- representar agregados con objetos de resumen inmutables y validados;
- separar la construcción del informe de su renderización;
- renderizar el mismo informe como texto plano o Markdown;
- escapar delimitadores de tablas Markdown en valores visibles;
- escribir archivos UTF-8 mediante un contrato explícito entre formato y extensión;
- probar períodos vacíos, fechas límite, orden, redondeo, renderización y escritura de archivos.

## 1. Propuesta del proyecto

Construye un generador de informes para un conjunto ficticio de actividades operativas.

El generador debe:

1. validar registros de actividad inmutables;
2. definir una ventana inclusiva de fechas para cada informe;
3. rechazar IDs de actividad duplicados en el conjunto de origen;
4. incluir solo registros cuya fecha esté dentro del período solicitado;
5. ordenar los registros incluidos de forma determinista;
6. calcular métricas de resumen sin depender de la presentación;
7. agrupar equipos sin distinguir mayúsculas/minúsculas, conservando la primera grafía aceptada para mostrar;
8. renderizar el mismo informe como texto plano estilo TXT o Markdown;
9. exigir que la extensión del archivo coincida con el formato seleccionado;
10. escribir archivos UTF-8 sin crear silenciosamente directorios inexistentes;
11. demostrar el contrato del informe con pruebas automatizadas.

Todos los datos de ejemplo son ficticios.

## 2. Pipeline del informe

El modelo central de aprendizaje es:

```text
registros validados
    -> validación del origen
    -> filtro inclusivo por fecha
    -> orden determinista
    -> resumen validado
    -> informe inmutable
    -> renderizador
    -> escritura opcional en archivo
```

La idea importante es que agregación, presentación y persistencia son responsabilidades diferentes.

## 3. Contrato del registro de actividad

Un elemento válido de origen se representa con `ActivityRecord`:

```python
ActivityRecord(
    activity_id=101,
    team="Accounting",
    status=WorkStatus.COMPLETED,
    duration_minutes=30,
    occurred_on=date(2026, 8, 1),
)
```

El registro exige:

```text
activity_id      -> entero positivo, excluyendo bool
team             -> texto legible no vacío, con espacios normalizados
status           -> valor del enum WorkStatus
duration_minutes -> entero no negativo, excluyendo bool
occurred_on      -> valor simple datetime.date
```

La dataclass es frozen y usa slots para que el código de informes reciba un objeto de valor estable.

## 4. Normalización de texto legible

Los títulos y nombres de equipo eliminan espacios externos y colapsan espacios repetidos.

Por ejemplo:

```python
team="  Shared   Services  "
```

se convierte en:

```text
Shared Services
```

Se rechazan valores vacíos y valores que superen los pequeños límites definidos por el proyecto.

La intención no es corregir texto agresivamente, sino mantener un contrato de normalización estrecho y visible.

## 5. Estados explícitos del flujo

El proyecto usa:

```python
class WorkStatus(str, Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
```

Una cadena sin procesar como `"completed"` no es aceptada por el constructor del registro.

Después de validar los datos, el resto del dominio trabaja con valores explícitos del enum.

## 6. Ventana del informe

`ReportWindow` contiene:

```text
title
start_date
end_date
```

Ambas fechas son inclusivas.

En una ventana desde `2026-08-01` hasta `2026-08-31`, se incluyen registros en ambas fechas límite.

Se rechaza una fecha inicial posterior a la fecha final.

## 7. Fechas simples en lugar de datetimes

Este proyecto exige valores exactos de `datetime.date` en el límite del dominio en lugar de aceptar silenciosamente subclases `datetime.datetime`.

El informe agrupa actividades por fecha calendario, por lo que aceptar valores con hora ampliaría el contrato sin necesidad.

## 8. Validación de identidad del origen

`activity_id` debe ser único en toda la colección proporcionada a una operación de informe.

Los IDs duplicados se rechazan antes del filtro de fechas.

Esto significa que un duplicado fuera del período también invalida el conjunto de origen.

La validez de identidad se considera una propiedad del origen, no un efecto secundario del período seleccionado.

## 9. Filtro inclusivo por período

`build_report(...)` valida el origen y luego conserva los registros donde:

```python
start_date <= record.occurred_on <= end_date
```

El informe resultante conserva:

```text
source_record_count
registros incluidos
```

A partir de esos valores también expone cuántos registros fueron excluidos sin perder visibilidad del tamaño original de la colección.

## 10. Orden determinista

Los registros incluidos se ordenan por:

```text
occurred_on
activity_id
```

Colecciones equivalentes producen el mismo orden aunque el llamador entregue los datos en una secuencia distinta.

Esto vuelve más confiables las pruebas, los diffs y los artefactos generados.

## 11. Métricas de resumen

`summarize_activities(...)` calcula:

- total de registros;
- completados;
- en progreso;
- bloqueados;
- duración total;
- duración promedio;
- mayor duración;
- porcentaje de finalización;
- conteo por equipo.

El resumen se representa con `ReportSummary`, no con un diccionario sin estructura.

## 12. Redondeo exacto a dos decimales

La duración promedio y el porcentaje de finalización usan valores `Decimal` con dos decimales.

El proyecto calcula unidades enteras escaladas y aplica redondeo half-up de forma explícita.

Por ejemplo:

```text
31 minutos / 3 registros -> 10.33
2 completados / 3 total  -> 66.67%
3 minutos / 8 registros  -> 0.38
```

El cálculo no depende del contexto decimal global del llamador.

## 13. Por qué no usar float para estas métricas

El punto flotante binario es excelente para muchos cálculos científicos y generales, pero las métricas de presentación con decimales suelen necesitar una política de redondeo visible.

Este proyecto hace explícita esa política para que el informe no dependa de contexto numérico oculto.

## 14. Agrupación por equipo

La comparación de nombres de equipo no distingue mayúsculas y minúsculas.

Estos registros:

```text
Accounting
accounting
```

pertenecen al mismo grupo lógico.

La primera grafía aceptada se convierte en el nombre de visualización y los grupos finales se ordenan sin distinguir mayúsculas/minúsculas.

## 15. Períodos sin registros

Un informe sin registros incluidos sigue siendo válido.

Su resumen contiene:

```text
total de registros: 0
todos los estados: 0
duración total: 0
duración promedio: 0.00
mayor duración: 0
finalización: 0.00%
conteo por equipo: vacío
```

Ambos renderizadores muestran un estado vacío explícito en lugar de fallar por división entre cero o producir una sección ambigua.

## 16. Invariantes del resumen

`ReportSummary` valida su constructor público.

Entre sus comprobaciones:

- los conteos de estado deben sumar el total;
- los campos de duración no pueden ser negativos;
- el promedio debe coincidir con la duración total y el número de registros;
- el porcentaje de finalización debe coincidir con completados y total;
- la mayor duración debe ser matemáticamente posible;
- los nombres de equipo deben estar normalizados;
- los equipos deben ser únicos sin distinguir mayúsculas/minúsculas;
- los equipos deben estar ordenados de forma determinista;
- los conteos por equipo deben sumar el total.

El resumen es, por tanto, más que una bolsa de números.

## 17. Límite inmutable del informe

`OperationalReport` combina:

```text
ReportWindow
source_record_count
tupla de ActivityRecord incluidos
ReportSummary
```

Valida que los registros incluidos estén ordenados, tengan IDs únicos y pertenezcan a la ventana solicitada.

La frontera pública usa tuplas para no exponer listas internas mutables.

## 18. Construcción frente a presentación

`build_report(...)` no decide si el documento final será TXT o Markdown.

Esa separación permite renderizar el mismo informe de varias maneras:

```python
report = build_report(...)

text = render_report(report, ReportFormat.TEXT)
markdown = render_report(report, ReportFormat.MARKDOWN)
```

El resultado de negocio no necesita recalcularse para cada formato de presentación.

## 19. Renderizador de texto plano

`render_text_report(...)` produce un documento amigable para CLI con:

```text
título
período
conteos de origen/incluidos/excluidos
resumen
conteos por equipo
detalles ordenados de registros
```

La salida termina con exactamente un salto de línea para mantener estables las comparaciones de archivos.

## 20. Renderizador Markdown

`render_markdown_report(...)` produce:

- un título de nivel uno;
- una línea de período;
- una tabla de resumen;
- conteos por equipo;
- una tabla de registros.

El mismo contenido se expresa mediante otra capa de presentación, sin duplicar la lógica de agregación.

## 21. Escape de delimitadores Markdown

Los nombres de equipo pueden contener barra vertical (`|`) o barra invertida.

Como `|` tiene significado estructural dentro de tablas Markdown, el renderizador escapa primero las barras invertidas y luego los delimitadores de tabla.

Es un ejemplo pequeño pero importante de adaptar texto válido del dominio a la sintaxis de un formato de salida.

## 22. Selección explícita de formato

El renderizador genérico acepta únicamente:

```python
ReportFormat.TEXT
ReportFormat.MARKDOWN
```

Una cadena como `"text"` es rechazada.

Después de validar, el programa trabaja con valores explícitos en lugar de reinterpretar configuración cruda repetidamente.

## 23. Contrato de extensión de archivo

`write_report(...)` exige que la extensión corresponda al formato:

```text
ReportFormat.TEXT     -> .txt
ReportFormat.MARKDOWN -> .md
```

La comparación no distingue mayúsculas/minúsculas, por lo que `REPORT.TXT` es válido para texto.

Una extensión ausente o incompatible se rechaza antes de escribir.

## 24. Salida UTF-8

Los informes se escriben con:

```python
encoding="utf-8"
newline="\n"
```

Esto hace visible el contrato de archivo y mantiene el texto generado consistente entre entornos compatibles.

## 25. No se crean directorios ausentes

Este proyecto escribe un archivo solicitado, pero deliberadamente **no** crea directorios padre inexistentes.

Si el directorio no existe, se propaga el `FileNotFoundError` normal.

El descubrimiento, creación, movimiento y organización de directorios pertenecen al siguiente proyecto: **File Organizer**.

## 26. Estructura del proyecto

```text
05-report-generator/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── report_generator.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_report_generator.py
```

## 27. Ejecutar la demostración determinista

Desde la raíz del repositorio:

```bash
python practical-projects/05-report-generator/demo.py
```

Inicio esperado de la salida:

```text
August Operations
=================
period: 2026-08-01 to 2026-08-31
source records: 4
included records: 3
excluded records: 1

SUMMARY
completed: 1
in progress: 1
blocked: 1
completion: 33.33%
```

El cuarto registro ficticio está fuera de agosto, haciendo visible la diferencia entre origen y registros incluidos.

## 28. Ejecutar las pruebas del proyecto

```bash
python -m pytest -q practical-projects/05-report-generator/tests
```

La suite inicial contiene **70 escenarios pytest** que cubren validación del modelo inmutable, normalización de texto, límites de enums, reglas de ventana de fechas, IDs duplicados, agregación, redondeo a dos decimales, agrupación sin distinguir mayúsculas/minúsculas, informes vacíos, orden determinista, invariantes del resumen, renderización TXT, renderización y escape Markdown, selección de renderizador, validación de extensión, escritura UTF-8 y fallos del filesystem.

## 29. Rutas de fallo para inspeccionar manualmente

Prueba con:

```text
activity_id = 0
activity_id duplicado
equipo vacío
status = "completed" en vez de WorkStatus.COMPLETED
duración negativa
datetime en vez de date
start_date posterior a end_date
formato = "text" en vez de ReportFormat.TEXT
Markdown escrito en report.txt
directorio de destino inexistente
```

Observa si el problema pertenece al registro, a la ventana, a la colección de origen, al renderizador o a la frontera del filesystem.

## 30. Nota de diseño: un resumen, varios renderizadores

Un error común en informes es mezclar cálculos directamente con el código de presentación.

Eso hace que cada nuevo formato repita lógica de negocio.

Aquí se construye un único modelo validado de informe y cada renderizador solo traduce ese modelo a su propia sintaxis.

## 31. Nota de diseño: validar antes de filtrar

Los IDs duplicados se verifican antes de aplicar el período.

Es deliberado.

Si la corrección del origen dependiera del filtro de fechas, el mismo conjunto podría considerarse válido en un informe e inválido en otro solo porque un duplicado quedó fuera del período.

## 32. Nota de diseño: un informe es una frontera

Un informe no es solamente una cadena.

Conecta:

```text
datos de dominio
reglas de agregación
reglas de orden
sintaxis de presentación
salida al filesystem
```

Mantener esas etapas explícitas facilita las pruebas y la evolución.

## 33. Lo que este proyecto no incluye intencionalmente

Esta versión no incluye:

- parsing de CSV;
- libros de Excel;
- pandas;
- gráficos o dashboards;
- generación de PDF;
- plantillas HTML;
- envío por correo electrónico;
- creación automática de directorios;
- manejo de colisiones de nombres de archivo;
- organización recursiva del filesystem;
- persistencia en base de datos;
- formato de fechas/números sensible a locale;
- interfaz gráfica.

Estas funciones son útiles, pero diluirían la lección de informes o anticiparían proyectos posteriores.

## 34. Desafío de extensión: renderizador JSON

Añade `ReportFormat.JSON` y renderiza el informe como JSON estructurado.

Decide si fechas y enums deben convertirse en cadenas en la frontera de renderización y prueba el orden determinista de claves cuando sea relevante.

## 35. Desafío de extensión: métricas agrupadas por equipo

Amplía cada resumen de equipo para incluir:

```text
cantidad de registros
duración total
duración promedio
porcentaje de finalización
```

Considera si un modelo inmutable dedicado `TeamSummary` resulta más claro que tuplas anidadas.

## 36. Desafío de extensión: sección de detalle opcional

Permite solicitar un informe solo de resumen.

Mantén sin cambios el cálculo del informe y decide si la opción de mostrar detalles pertenece al modelo del informe o únicamente a la configuración del renderizador.

## 37. Discusión de portafolio

Al presentar este proyecto, explica más que “escribe un informe”.

Puntos útiles de ingeniería incluyen:

- registros de origen inmutables y validados;
- ventanas inclusivas explícitas;
- validación de identidad a nivel del conjunto de datos;
- filtrado y orden deterministas;
- redondeo decimal explícito para métricas de presentación;
- agrupación sin distinguir mayúsculas/minúsculas con nombres de visualización estables;
- invariantes del resumen;
- separación entre construcción y renderización;
- varios formatos desde un mismo resultado de dominio;
- escape específico del formato;
- contratos explícitos de UTF-8 y extensión de archivo;
- límites deliberados de alcance antes de File Organizer.

## 38. Lista de revisión

Antes de considerar completa tu implementación, verifica:

- ¿Los registros de origen se validan antes de generar el informe?
- ¿Se evita que valores Booleanos se hagan pasar por enteros?
- ¿Los IDs duplicados se rechazan antes del filtro de fechas?
- ¿Ambas fechas límite son inclusivas?
- ¿Los registros incluidos se ordenan de forma determinista?
- ¿Los conteos de estado suman el total?
- ¿El redondeo de duración promedio es explícito y estable?
- ¿El porcentaje de finalización es determinista?
- ¿Los equipos se agrupan sin distinguir mayúsculas/minúsculas y se ordenan de forma estable?
- ¿El informe usa colecciones públicas inmutables?
- ¿El mismo informe puede renderizarse sin recalcular métricas?
- ¿Se escapan los delimitadores de tablas Markdown?
- ¿Cada formato exige su extensión correspondiente?
- ¿UTF-8 y los saltos de línea son explícitos?
- ¿Los directorios ausentes quedan bajo responsabilidad del llamador o del siguiente proyecto?
- ¿Todos los ejemplos son ficticios y seguros para publicación?

## 39. Siguiente proyecto

El Proyecto 05 transforma registros validados en artefactos de informe deterministas manteniendo separadas la agregación, la renderización y la persistencia.

A continuación, **Proyecto 06: File Organizer** desplaza el foco desde el contenido de un único archivo hacia flujos controlados del filesystem: descubrir archivos, clasificarlos, planificar movimientos, manejar colisiones y mantener las operaciones seguras y comprobables.
