<div align="center">

# Tuplas e Inmutabilidad

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Modificar listas y métodos comunes de listas](../02-modifying-lists-and-methods/README.es.md) · [Volver al índice de Colecciones](../README.es.md) · [Siguiente capítulo: Diccionarios: claves y valores](../04-dictionaries-keys-and-values/README.es.md)

Las listas enseñaron qué significa que una colección sea mutable. Las tuplas presentan la idea opuesta: una secuencia ordenada cuyas posiciones no pueden sustituirse, añadirse ni eliminarse después de crear la tupla.

Esa diferencia es útil porque la forma de algunos datos debe permanecer fija. Una tupla puede comunicar esa intención directamente.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar los Capítulos 01 y 02 de Colecciones |
| Tiempo estimado de estudio | 80 a 100 minutos |
| Conceptos principales | literales de tupla, secuencias inmutables, indexación, slicing, tuplas de un elemento, `tuple()`, `count()`, `index()`, empaquetado, desempaquetado, objetos mutables anidados |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué hace que una tupla sea una secuencia inmutable;
- crear tuplas vacías, de un elemento y de varios elementos;
- reconocer por qué la coma importa en la sintaxis de las tuplas;
- leer elementos de una tupla con índices positivos y negativos;
- obtener slices de tuplas sin cambiar la original;
- usar `len()`, `in` y `not in` con tuplas;
- crear tuplas con `tuple()`;
- usar `count()` e `index()`;
- explicar por qué los métodos de mutación de las listas no existen en las tuplas;
- reconocer el error causado por una asignación a una posición de la tupla;
- empaquetar varios valores en una tupla;
- desempaquetar una secuencia de tamaño fijo en variables;
- explicar por qué una tupla todavía puede contener un objeto mutable;
- elegir una tupla cuando una secuencia fija comunica mejor la intención de los datos que una lista.

## 1. ¿Qué es una tupla?

Una tupla es una **secuencia ordenada e inmutable**.

Ordenada significa que cada elemento tiene una posición. Inmutable significa que la tupla no puede cambiar sus posiciones después de su creación.

```python
course_info = ("Python", "Beginner", 90)

print(course_info)
print(type(course_info))
```

```text
('Python', 'Beginner', 90)
<class 'tuple'>
```

La tupla contiene tres elementos en un orden definido.

## 2. Tupla frente a lista

Las listas y las tuplas comparten muchas operaciones de secuencia, pero difieren en un comportamiento central.

```python
topics_list = ["strings", "numbers", "lists"]
topics_tuple = ("strings", "numbers", "lists")

print(type(topics_list))
print(type(topics_tuple))
print(topics_list[0])
print(topics_tuple[0])
```

```text
<class 'list'>
<class 'tuple'>
strings
strings
```

Ambas son ordenadas y permiten acceso por índice. La lista puede cambiar posteriormente sus posiciones y su tamaño. La tupla no.

Usa esa diferencia como una señal de diseño, no como una competencia sobre qué tipo es "mejor".

## 3. Crear una tupla

Un literal común de tupla usa valores separados por comas dentro de paréntesis:

```python
dimensions = (1920, 1080)
languages = ("Python", "SQL", "JavaScript")
```

Los paréntesis hacen que la tupla sea fácil de reconocer, pero hay un detalle sintáctico importante: la coma es lo que crea una tupla no vacía.

## 4. La coma importa

Estas dos expresiones no son iguales:

```python
grouped_value = ("Python")
single_item_tuple = ("Python",)

print(type(grouped_value))
print(type(single_item_tuple))
```

```text
<class 'str'>
<class 'tuple'>
```

`("Python")` es simplemente una expresión string entre paréntesis.

`("Python",)` es una tupla que contiene un elemento.

Esta es una de las reglas de sintaxis de tuplas más importantes para principiantes.

## 5. Tuplas vacías

Una tupla vacía se escribe con paréntesis vacíos:

```python
empty_tuple = ()

print(empty_tuple)
print(len(empty_tuple))
print(type(empty_tuple))
```

```text
()
0
<class 'tuple'>
```

A diferencia de una tupla de un elemento, la tupla vacía no necesita una coma.

## 6. Los paréntesis suelen ser opcionales

En una tupla no vacía, las comas pueden crear la tupla incluso sin paréntesis alrededor:

```python
coordinates = 10, 20

print(coordinates)
print(type(coordinates))
```

```text
(10, 20)
<class 'tuple'>
```

En código para principiantes, los paréntesis normalmente hacen más clara la intención de escribir una tupla:

```python
coordinates = (10, 20)
```

Hay contextos en los que los paréntesis son exigidos por la sintaxis circundante. La idea útil aquí es simplemente que las comas, y no los paréntesis por sí solos, definen una tupla no vacía.

## 7. Leer elementos por índice

La indexación de tuplas sigue el mismo modelo basado en cero usado por strings y listas:

```python
record = ("Ana", "Python", 3)

print(record[0])
print(record[1])
print(record[2])
```

```text
Ana
Python
3
```

El primer elemento está en el índice `0`.

## 8. Índices negativos

Los índices negativos funcionan igual que en strings y listas:

```python
record = ("Ana", "Python", 3)

print(record[-1])
print(record[-2])
```

```text
3
Python
```

`-1` significa el último elemento.

## 9. Slicing de una tupla

Los slices de tuplas crean otra tupla:

```python
steps = ("study", "understand", "practice", "review", "repeat")

print(steps[:2])
print(steps[1:4])
print(steps[-2:])
```

```text
('study', 'understand')
('understand', 'practice', 'review')
('review', 'repeat')
```

El slicing lee un rango. No modifica la tupla original.

## 10. Los pasos de slicing también funcionan

El modelo común de slicing de secuencias sigue aplicándose:

```python
steps = ("study", "understand", "practice", "review", "repeat")

print(steps[::2])
print(steps[::-1])
```

```text
('study', 'practice', 'repeat')
('repeat', 'review', 'practice', 'understand', 'study')
```

El slice invertido crea una nueva tupla. La original permanece sin cambios.

## 11. Longitud y pertenencia

`len()`, `in` y `not in` funcionan con tuplas:

```python
topics = ("strings", "numbers", "lists", "tuples")

print(len(topics))
print("tuples" in topics)
print("sets" not in topics)
```

```text
4
True
True
```

Estas operaciones inspeccionan la tupla sin modificarla.

## 12. Inmutabilidad en la práctica

Una posición de la tupla no puede reemplazarse:

```python
topics = ("strings", "numbers", "lists")

topics[1] = "numeric tools"
```

```text
TypeError: 'tuple' object does not support item assignment
```

Esto es diferente de una lista, donde el mismo estilo de asignación por índice sí está permitido.

No uses el error como técnica normal de flujo del programa. Su propósito aquí es hacer visible la regla.

## 13. Las tuplas no tienen métodos de mutación de listas

Una tupla no tiene los métodos `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `reverse()` ni `sort()`.

Esa ausencia es coherente con la inmutabilidad: esos métodos tendrían que modificar la secuencia existente.

Si los datos necesitan crecer, reducirse, reorganizarse en el propio objeto o sustituir posiciones con el tiempo, una lista suele ser la opción más clara.

## 14. La concatenación crea una nueva tupla

Dos tuplas pueden concatenarse con `+`:

```python
core_topics = ("strings", "numbers")
collection_topics = ("lists", "tuples")

all_topics = core_topics + collection_topics

print(all_topics)
print(core_topics)
```

```text
('strings', 'numbers', 'lists', 'tuples')
('strings', 'numbers')
```

Las tuplas originales no cambian. `+` produce una nueva tupla.

## 15. La repetición crea una nueva tupla

La repetición de secuencias también funciona:

```python
pattern = ("study", "practice")

repeated = pattern * 2

print(repeated)
print(pattern)
```

```text
('study', 'practice', 'study', 'practice')
('study', 'practice')
```

De nuevo, la tupla existente no se modifica.

## 16. Crear tuplas con `tuple()`

La función incorporada `tuple()` puede crear una tupla a partir de otro iterable. Una lista es un ejemplo ya conocido:

```python
topics_list = ["strings", "numbers", "lists"]
topics_tuple = tuple(topics_list)

print(topics_tuple)
print(type(topics_tuple))
```

```text
('strings', 'numbers', 'lists')
<class 'tuple'>
```

La nueva tupla contiene, en el mismo orden, los elementos proporcionados por la lista.

Todavía no necesitas explorar todos los tipos de iterable. Los loops de la Fase 4 harán más concreto ese concepto general.

## 17. `count()` responde cuántos

Las tuplas admiten `count()`:

```python
scores = (8, 10, 9, 10, 8, 10)

print(scores.count(10))
print(scores.count(7))
```

```text
3
0
```

`count(value)` devuelve cuántos elementos son iguales al valor solicitado.

No modifica la tupla.

## 18. `index()` encuentra la primera posición coincidente

Las tuplas también admiten `index()`:

```python
topics = ("strings", "numbers", "lists", "numbers")

print(topics.index("numbers"))
```

```text
1
```

Solo se devuelve la primera coincidencia igual.

Si el valor no existe, `index()` genera `ValueError`, igual que en las listas.

## 19. Empaquetado de tupla

Python puede empaquetar valores separados por comas en una tupla:

```python
study_record = "tuples", 45, True

print(study_record)
print(type(study_record))
```

```text
('tuples', 45, True)
<class 'tuple'>
```

Esto se llama **empaquetado de tupla**.

Los tres valores se convierten en un único valor de tipo tupla.

## 20. Desempaquetado de secuencia

Una secuencia de tamaño fijo puede desempaquetarse en variables separadas:

```python
study_record = ("tuples", 45, True)

topic, minutes, completed = study_record

print(topic)
print(minutes)
print(completed)
```

```text
tuples
45
True
```

Cada variable recibe el elemento de la posición correspondiente.

Aunque las tuplas hacen que este patrón sea especialmente común, el desempaquetado también funciona con otras secuencias.

## 21. La cantidad de destinos debe coincidir

En el desempaquetado básico, la cantidad de variables a la izquierda debe coincidir con la cantidad de elementos de la secuencia a la derecha:

```python
study_record = ("tuples", 45, True)

topic, minutes = study_record
```

```text
ValueError: too many values to unpack (expected 2)
```

Material posterior podrá explorar el desempaquetado extendido. Por ahora, mantén las formas con el mismo tamaño.

## 22. Empaquetado y desempaquetado explican la asignación múltiple

Esta asignación de apariencia especial:

```python
left = "A"
right = "B"

left, right = right, left

print(left)
print(right)
```

```text
B
A
```

funciona mediante empaquetado y desempaquetado.

El lado derecho produce los valores y el lado izquierdo los recibe por posición. Python no necesita una variable temporal para este intercambio.

## 23. La inmutabilidad trata de las posiciones de la tupla

Una regla sutil pero importante: una tupla puede contener objetos mutables.

```python
profile = ("Ana", ["Python"])

profile[1].append("SQL")

print(profile)
```

```text
('Ana', ['Python', 'SQL'])
```

La tupla sigue teniendo las mismas dos posiciones:

1. el string `"Ana"`;
2. el mismo objeto lista.

La tupla no reemplazó su segundo elemento. La lista almacenada en esa posición cambió internamente.

Por lo tanto, "la tupla es inmutable" **no** significa que "todo objeto alcanzable desde la tupla sea inmutable".

## 24. ¿Qué sigue fallando con un elemento mutable dentro?

Incluso cuando una tupla contiene una lista, todavía no puedes reemplazar esa posición de la tupla:

```python
profile = ("Ana", ["Python"])

profile[1] = ["SQL"]
```

```text
TypeError: 'tuple' object does not support item assignment
```

Este contraste separa dos ideas:

- cambiar las posiciones de la tupla;
- cambiar un objeto mutable que ya está almacenado en una de esas posiciones.

La primera está prohibida. La segunda puede ser posible dependiendo del propio tipo del objeto contenido.

## 25. Cuándo una tupla comunica bien la intención

Una tupla es útil cuando una secuencia representa una forma fija.

Algunos ejemplos:

- un par de ancho y alto;
- una coordenada `(x, y)`;
- un resumen fijo como `(topic, minutes, completed)`;
- valores que se desempaquetan naturalmente en una cantidad conocida de variables.

Esto es una recomendación de diseño, no un requisito de Python. Una lista técnicamente puede almacenar muchos de los mismos valores.

Elige el tipo que mejor comunique cómo se espera que se comporten los datos.

## 26. Cuándo una lista es más clara

Prefiere una lista cuando se espera que la colección cambie como parte normal del trabajo:

- se añadirán nuevos elementos;
- se eliminarán elementos;
- se sustituirán posiciones;
- la colección se ordenará o invertirá en el propio objeto;
- la cantidad de elementos crecerá o disminuirá naturalmente.

El capítulo anterior presentó las herramientas para esas tareas.

## 27. Ejemplo práctico: configuración fija de pantalla

```python
display_size = (1920, 1080)

width, height = display_size

print("Width:", width)
print("Height:", height)
print("Pixels:", width * height)
```

```text
Width: 1920
Height: 1080
Pixels: 2073600
```

El par tiene un significado fijo: primero ancho, después alto. El desempaquetado da nombres descriptivos a esas posiciones.

## 28. Ejemplo práctico: resumen de estudio

```python
study_summary = ("tuples", 50, True)

topic, minutes, completed = study_summary

print("Topic:", topic)
print("Minutes:", minutes)
print("Completed:", completed)
print("Fields:", len(study_summary))
```

```text
Topic: tuples
Minutes: 50
Completed: True
Fields: 3
```

Este es un ejemplo compacto de un registro de forma fija sin introducir diccionarios antes de tiempo. El próximo capítulo mostrará por qué las claves suelen ser más claras cuando los registros se vuelven más descriptivos.

## 29. Errores comunes

### Olvidar la coma en una tupla de un elemento

`("Python")` es una expresión string. `("Python",)` es una tupla de un elemento.

### Intentar modificar una tupla como una lista

La asignación por índice y los métodos de mutación de listas no están disponibles en las tuplas.

### Pensar que solo los paréntesis crean cualquier tupla

En tuplas no vacías, las comas son la sintaxis que define la tupla. Los paréntesis suelen mejorar la claridad y son obligatorios en algunos contextos.

### Suponer que la inmutabilidad es profunda

Una tupla puede contener un objeto mutable, como una lista, y ese objeto contenido todavía puede cambiar.

### Esperar que `+` modifique una tupla existente

La concatenación de tuplas devuelve una nueva tupla.

### Desempaquetar en una cantidad incorrecta de variables

El desempaquetado básico exige que la cantidad de destinos coincida con la longitud de la secuencia.

### Usar una tupla para una colección que crece y disminuye naturalmente

La inmutabilidad puede convertirse en fricción cuando la mutación realmente forma parte del ciclo de vida normal de los datos. Una lista puede comunicar mejor esa intención.

## 30. Conexiones con conceptos anteriores y posteriores

Este capítulo reutiliza ideas anteriores:

- la indexación y el slicing funcionan como las operaciones de secuencia aprendidas con strings y listas;
- `len()`, las pruebas de pertenencia, `count()` e `index()` inspeccionan el contenido de la colección;
- la mutación de listas proporciona el contraste que hace concreta la inmutabilidad de las tuplas;
- la conversión de tipos proporciona el modelo para `tuple()`.

También prepara material posterior:

- los diccionarios reemplazarán el significado basado en posiciones por significado basado en claves;
- los sets se centrarán en la unicidad en vez del acceso posicional;
- el último capítulo de Colecciones comparará las cuatro opciones;
- los loops de la Fase 4 recorrerán tuplas igual que otros iterables;
- las funciones de la Fase 5 harán cada vez más útiles el empaquetado, el desempaquetado y las formas inmutables de datos.

## 31. Ejercicio: desempaqueta un registro fijo de aprendizaje

Crea `tuple_practice.py`.

Empieza con:

```python
learning_record = ("collections", "tuples", 60, True)
```

Sin usar loops ni condicionales:

1. imprime la tupla;
2. imprime su longitud;
3. imprime el primer elemento;
4. imprime el último elemento;
5. imprime el slice que contiene `"tuples"` y `60`;
6. imprime si `"tuples"` está en la tupla;
7. desempaqueta los cuatro elementos en `phase`, `topic`, `minutes` y `completed`;
8. imprime cada valor desempaquetado con una etiqueta;
9. crea una tupla de un elemento llamada `next_topic` que contenga `"dictionaries"`;
10. imprime `next_topic` y su tipo;
11. concatena `learning_record` y `next_topic` en `extended_record`;
12. imprime ambas tuplas para confirmar que la original no cambió.

Una posible forma de salida final es:

```text
Record: ('collections', 'tuples', 60, True)
Length: 4
First: collections
Last: True
Middle: ('tuples', 60)
Contains tuples: True
Phase: collections
Topic: tuples
Minutes: 60
Completed: True
Next: ('dictionaries',)
Next type: <class 'tuple'>
Extended: ('collections', 'tuples', 60, True, 'dictionaries')
Original: ('collections', 'tuples', 60, True)
```

Intenta predecir el valor y el tipo de cada expresión antes de ejecutar el archivo.

## 32. Autoevaluación

Antes de avanzar, asegúrate de poder responder estas preguntas:

1. ¿Qué hace que una tupla sea una secuencia?
2. ¿Qué significa inmutable para una tupla?
3. ¿Por qué `("Python")` no es una tupla de un elemento?
4. ¿Cómo se escribe una tupla vacía?
5. ¿Las tuplas pueden indexarse y dividirse mediante slicing?
6. ¿Qué devuelven `count()` e `index()`?
7. ¿Qué ocurre al asignar a `items[0]` si `items` es una tupla?
8. ¿Qué es el empaquetado de tupla?
9. ¿Qué es el desempaquetado de secuencia?
10. ¿Por qué una lista almacenada dentro de una tupla todavía puede cambiar?
11. ¿`tuple_a + tuple_b` modifica alguna de las tuplas originales?
12. ¿Cuándo comunicaría una lista la intención con más claridad que una tupla?

Si alguna respuesta parece incierta, modifica uno de los ejemplos y observa qué permanece fijo y qué puede cambiar.

## 33. Referencia rápida

- Tupla de varios elementos: `items = ("a", "b", "c")`
- Tupla vacía: `items = ()`
- Tupla de un elemento: `items = ("a",)`
- Crear desde otro iterable: `items = tuple(values)`
- Leer un elemento: `items[index]`
- Leer un slice: `items[start:stop]`
- Longitud: `len(items)`
- Pertenencia: `value in items`
- Contar valores iguales: `items.count(value)`
- Primera posición igual: `items.index(value)`
- Concatenar en una nueva tupla: `combined = first + second`
- Repetir en una nueva tupla: `repeated = items * 2`
- Empaquetar valores: `record = value_a, value_b`
- Desempaquetar valores: `value_a, value_b = record`

Recuerda:

- las tuplas son ordenadas;
- las tuplas son inmutables;
- no se puede asignar ni eliminar posiciones de una tupla;
- la concatenación y la repetición de tuplas crean nuevas tuplas;
- una coma es necesaria para una tupla de un elemento;
- los objetos mutables contenidos todavía pueden tener sus propios cambios internos.

## 34. A dónde ir ahora

Ahora puedes comparar los dos tipos posicionales de colección presentados hasta aquí:

1. **Lista:** ordenada y mutable.
2. **Tupla:** ordenada e inmutable.

El siguiente capítulo de Colecciones presenta **diccionarios**, donde las posiciones dejan de ser el principal modelo de búsqueda. En lugar de pedir el elemento `0` o el elemento `1`, recuperarás valores mediante claves significativas.

---

Referencias oficiales utilizadas para la verificación técnica:

- [Python Tutorial: Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Built-in Types: Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Built-in Types: Tuples](https://docs.python.org/3/library/stdtypes.html#tuples)
- [Python Data Model: Tuples](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)
