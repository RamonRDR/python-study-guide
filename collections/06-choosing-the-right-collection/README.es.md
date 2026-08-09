<div align="center">

# Elegir la Colección Adecuada

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Conjuntos y valores únicos](../05-sets-and-unique-values/README.es.md) · [Volver al índice de Colecciones](../README.es.md) · [Ver el roadmap](../../docs/roadmap.es.md)

Ahora conoces cuatro modelos importantes de colecciones incorporadas: listas, tuplas, diccionarios y conjuntos.

La habilidad final de esta fase no consiste en memorizar otro método. Consiste en aprender a mirar un problema y preguntar:

**¿Qué relación existe entre estos valores?**

Esa pregunta es más útil que elegir una colección solo porque su sintaxis resulta familiar.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar los Capítulos 01 a 05 de Colecciones |
| Tiempo estimado de estudio | 90 a 120 minutos |
| Conceptos principales | elección de colección, datos posicionales, mutabilidad, mappings clave-valor, unicidad, pertenencia, decisiones semánticas, colecciones anidadas |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- comparar listas, tuplas, diccionarios y conjuntos según su propósito;
- identificar cuándo la posición forma parte del significado de los datos;
- decidir si la propia colección necesita cambiar;
- reconocer cuándo las claves significativas son más claras que las posiciones numéricas;
- reconocer cuándo la unicidad y la pertenencia son centrales;
- explicar por qué el orden de inserción de un diccionario no lo convierte en una secuencia posicional;
- explicar por qué convertir entre tipos de colección puede cambiar el modelo de los datos;
- combinar diferentes tipos de colección cuando existan relaciones diferentes en distintos niveles;
- justificar una elección de colección con lenguaje sencillo;
- entrar en la Fase 4 preparado para usar flujo de programa con colecciones que ya comprendes.

## 1. Empieza por la relación, no por los corchetes

Estos valores podrían escribirse usando varios tipos de colección:

```python
values = ["python", "sql", "git"]
```

```python
values = ("python", "sql", "git")
```

```python
values = {"python", "sql", "git"}
```

Los valores parecen similares, pero los modelos de colección no son equivalentes.

Antes de elegir, pregunta qué significan los valores juntos.

¿Forman una serie ordenada? ¿Una estructura posicional fija? ¿Campos con nombre? ¿Un grupo de miembros únicos?

La respuesta debe orientar la elección de la colección.

## 2. Los cuatro modelos de colección

Un resumen útil para principiantes es:

| Colección | Modelo principal |
|---|---|
| `list` | posiciones ordenadas que pueden cambiar |
| `tuple` | posiciones ordenadas cuya estructura de tupla no puede cambiar |
| `dict` | claves mapeadas a valores |
| `set` | miembros distintos sin búsqueda posicional |

Esta tabla describe la relación principal que comunica cada colección.

## 3. Un primer mapa de decisión

Usa estas preguntas en orden:

```text
Do meaningful keys identify the values?
    yes -> dict
    no
     |
     v
Is uniqueness or membership the central idea?
    yes -> set
    no
     |
     v
Do positions and order matter?
    yes
     |
     v
Should the sequence structure change later?
    yes -> list
    no  -> tuple
```

Esto es una ayuda de aprendizaje, no una ley completa para todos los programas de Python. El software real puede tener restricciones adicionales.

Para problemas de nivel principiante, sin embargo, estas preguntas ofrecen un punto de partida sólido.

Conviene hacer explícito un caso límite: si las claves significativas, la pertenencia distinta y el orden posicional reciben una respuesta negativa, ninguno de estos cuatro modelos representa exactamente "apariciones duplicadas sin orden". Si deben conservarse las apariciones repetidas, una lista es un contenedor práctico para principiantes aunque su orden sea incidental; deja claro que el orden no forma parte del significado de los datos. Si las apariciones repetidas no importan, reconsidera si un conjunto representa el problema.

## 4. Pregunta uno: ¿claves significativas identifican los valores?

Supón que quieres representar el nombre, la ruta y el nivel de una persona que estudia.

Una lista puede almacenar los valores:

```python
learner = ["Mina", "Python", "beginner"]
```

Pero el significado de cada posición debe recordarse por separado.

Un diccionario convierte las etiquetas en parte del modelo:

```python
learner = {
    "name": "Mina",
    "track": "Python",
    "level": "beginner",
}
```

Si la pregunta natural es "¿cuál es el valor de este campo?", un diccionario suele ser la elección más clara.

## 5. El orden de un diccionario no es búsqueda posicional

A partir de Python 3.7, preservar el orden de inserción de los diccionarios es una garantía del lenguaje, pero eso no los convierte en listas.

```python
profile = {
    "name": "Mina",
    "track": "Python",
}

print(profile["track"])
```

```text
Python
```

La búsqueda funciona porque `"track"` es una clave.

`profile[0]` no significa "la primera entrada", a menos que `0` sea literalmente una clave en ese diccionario.

Elige un diccionario por la **relación clave-valor**, no porque quieras posiciones numeradas.

## 6. Pregunta dos: ¿la unicidad es la idea central?

Supón que quieres representar nombres de temas completados y que cada tema debe aparecer como máximo una vez.

Un conjunto comunica esa relación directamente:

```python
completed = {"strings", "lists", "tuples"}

print("lists" in completed)
```

```text
True
```

La pregunta importante es la pertenencia: ¿un tema pertenece al grupo completado?

Si importan las apariciones duplicadas o las posiciones, un conjunto no es el modelo adecuado.

## 7. Pregunta tres: ¿las posiciones importan?

Una lista y una tupla son secuencias posicionales.

```python
steps = ["read", "practice", "review"]
checkpoint = (3, 4)

print(steps[0])
print(checkpoint[1])
```

```text
read
4
```

Aquí, la posición tiene significado.

En `steps`, la posición describe el orden de las actividades. En `checkpoint`, las dos posiciones forman una pequeña estructura fija parecida a una coordenada.

## 8. Pregunta cuatro: ¿la estructura de la secuencia debe cambiar?

Cuando la posición importa, la mutabilidad ayuda a diferenciar listas de tuplas.

Usa una lista cuando añadir, eliminar o reemplazar elementos de la secuencia forme parte del trabajo normal:

```python
steps = ["read", "practice"]
steps.append("review")

print(steps)
```

```text
['read', 'practice', 'review']
```

Usa una tupla cuando la propia estructura de la secuencia deba permanecer fija:

```python
checkpoint = (3, 4)

print(checkpoint)
```

```text
(3, 4)
```

La inmutabilidad de la tupla se aplica a la estructura de la tupla. Una tupla puede seguir conteniendo un objeto mutable, como aprendiste en el Capítulo 03.

## 9. Lista versus tupla

Usa esta comparación cuando ambas opciones parezcan razonables:

| Pregunta | `list` | `tuple` |
|---|---|---|
| ¿Secuencia posicional? | sí | sí |
| ¿Admite indexación y slicing? | sí | sí |
| ¿Puede cambiar la estructura de la secuencia? | sí | no |
| ¿Se permiten valores duplicados? | sí | sí |
| Intención típica para principiantes | serie ordenada que cambia | forma ordenada fija |

La diferencia importante no es corchetes versus paréntesis. Es si modificar la estructura de la secuencia forma parte del modelo.

## 10. Lista versus conjunto

Estas dos colecciones aparecen a menudo cuando deben almacenarse varios valores similares.

Elige una lista cuando:

- importa el orden de la secuencia;
- los duplicados pueden contener información;
- importa la búsqueda posicional;
- la secuencia puede cambiar.

Elige un conjunto cuando:

- cada miembro debe ser distinto;
- la pertenencia es central;
- relaciones de conjunto como intersección o diferencia son útiles;
- las posiciones no forman parte del significado.

No sustituyas una lista por un conjunto solo porque la lista contiene duplicados.

## 11. Tupla versus diccionario

Ambos pueden representar un pequeño grupo estructurado, pero comunican significados diferentes.

Una tupla enfatiza posiciones:

```python
version = (3, 13)

print(version[0])
```

```text
3
```

Un diccionario enfatiza etiquetas:

```python
version = {
    "major": 3,
    "minor": 13,
}

print(version["major"])
```

```text
3
```

Si quien lee debe recordar qué significa la posición `0`, las claves significativas pueden hacer más claro un diccionario.

Si la forma posicional en sí es significativa y compacta, una tupla puede ser apropiada.

## 12. Diccionario versus conjunto

Ambos usan llaves en formas literales comunes, pero sus modelos son muy diferentes.

Un diccionario almacena relaciones clave-valor:

```python
permissions = {
    "read": True,
    "write": False,
}
```

Un conjunto almacena miembros:

```python
permissions = {"read", "export"}
```

Pregunta si cada elemento necesita un valor asociado.

Si es así, un diccionario puede encajar. Si el elemento en sí simplemente pertenece o no pertenece, un conjunto puede encajar.

## 13. El comportamiento de los duplicados importa

Las listas y las tuplas conservan posiciones duplicadas:

```python
items = ["python", "python", "sql"]

print(len(items))
```

```text
3
```

Los conjuntos reducen miembros duplicados iguales:

```python
items = {"python", "python", "sql"}

print(len(items))
```

```text
2
```

Los diccionarios no pueden contener dos claves iguales separadas al mismo tiempo, aunque sus valores pueden repetirse.

Si las apariciones repetidas contienen información, modela eso deliberadamente en lugar de elegir un conjunto de forma automática.

## 14. La hashabilidad importa para diccionarios y conjuntos

Las claves de diccionario y los elementos de conjunto deben ser hashable.

Ejemplos comunes y seguros para principiantes incluyen strings, enteros y tuplas cuyo contenido sea hashable.

Las listas no pueden ser claves de diccionario ni elementos de conjuntos ordinarios porque las listas son mutables y unhashable.

Este requisito puede afectar al diseño de la colección, pero no conviertas el hashing en la primera pregunta de decisión. Empieza por la relación entre los valores y luego comprueba si el modelo elegido admite los valores que necesitas.

## 15. La mutabilidad se refiere al objeto colección

Las listas, los diccionarios y los conjuntos ordinarios son mutables.

Las tuplas son secuencias inmutables.

Pero los objetos anidados conservan su propio comportamiento.

Por ejemplo:

```python
record = (
    "Mina",
    ["strings", "lists"],
)

record[1].append("tuples")

print(record)
```

```text
('Mina', ['strings', 'lists', 'tuples'])
```

La estructura de la tupla no cambió. La lista almacenada dentro de ella sí cambió.

Por eso, "tupla significa que nada dentro puede cambiar" es un modelo mental incorrecto.

## 16. Un programa puede necesitar las cuatro colecciones

Pueden existir relaciones diferentes en distintos niveles del mismo problema.

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
}
planned_topics = ["lists", "tuples", "dictionaries", "sets"]
checkpoint = (3, 4)
completed_topics = {"lists", "tuples"}
```

Cada colección comunica algo diferente:

- `course` usa campos con nombre;
- `planned_topics` es una serie ordenada que puede crecer;
- `checkpoint` es un par posicional fijo;
- `completed_topics` es un grupo de miembros distintos.

Usar varios tipos de colección juntos es normal cuando las relaciones entre los datos son diferentes.

## 17. Las colecciones anidadas no son automáticamente avanzadas

Una colección puede contener otra colección cuando eso representa bien los datos.

```python
student = {
    "name": "Mina",
    "topics": ["strings", "lists"],
}
```

El diccionario exterior responde "¿qué campo?".

La lista interior responde "¿qué elementos de temas ordenados?".

Elige cada nivel por separado. No fuerces un único tipo de colección para representar todas las relaciones de una estructura mayor.

## 18. Los mismos valores pueden justificar modelos diferentes

Considera los valores `"python"`, `"sql"` y `"git"`.

Si representan una secuencia de estudio:

```python
skills = ["python", "sql", "git"]
```

Si representan una instantánea posicional fija de tres partes:

```python
skills = ("python", "sql", "git")
```

Si representan habilidades completadas y únicas:

```python
skills = {"python", "sql", "git"}
```

Los valores por sí solos no determinan la colección. La **relación y las operaciones previstas** sí.

## 19. Convertir tipos cambia el modelo

Python permite convertir entre formas de colección compatibles, pero la conversión no es meramente cosmética.

```python
entries = ["python", "sql", "python"]
unique_entries = set(entries)

print(len(entries))
print(len(unique_entries))
```

```text
3
2
```

El conjunto ya no representa las posiciones duplicadas de la lista.

Convertir de nuevo a una lista no recrea la información que fue descartada.

No conviertas tipos de colección solo para obtener corchetes diferentes en la salida.

## 20. No elijas por familiaridad con la sintaxis

Un hábito común de principiantes es usar listas para todo porque las listas se aprenden primero.

Otro es usar la colección que tenga el literal más corto.

Ambos hábitos ocultan el significado de los datos.

Prefiere este razonamiento:

- "Necesito posiciones ordenadas que cambiarán, así que elegí una lista."
- "Necesito una estructura posicional fija, así que elegí una tupla."
- "Necesito valores identificados por nombres, así que elegí un diccionario."
- "Necesito pertenencia distinta, así que elegí un conjunto."

Una explicación breve así es un excelente hábito de diseño.

## 21. No elijas solo por un método que recuerdas

Supón que recuerdas bien `append()`. Eso no hace que una lista sea automáticamente adecuada.

Supón que recuerdas que los conjuntos eliminan duplicados. Eso no significa que toda entrada con duplicados deba convertirse en conjunto.

Los métodos son operaciones disponibles **después** de haber elegido un modelo de datos.

Elige primero la relación y luego usa las operaciones que pertenecen a esa colección.

## 22. Una tabla práctica de comparación

| Necesidad | Primer candidato fuerte |
|---|---|
| Serie ordenada que cambiará | `list` |
| Secuencia posicional fija | `tuple` |
| Campos o identificadores con nombre | `dict` |
| Miembros distintos y pruebas de pertenencia | `set` |
| Las apariciones duplicadas deben permanecer | `list` o `tuple` |
| Clave asociada con un valor | `dict` |
| Unión/intersección/diferencia entre grupos | `set` |
| La posición numérica forma parte del significado | `list` o `tuple` |

"Primer candidato fuerte" es una elección deliberada de palabras. El diseño de software puede implicar más contexto del que una sola tabla puede representar.

## 23. Escenario: pasos de compra

Imagina estos pasos:

1. elegir artículos;
2. revisar carrito;
3. pagar.

Si el programa necesita preservar este orden y quizá insertar otro paso después, una lista es un modelo natural:

```python
steps = ["choose items", "review cart", "pay"]
```

Importan tanto la posición como la posibilidad de cambiar la secuencia.

## 24. Escenario: una coordenada

Una coordenada de dos partes tiene una pequeña forma posicional fija:

```python
point = (10, 20)
```

La primera y la segunda posición tienen roles definidos, y cambiar la cantidad de partes de la coordenada no es la operación normal.

Una tupla comunica bien esta forma fija de secuencia.

## 25. Escenario: un perfil

Un perfil tiene campos con nombre:

```python
profile = {
    "name": "Mina",
    "level": "beginner",
}
```

Las etiquetas son más significativas que decir que el nombre siempre debe recordarse como elemento `0`.

Un diccionario hace explícita la relación entre campos.

## 26. Escenario: funcionalidades compatibles

Supón que la pregunta importante es si una funcionalidad pertenece a un grupo compatible:

```python
supported = {"export", "search", "sync"}

print("search" in supported)
```

```text
True
```

Un conjunto comunica directamente la pertenencia distinta.

## 27. Ejemplo práctico: cuatro modelos juntos

El ejemplo aprobado `collection_models.py` usa una colección para cada relación:

```python
tasks = ["read", "practice", "review"]
checkpoint = (3, 4)
profile = {"name": "Mina", "track": "Python"}
completed = {"strings", "lists", "tuples"}

print(tasks[0])
print(checkpoint[1])
print(profile["track"])
print("lists" in completed)
```

```text
read
4
Python
True
```

La sintaxis difiere porque las preguntas difieren.

## 28. Ejemplo práctico: decisiones de mutabilidad

`collection_tradeoffs.py` refuerza qué estructuras externas de colección pueden cambiar:

```python
planned_topics = ["strings", "lists", "tuples"]
fixed_version = (3, 13)
student = {"name": "Mina", "active": False}
skills = {"python", "git"}

planned_topics.append("dictionaries")
student["active"] = True
skills.add("sql")

print(len(planned_topics))
print(fixed_version[0])
print(student["active"])
print("sql" in skills)
```

```text
4
3
True
True
```

La tupla se lee por posición, pero su estructura no se modifica.

## 29. Ejemplo práctico: un pequeño espacio de estudio

`study_workspace.py` combina los modelos de colección en un programa ficticio:

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
}
planned_topics = ["lists", "tuples", "dictionaries", "sets"]
checkpoint = (3, 4)
completed_topics = {"lists", "tuples"}

planned_topics.append("collection choices")
course["status"] = "in progress"
completed_topics.add("dictionaries")

print(course["title"])
print(planned_topics[0])
print(checkpoint)
print("dictionaries" in completed_topics)
print(len(completed_topics))
```

```text
Python Study Guide
lists
(3, 4)
True
3
```

Ninguna colección compite con las demás. Cada una se ocupa de una relación diferente.

## 30. Errores comunes

### Usar una lista para todos los problemas

Las listas son flexibles, pero la flexibilidad no las convierte en el modelo más claro para campos con nombre o pertenencia única.

### Usar una tupla solo porque los datos son cortos

La longitud por sí sola no determina si una tupla es adecuada. La pregunta importante es si una secuencia posicional fija tiene sentido.

### Tratar el orden de inserción del diccionario como indexación de lista

Los diccionarios preservan el orden de inserción, pero la búsqueda directa se hace por clave.

### Usar un conjunto cuando importan las apariciones duplicadas

Un conjunto elimina la pertenencia duplicada igual. Eso puede descartar información.

### Elegir un conjunto porque sus pruebas de pertenencia parecen atractivas

Primero confirma que la pertenencia distinta y no posicional corresponde al propio problema.

### Suponer que la inmutabilidad de la tupla congela objetos anidados

La estructura de la tupla es inmutable. Los objetos mutables almacenados dentro conservan su propio comportamiento.

### Convertir colecciones sin considerar el significado perdido

Cambiar el tipo puede modificar el tratamiento de duplicados, el comportamiento posicional, la mutabilidad o la forma de búsqueda.

### Forzar un tipo de colección en todos los niveles de anidamiento

Elige cada nivel según la relación que exista en ese nivel.

## 31. Checklist para elegir una colección

Antes de escribir el literal de la colección, pregunta:

1. ¿Los valores se identifican mediante nombres o claves significativas?
2. ¿La pertenencia distinta es la relación principal?
3. ¿Importan las posiciones numéricas?
4. ¿Importa el orden de la secuencia?
5. ¿La colección exterior debe cambiar después?
6. ¿Deben conservarse las apariciones duplicadas?
7. ¿Las claves de diccionario o elementos de conjunto deseados cumplen los requisitos de hashabilidad?
8. ¿Otra persona entendería la relación observando el tipo elegido?

No siempre necesitarás las ocho preguntas, pero hacen visibles suposiciones ocultas.

## 32. Ejercicio: elige antes de programar

Para cada escenario, elige `list`, `tuple`, `dict` o `set` y escribe una frase explicando el motivo.

1. Una cola de lectura ordenada que recibirá nuevos libros.
2. Un par fijo `(width, height)`.
3. Un tema de interfaz con configuraciones con nombre como `"font_size"` y `"dark_mode"`.
4. Un grupo de nombres únicos de funcionalidades habilitadas.
5. Los resultados ordenados de tres intentos donde deben conservarse puntuaciones repetidas.
6. Una tripleta RGB fija como `(255, 128, 0)`.
7. Un registro de producto identificado por campos como `"name"`, `"price"` y `"available"`.
8. Dos grupos cuyos miembros compartidos deben compararse con intersección.
9. Una secuencia de títulos de lecciones que puede reordenarse después.
10. Un pequeño par fijo que representa una posición inicial y final.

Después, crea `collection_choice_practice.py` con un ejemplo original de cada tipo de colección. No uses bucles ni condicionales.

Para cada variable, añade una breve explicación escrita debajo del código indicando por qué esa colección corresponde a la relación.

## 33. Extensión del ejercicio: combina los modelos

Crea un planificador ficticio de estudio con:

- un diccionario para información del curso con nombre;
- una lista para temas planificados en orden;
- una tupla para un checkpoint fijo de dos números;
- un conjunto para temas completados únicos.

Realiza al menos una operación segura para principiantes y apropiada para cada colección.

Ejemplos de operaciones apropiadas incluyen:

- leer un valor de diccionario por clave;
- añadir un elemento a la lista;
- leer una posición de la tupla;
- comprobar pertenencia en el conjunto.

El objetivo no es usar todos los métodos. El objetivo es dejar claro el papel de cada colección.

## 34. Autoevaluación

Antes de completar la Fase 3, asegúrate de poder responder estas preguntas:

1. ¿Qué relación comunica mejor una lista?
2. ¿Qué diferencia estructural importante separa una tupla de una lista?
3. ¿Cuándo son más claras las claves de diccionario que las posiciones numéricas?
4. ¿Qué relación es central en un conjunto?
5. ¿Los diccionarios preservan el orden de inserción?
6. ¿Eso convierte a los diccionarios en secuencias indexadas por posición?
7. ¿Qué tipos de colección preservan apariciones duplicadas de forma natural?
8. ¿Por qué convertir una lista en conjunto puede descartar información?
9. ¿Qué deben cumplir las claves de diccionario y los elementos de conjunto?
10. ¿Puede una tupla contener un objeto mutable?
11. ¿Por qué un programa puede usar los cuatro tipos de colección?
12. ¿Qué deberías preguntar antes de elegir según la sintaxis?

Si alguna respuesta no está clara, vuelve al capítulo que introdujo esa colección y modifica un ejemplo por tu cuenta.

## 35. Referencia rápida

- Secuencia ordenada que cambia: `list`
- Estructura de secuencia posicional fija: `tuple`
- Relaciones clave-valor significativas: `dict`
- Grupo orientado a pertenencia con miembros distintos: `set`
- Las listas, tuplas y strings admiten operaciones posicionales de secuencia.
- Los diccionarios usan claves para búsqueda directa.
- Los conjuntos no ofrecen indexación posicional ni slicing.
- Las listas, diccionarios y conjuntos ordinarios son mutables.
- La estructura de la tupla es inmutable.
- Las claves de diccionario y los elementos de conjunto deben ser hashable.
- Las apariciones duplicadas siguen siendo significativas en listas y tuplas.
- Los miembros de los conjuntos son distintos.
- Las claves de diccionario son únicas, mientras que los valores de diccionario pueden repetirse.
- La conversión entre tipos de colección puede cambiar el modelo de datos.
- Las estructuras anidadas pueden usar tipos de colección diferentes en niveles diferentes.

## 36. Modelo mental de la Fase 3

Toda la fase de Colecciones puede resumirse ahora así:

```text
list  -> ordered positions that can change
tuple -> ordered positions with an immutable tuple structure
dict  -> key -> value relationships
set   -> distinct membership without positional lookup
```

Y la regla final de diseño es:

**Elige la colección que haga que la relación entre los valores sea más fácil de entender.**

## 37. A dónde ir después

Has completado los principales modelos de colección de la Fase 3.

La Fase 4 introduce **flujo de programa**: `if`, `elif`, `else`, `for`, `while` y herramientas relacionadas.

Esa siguiente fase será mucho más sencilla porque los bucles y las condiciones actuarán sobre estructuras de colección cuyo significado ya comprendes.

En lugar de aprender "cómo recorrer corchetes misteriosos", sabrás qué representa la colección antes de controlar cómo se mueve el programa a través de ella.

---

Referencias oficiales utilizadas para la verificación técnica:

- [Tutorial de Python: Estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html)
- [Tipos incorporados de Python](https://docs.python.org/es/3/library/stdtypes.html)
