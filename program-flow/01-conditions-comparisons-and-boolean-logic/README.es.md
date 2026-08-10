<div align="center">

# Condiciones, Comparaciones y Lógica Booleana

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Flujo del Programa](../README.es.md) · [← Fase anterior: Elegir la Colección Adecuada](../../collections/06-choosing-the-right-collection/README.es.md) · [Siguiente: `if`, `elif` y `else` →](../02-if-elif-and-else/README.es.md)

Las condiciones son las preguntas que un programa puede evaluar antes de decidir qué debe ocurrir a continuación.

Ya encontraste partes de esta idea en fases anteriores. Comparaciones como `score >= 70` producen valores booleanos, pruebas de pertenencia como `"lists" in topics` responden si un valor está presente y `bool()` muestra cómo Python interpreta muchos valores como verdaderos o falsos.

Este capítulo conecta esas piezas antes de introducir `if`. El objetivo es comprender las expresiones que más adelante controlarán decisiones y bucles.

**Tiempo estimado de estudio:** 100–125 minutos.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- usar comparaciones de valor como `==`, `!=`, `<`, `<=`, `>` y `>=`;
- distinguir asignación con `=` de comparación con `==`;
- leer y escribir comparaciones encadenadas;
- usar `in` y `not in` con strings y colecciones;
- explicar por qué la pertenencia en diccionarios prueba claves de forma predeterminada;
- distinguir igualdad de valor de identidad de objeto;
- usar `is None` e `is not None` adecuadamente;
- reconocer valores falsos comunes y usar `bool()` para inspeccionar valores de verdad;
- combinar condiciones con `and`, `or` y `not`;
- explicar la evaluación de cortocircuito;
- recordar que `and` y `or` pueden devolver operandos en lugar de `True` o `False`;
- usar paréntesis cuando hagan más fáciles de leer las expresiones booleanas;
- preparar condiciones claras para el siguiente capítulo sobre `if`, `elif` y `else`.

## 1. Una condición es una expresión interpretada por su valor de verdad

Una **condición** es una expresión cuyo resultado Python puede interpretar como verdadero o falso.

Una comparación es una fuente habitual de condición:

```python
score = 82

print(score >= 70)
```

```text
True
```

La expresión `score >= 70` hace una pregunta sobre dos valores. El resultado es un valor booleano.

En el siguiente capítulo, las condiciones controlarán qué bloque de código se ejecuta. Por ahora, mantén la condición separada de la propia estructura de decisión.

## 2. Las comparaciones producen valores de verdad

Python ofrece seis operadores habituales de comparación de valores:

| Operador | Significado |
|---|---|
| `==` | igual |
| `!=` | distinto |
| `<` | menor que |
| `<=` | menor que o igual |
| `>` | mayor que |
| `>=` | mayor que o igual |

Ejemplo:

```python
score = 82

print(score == 82)
print(score != 90)
print(score < 100)
print(score >= 70)
```

```text
True
True
True
True
```

Las comparaciones normalmente producen `True` o `False`.

## 3. `=` asigna; `==` compara

Estos símbolos se parecen, pero realizan trabajos distintos.

La asignación almacena o vuelve a asociar un valor:

```python
score = 82
```

La comparación pregunta si dos valores son iguales:

```python
print(score == 82)
```

```text
True
```

Un hábito útil de lectura es:

- `=` → **almacenar o asociar**
- `==` → **preguntar si los valores son iguales**

Esta diferencia se vuelve especialmente importante cuando las condiciones aparecen dentro de estructuras de flujo del programa.

## 4. Igualdad y orden son preguntas diferentes

La igualdad pregunta si los valores se consideran iguales.

El orden pregunta si un valor viene antes, después, por debajo o por encima de otro según las reglas admitidas por esos tipos.

Para números:

```python
print(10 == 10.0)
print(10 < 12.5)
```

```text
True
True
```

Los tipos numéricos de Python a menudo pueden compararse entre tipos numéricos compatibles.

Eso **no** significa que cualquier par de tipos admita orden.

Por ejemplo:

```python
print(10 < "12")
```

produce `TypeError` porque Python no define ese orden entre `int` y `str`.

```text
TypeError
```

El traceback exacto contiene información de archivo y línea. Lo importante aquí es que las comparaciones de orden requieren tipos cuyas reglas de comparación admitan esa operación.

## 5. Las comparaciones encadenadas expresan intervalos con claridad

Python permite encadenar comparaciones:

```python
age = 28

print(18 <= age < 65)
```

```text
True
```

Para este ejemplo, la idea equivale a hacer estas dos preguntas:

```python
age = 28

print(age >= 18 and age < 65)
```

```text
True
```

La forma encadenada suele ser más fácil de leer para intervalos.

Python evalúa cada expresión de una cadena de comparaciones como máximo una vez. Este detalle importa más cuando las expresiones se vuelven complejas; para principiantes, la idea principal es que las comparaciones encadenadas son una característica real de Python, no un atajo producido al reescribir el texto del código.

## 6. Las cadenas de comparación no implican todas las comparaciones posibles

Considera:

```python
value = 5

print(1 < value < 10)
```

```text
True
```

Esto significa:

- `1 < value`
- y `value < 10`

No introduce ninguna comparación adicional entre `1` y `10`.

Mantén la cadena centrada en la relación que realmente quieres expresar.

## 7. Las pruebas de pertenencia preguntan si un valor está presente

Ya usaste `in` al estudiar colecciones.

```python
topics = ["strings", "numbers", "collections"]

print("collections" in topics)
print("loops" in topics)
```

```text
True
False
```

`in` pregunta si existe pertenencia.

`not in` pregunta lo contrario:

```python
topics = ["strings", "numbers", "collections"]

print("loops" not in topics)
```

```text
True
```

Ambas formas producen resultados booleanos.

## 8. La pertenencia también funciona con strings

Para strings, la prueba de pertenencia comprueba si una string aparece dentro de otra:

```python
message = "study python"

print("python" in message)
print("java" not in message)
```

```text
True
True
```

Aunque strings y listas son tipos diferentes, ambos ofrecen pruebas de pertenencia con un significado claro.

## 9. La pertenencia en diccionarios comprueba claves de forma predeterminada

Un diccionario representa relaciones entre clave y valor.

```python
profile = {"name": "Ava", "level": "beginner"}

print("name" in profile)
print("Ava" in profile)
```

```text
True
False
```

`"name" in profile` comprueba si `"name"` es una clave.

No busca en los valores del diccionario de forma predeterminada.

Si tu pregunta trata específicamente sobre los valores, haz visible esa intención:

```python
profile = {"name": "Ava", "level": "beginner"}

print("Ava" in profile.values())
```

```text
True
```

## 10. Igualdad e identidad no son el mismo concepto

`==` compara valores según las reglas de igualdad de un tipo.

`is` pregunta si dos referencias apuntan al **mismo objeto**.

Estas preguntas pueden producir respuestas diferentes:

```python
first = [1, 2]
second = [1, 2]

print(first == second)
print(first is second)
```

```text
True
False
```

Las listas contienen valores iguales, pero son objetos de lista separados.

Para comparaciones normales de valores, usa `==` y `!=`.

No sustituyas igualdad de valor por `is` solo porque un ejemplo pequeño parezca funcionar.

## 11. Usa comparación de identidad para `None`

`None` es un valor singleton utilizado para representar la ausencia de un valor normal en muchas APIs y programas Python.

PEP 8 recomienda comparación de identidad para singletons como `None`:

```python
result = None

print(result is None)
print(result is not None)
```

```text
True
False
```

Usa:

```python
result is None
```

en lugar de:

```python
result == None
```

La segunda expresión puede producir un resultado booleano, pero `is None` comunica la comprobación de identidad pretendida y sigue la guía de estilo estándar.

## 12. Las pruebas de valor de verdad van más allá de `True` y `False` literales

Python puede interpretar muchos objetos como verdaderos o falsos en un contexto booleano.

Entre los principales valores incorporados considerados falsos están:

- `False`;
- `None`;
- cero numérico, como `0` y `0.0`;
- strings vacías;
- listas y tuplas vacías;
- diccionarios vacíos;
- conjuntos vacíos.

Ejemplo:

```python
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(None))
```

```text
False
False
False
False
False
False
```

Este comportamiento se llama **prueba de valor de verdad**.

## 13. Las colecciones no vacías normalmente son truthy

Compara valores vacíos y no vacíos:

```python
print(bool("Python"))
print(bool(["lists"]))
print(bool({"topic": "python"}))
print(bool({"python"}))
```

```text
True
True
True
True
```

Para las colecciones incorporadas presentadas hasta ahora, estar vacía o no vacía es por tanto una distinción booleana útil.

No confundas truthiness con una afirmación sobre el significado del contenido. Una lista no vacía es truthy aunque su único elemento sea `False`:

```python
print(bool([False]))
```

```text
True
```

La propia lista no está vacía.

## 14. `bool()` hace explícita la interpretación de verdad

`bool()` convierte un valor en `True` o `False` según sus reglas de valor de verdad.

```python
value = []

print(bool(value))
print(type(bool(value)))
```

```text
False
<class 'bool'>
```

Esto es útil durante el aprendizaje y la depuración.

Más adelante, las condiciones normalmente podrán usar el valor directamente sin envolver cada expresión en `bool()`.

## 15. `and` exige que el lado izquierdo sea truthy antes de evaluar el derecho

Con operandos booleanos:

```python
has_ticket = True
venue_open = True

print(has_ticket and venue_open)
```

```text
True
```

Si cualquiera de los requisitos es falso, el resultado lógico combinado es falso:

```python
has_ticket = True
venue_open = False

print(has_ticket and venue_open)
```

```text
False
```

Lee `and` como la exigencia de que ambas condiciones se cumplan cuando los operandos son condiciones booleanas.

## 16. `or` acepta la primera alternativa truthy

Con operandos booleanos:

```python
has_permission = False
is_admin = True

print(has_permission or is_admin)
```

```text
True
```

Si al menos una condición booleana es verdadera, la expresión es verdadera.

Esto hace que `or` sea útil para alternativas.

## 17. `not` invierte la interpretación de verdad y devuelve un booleano

`not` produce un resultado booleano real:

```python
is_blocked = False

print(not is_blocked)
print(not "")
print(not "Python")
```

```text
True
True
False
```

`not` pregunta por el valor de verdad opuesto.

Siempre produce `True` o `False`.

## 18. `and` y `or` no siempre devuelven `bool`

Este es uno de los detalles más importantes de este capítulo.

`and` y `or` usan pruebas de valor de verdad, pero devuelven uno de sus operandos.

Ejemplo con `or`:

```python
display_name = "" or "Guest"

print(display_name)
print(type(display_name))
```

```text
Guest
<class 'str'>
```

La string vacía es falsy, así que `or` evalúa y devuelve `"Guest"`.

Ejemplo con `and`:

```python
result = "Python" and 3

print(result)
print(type(result))
```

```text
3
<class 'int'>
```

El primer operando es truthy, así que `and` evalúa y devuelve el segundo operando.

Cuando ambos operandos son condiciones booleanas reales, el resultado a menudo parece un `True` o `False` normal. No conviertas esa apariencia en una regla de que `and` y `or` siempre devuelven `bool`.

## 19. Los operadores booleanos usan cortocircuito

Python no siempre evalúa todos los operandos.

Para `and`:

- si el operando izquierdo es falsy, ese valor se devuelve y el operando derecho no se evalúa;
- en caso contrario, el operando derecho se evalúa y se devuelve.

Para `or`:

- si el operando izquierdo es truthy, ese valor se devuelve y el operando derecho no se evalúa;
- en caso contrario, el operando derecho se evalúa y se devuelve.

Esto se llama **evaluación de cortocircuito**.

Un pequeño ejemplo muestra por qué importa:

```python
denominator = 0

safe_check = denominator != 0 and 10 / denominator > 2

print(safe_check)
```

```text
False
```

`denominator != 0` es `False`, así que Python no evalúa `10 / denominator > 2`. La expresión de división por cero nunca se alcanza.

El cortocircuito puede hacer que las condiciones sean más seguras y claras, pero no ocultes efectos secundarios importantes dentro de expresiones booleanas solo para aprovechar el orden de evaluación.

## 20. Combina comparaciones en expresiones booleanas con significado

Los operadores booleanos son especialmente útiles cuando sus operandos son comparaciones.

```python
score = 82
is_active = True

eligible = score >= 70 and is_active

print(eligible)
```

```text
True
```

Otro ejemplo:

```python
temperature = 28

needs_attention = temperature < 5 or temperature > 35

print(needs_attention)
```

```text
False
```

Intenta nombrar las variables según la pregunta que responde la expresión.

## 21. La precedencia afecta cómo se agrupan las expresiones booleanas

Entre los operadores de este capítulo:

1. comparaciones como `>=`, `==`, `in` e `is` se enlazan con mayor prioridad que los operadores booleanos;
2. `not` tiene mayor prioridad que `and`;
3. `and` tiene mayor prioridad que `or`.

Por tanto:

```python
print(True or False and False)
```

```text
True
```

Python agrupa la parte con `and` antes de la parte con `or`.

Aunque conozcas las reglas de precedencia, los paréntesis pueden hacer más visible la intención:

```python
print(True or (False and False))
```

```text
True
```

Prefiere legibilidad antes que demostrar que memorizaste la tabla de precedencia.

## 22. Los paréntesis pueden documentar los grupos pretendidos

Considera:

```python
score = 82
has_project = False
has_certificate = True

eligible = score >= 70 and (has_project or has_certificate)

print(eligible)
```

```text
True
```

Los paréntesis hacen visualmente explícitas las alternativas.

No son decorativos cuando ayudan a una persona a comprender los grupos lógicos.

## 23. No sustituyas la lógica booleana por operadores bit a bit

Python también tiene operadores como `&`, `|` y `^`.

Son principalmente **operadores bit a bit** para operaciones de bits con enteros y pueden tener significados especializados para otros tipos.

Para condiciones lógicas normales, usa:

- `and`;
- `or`;
- `not`.

No aprendas `&` y `|` como formas alternativas de escribir `and` y `or`.

## 24. Ejemplo práctico: resultados de comparaciones

El archivo [`examples/comparison_results.py`](examples/comparison_results.py) contiene:

```python
age = 28
minimum_age = 18
maximum_age = 65
topics = ["strings", "numbers", "collections"]
profile = {"name": "Ava", "level": "beginner"}

print("At least 18:", age >= minimum_age)
print("Under 65:", age < maximum_age)
print("Inside interval:", minimum_age <= age < maximum_age)
print("Collections available:", "collections" in topics)
print("Name key exists:", "name" in profile)
print("Email key missing:", "email" not in profile)
```

Salida esperada:

```text
At least 18: True
Under 65: True
Inside interval: True
Collections available: True
Name key exists: True
Email key missing: True
```

Este ejemplo combina comparación de valores, un intervalo encadenado, pertenencia en una colección y pertenencia por clave en diccionario sin introducir todavía estructuras de control.

## 25. Ejemplo práctico: lógica booleana y cortocircuito

El archivo [`examples/boolean_logic.py`](examples/boolean_logic.py) contiene:

```python
has_ticket = True
venue_open = True
is_blocked = False
denominator = 0

can_enter = has_ticket and venue_open and not is_blocked
needs_attention = not has_ticket or is_blocked
safe_ratio_check = denominator != 0 and 10 / denominator > 2
display_name = "" or "Guest"

print("Can enter:", can_enter)
print("Needs attention:", needs_attention)
print("Safe ratio check:", safe_ratio_check)
print("Display name:", display_name)
```

Salida esperada:

```text
Can enter: True
Needs attention: False
Safe ratio check: False
Display name: Guest
```

Observa que el mismo ejemplo contiene tanto condiciones booleanas como el comportamiento de `or` de devolver un operando.

## 26. Ejemplo práctico: inspeccionar valores de verdad

El archivo [`examples/truth_values.py`](examples/truth_values.py) contiene:

```python
print("Empty string:", bool(""))
print("Text:", bool("Python"))
print("Zero:", bool(0))
print("Nonzero:", bool(-3))
print("None:", bool(None))
print("Empty list:", bool([]))
print("Filled list:", bool(["python"]))
print("Empty dictionary:", bool({}))
print("Filled dictionary:", bool({"topic": "python"}))
print("Empty set:", bool(set()))
print("Filled set:", bool({"python"}))
```

Salida esperada:

```text
Empty string: False
Text: True
Zero: False
Nonzero: True
None: False
Empty list: False
Filled list: True
Empty dictionary: False
Filled dictionary: True
Empty set: False
Filled set: True
```

Los valores se eligieron intencionalmente a partir de conceptos ya presentados en fases anteriores.

## 27. Errores comunes

### Error 1: confundir asignación e igualdad

```python
score = 82
print(score == 82)
```

`=` realiza asignación. `==` realiza una comparación de igualdad.

### Error 2: usar `is` para igualdad normal de valores

Evita tratar esto como sustituto de una comparación de valor:

```python
first = [1, 2]
second = [1, 2]

print(first is second)
```

```text
False
```

Usa `==` cuando la pregunta sea si los valores se consideran iguales.

### Error 3: esperar que `and` y `or` siempre devuelvan valores booleanos

```python
print("" or "fallback")
print("Python" and 5)
```

```text
fallback
5
```

Devuelven operandos según las pruebas de valor de verdad.

### Error 4: asumir que el texto `"False"` es falsy

```python
print(bool("False"))
```

```text
True
```

La string no está vacía.

### Error 5: olvidar que la pertenencia en diccionarios comprueba claves

```python
profile = {"name": "Ava"}

print("name" in profile)
print("Ava" in profile)
```

```text
True
False
```

### Error 6: hacer que la precedencia exija trabajo mental innecesario

Esto es válido:

```python
ready = True or False and False
```

Pero cuando las condiciones reales se vuelvan más largas, usa paréntesis si facilitan reconocer los grupos pretendidos.

### Error 7: comparar valores incompatibles con operadores de orden

```python
print(10 < "12")
```

Esto produce `TypeError`.

Convierte o modela los datos adecuadamente en lugar de esperar que cualquier par de tipos tenga una relación de orden.

## 28. Ejercicio: construye un conjunto de condiciones de preparación para el estudio

Crea un archivo llamado `study_readiness.py`.

Empieza con:

```python
completed_topics = ["strings", "numbers", "collections"]
score = 82
is_active = True
optional_note = ""
```

Sin usar `if`, `elif`, `else`, `for` ni `while`, crea e imprime expresiones que respondan estas preguntas:

1. ¿`score` es al menos `70`?
2. ¿`score` está dentro del intervalo de `70` a `100`, inclusive?
3. ¿`"collections"` está presente en `completed_topics`?
4. ¿`"loops"` está ausente de `completed_topics`?
5. ¿Son verdaderos tanto el requisito de puntuación mínima como `is_active`?
6. ¿`optional_note` es truthy?
7. ¿Qué valor produce `optional_note or "No note"`?

Una implementación posible es:

```python
completed_topics = ["strings", "numbers", "collections"]
score = 82
is_active = True
optional_note = ""

minimum_reached = score >= 70
inside_expected_range = 70 <= score <= 100
has_collections = "collections" in completed_topics
loops_not_started = "loops" not in completed_topics
ready = minimum_reached and is_active
has_note = bool(optional_note)
display_note = optional_note or "No note"

print("Minimum reached:", minimum_reached)
print("Inside expected range:", inside_expected_range)
print("Has collections:", has_collections)
print("Loops not started:", loops_not_started)
print("Ready:", ready)
print("Has note:", has_note)
print("Display note:", display_note)
```

Salida esperada:

```text
Minimum reached: True
Inside expected range: True
Has collections: True
Loops not started: True
Ready: True
Has note: False
Display note: No note
```

El ejercicio se detiene intencionalmente antes de `if`. El objetivo es hacer confiable primero la propia condición.

## 29. Lista de revisión

Antes de continuar, asegúrate de poder explicar:

- [ ] la diferencia entre `=` y `==`;
- [ ] qué pregunta cada uno de los seis operadores de comparación de valor;
- [ ] por qué `18 <= age < 65` es útil;
- [ ] qué prueban `in` y `not in`;
- [ ] qué comprueba por defecto la pertenencia en diccionarios;
- [ ] la diferencia entre `==` e `is`;
- [ ] por qué se prefiere `is None`;
- [ ] qué valores incorporados comunes son falsy;
- [ ] qué hace `bool()`;
- [ ] cómo se comportan `and`, `or` y `not`;
- [ ] por qué `and` y `or` pueden devolver operandos no booleanos;
- [ ] qué significa evaluación de cortocircuito;
- [ ] por qué los paréntesis pueden mejorar la legibilidad de las condiciones.

## 30. Consulta rápida

| Necesidad | Forma típica |
|---|---|
| Valores iguales | `a == b` |
| Valores diferentes | `a != b` |
| Orden | `a < b`, `a <= b`, `a > b`, `a >= b` |
| Intervalo | `lower <= value <= upper` |
| Pertenencia | `item in collection` |
| Ausencia | `item not in collection` |
| Identidad con `None` | `value is None` |
| Identidad negada con `None` | `value is not None` |
| Exigir ambas condiciones | `condition_a and condition_b` |
| Aceptar cualquiera de las condiciones | `condition_a or condition_b` |
| Invertir el valor de verdad | `not value` |
| Inspeccionar explícitamente el valor de verdad | `bool(value)` |

Recuerda:

```text
comparison -> truth value -> Boolean combination -> future decision
```

Este capítulo construyó el lado izquierdo de ese puente. El siguiente capítulo añade la estructura de decisión.

## Siguiente paso

El siguiente capítulo es **`if`, `elif` y `else`**.

Allí, estas condiciones dejan de ser valores que solo imprimes y comienzan a controlar qué código ejecuta Python.

## Referencias oficiales

- [Tipos incorporados de Python 3.13: pruebas de valor de verdad y operaciones booleanas](https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing)
- [Referencia del lenguaje Python 3.13: comparaciones](https://docs.python.org/3.13/reference/expressions.html#comparisons)
- [PEP 8: recomendaciones de programación](https://peps.python.org/pep-0008/#programming-recommendations)
