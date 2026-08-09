<div align="center">

# Diccionarios: Claves y Valores

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Tuplas e inmutabilidad](../03-tuples-and-immutability/README.es.md) · [Volver al índice de Colecciones](../README.es.md) · Próximo capítulo: Conjuntos y valores únicos

Las listas y las tuplas organizan valores por **posición**. Los diccionarios introducen un modelo diferente: cada valor almacenado se asocia con una **clave**.

Ese cambio es poderoso porque una clave puede describir qué significa un valor. En lugar de recordar que un nombre está en la posición `0`, puedes pedir el valor almacenado bajo la clave `"name"`.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar los Capítulos 01 a 03 de Colecciones |
| Tiempo estimado de estudio | 120 a 150 minutos |
| Conceptos principales | mappings, claves, valores, literales de diccionario, búsqueda, `get()`, mutación, `update()`, eliminación, pertenencia, orden de inserción, claves hashable, vistas de diccionario, `copy()` |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar cómo un diccionario se diferencia de una secuencia posicional;
- crear diccionarios vacíos y con contenido;
- identificar claves y sus valores asociados;
- leer un valor con `dictionary[key]`;
- explicar por qué una búsqueda directa de una clave ausente produce `KeyError`;
- usar `get()` cuando una clave ausente debe devolver un valor alternativo en lugar de producir `KeyError`;
- añadir un nuevo par clave-valor mediante asignación;
- actualizar el valor asociado con una clave existente;
- combinar entradas con `update()`;
- eliminar entradas con `del`, `pop()` y `clear()`;
- comprobar pertenencia de claves con `in` y `not in`;
- explicar que las claves de un diccionario son únicas;
- reconocer tipos de clave comunes y seguros para principiantes y comprender el significado práctico de *hashable*;
- inspeccionar `keys()`, `values()` e `items()`;
- explicar el orden de inserción sin tratar un diccionario como una secuencia posicional;
- distinguir otra referencia al mismo diccionario de una copia superficial;
- elegir un diccionario cuando los valores se identifican naturalmente mediante claves significativas.

## 1. De posiciones a claves

Considera una tupla que representa a una persona ficticia que estudia:

```python
learner = ("Ana", "Python", "beginner")

print(learner[0])
print(learner[1])
```

```text
Ana
Python
```

Esto funciona, pero el significado de las posiciones `0` y `1` debe recordarse por separado.

Un diccionario hace explícitas esas relaciones:

```python
learner = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

print(learner["name"])
print(learner["track"])
```

```text
Ana
Python
```

Las claves `"name"` y `"track"` describen los valores que identifican.

Esa es la idea central de un diccionario:

**clave → valor**

## 2. Qué es un diccionario

El tipo de diccionario incorporado de Python es `dict`.

Un diccionario es un **mapping**. Un mapping asocia claves con valores en lugar de asignar valores a posiciones numeradas.

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
    "available": True,
}

print(type(course))
```

```text
<class 'dict'>
```

El diccionario contiene tres entradas. Cada entrada tiene una clave y un valor asociado.

## 3. Sintaxis de un literal de diccionario

Un literal de diccionario usa llaves con pares `key: value` separados por comas:

```python
profile = {
    "name": "Mina",
    "city": "Lisbon",
    "active": True,
}
```

Lee cada par de izquierda a derecha:

- `"name"` se mapea a `"Mina"`;
- `"city"` se mapea a `"Lisbon"`;
- `"active"` se mapea a `True`.

En diccionarios de varias líneas, una coma final después de la última entrada es un estilo común y legible.

## 4. Crear un diccionario vacío

Usa llaves vacías para crear un diccionario vacío:

```python
settings = {}

print(settings)
print(type(settings))
print(len(settings))
```

```text
{}
<class 'dict'>
0
```

Esto volverá a ser importante en el próximo capítulo: `{}` crea un **diccionario** vacío, no un conjunto vacío.

## 5. Las claves y los valores tienen roles diferentes

Una clave identifica una entrada. Un valor es la información asociada con esa clave.

```python
book = {
    "title": "A Small Python Book",
    "pages": 180,
    "finished": False,
}
```

Aquí:

- las claves son `"title"`, `"pages"` y `"finished"`;
- los valores son `"A Small Python Book"`, `180` y `False`.

Los valores no necesitan tener el mismo tipo.

## 6. Leer un valor con corchetes

Usa una clave entre corchetes para recuperar su valor:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

print(profile["name"])
print(profile["level"])
```

```text
Ana
beginner
```

Los corchetes pueden parecer familiares por las listas y tuplas, pero el modelo de búsqueda es diferente.

En una lista, la expresión entre corchetes normalmente es una posición entera. En un diccionario, es una clave.

## 7. Un diccionario no está indexado por posición

El orden de inserción no convierte un diccionario en una lista.

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

print(profile[0])
```

El diccionario anterior no tiene la clave `0`, por lo que esta búsqueda produce `KeyError`.

Si un diccionario realmente tiene una clave entera, ese entero funciona porque es una clave, no porque sea una posición:

```python
labels = {
    0: "zero",
    10: "ten",
}

print(labels[10])
```

```text
ten
```

Mantén separados los dos modelos:

- secuencia: **posición → valor**;
- diccionario: **clave → valor**.

## 8. Claves ausentes y `KeyError`

Una búsqueda directa requiere que la clave exista:

```python
profile = {
    "name": "Ana",
}

print(profile["city"])
```

Como `"city"` está ausente, Python produce `KeyError`.

Esto es útil cuando una clave ausente representa un error de programación o una suposición inválida. Más adelante, los capítulos sobre manejo de errores mostrarán cómo tratar excepciones de forma deliberada.

## 9. Leer de forma segura con `get()`

`get()` lee una clave sin producir `KeyError` cuando está ausente:

```python
profile = {
    "name": "Ana",
}

print(profile.get("name"))
print(profile.get("city"))
```

```text
Ana
None
```

Sin un valor alternativo explícito, `get()` devuelve `None` para una clave ausente.

## 10. Proporcionar un valor alternativo a `get()`

Pasa un segundo argumento cuando otro valor alternativo comunique mejor la situación:

```python
profile = {
    "name": "Ana",
}

print(profile.get("city", "not provided"))
print(profile.get("level", "unknown"))
```

```text
not provided
unknown
```

El valor alternativo se devuelve solo cuando la clave solicitada está ausente. `get()` no añade esa clave al diccionario.

## 11. Un `None` almacenado y una clave ausente pueden verse iguales

Esta diferencia importa:

```python
profile = {
    "nickname": None,
}

print(profile.get("nickname"))
print(profile.get("city"))
```

```text
None
None
```

El primer `None` está almacenado en el diccionario. El segundo `None` es el resultado predeterminado para una clave ausente.

Cuando tu programa necesite distinguir esos casos, la pertenencia de la clave se vuelve importante.

## 12. Contar entradas con `len()`

`len()` devuelve la cantidad de entradas clave-valor:

```python
profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

print(len(profile))
```

```text
3
```

Una clave y su valor asociado cuentan juntos como una entrada del diccionario.

## 13. La pertenencia comprueba claves de forma predeterminada

Los operadores `in` y `not in` comprueban las **claves** del diccionario:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("name" in profile)
print("Python" in profile)
print("city" not in profile)
```

```text
True
False
True
```

`"Python"` es un valor, no una clave, por lo que `"Python" in profile` es `False`.

Para comprobar explícitamente los valores actuales, usa la vista de valores:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("Python" in profile.values())
```

```text
True
```

## 14. Añadir una nueva entrada mediante asignación

Asigna a una clave que todavía no existe:

```python
profile = {
    "name": "Ana",
}

profile["track"] = "Python"
profile["active"] = True

print(profile)
```

```text
{'name': 'Ana', 'track': 'Python', 'active': True}
```

A diferencia de la asignación directa a un elemento de una lista, la asignación en diccionarios no requiere que una posición numérica exista primero. Una nueva clave crea una nueva entrada.

## 15. Actualizar un valor existente

Asigna a una clave que ya existe para reemplazar su valor asociado:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

profile["level"] = "intermediate"

print(profile)
```

```text
{'name': 'Ana', 'level': 'intermediate'}
```

La clave permanece igual. Su valor cambia.

Esto es mutación de diccionario: los diccionarios son objetos mutables.

## 16. Las claves de un diccionario son únicas

Un diccionario no puede contener dos entradas separadas con claves iguales al mismo tiempo.

Si la misma clave aparece más de una vez al construir un diccionario, el valor posterior pasa a ser el valor asociado con esa clave:

```python
profile = {
    "name": "Ana",
    "name": "Mina",
}

print(profile)
```

```text
{'name': 'Mina'}
```

Aunque Python define este comportamiento, repetir una clave literal normalmente perjudica la legibilidad. Prefiere una entrada clara por clave.

Los valores, en cambio, pueden repetirse:

```python
scores = {
    "first": 10,
    "second": 10,
}

print(scores)
```

```text
{'first': 10, 'second': 10}
```

## 17. Actualizar varias entradas con `update()`

`update()` aplica entradas de otro mapping o fuente compatible al diccionario existente:

```python
profile = {
    "name": "Ana",
    "level": "beginner",
}

profile.update({
    "level": "intermediate",
    "active": True,
})

print(profile)
```

```text
{'name': 'Ana', 'level': 'intermediate', 'active': True}
```

El valor existente de `"level"` fue reemplazado, mientras que `"active"` fue añadido.

Como muchos métodos de mutación in-place vistos con listas, `dict.update()` devuelve `None`.

## 18. Eliminar una entrada con `del`

Usa `del` cuando conoces la clave y no necesitas el valor eliminado:

```python
profile = {
    "name": "Ana",
    "temporary": True,
}

del profile["temporary"]

print(profile)
```

```text
{'name': 'Ana'}
```

Si la clave está ausente, `del dictionary[key]` produce `KeyError`.

## 19. Eliminar y devolver con `pop()`

`pop(key)` elimina una entrada y devuelve su valor:

```python
settings = {
    "theme": "dark",
    "language": "en",
}

removed_language = settings.pop("language")

print("Removed:", removed_language)
print("Settings:", settings)
```

```text
Removed: en
Settings: {'theme': 'dark'}
```

Esto repite una idea útil de las listas: `pop()` modifica la colección y también proporciona el valor eliminado.

También puedes proporcionar un valor alternativo para una clave ausente:

```python
settings = {
    "theme": "dark",
}

removed = settings.pop("language", "not set")

print(removed)
print(settings)
```

```text
not set
{'theme': 'dark'}
```

Con un valor alternativo, la clave ausente no produce `KeyError`.

## 20. Eliminar todas las entradas con `clear()`

`clear()` conserva el objeto diccionario, pero elimina todas sus entradas:

```python
settings = {
    "theme": "dark",
    "language": "en",
}

settings.clear()

print(settings)
print(len(settings))
```

```text
{}
0
```

`clear()` modifica el diccionario in-place y devuelve `None`.

## 21. Los diccionarios preservan el orden de inserción

A partir de Python 3.7, preservar el orden de inserción de los diccionarios es una garantía de la especificación del lenguaje Python. CPython 3.6 también preservaba el orden de inserción, pero solo como un detalle de implementación, por lo que el código destinado a Python 3.6 no debe tratar ese comportamiento como una garantía del lenguaje en todas las implementaciones.

Esto significa que, en Python 3.7 y posteriores, las entradas se observan en el orden en que se insertaron sus claves:

```python
profile = {}

profile["name"] = "Ana"
profile["track"] = "Python"
profile["level"] = "beginner"

print(profile)
```

```text
{'name': 'Ana', 'track': 'Python', 'level': 'beginner'}
```

Actualizar el valor de una clave existente no mueve esa clave a una nueva posición:

```python
profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

profile["track"] = "Data"

print(profile)
```

```text
{'name': 'Ana', 'track': 'Data', 'level': 'beginner'}
```

El orden es útil para una observación predecible, pero la búsqueda en diccionarios sigue basándose en claves, no en posiciones numeradas.

## 22. ¿Qué tipos de valores pueden ser claves?

Las claves de un diccionario deben ser **hashable**.

Para una persona principiante, el modelo práctico es:

- los strings se usan con frecuencia como claves;
- los enteros pueden ser claves;
- los booleanos pueden ser claves, aunque las claves de string descriptivas suelen ser más claras para registros;
- las tuplas pueden ser claves cuando todo su contenido es hashable;
- las listas, los diccionarios y los conjuntos no pueden ser claves de diccionario.

Una clave hashable tiene un valor hash estable adecuado para la búsqueda en diccionarios y cumple las reglas de igualdad/hash de Python. No necesitas implementar hashing por tu cuenta para usar diccionarios normales.

Esto funciona:

```python
coordinates = {
    (10, 20): "checkpoint",
}

print(coordinates[(10, 20)])
```

```text
checkpoint
```

Esto no funciona porque una lista es mutable y unhashable:

```python
invalid = {
    [10, 20]: "checkpoint",
}
```

Python produce `TypeError` al intentar usar la lista como clave.

## 23. Los valores de un diccionario son flexibles

Los valores no tienen la misma restricción que las claves. Un valor puede ser un string, número, booleano, lista, tupla, otro diccionario o muchos otros objetos de Python.

```python
profile = {
    "name": "Ana",
    "topics": ["strings", "lists"],
    "progress": (3, 6),
}

print(profile["topics"])
print(profile["progress"])
```

```text
['strings', 'lists']
(3, 6)
```

Un valor mutable dentro de un diccionario puede seguir siendo modificado:

```python
profile = {
    "name": "Ana",
    "topics": ["strings"],
}

profile["topics"].append("lists")

print(profile)
```

```text
{'name': 'Ana', 'topics': ['strings', 'lists']}
```

El diccionario mapea `"topics"` a una lista, y esa lista tiene su propio comportamiento de mutabilidad.

## 24. Inspeccionar claves con `keys()`

`keys()` devuelve una vista de diccionario que contiene las claves actuales:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.keys())
print(list(course.keys()))
```

```text
dict_keys(['title', 'phase', 'chapter'])
['title', 'phase', 'chapter']
```

Convertir la vista con `list()` es útil cuando necesitas específicamente una lista separada de las claves actuales.

## 25. Inspeccionar valores con `values()`

`values()` devuelve una vista de los valores actuales:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.values())
print(list(course.values()))
```

```text
dict_values(['Python', 3, 4])
['Python', 3, 4]
```

Recuerda que los valores no necesitan ser únicos.

## 26. Inspeccionar pares con `items()`

`items()` devuelve una vista de pares clave-valor:

```python
course = {
    "title": "Python",
    "phase": 3,
    "chapter": 4,
}

print(course.items())
print(list(course.items()))
```

```text
dict_items([('title', 'Python'), ('phase', 3), ('chapter', 4)])
[('title', 'Python'), ('phase', 3), ('chapter', 4)]
```

Cada par se comporta como una tupla de dos elementos que contiene la clave y su valor.

En la Fase 4, los bucles harán que `items()` sea especialmente útil porque podrás procesar esos pares uno por uno.

## 27. Las vistas de diccionario reflejan cambios posteriores

Los objetos devueltos por `keys()`, `values()` e `items()` son **vistas**, no snapshots congelados.

```python
profile = {
    "name": "Ana",
}

keys_view = profile.keys()
profile["level"] = "beginner"

print(list(keys_view))
```

```text
['name', 'level']
```

La vista refleja el diccionario actual.

Si necesitas un snapshot separado en código para principiantes, convertir la vista en una lista crea una lista separada en ese momento.

## 28. Crear diccionarios con `dict()`

El constructor `dict()` también puede crear diccionarios.

La construcción mediante argumentos con nombre es concisa cuando las claves de string deseadas son identificadores válidos de Python y no son palabras reservadas:

```python
profile = dict(name="Ana", level="beginner")

print(profile)
```

```text
{'name': 'Ana', 'level': 'beginner'}
```

Como ya conoces tuplas y listas, también puedes comprender una secuencia de pares clave-valor:

```python
pairs = [
    ("name", "Ana"),
    ("level", "beginner"),
]

profile = dict(pairs)

print(profile)
```

```text
{'name': 'Ana', 'level': 'beginner'}
```

Los literales de diccionario suelen ser la opción más clara para registros fijos escritos directamente en el código, pero `dict()` es útil cuando tus datos ya existen en otra forma compatible.

## 29. Otro nombre no es una copia

Los diccionarios son mutables, por lo que la lección de referencias compartidas de las listas se aplica nuevamente:

```python
original = {
    "theme": "light",
}

alias = original
alias["theme"] = "dark"

print("Original:", original)
print("Alias:", alias)
```

```text
Original: {'theme': 'dark'}
Alias: {'theme': 'dark'}
```

Ambas variables hacen referencia al mismo diccionario.

## 30. Crear una copia superficial con `copy()`

`copy()` crea un diccionario externo separado:

```python
original = {
    "theme": "light",
    "language": "en",
}

copied = original.copy()
copied["theme"] = "dark"

print("Original:", original)
print("Copied:", copied)
```

```text
Original: {'theme': 'light', 'language': 'en'}
Copied: {'theme': 'dark', 'language': 'en'}
```

Al igual que `list.copy()`, `dict.copy()` es **superficial**. Los objetos mutables anidados siguen compartidos a menos que se copien por separado.

Ese tema de copia profunda pertenece a una etapa posterior. Por ahora, recuerda que `copy()` separa el propio diccionario externo.

## 31. Cuándo un diccionario es una buena opción

Un diccionario suele ser una buena elección cuando:

- cada valor tiene una etiqueta o identificador significativo;
- quieres recuperar información mediante esa etiqueta;
- la relación entre los campos importa más que posiciones numeradas;
- necesitas añadir o actualizar campos mediante claves.

Por ejemplo:

```python
student = {
    "name": "Mina",
    "track": "Python",
    "completed_chapters": 3,
}
```

Las claves hacen que el registro se describa a sí mismo.

Una lista suele ser más clara cuando la idea principal es una serie ordenada de elementos similares. Una tupla es útil cuando la forma ordenada es intencionalmente fija. El capítulo final de Colecciones comparará directamente los cuatro tipos de colección.

## 32. Ejemplo práctico: actualizar un perfil de estudio

```python
study_profile = {
    "name": "Ana",
    "track": "Python",
    "level": "beginner",
}

study_profile["level"] = "intermediate"
study_profile["active"] = True
study_profile["topics"] = ["lists", "tuples", "dictionaries"]
removed_active = study_profile.pop("active")

print("Name:", study_profile["name"])
print("Level:", study_profile.get("level"))
print("Removed active:", removed_active)
print("Keys:", list(study_profile.keys()))
print("Profile:", study_profile)
```

```text
Name: Ana
Level: intermediate
Removed active: True
Keys: ['name', 'track', 'level', 'topics']
Profile: {'name': 'Ana', 'track': 'Python', 'level': 'intermediate', 'topics': ['lists', 'tuples', 'dictionaries']}
```

Este ejemplo combina búsqueda, actualización, adición, eliminación e inspección de claves sin necesitar bucles ni condicionales.

## 33. Errores comunes

### Tratar un diccionario como una lista

`dictionary[0]` no significa “la primera entrada”, a menos que `0` sea literalmente una clave.

### Suponer que `in` busca valores

`value in dictionary` comprueba claves. Usa `value in dictionary.values()` cuando necesites intencionalmente comprobar pertenencia entre valores.

### Usar búsqueda directa para una clave opcional

`dictionary[key]` produce `KeyError` cuando la clave está ausente. `get()` puede devolver un valor alternativo cuando se espera la ausencia.

### Olvidar que `get()` no añade la clave

Leer `dictionary.get("city", "unknown")` devuelve el valor alternativo pero deja el diccionario sin cambios.

### Suponer que todo `None` devuelto por `get()` significa “ausente”

Una clave puede almacenar legítimamente `None`. Usa información de pertenencia cuando tu programa necesite distinguir esos casos.

### Esperar que claves duplicadas creen entradas duplicadas

Las claves son únicas dentro de un diccionario. Asignar o construir la misma clave nuevamente reemplaza el valor asociado.

### Usar una lista como clave de diccionario

Las listas son unhashable y no pueden ser claves. Usa un valor hashable adecuado.

### Olvidar que los diccionarios son mutables

Otra variable puede hacer referencia al mismo diccionario. La asignación por sí sola no lo copia.

### Suponer que `copy()` duplica valores mutables anidados

`dict.copy()` es superficial. Separa el diccionario externo, no todos los objetos almacenados dentro de él.

### Confundir el orden de inserción con búsqueda posicional

El orden del diccionario se preserva, pero la búsqueda sigue basándose en claves.

## 34. Legibilidad y diseño de claves

Buenas claves de diccionario hacen que los datos sean más fáciles de comprender.

Prefiere claves que describan claramente el significado de sus valores:

```python
profile = {
    "name": "Ana",
    "completed_chapters": 4,
    "is_active": True,
}
```

Compáralo con claves vagas como `"a"`, `"b"` y `"c"`. La versión más corta puede ahorrar caracteres, pero obliga a quien lee a memorizar significados ocultos.

El mismo principio de nombres usado para variables se aplica a las claves de diccionario: elige nombres que hagan visible la relación.

## 35. Conexiones con conceptos anteriores y posteriores

Este capítulo reutiliza ideas que ya conoces:

- los corchetes se introdujeron con secuencias, pero ahora contienen claves en lugar de posiciones;
- los diccionarios son mutables como las listas;
- `copy()` de diccionario repite la idea de copia superficial de las listas;
- las tuplas pueden servir como claves de diccionario cuando su contenido es hashable;
- las listas pueden aparecer como valores de diccionario y conservar su propio comportamiento de mutabilidad;
- `len()` y los operadores de pertenencia funcionan con un nuevo modelo de colección.

También prepara conceptos posteriores:

- los conjuntos reutilizarán la idea de valores hashable y pondrán la unicidad en el centro;
- los bucles de la Fase 4 recorrerán claves, valores y pares clave-valor repetidamente;
- las funciones a menudo recibirán o devolverán diccionarios que representan datos estructurados;
- el trabajo con JSON más adelante en la guía resultará familiar porque los objetos JSON se parecen a mappings con claves de string, aunque JSON y los diccionarios de Python no son conceptos idénticos.

## 36. Ejercicio: construir y mantener un registro de aprendizaje

Crea `learning_record.py` con este diccionario inicial:

```python
record = {
    "name": "Mina",
    "track": "Python",
    "level": "beginner",
}
```

Sin usar bucles ni condicionales:

1. imprime el valor asociado con `"name"` usando búsqueda con corchetes;
2. imprime `"city"` con `get()` y el valor alternativo `"not provided"`;
3. cambia `"level"` a `"intermediate"`;
4. añade la clave `"active"` con valor `True`;
5. añade `"topics"` con la lista `["lists", "tuples"]`;
6. añade `"dictionaries"` a la lista almacenada bajo `"topics"`;
7. imprime la cantidad de entradas con `len()`;
8. imprime si `"track"` es una clave;
9. elimina `"active"` con `pop()` y guarda su valor en `removed_active`;
10. imprime `removed_active`;
11. imprime las claves como una lista;
12. imprime los valores como una lista;
13. crea una copia superficial llamada `record_copy`;
14. cambia solo `record_copy["level"]` a `"advanced"`;
15. imprime ambos diccionarios y confirma que la entrada externa `"level"` cambió solo en la copia.

Un posible formato de salida final es:

```text
Name: Mina
City: not provided
Entries: 5
Has track: True
Removed active: True
Keys: ['name', 'track', 'level', 'topics']
Values: ['Mina', 'Python', 'intermediate', ['lists', 'tuples', 'dictionaries']]
Original: {'name': 'Mina', 'track': 'Python', 'level': 'intermediate', 'topics': ['lists', 'tuples', 'dictionaries']}
Copy: {'name': 'Mina', 'track': 'Python', 'level': 'advanced', 'topics': ['lists', 'tuples', 'dictionaries']}
```

Intenta predecir el diccionario después de cada mutación antes de ejecutar el programa.

## 37. Autoevaluación

Antes de continuar, asegúrate de poder responder estas preguntas:

1. ¿Cuál es la principal diferencia de búsqueda entre una secuencia y un diccionario?
2. ¿Qué hace `dictionary[key]` cuando la clave está ausente?
3. ¿Qué devuelve `get()` para una clave ausente cuando no se proporciona un valor alternativo?
4. ¿`get()` añade una clave ausente?
5. ¿Qué comprueba `in` en un diccionario de forma predeterminada?
6. ¿Qué ocurre cuando asignas a una nueva clave?
7. ¿Qué ocurre cuando asignas a una clave existente?
8. ¿Puede un diccionario contener dos claves iguales separadas al mismo tiempo?
9. ¿Por qué un string normalmente puede ser una clave mientras que una lista no puede?
10. ¿Qué exponen `keys()`, `values()` e `items()`?
11. ¿El orden de inserción convierte posiciones enteras en índices válidos de un diccionario?
12. ¿Qué devuelve `pop(key)`?
13. ¿Por qué las mutaciones mediante un alias pueden afectar al diccionario original?
14. ¿Qué separa `copy()` y sobre qué advierte la palabra *superficial*?

Si alguna respuesta no está clara, vuelve a la sección correspondiente y modifica uno de los ejemplos por tu cuenta.

## 38. Referencia rápida

- Crear un diccionario vacío: `data = {}`
- Crear entradas: `data = {"key": "value"}`
- Leer una clave existente: `value = data["key"]`
- Leer con valor alternativo: `value = data.get("key", fallback)`
- Contar entradas: `len(data)`
- Comprobar una clave: `"key" in data`
- Comprobar un valor explícitamente: `value in data.values()`
- Añadir o reemplazar: `data["key"] = value`
- Aplicar varias entradas: `data.update(other)`
- Eliminar por clave: `del data["key"]`
- Eliminar y devolver: `removed = data.pop("key")`
- Vaciar el diccionario: `data.clear()`
- Inspeccionar claves: `data.keys()`
- Inspeccionar valores: `data.values()`
- Inspeccionar pares clave-valor: `data.items()`
- Crear una copia superficial externa: `other = data.copy()`

Recuerda el modelo:

- las claves identifican entradas;
- las claves son únicas y deben ser hashable;
- los valores pueden repetirse y pueden ser mutables;
- los diccionarios son mutables;
- los diccionarios preservan el orden de inserción;
- el orden preservado no crea indexación posicional.

## 39. A dónde ir después

Ahora conoces tres modelos diferentes de colección:

1. **Lista:** posiciones ordenadas que pueden modificarse.
2. **Tupla:** posiciones ordenadas cuya estructura de tupla no puede modificarse.
3. **Diccionario:** claves significativas mapeadas a valores.

El próximo capítulo de Colecciones introduce **conjuntos y valores únicos**. Los conjuntos eliminarán por completo los pares clave-valor y la búsqueda posicional, colocando la unicidad y la pertenencia en el centro del modelo.

---

Referencias oficiales utilizadas para la verificación técnica:

- [Tutorial de Python: Diccionarios](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Tipos incorporados de Python: Mapping Types — `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Glosario de Python: hashable](https://docs.python.org/3/glossary.html#term-hashable)
