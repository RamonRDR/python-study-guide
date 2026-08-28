<div align="center">

# Controlando Dialectos CSV, Quoting y Contratos Tabulares

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

> **Fase 8 · Biblioteca Estándar · Capítulo 04**

CSV parece simple porque un archivo pequeño puede parecer una serie de líneas separadas por comas. Las interfaces CSV reales son más exigentes: los productores difieren en delimitadores, quoting, finales de línea, valores nulos, encabezados, encodings y filas malformadas. El módulo `csv` de Python existe para modelar esas reglas explícitamente en lugar de reconstruir un parser con `split(",")`.

Este capítulo revisita CSV a un nivel más profundo de biblioteca. La Fase 7 introdujo CSV como formato de archivo. Aquí el foco es el **contrato** alrededor de `csv.reader`, `csv.writer`, `DictReader`, `DictWriter`, dialectos, modos de quoting, entrada malformada, límites de recursos e interoperabilidad.

## 1. ¿Qué problema resuelve `csv`?

El módulo lee y escribe **texto tabular delimitado** de acuerdo con un dialecto.

```python
import csv
from io import StringIO

text = "name,score\nAna,88\nBob,91\n"
reader = csv.reader(StringIO(text, newline=""))

for row in reader:
    print(row)
```

Por defecto, los campos se devuelven como strings. CSV por sí solo no proporciona un schema completo de la aplicación, por lo que parsear filas y validar el significado de negocio son responsabilidades separadas.

## 2. CSV es una familia de dialectos, no un diseño universal

"CSV" no garantiza que cada productor use el mismo delimitador ni las mismas reglas de quoting.

Variaciones comunes incluyen:

```text
delimitador coma
delimitador punto y coma
delimitador tab
campos entre comillas
campos escapados
diferentes finales de línea
diferentes encodings de caracteres
```

Python agrupa las decisiones de parsing y formato en un `Dialect`. Los dialectos incorporados incluyen `excel`, `excel-tab` y `unix`.

Un dialecto describe sintaxis. No demuestra que los datos tengan las columnas o reglas de valores exigidas por tu aplicación.

## 3. Los readers parsean texto; los writers formatean texto

Un writer recibe valores Python y escribe texto delimitado mediante un objeto file-like con `write()`.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(stream, lineterminator="\n")
writer.writerow(["name", "score"])
writer.writerow(["Ana", 88])

print(stream.getvalue())
```

Un reader consume un iterable de strings. Al trabajar con archivos reales, la decodificación de caracteres pertenece a `open()`, mientras que el parsing de sintaxis CSV pertenece a `csv`.

Esa separación se parece a la frontera JSON del capítulo anterior:

```text
bytes en almacenamiento/red
   ↓ decodificación de texto
Python str
   ↓ parsing CSV
filas y campos
   ↓ validación de la aplicación
valores de dominio confiables
```

## 4. Usa `newline=""` en objetos de archivo CSV

Cuando se pasa un archivo real a `csv.reader()` o `csv.writer()`, la documentación de Python recomienda abrirlo con `newline=""`.

```python
import csv

with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Esto permite que el módulo `csv` realice su propio manejo de nuevas líneas. Importa especialmente para campos entre comillas con saltos de línea y para evitar comportamiento no deseado de carriage return en plataformas que usan `\r\n`.

`newline=""` es una política de apertura del archivo. No es una configuración de delimitador ni de schema de registro.

## 5. `delimiter` y `quotechar` forman parte de la interfaz

Si un productor usa punto y coma, configúralo explícitamente:

```python
import csv
from io import StringIO

text = 'name;note\nAna;"uses;semicolon"\n'
reader = csv.reader(
    StringIO(text, newline=""),
    delimiter=";",
    quotechar='"',
)

print(list(reader))
```

El delimitador y el carácter de comillas son decisiones de sintaxis de un solo carácter. Siempre que sea posible, deben venir de un contrato conocido de la interfaz.

No adivines un delimitador solamente porque una muestra contiene cierto signo de puntuación.

## 6. `QUOTE_MINIMAL` usa comillas solamente cuando la sintaxis CSV lo necesita

`csv.QUOTE_MINIMAL` es el valor habitual por defecto cuando existe un carácter de comillas.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerow(["Ana", "uses;semicolon"])

print(stream.getvalue())
```

Aquí el segundo campo contiene el delimitador, así que el writer lo coloca entre comillas.

Otras políticas importantes son:

- `QUOTE_ALL`: coloca todos los campos entre comillas;
- `QUOTE_MINIMAL`: usa comillas solamente cuando el dialecto lo exige;
- `QUOTE_NONNUMERIC`: el writer coloca campos no numéricos entre comillas y el reader convierte campos sin comillas a `float`;
- `QUOTE_NONE`: nunca procesa caracteres de comillas de forma especial;
- `QUOTE_NOTNULL`: coloca entre comillas todo campo distinto de `None` y conserva un campo vacío sin comillas como `None` al leer;
- `QUOTE_STRINGS`: coloca strings entre comillas, aplica conversión estilo `QUOTE_NONNUMERIC` a valores numéricos sin comillas y usa campos vacíos sin comillas con semántica `None`.

`QUOTE_NOTNULL` y `QUOTE_STRINGS` se añadieron en Python 3.12 y están disponibles en Python 3.14.

## 7. `QUOTE_NONNUMERIC` cambia tipos durante la lectura

La mayor parte de la lectura CSV devuelve strings. `QUOTE_NONNUMERIC` es una excepción importante.

```python
import csv
from io import StringIO

text = '3,19.90,"ready"\n'
reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NONNUMERIC,
)

row = next(reader)
print(row)
print([type(value).__name__ for value in row])
```

Los campos sin comillas se convierten a `float`; los campos entre comillas permanecen como strings.

Este modo no es un sistema general de schema. Algunos valores producidos a partir de tipos Python con apariencia numérica, como `bool`, `Fraction` o `IntEnum`, pueden tener representaciones de texto que no se pueden convertir de vuelta a `float`.

Usa validación explícita de la aplicación cuando importen tipos exactos.

## 8. `QUOTE_NOTNULL` puede distinguir `None` de string vacío

El writer normal serializa `None` como string vacío, lo que por sí solo no es reversible.

Python 3.12+ ofrece `QUOTE_NOTNULL`:

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NOTNULL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", None])
writer.writerow(["Bob", ""])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NOTNULL,
)
print(list(reader))
```

Con esta política:

- `None` se convierte en un campo vacío **sin comillas**;
- un string vacío sigue siendo un valor distinto de `None` y se coloca entre comillas;
- el reader correspondiente interpreta un campo vacío sin comillas como `None`.

Esto es útil solamente cuando ambos extremos acuerdan esa política de dialecto.

## 9. `QUOTE_STRINGS` solo es útil cuando encaja su contrato de conversión

`QUOTE_STRINGS` coloca campos string entre comillas, escribe `None` como campo vacío sin comillas y hace que el reader interprete campos no vacíos sin comillas de forma semejante a `QUOTE_NONNUMERIC`.

Eso significa que los valores sin comillas son candidatos a conversión a `float`. No equivale a "preservar tipos Python arbitrarios."

Si la interfaz contiene columnas como IDs, booleanos, decimales, fechas o enums, un schema columna por columna suele ser más claro que depender del modo de quoting para inferir tipos.

## 10. `QUOTE_NONE` normalmente requiere una estrategia de escape

Si quoting está desactivado, los delimitadores y otros caracteres especiales todavía necesitan representación.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
    lineterminator="\n",
)
writer.writerow(["Ana", "A,B"])

print(stream.getvalue())
```

Sin un `escapechar` utilizable, el writer puede lanzar `csv.Error` al encontrar caracteres que necesitan escape.

`doublequote`, `quotechar`, `escapechar` y `quoting` trabajan juntos. Cambiar una configuración puede alterar lo que las demás necesitan hacer.

## 11. El `lineterminator` del writer es explícito

Un dialecto también controla el final de línea del writer. El dialecto `excel` usa `\r\n` por defecto.

Para texto generado de forma determinista, puedes definir:

```python
writer = csv.writer(file, lineterminator="\n")
```

Actualmente el reader reconoce `\r` o `\n` de forma fija como final de línea y no usa el `lineterminator` del dialecto como regla de coincidencia. No enseñes `lineterminator` como un contrato simétrico entre reader y writer.

## 12. `DictReader` mapea un encabezado a diccionarios

Cuando la primera fila es un encabezado, `DictReader` permite acceso por nombre:

```python
import csv
from io import StringIO

text = "name,score\nAna,88\nBob,91\n"
reader = csv.DictReader(StringIO(text, newline=""))

for row in reader:
    print(row["name"], row["score"])
```

Si se omite `fieldnames`, la primera fila pasa a ser la secuencia de nombres de campos y no se devuelve como dato.

El mapeo resultante preserva el orden de los nombres, pero los valores siguen siendo campos decodificados de CSV, normalmente strings.

## 13. Campos extra y faltantes necesitan una política explícita

Una fila puede contener más o menos campos que el encabezado.

```python
import csv
from io import StringIO

text = "name,score\nAna,88,extra\nBob\n"
reader = csv.DictReader(
    StringIO(text, newline=""),
    restkey="_extra",
    restval="_missing",
)

for row in reader:
    print(row)
```

En `DictReader`:

- los campos extra se guardan bajo `restkey` como lista;
- los campos faltantes reciben `restval`;
- ambos usan `None` por defecto si no eliges otra cosa.

Usar los valores por defecto puede hacer menos evidentes las anchuras de fila malformadas. En contratos estrictos, verifica deliberadamente valores extra y faltantes.

## 14. `DictWriter` tiene su propia frontera de schema

`DictWriter` exige una secuencia `fieldnames` explícita.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.DictWriter(
    stream,
    fieldnames=["name", "score"],
    extrasaction="raise",
    lineterminator="\n",
)
writer.writeheader()
writer.writerow({"name": "Ana", "score": 88})

print(stream.getvalue())
```

Si un diccionario de entrada contiene una clave desconocida:

- `extrasaction="raise"` lanza `ValueError` y es el valor por defecto;
- `extrasaction="ignore"` excluye silenciosamente la clave extra.

Las claves esperadas que faltan se escriben usando `restval`, cuyo valor por defecto es un string vacío.

Elige estas políticas de forma intencional. La omisión silenciosa puede ser conveniente, pero también puede esconder un error del productor.

## 15. Un encabezado CSV no es lo mismo que un schema validado

Comprobar el encabezado exacto suele ser una buena primera frontera:

```python
import csv
from io import StringIO

EXPECTED = ["name", "score"]

text = "name,score\nAna,88\n"
reader = csv.DictReader(StringIO(text, newline=""))

if reader.fieldnames != EXPECTED:
    raise ValueError("unexpected CSV header")

rows = list(reader)
print(rows)
```

La aplicación también puede necesitar validar:

```text
cantidad exacta de columnas
columnas obligatorias
orden de columnas
identificadores no vacíos
rangos de enteros
formatos de fecha
reglas decimales
estados permitidos
identificadores duplicados
relaciones entre filas
```

El módulo `csv` maneja la sintaxis. La aplicación es responsable de la validación semántica.

## 16. El manejo de espacios no es limpieza automática

`skipinitialspace=True` ignora espacios inmediatamente después de los delimitadores.

No significa "aplicar strip a cada campo". Los espacios finales, por ejemplo, siguen siendo datos hasta que la aplicación los elimine.

Además, combinar `delimiter=" "` con `skipinitialspace=True` no permite campos vacíos sin comillas. Trata las reglas de whitespace como parte del dialecto, no como limpieza genérica.

## 17. `strict=True` pide al parser que rechace entrada CSV incorrecta

El dialecto por defecto es relativamente permisivo. En interfaces que deben rechazar sintaxis CSV malformada, usa `strict=True`.

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'

try:
    list(csv.reader(StringIO(text, newline=""), strict=True))
except csv.Error:
    print("Malformed CSV rejected")
```

`strict=True` se ocupa de la sintaxis CSV. Una fila sintácticamente válida todavía puede violar el schema de la aplicación.

## 18. `csv.Error` es la excepción de parsing/formato del módulo

Cuando el procesamiento CSV detecta un error, puede lanzar `csv.Error`.

Un reader también expone `line_num`:

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'
reader = csv.reader(StringIO(text, newline=""), strict=True)

try:
    for row in reader:
        print(row)
except csv.Error:
    print(f"CSV error near physical line {reader.line_num}")
```

`line_num` cuenta líneas físicas leídas del origen. No es necesariamente igual a la cantidad de registros devueltos porque un registro entre comillas puede abarcar varias líneas físicas.

## 19. `Sniffer` es una heurística, no validación

`csv.Sniffer().sniff()` puede estimar un dialecto a partir de una muestra de texto.

```python
import csv

sample = "name;score\nAna;88\nBob;91\n"
dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")

print(dialect.delimiter)
```

`Sniffer.has_header()` también puede estimar si la primera fila parece un encabezado.

Ambos son heurísticos. `has_header()` puede producir falsos positivos o negativos, y `sniff()` puede elegir entre delimitadores plausibles usando sus preferencias.

Usa sniffing para descubrimiento cuando realmente no controles el formato y después valida el resultado contra políticas permitidas por la interfaz antes de confiar en él.

## 20. Los dialectos registrados pueden centralizar sintaxis repetida

Si varios archivos comparten la misma sintaxis, registra un dialecto con nombre:

```python
import csv
from io import StringIO

csv.register_dialect(
    "study_semicolon",
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
)

reader = csv.reader(
    StringIO("name;score\nAna;88\n", newline=""),
    dialect="study_semicolon",
)
print(list(reader))

csv.unregister_dialect("study_semicolon")
```

`get_dialect()` devuelve un objeto dialecto inmutable y `list_dialects()` muestra los nombres registrados.

El registro global de dialectos afecta el registry de todo el proceso. En bibliotecas, parámetros locales explícitos o nombres de dialecto cuidadosamente namespaced pueden resultar más fáciles de razonar.

## 21. Limita el tamaño de campos para entrada no confiable o restringida

`csv.field_size_limit()` devuelve el tamaño máximo de campo actual del parser. Pasar un argumento cambia ese límite para el proceso.

```python
import csv
from io import StringIO

previous_limit = csv.field_size_limit()

try:
    csv.field_size_limit(8)
    try:
        list(csv.reader(StringIO("value\n123456789\n", newline="")))
    except csv.Error:
        print("Field limit enforced")
finally:
    csv.field_size_limit(previous_limit)
```

Un límite de campo es una frontera de recursos, no una solución de seguridad completa. El documento todavía puede contener muchas filas, y la validación posterior todavía puede consumir tiempo o memoria.

Como el límite es global al proceso, restáuralo cuando hagas un cambio temporal dentro de código reutilizable.

## 22. El encoding pertenece a la frontera del archivo de texto

El módulo `csv` trabaja con strings. `open()` decide cómo los bytes se convierten en texto.

Para CSV UTF-8 normal:

```python
with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Algunos archivos UTF-8 producidos por hojas de cálculo empiezan con BOM. Cuando eso forme parte del contrato externo, `encoding="utf-8-sig"` puede consumirlo:

```python
import csv

with open(
    "records.csv",
    encoding="utf-8-sig",
    newline="",
) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

No elijas `utf-8-sig` automáticamente para todo CSV. El encoding es una decisión de interfaz.

## 23. La conversión por defecto de `None` del writer pierde información

Para `csv.writer` normal, `None` se escribe como string vacío. Esto facilita exports de bases de datos, pero la transformación no es reversible por defecto.

Si `None` y `""` significan cosas distintas en tu aplicación, elige una política de representación como:

```text
un sentinel acordado
una columna de presencia separada
QUOTE_NOTNULL en Python 3.12+
otro formato con semántica null explícita
```

La elección correcta depende de los requisitos de interoperabilidad.

## 24. El quoting CSV no define la política de ejecución de una hoja de cálculo

El quoting protege la sintaxis CSV. No convierte automáticamente un valor en inofensivo cuando otro programa interpreta la celda después de abrir el archivo.

Si datos controlados por usuarios se abrirán en software de hoja de cálculo, las fórmulas y otras interpretaciones específicas del consumidor necesitan una política de seguridad de salida separada.

Trátalo como otra frontera:

```text
sintaxis CSV válida
        ≠
comportamiento seguro en cada consumidor CSV
```

## 25. Haz streaming de archivos grandes en lugar de construir listas innecesarias

Los readers son iteradores. Puedes procesar registros uno a uno:

```python
import csv

with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        process_name = row["name"].strip()
        print(process_name)
```

Esto puede mantener el uso de memoria mucho más bajo que `list(reader)` para archivos grandes.

El streaming no elimina la necesidad de límites. Aún puedes necesitar políticas para tamaño de archivo, cantidad de filas, longitud de campos y tiempo de procesamiento.

## 26. `writerows()` acepta un iterable de filas

Un writer puede consumir un generator:

```python
import csv
from io import StringIO

rows = (
    [name, score]
    for name, score in [("Ana", 88), ("Bob", 91)]
)

stream = StringIO(newline="")
writer = csv.writer(stream, lineterminator="\n")
writer.writerows(rows)

print(stream.getvalue())
```

Esto es útil para pipelines que transforman registros de forma lazy.

Recuerda que el writer todavía convierte valores no string según las reglas del módulo. El streaming cambia el comportamiento de memoria, no el significado del schema.

## 27. Un round trip CSV no preserva tipos Python arbitrarios

Con el par reader/writer normal:

```text
Python int 88
   ↓ writer
campo CSV 88
   ↓ reader
Python str "88"
```

`QUOTE_NONNUMERIC`, `QUOTE_NOTNULL` y `QUOTE_STRINGS` cambian partes específicas de este comportamiento, pero ninguno convierte CSV en un formato general de serialización de objetos Python.

Si importa la reconstrucción exacta de tipos, defínela columna por columna.

## 28. Cuándo CSV encaja bien

CSV es útil cuando:

- los datos son naturalmente tabulares;
- las filas comparten un contrato estable de columnas;
- personas o herramientas de hoja de cálculo necesitan inspeccionar los datos;
- importa la interoperabilidad con sistemas que ya intercambian texto delimitado;
- resulta valioso el procesamiento en streaming fila por fila.

## 29. Cuándo CSV encaja mal

Considera otro formato cuando:

- los datos están profundamente anidados;
- null frente a string vacío debe ser inequívoco sin un dialecto personalizado;
- tipos ricos deben hacer round trip directamente;
- los schemas por registro varían mucho;
- los datos binarios son un campo de primera clase;
- necesitas un envelope o modelo de metadatos fuertemente estandarizado.

## 30. Errores comunes

### Error 1: usar `split(",")`

```python
line = 'Ana,"A,B"'
print(line.split(","))
```

Esto ignora las reglas de quoting. Usa `csv.reader()`.

### Error 2: omitir `newline=""` en archivos CSV reales

Deja que el módulo `csv` maneje las nuevas líneas CSV.

### Error 3: asumir que todo archivo `.csv` usa comas

Confirma o configura el dialecto.

### Error 4: tratar un encabezado como validación de schema

Valida la anchura de fila y la semántica de valores por separado.

### Error 5: esperar que los tipos numéricos hagan round trip automáticamente

El reader por defecto devuelve strings.

### Error 6: confiar en `Sniffer` como prueba

Es una heurística.

### Error 7: ignorar silenciosamente claves extra de diccionarios

Usa `extrasaction="raise"` salvo que la omisión sea intencional.

### Error 8: asumir que una salida entre comillas es segura en cualquier hoja de cálculo

La sintaxis CSV y el comportamiento de ejecución de la hoja de cálculo son fronteras diferentes.

## 31. Ejemplo práctico: round trip con dialecto de punto y coma

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", "uses;semicolon"])
writer.writerow(["Bob", 'says "hello"'])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    delimiter=";",
)
print(list(reader))
```

Versión ejecutable: [`examples/semicolon_dialect.py`](examples/semicolon_dialect.py).

## 32. Ejemplo práctico: validar un contrato de filas en diccionario

```python
import csv
from io import StringIO

EXPECTED_FIELDS = ["name", "score"]

text = "name,score\nAna,88\nBob,91\n"
reader = csv.DictReader(StringIO(text, newline=""))

if reader.fieldnames != EXPECTED_FIELDS:
    raise ValueError("unexpected header")

for row in reader:
    if None in row:
        raise ValueError("row has extra fields")
    if any(value is None for value in row.values()):
        raise ValueError("row has missing fields")
    print(row)
```

Versión ejecutable: [`examples/dict_contract.py`](examples/dict_contract.py).

## 33. Ejemplo práctico: preservar `None` frente a string vacío

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NOTNULL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", None])
writer.writerow(["Bob", ""])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NOTNULL,
)
print(list(reader))
```

Versión ejecutable: [`examples/quote_notnull.py`](examples/quote_notnull.py).

## 34. Ejemplo práctico: rechazar sintaxis CSV malformada

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'

try:
    list(csv.reader(StringIO(text, newline=""), strict=True))
except csv.Error:
    print("Malformed CSV rejected")
```

Versión ejecutable: [`examples/strict_csv.py`](examples/strict_csv.py).

## 35. Ejercicio

Crea `decode_inventory_csv(text)` para este contrato:

```text
encabezado: item,quantity,active
delimitador: coma
quoting: quoting CSV normal
concepto de nivel superior: una fila por elemento de inventario
```

Requisitos:

1. parsea con `csv.DictReader`;
2. exige el orden exacto de encabezado `item`, `quantity`, `active`;
3. rechaza filas con campos extra o faltantes;
4. exige que `item` sea un string no vacío después de quitar whitespace de los extremos;
5. convierte `quantity` con `int()` y exige cero o más;
6. acepta solamente `true` o `false` para `active`, sin distinguir mayúsculas y minúsculas;
7. devuelve diccionarios validados donde `quantity` sea `int` y `active` sea `bool`;
8. rechaza sintaxis CSV malformada con un error claro a nivel de aplicación.

Después crea `encode_inventory_csv(rows)` que escriba el mismo orden de campos con:

```text
escritura CSV consciente de newline
lineterminator explícito
extrasaction="raise"
```

Prueba datos válidos y también:

```text
encabezado incorrecto
campo extra
campo faltante
entero inválido
cantidad negativa
booleano inválido
coma entre comillas dentro de item
```

El objetivo es hacer que la frontera sea explicable, no solamente lograr que funcione el happy path.

## 36. Referencia rápida

| Necesidad | Herramienta / política |
|---|---|
| Leer filas | `csv.reader(...)` |
| Escribir filas | `csv.writer(...)` |
| Leer filas mapeadas por encabezado | `csv.DictReader(...)` |
| Escribir diccionarios | `csv.DictWriter(...)` |
| Abrir archivos CSV reales | `newline=""` |
| Elegir delimitador | `delimiter=";"` u otro valor de un carácter |
| Elegir carácter de comillas | `quotechar='"'` |
| Quoting mínimo | `csv.QUOTE_MINIMAL` |
| Colocar todos los campos entre comillas | `csv.QUOTE_ALL` |
| Convertir campos sin comillas a `float` al leer | `csv.QUOTE_NONNUMERIC` |
| Preservar campo vacío sin comillas como `None` | `csv.QUOTE_NOTNULL` |
| Colocar strings entre comillas con conversión numérica para valores sin comillas | `csv.QUOTE_STRINGS` |
| Desactivar procesamiento de comillas | `csv.QUOTE_NONE` |
| Escapar caracteres especiales | `escapechar=...` |
| Final de línea explícito del writer | `lineterminator="\n"` |
| Rechazar sintaxis CSV malformada | `strict=True` |
| Error del parser/formatter CSV | `csv.Error` |
| Inspeccionar progreso de línea física | `reader.line_num` |
| Estimar dialecto | `csv.Sniffer().sniff(...)` |
| Estimar presencia de encabezado | `csv.Sniffer().has_header(...)` |
| Registrar dialecto reutilizable | `csv.register_dialect(...)` |
| Limitar tamaño de campo del parser | `csv.field_size_limit(...)` |
| Rechazar claves desconocidas en DictWriter | `extrasaction="raise"` |

## 37. Checklist de diseño

Antes de publicar o consumir una interfaz CSV, pregunta:

```text
¿Qué delimitador se exige?
¿Qué reglas de comillas y escape se exigen?
¿Qué final de línea producirán los writers?
¿Qué encoding de caracteres transporta el texto?
¿Hay encabezado y su orden es significativo?
¿Cómo se manejan campos extra o faltantes?
¿Cómo se distinguen null y string vacío?
¿Qué columnas requieren conversión de tipos?
¿Cómo se reportan filas malformadas?
¿Qué límites de tamaño se aplican?
¿Se permite sniffing de dialecto o el formato debe ser explícito?
¿El software de hoja de cálculo interpretará el contenido de las celdas exportadas?
```

Cuando esas respuestas son explícitas, CSV deja de ser "solo texto separado por comas" y se convierte en un contrato de interfaz comprobable.

## Referencias

- [Documentación Python 3.14: `csv` — CSV File Reading and Writing](https://docs.python.org/3.14/library/csv.html)
- [PEP 305: CSV File API](https://peps.python.org/pep-0305/)
- [RFC 4180: Common Format and MIME Type for CSV Files](https://www.rfc-editor.org/rfc/rfc4180)

## Próximo capítulo

Continúa con el **Capítulo 05: `logging`** cuando esté disponible. Profundizará jerarquías de loggers, handlers, formatters, niveles, configuración y logging de aplicación frente a biblioteca.

[← Anterior: Capítulo 03 · `json`](../03-json/README.es.md)
