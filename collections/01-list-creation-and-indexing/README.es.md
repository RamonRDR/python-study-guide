<div align="center">

# Creación, Indexación y Slicing de Listas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de Colecciones](../README.es.md) · [Siguiente capítulo: Modificar listas y métodos comunes de listas →](../02-modifying-lists-and-methods/README.es.md)

La Fase 2 enseñó cómo las strings ordenadas exponen posiciones y slices. La Fase 3 comienza aplicando esa idea familiar a un nuevo tipo de valor: una **lista**, que puede mantener varios valores relacionados juntos bajo un solo nombre.

Una lista de Python es una secuencia mutable. En este capítulo, concéntrate primero en la parte de secuencia: las listas conservan el orden de sus elementos, admiten indexación con enteros y admiten slicing. El siguiente capítulo se centrará en la mutabilidad y en los métodos que modifican listas.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar las Fases 1 y 2 |
| Tiempo estimado de estudio | 75 a 95 minutos |
| Conceptos principales | `list`, literales de lista, `len()`, indexación, índices negativos, slicing, pertenencia, `IndexError`, introducción a la mutabilidad |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar por qué una lista es útil cuando varios valores relacionados pertenecen a una misma colección;
- crear listas vacías y con elementos usando corchetes;
- reconocer que el orden de una lista es significativo;
- medir una lista con `len()`;
- leer elementos con índices positivos y negativos;
- leer rangos con slicing;
- explicar por qué un índice directo inválido genera `IndexError`;
- explicar por qué se permiten límites amplios en un slice;
- comprobar si un valor está presente con `in` y `not in`;
- relacionar la indexación y el slicing de listas con el comportamiento de strings aprendido en la Fase 2;
- explicar, a alto nivel, qué significa que una lista sea mutable.

## 1. Por qué existen las listas

Antes de las colecciones, puedes guardar valores relacionados en variables separadas:

```python
first_topic = "strings"
second_topic = "numbers"
third_topic = "lists"
```

Eso funciona para un ejemplo pequeño y fijo, pero la relación entre los valores existe principalmente en los nombres de las variables.

Una lista permite que un solo valor represente la colección:

```python
topics = ["strings", "numbers", "lists"]

print(topics)
```

```text
['strings', 'numbers', 'lists']
```

Ahora `topics` representa claramente una colección ordenada de elementos relacionados.

## 2. Crear un literal de lista

Los corchetes crean un literal de lista. Separa los elementos con comas:

```python
languages = ["Python", "JavaScript", "SQL"]
scores = [8, 9, 10]
prices = [12.50, 8.75, 21.00]

print(languages)
print(scores)
print(prices)
```

```text
['Python', 'JavaScript', 'SQL']
[8, 9, 10]
[12.5, 8.75, 21.0]
```

Los corchetes y las comas son sintaxis. Los elementos que están dentro son los valores almacenados por la lista.

## 3. Crear una lista vacía

Una lista puede empezar sin elementos:

```python
tasks = []

print(tasks)
print(len(tasks))
print(type(tasks))
```

```text
[]
0
<class 'list'>
```

Una lista vacía sigue siendo un valor `list` válido.

El siguiente capítulo mostrará cómo una lista puede ganar, cambiar y perder elementos después de su creación.

## 4. Las listas conservan el orden

El orden de los elementos forma parte del valor de una lista:

```python
first_order = ["study", "practice", "review"]
second_order = ["review", "practice", "study"]

print(first_order == second_order)
```

```text
False
```

Las dos listas contienen las mismas tres strings, pero las posiciones son diferentes.

Esta estructura ordenada es lo que hace significativas la indexación y el slicing.

## 5. Las listas pueden contener distintos tipos de valores

Python permite que los elementos de una lista tengan tipos diferentes:

```python
mixed_values = ["Python", 3, True, 9.5]

print(mixed_values)
```

```text
['Python', 3, True, 9.5]
```

Eso no significa que mezclar valores sin relación siempre sea un buen diseño. Las listas son más fáciles de comprender cuando los elementos pertenecen a un concepto claro, aunque sus tipos exactos no siempre sean iguales.

Por ejemplo, una lista de puntuaciones o una lista de nombres de temas comunica mejor la intención que una lista de datos sin relación.

## 6. Medir una lista con `len()`

`len()` devuelve la cantidad de elementos:

```python
topics = ["strings", "numbers", "lists"]

print(len(topics))
```

```text
3
```

El resultado es un `int`, igual que cuando medías una string.

Para una lista no vacía de longitud `n`, los índices positivos van desde `0` hasta `n - 1`.

## 7. La indexación positiva comienza en cero

Usa corchetes después del valor de la lista o del nombre de la variable para leer una posición:

```python
topics = ["strings", "numbers", "lists"]

print(topics[0])
print(topics[1])
print(topics[2])
```

```text
strings
numbers
lists
```

Un mapa útil de posiciones es:

```text
Item:   strings  numbers  lists
Index:        0        1      2
```

Este es el mismo modelo de indexación basada en cero que ya utilizaste con strings.

## 8. Los índices negativos cuentan desde el final

Los índices negativos leen posiciones relativas al final:

```python
topics = ["strings", "numbers", "lists"]

print(topics[-1])
print(topics[-2])
print(topics[-3])
```

```text
lists
numbers
strings
```

```text
Item:      strings  numbers  lists
Positive:        0        1      2
Negative:       -3       -2     -1
```

`-1` significa el último elemento.

## 9. La indexación devuelve el elemento almacenado

Indexar una string siempre devolvía otra `str`, porque una string almacena puntos de código de texto. Una lista puede almacenar valores de muchos tipos, así que indexar una lista devuelve el elemento de esa posición con su propio tipo.

```python
values = ["Python", 42, True]

print(values[0])
print(type(values[0]))
print(values[1])
print(type(values[1]))
print(values[2])
print(type(values[2]))
```

```text
Python
<class 'str'>
42
<class 'int'>
True
<class 'bool'>
```

La lista es el contenedor. La indexación lee uno de los valores contenidos.

## 10. Los índices directos inválidos generan `IndexError`

Un índice directo solicita una posición exacta:

```python
topics = ["strings", "numbers", "lists"]

print(topics[3])
```

```text
IndexError: list index out of range
```

La lista tiene longitud `3`, por lo que sus índices positivos válidos son `0`, `1` y `2`.

Una lista vacía no tiene ningún índice directo válido.

## 11. El slicing lee un rango

El slicing de listas usa la misma sintaxis básica que el slicing de strings:

```text
items[start:stop]
```

El límite inicial se incluye y el límite final se excluye.

```python
topics = ["strings", "numbers", "lists", "tuples", "dictionaries"]

print(topics[1:4])
```

```text
['numbers', 'lists', 'tuples']
```

Los índices `1`, `2` y `3` se incluyen. El índice `4` marca dónde termina el slice.

## 12. Un slice de lista produce una lista

Hacer slicing sobre una lista produce otra lista:

```python
topics = ["strings", "numbers", "lists", "tuples"]

selected_topics = topics[1:3]

print(selected_topics)
print(type(selected_topics))
```

```text
['numbers', 'lists']
<class 'list'>
```

Esto es diferente de la indexación directa:

```text
topics[1]    -> one stored item
topics[1:3]  -> a new list containing a range of items
```

Un slice crea un nuevo objeto lista. Si los propios elementos hacen referencia a objetos mutables, esos objetos internos todavía pueden compartirse; ese tema más profundo queda fuera de este capítulo para principiantes.

## 13. Omitir límites del slice

Omite el límite inicial para empezar en el primer elemento:

```python
steps = ["study", "understand", "practice", "review"]

print(steps[:2])
print(steps[2:])
print(steps[:])
```

```text
['study', 'understand']
['practice', 'review']
['study', 'understand', 'practice', 'review']
```

Omitir el límite final continúa hasta el final. Omitir ambos selecciona el rango completo.

## 14. Los índices negativos también funcionan en slices

Los límites negativos son útiles cuando el final de la lista es el punto de referencia natural:

```python
steps = ["study", "understand", "practice", "review", "repeat"]

print(steps[-2:])
print(steps[:-2])
```

```text
['review', 'repeat']
['study', 'understand', 'practice']
```

Prefiere límites que hagan fácil de entender la intención.

## 15. Los slices toleran límites amplios

Al igual que los slices de strings, los slices de listas pueden extenderse más allá de las posiciones disponibles:

```python
topics = ["strings", "numbers", "lists"]

print(topics[:100])
print(topics[100:])
```

```text
['strings', 'numbers', 'lists']
[]
```

Compara las dos ideas:

```text
topics[100]   -> one exact missing position -> IndexError
topics[:100]  -> available range            -> valid list
```

## 16. Pasos en slices

Un slice puede incluir un paso:

```text
items[start:stop:step]
```

Para un primer ejemplo, omite inicio y final y selecciona un elemento de cada dos:

```python
steps = ["study", "understand", "practice", "review", "repeat"]

print(steps[::2])
```

```text
['study', 'practice', 'repeat']
```

Los trucos avanzados de slicing no son el objetivo aquí. Usa pasos cuando hagan el código más claro.

## 17. Comprobar pertenencia con `in`

El operador `in` comprueba si hay un elemento igual presente:

```python
topics = ["strings", "numbers", "lists"]

print("lists" in topics)
print("tuples" in topics)
print("tuples" not in topics)
```

```text
True
False
True
```

Estas expresiones producen valores `bool`, conectando directamente las colecciones con los conceptos booleanos de la Fase 2.

Las comprobaciones de pertenencia responden si un valor está presente. No indican en qué posición aparece.

## 18. Las listas son mutables, pero este capítulo primero las lee

Una diferencia importante entre strings y listas es la **mutabilidad**.

- una string no permite reemplazar una de sus posiciones dentro del mismo objeto;
- una lista permite cambiar su contenido después de su creación.

Este capítulo se centra intencionalmente en crear y leer listas para que primero se vuelva familiar el modelo de secuencia.

El siguiente capítulo enseñará asignación de elementos, `append()`, `insert()`, `remove()`, `pop()`, `clear()` y `del`, y hará explícitas las reglas de mutación.

## 19. Cuándo una lista es una buena elección

Una lista es una buena elección inicial cuando:

- varios valores pertenecen a una colección ordenada;
- las posiciones importan;
- la cantidad de elementos puede cambiar más adelante;
- se permiten valores duplicados;
- esperas leer valores por índice o separar rangos mediante slicing.

Algunos ejemplos son una secuencia de temas de estudio, una lista de compras, pasos ordenados o un conjunto de puntuaciones registradas en orden.

## 20. Cuándo una lista puede no ser la mejor elección

Una lista puede ser una mala opción cuando la relación principal entre los datos no es posicional.

Más adelante en esta fase aprenderás alternativas:

- tuplas para datos secuenciales donde la inmutabilidad comunica intención;
- diccionarios para relaciones entre clave y valor;
- conjuntos para valores únicos y operaciones de pertenencia propias de conjuntos.

No elijas una colección solo porque su sintaxis te resulta familiar. Elige la estructura que exprese la relación entre los valores.

## 21. Ejemplo práctico: inspeccionar un plan de estudio

```python
study_plan = ["strings", "numbers", "lists", "tuples", "dictionaries"]

print("Plan:", study_plan)
print("Length:", len(study_plan))
print("Current:", study_plan[2])
print("Next:", study_plan[3])
print("Last two:", study_plan[-2:])
print("Lists included:", "lists" in study_plan)
```

```text
Plan: ['strings', 'numbers', 'lists', 'tuples', 'dictionaries']
Length: 5
Current: lists
Next: tuples
Last two: ['tuples', 'dictionaries']
Lists included: True
```

Este ejemplo utiliza la colección como un plan ordenado sin modificarla todavía.

## 22. Ejemplo práctico: reutilizar herramientas numéricas de la Fase 2

Las listas se vuelven especialmente útiles cuando herramientas anteriores pueden trabajar con varios valores relacionados:

```python
scores = [8, 9, 10]

print("Lowest:", min(scores))
print("Highest:", max(scores))
print("Total:", sum(scores))
```

```text
Lowest: 8
Highest: 10
Total: 27
```

Ya aprendiste estas funciones incorporadas en la Fase 2. La nueva idea es que una sola lista puede proporcionar los valores relacionados como una colección.

## 23. Errores comunes

### Empezar por el índice `1`

```python
topics = ["strings", "numbers", "lists"]
print(topics[1])
```

Esto imprime `numbers`, no `strings`. El primer índice es `0`.

### Usar `len(items)` como último índice válido

Si una lista tiene longitud `3`, el índice `3` ya está fuera de ella. El último índice positivo válido es `len(items) - 1`, y `items[-1]` suele ser más claro.

### Esperar que un slice devuelva un solo elemento

`items[1]` lee un elemento. `items[1:2]` devuelve una lista que contiene como máximo un elemento.

### Esperar que el límite final del slice esté incluido

`items[1:3]` incluye los índices `1` y `2`, no el índice `3`.

### Confundir una lista vacía con un valor ausente

`[]` es una lista real que contiene cero elementos. No es el mismo valor que `None`.

### Mezclar valores sin relación y sin motivo

Python permite tipos de elementos mezclados, pero una colección es más fácil de comprender cuando sus elementos representan una idea clara.

## 24. Conexiones con conceptos anteriores y posteriores

Este capítulo reutiliza varias ideas que ya conoces:

- las variables dan nombre a valores;
- `type()` identifica la lista y los tipos de los elementos indexados;
- `len()` devuelve una cantidad entera;
- los índices son enteros;
- el slicing sigue el mismo modelo de incluir el inicio y excluir el final utilizado por strings;
- `in` y `not in` producen resultados booleanos;
- `min()`, `max()` y `sum()` pueden trabajar con valores apropiados dentro de listas.

También prepara los siguientes pasos:

- el Capítulo 02 modifica deliberadamente el contenido de listas;
- el Capítulo 03 compara listas con tuplas e introduce la inmutabilidad como elección de diseño para colecciones;
- el Capítulo 04 reemplaza la búsqueda posicional por claves de diccionario;
- el Capítulo 05 introduce conjuntos, donde la indexación no es el modelo organizativo;
- la Fase 4 usará bucles para visitar repetidamente los elementos de colecciones.

## 25. Ejercicio: crea un inspector de colección

Crea `collection_inspector.py` con este valor inicial:

```python
topics = ["variables", "strings", "numbers", "lists", "tuples"]
```

Muestra:

1. la lista completa;
2. su longitud;
3. el primer elemento;
4. el último elemento;
5. los tres elementos centrales mediante un slice;
6. los tres primeros elementos mediante un slice;
7. los dos últimos elementos mediante un slice;
8. un elemento de cada dos;
9. si `"lists"` está presente;
10. el tipo de la colección completa;
11. el tipo del primer elemento indexado.

Una forma posible de salida es:

```text
Topics: ['variables', 'strings', 'numbers', 'lists', 'tuples']
Length: 5
First: variables
Last: tuples
Middle three: ['strings', 'numbers', 'lists']
First three: ['variables', 'strings', 'numbers']
Last two: ['lists', 'tuples']
Every second: ['variables', 'numbers', 'tuples']
Contains lists: True
Collection type: <class 'list'>
First item type: <class 'str'>
```

Intenta resolverlo sin bucles. La Fase 4 introducirá la iteración repetida más adelante.

### Desafío adicional

Crea una segunda lista con cinco puntuaciones numéricas. Muestra su primer y último valor, un slice con las puntuaciones centrales, su valor mínimo, su valor máximo y su total.

Todavía no modifiques ninguna de las listas. Esa es la tarea del siguiente capítulo.

## 26. Autoevaluación

Asegúrate de poder responder:

1. ¿Qué problema resuelve una lista en comparación con varias variables separadas?
2. ¿Qué símbolos crean un literal de lista?
3. ¿Qué cuenta `len()` en una lista?
4. ¿Cuál es el primer índice positivo?
5. ¿Qué significa el índice `-1`?
6. ¿Cuál es la diferencia entre `items[1]` e `items[1:2]`?
7. ¿Se incluye el límite final de un slice?
8. ¿Qué sucede cuando un índice directo está fuera de la lista?
9. ¿Por qué `items[:100]` puede funcionar cuando `items[100]` falla?
10. ¿Qué tipo de resultado produce un slice de lista?
11. ¿Qué devuelven `in` y `not in`?
12. A alto nivel, ¿qué significa que una lista sea mutable?

## 27. Referencia rápida

| Objetivo | Sintaxis | Ejemplo |
|---|---|---|
| Lista vacía | `[]` | `items = []` |
| Crear elementos | `[a, b, c]` | `topics = ["strings", "lists"]` |
| Cantidad de elementos | `len(items)` | `len(topics)` |
| Primer elemento | `items[0]` | `topics[0]` |
| Último elemento | `items[-1]` | `topics[-1]` |
| Rango | `items[start:stop]` | `topics[1:3]` |
| Desde el inicio | `items[:stop]` | `topics[:2]` |
| Hasta el final | `items[start:]` | `topics[2:]` |
| Un elemento de cada dos | `items[::2]` | `topics[::2]` |
| Pertenencia | `value in items` | `"lists" in topics` |
| Ausencia | `value not in items` | `"sets" not in topics` |
| Tipo | `type(items)` | `type(topics)` |

## 28. Referencias oficiales

- [Documentación de Python: Lists](https://docs.python.org/3/library/stdtypes.html#lists)
- [Documentación de Python: Operaciones comunes de secuencias](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

## Siguiente paso

Continúa con **Modificar Listas y Métodos Comunes de Listas** para aprender cómo funciona la mutabilidad en la práctica.
