<div align="center">

# Creación e Indexación de Strings

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [Siguiente capítulo: Métodos comunes de strings →](../02-common-string-methods/README.es.md)

La Fase 1 enseñó que los valores de texto comunes usan el tipo `str`. Este primer capítulo de la Fase 2 profundiza ese concepto: muestra cómo crear strings y cómo leer posiciones individuales e intervalos dentro de ellas.

Una string en Python es una secuencia inmutable de puntos de código Unicode. Para quien está empezando, un modelo mental útil es más simple: una string es un valor de texto ordenado cuyas posiciones pueden leerse, pero no reemplazarse dentro del mismo valor.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar la Fase 1: Fundamentos |
| Tiempo estimado de estudio | 70 a 90 minutos |
| Conceptos principales | `str`, literales de string, `len()`, indexación, índices negativos, slicing, inmutabilidad, `IndexError` |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- crear strings con comillas simples, dobles y triples;
- explicar qué hacen las comillas del código fuente y qué no se convierte en parte del valor;
- usar secuencias de escape comunes cuando sea necesario;
- medir una string con `len()`;
- leer posiciones con índices positivos y negativos;
- explicar por qué el primer índice es `0`;
- leer intervalos con slices;
- explicar por qué un slice excluye su límite final;
- distinguir un índice directo inválido de un slice amplio y válido;
- explicar la inmutabilidad de las strings;
- reconocer que indexar una string devuelve otro `str`.

## 1. Las strings son valores de texto ordenados

Ya has usado strings a lo largo de la guía:

```python
course_name = "Python Study Guide"
current_topic = "Strings"
```

El orden importa. `"Python"` y `"nohtyP"` contienen las mismas letras, pero son strings diferentes porque sus elementos aparecen en secuencias distintas.

Esa estructura ordenada hace posible la indexación.

```text
Text:   P y t h o n
Index:  0 1 2 3 4 5
```

Cada posición tiene un índice entero. La primera posición es `0`.

## 2. Creación de literales de string

Un literal de string es una notación en el código fuente que crea un valor de string.

Las comillas simples y dobles crean strings comunes:

```python
single_quoted = 'Python'
double_quoted = "Python"

print(single_quoted == double_quoted)
```

```text
True
```

Para strings comunes, la elección de comillas no cambia el texto resultante. Elige la forma que mantenga el código fuente más legible.

```python
message = "Python's syntax can be readable."
quotation = 'She said "practice".'
```

Las comillas que delimitan el literal forman parte de la sintaxis. Normalmente no forman parte del valor resultante.

## 3. Escapes dentro de un literal

Una barra invertida puede iniciar una secuencia de escape cuando el texto necesita un carácter que sería incómodo escribir directamente.

```python
message = "She said \"practice\"."
two_lines = "first line\nsecond line"

print(message)
print(two_lines)
```

```text
She said "practice".
first line
second line
```

Algunas secuencias de escape útiles al principio son:

- `\n` para una nueva línea;
- `\t` para una tabulación;
- `\\` para una barra invertida literal;
- `\"` para una comilla doble;
- `\'` para una comilla simple.

No intentes memorizarlas todas de una vez. Úsalas cuando un valor real las necesite.

## 4. Strings con comillas triples

Grupos coincidentes de tres comillas simples o tres comillas dobles pueden abarcar varias líneas físicas.

```python
message = """Study
understand
practice"""

print(message)
```

```text
Study
understand
practice
```

Los saltos de línea forman parte del valor de la string.

Las strings con comillas triples también aparecen en docstrings, pero una string con comillas triples no es automáticamente una docstring. Su función depende de dónde aparezca en el programa.

## 5. La string vacía

Una string puede no contener ningún punto de código.

```python
empty_text = ""

print(len(empty_text))
```

```text
0
```

La string vacía sigue siendo un `str` válido. No es lo mismo que `None`.

## 6. Medición de una string con `len()`

`len()` devuelve la cantidad de elementos de una secuencia. Para strings, devuelve la cantidad de puntos de código Unicode.

```python
language = "Python"
topic = "Python strings"

print(len(language))
print(len(topic))
```

```text
6
14
```

Los espacios también cuentan porque forman parte de la string.

Para ejemplos cotidianos de nivel principiante, `len(text)` es una buena forma de razonar sobre cuántas posiciones indexadas expone la string.

### Nota de precisión sobre Unicode

Las strings de Python son texto Unicode. `len()` cuenta puntos de código Unicode, no bytes. Algunos símbolos visibles pueden representarse con varios puntos de código, por lo que la cantidad de símbolos visuales y el resultado de `len()` no están garantizados como iguales en todos los sistemas de escritura o secuencias de emoji.

No necesitas estudiar algoritmos de segmentación Unicode en este capítulo. La idea principal es que el texto de Python no se modela como bytes sin procesar.

## 7. La indexación positiva comienza en cero

Los corchetes leen una posición de una string.

```python
language = "Python"

print(language[0])
print(language[1])
print(language[5])
```

```text
P
y
n
```

Para una string no vacía de longitud `n`, los índices positivos válidos van de `0` a `n - 1`.

```text
len("Python") == 6
valid indexes: 0 1 2 3 4 5
```

El índice `6` ya está fuera de la string.

## 8. Por qué el primer índice es cero

Ayuda pensar en un índice como un desplazamiento desde el inicio.

```text
P y t h o n
^
0 positions away from the beginning
```

El elemento del índice `0` está a cero posiciones del inicio. El elemento del índice `1` está a una posición del inicio.

Python usa esta convención de indexación basada en cero para muchos tipos de secuencia, no solo para strings.

## 9. Los índices negativos cuentan desde el final

Los índices negativos permiten leer posiciones relativas al final.

```python
language = "Python"

print(language[-1])
print(language[-2])
print(language[-6])
```

```text
n
o
P
```

```text
Text:       P  y  t  h  o  n
Positive:   0  1  2  3  4  5
Negative:  -6 -5 -4 -3 -2 -1
```

`-1` representa el último elemento, `-2` el anterior y así sucesivamente.

## 10. La indexación devuelve otra string

Python no tiene un tipo incorporado separado para caracteres.

```python
language = "Python"
first_item = language[0]

print(first_item)
print(type(first_item))
print(len(first_item))
```

```text
P
<class 'str'>
1
```

Un elemento textual indexado es simplemente un `str` de longitud `1`.

## 11. Los índices directos inválidos generan `IndexError`

Un índice directo solicita una posición exacta. Si esa posición no existe, Python genera `IndexError`.

```python
language = "Python"

print(language[6])
```

```text
IndexError: string index out of range
```

El traceback completo también contiene información de archivo y línea. Aquí, la parte importante es el tipo de excepción y su mensaje.

Una string vacía no tiene ningún índice directo válido.

## 12. El slicing lee un intervalo

La indexación lee un elemento. El slicing lee un intervalo y devuelve un resultado de tipo string sin modificar la string original.

Sintaxis básica:

```text
text[start:stop]
```

El límite `start` se incluye. El límite `stop` se excluye.

```python
language = "Python"

print(language[0:3])
```

```text
Pyt
```

Los índices `0`, `1` y `2` se incluyen. El índice `3` marca dónde termina el slice.

## 13. Por qué se excluye el límite final

Los límites finales exclusivos permiten que intervalos adyacentes encajen limpiamente.

```python
language = "Python"

prefix = language[0:3]
suffix = language[3:6]

print(prefix)
print(suffix)
print(prefix + suffix)
```

```text
Pyt
hon
Python
```

El límite `3` termina el primer slice e inicia el segundo.

Con el paso unitario predeterminado, cuando `0 <= start <= stop <= len(text)`, la longitud del slice es `stop - start`.

## 14. Omisión de límites del slice

Omite `start` para comenzar desde el inicio de la string:

```python
language = "Python"

print(language[:3])
print(language[3:])
print(language[:])
```

```text
Pyt
hon
Python
```

Omitir `stop` continúa hasta el final. Omitir ambos devuelve el texto completo como un slice.

Como las strings son inmutables, un slice completo normalmente no es necesario solo para "proteger" el valor original.

## 15. Índices negativos en slices

Los límites de un slice también pueden ser negativos.

```python
filename = "notes.txt"

print(filename[:-4])
print(filename[-3:])
```

```text
notes
txt
```

Esto puede ser útil cuando un límite se describe naturalmente desde el final.

Ten en cuenta la legibilidad. Una expresión más corta no es automáticamente una expresión más clara.

## 16. Los slices toleran límites amplios

Un índice directo fuera de la string genera `IndexError`, pero un slice puede extenderse más allá del intervalo disponible.

```python
language = "Python"

print(language[:100])
print(language[100:])
```

```text
Python

```

El primer slice devuelve todo el texto disponible. El segundo devuelve la string vacía.

```text
language[100]   -> one exact missing position -> IndexError
language[:100] -> available range             -> valid string
```

## 17. Primer contacto con el paso de un slice

Los slices pueden tener un tercer componente:

```text
text[start:stop:step]
```

El paso controla cómo se recorren las posiciones.

```python
language = "Python"

print(language[::2])
```

```text
Pto
```

Esto recorre los índices `0`, `2` y `4`.

No necesitas rompecabezas avanzados de slicing en esta etapa. Los slices con inicio y fin son más importantes para escribir código principiante legible.

## 18. Las strings son inmutables

Una string inmutable no permite reemplazar una de sus posiciones dentro del mismo valor después de su creación.

```python
language = "Python"
language[0] = "J"
```

```text
TypeError: 'str' object does not support item assignment
```

Para producir un texto diferente, crea otro valor de string.

```python
language = "Python"
updated_language = "J" + language[1:]

print(language)
print(updated_language)
```

```text
Python
Jython
```

El próximo capítulo presenta métodos de string que suelen expresar transformaciones de texto de manera más clara.

## 19. Reasignación no es mutación

Un nombre de variable puede volver a asociarse con otra string.

```python
topic = "indexing"
topic = "slicing"

print(topic)
```

```text
slicing
```

El nombre ahora se refiere a otro valor de string. La string original no fue editada dentro del mismo objeto.

Esto se conecta directamente con la distinción entre nombres y valores estudiada en la Fase 1.

## 20. Ejemplo práctico: texto de posiciones fijas

Cuando un formato realmente tiene posiciones fijas, la indexación y el slicing pueden separar sus partes.

```python
record_code = "PY-2048"

category = record_code[:2]
separator = record_code[2]
number_text = record_code[3:]

print("Category:", category)
print("Separator:", separator)
print("Number text:", number_text)
```

```text
Category: PY
Separator: -
Number text: 2048
```

Esto es apropiado solo cuando las reglas de posición son estables y conocidas. Los índices fijos se vuelven frágiles cuando el formato de entrada puede variar.

## 21. Ejemplo práctico: inspeccionar un texto corto

```python
label = "practice"

print("Length:", len(label))
print("First:", label[0])
print("Last:", label[-1])
print("First four:", label[:4])
print("Remaining:", label[4:])
```

```text
Length: 8
First: p
Last: e
First four: prac
Remaining: tice
```

Este ejemplo combina las herramientas principales del capítulo sin introducir todavía métodos de string.

## 22. Errores comunes

### Tratar el índice `1` como la primera posición

```python
language = "Python"
print(language[1])
```

Esto imprime `y`, no `P`. El primer índice es `0`.

### Usar `len(text)` como un índice válido

```python
language = "Python"
print(language[len(language)])
```

`len(language)` es `6`, pero el último índice positivo válido es `5`. Para el último elemento, `language[-1]` es más claro.

### Esperar que el límite final del slice esté incluido

`language[0:3]` produce `"Pyt"`, no `"Pyth"`.

### Confundir reasignación con mutación

Volver a asociar un nombre es válido. Asignar a `text[0]` intenta modificar una string y genera `TypeError`.

### Indexar texto que puede estar vacío

Un índice directo exige que exista la posición solicitada. Los capítulos posteriores sobre condicionales mostrarán cómo proteger estas suposiciones dinámicamente.

### Usar posiciones fijas para formatos variables

Usa índices fijos únicamente cuando el formato de los datos realmente garantice esas posiciones.

## 23. Conexiones con conceptos anteriores

Este capítulo se basa directamente en la Fase 1:

- las variables dan nombres a valores de string;
- `type()` puede confirmar que los resultados indexados son valores `str`;
- `len()` devuelve un entero;
- los índices son enteros;
- los slices devuelven resultados de tipo string sin modificar la original;
- `print()` sigue siendo útil para inspeccionar resultados.

También prepara temas posteriores:

- los métodos de string transforman y buscan texto;
- listas y tuplas también admiten indexación y slicing;
- los bucles pueden recorrer repetidamente los elementos de una secuencia;
- los condicionales pueden proteger suposiciones sobre texto vacío;
- los archivos y datos externos a menudo llegan como strings que deben interpretarse.

## 24. Ejercicio: construye un inspector de texto

Crea `text_inspector.py` con este valor inicial:

```python
text = "Python practice"
```

Muestra:

1. el texto completo;
2. su longitud;
3. su primer elemento;
4. su último elemento;
5. los primeros seis elementos;
6. la segunda palabra usando un slice;
7. un elemento cada dos posiciones usando el paso de un slice;
8. el tipo del primer elemento indexado.

Una forma posible de salida es:

```text
Text: Python practice
Length: 15
First: P
Last: e
First six: Python
Second word: practice
Every second: Pto rcie
Indexed type: <class 'str'>
```

Intenta escribir las expresiones por tu cuenta antes de compararlas con los ejemplos del repositorio.

### Desafío extra

Crea un código ficticio de formato fijo, como `"AB-2048"`, y separa el prefijo de dos letras, el guion y el texto numérico mediante índices y slices.

Todavía no conviertas el texto numérico. El objetivo es practicar posiciones en texto.

## 25. Autoevaluación

Asegúrate de poder responder:

1. ¿Qué tipo representa texto común en Python?
2. ¿Cuál es el primer índice válido de una string no vacía?
3. ¿Qué representa `-1`?
4. ¿Por qué `text[len(text)]` está fuera del intervalo válido?
5. ¿Cuál es la diferencia entre indexación y slicing?
6. ¿Se incluye el límite final de un slice?
7. ¿Qué ocurre cuando un índice directo está fuera de la string?
8. ¿Por qué un slice amplio puede funcionar donde falla un índice directo amplio?
9. ¿Qué impide la inmutabilidad de las strings?
10. ¿La indexación produce un tipo separado para caracteres?

## 26. Referencia rápida

| Objetivo | Sintaxis | Ejemplo |
|---|---|---|
| Crear texto | comillas | `name = "Python"` |
| String vacía | comillas vacías | `text = ""` |
| Medir texto | `len(text)` | `len("Python")` → `6` |
| Primer elemento | `text[0]` | `"Python"[0]` → `"P"` |
| Último elemento | `text[-1]` | `"Python"[-1]` → `"n"` |
| Leer un intervalo | `text[start:stop]` | `"Python"[0:3]` → `"Pyt"` |
| Desde el inicio | `text[:stop]` | `"Python"[:3]` → `"Pyt"` |
| Hasta el final | `text[start:]` | `"Python"[3:]` → `"hon"` |
| Usar un paso | `text[start:stop:step]` | `"Python"[::2]` → `"Pto"` |
| Índice directo inválido | posición exacta inexistente | genera `IndexError` |
| Reemplazar un elemento | no compatible | genera `TypeError` |

## 27. Ejemplos del repositorio

Ejecuta los ejemplos deterministas:

```bash
python strings-and-numbers/01-string-creation-and-indexing/examples/string_basics.py
python strings-and-numbers/01-string-creation-and-indexing/examples/fixed_position_text.py
```

Después ejecuta las verificaciones del repositorio:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 28. Qué viene después

Ahora puedes crear strings, medirlas, leer posiciones exactas, leer intervalos y explicar por qué una string no puede editarse elemento por elemento.

El próximo capítulo pasa de posiciones a comportamiento: **métodos comunes de strings** para tareas como cambiar mayúsculas y minúsculas, quitar espacios adicionales, buscar, reemplazar, dividir y unir texto.

## Referencias oficiales

- [Python Language Reference — String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)
- [Python Built-in Types — Text Sequence Type `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python Built-in Types — Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Built-in Functions — `len()`](https://docs.python.org/3/library/functions.html#len)

[← Volver al índice de la sección](../README.es.md)
