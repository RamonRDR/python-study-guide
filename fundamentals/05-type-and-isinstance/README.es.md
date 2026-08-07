<div align="center">

# `type()` e `isinstance()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Tipos de datos incorporados](../04-built-in-data-types/README.es.md)

El Capítulo 04 enseñó a reconocer tipos comunes de valores a partir de la notación del código fuente. Este capítulo añade la inspección directa. Python proporciona `type()` para revelar el tipo exacto de un valor e `isinstance()` para preguntar si un valor pertenece a un tipo o a una familia de tipos compatible.

La diferencia importa. La identidad exacta del tipo y la compatibilidad de tipos responden preguntas distintas, especialmente cuando interviene la herencia.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar los Capítulos 01 a 04 |
| Tiempo estimado de estudio | 55 a 75 minutos |
| Conceptos principales | `type()`, `isinstance()`, tipo exacto, tipo compatible, objeto de tipo, tupla de tipos |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- inspeccionar un valor con `type()`;
- leer resultados comunes de `type()`;
- explicar que `type()` retorna un objeto de tipo y no texto;
- verificar un valor con `isinstance()`;
- pasar un tipo o una tupla de tipos a `isinstance()`;
- explicar la diferencia entre inspección del tipo exacto y verificación de compatibilidad;
- comprender por qué `isinstance(True, int)` es `True`;
- evitar comparar resultados de `type()` con strings;
- elegir entre `type()` e `isinstance()` en tareas sencillas para principiantes.

## 1. Reconocer un tipo no siempre es suficiente

A menudo puedes prever el tipo de un valor leyendo el código fuente:

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

Sin embargo, los programas no siempre reciben valores como literales evidentes. Los valores pueden provenir de llamadas a funciones, archivos, bibliotecas, cálculos o entradas de la persona usuaria.

La inspección directa responde preguntas que una simple observación visual no siempre puede responder de forma segura.

## 2. `type()` revela el tipo exacto

Llama a `type()` con un valor:

```python
course_name = "Python Study Guide"

print(type(course_name))
```

Salida esperada:

```text
<class 'str'>
```

El resultado indica que `course_name` actualmente referencia una instancia de `str`.

## 3. Inspecciona los tipos comunes del Capítulo 04

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None

print(type(course_name))
print(type(chapter_number))
print(type(estimated_minutes))
print(type(is_available))
print(type(next_chapter))
```

Salida esperada:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
```

La representación entre signos de menor y mayor es Python mostrando objetos de tipo de forma legible.

## 4. `type()` retorna un objeto, no una string de etiqueta

Esta distinción es importante:

```python
chapter_number = 5
chapter_type = type(chapter_number)

print(chapter_type)
```

`chapter_type` referencia el objeto de tipo `int`. No contiene el texto `"int"`.

Por lo tanto, esta idea es incorrecta:

```text
type(chapter_number) == "int"
```

El lado izquierdo es un objeto de tipo. El lado derecho es una string.

## 5. Los nombres de tipos como `str` e `int` también son objetos

Nombres como `str`, `int`, `float` y `bool` referencian objetos de tipo incorporados.

Por eso puedes comparar un resultado exacto de `type()` con un objeto de tipo:

```python
chapter_number = 5

print(type(chapter_number) is int)
print(type(chapter_number) is str)
```

Salida esperada:

```text
True
False
```

Aquí, `is` pregunta si las dos referencias apuntan al mismo objeto. Las comparaciones de identidad en detalle pertenecen a un tema posterior de flujo del programa; por ahora, interpreta este patrón como una verificación de tipo exacto.

## 6. Las verificaciones de tipo exacto son deliberadamente estrictas

```python
is_available = True

print(type(is_available) is bool)
print(type(is_available) is int)
```

Salida esperada:

```text
True
False
```

`type()` informa el tipo exacto del valor en tiempo de ejecución. Para `True`, ese tipo exacto es `bool`.

Esta rigidez puede ser útil, pero no siempre es la mejor manera de preguntar si un valor es aceptable para una categoría más amplia.

## 7. `isinstance()` hace una pregunta de compatibilidad

`isinstance()` recibe un valor y un tipo:

```python
chapter_number = 5

print(isinstance(chapter_number, int))
print(isinstance(chapter_number, str))
```

Salida esperada:

```text
True
False
```

Lee la primera llamada como:

> ¿`chapter_number` es una instancia de `int` o de un tipo derivado de `int`?

Esa última parte es la principal diferencia frente a una verificación exacta con `type()`.

## 8. `isinstance()` retorna un booleano

El resultado de `isinstance()` siempre es `True` o `False`:

```python
course_name = "Python Study Guide"
is_text = isinstance(course_name, str)

print(is_text)
```

Salida esperada:

```text
True
```

Puedes guardar el resultado en una variable booleana con un nombre claro y reutilizarlo después.

## 9. Verifica más de un tipo aceptado

El segundo argumento de `isinstance()` puede ser una tupla de tipos:

```python
whole_number = 5
decimal_number = 5.0
text_number = "5"

print(isinstance(whole_number, (int, float)))
print(isinstance(decimal_number, (int, float)))
print(isinstance(text_number, (int, float)))
```

Salida esperada:

```text
True
True
False
```

Esto pregunta si el valor es compatible con cualquiera de los tipos de la tupla.

## 10. No escribas `int or float` como argumento de tipo

Esta no es la misma verificación:

```text
isinstance(value, int or float)
```

La expresión `int or float` se evalúa antes de que `isinstance()` la reciba, por lo que no significa “`int` o `float`” en este contexto.

Usa una tupla:

```python
value = 5.0

print(isinstance(value, (int, float)))
```

## 11. La relación entre `bool` e `int`

Python define `bool` como una subclase de `int`. Eso produce un resultado que sorprende a muchas personas principiantes:

```python
is_available = True

print(type(is_available) is bool)
print(type(is_available) is int)
print(isinstance(is_available, bool))
print(isinstance(is_available, int))
```

Salida esperada:

```text
True
False
True
True
```

El tipo exacto es `bool`, pero un booleano también se considera una instancia de `int` en verificaciones basadas en herencia.

## 12. Por qué importa el detalle de `bool`

Imagina un programa que acepta cantidades enteras:

```python
quantity = True

print(isinstance(quantity, int))
```

Esto imprime `True`, aunque `True` puede ser una mala elección semántica para una cantidad.

La compatibilidad de tipos no reemplaza el significado del dominio. El programa todavía debe decidir si el valor tiene sentido para su finalidad.

## 13. `type()` frente a `isinstance()`

Una regla útil para principiantes es:

| Pregunta | Prefiere |
|---|---|
| ¿Cuál es el tipo exacto de este valor? | `type(value)` |
| ¿Este valor es compatible con este tipo? | `isinstance(value, SomeType)` |
| ¿Es compatible con cualquiera de varios tipos? | `isinstance(value, (TypeA, TypeB))` |
| ¿Necesito considerar subclases? | Normalmente `isinstance()` |

Usa verificaciones exactas cuando la exactitud sea realmente el requisito. Usa `isinstance()` cuando las subclases compatibles también deban contar.

## 14. `input()` es un buen ejemplo de inspección

El Capítulo 04 afirmó que `input()` retorna texto. Ahora puedes comprobarlo directamente:

```python
response = input("Practice minutes: ")

print(type(response))
```

Si la persona escribe `45`, la línea final todavía mostrará:

```text
<class 'str'>
```

Los caracteres pueden parecer numéricos, pero el valor retornado es una string.

## 15. `None` también puede inspeccionarse

```python
review_note = None

print(type(review_note))
print(isinstance(review_note, type(None)))
```

Salida esperada:

```text
<class 'NoneType'>
True
```

En el Python cotidiano, la ausencia normalmente se verifica con `is None`, no inspeccionando `NoneType`. Este ejemplo existe para conectar `None` con el sistema de tipos, no para recomendar una verificación de ausencia más larga.

## 16. La inspección de tipos es una herramienta de diagnóstico

`type()` es especialmente útil durante el aprendizaje, la depuración, la exploración de valores desconocidos y la comprobación de suposiciones.

Por ejemplo:

```python
value = "42"

print("Value:", value)
print("Type:", type(value))
```

La salida visible y la inspección del tipo juntas proporcionan más información que cualquiera de ellas por separado.

## 17. Evita distribuir verificaciones de tipo por todas partes

Un programa no se vuelve más seguro simplemente por añadir `type()` o `isinstance()` alrededor de cada valor.

Las verificaciones excesivas pueden:

- duplicar garantías ya proporcionadas en otra parte;
- volver ruidoso un código sencillo;
- ocultar un problema de diseño;
- rechazar objetos útiles y compatibles cuando las verificaciones exactas son demasiado estrictas.

Usa inspección cuando la pregunta sobre el tipo sea relevante para el programa.

## 18. Prefiere el comportamiento cuando el comportamiento sea el requisito real

A veces un programa no necesita conocer el tipo exacto. Solo necesita un objeto que soporte una operación determinada.

Esta idea más amplia suele asociarse al estilo de “duck typing” de Python. Se vuelve más útil después, cuando conozcas funciones, excepciones, protocolos y clases personalizadas.

Por ahora, recuerda: una verificación de tipo debe responder a un requisito real, no simplemente satisfacer curiosidad dentro de la lógica de producción.

## 19. Ejemplos del repositorio

| Archivo | Finalidad | Ejecución automática |
|---|---|---|
| [`inspect_types.py`](examples/inspect_types.py) | Muestra los tipos exactos del conjunto de valores del Capítulo 04 | Sí |
| [`check_type_families.py`](examples/check_type_families.py) | Compara verificaciones exactas, `isinstance()`, tuplas de tipos y la relación `bool`/`int` | Sí |

Ambos ejemplos son deterministas, no interactivos y adecuados para verificaciones sin supervisión.

## 20. Ejemplo práctico: inspecciona un pequeño catálogo de valores

Crea `inspect_types.py`:

```python
course_name = "Python Study Guide"
chapter_number = 5
estimated_minutes = 60.0
is_available = True
next_chapter = None

print("course_name:", type(course_name))
print("chapter_number:", type(chapter_number))
print("estimated_minutes:", type(estimated_minutes))
print("is_available:", type(is_available))
print("next_chapter:", type(next_chapter))
```

Salida esperada:

```text
course_name: <class 'str'>
chapter_number: <class 'int'>
estimated_minutes: <class 'float'>
is_available: <class 'bool'>
next_chapter: <class 'NoneType'>
```

## 21. Ejemplo práctico: tipo exacto y tipo compatible

Crea `check_type_families.py`:

```python
whole_number = 5
decimal_number = 5.0
is_available = True

print("Exact int:", type(whole_number) is int)
print("Number family:", isinstance(whole_number, (int, float)))
print("Float in number family:", isinstance(decimal_number, (int, float)))
print("Exact bool:", type(is_available) is bool)
print("Bool is int-compatible:", isinstance(is_available, int))
```

Salida esperada:

```text
Exact int: True
Number family: True
Float in number family: True
Exact bool: True
Bool is int-compatible: True
```

## 22. Ejercicio

Crea `value_inspector.py` con estos nombres exactos:

```python
guide_name
chapter_number
completion_rate
is_published
review_note
```

Asigna un valor de cada tipo presentado en el Capítulo 04.

Después:

1. imprime cada valor;
2. imprime el resultado de `type()` para cada valor;
3. usa `isinstance()` para confirmar que `guide_name` es una `str`;
4. usa `isinstance()` para confirmar que `chapter_number` pertenece a `(int, float)`;
5. comprueba si `completion_rate` pertenece a `(int, float)`;
6. inspecciona `is_published` con `type()` y también con `isinstance(..., int)`;
7. explica por qué los resultados finales relacionados con booleanos no son contradictorios.

## 23. Errores comunes

### Comparar un objeto de tipo con texto

```text
type(value) == "str"
```

Usa el objeto de tipo `str`, no la string `"str"`.

### Pasar una string a `isinstance()`

```text
isinstance(value, "str")
```

El argumento de tipo debe ser un objeto de tipo o una tupla aceptada de objetos de tipo.

### Usar `int or float`

```text
isinstance(value, int or float)
```

Usa:

```python
isinstance(value, (int, float))
```

### Suponer que `isinstance(True, int)` es falso

Es `True` porque `bool` es una subclase de `int`.

### Usar verificaciones exactas cuando las subclases deben contar

```python
type(value) is int
```

Esto rechaza valores cuyo tipo deriva de `int`. Usa `isinstance(value, int)` cuando las subclases compatibles también deban contar.

### Usar verificaciones de tipo en lugar de comprender los datos

Saber que un valor es `int` no indica si representa una edad, cantidad, porcentaje o identificador válido. Tipo y significado son asuntos relacionados, pero diferentes.

## 24. Autoverificación

Estás listo para el próximo capítulo cuando puedas responder:

- ¿Qué retorna `type()`?
- ¿Por qué `<class 'str'>` no es lo mismo que el texto `"str"`?
- ¿Qué pregunta responde `isinstance()`?
- ¿Cómo compruebas si un valor es `int` o `float`?
- ¿Por qué `isinstance(True, int)` es verdadero?
- ¿Cuál es el tipo exacto de `True`?
- ¿Cuándo una verificación exacta con `type()` es más estricta que `isinstance()`?
- ¿Por qué no deben añadirse verificaciones de tipo automáticamente en todas partes?
- ¿Qué tipo retorna `input()`?
- ¿Qué problema resolverá la conversión de tipos en el próximo capítulo?

## 25. Resumen de consulta rápida

| Objetivo | Ejemplo |
|---|---|
| Inspeccionar el tipo exacto | `type(value)` |
| Verificar un tipo incorporado exacto | `type(value) is int` |
| Verificar un tipo compatible | `isinstance(value, int)` |
| Aceptar varios tipos | `isinstance(value, (int, float))` |
| Inspeccionar el resultado de entrada | `type(response)` |
| Tipo booleano exacto | `type(flag) is bool` |
| Booleano compatible con `int` | `isinstance(flag, int)` |
| Evitar comparación con string | Usa `str`, no `"str"` |

## 26. Ejecuta los ejemplos del repositorio

Desde la raíz del repositorio:

```bash
python fundamentals/05-type-and-isinstance/examples/inspect_types.py
python fundamentals/05-type-and-isinstance/examples/check_type_families.py
```

## 27. Ejecuta las verificaciones del repositorio

Desde la raíz del repositorio:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

Ambos ejemplos de este capítulo están aprobados para ejecución sin supervisión.

## Referencias oficiales

- [Función incorporada de Python — `type()`](https://docs.python.org/3/library/functions.html#type)
- [Función incorporada de Python — `isinstance()`](https://docs.python.org/3/library/functions.html#isinstance)
- [Tipos incorporados de Python — valores booleanos](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)
- [Modelo de datos de Python — objetos, valores y tipos](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Tipos de datos incorporados](../04-built-in-data-types/README.es.md)
