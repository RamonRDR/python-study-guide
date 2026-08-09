<div align="center">

# Conjuntos y Valores Únicos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Diccionarios: claves y valores](../04-dictionaries-keys-and-values/README.es.md) · [Volver al índice de Colecciones](../README.es.md) · [Próximo capítulo: Elegir la colección adecuada →](../06-choosing-the-right-collection/README.es.md)

Las listas y las tuplas organizan valores por posición. Los diccionarios organizan valores mediante claves. Los conjuntos introducen otro modelo: un valor **pertenece a la colección o no pertenece**.

Ese modelo es especialmente útil cuando importa la unicidad, cuando quieres comprobar pertenencia o cuando deseas comparar grupos de valores.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar los Capítulos 01 a 04 de Colecciones |
| Tiempo estimado de estudio | 120 a 150 minutos |
| Conceptos principales | `set`, elementos únicos, pertenencia, elementos hashable, `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`, unión, intersección, diferencia, diferencia simétrica, subconjunto, superconjunto, conjuntos disjuntos, copia |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué hace diferente a un conjunto de las listas, tuplas y diccionarios;
- crear conjuntos vacíos y con contenido;
- explicar por qué los valores duplicados se reducen a un solo elemento del conjunto;
- convertir otro iterable en un conjunto con `set()`;
- explicar por qué los conjuntos no admiten indexación posicional ni slicing;
- contar elementos con `len()`;
- comprobar pertenencia con `in` y `not in`;
- añadir un elemento con `add()`;
- añadir varios elementos con `update()`;
- distinguir `remove()` de `discard()`;
- explicar por qué `pop()` no significa "eliminar el último elemento" en un conjunto;
- vaciar un conjunto;
- reconocer qué valores pueden ser elementos de un conjunto;
- calcular unión, intersección, diferencia y diferencia simétrica;
- comprobar relaciones de subconjunto, superconjunto y conjuntos disjuntos;
- distinguir otra referencia al mismo conjunto de una copia superficial;
- elegir un conjunto cuando la unicidad o la pertenencia sean más importantes que la posición.

## 1. De claves a pertenencia

El capítulo anterior utilizó claves significativas de diccionario:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("track" in profile)
```

```text
True
```

En un diccionario, la pertenencia comprueba las claves de forma predeterminada.

Un conjunto elimina por completo la relación clave-valor:

```python
topics = {"strings", "lists", "dictionaries"}

print("lists" in topics)
print("files" in topics)
```

```text
True
False
```

No hay un valor almacenado "bajo" `"lists"`. El propio valor `"lists"` es un elemento del conjunto.

Esa es la idea central de un conjunto:

**valor → pertenece o no pertenece**

## 2. Qué es un conjunto

El tipo mutable de conjunto incorporado de Python es `set`.

Un conjunto es una colección no ordenada de **elementos distintos y hashable**.

```python
skills = {"python", "sql", "git"}

print(type(skills))
print(len(skills))
```

```text
<class 'set'>
3
```

Tres ideas importan desde el principio:

- **distintos:** los elementos iguales no aparecen como duplicados separados;
- **sin orden posicional:** un conjunto no ofrece ordenación por posición para realizar búsquedas;
- **elementos hashable:** cada elemento debe ser adecuado para la búsqueda de pertenencia en conjuntos.

El capítulo de diccionarios ya introdujo el significado práctico de *hashable*. Los conjuntos reutilizan el mismo requisito para sus elementos.

## 3. Sintaxis de un literal de conjunto

Un literal de conjunto no vacío usa llaves con elementos separados por comas:

```python
languages = {"Python", "JavaScript", "SQL"}
```

Esto se parece a las llaves de un diccionario, pero no hay pares `key: value`.

Compara las formas:

```python
mapping = {"language": "Python"}
collection = {"Python"}

print(type(mapping))
print(type(collection))
```

```text
<class 'dict'>
<class 'set'>
```

Los dos puntos son la pista visual de que el primer objeto contiene una entrada de diccionario.

## 4. Un conjunto vacío usa `set()`

Las llaves vacías crean un diccionario vacío, no un conjunto vacío:

```python
empty_braces = {}
empty_set = set()

print(type(empty_braces))
print(type(empty_set))
```

```text
<class 'dict'>
<class 'set'>
```

Esta es una de las diferencias de sintaxis más importantes que debes recordar en este capítulo.

Usa:

```python
items = set()
```

cuando necesites un conjunto vacío.

## 5. Los valores duplicados se reducen

Un conjunto almacena elementos distintos. Repetir un valor igual no crea otro elemento separado:

```python
topics = {"lists", "sets", "lists", "sets", "tuples"}

print(len(topics))
print("lists" in topics)
print("tuples" in topics)
```

```text
3
True
True
```

El conjunto tiene tres elementos distintos, aunque en el literal se hayan escrito cinco valores.

Esto hace que los conjuntos sean útiles cuando la pregunta es "¿qué valores únicos están presentes?" en lugar de "¿cuántas veces apareció cada valor?".

## 6. La igualdad depende de los miembros, no del orden escrito

Dos conjuntos son iguales cuando contienen los mismos elementos:

```python
first = {"python", "sql", "git"}
second = {"git", "python", "sql"}

print(first == second)
```

```text
True
```

No interpretes esto como si los conjuntos "recordaran un orden diferente y lo ignoraran después". Un conjunto no proporciona orden posicional de secuencia desde el principio.

## 7. Los conjuntos no admiten indexación

Las listas y las tuplas admiten búsquedas por posición:

```python
items = ["python", "sql", "git"]
print(items[0])
```

```text
python
```

Un conjunto no:

```python
items = {"python", "sql", "git"}
print(items[0])
```

El segundo ejemplo produce `TypeError` porque los conjuntos no son secuencias subscriptables.

Si tu programa necesita un elemento "primero", "segundo" o "tercero" estable, normalmente un conjunto es el modelo de colección incorrecto.

## 8. Los conjuntos no admiten slicing

El slicing describe un rango posicional, por lo que tampoco se aplica a los conjuntos:

```python
items = {"python", "sql", "git"}
print(items[0:2])
```

Python produce `TypeError` porque un conjunto no tiene un segmento posicional que recuperar.

Este es un contraste importante con strings, listas y tuplas.

## 9. No dependas del orden mostrado por un conjunto

Como los conjuntos no definen posiciones ni orden de inserción, el código no debe depender del orden en que aparecen varios elementos al mostrar el conjunto.

Por ejemplo, esto crea un conjunto válido:

```python
skills = {"python", "sql", "git"}
```

Pero esta guía no asociará una salida fija de `print(skills)` con varios elementos a ese ejemplo.

Cuando los ejemplos necesiten una verificación determinista, usarán pertenencia, longitud, igualdad u otro resultado cuyo significado no dependa del orden de visualización.

## 10. Crear un conjunto a partir de otro iterable

El constructor `set()` puede reunir elementos distintos de otro iterable.

A partir de una lista:

```python
languages = ["Python", "SQL", "Python", "Git"]
unique_languages = set(languages)

print(len(unique_languages))
print(unique_languages == {"Python", "SQL", "Git"})
```

```text
3
True
```

La lista original sigue conteniendo sus valores originales. `set(languages)` crea un nuevo conjunto.

## 11. Convertir un string en conjunto

Un string es iterable, por lo que `set()` puede leer sus caracteres:

```python
letters = set("banana")

print(len(letters))
print("b" in letters)
print("n" in letters)
print("z" in letters)
```

```text
3
True
True
False
```

Los caracteres distintos son `"b"`, `"a"` y `"n"`, pero el conjunto no debe tratarse como una secuencia de caracteres con posiciones.

## 12. Usar `len()` con un conjunto

`len()` devuelve la cantidad de elementos distintos almacenados actualmente:

```python
permissions = {"read", "write", "export"}

print(len(permissions))
```

```text
3
```

Añadir un duplicado no aumenta esa cantidad.

## 13. La pertenencia es una operación natural de conjuntos

Usa `in` y `not in` para comprobar pertenencia:

```python
completed = {"strings", "lists", "tuples"}

print("lists" in completed)
print("sets" not in completed)
```

```text
True
True
```

Comprobar pertenencia es una de las principales razones por las que los conjuntos son útiles.

## 14. Añadir un elemento con `add()`

Los conjuntos son mutables. Usa `add()` para añadir un elemento:

```python
skills = {"python", "sql"}

skills.add("git")

print("git" in skills)
print(len(skills))
```

```text
True
3
```

Llamar a `add()` con un elemento que ya está presente no cambia la pertenencia:

```python
skills.add("python")
print(len(skills))
```

```text
3
```

`add()` modifica el conjunto in-place y devuelve `None`.

## 15. Añadir varios elementos con `update()`

Usa `update()` cuando otro iterable contiene varios valores que deseas añadir:

```python
skills = {"python"}

skills.update(["sql", "git", "python"])

print(len(skills))
print(skills == {"python", "sql", "git"})
```

```text
3
True
```

`update()` añade los elementos del iterable. No añade la propia lista como un solo elemento.

Al igual que `dict.update()`, `set.update()` modifica el objeto existente y devuelve `None`.

## 16. `add()` y `update()` significan cosas diferentes

Compara estas intenciones:

```python
skills = {"python"}
skills.add("sql")
```

`add()` recibe un elemento.

```python
skills = {"python"}
skills.update(["sql", "git"])
```

`update()` lee elementos de un iterable y los añade individualmente.

Con strings, esa diferencia importa:

```python
letters = set()
letters.add("ab")

print("ab" in letters)
print(len(letters))
```

```text
True
1
```

Pero:

```python
letters = set()
letters.update("ab")

print("a" in letters)
print("b" in letters)
print(len(letters))
```

```text
True
True
2
```

El primer conjunto contiene un elemento string, `"ab"`. El segundo recibe los dos caracteres del string iterable.

## 17. Eliminar un elemento con `remove()`

`remove(element)` elimina un elemento que debe estar presente:

```python
skills = {"python", "sql", "git"}

skills.remove("git")

print("git" in skills)
print(len(skills))
```

```text
False
2
```

Si el elemento solicitado está ausente, `remove()` produce `KeyError`.

Usa `remove()` cuando la ausencia deba tratarse como un error en lugar de ignorarse silenciosamente.

## 18. Eliminar de forma tolerante con `discard()`

`discard(element)` elimina el elemento si está presente, pero no produce `KeyError` cuando está ausente:

```python
skills = {"python", "sql"}

skills.discard("git")
skills.discard("sql")

print(skills == {"python"})
```

```text
True
```

Esto hace que `discard()` sea útil cuando "ya estar ausente" es un estado aceptable.

## 19. `remove()` versus `discard()`

Ambos métodos pueden eliminar un elemento presente. El comportamiento con un elemento ausente es la diferencia importante:

| Método | Elemento presente | Elemento ausente |
|---|---|---|
| `remove(value)` | lo elimina | produce `KeyError` |
| `discard(value)` | lo elimina | deja el conjunto sin cambios |

Ambos métodos modifican el conjunto in-place y devuelven `None`; ninguno devuelve el elemento eliminado.

Elige según si la ausencia del valor debe considerarse excepcional para esa operación.

## 20. `pop()` elimina un elemento arbitrario

`set.pop()` elimina y devuelve un elemento **arbitrario**.

No transfieras a los conjuntos el significado de `pop()` de las listas. Un conjunto no tiene una posición de "último elemento".

Un conjunto de un solo elemento nos proporciona un ejemplo determinista para principiantes:

```python
status = {"ready"}
removed = status.pop()

print(removed)
print(len(status))
```

```text
ready
0
```

En un conjunto con varios elementos, tu programa no debe depender de cuál elige `pop()`.

Llamar a `pop()` sobre un conjunto vacío produce `KeyError`.

## 21. Vaciar un conjunto

`clear()` elimina todos los elementos conservando el objeto conjunto:

```python
skills = {"python", "sql", "git"}

skills.clear()

print(skills)
print(len(skills))
```

```text
set()
0
```

Observa cómo Python muestra un conjunto vacío como `set()`, lo que también refuerza por qué `{}` no puede representar un conjunto vacío.

`clear()` modifica el conjunto in-place y devuelve `None`.

## 22. Los elementos de un conjunto deben ser hashable

La misma regla práctica de las claves de diccionario se aplica a los elementos de los conjuntos.

Elementos comunes y seguros para principiantes incluyen:

- strings;
- enteros;
- números de punto flotante;
- booleanos;
- tuplas cuyo contenido sea hashable.

Las listas, los diccionarios y los conjuntos ordinarios son mutables y unhashable, por lo que no pueden ser elementos de un conjunto.

Esto funciona:

```python
points = {(10, 20), (30, 40)}

print((10, 20) in points)
```

```text
True
```

Esto no funciona:

```python
invalid = {[10, 20]}
```

Python produce `TypeError` al intentar usar la lista como elemento del conjunto.

## 23. Un conjunto normalmente no puede contener otro conjunto

Un `set` ordinario es mutable y, por lo tanto, unhashable:

```python
outer = set()
inner = {"python", "sql"}

outer.add(inner)
```

Python produce `TypeError` porque `inner` es un conjunto ordinario.

Python también proporciona `frozenset`, un tipo de conjunto inmutable y hashable. Puede usarse cuando un valor inmutable de tipo conjunto necesita convertirse en clave de diccionario o elemento de otro conjunto:

```python
frozen_skills = frozenset({"python", "sql"})
groups = {frozen_skills}

print(frozen_skills in groups)
```

```text
True
```

Este capítulo se centra en el `set` mutable ordinario. Por ahora, reconoce `frozenset` como su contraparte inmutable y no como una nueva colección que debas dominar en profundidad.

## 24. La unión combina miembros

La unión de dos conjuntos contiene todos los elementos que aparecen en cualquiera de ellos.

Usa `union()`:

```python
backend = {"python", "sql"}
data = {"python", "pandas"}

combined = backend.union(data)

print(combined == {"python", "sql", "pandas"})
print(backend == {"python", "sql"})
```

```text
True
True
```

`union()` crea un nuevo conjunto. No modifica `backend` en este ejemplo.

El operador `|` expresa la misma unión cuando ambos operandos son conjuntos:

```python
combined = backend | data
```

## 25. La intersección conserva miembros compartidos

La intersección contiene elementos presentes en ambos conjuntos:

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

shared = backend.intersection(data)

print(shared == {"python", "sql"})
```

```text
True
```

El operador `&` es la forma de operador de conjunto:

```python
shared = backend & data
```

Piensa en la intersección como la respuesta a: **¿qué tienen en común estos grupos?**

## 26. La diferencia conserva miembros de un solo lado

La diferencia entre conjuntos es direccional.

`A - B` significa "elementos en A que no están en B":

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

backend_only = backend.difference(data)
data_only = data.difference(backend)

print(backend_only == {"git"})
print(data_only == {"pandas"})
```

```text
True
True
```

La forma con operador es:

```python
backend_only = backend - data
```

Invertir los operandos puede cambiar el resultado.

## 27. La diferencia simétrica conserva miembros no compartidos

La diferencia simétrica contiene elementos que aparecen en uno de los conjuntos, pero no en ambos:

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

exclusive = backend.symmetric_difference(data)

print(exclusive == {"git", "pandas"})
```

```text
True
```

La forma con operador usa `^`:

```python
exclusive = backend ^ data
```

Piensa así: **¿qué miembros pertenecen exactamente a uno de los dos grupos?**

## 28. Un mapa compacto de operaciones

Para dos conjuntos `a` y `b`:

| Pregunta | Método | Operador |
|---|---|---|
| Todo lo de cualquiera de los conjuntos | `a.union(b)` | `a | b` |
| Compartido por ambos | `a.intersection(b)` | `a & b` |
| En `a`, no en `b` | `a.difference(b)` | `a - b` |
| En exactamente un conjunto | `a.symmetric_difference(b)` | `a ^ b` |

Las formas con métodos suelen ser más fáciles de leer durante el aprendizaje inicial. Los operadores son compactos una vez que las relaciones resultan familiares.

## 29. Subconjuntos

Un conjunto es subconjunto de otro cuando todos sus elementos están contenidos en el otro conjunto.

```python
core = {"python", "sql"}
all_skills = {"python", "sql", "git", "testing"}

print(core.issubset(all_skills))
print(core <= all_skills)
```

```text
True
True
```

`<=` también permite igualdad. `<` significa **subconjunto propio**, por lo que los conjuntos no pueden ser iguales.

## 30. Superconjuntos

Un conjunto es superconjunto cuando contiene todos los elementos de otro conjunto:

```python
core = {"python", "sql"}
all_skills = {"python", "sql", "git", "testing"}

print(all_skills.issuperset(core))
print(all_skills >= core)
```

```text
True
True
```

`>` significa superconjunto propio, lo que exige que los conjuntos sean diferentes.

Las relaciones de subconjunto y superconjunto describen contención, no solamente tamaño numérico.

## 31. Conjuntos disjuntos

Dos conjuntos son disjuntos cuando no tienen elementos en común:

```python
frontend = {"html", "css"}
backend = {"python", "sql"}

print(frontend.isdisjoint(backend))
```

```text
True
```

Si su intersección está vacía, los conjuntos son disjuntos.

Esto es útil cuando necesitas preguntar si dos grupos se superponen de alguna manera.

## 32. Métodos de conjunto versus operadores

Las formas con métodos de unión, intersección, diferencia y diferencia simétrica aceptan iterables apropiados como argumentos.

Las formas con operadores como `|`, `&`, `-` y `^` requieren operandos de tipo conjunto.

Para código de principiante, usar dos conjuntos reales a ambos lados mantiene clara la intención:

```python
first = {"python", "sql"}
second = {"sql", "git"}
shared = first & second

print(shared == {"sql"})
```

```text
True
```

No memorices ahora todas las variaciones de entrada aceptadas. La idea importante es la relación entre conjuntos que representa cada operación.

## 33. Otro nombre no es una copia

Los conjuntos son mutables, por lo que compartir referencias funciona igual que con listas y diccionarios:

```python
original = {"python", "sql"}
alias = original

alias.add("git")

print("git" in original)
print(original is alias)
```

```text
True
True
```

Ambas variables hacen referencia al mismo objeto conjunto.

## 34. Crear una copia superficial

Usa `copy()` cuando necesites un objeto conjunto externo separado:

```python
original = {"python", "sql"}
copied = original.copy()

copied.add("git")

print("git" in original)
print("git" in copied)
print(original is copied)
```

```text
False
True
False
```

`set.copy()` es una copia superficial. En conjuntos ordinarios de nivel principiante, los propios elementos ya deben ser hashable, por lo que la lección principal aquí es que el objeto conjunto externo queda separado.

## 35. Eliminar duplicados de otra colección

Convertir a conjunto es una forma compacta de obtener valores únicos:

```python
entries = ["python", "sql", "python", "git", "sql"]
unique_entries = set(entries)

print(len(unique_entries))
print(unique_entries == {"python", "sql", "git"})
```

```text
3
True
```

Pero convertir a conjunto también abandona las posiciones de secuencia y no conserva un contrato de orden al estilo de las listas.

Si el orden original o la cantidad de duplicados importan, no sustituyas la colección original por un conjunto solo porque existen duplicados.

## 36. Cuándo un conjunto es una buena opción

Un conjunto suele ser una buena elección cuando:

- cada elemento debe aparecer como máximo una vez;
- la pertenencia es una pregunta central;
- necesitas comparar grupos mediante unión o intersección;
- necesitas encontrar valores presentes en un grupo y ausentes en otro;
- la búsqueda posicional no forma parte del problema.

Por ejemplo, un conjunto puede representar nombres de temas completados:

```python
completed_topics = {"strings", "lists", "tuples"}
```

El significado es "estos temas pertenecen al grupo completado", no "strings es el elemento 0".

## 37. Cuándo un conjunto no es una buena opción

Evita elegir un conjunto cuando:

- la posición o el slicing importan;
- las apariciones duplicadas contienen información;
- necesitas relaciones clave-valor;
- los elementos necesarios son objetos mutables y unhashable, como listas;
- tu programa depende de un orden de secuencia estable.

La colección debe representar la relación entre los valores, no limitarse a usar la sintaxis más corta.

## 38. Ejemplo práctico: comparar temas de aprendizaje

Supón que dos rutas de estudio ficticias comparten algunos temas y difieren en otros:

```python
python_track = {"python", "sql", "git", "testing"}
data_track = {"python", "sql", "pandas", "statistics"}

shared = python_track & data_track
python_only = python_track - data_track
data_only = data_track - python_track
all_topics = python_track | data_track

print("Shared is correct:", shared == {"python", "sql"})
print("Python-only is correct:", python_only == {"git", "testing"})
print("Data-only is correct:", data_only == {"pandas", "statistics"})
print("Total unique topics:", len(all_topics))
print("Python is shared:", "python" in shared)
```

```text
Shared is correct: True
Python-only is correct: True
Data-only is correct: True
Total unique topics: 6
Python is shared: True
```

El ejemplo comprueba deliberadamente pertenencia e igualdad en lugar de depender del orden mostrado por el conjunto.

## 39. Errores comunes

### Usar `{}` para un conjunto vacío

`{}` crea un diccionario vacío. Usa `set()` para un conjunto vacío.

### Esperar que permanezcan los duplicados

Un conjunto almacena elementos distintos. Los duplicados iguales se reducen a una sola entrada de pertenencia.

### Intentar leer `set[0]`

Los conjuntos no admiten indexación posicional.

### Intentar hacer slicing sobre un conjunto

El slicing necesita posiciones de secuencia. Los conjuntos no las tienen.

### Depender del orden de visualización

El orden mostrado por un conjunto no es un contrato posicional ni de inserción. No escribas lógica que dependa de él.

### Usar `add()` cuando quieres `update()`

`add()` añade un elemento. `update()` lee elementos de un iterable.

### Suponer que `remove()` ignora silenciosamente valores ausentes

`remove()` produce `KeyError` cuando el elemento está ausente. `discard()` no.

### Tratar `pop()` como `list.pop()`

`set.pop()` elimina un elemento arbitrario, no el "último".

### Añadir una lista o conjunto como elemento

Los elementos de un conjunto deben ser hashable. Las listas y los conjuntos ordinarios no lo son.

### Suponer que convertir a `set` solo elimina duplicados

También cambia el modelo de la colección. Pierdes el comportamiento posicional de secuencia.

### Confundir la dirección de la diferencia

`a - b` significa "miembros de `a` que no están en `b`". Invertir los operandos puede cambiar el resultado.

### Olvidar que la asignación comparte el mismo conjunto

`alias = original` no copia un conjunto mutable.

## 40. Conexiones con conceptos anteriores y posteriores

Este capítulo reutiliza ideas que ya conoces:

- operadores de pertenencia de strings, listas, tuplas y diccionarios;
- mutabilidad de listas y diccionarios;
- hashabilidad de las claves de diccionario;
- `len()` para el tamaño de colecciones;
- aliasing y copias superficiales;
- comparaciones de igualdad.

También prepara el siguiente capítulo:

- las listas representarán secuencias mutables y ordenadas;
- las tuplas representarán estructuras de secuencia ordenadas e inmutables;
- los diccionarios representarán mappings clave-valor;
- los conjuntos representarán grupos distintos orientados a la pertenencia.

El capítulo final de Colecciones comparará directamente estos cuatro modelos y te ayudará a elegir según la intención.

## 41. Ejercicio: comparar dos grupos de habilidades

Crea `skill_groups.py` con estos conjuntos iniciales:

```python
backend = {"python", "sql", "git"}
automation = {"python", "testing", "git"}
```

Sin usar bucles ni condicionales:

1. imprime la cantidad de elementos distintos de cada conjunto;
2. imprime si `"python"` pertenece a ambos conjuntos comprobando cada expresión de pertenencia;
3. crea `shared` usando intersección;
4. crea `backend_only` usando diferencia;
5. crea `automation_only` usando diferencia en la dirección opuesta;
6. crea `combined` usando unión;
7. crea `exclusive` usando diferencia simétrica;
8. verifica `shared == {"python", "git"}`;
9. verifica `backend_only == {"sql"}`;
10. verifica `automation_only == {"testing"}`;
11. verifica `exclusive == {"sql", "testing"}`;
12. añade `"apis"` a `backend`;
13. descarta `"testing"` de `automation`;
14. imprime si `"apis"` ahora está en `backend`;
15. imprime si `"testing"` todavía está en `automation`;
16. crea `backend_copy = backend.copy()`;
17. añade `"linux"` solamente a la copia;
18. verifica que `"linux"` no está en el original pero sí en la copia.

Un posible formato de salida determinista es:

```text
Backend count: 3
Automation count: 3
Python in backend: True
Python in automation: True
Shared correct: True
Backend-only correct: True
Automation-only correct: True
Exclusive correct: True
APIs in backend: True
Testing in automation: False
Linux in original: False
Linux in copy: True
```

Intenta predecir cada resultado booleano antes de ejecutar el programa.

## 42. Autoevaluación

Antes de continuar, asegúrate de poder responder estas preguntas:

1. ¿Por qué un conjunto es diferente de una lista incluso cuando ambos contienen varios valores?
2. ¿Por qué `{}` no crea un conjunto vacío?
3. ¿Qué ocurre con elementos duplicados iguales dentro de un conjunto?
4. ¿Por qué no puedes usar `set[0]` ni slicing en conjuntos?
5. ¿Qué comprueban `in` y `not in`?
6. ¿Cuál es la diferencia entre `add()` y `update()`?
7. ¿Cuál es la diferencia entre `remove()` y `discard()`?
8. ¿Por qué `set.pop()` no debe describirse como eliminación del último elemento?
9. ¿Qué requisito debe cumplir todo elemento de un conjunto?
10. ¿Por qué una tupla puede ser a veces un elemento de conjunto mientras que una lista no puede?
11. ¿Qué contiene la unión?
12. ¿Qué contiene la intersección?
13. ¿Por qué la diferencia entre conjuntos es direccional?
14. ¿Qué contiene la diferencia simétrica?
15. ¿Qué significa que un conjunto sea subconjunto de otro?
16. ¿Qué indica `isdisjoint()`?
17. ¿Por qué convertir una lista en conjunto puede cambiar más cosas que el tratamiento de duplicados?
18. ¿Por qué las mutaciones realizadas mediante un alias pueden afectar al conjunto original?

Si alguna respuesta no está clara, vuelve a la sección correspondiente y modifica uno de los ejemplos por tu cuenta.

## 43. Referencia rápida

- Conjunto vacío: `values = set()`
- Conjunto no vacío: `values = {"a", "b"}`
- Convertir un iterable: `values = set(source)`
- Contar elementos distintos: `len(values)`
- Pertenencia: `item in values`
- No pertenencia: `item not in values`
- Añadir un elemento: `values.add(item)`
- Añadir varios elementos: `values.update(iterable)`
- Eliminar, error si falta: `values.remove(item)`
- Eliminar si está presente: `values.discard(item)`
- Eliminar y devolver un elemento arbitrario: `item = values.pop()`
- Eliminar todos los elementos: `values.clear()`
- Unión: `a.union(b)` o `a | b`
- Intersección: `a.intersection(b)` o `a & b`
- Diferencia: `a.difference(b)` o `a - b`
- Diferencia simétrica: `a.symmetric_difference(b)` o `a ^ b`
- Subconjunto: `a.issubset(b)` o `a <= b`
- Superconjunto: `a.issuperset(b)` o `a >= b`
- Disjuntos: `a.isdisjoint(b)`
- Copia superficial: `other = values.copy()`

Recuerda el modelo:

- los elementos de los conjuntos son distintos;
- los elementos de los conjuntos deben ser hashable;
- los conjuntos ordinarios son mutables;
- los conjuntos no proporcionan indexación posicional ni slicing;
- no dependas del orden de visualización de conjuntos con varios elementos;
- la pertenencia y las relaciones entre grupos son las principales fortalezas de los conjuntos.

## 44. A dónde ir después

Ahora conoces los cuatro principales modelos de colección usados en esta fase:

1. **Lista:** secuencia ordenada y mutable.
2. **Tupla:** estructura de secuencia ordenada e inmutable.
3. **Diccionario:** mapping clave-valor.
4. **Conjunto:** colección no ordenada de miembros distintos y hashable.

El capítulo final de Colecciones reunirá todo en **Elegir la colección adecuada**. En lugar de aprender otra familia de sintaxis, practicarás cómo decidir qué modelo representa mejor la relación entre tus valores.

---

Referencias oficiales utilizadas para la verificación técnica:

- [Tutorial de Python: Conjuntos](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Tipos incorporados de Python: Tipos de conjunto — `set`, `frozenset`](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Glosario de Python: hashable](https://docs.python.org/3/glossary.html#term-hashable)
