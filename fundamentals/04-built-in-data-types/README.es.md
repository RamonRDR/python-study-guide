<div align="center">

# Tipos de Datos Incorporados

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Variables y nombres](../03-variables-and-naming/README.es.md)

Las variables proporcionan nombres útiles a los valores. La siguiente pregunta es qué tipo de valor referencia cada nombre. Los valores de Python tienen tipos, y un tipo ayuda a determinar cómo se representa un valor, qué operaciones tienen sentido y cómo puede utilizarlo el programa.

Este capítulo presenta un primer grupo específico de tipos incorporados: `str`, `int`, `float`, `bool` y `NoneType`. No intenta catalogar todos los tipos de Python y deja la inspección formal con `type()` e `isinstance()` para el próximo capítulo.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar los Capítulos 01 a 03 |
| Tiempo estimado de estudio | 55 a 75 minutos |
| Conceptos principales | Valor, tipo, tipo incorporado, literal, `str`, `int`, `float`, `bool`, `None` |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar que todo valor de Python tiene un tipo;
- reconocer formas comunes en el código fuente que crean textos, enteros, números de punto flotante, valores booleanos y `None`;
- distinguir `"42"`, `42` y `42.0`;
- explicar por qué las comillas cambian el tipo de valor creado;
- escribir `True`, `False` y `None` con la capitalización obligatoria;
- usar `None` para representar un valor intencionalmente ausente;
- predecir comportamientos simples que cambian según el tipo del valor;
- recordar que `input()` retorna texto;
- reconocer que este capítulo cubre solamente un primer subconjunto de los tipos incorporados de Python.

## 1. Los valores tienen tipos

Un **valor** es un dato utilizado por un programa. Un **tipo** clasifica ese valor y define partes importantes de su comportamiento.

```text
notación del código fuente ──crea──▶ valor ──tiene──▶ tipo
```

Considera estas asignaciones:

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

Los nombres son diferentes, pero la distinción decisiva también está en los valores:

- `"Python Study Guide"` es texto;
- `4` es un número entero;
- `60.0` es un número de punto flotante;
- `True` es un valor booleano;
- `None` indica la ausencia de un valor.

## 2. Qué significa “incorporado”

Un tipo incorporado está disponible como parte del propio Python. No necesitas instalar un paquete ni escribir una instrucción `import` para crear strings, enteros, floats, valores booleanos o `None` comunes.

“Incorporado” no significa “los únicos tipos que admite Python”. Los programas también pueden utilizar tipos de colecciones, tipos proporcionados por bibliotecas y tipos creados por programadores.

## 3. La notación del código fuente crea valores

Un programa utiliza formas reconocibles en el código fuente para crear valores directamente. Las comillas, los puntos decimales y las palabras reservadas son partes significativas de esa notación.

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

Un pequeño cambio de carácter puede crear otro tipo de valor:

- `"4"` crea texto;
- `4` crea un entero;
- `4.0` crea un número de punto flotante.

El próximo capítulo mostrará cómo inspeccionar estos tipos directamente. Aquí, el objetivo es reconocerlos a partir del código fuente.

## 4. Los textos usan `str`

Python representa los datos textuales con el tipo incorporado `str`, pronunciado “string”.

```python
course_name = "Python Study Guide"
learner_name = 'Ada'

print(course_name)
print(learner_name)
```

Salida esperada:

```text
Python Study Guide
Ada
```

Las comillas simples o dobles coincidentes pueden crear literales de string comunes. Este proyecto normalmente usa comillas dobles en ejemplos pequeños por coherencia, pero ambas formas son válidas.

## 5. Las comillas no son decoración

Las comillas indican a Python que los caracteres delimitados forman texto:

```python
chapter_label = "4"
```

Sin comillas, la misma secuencia de dígitos crea un número:

```python
chapter_number = 4
```

Las comillas pertenecen al código fuente. `print()` muestra el contenido de la string sin mostrar normalmente las comillas que la delimitan.

## 6. Los números enteros usan `int`

Python representa los números enteros con el tipo incorporado `int`.

```python
chapter_number = 4
practice_minutes = 45

print(chapter_number)
print(practice_minutes)
```

Los enteros no contienen un punto decimal en su notación decimal ordinaria. Pueden ser positivos, negativos o cero:

```python
positive_value = 12
negative_value = -3
zero_value = 0
```

La aritmética detallada pertenece a la fase de textos y números. Por ahora, reconoce que `45` es un dato numérico, mientras que `"45"` es texto.

## 7. Los números de punto flotante usan `float`

Un número escrito con punto decimal normalmente crea un `float`:

```python
estimated_hours = 1.5
completion_rate = 0.75

print(estimated_hours)
print(completion_rate)
```

Los valores de punto flotante son útiles para mediciones, tasas, promedios y muchos cálculos que no se limitan a números enteros.

El punto flotante binario no puede representar exactamente todas las fracciones decimales. Ese tema de precisión importa en programas reales, pero pertenece a un capítulo numérico posterior.

## 8. Los valores lógicos usan `bool`

El tipo `bool` tiene dos valores:

- `True`;
- `False`.

```python
is_available = True
needs_review = False

print(is_available)
print(needs_review)
```

Salida esperada:

```text
True
False
```

Los valores booleanos suelen representar estados de sí o no, como disponibilidad, finalización, permiso o si se cumplió una condición.

## 9. `True` y `False` requieren capitalización

La primera letra debe ser mayúscula:

```python
is_available = True
needs_review = False

print(is_available)
print(needs_review)
```

Estas formas en minúsculas no son literales booleanos:

```text
is_available = true
needs_review = false
```

Python trata `true` y `false` en minúsculas como nombres ordinarios. Si esos nombres no fueron asignados antes, leerlos produce `NameError`.

## 10. `None` representa un valor ausente

`None` es una constante incorporada especial que se usa con frecuencia para representar la ausencia de un valor.

```python
next_chapter = None
print(next_chapter)
```

Salida esperada:

```text
None
```

`None` es la única instancia del tipo `NoneType`. Las personas principiantes normalmente escriben `None` directamente en lugar de intentar construir un valor `NoneType`.

## 11. `None` es información intencional

`None` no significa necesariamente que algo salió mal. Puede comunicar deliberadamente:

- todavía no hay un resultado disponible;
- no se proporcionó un valor opcional;
- un campo no tiene un valor aplicable;
- se espera que una etapa posterior proporcione el valor.

Elige `None` cuando “ningún valor” sea significativamente diferente de un texto válido o de un número válido.

## 12. Salidas similares pueden ocultar tipos diferentes

Estos valores parecen relacionados cuando se imprimen:

```python
text_number = "42"
whole_number = 42
decimal_number = 42.0

print(text_number)
print(whole_number)
print(decimal_number)
```

Salida esperada:

```text
42
42
42.0
```

Las dos primeras líneas muestran `42`, pero el primer valor es texto y el segundo es un entero. La salida simple no siempre revela claramente el tipo.

## 13. El tipo afecta las operaciones

El mismo operador puede comportarse de maneras diferentes con tipos distintos:

```python
text_number = "42"
whole_number = 42
decimal_number = 42.0

print("Text repeated:", text_number + text_number)
print("Integer added:", whole_number + whole_number)
print("Float added:", decimal_number + decimal_number)
```

Salida esperada:

```text
Text repeated: 4242
Integer added: 84
Float added: 84.0
```

Para las strings, `+` une textos. Para los números, `+` realiza una suma. Python utiliza los tipos de los operandos para decidir qué comportamiento se aplica.

## 14. Un booleano entre comillas es solamente texto

Compara:

```python
real_flag = True
text_flag = "True"

print(real_flag)
print(text_flag)
```

Las dos líneas muestran una palabra similar, pero `real_flag` almacena un booleano y `text_flag` almacena texto.

Usa valores booleanos reales para estados lógicos. Usa strings solamente cuando el programa realmente necesite la palabra escrita.

## 15. La palabra `"None"` no es `None`

Compara:

```python
missing_value = None
written_word = "None"

print(missing_value)
print(written_word)
```

`missing_value` almacena el marcador especial de ausencia. `written_word` almacena cuatro caracteres ordinarios de texto.

Pueden imprimirse de forma similar, pero comunican información diferente al programa.

## 16. `input()` continúa retornando `str`

El Capítulo 02 estableció una regla importante:

```python
practice_minutes = input("Practice minutes: ")
print("Stored response:", practice_minutes)
```

Aunque la persona escriba `45`, el valor retornado es texto. Python no convierte automáticamente la entrada de la terminal en un entero o un float.

La conversión de tipos tiene su propio capítulo después de que la persona estudiante pueda inspeccionar tipos de manera confiable.

## 17. Un nombre puede referenciar después otro tipo

Los nombres en Python no se declaran permanentemente como un único tipo:

```python
current_value = "42"
print(current_value)

current_value = 42
print(current_value)

current_value = 42.0
print(current_value)
```

El nombre `current_value` primero referencia una string, después un entero y finalmente un float.

Esta flexibilidad es útil, pero cambiar el significado y el tipo de la misma variable sin una razón clara puede dificultar la comprensión del código.

## 18. Los nombres deben apoyar, no reemplazar, la comprensión de los tipos

Los nombres claros pueden sugerir qué representa un valor:

```python
age_text = "30"
age_number = 30
is_active = True
missing_note = None
```

Los sufijos y prefijos mejoran la legibilidad, pero Python no los impone. Una persona todavía podría asignar el tipo incorrecto de valor.

Usa nombres significativos junto con la comprensión del valor real y de su tipo.

## 19. Este capítulo no es un catálogo completo

Python incluye muchos otros tipos incorporados. Una breve vista previa:

```python
topics = ["variables", "types"]
coordinates = (10, 20)
learner = {"name": "Ada"}
tags = {"python", "beginner"}
```

Estos ejemplos presentan listas, tuplas, diccionarios y conjuntos solamente como un mapa de lo que existe. Sus estructuras y operaciones pertenecen a la fase de colecciones.

Python también tiene otros tipos numéricos y de datos binarios. La ruta de aprendizaje los presenta cuando resultan útiles.

## 20. Ejemplos del repositorio

| Archivo | Propósito | Ejecución automática |
|---|---|---|
| [`value_catalog.py`](examples/value_catalog.py) | Almacena y muestra un ejemplo de cada categoría de valor estudiada | Sí |
| [`same_looking_values.py`](examples/same_looking_values.py) | Demuestra que valores con apariencia similar pueden comportarse de forma diferente | Sí |

Los dos ejemplos son deterministas, no interactivos y están incluidos en el manifiesto de ejemplos ejecutados sin supervisión.

## 21. Ejemplo práctico: catálogo de valores

Crea `value_catalog.py`:

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None

print("Course:", course_name)
print("Chapter:", chapter_number)
print("Estimated minutes:", estimated_minutes)
print("Available:", is_available)
print("Next chapter:", next_chapter)
```

Salida esperada:

```text
Course: Python Study Guide
Chapter: 4
Estimated minutes: 60.0
Available: True
Next chapter: None
```

Las etiquetas hacen visible la función de cada valor. La notación del código fuente revela la categoría del tipo incluso antes de que el próximo capítulo presente la inspección directa.

## 22. Ejercicio

Crea `chapter_status.py` utilizando exactamente estos nombres:

```python
guide_name
chapter_number
estimated_minutes
is_published
review_note
```

Almacena:

1. el texto `"Python Study Guide"` en `guide_name`;
2. el entero `4` en `chapter_number`;
3. el float `60.0` en `estimated_minutes`;
4. el booleano `True` en `is_published`;
5. `None` en `review_note`.

Imprime cada valor en una línea etiquetada. Después crea una versión textual del número del capítulo llamada `chapter_number_text` y asígnale `"4"`.

Añade estas dos líneas finales:

```python
print("Number result:", chapter_number + chapter_number)
print("Text result:", chapter_number_text + chapter_number_text)
```

Antes de ejecutar el programa, predice ambos resultados. Explica por qué son diferentes.

## 23. Errores comunes

### Añadir comillas a todos los valores

```python
chapter_number = "4"
```

Esto almacena texto, no un entero. Usa `4` cuando el valor deba comportarse como un número entero.

### Olvidar el punto decimal cuando se desea un float

```python
estimated_hours = 2
```

Esto crea un entero. Escribe `2.0` cuando el ejemplo necesite específicamente un valor float.

### Escribir estados lógicos como strings

```text
is_ready = "False"
```

La string `"False"` es texto. Usa el valor booleano `False` para un estado lógico.

### Escribir datos ausentes como texto

```text
next_chapter = "None"
```

La string `"None"` no es el marcador de ausencia. Usa `None`.

### Usar la capitalización incorrecta

```text
is_ready = TRUE
next_chapter = none
```

Escribe `True`, `False` y `None` exactamente como Python los define.

### Confiar solamente en la apariencia impresa

`print()` está diseñado para producir una salida legible. Tipos diferentes pueden generar textos visibles similares, por lo que la salida por sí sola no siempre basta para identificar el tipo de un valor.

El próximo capítulo presenta la inspección directa con `type()` y las verificaciones de relación con `isinstance()`.

## 24. Autoevaluación

Estás listo para el próximo capítulo cuando puedas responder:

- ¿Cuál es la relación entre un valor y un tipo?
- ¿Qué significa “incorporado”?
- ¿Qué tipo representa texto?
- ¿Cuál es la diferencia entre `"42"`, `42` y `42.0`?
- ¿Qué dos valores pertenecen a `bool`?
- ¿Por qué `true` y `false` son incorrectos en Python?
- ¿Qué representa normalmente `None`?
- ¿`"None"` es el mismo valor que `None`?
- ¿Qué tipo retorna `input()`?
- ¿Por qué el mismo símbolo `+` puede comportarse de forma diferente para strings y números?
- ¿Este capítulo enumera todos los tipos incorporados de Python?

## 25. Resumen de consulta rápida

| Categoría del valor | Ejemplo en el código fuente | Tipo incorporado |
|---|---|---|
| Texto | `"Python"` | `str` |
| Número entero | `42` | `int` |
| Número con punto decimal | `42.0` | `float` |
| Valor lógico | `True` o `False` | `bool` |
| Marcador de ausencia | `None` | `NoneType` |

Recordatorios adicionales:

- las comillas crean texto;
- un punto decimal normalmente indica un literal float;
- `True`, `False` y `None` distinguen mayúsculas y minúsculas;
- la apariencia impresa puede no revelar el tipo;
- `input()` retorna `str`;
- la conversión de tipos es deliberada y pertenece a un capítulo posterior.

## 26. Ejecuta los ejemplos del repositorio

Desde la raíz del repositorio:

```bash
python fundamentals/04-built-in-data-types/examples/value_catalog.py
python fundamentals/04-built-in-data-types/examples/same_looking_values.py
```

Los dos ejemplos están aprobados para ejecución sin supervisión.

## 27. Ejecuta las verificaciones del repositorio

Desde la raíz del repositorio:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## Referencias oficiales

- [Modelo de datos de Python — Objetos, valores y tipos](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [Biblioteca estándar de Python — Tipos incorporados](https://docs.python.org/3/library/stdtypes.html)
- [Referencia del lenguaje Python — Literales](https://docs.python.org/3/reference/lexical_analysis.html#literals)
- [Biblioteca estándar de Python — Constantes incorporadas](https://docs.python.org/3/library/constants.html)

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Variables y nombres](../03-variables-and-naming/README.es.md)
