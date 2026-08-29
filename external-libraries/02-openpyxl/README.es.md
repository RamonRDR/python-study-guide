<div align="center">

# Automatizando Libros de Excel con `openpyxl`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Bibliotecas Externas](../README.es.md) · [← Anterior: `pandas`](../01-pandas/README.es.md)

`pandas` trata los datos similares a hojas de cálculo principalmente como tablas. `openpyxl` trabaja en otra capa: el propio libro de Excel. Permite que Python cree, inspeccione, edite, formatee y guarde libros Office Open XML conservando conceptos como hojas, celdas, fórmulas, estilos, tablas, validaciones, gráficos y configuración de impresión.

Este capítulo apunta a **openpyxl 3.1.x** y fue investigado con la documentación actual de la serie 3.1 y el paquete estable **openpyxl 3.1.5** publicado en PyPI. PyPI declara Python 3.8 o superior; este repositorio valida los ejemplos en Python 3.13.

**Tiempo estimado de estudio:** 240–330 minutos.

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- explicar cuándo `openpyxl` encaja mejor que `pandas` o el módulo estándar `csv`;
- crear, cargar, inspeccionar y guardar libros `.xlsx`;
- trabajar de forma segura con hojas, celdas, rangos e iteración por filas;
- distinguir fórmulas de valores calculados;
- entender qué significan realmente `data_only`, `read_only`, `write_only` y `keep_vba`;
- aplicar estilos reutilizables, formatos numéricos, dimensiones y paneles congelados;
- crear tablas, reglas de validación, filtros, comentarios, hipervínculos y gráficos;
- comprender los límites de celdas combinadas, movimiento de filas/columnas, traducción de fórmulas, preservación de VBA y fidelidad de round-trip;
- elegir modos optimizados para libros grandes;
- tratar archivos de hoja de cálculo como entrada externa con límites explícitos de seguridad y validación;
- combinar `pandas` y `openpyxl` sin confundir sus responsabilidades;
- construir automatizaciones deterministas de libros que puedan revisarse y probarse sin Microsoft Excel instalado.

## 1. Por qué existe `openpyxl`

Los libros de Excel contienen más que datos rectangulares. Pueden contener varias hojas, fórmulas, formato, tablas, reglas de validación, regiones combinadas, gráficos, comentarios, hipervínculos, configuración de impresión y metadatos del libro.

`openpyxl` es una biblioteca Python de terceros para leer y escribir archivos de hoja de cálculo Office Open XML, como `.xlsx` y `.xlsm`.

Úsala cuando la **estructura del libro en sí importa**.

## 2. `pandas` y `openpyxl` resuelven problemas diferentes

Una distinción útil es:

```text
pandas   -> manipulate tabular data
openpyxl -> manipulate Excel workbook structure
```

Si necesitas agrupar diez millones de filas, `pandas` suele ser una abstracción más fuerte. Si necesitas establecer `B2` como fórmula, congelar la primera fila, aplicar un formato numérico, crear una tabla de Excel o conservar el diseño del libro, `openpyxl` es la capa más natural.

Muchos flujos reales usan ambos.

## 3. Las bibliotecas externas requieren un contrato de dependencias

El repositorio declara las dependencias ejecutables de la Fase 9 en `requirements-external.txt`.

Para este capítulo, el contrato es:

```text
openpyxl >= 3.1 and < 3.2
```

Fijar una serie minor compatible evita enseñar silenciosamente contra una API futura desconocida y permite releases de patch compatibles.

## 4. Instala la dependencia en un entorno aislado

Crea un entorno virtual:

```bash
python -m venv .venv
```

Actívalo según tu sistema operativo e instala el contrato del repositorio:

```bash
python -m pip install -r requirements-external.txt
```

Un `pip install openpyxl` directo es válido para experimentar, pero un archivo de dependencias hace reproducible el entorno del proyecto.

## 5. Conoce los formatos de libro dentro del alcance

`openpyxl` está diseñado alrededor de formatos Office Open XML como:

```text
.xlsx
.xlsm
.xltx
.xltm
```

No es un lector general para todos los archivos que Excel puede abrir. En particular, los archivos binarios heredados `.xls` y los libros `.xlsb` son formatos diferentes y requieren otras herramientas.

Trata la extensión como parte del contrato de entrada.

## 6. Crea un libro

La clase central es `Workbook`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
print(worksheet.title)
```

```text
Sheet
```

Un libro normal nuevo comienza con una hoja activa.

## 7. Da nombres significativos a las hojas

Renombra la hoja activa o crea hojas adicionales explícitamente:

```python
from openpyxl import Workbook


workbook = Workbook()
summary = workbook.active
summary.title = "Summary"
details = workbook.create_sheet("Details")
print(workbook.sheetnames)
```

```text
['Summary', 'Details']
```

Los nombres de hojas forman parte de la navegación del libro y también pueden aparecer en fórmulas y nombres definidos.

## 8. Selecciona una hoja por nombre

Usa acceso similar a un mapeo:

```python
from openpyxl import Workbook


workbook = Workbook()
workbook.active.title = "Summary"
worksheet = workbook["Summary"]
print(worksheet.title)
```

Evita depender de la posición física de una hoja cuando su nombre es el contrato real.

## 9. Las celdas usan coordenadas estilo Excel

Las celdas pueden accederse con coordenadas como `A1`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = "status"
worksheet["B1"] = "ready"
print(worksheet["B1"].value)
```

```text
ready
```

Las coordenadas son convenientes cuando el diseño del libro es fijo y significativo.

## 10. `cell()` usa índices de fila y columna desde uno

La generación programática suele encajar mejor con `Worksheet.cell()`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.cell(row=2, column=3, value=42)
print(worksheet["C2"].value)
```

```text
42
```

Las filas y columnas de Excel se indexan desde uno en esta API.

## 11. Acceder a celdas puede crearlas en memoria

Una hoja normal crea objetos de celda cuando se acceden por primera vez. Por eso, un bucle sobre un rango gigantesco e innecesario puede asignar muchas celdas incluso sin guardar datos útiles.

No recorras un rectángulo de un millón por un millón solo para descubrir qué celdas existen.

Usa rangos conocidos, dimensiones de hoja o lectura optimizada cuando corresponda.

## 12. Agrega filas completas con `append()`

Para salida orientada a filas, `append()` suele ser más claro que asignar cada coordenada:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["item", "quantity"])
worksheet.append(["Cable", 3])
worksheet.append(["Adapter", 2])
print(worksheet.max_row)
```

```text
3
```

Funciona bien para exportaciones construidas registro por registro.

## 13. Itera filas en lugar de codificar cada celda

`iter_rows()` expone una región rectangular:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["name", "score"])
worksheet.append(["A", 8])
worksheet.append(["B", 9])

for row in worksheet.iter_rows(min_row=2, values_only=True):
    print(row)
```

```text
('A', 8)
('B', 9)
```

`values_only=True` devuelve valores Python en lugar de objetos `Cell` cuando no necesitas metadatos de celda.

## 14. Itera columnas solo cuando el patrón de acceso lo necesite

Las hojas normales también admiten `iter_cols()`. La iteración por filas suele ser más natural para datos tipo registro, mientras la iteración por columnas sirve cuando la regla del libro está orientada a una columna.

El modo read-only optimizado tiene una API más limitada, así que no diseñes todo el flujo alrededor de métodos que allí no existen.

## 15. Las dimensiones de hoja son una pista, no una regla de negocio

Propiedades como `max_row`, `max_column` y `calculate_dimension()` describen la región aparentemente usada.

No prueban que cada celda dentro de esa región contenga datos significativos.

Celdas vacías pero formateadas, metadatos antiguos o generadores de terceros pueden hacer que las dimensiones sean mayores o menores de lo esperado.

## 16. Guarda deliberadamente en una ruta nueva

Un libro se persiste con `save()`:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from openpyxl import Workbook


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "report.xlsx"
    workbook = Workbook()
    workbook.active["A1"] = "ready"
    workbook.save(path)
    print(path.exists())
```

```text
True
```

En automatizaciones de producción, prefiere una ruta de salida deliberada antes que sobrescribir casualmente el libro fuente.

## 17. Carga un libro existente

Usa `load_workbook()`:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from openpyxl import Workbook, load_workbook


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "input.xlsx"
    workbook = Workbook()
    workbook.active["A1"] = "loaded"
    workbook.save(path)

    reloaded = load_workbook(path)
    print(reloaded.active["A1"].value)
    reloaded.close()
```

```text
loaded
```

Cerrar explícitamente es especialmente importante para libros read-only y es un buen hábito para recursos respaldados por archivos.

## 18. Un round-trip puede perder características no soportadas

Abrir un libro complejo y guardarlo otra vez no garantiza conservar cada artefacto creado por Excel u otra aplicación.

El tutorial oficial advierte que openpyxl no lee todos los elementos posibles de un libro y que algunas shapes pueden perderse durante un round-trip load/save.

Por lo tanto:

```text
load -> edit one cell -> save
```

no es automáticamente una transformación sin pérdidas para cualquier libro.

## 19. `read_only=True` es un modo de operación diferente

Los libros grandes pueden consumir mucha memoria. El modo read-only transmite el contenido de la hoja de forma lazy:

```python
from openpyxl import load_workbook


workbook = load_workbook("large.xlsx", read_only=True, data_only=True)
worksheet = workbook["Data"]
for row in worksheet.iter_rows(values_only=True):
    process = row
workbook.close()
```

El ejemplo es intencionalmente ilustrativo y no ejecutable en el repositorio porque depende de un archivo externo.

Las hojas read-only no son hojas editables normales.

## 20. El modo read-only debe cerrarse explícitamente

La documentación oficial de modos optimizados destaca `close()` para libros read-only.

Usa un límite `try/finally` cuando el procesamiento posterior pueda fallar:

```python
from openpyxl import load_workbook


workbook = load_workbook("large.xlsx", read_only=True)
try:
    worksheet = workbook.active
    for row in worksheet.iter_rows(values_only=True):
        process = row
finally:
    workbook.close()
```

La liberación de recursos debe sobrevivir a excepciones.

## 21. Las dimensiones en read-only pueden ser incorrectas

La lectura lazy depende de metadatos de dimensión almacenados en el libro. Algunas aplicaciones productoras escriben esos datos de forma incorrecta.

La documentación recomienda revisar `calculate_dimension()` y, cuando sabes que el metadato está mal, usar `reset_dimensions()` sobre una hoja read-only.

Hazlo solo cuando exista una razón externa para saber que las dimensiones guardadas son incorrectas.

## 22. `write_only=True` está optimizado para salida en streaming

Los libros write-only se crean de forma diferente:

```python
from openpyxl import Workbook


workbook = Workbook(write_only=True)
worksheet = workbook.create_sheet("Data")
worksheet.append(["id", "value"])
worksheet.append([1, 10])
worksheet.append([2, 20])
```

A diferencia de un `Workbook()` normal, un libro write-only empieza sin hojas. Debes crear una explícitamente.

## 23. El modo write-only está orientado a `append()`

Una hoja write-only está diseñada para salida secuencial. Las filas se agregan con `append()` en vez de lectura y escritura arbitraria de celdas.

Es una buena opción para grandes exportaciones donde los registros llegan en orden y no necesitas volver a editar filas antiguas.

## 24. Un libro write-only solo puede guardarse una vez

La documentación de modos optimizados establece que un libro write-only puede guardarse una sola vez.

El flujo debe ser:

```text
configure workbook -> append rows -> save once
```

y no:

```text
save -> append more -> save again
```

Configura todo lo que deba aparecer antes de los datos antes de empezar el streaming de filas.

## 25. Elige conscientemente entre normal, read-only y write-only

| Necesidad | Prefiere |
|---|---|
| editar celdas arbitrarias | libro normal |
| inspeccionar estilos, gráficos, imágenes y estructura completa | libro normal |
| transmitir una hoja existente muy grande | `read_only=True` |
| transmitir una exportación nueva muy grande | `Workbook(write_only=True)` |
| guardar repetidamente mientras editas | libro normal |

Los modos optimizados intercambian capacidades por menor uso de memoria.

## 26. Los valores Python se convierten en valores de celda

Las celdas pueden almacenar valores Python comunes como strings, números, booleanos, fechas, datetimes y fórmulas representadas como strings que empiezan con `=`.

Mantén separada la validación de dominio. Que un valor pueda almacenarse en una celda no significa que sea válido para tu aplicación.

## 27. Las fechas son valores más formatos numéricos

Excel almacena valores de fecha/hora con semántica de fecha de hoja de cálculo y los muestra mediante formatos numéricos.

Al asignar un `datetime` de Python, openpyxl aplica automáticamente un formato compatible:

```python
from datetime import datetime

from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = datetime(2026, 8, 29, 14, 30)
print(worksheet["A1"].is_date)
```

```text
True
```

No trates el texto visible en Excel como la única representación relevante.

## 28. Excel tiene dos sistemas de fechas

Las fechas de hoja de cálculo pueden usar el sistema 1900 o 1904 según la configuración e historia del libro.

Deja que el libro y openpyxl administren la conversión en lugar de sumar manualmente un número fijo de días a valores seriales.

La aritmética manual de seriales facilita errores de época y desplazamiento.

## 29. Las fórmulas se almacenan como fórmulas

Asigna un string de fórmula que empiece con `=`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = 10
worksheet["A2"] = 20
worksheet["A3"] = "=SUM(A1:A2)"
print(worksheet["A3"].value)
```

```text
=SUM(A1:A2)
```

La celda contiene una expresión de fórmula, no un cálculo Python.

## 30. `openpyxl` no calcula fórmulas

Este es uno de los límites más importantes de la biblioteca.

`openpyxl` puede leer y escribir expresiones de fórmula, pero no es un motor de cálculo de Excel. Escribir `=SUM(A1:A2)` no hace que openpyxl calcule `30`.

Si tu flujo Python necesita el resultado en ese momento, calcula el valor en Python o usa un motor de cálculo separado con contrato documentado.

## 31. `data_only=True` lee resultados en caché

Al cargar un libro, `data_only` controla si las celdas con fórmula exponen la fórmula o el valor en caché dejado por la última aplicación de hoja de cálculo que calculó el libro.

```text
load_workbook(path, data_only=False) -> formula text
load_workbook(path, data_only=True)  -> cached result, if available
```

Un libro recién creado puede no tener ningún valor calculado en caché.

No confundas `data_only=True` con “calcular fórmulas ahora”.

## 32. Los nombres de funciones se escriben en inglés

La documentación de fórmulas de openpyxl indica que los nombres de funciones deben estar en inglés y los argumentos se separan con comas.

Por ejemplo:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = "=SUM(1,2,3)"
print(worksheet["A1"].value)
```

```text
=SUM(1,2,3)
```

No generes sintaxis localizada basándote en cómo Excel muestra fórmulas en una máquina concreta.

## 33. Los estilos son objetos del libro, no strings de apariencia

Componentes comunes incluyen:

```text
Font
PatternFill / GradientFill
Border
Alignment
Protection
number_format
```

El modelo es explícito porque la apariencia de una celda de Excel se compone de varias propiedades independientes.

## 34. Aplica fuente, relleno y alineación

```python
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill


workbook = Workbook()
worksheet = workbook.active
cell = worksheet["A1"]
cell.value = "Header"
cell.font = Font(bold=True)
cell.fill = PatternFill(fill_type="solid", fgColor="D9EAF7")
cell.alignment = Alignment(horizontal="center")
print(cell.font.bold)
```

```text
True
```

El formato debe comunicar estructura, no compensar datos poco claros.

## 35. Los estilos de celda son efectivamente inmutables después de asignarse

La documentación oficial explica que los componentes de estilo asignados se comparten y no pueden mutarse in-place.

Esto es deliberadamente inválido:

```text
a1.font.italic = True
```

Asigna un nuevo objeto `Font`:

```python
from openpyxl import Workbook
from openpyxl.styles import Font


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"].font = Font(color="FF0000")
worksheet["A1"].font = Font(color="FF0000", italic=True)
print(worksheet["A1"].font.italic)
```

```text
True
```

## 36. Reutiliza estilos en lugar de crear miles de variaciones

Si muchas celdas comparten el mismo rol visual, reutiliza la misma definición o un `NamedStyle`.

Crear objetos ligeramente distintos para cada celda puede inflar la tabla de estilos y el tamaño del archivo.

Trata los estilos como vocabulario controlado: encabezado, moneda, fecha, advertencia, entrada, salida.

## 37. Los formatos numéricos cambian la visualización, no el valor almacenado

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = 0.125
worksheet["A1"].number_format = "0.00%"
print(worksheet["A1"].value)
```

```text
0.125
```

Excel puede mostrar `12.50%`, pero el valor almacenado sigue siendo `0.125`.

La diferencia importa cuando otro programa lee el libro.

## 38. Los named styles hacen explícito el formato repetido

```python
from openpyxl import Workbook
from openpyxl.styles import Font, NamedStyle


workbook = Workbook()
worksheet = workbook.active
header = NamedStyle(name="header")
header.font = Font(bold=True)
workbook.add_named_style(header)
worksheet["A1"].style = "header"
print(worksheet["A1"].style)
```

```text
header
```

Una vez asignado un named style a una celda, cambios posteriores al `NamedStyle` no vuelven a estilizar esa celda de forma retroactiva.

## 39. El ancho de columna y la altura de fila son metadatos de diseño

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.column_dimensions["A"].width = 24
worksheet.row_dimensions[1].height = 30
print(worksheet.column_dimensions["A"].width)
```

```text
24.0
```

No supongas que openpyxl reproducirá el AutoFit interactivo de Excel solo a partir del contenido.

## 40. Freeze panes conserva contexto al desplazarse

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.freeze_panes = "A2"
print(worksheet.freeze_panes)
```

```text
A2
```

`A2` congela las filas por encima de la fila 2, manteniendo visible la primera fila.

## 41. Las celdas combinadas tienen una sola celda real de valor

Cuando se combina un rango, solo la celda superior izquierda es la celda normal que contiene valor. Las demás posiciones se convierten en placeholders de merged cell.

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.merge_cells("A1:C1")
worksheet["A1"] = "Quarterly report"
print(worksheet["A1"].value)
```

```text
Quarterly report
```

Las celdas combinadas son estructura de presentación, no sustituto de datos tabulares normalizados.

## 42. Insertar y eliminar no administra todas las dependencias

`insert_rows()`, `delete_rows()`, `insert_cols()` y `delete_cols()` pueden desplazar celdas.

La documentación oficial indica que openpyxl no administra todas las dependencias que puedan referenciar esas celdas, como fórmulas, tablas o gráficos.

Una edición estructural puede requerir lógica específica de la aplicación para reparar referencias.

## 43. `move_range()` puede traducir algunas fórmulas, no todas las referencias

`move_range(..., translate=True)` puede traducir fórmulas dentro de las celdas movidas.

Sin embargo, referencias a esas celdas desde otras celdas o nombres definidos no se actualizan automáticamente.

No confundas “celdas movidas” con “semántica del libro reparada”.

## 44. Las tablas de hoja agregan semántica de tabla de Excel

Una tabla de worksheet es más que un rango coloreado. Tiene nombre y una referencia de celdas definida:

```python
from openpyxl import Workbook
from openpyxl.worksheet.table import Table


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["item", "amount"])
worksheet.append(["A", 10])
worksheet.append(["B", 20])
table = Table(displayName="SalesTable", ref="A1:B3")
worksheet.add_table(table)
print(list(worksheet.tables.keys()))
```

```text
['SalesTable']
```

Las tablas son útiles cuando usuarios posteriores de Excel esperan referencias estructuradas y formato consciente de tabla.

## 45. Los nombres y encabezados de tabla son contratos

Los display names deben ser válidos y únicos dentro del namespace correspondiente. La documentación también requiere que los encabezados de las columnas sean strings.

Valida los encabezados antes de crear la tabla en lugar de depender de que Excel repare una salida defectuosa.

## 46. Los filtros describen comportamiento del libro; no filtran datos Python

Los auto filters pueden configurarse para que una aplicación de hoja de cálculo sepa qué filas mostrar según determinados criterios.

Eso es distinto de filtrar registros en Python antes de escribirlos.

Si un reporte debe contener físicamente solo filas aprobadas, filtra primero los datos Python. Si los usuarios necesitan filtrado interactivo en Excel, configura una tabla o auto filter como comportamiento de presentación.

## 47. Las reglas de validación se escriben, no se ejecutan por openpyxl

La documentación oficial es explícita: los validadores no son aplicados ni evaluados por openpyxl.

```python
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation


workbook = Workbook()
worksheet = workbook.active
validation = DataValidation(type="list", formula1='"open,closed"')
worksheet.add_data_validation(validation)
validation.add("A2:A20")
print(len(worksheet.data_validations.dataValidation))
```

```text
1
```

La regla pasa a ser metadato que Excel u otra aplicación compatible puede aplicar de forma interactiva.

## 48. El formato condicional también es comportamiento del libro

Las reglas de conditional formatting indican a una aplicación cómo formatear celdas cuando se cumplen condiciones.

No uses formato condicional como sustituto oculto de validación. Una celda roja puede comunicar un error a una persona, pero tu programa Python debe validar entradas críticas explícitamente.

## 49. Los gráficos referencian datos de hoja

`openpyxl.chart` puede construir gráficos a partir de rangos. Un flujo típico crea un chart, define objetos `Reference` para datos y categorías y ancla el gráfico en una hoja.

Los gráficos son objetos de presentación sobre datos. Prueba los números subyacentes por separado del diseño visual.

## 50. Las imágenes introducen una dependencia opcional de Pillow

La API de imágenes puede insertar imágenes raster en hojas, pero su manejo depende de Pillow.

Como el contrato ejecutable de este capítulo no necesita imágenes, Pillow no se agrega solo por un ejemplo decorativo.

Agrega dependencias opcionales únicamente cuando el proyecto realmente necesite la función.

## 51. Comentarios e hipervínculos son metadatos de celda

Las celdas pueden tener comentarios e hipervínculos además de valores y estilos.

Úsalos cuando aporten contexto útil a personas, pero conserva la información esencial legible por máquina en celdas normales o datos estructurados, no escondida en comentarios.

## 52. Los nombres definidos pueden representar referencias de libro

Los defined names de Excel pueden apuntar a celdas, rangos, constantes o fórmulas y pueden tener alcance de libro o de hoja.

Son útiles para contratos de workbook, pero crean otra capa de dependencia cuando se mueven celdas o se renombran hojas.

Inspecciona los nombres definidos antes de realizar ediciones estructurales en plantillas complejas.

## 53. La protección de hoja no es cifrado

La protección de celdas y hojas controla comportamiento de edición en la interfaz. No sustituye cifrado de archivos sensibles ni autorización del lado servidor.

Trata la protección del libro como una restricción de interfaz, no como una frontera de seguridad.

## 54. La configuración de impresión forma parte del producto

Orientación de página, márgenes, áreas de impresión, títulos repetidos y escala pueden importar cuando un `.xlsx` debe convertirse en PDF o imprimirse.

Para un libro de intercambio de datos puede ser irrelevante. Para un reporte humano, puede formar parte de los criterios de aceptación.

## 55. Entiende las flags importantes de `load_workbook()`

Flags comunes incluyen:

```text
read_only=True  -> lazy, lower-memory reading
data_only=True  -> cached formula results instead of formula text
keep_vba=True   -> preserve VBA content when possible
keep_links=True -> preserve cached external-link data
rich_text=True  -> preserve rich text formatting in cells
```

Cada flag modifica el contrato. No las actives solo porque parezcan más seguras o completas.

## 56. `keep_vba=True` preserva VBA; no permite editarlo

El tutorial oficial indica que los elementos VBA pueden preservarse, pero no son editables mediante openpyxl.

Si un `.xlsm` con macros debe hacer round-trip conservando VBA, usa la extensión correcta y `keep_vba=True`, y prueba el artefacto real.

Preservar no significa ejecutar, inspeccionar ni modificar.

## 57. Incompatibilidades entre plantilla y extensión pueden romper expectativas

Tipo de libro, extensión del archivo y configuración de VBA/template deben coincidir.

Guardar un libro con macros bajo una extensión incorrecta o ignorar el contrato VBA puede producir un archivo rechazado por Excel o que pierde funcionalidad silenciosamente.

Trata explícitamente los tipos de origen y destino.

## 58. Los libros no confiables son una frontera de seguridad

Un `.xlsx` es un paquete ZIP con XML y recursos relacionados. La página de openpyxl en PyPI advierte que openpyxl no protege por defecto contra ataques XML de quadratic blowup o billion laughs y recomienda `defusedxml`.

Para ejemplos confiables generados por el repositorio no es necesario. Para servicios que aceptan libros arbitrarios subidos por usuarios, el modelado de amenazas y el parsing XML endurecido forman parte del diseño.

## 59. Los archivos inválidos deben fallar de forma visible

`load_workbook()` puede rechazar archivos OOXML malformados o no conformes.

Captura excepciones solo cuando puedas agregar contexto útil y conserva la falla:

```python
from pathlib import Path
from zipfile import BadZipFile

from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException


def read_sheet_names(path: Path) -> list[str]:
    try:
        workbook = load_workbook(path, read_only=True)
    except (BadZipFile, InvalidFileException, OSError) as exc:
        raise RuntimeError(f"Could not open workbook: {path.name}") from exc

    try:
        return workbook.sheetnames
    finally:
        workbook.close()
```

No conviertas todos los errores de libro en un reporte vacío.

## 60. Prefiere validar la salida a aceptar solo “save funcionó”

Un `save()` exitoso demuestra que se escribieron bytes. No demuestra que el libro cumpla el contrato de negocio o presentación.

Comprobaciones útiles después de guardar incluyen:

```text
file exists
expected sheet names exist
required cells contain expected values or formulas
expected table names exist
expected validations exist
critical number formats/styles are present
workbook reopens successfully
```

Para plantillas importantes, abre también el artefacto generado en la aplicación objetivo durante las pruebas de aceptación.

## 61. Ejemplo: crea un libro y conserva una fórmula

[`examples/workbook_basics.py`](examples/workbook_basics.py) crea un libro temporal, añade filas y fórmulas, guarda, vuelve a cargar con fórmulas visibles y verifica la estructura.

Salida esperada:

```text
sheet: Summary
rows: 3
formula: =B2*C2
```

El ejemplo prueba lo que openpyxl realmente controla: texto de fórmula y estructura del libro, no su cálculo.

## 62. Ejemplo: transmite filas de un libro

[`examples/load_and_iterate.py`](examples/load_and_iterate.py) escribe un libro pequeño, lo reabre con `read_only=True`, itera valores y calcula un total en Python.

Salida esperada:

```text
orders: 3
total: 100.00
```

Esto separa deliberadamente lectura de libro de cálculo de negocio.

## 63. Ejemplo: crea un reporte con estilo

[`examples/styled_report.py`](examples/styled_report.py) aplica tratamiento reutilizable de encabezado, formato numérico, freeze pane y anchos de columna, después recarga el libro para verificar metadatos persistidos.

Salida esperada:

```text
header bold: True
number format: #,##0.00
freeze panes: A2
```

Una prueba determinista puede inspeccionar metadatos sin abrir Excel.

## 64. Ejemplo: tablas y reglas de validación

[`examples/table_and_validation.py`](examples/table_and_validation.py) crea una tabla de Excel y una validación por lista, guarda, recarga y verifica que ambas estructuras existan.

Salida esperada:

```text
tables: ['CatalogTable']
validations: 1
```

Recuerda que la regla de validación se almacena, no se ejecuta, por openpyxl.

## 65. Ejemplo: exportación write-only

[`examples/write_only_export.py`](examples/write_only_export.py) transmite filas a un libro write-only, guarda una sola vez y luego reabre el resultado en modo read-only para verificarlo.

Salida esperada:

```text
rows: 3
sum: 60
```

Esto modela el ciclo de vida de una gran exportación secuencial sin necesitar un fixture enorme.

## 66. Errores comunes, guía de decisión, ejercicio y referencias

Evita estos errores:

- usar `openpyxl` para análisis tabular pesado que corresponde a `pandas`;
- esperar soporte `.xls` o `.xlsb` de una biblioteca `.xlsx`;
- asumir que `data_only=True` recalcula fórmulas;
- sobrescribir un libro fuente complejo antes de verificar fidelidad de round-trip;
- usar dimensiones como prueba de datos válidos;
- usar modo normal para cargas enormes sin considerar memoria;
- olvidar cerrar libros read-only;
- guardar un libro write-only más de una vez;
- mutar estilos asignados in-place;
- crear miles de variantes de estilo casi idénticas;
- confundir formatos numéricos con valores almacenados;
- asumir que inserciones de filas/columnas reparan fórmulas, tablas, gráficos y nombres definidos;
- esperar que data validation sea ejecutada por openpyxl;
- tratar protección de hoja como seguridad;
- preservar VBA sin probar el artefacto `.xlsm`;
- aceptar libros no confiables sin estrategia de seguridad XML;
- considerar `save()` por sí solo como verificación suficiente.

### Tabla de decisión

| Necesidad | Prefiere |
|---|---|
| filtrar/agrupar/unir datos | `pandas` |
| intercambio simple CSV | `csv` o `pandas` |
| crear/editar estructura `.xlsx` | `openpyxl` |
| editar celdas arbitrarias | libro normal |
| lectura secuencial grande | `read_only=True` |
| escritura secuencial grande | `Workbook(write_only=True)` |
| texto de fórmula | carga normal / `data_only=False` |
| valor de fórmula en caché | `data_only=True` |
| preservar contenedor VBA | `keep_vba=True` + contrato `.xlsm` |
| formato repetido | estilos reutilizados / `NamedStyle` |
| validación interactiva Excel | `DataValidation` |
| validación de máquina | validación Python antes de escribir |

### Referencia rápida

```text
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws = wb["SheetName"]
wb.create_sheet("Details")

ws["A1"] = "value"
ws.cell(row=1, column=1, value="value")
ws.append([...])
ws.iter_rows(values_only=True)

wb.save(path)
wb = load_workbook(path)
wb = load_workbook(path, read_only=True, data_only=True)
wb.close()

ws.freeze_panes = "A2"
ws.column_dimensions["A"].width = 20
ws["B2"].number_format = "#,##0.00"

ws.merge_cells("A1:C1")
ws.unmerge_cells("A1:C1")

ws.add_table(...)
ws.add_data_validation(...)
```

### Checklist de diseño

Antes de aceptar una automatización de libro, pregunta:

- ¿Qué formatos están permitidos?
- ¿El archivo es confiable o subido por usuarios?
- ¿Los artefactos no soportados deben sobrevivir al round-trip?
- ¿Se puede sobrescribir la fuente?
- ¿Qué hojas, celdas, tablas y nombres forman el contrato?
- ¿Las fórmulas necesitan texto o valor calculado?
- ¿Quién es responsable del cálculo?
- ¿Los valores en caché son suficientemente recientes?
- ¿Conviene modo normal, read-only o write-only?
- ¿Los recursos del libro se cierran?
- ¿Los estilos se reutilizan intencionalmente?
- ¿Los formatos numéricos están separados de los valores almacenados?
- ¿Las ediciones estructurales pueden romper referencias?
- ¿Las reglas de validación son solo UI o validación real de negocio?
- ¿Debe preservarse VBA?
- ¿La salida vuelve a abrirse correctamente?
- ¿Se verifican estructuras críticas después de guardar?

### Ejercicio

Construye un libro ficticio de operaciones mensuales:

1. Crea un `.xlsx` con hojas `Summary` y `Transactions`.
2. Agrega una fila de encabezado y al menos diez transacciones ficticias.
3. Usa valores Python `date` o `datetime` explícitos para fechas.
4. Agrega una fórmula Excel en la hoja de resumen.
5. Explica por qué la prueba debe verificar el texto de fórmula en vez de esperar que openpyxl la calcule.
6. Formatea celdas monetarias con number format.
7. Reutiliza un estilo de encabezado en lugar de inventar formato por celda.
8. Congela la fila de encabezado de transacciones.
9. Crea una tabla Excel sobre los datos.
10. Agrega una validación por lista a una columna de estado.
11. Guarda en una ruta nueva.
12. Reabre y verifica nombres de hojas, texto de fórmula, nombre de tabla, cantidad de validaciones y un estilo crítico.
13. Agrega una función read-only que calcule un total Python a partir de las filas guardadas.
14. Haz visibles los fallos con contexto útil.

Desafíos adicionales:

- crea un gráfico con los valores del resumen;
- agrega un nombre definido e inspecciónalo tras recargar;
- compara diseños de export normal y write-only;
- procesa un `DataFrame` de pandas y usa openpyxl solo para la capa de presentación;
- diseña una prueba segura de round-trip `.xlsm` con `keep_vba=True` sin intentar editar el proyecto VBA.

### Conexiones con conceptos anteriores

`openpyxl` se apoya directamente en material previo:

- **funciones y módulos:** aislar generación y validación;
- **excepciones:** informar entradas malformadas o incompatibles;
- **`pathlib`:** modelar rutas de origen y destino;
- **fechas:** almacenar valores temporales Python con formatos de hoja;
- **`decimal`:** decidir cómo valores monetarios exactos cruzan hacia celdas numéricas de Excel;
- **`logging`:** registrar rutas, nombres de hojas, conteos y fallos sin ocultar excepciones;
- **`os` y `shutil`:** descubrir, preparar, copiar y archivar libros con seguridad;
- **`pandas`:** transformar datos tabulares antes de que openpyxl construya la presentación final.

### Referencias primarias

- [documentación de openpyxl](https://openpyxl.readthedocs.io/)
- [tutorial de openpyxl](https://openpyxl.readthedocs.io/en/stable/tutorial.html)
- [Optimised Modes](https://openpyxl.readthedocs.io/en/stable/optimized.html)
- [Working with styles](https://openpyxl.readthedocs.io/en/stable/styles.html)
- [Worksheet tables](https://openpyxl.readthedocs.io/en/stable/worksheet_tables.html)
- [Data validation](https://openpyxl.readthedocs.io/en/stable/validation.html)
- [Worksheet editing](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html)
- [openpyxl en PyPI](https://pypi.org/project/openpyxl/)

Cuando se preparó este capítulo, PyPI listaba openpyxl 3.1.5 como la release estable más reciente. El currículo apunta a la serie 3.1.x en lugar de depender de una versión futura sin límite.

## 67. Próximo capítulo

La Fase 9 ahora tiene dos capas prácticas de datos/libro:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
```

La próxima biblioteca planificada es **`requests`**, donde la frontera pasa de archivos locales a servicios HTTP y APIs.

Antes de continuar, practica generando libros que puedas inspeccionar manualmente y validar automáticamente. La automatización de hojas de cálculo se vuelve confiable cuando tanto el contrato de datos como el contrato del workbook son explícitos.
