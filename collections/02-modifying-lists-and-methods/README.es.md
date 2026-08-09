<div align="center">

# Modificar Listas y Métodos Comunes de Listas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Creación, indexación y slicing de listas](../01-list-creation-and-indexing/README.es.md) · [Volver al índice de Colecciones](../README.es.md) · Siguiente capítulo: Tuplas e inmutabilidad

El capítulo anterior enseñó a crear y leer listas. Ahora la otra mitad del modelo de listas se vuelve importante: una lista es **mutable**, lo que significa que su contenido puede cambiar después de que la lista se crea.

Este capítulo convierte esa idea en operaciones concretas. Reemplazarás elementos, añadirás elementos, eliminarás elementos, reorganizarás elementos, consultarás posiciones y cantidades, y aprenderás por qué algunos métodos cambian una lista pero devuelven `None` de forma intencional.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar el Capítulo 01 de Colecciones |
| Tiempo estimado de estudio | 100 a 125 minutos |
| Conceptos principales | mutabilidad, asignación por índice, asignación por slice, `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `del`, `index()`, `count()`, `reverse()`, `sort()`, `copy()` |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar la mutabilidad de las listas mediante cambios observables;
- reemplazar un elemento existente por índice;
- reemplazar un slice con otros valores;
- añadir un elemento con `append()`;
- añadir varios elementos con `extend()`;
- insertar un elemento en una posición elegida con `insert()`;
- eliminar por valor con `remove()`;
- eliminar y recuperar por posición con `pop()`;
- eliminar elementos con `del` y vaciar una lista con `clear()`;
- localizar el primer valor coincidente con `index()`;
- contar valores coincidentes con `count()`;
- invertir u ordenar una lista en el propio objeto;
- reconocer qué métodos comunes de listas devuelven `None`;
- distinguir entre asignar otro nombre a la misma lista y crear una copia superficial con `copy()`;
- elegir una operación de modificación según la intención y no por costumbre.

## 1. Qué significa mutabilidad

Un objeto mutable puede cambiar mientras sigue siendo el valor referenciado por la misma variable.

```python
topics = ["strings", "numbers", "lists"]

topics[1] = "numeric tools"

print(topics)
```

```text
['strings', 'numeric tools', 'lists']
```

La variable sigue llamándose `topics` y sigue haciendo referencia a una lista. El contenido de esa lista cambió.

Esta es la diferencia central respecto de las strings. Las posiciones de una string pueden leerse, pero no reemplazarse en el propio objeto. Las posiciones de una lista pueden leerse y también reemplazarse.

## 2. Reemplazar un elemento por índice

Usa un objetivo de asignación con corchetes para reemplazar una posición que ya existe:

```python
languages = ["Python", "Java", "SQL"]

languages[1] = "JavaScript"

print(languages)
```

```text
['Python', 'JavaScript', 'SQL']
```

El lado derecho proporciona el nuevo valor. La posición indexada del lado izquierdo identifica dónde debe colocarse ese valor.

Los índices negativos también funcionan:

```python
steps = ["study", "practice", "draft"]

steps[-1] = "review"

print(steps)
```

```text
['study', 'practice', 'review']
```

Usa el mismo modelo de índices que aprendiste en el capítulo anterior.

## 3. La asignación no crea una posición ausente

La asignación a un elemento reemplaza una posición que debe existir.

```python
topics = ["strings", "numbers", "lists"]

topics[3] = "tuples"
```

```text
IndexError: list assignment index out of range
```

La lista tiene tres elementos, por lo que sus índices positivos válidos son `0`, `1` y `2`.

Si tu intención es añadir un elemento nuevo en lugar de reemplazar uno existente, usa una operación de adición como `append()` o `insert()`.

## 4. Reemplazar un rango con asignación por slice

Un slice puede aparecer en el lado izquierdo de una asignación:

```python
steps = ["study", "practice", "review", "repeat"]

steps[1:3] = ["understand", "practice"]

print(steps)
```

```text
['study', 'understand', 'practice', 'repeat']
```

El slice seleccionado se reemplaza por los valores de la derecha.

A diferencia de asignar un único índice directo, la asignación normal por slice también puede cambiar la cantidad de elementos:

```python
steps = ["study", "review", "repeat"]

steps[1:2] = ["understand", "practice", "review"]

print(steps)
```

```text
['study', 'understand', 'practice', 'review', 'repeat']
```

Todavía no necesitas patrones avanzados de asignación por slice. La idea útil para principiantes es que un objetivo en forma de slice puede reemplazar un rango, no solo una posición.

## 5. Añadir un elemento con `append()`

`append()` añade un valor al final de la lista existente:

```python
topics = ["strings", "numbers"]

topics.append("lists")

print(topics)
```

```text
['strings', 'numbers', 'lists']
```

La lista se modifica en el propio objeto.

Usa `append()` cuando el valor completo que pasas al método debe convertirse en un único elemento nuevo.

## 6. `append()` añade exactamente un elemento

Si el valor pasado a `append()` es otra lista, esa lista completa se convierte en un único elemento anidado:

```python
topics = ["strings", "numbers"]

topics.append(["lists", "tuples"])

print(topics)
print(len(topics))
```

```text
['strings', 'numbers', ['lists', 'tuples']]
3
```

Esto es Python válido. Que esa sea la estructura que querías crear es una pregunta distinta.

Si quieres que los valores de otra lista se conviertan en elementos separados, usa `extend()`.

## 7. Añadir varios elementos con `extend()`

`extend()` añade al final de la lista los elementos de otro iterable. En este capítulo para principiantes, otra lista es el ejemplo más claro:

```python
topics = ["strings", "numbers"]

topics.extend(["lists", "tuples"])

print(topics)
```

```text
['strings', 'numbers', 'lists', 'tuples']
```

Compara la intención:

- `append(value)` añade `value` como un único elemento.
- `extend(values)` añade los elementos proporcionados por `values`.

El término general de Python *iterable* describe objetos capaces de proporcionar elementos uno tras otro. Los bucles harán este concepto más concreto en la Fase 4. Por ahora, usar otra lista con `extend()` es suficiente.

## 8. Insertar en una posición con `insert()`

`insert(index, value)` coloca un valor antes del elemento que actualmente está en ese índice:

```python
steps = ["study", "review", "repeat"]

steps.insert(1, "practice")

print(steps)
```

```text
['study', 'practice', 'review', 'repeat']
```

Usa `insert()` cuando la posición tenga significado por sí misma.

A diferencia de la asignación directa por índice, `insert()` no exige que el índice señale un elemento que ya exista. Python ajusta un índice de inserción fuera de los límites a uno de los extremos: `items.insert(len(items), value)` y los índices positivos mayores insertan al final, mientras que los índices negativos suficientemente pequeños insertan al principio. Por lo tanto, un índice de inserción fuera de los límites no genera `IndexError` solo por estar fuera del rango actual.

Si el nuevo elemento simplemente pertenece al final, `append()` comunica esa intención de forma más directa.

## 9. Eliminar por valor con `remove()`

`remove(value)` elimina el primer valor igual que encuentra:

```python
topics = ["lists", "strings", "lists", "tuples"]

topics.remove("lists")

print(topics)
```

```text
['strings', 'lists', 'tuples']
```

Solo se eliminó el primer elemento `"lists"` coincidente.

Usa `remove()` cuando conoces el valor que quieres eliminar y no necesitas recibir el valor eliminado como resultado.

## 10. Los valores ausentes hacen que `remove()` genere `ValueError`

`remove()` espera que exista un valor coincidente:

```python
topics = ["strings", "numbers", "lists"]

topics.remove("tuples")
```

```text
ValueError: list.remove(x): x not in list
```

Más adelante, el flujo de programa te permitirá decidir de forma condicional qué hacer cuando un valor puede estar o no presente. En este capítulo, la regla importante es simplemente que un valor ausente provoca `ValueError`.

## 11. Eliminar y recuperar con `pop()`

`pop()` elimina un elemento y devuelve el valor eliminado.

Sin argumento, usa la última posición:

```python
topics = ["strings", "numbers", "lists"]

removed_topic = topics.pop()

print("Removed:", removed_topic)
print("Remaining:", topics)
```

```text
Removed: lists
Remaining: ['strings', 'numbers']
```

También puedes proporcionar un índice:

```python
topics = ["strings", "numbers", "lists"]

removed_topic = topics.pop(0)

print("Removed:", removed_topic)
print("Remaining:", topics)
```

```text
Removed: strings
Remaining: ['numbers', 'lists']
```

Usa `pop()` cuando importan ambas acciones: cambiar la lista y conservar el valor eliminado para usarlo después.

## 12. Las posiciones inválidas en `pop()` generan `IndexError`

No se puede hacer `pop()` de un índice inválido. Llamar a `pop()` en una lista vacía tampoco ofrece ningún elemento para eliminar.

```python
topics = []

topics.pop()
```

```text
IndexError: pop from empty list
```

Esto es diferente de `remove()`: un valor ausente lleva a `ValueError`, mientras que una posición inválida o no disponible para `pop()` lleva a `IndexError`.

## 13. Eliminar con `del`

`del` es una instrucción que puede eliminar un elemento por índice:

```python
topics = ["strings", "numbers", "lists", "tuples"]

del topics[1]

print(topics)
```

```text
['strings', 'lists', 'tuples']
```

También puede eliminar un slice:

```python
topics = ["variables", "strings", "numbers", "lists", "tuples"]

del topics[1:3]

print(topics)
```

```text
['variables', 'lists', 'tuples']
```

A diferencia de `pop()`, `del` no devuelve el elemento eliminado como resultado de un método.

## 14. Vaciar una lista con `clear()`

`clear()` elimina todos los elementos mientras mantiene disponible la propia lista:

```python
topics = ["strings", "numbers", "lists"]

topics.clear()

print(topics)
print(len(topics))
```

```text
[]
0
```

La variable sigue haciendo referencia a una lista, pero esa lista ahora contiene cero elementos.

## 15. Encontrar la primera posición coincidente con `index()`

`index(value)` busca el primer valor igual y devuelve su índice basado en cero:

```python
topics = ["lists", "strings", "lists", "tuples"]

print(topics.index("lists"))
print(topics.index("tuples"))
```

```text
0
3
```

`index()` no modifica la lista.

Si el valor está ausente, `index()` genera `ValueError`.

## 16. Contar valores coincidentes con `count()`

`count(value)` devuelve cuántos elementos iguales aparecen:

```python
topics = ["lists", "strings", "lists", "tuples"]

print(topics.count("lists"))
print(topics.count("numbers"))
```

```text
2
0
```

Un valor ausente no es un error para `count()`. Su cantidad es simplemente `0`.

Esto hace que `count()` sea diferente tanto de `index()` como de `remove()`.

## 17. Invertir el orden actual con `reverse()`

`reverse()` invierte el orden existente en el propio objeto:

```python
steps = ["study", "practice", "review"]

steps.reverse()

print(steps)
```

```text
['review', 'practice', 'study']
```

`reverse()` no ordena por valor. Solo invierte el orden que la lista ya tiene.

## 18. Ordenar en el propio objeto con `sort()`

`sort()` reorganiza una lista en el propio objeto cuando sus elementos admiten las comparaciones necesarias:

```python
scores = [9, 7, 10, 8]

scores.sort()

print(scores)
```

```text
[7, 8, 9, 10]
```

Una lista simple de strings también puede ordenarse según las reglas de ordenación de Python:

```python
topics = ["tuples", "lists", "dictionaries"]

topics.sort()

print(topics)
```

```text
['dictionaries', 'lists', 'tuples']
```

La personalización avanzada de ordenación con `key=` queda fuera de este capítulo. Primero aprende la distinción importante: `sort()` cambia la lista existente.

## 19. No toda mezcla puede ordenarse

Una lista puede contener legalmente tipos diferentes, pero eso no garantiza que esos valores tengan entre sí una relación de ordenación significativa.

```python
values = ["Python", 3, None]

values.sort()
```

```text
TypeError: '<' not supported between instances of 'int' and 'str'
```

No interpretes esto como una regla que prohíbe listas con tipos mixtos. El problema es más específico: `sort()` necesita comparaciones que los valores contenidos puedan realizar.

## 20. Los métodos mutadores in-place normalmente devuelven `None`

Este es uno de los hábitos más importantes que conviene aprender temprano sobre listas.

Los métodos cuyo propósito principal es modificar una lista en el propio objeto, como `append()`, `extend()`, `insert()`, `remove()`, `clear()`, `reverse()` y `sort()`, devuelven `None` en lugar de la lista modificada.

```python
topics = ["strings", "numbers"]

result = topics.append("lists")

print("Topics:", topics)
print("Result:", result)
```

```text
Topics: ['strings', 'numbers', 'lists']
Result: None
```

El resultado útil de `append()` es la propia lista `topics` modificada. El valor de retorno del método es `None`.

`pop()` es intencionalmente diferente porque recuperar el elemento eliminado forma parte de su propósito.

## 21. El error común `items = items.append(...)`

Como `append()` devuelve `None`, este patrón destruye la referencia útil de la variable a la lista:

```python
items = ["strings", "numbers"]

items = items.append("lists")

print(items)
```

```text
None
```

Usa el método mutador como una instrucción independiente:

```python
items = ["strings", "numbers"]

items.append("lists")

print(items)
```

```text
['strings', 'numbers', 'lists']
```

La misma precaución se aplica a otros métodos in-place como `sort()` y `reverse()`.

## 22. La asignación puede crear otro nombre para la misma lista

Esta línea no copia una lista:

```python
original = ["strings", "numbers"]
alias = original

alias.append("lists")

print("Original:", original)
print("Alias:", alias)
```

```text
Original: ['strings', 'numbers', 'lists']
Alias: ['strings', 'numbers', 'lists']
```

Los dos nombres de variables hacen referencia a la misma lista mutable, por lo que una mutación observada a través de un nombre es visible a través del otro.

Por eso la mutabilidad importa más allá de una sola línea de código.

## 23. Crear una lista separada con `copy()`

`copy()` crea una lista nueva que contiene referencias a los mismos elementos actuales:

```python
original = ["strings", "numbers"]
independent = original.copy()

independent.append("lists")

print("Original:", original)
print("Copy:", independent)
```

```text
Original: ['strings', 'numbers']
Copy: ['strings', 'numbers', 'lists']
```

Cambiar la lista externa copiada ya no cambia la lista externa original.

El término oficial es **shallow copy**, o copia superficial. Si una lista contiene objetos mutables dentro de ella, esos objetos internos todavía pueden compartirse entre las dos listas externas. Copiar objetos anidados es un tema más profundo; por ahora, recuerda que `copy()` proporciona una lista externa separada.

## 24. Una comparación: alias frente a copia

```python
original = ["strings", "numbers"]
alias = original
independent = original.copy()

alias.append("lists")
independent.append("tuples")

print("Original:", original)
print("Alias:", alias)
print("Copy:", independent)
```

```text
Original: ['strings', 'numbers', 'lists']
Alias: ['strings', 'numbers', 'lists']
Copy: ['strings', 'numbers', 'tuples']
```

Vale la pena ejecutar y modificar este ejemplo. Hace visible el uso compartido de referencias sin exigir terminología avanzada del modelo de memoria.

## 25. Elegir la operación según la intención

Varias operaciones pueden cambiar una lista, pero comunican intenciones distintas.

| Intención | Operación |
|---|---|
| Reemplazar una posición existente | `items[index] = value` |
| Reemplazar un rango | `items[start:stop] = values` |
| Añadir un elemento al final | `append()` |
| Añadir varios elementos al final | `extend()` |
| Añadir un elemento en una posición específica | `insert()` |
| Eliminar el primer valor coincidente | `remove()` |
| Eliminar y recuperar un elemento por posición | `pop()` |
| Eliminar por índice o slice sin recuperar | `del` |
| Eliminar todos los elementos | `clear()` |
| Encontrar la primera posición coincidente | `index()` |
| Contar valores coincidentes | `count()` |
| Invertir el orden existente | `reverse()` |
| Ordenar la lista existente | `sort()` |
| Crear una copia superficial externa separada | `copy()` |

Prefiere la operación cuyo nombre o sintaxis exprese mejor el trabajo que estás realizando.

## 26. Ejemplo práctico: actualizar una cola de estudio

```python
study_queue = ["strings", "numbers"]

study_queue.append("lists")
study_queue.insert(1, "variables")
study_queue.remove("numbers")
completed_topic = study_queue.pop(0)

print("Completed:", completed_topic)
print("Queue:", study_queue)
```

```text
Completed: strings
Queue: ['variables', 'lists']
```

El ejemplo usa operaciones distintas porque las intenciones son diferentes: añadir al final, insertar en una posición, eliminar por valor y después eliminar y recuperar por posición.

## 27. Ejemplo práctico: corregir y resumir puntuaciones

```python
scores = [8, 10, 7, 9, 10]

scores[2] = 8
scores.append(9)

print("Tens:", scores.count(10))
print("First ten index:", scores.index(10))

scores.sort()

print("Sorted:", scores)
print("Lowest:", min(scores))
print("Highest:", max(scores))
print("Total:", sum(scores))
```

```text
Tens: 2
First ten index: 1
Sorted: [8, 8, 9, 9, 10, 10]
Lowest: 8
Highest: 10
Total: 54
```

Esto combina herramientas numéricas de la Fase 2 con la nueva capacidad de cambiar y reorganizar una lista.

## 28. Errores comunes

### Asignar el resultado de un método mutador

`items.append(value)`, `items.sort()` y métodos in-place similares devuelven `None`. No reemplaces tu variable de lista por ese valor de retorno.

### Usar `append()` cuando querías `extend()`

`append(["lists", "tuples"])` añade un único elemento que es una lista anidada. `extend(["lists", "tuples"])` añade dos elementos separados.

### Confundir eliminación por valor con eliminación por posición

`remove(value)` busca por igualdad. `pop(index)` y `del items[index]` trabajan por posición.

### Esperar que `remove()` elimine todos los duplicados

`remove(value)` elimina solo la primera coincidencia igual.

### Esperar que `pop()` devuelva la lista modificada

`pop()` devuelve el elemento que fue eliminado, no la lista.

### Suponer que una asignación copia una lista

`second = first` crea otra referencia a la misma lista. Usa `copy()` cuando necesites una lista externa separada.

### Tratar `reverse()` como ordenación

`reverse()` invierte el orden actual. No decide qué valor debería aparecer primero según tamaño u orden alfabético.

### Ordenar valores que no admiten ordenación entre sí

Una lista puede contener tipos mixtos incluso cuando `sort()` no puede comparar esos valores concretos.

## 29. Mutación y código legible

La mutación es útil, pero un programa se vuelve más difícil de razonar cuando una lista cambia en muchos lugares sin relación entre sí.

Para código de principiante, prefiere un hábito sencillo:

- usa nombres de variables descriptivos;
- realiza un cambio por una razón clara;
- elige una operación que exprese la intención;
- inspecciona la lista después de experimentar con una mutación;
- evita cadenas ingeniosas de operaciones cuando las instrucciones separadas sean más fáciles de entender.

Fases posteriores proporcionarán funciones, bucles y pruebas que harán más fáciles de organizar los flujos de mutación más grandes.

## 30. Conexiones con conceptos anteriores y posteriores

Este capítulo se apoya directamente en material anterior:

- los índices y slices vienen de leer strings y listas;
- la asignación ya conectaba nombres con valores;
- `None` ya fue presentado como un valor incorporado;
- `IndexError` ya apareció al leer una posición inválida de una lista;
- las herramientas Booleanas y numéricas siguen funcionando con contenido de lista apropiado.

También prepara ideas posteriores:

- el Capítulo 03 contrastará listas mutables con tuplas inmutables;
- los diccionarios y conjuntos tienen sus propias operaciones y reglas de mutación;
- la Fase 4 usará condicionales y bucles para decidir cuándo y cómo ocurren cambios repetidos en colecciones;
- las funciones de la Fase 5 harán importante entender cuándo un objeto mutable puede modificarse a través de una referencia pasada a otro lugar.

## 31. Ejercicio: administra un backlog de aprendizaje

Crea `learning_backlog.py` con esta lista inicial:

```python
backlog = ["strings", "numbers", "lists"]
```

Sin usar bucles ni condicionales:

1. reemplaza `"numbers"` por `"numeric tools"` por índice;
2. añade `"tuples"` con `append()`;
3. extiende la lista con `"dictionaries"` y `"sets"`;
4. inserta `"variables"` en el índice `0`;
5. imprime cuántas veces aparece `"lists"`;
6. imprime el índice de `"tuples"`;
7. elimina `"numeric tools"` por valor;
8. elimina el último elemento con `pop()` y guárdalo en `removed_topic`;
9. imprime el tema eliminado;
10. imprime el backlog resultante;
11. crea una copia superficial llamada `backlog_copy`;
12. invierte solamente `backlog_copy`;
13. imprime ambas listas para confirmar que invertir la copia no invirtió la original.

Un posible formato de salida final es:

```text
Lists count: 1
Tuples index: 4
Removed: sets
Backlog: ['variables', 'strings', 'lists', 'tuples', 'dictionaries']
Copy: ['dictionaries', 'tuples', 'lists', 'strings', 'variables']
```

Intenta predecir cada lista intermedia antes de ejecutar el archivo.

## 32. Autoevaluación

Antes de continuar, asegúrate de poder responder estas preguntas sin adivinar:

1. ¿Por qué un elemento de lista puede reemplazarse mientras que un carácter de string no?
2. ¿Cuál es la diferencia entre `append()` y `extend()`?
3. ¿Cuál es la diferencia entre `remove()` y `pop()`?
4. ¿Qué devuelve `pop()`?
5. ¿Por qué `items = items.append(value)` suele romper código de principiante?
6. ¿Qué cambia `clear()`?
7. ¿`reverse()` ordena valores?
8. ¿Qué devuelven `index()` y `count()`?
9. ¿Por qué `second = first` puede hacer visibles las mutaciones a través de ambos nombres?
10. ¿Qué separa `copy()` y sobre qué advierte la palabra *shallow*?

Si alguna respuesta todavía no está clara, vuelve a la sección correspondiente y modifica uno de los ejemplos por tu cuenta.

## 33. Referencia rápida

- Reemplazar un elemento: `items[index] = value`
- Reemplazar un rango: `items[start:stop] = values`
- Añadir un elemento al final: `items.append(value)`
- Añadir varios elementos: `items.extend(values)`
- Insertar antes de una posición: `items.insert(index, value)`
- Eliminar el primer valor igual: `items.remove(value)`
- Eliminar y devolver un elemento: `removed = items.pop()` o `removed = items.pop(index)`
- Eliminar por posición o rango: `del items[index]` o `del items[start:stop]`
- Eliminar todos los elementos: `items.clear()`
- Encontrar el primer valor igual: `position = items.index(value)`
- Contar valores iguales: `quantity = items.count(value)`
- Invertir en el propio objeto: `items.reverse()`
- Ordenar en el propio objeto: `items.sort()`
- Crear una copia superficial externa: `other = items.copy()`

Recuerda el patrón de valores de retorno:

- `append()`, `extend()`, `insert()`, `remove()`, `clear()`, `reverse()` y `sort()` cambian la lista y devuelven `None`.
- `pop()` cambia la lista y devuelve el elemento eliminado.
- `index()` y `count()` no cambian la lista y devuelven información.
- `copy()` no cambia la lista original y devuelve una nueva lista superficial.

## 34. Adónde continuar

Ahora conoces las dos mitades del modelo de listas para principiantes:

1. Crea y lee una lista.
2. Cambia una lista de forma deliberada.
3. Compara listas mutables con tuplas inmutables.

El siguiente capítulo de Colecciones presenta **tuplas e inmutabilidad**. Esa comparación hará mucho más clara la elección de diseño detrás de la mutabilidad de las listas.

---

Referencias oficiales utilizadas para la verificación técnica:

- [Python Tutorial: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Built-in Types: Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
- [Python Built-in Types: Lists](https://docs.python.org/3/library/stdtypes.html#lists)
