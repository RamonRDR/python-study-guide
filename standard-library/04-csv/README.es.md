<div align="center">

# Controlando Dialectos CSV y Contratos de Texto Tabular

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Biblioteca Estándar](../README.es.md) · [← Anterior: Controlando Contratos de Serialización y Decodificación JSON](../03-json/README.es.md)

La Fase 7 presentó CSV como formato tabular y enseñó el uso práctico de `csv.reader()`, `csv.writer()`, `csv.DictReader()` y `csv.DictWriter()`. Este capítulo avanza una capa.

El módulo `csv` no es solo una forma de separar filas en columnas. Es una herramienta de frontera para definir cómo se comportan entre sistemas los delimitadores, quoting, escaping, finales de línea, encabezados, campos ausentes, campos extra y conversión de tipos.

El objetivo es transformar "este es un archivo CSV" en una pregunta más precisa:

```text
¿Qué contrato de texto tabular acepta y produce este programa?
```

**Tiempo estimado de estudio:** 120–160 minutos.

**Requisito de Python:** Python 3.10 o posterior para las APIs centrales enseñadas aquí. `csv.QUOTE_NOTNULL` y `csv.QUOTE_STRINGS` fueron añadidos en Python 3.12 y su comportamiento de escritura está disponible en esa versión. Debido a un bug documentado de Python 3.12, su comportamiento especial de lectura requiere Python 3.13 o posterior.

**Base de documentación:** los comportamientos y ejemplos fueron verificados con la documentación oficial de `csv` de Python 3.14.

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- tratar CSV como una familia de contratos de texto tabular y no como un único diseño universal;
- separar la codificación de texto de las reglas del dialecto CSV;
- explicar por qué los objetos de archivo CSV deben abrirse con `newline=""`;
- distinguir registros CSV lógicos de líneas físicas de texto;
- configurar deliberadamente delimitadores, caracteres de comillas, escaping y terminadores de línea;
- explicar el comportamiento de los principales modos `QUOTE_*`;
- reconocer el comportamiento de conversión de tipos de `QUOTE_NONNUMERIC`;
- entender el comportamiento de escritura de `QUOTE_NOTNULL` y `QUOTE_STRINGS` en Python 3.12+, además de su semántica corregida de lectura en Python 3.13+;
- explicar por qué la conversión predeterminada de `None` del writer pierde información;
- validar encabezados de `DictReader` y anchos irregulares de filas;
- controlar claves extra y ausentes con `DictWriter`;
- usar `strict=True` y `csv.Error` cuando una entrada malformada debe fallar de forma visible;
- usar `field_size_limit()` como uno de los controles de frontera de entrada;
- tratar `Sniffer` y `has_header()` como heurísticas y no como autoridades;
- manejar BOM UTF-8 solo cuando la interfaz circundante lo requiera;
- distinguir la seguridad del parsing CSV de la interpretación de fórmulas por hojas de cálculo;
- diseñar contratos explícitos y comprobables de importación y exportación CSV.

## 1. ¿Qué cambia respecto de la introducción a CSV de la Fase 7?

Ya conoces las APIs centrales orientadas a filas:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

y las variantes orientadas a diccionarios:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])
```

La Fase 7 se centró en elegir el parser correcto y mantener el parsing separado de la validación.

Este capítulo se centra en la política alrededor del parser:

```text
bytes de texto
   ↓ decodificación de caracteres
texto Python
   ↓ dialecto CSV + política de parsing
filas y campos
   ↓ schema + validación de tipos
valores confiables para la aplicación
```

Las APIs son conocidas. El contrato es más profundo.

## 2. CSV no es un único dialecto universal

El nombre CSV sugiere valores separados por comas, pero las interfaces reales de texto tabular difieren en varios aspectos:

- delimitador;
- carácter de comillas;
- regla de escaping;
- terminador de línea;
- si los espacios después de delimitadores son significativos;
- si una entrada malformada debe aceptarse o rechazarse;
- si existe encabezado;
- qué significan los nombres de las columnas;
- qué codificación de texto transporta el archivo.

RFC 4180 documenta un formato CSV común y el media type `text/csv`, pero es informativo y no elimina los muchos dialectos utilizados en la práctica.

Por lo tanto, un nombre de archivo terminado en `.csv` no es un contrato completo de parsing.

## 3. La codificación de texto y el dialecto CSV son capas separadas

Un parser CSV opera sobre texto. Si la fuente está almacenada como bytes, la decodificación de caracteres ocurre primero.

Mantén las capas separadas:

```text
bytes
   ↓ UTF-8, UTF-8 con BOM u otra codificación declarada
texto
   ↓ reglas de delimitador + quoting + escaping
campos
```

Para un contrato UTF-8:

```python
with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Cambiar `delimiter=","` por `delimiter=";"` no cambia la codificación de caracteres. Cambiar `encoding="utf-8"` no elige el delimitador CSV.

## 4. Usa `newline=""` para objetos de archivo CSV

Cuando se pasa un archivo real al módulo `csv`, ábrelo con `newline=""`:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)
```

El módulo `csv` realiza su propio manejo de nuevas líneas. La documentación oficial señala que omitir `newline=""` puede romper nuevas líneas incrustadas dentro de campos entre comillas y puede introducir un carriage return adicional al escribir en plataformas que usan finales de línea `\r\n`.

Trata `newline=""` como parte del patrón de I/O de archivos CSV, no como sintaxis decorativa.

## 5. Un registro CSV puede ocupar varias líneas físicas

Este es un único registro CSV lógico:

```text
name,note
Ada,"first line
second line"
```

La nueva línea dentro del campo entre comillas pertenece a los datos del campo. No necesariamente termina el registro CSV.

Por eso, código como este no es seguro para parsing CSV general:

```python
for line in file:
    columns = line.split(",")
```

Un parser CSV entiende quoting y fronteras de registros. Un bucle por líneas físicas, por sí solo, no tiene información suficiente.

## 6. Un dialecto agrupa decisiones de formato

Python agrupa opciones relacionadas de formato CSV en un **dialecto**.

Un dialecto puede definir configuraciones como:

- `delimiter`;
- `quotechar`;
- `doublequote`;
- `escapechar`;
- `lineterminator`;
- `quoting`;
- `skipinitialspace`;
- `strict`.

Puedes proporcionar un dialecto con nombre:

```python
reader = csv.reader(file, dialect="excel")
```

o proporcionar parámetros de formato directamente:

```python
reader = csv.reader(
    file,
    delimiter=";",
    quotechar='"',
    strict=True,
)
```

Lo importante no es si la política tiene nombre o está inline. Lo importante es que productor y consumidor estén de acuerdo con ella.

## 7. Python incluye varios dialectos registrados

Los nombres incorporados comunes incluyen:

- `excel`;
- `excel-tab`;
- `unix`.

Puedes inspeccionar los nombres registrados:

```python
import csv

print(csv.list_dialects())
```

No supongas que un archivo producido por una aplicación de hojas de cálculo coincide automáticamente con cada detalle del dialecto `excel` de Python. Las opciones de exportación, locale, comportamiento de la aplicación y transformaciones posteriores pueden cambiar el contrato de texto real.

Inspecciona o documenta la interfaz que realmente recibes.

## 8. Registra un dialecto con nombre cuando la reutilización mejora la claridad

Una aplicación controlada puede registrar una política de dialecto repetida:

```python
import csv

csv.register_dialect(
    "study_semicolon",
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
```

Después puede reutilizarse:

```python
reader = csv.reader(file, dialect="study_semicolon")
```

Otras herramientas relacionadas incluyen:

- `csv.get_dialect()`;
- `csv.list_dialects()`;
- `csv.unregister_dialect()`.

Registra un nombre compartido en el proceso solo cuando ese nombre haga el contrato más fácil de entender. Los parámetros explícitos pueden ser más claros para una frontera de uso único.

## 9. Los parámetros de formato pueden sobrescribir un dialecto

`reader()` y `writer()` aceptan un dialecto y también parámetros individuales de formato. Esos parámetros pueden sobrescribir partes del dialecto seleccionado.

Por ejemplo:

```python
reader = csv.reader(
    file,
    dialect="excel",
    delimiter=";",
)
```

El resultado ya no es simplemente "el dialecto Excel". Es el dialecto Excel con un override de delimitador.

Al diagnosticar una interfaz, inspecciona la política efectiva completa en lugar de razonar solo a partir del nombre del dialecto.

## 10. El delimitador es un separador de campos de un carácter

El dialecto `excel` predeterminado usa una coma:

```python
reader = csv.reader(file, delimiter=",")
```

Un contrato con punto y coma puede ser explícito:

```python
reader = csv.reader(file, delimiter=";")
```

La configuración `delimiter` es una cadena de un carácter. Separadores de varios caracteres pertenecen a otro diseño de parsing.

No adivines el delimitador a partir de convenciones regionales cuando el productor pueda definirlo explícitamente.

## 11. `quotechar` protege contenido especial

El carácter de comillas predeterminado es la comilla doble:

```text
name,note
Ada,"commas, stay inside this field"
```

Las comillas forman parte de la representación CSV y normalmente no forman parte del valor devuelto del campo.

Con la política normal `doublequote=True`, una comilla dentro de un campo entre comillas se representa duplicándola:

```text
name,note
Ada,"She said ""hello"""
```

El reader reconstruye el contenido del campo según el dialecto.

## 12. `doublequote` y `escapechar` definen cómo se escapan las comillas

Cuando `doublequote=True`, un `quotechar` interno se duplica.

Cuando `doublequote=False`, se utiliza en su lugar el `escapechar` configurado.

Por ejemplo:

```python
writer = csv.writer(
    file,
    doublequote=False,
    escapechar="\\",
)
```

Si `doublequote=False` y no existe `escapechar`, escribir un campo que contenga el carácter de comillas puede lanzar `csv.Error`.

Escaping es una regla de representación. Debe coincidir con las expectativas del consumidor.

## 13. Los modos de quoting son política de parser y writer

Python expone varias constantes `QUOTE_*`:

| Modo | Idea principal |
|---|---|
| `QUOTE_MINIMAL` | Poner comillas solo en campos que las requieren por caracteres especiales |
| `QUOTE_ALL` | Poner comillas en todos los campos |
| `QUOTE_NONNUMERIC` | Poner comillas en campos de salida no numéricos y convertir campos de entrada sin comillas a `float` |
| `QUOTE_NONE` | Nunca usar quoting; escaping pasa a ser necesario para caracteres especiales |
| `QUOTE_NOTNULL` | Python 3.12+: distinguir campos vacíos sin comillas como `None` |
| `QUOTE_STRINGS` | Python 3.12+: poner comillas en strings y usar campos vacíos sin comillas para `None` |

El modo no es solamente formato visual. Algunos modos también cambian el comportamiento de decodificación.

## 14. `QUOTE_MINIMAL` y `QUOTE_ALL` expresan políticas de salida diferentes

`QUOTE_MINIMAL` es el valor predeterminado más habitual:

```python
writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
```

Solo los campos que requieren comillas según el dialecto se citan.

`QUOTE_ALL` pone comillas en todos los campos:

```python
writer = csv.writer(file, quoting=csv.QUOTE_ALL)
```

Poner comillas en todos los campos puede hacer la representación más uniforme, pero no resuelve automáticamente validación de schema, diferencias de encoding o cuestiones de seguridad específicas de hojas de cálculo.

## 15. `QUOTE_NONE` exige una política deliberada de escaping

Con `QUOTE_NONE`, el writer nunca pone campos entre comillas:

```python
writer = csv.writer(
    file,
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
)
```

Los caracteres que requieren escaping reciben como prefijo el `escapechar` configurado.

Si no se configura `escapechar` y un campo contiene un carácter que requiere escaping, el writer lanza `csv.Error`.

Usa `QUOTE_NONE` solo cuando la interfaz receptora defina reglas de escaping compatibles.

## 16. `QUOTE_NONNUMERIC` cambia los tipos de entrada

Por defecto, los readers CSV devuelven campos como strings.

`QUOTE_NONNUMERIC` es diferente. Al leer, los campos sin comillas se convierten a `float`:

```python
import csv
from io import StringIO

source = StringIO('"name","score"\n"Ada",91\n')
reader = csv.reader(source, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    print(row)
```

El campo numérico `91` se convierte en `91.0` porque no estaba entre comillas.

Esta es una regla de conversión guiada por la representación, no un sistema completo de tipos de la aplicación. Algunos valores numéricos de Python, incluyendo tipos cuya representación en string no puede convertirse a `float`, no son adecuados para round trip con este modo.

Para muchos contratos de aplicación, la conversión explícita después del parsing normal de strings es más fácil de validar y explicar.

## 17. Python 3.12 añadió `QUOTE_NOTNULL`; el soporte del reader se corrigió en 3.13

`csv.QUOTE_NOTNULL` fue añadido en Python 3.12. Su comportamiento de escritura está disponible en esa versión, pero Python 3.12 tiene un bug documentado: esta constante no afecta a los objetos `reader`. Ese bug de lectura fue corregido en Python 3.13.

Al escribir en Python 3.12+, pone comillas en todo campo que no sea `None`. Un valor `None` se escribe como campo vacío sin comillas.

A partir de Python 3.13, al leer, un campo vacío sin comillas se convierte en `None`, mientras que los demás campos se comportan como en `QUOTE_ALL`.

Esto crea una distinción a nivel de representación entre:

```text

```

y:

```text
""
```

A partir de Python 3.13, el primero puede leerse como `None` bajo este modo, mientras que la cadena vacía entre comillas continúa siendo una cadena vacía.

Úsalo solo cuando ambos lados de la interfaz estén de acuerdo con ese significado y documenta si el contrato necesita soporte de escritura desde Python 3.12 o la semántica nullable del reader a partir de Python 3.13.

## 18. Python 3.12 añadió `QUOTE_STRINGS`; el soporte del reader se corrigió en 3.13

`csv.QUOTE_STRINGS` también fue añadido en Python 3.12. Su comportamiento de escritura está disponible en esa versión, pero su comportamiento especial de lectura está afectado por el mismo bug de Python 3.12 y requiere Python 3.13+.

Al escribir en Python 3.12+, los campos string siempre reciben comillas, mientras que `None` se convierte en un campo vacío sin comillas.

A partir de Python 3.13, al leer, los campos vacíos sin comillas se convierten en `None`, y el comportamiento restante sigue `QUOTE_NONNUMERIC`, incluyendo la conversión de campos no vacíos y sin comillas a `float`.

Ese comportamiento de conversión significa que el modo no es simplemente "pon comillas en todas las strings". También transporta una política de decodificación.

Las constantes específicas de versión deben documentarse en interfaces que puedan ejecutarse en versiones anteriores de Python.

## 19. La conversión predeterminada de `None` del writer pierde información

El writer CSV normal escribe `None` como una cadena vacía:

```python
import csv
from io import StringIO

output = StringIO(newline="")
writer = csv.writer(output, lineterminator="\n")
writer.writerow(["Ada", None, ""])

print(output.getvalue())
```

Por lo tanto, tanto `None` como la cadena vacía pueden convertirse en campos vacíos con la política predeterminada.

Esa transformación es intencionalmente no reversible.

Si tu aplicación necesita distinguir valores ausentes de cadenas vacías, define una representación explícita, como:

- un texto centinela documentado;
- una representación nullable definida por el schema;
- `QUOTE_NOTNULL` o `QUOTE_STRINGS` en Python 3.12+ cuando su semántica encaje en la interfaz;
- otro formato de datos cuando CSV no pueda preservar claramente las distinciones necesarias.

## 20. Los campos CSV son strings por defecto, no valores inferidos de la aplicación

Con el comportamiento normal de `csv.reader()`:

```text
91
false
2026-08-28
```

todos llegan como campos de texto.

Tu programa decide si significan:

- un entero;
- un booleano;
- una fecha;
- o simplemente una cadena.

Mantén visibles las etapas:

```text
texto del campo CSV
   ↓ conversión de la aplicación
valor candidato
   ↓ validación
valor confiable
```

No dependas solo de la apariencia de un campo para definir su tipo.

## 21. Convierte y valida después del parsing

Un conversor estrecho hace que el contrato sea comprobable:

```python
def parse_score(text: str) -> int:
    score = int(text)
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score
```

El parser CSV responde dónde termina un campo y comienza el siguiente. El conversor responde qué significa un campo para la aplicación.

Son responsabilidades distintas.

## 22. `DictReader` hace que el encabezado forme parte de la interfaz

Cuando se omite `fieldnames`, `DictReader` usa el primer registro como claves del diccionario y no devuelve ese registro como dato:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])
```

Si proporcionas `fieldnames` explícitamente, la primera fila se trata como dato.

Esa diferencia importa cuando una interfaz no tiene encabezado o cuando la aplicación proporciona un schema fijo independientemente del archivo.

## 23. `restkey` y `restval` revelan anchos irregulares de filas

Un `DictReader` puede encontrar filas con más o menos campos que el encabezado.

Si una fila tiene campos extra, se almacenan en una lista bajo `restkey`. El `restkey` predeterminado es `None`.

Si una fila no vacía tiene menos campos, los valores ausentes se rellenan con `restval`. El valor predeterminado es `None`.

Para validación, un objeto centinela privado puede hacer visibles los campos ausentes sin colisionar con texto CSV legítimo:

```python
missing = object()
reader = csv.DictReader(
    file,
    restkey="_extra_fields",
    restval=missing,
)
```

Como los campos CSV normales son strings, este objeto privado no puede confundirse con texto legítimo de un campo. Tu aplicación puede rechazar campos extra con `row.get(restkey)` y campos ausentes mediante una comprobación de identidad como `value is missing`.

No permitas que la recuperación del parser se convierta silenciosamente en aceptación por parte de la aplicación.

## 24. Los nombres duplicados de encabezado necesitan una política explícita

Un contrato tabular normalmente espera nombres de columnas únicos.

Antes de depender del acceso por diccionario, valida el encabezado cuando la unicidad importe:

```python
def require_unique_header(header: list[str]) -> None:
    if len(header) != len(set(header)):
        raise ValueError("CSV header contains duplicate names")
```

Un enfoque claro es:

```text
leer encabezado como fila normal
   ↓ validar nombres, orden y unicidad
crear o continuar la política de lectura de filas
```

Un diccionario no puede preservar dos valores independientes bajo el mismo nombre de clave. Si las columnas duplicadas son significativas, una interfaz orientada a diccionario probablemente sea la abstracción equivocada.

## 25. `DictWriter` hace explícito el orden de las columnas de salida

`DictWriter` requiere `fieldnames`:

```python
import csv

fieldnames = ["name", "score", "status"]

with open("records.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {"name": "Ada", "score": 91, "status": "complete"}
    )
```

La secuencia de fieldnames define el orden de las columnas de salida.

Eso hace que el schema sea más fácil de revisar que depender de una construcción arbitraria de diccionarios en otro lugar del programa.

## 26. `extrasaction` controla claves inesperadas del diccionario

Por defecto, `DictWriter` lanza `ValueError` cuando un diccionario de entrada contiene una clave que no aparece en `fieldnames`.

Puedes elegir:

```python
writer = csv.DictWriter(
    file,
    fieldnames=fieldnames,
    extrasaction="ignore",
)
```

pero ignorar claves inesperadas puede descartar datos silenciosamente.

Prefiere el comportamiento predeterminado `"raise"` a menos que eliminar claves extra sea una política de exportación deliberada y documentada.

## 27. Las claves ausentes de `DictWriter` usan `restval`

Si un diccionario de entrada no contiene uno de los campos de salida configurados, `DictWriter` escribe su `restval`. El valor predeterminado es una cadena vacía.

Puedes hacer explícita la política:

```python
writer = csv.DictWriter(
    file,
    fieldnames=fieldnames,
    restval="N/A",
)
```

Un centinela como `N/A` solo es apropiado si el contrato receptor le asigna ese significado.

No inventes texto placeholder solamente para hacer rectangular una fila.

## 28. `strict=True` puede hacer que CSV malformado falle de forma visible

La opción `strict` de un dialecto es `False` por defecto.

Cuando `strict=True`, una entrada CSV malformada detectada por el parser lanza `csv.Error`:

```python
reader = csv.reader(file, strict=True)
```

Captura `csv.Error` donde puedas informar o recuperarte de forma útil:

```python
try:
    rows = list(reader)
except csv.Error as error:
    print(f"Invalid CSV: {error}")
```

El parsing estricto todavía no valida tu encabezado, tipos, campos obligatorios o reglas de negocio.

## 29. `reader.line_num` cuenta líneas leídas de la fuente, no registros lógicos

Los objetos reader exponen `line_num`.

Como un registro CSV puede ocupar varias líneas físicas, `line_num` es el número de líneas leídas de la fuente, no simplemente la cantidad de registros devueltos.

Esto es útil para diagnósticos, pero etiquétalo correctamente:

```text
contexto de línea de la fuente
```

no siempre es igual a:

```text
número de registro
```

## 30. `field_size_limit()` puede limitar campos individuales procesados

El módulo expone el tamaño máximo actual de campo aceptado por el parser:

```python
import csv

current_limit = csv.field_size_limit()
print(current_limit)
```

Puedes establecer un nuevo límite:

```python
csv.field_size_limit(1_000_000)
```

Un límite de tamaño de campo puede formar parte de una política de frontera de entrada, pero no sustituye límites de tamaño total de archivo, número de registros, tiempo de procesamiento o contenido específico de la aplicación.

Si cambias el límite en un proceso compartido, documenta la decisión porque afecta el parsing CSV posterior en ese intérprete.

## 31. `Sniffer.sniff()` es una heurística

`csv.Sniffer` puede inspeccionar una muestra e inferir un dialecto:

```python
import csv

sample = "name;score\nAda;91\nLin;88\n"
dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")

print(dialect.delimiter)
```

Esto es útil cuando el productor no puede declarar el delimitador, pero inferencia no significa certeza.

Restringir los delimitadores candidatos puede alinear mejor la heurística con los formatos que la aplicación realmente admite.

## 32. Reposiciona el archivo después de leer la muestra

Al usar Sniffer con un archivo, leer una muestra avanza la posición del archivo:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    sample = file.read(1024)
    dialect = csv.Sniffer().sniff(sample)
    file.seek(0)
    reader = csv.reader(file, dialect)
```

Sin `file.seek(0)`, el parsing comenzaría después de la muestra y no al inicio del archivo.

El muestreo es una operación de I/O, por lo que la posición del cursor forma parte del flujo.

## 33. `Sniffer.has_header()` también es una heurística

`has_header()` examina una muestra e intenta adivinar si el primer registro parece contener nombres de columnas.

La documentación oficial describe explícitamente este método como una heurística aproximada que puede producir falsos positivos y falsos negativos.

Por lo tanto:

```text
Sniffer dice que hay encabezado
```

no debe significar automáticamente:

```text
el contrato de la interfaz garantiza encabezado
```

Si el productor puede especificar si existe encabezado, usa ese contrato explícito en lugar de adivinar.

## 34. `skipinitialspace=True` no es limpieza general de espacios

Con `skipinitialspace=True`, se ignoran los espacios inmediatamente después del delimitador:

```python
reader = csv.reader(file, skipinitialspace=True)
```

Esa es una regla de dialecto, no una instrucción general para recortar todos los campos.

Por ejemplo, los espacios iniciales o finales dentro de contenido entre comillas todavía pueden ser datos significativos.

Evita aplicar `.strip()` ciegamente a menos que el contrato de la aplicación defina explícitamente esa normalización.

## 35. `lineterminator` es principalmente una política del writer

El writer usa `lineterminator` para finalizar registros de salida. Su valor predeterminado es `"\r\n"`.

Puedes definir una representación controlada:

```python
writer = csv.writer(file, lineterminator="\n")
```

El comportamiento actual del reader es diferente: reconoce `\r` o `\n` como final de línea e ignora la configuración `lineterminator` del dialecto.

No supongas que un terminador personalizado del writer se convierte en una regla simétrica del reader.

## 36. El manejo de BOM UTF-8 pertenece a la frontera de texto

Algunos productores CSV, especialmente flujos orientados a hojas de cálculo, pueden generar texto UTF-8 con un byte-order mark al principio.

Si la interfaz permite explícitamente esa representación, el codec `utf-8-sig` de Python puede consumir el BOM durante la decodificación:

```python
with open("records.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)
```

No uses `utf-8-sig` como un botón mágico de reparación CSV. Decide si la entrada con BOM realmente forma parte del contrato de texto admitido.

El encoding sigue separado de las reglas de delimitador y quoting.

## 37. Los parsers CSV no evalúan fórmulas de hojas de cálculo

El módulo `csv` procesa campos de texto. No ejecuta fórmulas de hojas de cálculo.

El riesgo puede aparecer después, cuando datos CSV exportados que contienen texto no confiable se abren en software de hojas de cálculo. Algunas aplicaciones pueden interpretar como fórmulas valores de celdas que comienzan con caracteres como `=`, `+`, `-` o `@`.

Eso crea dos preguntas distintas:

```text
¿Este campo está escapado correctamente como CSV?
```

y:

```text
¿La hoja de cálculo de destino interpretará esta celda como contenido ejecutable de fórmula?
```

El quoting CSV correcto no responde universalmente a la segunda pregunta.

No existe una única transformación de sanitización segura para todas las aplicaciones de hojas de cálculo y todos los consumidores programáticos posteriores. Si una exportación está destinada a visualizarse en hojas de cálculo y contiene datos no confiables, define y prueba una política de mitigación específica para el destino.

## 38. Valida el schema tabular después del parsing

Una frontera de importación útil puede validar varias capas de forma independiente:

```text
codificación de texto
   ↓
sintaxis CSV y dialecto
   ↓
nombres y unicidad del encabezado
   ↓
ancho de fila
   ↓
conversión de tipos de campos
   ↓
reglas de valor de campos
```

Por ejemplo, una tabla de puntuaciones puede requerir:

```text
encabezado exacto: name,score,status
name: texto no vacío
score: entero 0..100
status: uno de complete, review
sin campos extra
sin campos ausentes
```

La sintaxis CSV por sí sola no puede imponer esas reglas.

## 39. Errores comunes

### Error 1: suponer que `.csv` significa coma más configuración Excel predeterminada

La extensión no define cada regla de dialecto y encoding.

### Error 2: omitir `newline=""` en objetos de archivo CSV reales

Eso puede romper nuevas líneas incrustadas y finales de línea de salida.

### Error 3: separar líneas físicas manualmente

Los campos CSV entre comillas pueden contener delimitadores y nuevas líneas incrustadas.

### Error 4: tratar `QUOTE_NONNUMERIC` como conversor completo de schema

Solo aplica una regla específica de conversión a `float` guiada por la representación.

### Error 5: olvidar que la salida predeterminada de `None` pierde información

`None` y una cadena vacía pueden serializarse al mismo campo vacío.

### Error 6: aceptar filas irregulares de `DictReader` sin comprobar `restkey` y `restval`

La recuperación del parser puede ocultar formas de tabla inválidas.

### Error 7: usar `extrasaction="ignore"` solo para silenciar errores de exportación

Campos inesperados pueden desaparecer sin aviso.

### Error 8: confiar en `Sniffer` como detector garantizado de schema

La detección de delimitador y encabezado es heurística.

### Error 9: usar `.strip()` automáticamente en todos los campos

Los espacios pueden ser datos significativos.

### Error 10: suponer que quoting CSV correcto impide la interpretación de fórmulas en hojas de cálculo

La seguridad de sintaxis CSV y el comportamiento de ejecución de hojas de cálculo son preocupaciones separadas.

## 40. Ejemplo práctico: round trip con dialecto explícito

```python
import csv
from io import StringIO


rows = [
    ["name", "note"],
    ["Ada", "comma, semicolon; and newline\ninside"],
    ["Lin", 'She said "hello"'],
]

output = StringIO(newline="")
writer = csv.writer(
    output,
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerows(rows)

text = output.getvalue()
print(text)

source = StringIO(text, newline="")
reader = csv.reader(
    source,
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
)
print(list(reader))
```

Versión ejecutable: [`examples/dialect_round_trip.py`](examples/dialect_round_trip.py).

## 41. Ejemplo práctico: validar filas de diccionario

```python
import csv
from io import StringIO


text = "name,score,status\nAda,91,complete\nLin,88,review\n"
source = StringIO(text, newline="")
missing = object()
reader = csv.DictReader(
    source,
    restkey="_extra_fields",
    restval=missing,
)

expected_fields = ["name", "score", "status"]
if reader.fieldnames != expected_fields:
    raise ValueError("unexpected CSV header")

records = []
for row in reader:
    if row.get("_extra_fields") is not None:
        raise ValueError("row contains extra fields")
    if any(value is missing for value in row.values()):
        raise ValueError("row contains missing fields")

    score = int(row["score"])
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    records.append(
        {
            "name": row["name"],
            "score": score,
            "status": row["status"],
        }
    )

print(records)
```

Versión ejecutable: [`examples/validate_dict_rows.py`](examples/validate_dict_rows.py).

## 42. Ejemplo práctico: detectar un delimitador permitido

```python
import csv
from io import StringIO


text = 'name;note\nAda;"uses, commas in text"\nLin;ready\n'
dialect = csv.Sniffer().sniff(text, delimiters=",;\t")

print(repr(dialect.delimiter))

source = StringIO(text, newline="")
reader = csv.reader(source, dialect)
print(list(reader))
```

Versión ejecutable: [`examples/sniff_delimiter.py`](examples/sniff_delimiter.py).

## 43. Ejemplo práctico: escaping sin quoting

```python
import csv
from io import StringIO


row = ["alpha,beta", 'quoted "text"', "line\nbreak"]

output = StringIO(newline="")
writer = csv.writer(
    output,
    delimiter=",",
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
    lineterminator="\n",
)
writer.writerow(row)

text = output.getvalue()
print(repr(text))

source = StringIO(text, newline="")
reader = csv.reader(
    source,
    delimiter=",",
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
)
print(next(reader))
```

Versión ejecutable: [`examples/quote_none_escape.py`](examples/quote_none_escape.py).

## 44. Ejercicio

Crea una función llamada `decode_results(text)` para un contrato controlado de importación CSV.

Requisitos:

1. Analiza texto CSV con `StringIO` y `csv.DictReader`.
2. Exige el encabezado exacto `name,score,status` en ese orden.
3. Rechaza nombres de encabezado duplicados.
4. Rechaza filas con campos extra.
5. Rechaza filas con campos ausentes.
6. Exige que `name` no esté vacío después de la política de normalización que elijas explícitamente.
7. Convierte `score` a `int` y exige un valor de 0 a 100.
8. Exige que `status` sea `complete` o `review`.
9. Devuelve una lista de diccionarios validados cuyos valores `score` sean enteros.

Luego crea `encode_results(records)` que:

1. escriba los mismos tres campos en el mismo orden;
2. escriba el encabezado explícitamente;
3. use `lineterminator="\n"` para una salida determinista;
4. rechace diccionarios con claves inesperadas en lugar de descartarlas silenciosamente;
5. devuelva el texto CSV generado.

Prueba al menos estos casos:

```text
filas válidas
orden incorrecto del encabezado
encabezado duplicado
campo extra
campo ausente
score = texto
score = 101
status desconocido
campo que contiene una coma
campo que contiene una nueva línea incrustada
```

Lo importante no es solo procesar filas válidas. Haz visible cada suposición sobre la tabla para que otro programador pueda explicar por qué se rechaza un archivo inválido.

## 45. Referencia rápida

| Necesidad | Herramienta / política |
|---|---|
| Leer filas CSV | `csv.reader()` |
| Escribir filas CSV | `csv.writer()` |
| Leer filas por nombre de columna | `csv.DictReader()` |
| Escribir diccionarios en orden fijo de columnas | `csv.DictWriter()` |
| Abrir correctamente archivos CSV reales | `newline=""` |
| Elegir separador de campos | `delimiter=...` |
| Elegir carácter de comillas | `quotechar=...` |
| Escapar sin quoting normal | `escapechar=...`, frecuentemente con `QUOTE_NONE` |
| Poner comillas solo cuando sea necesario | `csv.QUOTE_MINIMAL` |
| Poner comillas en todos los campos | `csv.QUOTE_ALL` |
| Convertir campos de entrada sin comillas a `float` | `csv.QUOTE_NONNUMERIC` |
| Distinguir `None` de cadena vacía entre comillas al escribir (3.12+) y al leer (3.13+) | `csv.QUOTE_NOTNULL` |
| Poner comillas en strings / representar `None` al escribir (3.12+); usar semántica nullable del reader desde 3.13 | `csv.QUOTE_STRINGS` |
| Rechazar entrada malformada del parser con mayor rigor | `strict=True` |
| Detectar ancho irregular de fila en `DictReader` | `restkey=...`, `restval=...` |
| Rechazar o ignorar claves extra en `DictWriter` | `extrasaction="raise"` / `"ignore"` |
| Controlar final de registro del writer | `lineterminator=...` |
| Limitar tamaño de campo del parser | `csv.field_size_limit()` |
| Inferir dialecto a partir de una muestra | `csv.Sniffer().sniff()` |
| Inferir si existe encabezado | `csv.Sniffer().has_header()` |
| Leer texto UTF-8 que puede comenzar con BOM | `encoding="utf-8-sig"` |
| Capturar errores del parser CSV | `csv.Error` |

## 46. Checklist de diseño

Antes de publicar o consumir una interfaz CSV, pregunta:

```text
¿Qué codificación de caracteres se usa?
¿Se permite BOM UTF-8?
¿Qué delimitador es obligatorio?
¿Qué reglas de comillas y escaping son obligatorias?
¿Qué final de línea escribe el productor?
¿Existe encabezado?
¿Los nombres del encabezado son únicos y case-sensitive?
¿Es significativa la ordenación de columnas?
¿Cómo se manejan campos ausentes y extra?
¿Cómo se representa None de manera distinta de una cadena vacía?
¿Qué campos requieren conversión explícita de tipos?
¿Qué límites de archivo, campo y cantidad de filas se aplican?
¿Se permite detección de dialecto o el formato debe ser explícito?
¿Los campos no confiables se abrirán después en software de hojas de cálculo?
```

Si esas respuestas son explícitas, CSV se convierte en una interfaz comprobable en lugar de una colección de suposiciones escondidas detrás de la extensión `.csv`.

## Referencias

- [Documentación de Python 3.14: `csv` — lectura y escritura de archivos CSV](https://docs.python.org/3.14/library/csv.html)
- [Documentación de Python 3.14: `codecs` — registro de codecs y clases base](https://docs.python.org/3.14/library/codecs.html)
- [RFC 4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://www.rfc-editor.org/rfc/rfc4180)
- [OWASP: CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection)

## Próximo capítulo

Continúa con el [**Capítulo 05: Diseñando Pipelines de Logging y Contratos de Contexto en Runtime**](../05-logging/README.es.md). Profundiza niveles efectivos, enrutamiento por handlers, propagación, configuración, registros contextuales, entrega mediante colas, concurrencia y seguridad operativa de logging.
