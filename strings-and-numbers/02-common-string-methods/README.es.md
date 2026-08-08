# Métodos Comunes de Strings

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Creación e indexación de strings](../01-string-creation-and-indexing/README.es.md)

El capítulo anterior enseñó cómo crear strings y leer sus posiciones e intervalos. Este capítulo añade una nueva idea: las strings también ofrecen **métodos**, operaciones reutilizables que pueden inspeccionar texto o producir un resultado de tipo string sin modificar el valor original.

Aprenderás un conjunto enfocado de métodos que aparece constantemente en programas reales. El objetivo no es memorizar toda la API de `str`. Es comprender el patrón de llamada de métodos, reconocer tareas comunes con texto y elegir una operación cuyo comportamiento corresponda a tu intención.

## Información del capítulo

| Elemento | Valor |
|---|---|
| Fase | 2 — Textos y números |
| Capítulo | 02 |
| Nivel | Principiante |
| Prerrequisito | Capítulo 01 — Creación e indexación de strings |
| Tipo principal | `str` |
| Idea principal | Llamar métodos comunes de strings deliberadamente, respetando la inmutabilidad |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué es un método de string;
- llamar métodos mediante notación con punto;
- distinguir la string original del resultado de un método;
- normalizar mayúsculas y minúsculas con `lower()` y `upper()`;
- eliminar espacios en blanco alrededor con `strip()`;
- eliminar prefijos y sufijos exactos con `removeprefix()` y `removesuffix()`;
- reemplazar texto con `replace()`;
- comprobar comienzos y finales con `startswith()` y `endswith()`;
- localizar y contar substrings con `find()` y `count()`;
- dividir texto en partes con `split()`;
- unir strings con `join()`;
- combinar algunos métodos sin ocultar la intención del programa.

## 1. ¿Qué es un método?

Un **método** es una operación parecida a una función asociada a un objeto.

Un valor de string sabe realizar operaciones específicas de strings. Le pides una de ellas mediante **notación con punto**:

```python
language = "Python"

print(language.upper())
```

```text
PYTHON
```

El punto conecta el valor de la izquierda con un método proporcionado por su tipo.

```text
value.method(arguments)
```

Algunos métodos no reciben argumentos. Otros necesitan información entre los paréntesis.

## 2. Los métodos pertenecen a los valores, no a los nombres de variables

No es el nombre de la variable el que posee el método. Es el valor de string.

Estas dos llamadas son válidas:

```python
language = "Python"

print(language.lower())
print("Practice".lower())
```

```text
python
practice
```

Un nombre es simplemente una forma de referirse a un valor. Esto conecta directamente con la distinción entre nombres y valores estudiada en la Fase 1.

## 3. Los métodos de string no editan la string original en el lugar

Las strings son inmutables. Un método como `lower()` produce un resultado, pero no reescribe el valor de string que ya existía.

```python
language = "Python"

lowercase_language = language.lower()

print(language)
print(lowercase_language)
```

```text
Python
python
```

Si necesitas conservar el resultado, asígnalo a un nombre.

```python
language = "Python"
language = language.lower()

print(language)
```

```text
python
```

Eso es reasignación. La string original no fue modificada.

## 4. `lower()` y `upper()` cambian el uso de mayúsculas en el resultado

Usa `lower()` cuando necesites un resultado en minúsculas:

```python
message = "Python Practice"

print(message.lower())
```

```text
python practice
```

Usa `upper()` cuando necesites un resultado en mayúsculas:

```python
message = "Python Practice"

print(message.upper())
```

```text
PYTHON PRACTICE
```

La conversión entre mayúsculas y minúsculas es útil para presentación y para algunas tareas de normalización.

No supongas que cambiar las mayúsculas valida el significado. `"YES".lower()` se convierte en `"yes"`, pero tu programa aún necesita reglas para decidir qué significa `"yes"`.

## 5. Normaliza antes de comparar cuando las mayúsculas no deban importar

Supón que dos textos deben tratarse igual independientemente de sus mayúsculas y minúsculas.

```python
expected = "python"
received = "PyThOn"

print(received.lower() == expected)
```

```text
True
```

Este es un patrón común para principiantes.

Para comparaciones sin distinción de mayúsculas más avanzadas e internacionalizadas, Python también ofrece `casefold()`. Esa diferencia se pospone deliberadamente para mantener este capítulo centrado en las operaciones más comunes para principiantes.

## 6. `strip()` elimina espacios en blanco alrededor por defecto

La entrada del usuario y los textos externos a menudo contienen espacios o saltos de línea alrededor del contenido importante.

```python
raw_name = "   Python   "

clean_name = raw_name.strip()

print("[" + raw_name + "]")
print("[" + clean_name + "]")
```

```text
[   Python   ]
[Python]
```

Sin argumento, `strip()` elimina espacios en blanco iniciales y finales.

**No** elimina espacios del medio:

```python
text = "  Python Study Guide  "

print(text.strip())
```

```text
Python Study Guide
```

## 7. `strip(chars)` trata `chars` como un conjunto de caracteres eliminables

Este detalle importa.

```python
text = "...Python..."

print(text.strip("."))
```

```text
Python
```

Cuando se proporciona un argumento, `strip()` elimina combinaciones de esos caracteres de ambos extremos. No es un eliminador de "prefijo exacto" o "sufijo exacto".

Por eso este estilo puede ser engañoso:

```python
filename = "report.txt"

print(filename.strip(".txt"))
```

El argumento se trata como caracteres eliminables, no como el sufijo exacto `".txt"`.

Cuando la intención sea eliminar un prefijo o sufijo exacto, usa los métodos diseñados para esa tarea.

## 8. `removeprefix()` y `removesuffix()` eliminan texto exacto

**Nota de compatibilidad:** `str.removeprefix()` y `str.removesuffix()` se añadieron en Python 3.9. Por lo tanto, los ejemplos de esta sección requieren Python 3.9 o una versión posterior. En Python 3.8 o anteriores, estos métodos no están disponibles y llamarlos genera `AttributeError`.

Usa `removeprefix()` para un prefijo conocido:

```python
resource = "draft-report"

print(resource.removeprefix("draft-"))
```

```text
report
```

Usa `removesuffix()` para un sufijo conocido:

```python
filename = "report.txt"

print(filename.removesuffix(".txt"))
```

```text
report
```

Si el prefijo o sufijo exacto no está presente, el valor textual se conserva.

Estos métodos expresan la intención con más precisión que intentar imitar la eliminación de prefijos o sufijos mediante `strip()`.

## 9. `replace()` sustituye ocurrencias

`replace(old, new)` produce un resultado en el que las ocurrencias de `old` se sustituyen por `new`.

```python
sentence = "Python is clear. Python is practical."

print(sentence.replace("Python", "Code"))
```

```text
Code is clear. Code is practical.
```

Puedes limitar la cantidad de sustituciones con un tercer argumento:

```python
sentence = "one one one"

print(sentence.replace("one", "two", 1))
```

```text
two one one
```

`replace()` realiza sustitución textual. No comprende palabras, gramática, formatos de archivo ni significado de negocio a menos que tu programa añada esas reglas.

## 10. Usa `in` cuando solo necesitas saber si existe un texto

El operador de pertenencia suele ser la forma más clara de preguntar si una substring está presente.

```python
message = "Learn Python step by step"

print("Python" in message)
print("Java" in message)
```

```text
True
False
```

No es un método, pero pertenece junto a las herramientas de búsqueda de strings porque suele ser la mejor opción para una simple comprobación de presencia.

## 11. `startswith()` y `endswith()` expresan comprobaciones en los límites

Usa `startswith()` cuando importa el comienzo:

```python
filename = "report-2026.csv"

print(filename.startswith("report-"))
```

```text
True
```

Usa `endswith()` cuando importa el final:

```python
filename = "report-2026.csv"

print(filename.endswith(".csv"))
```

```text
True
```

Estos métodos devuelven valores booleanos, conectando el trabajo con strings con el tipo `bool` de la Fase 1.

## 12. `find()` devuelve la primera posición coincidente o `-1`

Usa `find()` cuando necesites la posición de una substring.

```python
message = "Learn Python"

print(message.find("Python"))
print(message.find("Java"))
```

```text
6
-1
```

Una substring encontrada devuelve su menor índice coincidente. Una substring ausente devuelve `-1`.

Si solo necesitas saber si la substring existe, prefiere `in` porque su resultado comunica directamente la pregunta.

## 13. `find()` e `index()` son parecidos, pero fallan de manera diferente

Las strings también ofrecen `index()`.

```python
message = "Learn Python"

print(message.index("Python"))
```

```text
6
```

La diferencia importante aparece cuando la substring no existe:

- `find()` devuelve `-1`;
- `index()` genera `ValueError`.

En código para principiantes, elige según el comportamiento que tu programa realmente necesite. No uses `index()` solo porque su nombre parezca más familiar.

## 14. `count()` cuenta ocurrencias no superpuestas

Usa `count()` cuando necesites la cantidad de ocurrencias.

```python
text = "banana"

print(text.count("a"))
print(text.count("na"))
```

```text
3
2
```

El conteo se basa en coincidencias que no se superponen.

Un conteo de cero significa que no se encontró la substring.

## 15. `split()` separa texto en una lista de strings

Sin un separador explícito, `split()` separa por secuencias de espacios en blanco.

```python
text = "Python   makes   text readable"

words = text.split()

print(words)
```

```text
['Python', 'makes', 'text', 'readable']
```

El resultado es una **lista** de strings.

Las listas tendrán su propia sección completa más adelante en la guía. Por ahora, solo necesitas reconocer que `split()` puede convertir una string en una colección ordenada de partes de tipo string.

## 16. `split(separator)` usa un delimitador explícito

Cuando proporcionas un separador, Python divide usando exactamente esa string separadora.

```python
record = "python|beginner|active"

parts = record.split("|")

print(parts)
```

```text
['python', 'beginner', 'active']
```

Esto es diferente del comportamiento de espacios en blanco de `split()` sin argumento.

Los separadores explícitos también pueden producir elementos string vacíos:

```python
record = "a||b"

print(record.split("|"))
```

```text
['a', '', 'b']
```

Ese elemento vacío es información: no había nada entre dos separadores.

## 17. El texto vacío se comporta de manera diferente con división predeterminada y explícita

Compara estas dos llamadas:

```python
text = ""

print(text.split())
print(text.split(","))
```

```text
[]
['']
```

Sin separador, una string vacía o que contiene solo espacios en blanco produce una lista vacía.

Con un separador explícito, una string vacía produce una lista que contiene una string vacía porque había un campo y ninguna aparición del separador.

Esta pequeña diferencia se vuelve importante al procesar datos delimitados.

## 18. `join()` combina strings usando un separador

`join()` suele parecer invertido al principio.

```python
words = ["Python", "Study", "Guide"]

print(" ".join(words))
print("-".join(words))
```

```text
Python Study Guide
Python-Study-Guide
```

La string **antes del punto** es el separador.

Una forma útil de leerlo es:

```text
separator.join(strings)
```

El separador pide colocarse entre los elementos string.

## 19. `join()` exige elementos de tipo string

Esto funciona:

```python
parts = ["chapter", "02", "methods"]

print("/".join(parts))
```

```text
chapter/02/methods
```

Pero `join()` no convierte automáticamente valores arbitrarios a texto. Si la colección contiene elementos que no son strings, Python genera `TypeError`.

Este diseño evita que conversiones silenciosas oculten errores. Convierte valores deliberadamente cuando el texto sea realmente la representación deseada.

## 20. Dividir y unir son ideas complementarias

Puedes dividir texto en partes y luego unir esas partes string con otro separador.

```python
path_text = "docs/guides/python"

parts = path_text.split("/")
rebuilt = " > ".join(parts)

print(parts)
print(rebuilt)
```

```text
['docs', 'guides', 'python']
docs > guides > python
```

La lista es una representación temporal de las partes. `join()` crea el resultado textual final.

## 21. Los métodos pueden encadenarse

Como muchos métodos de string devuelven resultados de tipo string, a veces otro método de string puede llamarse inmediatamente sobre ese resultado.

```python
raw_title = "  Python Guide  "

normalized_title = raw_title.strip().lower().replace(" ", "-")

print(normalized_title)
```

```text
python-guide
```

Las llamadas se evalúan de izquierda a derecha:

```text
raw_title
    -> strip()
    -> lower()
    -> replace(" ", "-")
```

El encadenamiento es conveniente cuando cada paso sigue siendo evidente.

## 22. No conviertas las cadenas de métodos en acertijos

Una expresión más corta no es automáticamente más clara.

Esto es legible:

```python
raw_title = "  Python Guide  "
clean_title = raw_title.strip()
lowercase_title = clean_title.lower()
normalized_title = lowercase_title.replace(" ", "-")

print(normalized_title)
```

```text
python-guide
```

Los valores intermedios con nombre son útiles cuando:

- una transformación necesita explicación;
- quieres inspeccionar un paso;
- la cadena está creciendo demasiado;
- distintos pasos representan distintas intenciones.

La claridad vale más que comprimir toda transformación en una sola línea.

## 23. Ejemplo práctico: normaliza una etiqueta

```python
raw_title = "  Python Study Guide  "

clean_title = raw_title.strip()
normalized_title = clean_title.lower().replace(" ", "-")

print("Raw:", "[" + raw_title + "]")
print("Clean:", clean_title)
print("Normalized:", normalized_title)
print("Starts with python:", clean_title.lower().startswith("python"))
print("Word count:", len(clean_title.split()))
```

```text
Raw: [  Python Study Guide  ]
Clean: Python Study Guide
Normalized: python-study-guide
Starts with python: True
Word count: 3
```

Este ejemplo combina limpieza, normalización de mayúsculas, reemplazo, comprobación de inicio y división de texto sin modificar la entrada original en el lugar.

## 24. Ejemplo práctico: divide y reconstruye un texto parecido a una ruta

```python
path_text = "docs/guides/python"

parts = path_text.split("/")

print("Parts:", parts)
print("Joined:", " > ".join(parts))
print("First separator:", path_text.find("/"))
print("Slash count:", path_text.count("/"))
print("Ends with python:", path_text.endswith("python"))
```

```text
Parts: ['docs', 'guides', 'python']
Joined: docs > guides > python
First separator: 4
Slash count: 2
Ends with python: True
```

Esto es texto simple deliberadamente, no lógica de sistema de archivos. Un capítulo posterior de la biblioteca estándar presentará `pathlib` para rutas reales del sistema de archivos.

## 25. Errores comunes

### Olvidar los paréntesis

Una llamada de método necesita paréntesis:

```python
language = "Python"

print(language.lower())
```

Sin `()`, te estás refiriendo al propio método en lugar de llamarlo.

### Esperar que un método modifique la string

```python
language = "Python"
language.lower()

print(language)
```

```text
Python
```

Guarda o reasigna el resultado cuando lo necesites.

### Usar `strip()` como eliminador de prefijo o sufijo exacto

`strip(chars)` elimina caracteres de ambos extremos según un conjunto de caracteres. Usa `removeprefix()` o `removesuffix()` para texto exacto en los límites.

### Usar `find()` directamente como booleano

Una substring encontrada puede estar en el índice `0`, y `0` es falso. Una substring ausente produce `-1`, y `-1` es verdadero.

Por eso esta es una mala comprobación de presencia:

```python
text = "Python"

print(bool(text.find("Python")))
print(bool(text.find("Java")))
```

```text
False
True
```

Usa `"Python" in text` cuando la pregunta sea simplemente si existe la substring.

### Olvidar que los separadores explícitos de `split()` conservan campos vacíos

`"a||b".split("|")` contiene una string vacía entre los dos separadores. No descartes ese hecho a menos que las reglas de tus datos indiquen que es seguro.

### Llamar `join()` sobre la colección en lugar del separador

El patrón es:

```text
separator.join(strings)
```

y no `strings.join(separator)`.

## 26. Conexiones con conceptos anteriores

Este capítulo combina varias ideas ya estudiadas:

- los valores de string son instancias de `str`;
- las strings son inmutables;
- los resultados de métodos pueden asignarse a variables;
- aparecen resultados `bool` en `startswith()` y `endswith()`;
- aparecen índices en `find()`;
- `len()` puede medir la lista devuelta por `split()`;
- la conversión de tipos sigue siendo explícita cuando valores que no son strings deben convertirse en texto.

También anticipa temas posteriores:

- las listas explicarán en profundidad el objeto devuelto por `split()`;
- los condicionales actuarán sobre resultados booleanos de búsqueda;
- los bucles procesarán muchas partes de strings;
- archivos y datos CSV exigirán divisiones cuidadosas o parsers estructurados;
- `pathlib` reemplazará trucos manuales con strings para rutas reales del sistema de archivos.

## 27. Ejercicio: limpia e inspecciona un valor de texto

Crea `text_methods_practice.py` con:

```python
raw_text = "  Python,practice,python  "
```

Produce y muestra:

1. el texto original rodeado por corchetes;
2. el texto después de `strip()`;
3. una versión en minúsculas;
4. la cantidad de ocurrencias de `"python"` en minúsculas después de normalizar;
5. una versión donde las comas se reemplazan por `" | "`;
6. si el texto limpio comienza con `"Python"`;
7. si termina con `"python"`;
8. la lista producida al dividir por comas;
9. las mismas partes unidas con `" -> "`.

Una forma posible de salida es:

```text
Original: [  Python,practice,python  ]
Clean: Python,practice,python
Lowercase: python,practice,python
Python count: 2
Replaced: Python | practice | python
Starts with Python: True
Ends with python: True
Parts: ['Python', 'practice', 'python']
Joined: Python -> practice -> python
```

Intenta resolver cada transformación por separado antes de comprimir pasos en una cadena de métodos.

## 28. Autoevaluación

Asegúrate de poder responder:

1. ¿Qué significa el punto en `text.lower()`?
2. ¿Por qué `text.lower()` no modifica `text` en el lugar?
3. ¿Qué elimina `strip()` cuando se llama sin argumentos?
4. ¿Por qué `strip(".txt")` no representa la misma idea que `removesuffix(".txt")`?
5. ¿Cuándo es `in` más claro que `find()`?
6. ¿Qué devuelve `find()` cuando no existe una coincidencia?
7. ¿Qué mide `count()`?
8. ¿Qué tipo devuelve `split()`?
9. ¿Por qué `split("|")` puede producir elementos string vacíos?
10. ¿Qué objeto proporciona el separador en `" - ".join(parts)`?
11. ¿Por qué una cadena de métodos larga puede reducir la legibilidad?
12. ¿Qué debes hacer cuando `join()` recibe valores que no son strings?

## 29. Referencia rápida

| Objetivo | Operación | Resultado de ejemplo |
|---|---|---|
| Minúsculas | `text.lower()` | `"Py".lower()` → `"py"` |
| Mayúsculas | `text.upper()` | `"Py".upper()` → `"PY"` |
| Quitar espacios alrededor | `text.strip()` | `"  Py  ".strip()` → `"Py"` |
| Eliminar prefijo exacto | `text.removeprefix(prefix)` | `"pre-item".removeprefix("pre-")` → `"item"` |
| Eliminar sufijo exacto | `text.removesuffix(suffix)` | `"file.txt".removesuffix(".txt")` → `"file"` |
| Reemplazar texto | `text.replace(old, new)` | `"a-b".replace("-", "/")` → `"a/b"` |
| Comprobar presencia | `sub in text` | `"Py" in "Python"` → `True` |
| Comprobar inicio | `text.startswith(prefix)` | `"Python".startswith("Py")` → `True` |
| Comprobar final | `text.endswith(suffix)` | `"a.py".endswith(".py")` → `True` |
| Encontrar primera posición | `text.find(sub)` | `"Python".find("th")` → `2` |
| Contar ocurrencias | `text.count(sub)` | `"banana".count("a")` → `3` |
| Dividir por espacios | `text.split()` | `"a  b".split()` → `['a', 'b']` |
| Dividir por delimitador | `text.split(sep)` | `"a|b".split("|")` → `['a', 'b']` |
| Unir strings | `sep.join(strings)` | `"-".join(["a", "b"])` → `"a-b"` |

## 30. Ejemplos del repositorio

Ejecuta los ejemplos deterministas:

```bash
python strings-and-numbers/02-common-string-methods/examples/normalize_text.py
python strings-and-numbers/02-common-string-methods/examples/split_and_join.py
```

Después ejecuta las verificaciones del repositorio:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 31. Qué viene después

Ahora puedes transformar, inspeccionar, dividir y unir texto manteniendo en mente la inmutabilidad de las strings.

El siguiente capítulo cambia el foco del texto a valores numéricos y lógicos: **`int`, `float` y `bool` con mayor profundidad**.

## Referencias oficiales

- [Tipos incorporados de Python — Tipo de secuencia de texto `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Tipos incorporados de Python — Métodos de string](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Tipos incorporados de Python — Resumen de métodos de secuencias de texto y binarias](https://docs.python.org/3/library/stdtypes.html#text-and-binary-sequence-type-methods-summary)
- [What’s New In Python 3.9 — New String Methods to Remove Prefixes and Suffixes](https://docs.python.org/3/whatsnew/3.9.html#new-string-methods-to-remove-prefixes-and-suffixes)

[← Volver al índice de la sección](../README.es.md)
