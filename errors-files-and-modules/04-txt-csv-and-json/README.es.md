<div align="center">

# Trabajar con TXT, CSV y JSON

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Errores, Archivos y Módulos](../README.es.md) · [← Anterior: Abrir Archivos de Forma Segura con `open()` y `with`](../03-open-and-with/README.es.md)

Abrir un archivo de forma segura es solo la mitad del trabajo. Un programa también necesita comprender **cómo están organizados los datos dentro de ese archivo**.

Un archivo `.txt` puede contener un registro por línea, un CSV puede representar filas y columnas y un documento JSON puede representar objetos y arrays anidados. La extensión es una pista útil, pero el contrato real es el formato de los datos y las reglas usadas para interpretarlos.

Este capítulo introduce registros de texto simple, el módulo `csv` de Python y el módulo `json` de Python. El objetivo no es memorizar todas las opciones. El objetivo es elegir un formato deliberadamente, usar el parser responsable de ese formato y mantener el parsing separado de la validación y la lógica de la aplicación.

**Tiempo estimado de estudio:** 120–160 minutos.

**Requisito de Python:** Python 3.10 o posterior. El comportamiento de `csv` y `json` enseñado aquí se verificó con la documentación oficial de Python 3.14.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar la diferencia entre una extensión de archivo y un formato de datos;
- usar texto simple cuando un contrato orientado a líneas sea suficiente;
- explicar por qué CSV no debe analizarse con un `split(",")` ingenuo;
- leer y escribir filas CSV con el módulo `csv` de la biblioteca estándar;
- usar `DictReader` y `DictWriter` cuando las columnas con nombre mejoren la claridad;
- explicar por qué los valores CSV normalmente llegan como strings y convertirlos deliberadamente;
- abrir archivos CSV con `newline=""` y una codificación de texto conocida;
- distinguir objetos, arrays, strings, números, booleanos y `null` en JSON;
- usar correctamente `json.load()`, `json.loads()`, `json.dump()` y `json.dumps()`;
- manejar JSON no válido con `json.JSONDecodeError` cuando exista una recuperación significativa;
- distinguir parsing de validación;
- elegir TXT, CSV o JSON según la forma y el contrato de los datos;
- evitar parsers hechos a mano cuando ya existe un parser específico del formato.

## 1. Un archivo es un contenedor; un formato es un contrato

El Capítulo 03 se centró en abrir, leer, escribir y cerrar archivos. Este capítulo añade otra pregunta:

```text
bytes en almacenamiento
      ↓ decodificación
texto en Python
      ↓ parsing
valores Python estructurados
      ↓ validación
valores en los que el programa confía
```

Abrir un archivo responde **de dónde vienen los datos**. Hacer parsing responde **qué significa el texto**.

Son responsabilidades relacionadas, pero no son la misma responsabilidad.

## 2. La extensión no interpreta mágicamente el contenido

Un nombre como `topics.txt`, `scores.csv` o `profile.json` comunica intención a personas y herramientas. Python no inspecciona automáticamente la extensión y transforma el contenido en la estructura correspondiente.

Tú eliges la operación apropiada:

```python
with open("topics.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

o un parser específico del formato, como `csv.reader()` o `json.load()`.

## 3. TXT significa texto, no un único esquema universal

`.txt` normalmente significa texto simple, pero no existe un único formato universal de registros TXT.

Todos estos podrían ser contratos válidos de archivo de texto:

```text
Functions
Exceptions
Files
```

```text
topic=Functions
level=2
active=true
```

```text
2026-08-26 | Files | completed
```

El programa y quien produce el archivo deben acordar las reglas.

## 4. Un contrato TXT simple puede tener un registro por línea

Si cada línea es un valor de texto independiente, el formato puede mantenerse intencionalmente simple:

```python
with open("topics.txt", "r", encoding="utf-8") as file:
    topics = [line.rstrip("\n") for line in file]
```

Aquí el parser es pequeño porque el contrato es pequeño: cada línea física representa un tema.

## 5. Conserva el espacio significativo de forma deliberada

Evita usar `strip()` automáticamente cuando los espacios puedan pertenecer a los datos.

```python
clean_line = line.rstrip("\n")
```

Esto elimina solo el carácter de nueva línea definido por la decisión de formato anterior.

Si tu formato define otras reglas de normalización, aplícalas explícitamente en lugar de tratar todo espacio en blanco como descartable.

## 6. Los separadores personalizados simples siguen formando un formato que debe definirse

Supón que un archivo controlado contiene un par clave-valor por línea:

```text
topic=Files
level=2
```

Un parser deliberado puede dividir solo en el primer separador:

```python
key, value = line.rstrip("\n").split("=", 1)
```

El `1` importa si el propio valor puede contener `=` después.

Cuando aparecen escape, comillas, columnas opcionales, datos anidados o muchos casos límite, un formato estándar suele ser mejor que hacer crecer un minilenguaje privado.

## 7. CSV representa registros tabulares

CSV es útil cuando los datos naturalmente parecen filas con las mismas columnas:

```text
topic,score,status
Functions,91,complete
Files,88,complete
JSON,79,review
```

El nombre significa valores separados por comas, pero los datos CSV reales pueden usar delimitadores y reglas de comillas diferentes. Python modela esas elecciones mediante dialectos y opciones de formato CSV.

## 8. No analices CSV con `split(",")`

Esto parece tentador:

```python
columns = line.split(",")
```

pero un campo válido puede contener una coma cuando está entre comillas:

```text
topic,note
Files,"Read, write, and validate"
```

Un parser CSV entiende delimitadores, comillas, nuevas líneas incrustadas y otras reglas del formato. Un simple split de string no.

## 9. Importa el módulo `csv` de la biblioteca estándar

El módulo forma parte de la biblioteca estándar de Python:

```python
import csv
```

Proporciona APIs orientadas a filas como:

- `csv.reader()`;
- `csv.writer()`;
- `csv.DictReader()`;
- `csv.DictWriter()`.

Este capítulo enseña el núcleo práctico. Una fase posterior sobre Biblioteca Estándar podrá revisar opciones más amplias y personalizaciones del módulo.

## 10. Abre archivos CSV con `newline=""`

Cuando se pasa un objeto archivo al módulo `csv`, la documentación oficial recomienda abrirlo con `newline=""` para que el propio módulo CSV realice correctamente el manejo de nuevas líneas.

```python
with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Mantén `encoding="utf-8"` explícito cuando UTF-8 forme parte del contrato de los datos.

## 11. `csv.reader()` devuelve filas como listas

Un reader básico trata cada registro como una secuencia de campos:

```python
import csv

with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Con el ejemplo anterior, las filas son listas como:

```text
['topic', 'score', 'status']
['Functions', '91', 'complete']
```

Observa que `91` es una string.

## 12. CSV normalmente no infiere los tipos de tu aplicación

De forma predeterminada, `csv.reader()` devuelve los campos como strings. `DictReader` también entrega valores string para campos normales.

Tu programa debe decidir qué conversiones forman parte del contrato:

```python
score = int(row[1])
```

La conversión puede fallar, por lo que este también es un límite de validación.

## 13. `csv.writer()` da formato a las filas por ti

No construyas registros CSV manualmente uniendo valores con comas.

```python
import csv

rows = [
    ["topic", "score"],
    ["Functions", 91],
    ["Files", 88],
]

with open("scores.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

El writer aplica las reglas configuradas de comillas y delimitadores CSV.

## 14. `DictReader` da nombres a las columnas

Cuando la primera fila es un encabezado, `DictReader` puede hacer el código más fácil de leer:

```python
import csv

with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["topic"], row["score"])
```

Los valores del encabezado se convierten en claves del diccionario.

## 15. Los nombres de encabezado forman parte del contrato CSV

El código que espera `row["score"]` depende de una columna llamada exactamente `score`.

Si un productor cambia el encabezado a `final_score`, tu parser puede lanzar `KeyError` o tu validación puede rechazar el registro.

Trata los nombres de columnas, los requisitos de orden, la elección del delimitador y los campos obligatorios como decisiones explícitas de interfaz.

## 16. `DictWriter` hace explícitas las columnas de salida

`DictWriter` requiere `fieldnames`, que definen el orden de las columnas:

```python
import csv

fieldnames = ["topic", "score", "status"]

with open("scores.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {"topic": "Files", "score": 88, "status": "complete"}
    )
```

Esto suele ser más claro que los índices posicionales cuando la tabla tiene columnas con nombre.

## 17. Los delimitadores varían

La coma es el delimitador predeterminado del dialecto común estilo Excel, pero algunos contratos usan punto y coma, tabulaciones u otros delimitadores.

```python
reader = csv.reader(file, delimiter=";")
```

No adivines basándote en hábitos regionales ni en una sola fila de muestra. Conoce o documenta el contrato siempre que sea posible.

## 18. Las comillas protegen campos con caracteres especiales

El writer CSV puede entrecomillar campos que contienen delimitadores, caracteres de comillas o terminadores de línea.

```python
import csv

row = ["Files", "Read, write, and validate"]
```

Con reglas normales de quoting, la coma dentro de la nota puede seguir formando parte de un solo campo.

Esta es otra razón para dejar que `csv` genere el texto serializado.

## 19. Parsing CSV y validación CSV son pasos diferentes

Una fila puede ser CSV sintácticamente válido y aun así violar las reglas de la aplicación:

```text
topic,score
Files,one hundred
```

El parser CSV puede devolver correctamente `"one hundred"`. Después, tu aplicación decide si `score` debe ser un entero.

```text
texto CSV
   ↓ parser
campos de la fila
   ↓ conversión + validación
registro confiable
```

## 20. JSON representa valores estructurados

JSON es útil para objetos y arrays anidados, no solo tablas planas.

```json
{
  "topic": "Files",
  "score": 88,
  "tags": ["io", "formats"],
  "complete": true
}
```

JSON es un formato de intercambio de datos. Se parece a algunos literales de Python, pero no es código fuente de Python.

## 21. Los valores JSON principales se mapean a valores Python familiares

Un mapeo útil para principiantes es:

| JSON | Valor Python típico |
|---|---|
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` o `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

El mapeo es lo bastante cercano para resultar familiar, pero las sintaxis no son intercambiables.

## 22. La sintaxis JSON no es sintaxis de literal Python

Estos tokens JSON están en minúsculas:

```json
{"active": true, "result": null}
```

Python usa:

```python
data = {"active": True, "result": None}
```

No analices JSON con `eval()`.

## 23. `json.loads()` analiza una string JSON

La `s` de `loads` es una buena ayuda de memoria cuando trabajas con un valor string:

```python
import json

text = '{"topic": "Files", "score": 88}'
data = json.loads(text)

print(data["topic"])
```

`loads()` devuelve valores Python creados a partir del documento JSON.

## 24. `json.dumps()` crea una string JSON

`dumps()` serializa un valor Python compatible a una string con formato JSON:

```python
import json

data = {"topic": "Files", "score": 88}
text = json.dumps(data)

print(text)
```

Serialización significa convertir un valor en memoria en una representación adecuada para almacenamiento o transporte.

## 25. `json.load()` lee JSON desde un objeto archivo o similar

Cuando el documento JSON ya está en un archivo de texto, usa `load()` con el archivo abierto:

```python
import json

with open("profile.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

`open()` gestiona el acceso al archivo. `json.load()` analiza el texto y lo convierte en valores Python.

## 26. `json.dump()` escribe un valor JSON en un objeto archivo o similar

```python
import json

data = {"topic": "Files", "complete": True}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
```

`json.dump()` escribe strings en el destino. En el uso común con archivos, abre ese destino en modo texto.

## 27. `ensure_ascii=False` mantiene legible el texto no ASCII

De forma predeterminada, el encoder JSON escapa los caracteres no ASCII. Cuando un archivo UTF-8 es el contrato explícito, `ensure_ascii=False` puede mantener esos caracteres legibles en el documento serializado:

```python
import json

data = {"language": "Português"}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)
```

La elección afecta a la representación, no al valor de la string Python después de una decodificación correcta.

## 28. `indent` mejora la legibilidad humana

El JSON con formato es útil para configuración, ejemplos y archivos que las personas inspeccionan manualmente:

```python
json.dump(data, file, ensure_ascii=False, indent=2)
```

La indentación aumenta el tamaño del archivo, así que una salida compacta puede ser mejor en algunas interfaces orientadas a máquinas. Elige según el contrato, no solo por estética.

## 29. JSON no válido lanza `JSONDecodeError`

Los errores de sintaxis en un documento JSON se informan con `json.JSONDecodeError`, una subclase de `ValueError`:

```python
import json

text = '{"topic": "Files",}'

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")
```

Captúrala solo donde el programa tenga una política útil de recuperación o informe.


El decoder de Python también tiene una extensión deliberada de interoperabilidad: de forma predeterminada, `json.loads()` acepta `NaN`, `Infinity` y `-Infinity` y los convierte en valores de punto flotante, aunque esos tokens no son JSON válido según la especificación interoperable de JSON. Por lo tanto, una llamada exitosa a `json.loads()` **no** demuestra por sí sola que la entrada cumpla el estándar JSON.

Cuando el cumplimiento estricto del estándar forme parte del contrato, proporciona `parse_constant` con un callback que rechace esos valores explícitamente:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


text = '{"value": NaN}'

try:
    data = json.loads(text, parse_constant=reject_nonstandard_constant)
except ValueError as error:
    print(error)
```

Aquí, el `ValueError` es lanzado deliberadamente por el callback. `JSONDecodeError` sigue representando errores comunes de sintaxis JSON, como la coma final del ejemplo anterior.


El encoder tiene la preocupación de interoperabilidad correspondiente en la dirección inversa. De forma predeterminada, `json.dumps()` y `json.dump()` usan `allow_nan=True`, por lo que Python puede serializar valores de punto flotante no finitos como `NaN`, `Infinity` y `-Infinity`. Esos tokens están fuera del JSON compatible con el estándar y pueden ser rechazados por consumidores estrictos.

Cuando la salida JSON estricta forme parte del contrato, establece `allow_nan=False`:

```python
import json

data = {"value": float("nan")}

try:
    text = json.dumps(data, allow_nan=False)
except ValueError as error:
    print(error)
```

Con `allow_nan=False`, Python lanza `ValueError` en lugar de emitir una constante JSON no estándar. La misma opción está disponible en `json.dump()`.

## 30. No todos los objetos Python son serializables a JSON de forma predeterminada

El encoder predeterminado maneja estructuras comunes compatibles con JSON, pero los objetos arbitrarios no se convierten automáticamente.

```python
import json

values = {1, 2, 3}
json.dumps(values)
```

Un `set` no es un tipo JSON, por lo que esto lanza `TypeError` sin una transformación o personalización deliberada.

Para código de principiantes, una transformación explícita suele ser más clara que un encoder personalizado.

## 31. Un round trip JSON puede cambiar estructuras específicas de Python

Los arrays JSON vuelven como listas. Eso significa que una tupla serializada como array no vuelve automáticamente como tupla:

```python
import json

original = ("Files", "JSON")
restored = json.loads(json.dumps(original))

print(type(restored).__name__)
```

Salida:

```text
list
```

JSON representa tipos JSON, no todas las distinciones del modelo de objetos de Python.

## 32. Las claves de objetos JSON son strings en el modelo de datos

El encoder de Python acepta algunas claves básicas que no son strings y las convierte para JSON, pero los nombres de miembros de objetos JSON son strings.

Por ello, un diccionario con claves no string puede no ser igual después de un round trip dump/load.

Si el tipo de clave importa para tu aplicación, diseña esa representación de forma explícita.

## 33. No añadas documentos JSON independientes con llamadas repetidas a `dump()`

JSON no es un protocolo enmarcado. Escribir dos valores JSON de nivel superior uno detrás de otro no crea automáticamente un único documento JSON válido:

```python
json.dump(first, file)
json.dump(second, file)
```

Si necesitas varios registros, elige un contenedor definido, como un único array JSON, u otro formato especificado explícitamente.

## 34. Parsing no es validación

Un parser responde si el texto sigue la sintaxis del formato y reconstruye valores.

La validación responde si esos valores satisfacen las reglas del programa.

```python
import json

data = json.loads('{"score": -50}')

if not 0 <= data["score"] <= 100:
    raise ValueError("score must be between 0 and 100")
```

El JSON es sintácticamente válido. El valor de la aplicación es inválido.

## 35. Separa I/O, parsing y validación cuando el programa crezca

Los programas pequeños pueden mantener estos pasos cerca, pero funciones claras ayudan cuando aumenta la complejidad:

```text
leer bytes/texto
     ↓
analizar formato
     ↓
validar valores
     ↓
transformar/usar datos
```

Esta separación facilita identificar si un fallo vino del acceso al archivo, la sintaxis del formato, la conversión de tipos o una regla de la aplicación.

## 36. Ejemplo práctico: un registro TXT por línea

El ejemplo ejecutable usa un directorio temporal solo para mantener limpios los tests del repositorio:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "topics.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Functions\n")
        file.write("Files\n")
        file.write("JSON\n")

    with open(path, "r", encoding="utf-8") as file:
        topics = [line.rstrip("\n") for line in file]

    print(topics)
```

Salida:

```text
['Functions', 'Files', 'JSON']
```

Versión ejecutable: [`examples/text_records.py`](examples/text_records.py).

## 37. Ejemplo práctico: diccionarios CSV y conversión explícita

```python
import csv
import os
import tempfile


records = [
    {"topic": "Functions", "score": 91, "note": "Clear flow"},
    {"topic": "Files", "score": 88, "note": "Read, write, validate"},
]

with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "scores.csv")
    fieldnames = ["topic", "score", "note"]

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            score = int(row["score"])
            print(f'{row["topic"]}: {score} - {row["note"]}')
```

Salida:

```text
Functions: 91 - Clear flow
Files: 88 - Read, write, validate
```

Versión ejecutable: [`examples/csv_records.py`](examples/csv_records.py).

## 38. Ejemplo práctico: escribir y leer un documento JSON

```python
import json
import os
import tempfile


profile = {
    "topic": "Files",
    "score": 88,
    "tags": ["io", "formats"],
    "complete": True,
}

with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "profile.json")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)

    print(restored["topic"])
    print(restored["tags"])
    print(restored["complete"])
```

Salida:

```text
Files
['io', 'formats']
True
```

Versión ejecutable: [`examples/json_document.py`](examples/json_document.py).

## 39. Ejemplo práctico: manejar JSON no válido deliberadamente

```python
import json


text = '{"topic": "Files",}'

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")
else:
    print(data)
```

Salida:

```text
Invalid JSON
```

Versión ejecutable: [`examples/handle_invalid_json.py`](examples/handle_invalid_json.py).

## 40. Error común: tratar todo archivo de texto como CSV

Un archivo de texto con prosa, líneas de log o un valor por línea no se convierte en CSV solo porque teóricamente podrían separarse campos.

Usa CSV cuando el contrato sea realmente tabular y sus reglas de comillas y delimitadores sean apropiadas.

Usa texto más simple cuando el texto simple sea el formato real.

## 41. Error común: construir JSON manualmente

Evita este estilo:

```python
text = '{"name": "' + name + '", "score": ' + str(score) + '}'
```

Escapar comillas, barras invertidas, caracteres de control, estructuras anidadas, booleanos y `null` se vuelve rápidamente propenso a errores.

Construye valores Python y deja que `json.dumps()` o `json.dump()` los serialicen.

## 42. Error común: confiar automáticamente en los datos analizados

Un parsing correcto no demuestra que existan los campos obligatorios, que los tipos cumplan el contrato de la aplicación, que los rangos numéricos sean válidos o que las strings sean aceptables.

Trata los datos de archivos y red como entrada:

```text
parsing correcto
      ≠
seguro y válido para todo uso
```

Valida las propiedades de las que tu programa realmente depende.

## 43. Elegir entre TXT, CSV y JSON

| Forma o necesidad | Buena elección inicial |
|---|---|
| Líneas simples legibles por personas | TXT |
| Filas planas con columnas consistentes | CSV |
| Objetos anidados, arrays, booleanos y nulls | JSON |
| Datos ya gobernados por un contrato de formato externo | Usa el formato requerido |

La extensión no es el factor decisivo. Lo son el modelo de datos y el contrato de interoperabilidad.

## 44. Cuándo evitar inventar un formato de texto personalizado

Un formato privado diminuto puede estar bien para una tarea pequeña y controlada. Se vuelve arriesgado cuando empiezas a añadir:

- reglas de escape;
- campos opcionales o repetidos;
- delimitadores entrecomillados;
- valores anidados;
- versionado;
- múltiples productores y consumidores independientes.

En ese punto, un formato estándar normalmente aporta parsers probados e interoperabilidad más clara.

## 45. Ejercicio

Crea un programa llamado `study_export.py` con estos requisitos:

1. Empieza con una lista de diccionarios que contengan `topic`, `score` y `complete`.
2. Escribe los registros en `study.csv` con `csv.DictWriter`.
3. Vuelve a abrir el CSV con `csv.DictReader`, convierte `score` a `int` y convierte `complete` de nuevo a `bool` con un mapeo explícito como `{"True": True, "False": False}`; rechaza texto inesperado en vez de usar `bool()` directamente.
4. Construye una nueva lista con los registros convertidos.
5. Escribe esa lista en `study.json` usando `json.dump()` con UTF-8, `ensure_ascii=False` e `indent=2`.
6. Vuelve a abrir el JSON con `json.load()`.
7. Muestra solo los temas cuyo score sea al menos 80.
8. Usa `with` para cada operación real de archivo.

Preguntas extra:

- ¿Por qué se usa `newline=""` para el archivo CSV?
- ¿Por qué el score del CSV debe convertirse explícitamente?
- ¿Por qué `bool(row["complete"])` sería incorrecto cuando el texto CSV sea `"False"`?
- ¿Qué excepción lanzaría una sintaxis JSON no válida?
- ¿Por qué `split(",")` sería inseguro para una nota que contiene comas?
- ¿Qué paso es parsing y qué paso es validación de la aplicación?

## 46. Lista de revisión

Antes de continuar, confirma que puedes responder sin adivinar:

- ¿Cuál es la diferencia entre una extensión de archivo y un formato de datos?
- ¿`.txt` define una única estructura universal de registros?
- ¿Por qué CSV no debe analizarse con un split ingenuo por comas?
- ¿Por qué se recomienda `newline=""` cuando se usa un objeto archivo con `csv`?
- ¿Qué contienen de forma predeterminada las filas de `csv.reader()`?
- ¿Por qué `DictReader` puede ser más claro que índices numéricos de columna?
- ¿Cuál es la diferencia entre `json.load()` y `json.loads()`?
- ¿Cuál es la diferencia entre `json.dump()` y `json.dumps()`?
- ¿Qué valor JSON se corresponde con `None` de Python?
- ¿Qué excepción indica sintaxis JSON no válida?
- ¿Todo objeto Python puede serializarse automáticamente a JSON?
- ¿Por qué parsing y validación son conceptos separados?

## 47. Referencia rápida

| Necesidad | Patrón |
|---|---|
| Leer texto UTF-8 simple | `open(path, "r", encoding="utf-8")` |
| Leer filas CSV | `csv.reader(file)` |
| Escribir filas CSV | `csv.writer(file)` |
| Leer CSV con columnas nombradas | `csv.DictReader(file)` |
| Escribir CSV con columnas nombradas | `csv.DictWriter(file, fieldnames=...)` |
| Abrir un objeto archivo para CSV | `open(path, ..., encoding="utf-8", newline="")` |
| Analizar string JSON | `json.loads(text)` |
| Crear string JSON | `json.dumps(data)` |
| Analizar archivo JSON | `json.load(file)` |
| Escribir archivo JSON | `json.dump(data, file)` |
| Conservar Unicode legible en la salida | `ensure_ascii=False` |
| Formatear JSON | `indent=2` |
| Sintaxis JSON no válida | `json.JSONDecodeError` |
| Objeto incompatible con JSON al serializar | `TypeError` |

Un pipeline predeterminado útil es:

```text
abrir de forma segura
    ↓
analizar con el parser del formato
    ↓
convertir y validar valores de la aplicación
    ↓
usar o transformar datos confiables
```

## Qué sigue

El Capítulo 04 añade formatos comunes de datos textuales a la base de gestión de archivos. El último capítulo de la Fase 7, **Imports, Módulos y Paquetes**, pasará de datos almacenados en varios archivos a código Python organizado en varios archivos.

```text
excepciones
    ↓
señalización deliberada de excepciones
    ↓
tiempo de vida seguro de archivos
    ↓
límites de datos TXT / CSV / JSON
    ↓
imports / módulos / paquetes
```

## Referencias oficiales

- Documentación `csv` de Python 3.14: <https://docs.python.org/3.14/library/csv.html>
- Documentación `json` de Python 3.14: <https://docs.python.org/3.14/library/json.html>
- Tutorial de Python 3.14, Reading and Writing Files: <https://docs.python.org/3.14/tutorial/inputoutput.html#reading-and-writing-files>
- Tutorial de Python 3.14, Saving structured data with `json`: <https://docs.python.org/3.14/tutorial/inputoutput.html#saving-structured-data-with-json>
