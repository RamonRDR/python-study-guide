<div align="center">

# `if`, `elif` y `else`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Flujo del Programa](../README.es.md) · [← Anterior: Condiciones, Comparaciones y Lógica Booleana](../01-conditions-comparisons-and-boolean-logic/README.es.md)

Las condiciones responden preguntas. Una sentencia `if` permite que el programa **haga algo debido a la respuesta**.

El capítulo anterior construyó expresiones como `score >= 70`, `topic in topics` y `has_access and is_active`. Este capítulo usa esas expresiones para elegir qué sentencias ejecuta Python.

**Tiempo estimado de estudio:** 100–125 minutos.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué significa la ejecución condicional;
- escribir una sentencia `if` básica;
- usar correctamente los dos puntos y la indentación;
- distinguir la sintaxis de indentación de Python de la recomendación de PEP 8 de cuatro espacios por nivel;
- explicar qué ocurre cuando una condición de `if` es truthy o falsy;
- usar `else` para una decisión de dos caminos;
- usar una o más cláusulas `elif` para alternativas adicionales;
- explicar por qué solo se ejecuta la primera rama truthy de una cadena `if`/`elif`;
- ordenar deliberadamente condiciones que se solapan;
- distinguir sentencias `if` independientes de una sola cadena mutuamente exclusiva;
- combinar `if` con `and`, `or`, `not`, pruebas de pertenencia, colecciones truthy e `is None`;
- usar anidamiento moderado cuando una segunda decisión solo tiene sentido dentro de una primera;
- evitar dejar variables sin definir porque una rama no se ejecutó;
- reconocer errores comunes de principiantes relacionados con indentación, `=`, `==` y orden de ramas;
- prepararte para la coincidencia de patrones estructurales con `match` y `case` en el próximo capítulo.

## 1. Qué significa la ejecución condicional

Hasta ahora, la mayoría de los ejemplos se ejecutaron de arriba abajo y se alcanzaron todas las sentencias.

La ejecución condicional cambia ese patrón. Python evalúa una condición y usa su valor de verdad para decidir si debe ejecutar un bloque de sentencias.

La idea central es:

1. evaluar una condición;
2. si la condición es truthy, ejecutar su bloque indentado;
3. de lo contrario, omitir ese bloque;
4. continuar con el código después de la decisión completa.

Este es el primer gran punto en el que tus programas pueden seguir caminos distintos.

## 2. La sintaxis básica de `if`

Una sentencia `if` básica tiene una condición, dos puntos y un bloque indentado:

```python
if condition:
    statement
```

La palabra `if` inicia la decisión.

La expresión después de `if` se evalúa según su valor de verdad. Los dos puntos `:` terminan el encabezado de la cláusula. Las sentencias indentadas pertenecen al bloque controlado por esa cláusula.

Un ejemplo real:

```python
temperature = 24

if temperature >= 20:
    print("Comfortable temperature")
```

Salida:

```text
Comfortable temperature
```

Como `temperature >= 20` es `True`, el `print()` indentado se ejecuta.

## 3. La condición no tiene que ser literalmente `True` o `False`

Python usa pruebas de valor de verdad para la expresión que aparece después de `if`.

Esto significa que ambas formas pueden controlar una decisión:

```python
score = 82

if score >= 70:
    print("Passed")
```

y:

```python
topics = ["lists", "tuples"]

if topics:
    print("Topics available")
```

La primera condición se evalúa como el valor Booleano `True`.

La segunda condición usa el valor de verdad de una lista no vacía. Aprendiste ese comportamiento en el capítulo anterior; ahora `if` le da un propósito práctico.

## 4. Los dos puntos forman parte de la sintaxis

Cada encabezado de cláusula `if`, `elif` y `else` termina con dos puntos.

Correcto:

```python
age = 20

if age >= 18:
    print("Adult")
```

Olvidar los dos puntos es un error de sintaxis:

```python
age = 20

if age >= 18
    print("Adult")
```

Los dos puntos separan visual y sintácticamente el encabezado de la cláusula del bloque que controla.

## 5. La indentación define el bloque

Python usa la indentación inicial para agrupar sentencias en bloques.

```python
age = 20

if age >= 18:
    print("Adult")
    print("Access rule checked")

print("Done")
```

Salida:

```text
Adult
Access rule checked
Done
```

Las dos llamadas a `print()` indentadas pertenecen al bloque del `if`.

El `print("Done")` final ya no está indentado, por lo que queda fuera del bloque y se ejecuta después de la decisión.

## 6. La indentación es sintaxis; cuatro espacios son una recomendación de estilo

Estos son dos hechos relacionados, pero diferentes:

- Python usa niveles de indentación para determinar cómo se agrupan las sentencias;
- PEP 8 recomienda **cuatro espacios por nivel de indentación** para código Python normal.

Esta guía sigue la recomendación de PEP 8:

```python
if age >= 18:
    print("Adult")
```

No elimines la indentación:

```python
if age >= 18:
print("Adult")
```

Y no mezcles tabs y espacios de manera casual. Python puede rechazar una indentación inconsistente entre tabs y espacios con `TabError`.

Para quien está empezando, la regla práctica es sencilla: configura el editor para insertar cuatro espacios por nivel de indentación y mantén la consistencia.

## 7. Cuando la condición es truthy, el bloque se ejecuta

```python
score = 85

if score >= 70:
    print("Passed")

print("Result checked")
```

Salida:

```text
Passed
Result checked
```

La condición es truthy, así que Python entra en el bloque. Cuando el bloque termina, la ejecución continúa con la siguiente sentencia sin indentación.

## 8. Cuando la condición es falsy, el bloque se omite

```python
score = 50

if score >= 70:
    print("Passed")

print("Result checked")
```

Salida:

```text
Result checked
```

La sentencia `print("Passed")` se omite porque `score >= 70` es falsa.

El programa no se detiene. Simplemente continúa después del bloque de `if`.

## 9. Usa `if` cuando una acción sea opcional

Un `if` independiente es útil cuando algo debe ocurrir solo si se cumple una condición, pero no se necesita ninguna acción especial en caso contrario.

```python
has_notification = True

if has_notification:
    print("New notification")

print("Application ready")
```

Salida:

```text
New notification
Application ready
```

No es obligatorio añadir `else` a toda sentencia `if`.

## 10. `else` crea una decisión de dos caminos

Usa `else` cuando necesitas un bloque para el caso truthy y otro bloque para todos los casos restantes.

```python
is_member = False

if is_member:
    print("Member price")
else:
    print("Standard price")
```

Salida:

```text
Standard price
```

Exactamente uno de estos dos bloques se ejecuta.

## 11. `else` no tiene condición

La cláusula `else` significa: **ninguna de las condiciones anteriores de esta cadena seleccionó una rama**.

Por eso, su sintaxis es:

```python
if condition:
    statement_a
else:
    statement_b
```

Y no:

```python
if condition:
    statement_a
else other_condition:
    statement_b
```

Si necesitas otra condición, usa `elif`.

## 12. `elif` añade otra condición a la misma decisión

`elif` es la forma de Python de crear otra rama condicional dentro de la misma cadena.

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Salida:

```text
Result: Passed
```

Python comprueba las condiciones de arriba abajo.

`score >= 90` es falsa, así que continúa con el `elif`. `score >= 70` es verdadera, por lo que ese bloque se ejecuta y el resto de la cadena se omite.

## 13. Una cadena puede contener cero o más cláusulas `elif`

La gramática del lenguaje permite:

- una cláusula `if` obligatoria;
- cero o más cláusulas `elif`;
- una cláusula `else` opcional.

Una decisión de dos caminos no necesita `elif`:

```python
if is_ready:
    print("Start")
else:
    print("Wait")
```

Una decisión de varios caminos puede usar varias:

```python
level = 3

if level == 1:
    print("Beginner")
elif level == 2:
    print("Intermediate")
elif level == 3:
    print("Advanced")
else:
    print("Unknown level")
```

Salida:

```text
Advanced
```

## 14. Una cadena `if`/`elif` selecciona como máximo una rama

Esta es una de las reglas más importantes del capítulo.

Python evalúa las condiciones en orden. En cuanto una es truthy, Python ejecuta esa rama y omite el resto de la misma cadena.

```python
score = 95

if score >= 70:
    print("Passed")
elif score >= 90:
    print("Excellent")
```

Salida:

```text
Passed
```

Ambas comparaciones son matemáticamente verdaderas para `95`, pero la segunda nunca se alcanza porque la primera rama ya ganó.

## 15. El orden de las condiciones puede cambiar el resultado

Cuando las condiciones se solapan, ordénalas deliberadamente.

Un umbral más específico suele necesitar aparecer antes que uno más amplio:

```python
score = 95

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Passed")
else:
    print("Keep practicing")
```

Salida:

```text
Excellent
```

Esto no es una regla de Python que diga que "los números mayores deben ir primero". Es una consecuencia de diseño de la regla de la primera rama truthy.

Pregunta qué condiciones se solapan y ordénalas según el comportamiento que quieres obtener.

## 16. Las condiciones posteriores de la misma cadena no se evalúan después de una coincidencia

La referencia del lenguaje va más allá de decir que las ramas posteriores no se ejecutan: después de seleccionar una rama, las condiciones posteriores de esa sentencia `if` tampoco se evalúan.

```python
value = 10

if value > 0:
    print("Positive")
elif 10 / 0 > 1:
    print("Never reached")
```

Salida:

```text
Positive
```

La expresión de división fallaría si Python la evaluara. Nunca se alcanza porque `value > 0` ya seleccionó la primera rama.

Este ejemplo demuestra el orden de evaluación, no recomienda esconder expresiones inseguras en ramas posteriores.

## 17. Las sentencias `if` independientes son diferentes

Dos sentencias `if` separadas representan dos decisiones separadas.

```python
minutes = 50

if minutes >= 30:
    print("At least 30 minutes")

if minutes >= 45:
    print("At least 45 minutes")
```

Salida:

```text
At least 30 minutes
At least 45 minutes
```

Ambos bloques pueden ejecutarse porque estas son dos sentencias independientes.

## 18. Cadena frente a decisiones independientes

Compara la intención:

| Estructura | Significado |
|---|---|
| sentencias `if` separadas | cada condición es una pregunta independiente; varios bloques pueden ejecutarse |
| una cadena `if`/`elif`/`else` | elige como máximo una rama de un conjunto de alternativas |

Usa sentencias `if` independientes cuando varios hechos puedan requerir sus propias acciones.

Usa una cadena `if`/`elif` cuando las ramas sean alternativas dentro de una sola decisión.

Elegir la estructura equivocada puede producir código sintácticamente válido, pero lógicamente incorrecto.

## 19. Combina condiciones con `and`

La lógica Booleana del Capítulo 01 encaja directamente dentro de `if`.

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

Salida:

```text
Entry allowed
```

El bloque se ejecuta solo cuando ambos requisitos son truthy.

## 20. Combina alternativas con `or`

```python
is_admin = False
is_editor = True

if is_admin or is_editor:
    print("Edit access")
```

Salida:

```text
Edit access
```

Solo uno de los lados necesita ser truthy para que la condición combinada sea truthy.

Recuerda que `and` y `or` devuelven operandos, pero una sentencia `if` interpreta el valor resultante según su valor de verdad.

## 21. Usa `not` cuando la condición negativa sea más clara

```python
is_blocked = False

if not is_blocked:
    print("Account available")
```

Salida:

```text
Account available
```

Prefiere una condición que se lea de forma natural. Demasiadas capas de negación pueden hacer que una decisión sea más difícil de entender.

## 22. Las pruebas de pertenencia crean condiciones útiles

```python
topics = ["lists", "dictionaries", "sets"]

if "dictionaries" in topics:
    print("Dictionary topic found")
```

Salida:

```text
Dictionary topic found
```

El mismo patrón funciona con `not in` cuando la ausencia es la condición que te interesa.

## 23. La pertenencia en diccionarios sigue comprobando claves por defecto

Las reglas de la fase de Colecciones siguen aplicándose dentro de una sentencia `if`.

```python
profile = {"name": "Ana", "level": "beginner"}

if "name" in profile:
    print("Name field exists")
```

Salida:

```text
Name field exists
```

Esto comprueba si `"name"` es una clave. No busca en los valores del diccionario.

## 24. Las colecciones truthy pueden simplificar las pruebas de presencia

Una colección incorporada vacía es falsy; una no vacía es truthy.

```python
tasks = ["review"]

if tasks:
    print("Tasks available")
```

Salida:

```text
Tasks available
```

Para una prueba simple de presencia, esta forma suele ser más clara que escribir `if len(tasks) > 0:`.

La forma explícita con `len()` no es inválida. La forma truthy es un idioma común de Python cuando no se necesita la longitud exacta.

## 25. `not` funciona de forma natural con colecciones vacías

```python
tasks = []

if not tasks:
    print("No tasks")
```

Salida:

```text
No tasks
```

Como una lista vacía es falsy, `not tasks` se vuelve verdadero.

## 26. Usa comprobaciones de identidad para `None`

PEP 8 recomienda comparar valores singleton como `None` con `is` o `is not`.

```python
next_topic = None

if next_topic is None:
    print("No next topic selected")
```

Salida:

```text
No next topic selected
```

Esto es más claro y preciso que usar `== None`.

## 27. No escribas `== True` cuando la intención real sea probar la verdad

Supón que un nombre ya representa si algo está activo:

```python
is_active = True

if is_active:
    print("Active")
```

Salida:

```text
Active
```

Escribir `if is_active == True:` suele ser innecesario cuando simplemente quieres que Python pruebe el valor según su verdad.

Existen situaciones especializadas donde importan las comparaciones de valor o tipo exactos, pero no son el caso normal de principiante para una condición de `if`.

## 28. Las sentencias `if` anidadas crean decisiones dentro de decisiones

Un bloque controlado por un `if` puede contener otra sentencia `if`.

```python
has_account = True
email_verified = True

if has_account:
    print("Account found")

    if email_verified:
        print("Email verified")
```

Salida:

```text
Account found
Email verified
```

La segunda decisión solo se alcanza después de que la primera condición sea truthy.

## 29. Anida cuando la segunda pregunta dependa de alcanzar el primer bloque

El anidamiento puede comunicar una dependencia:

- primero determinar si existe una cuenta;
- solo entonces evaluar algo que tenga sentido sobre esa cuenta.

Pero, si dos condiciones simplemente forman un único requisito conjunto, `and` puede ser más claro:

```python
has_account = True
email_verified = True

if has_account and email_verified:
    print("Account ready")
```

Salida:

```text
Account ready
```

Ningún estilo es universalmente correcto. Elige la estructura que represente la relación entre las decisiones.

## 30. Evita el anidamiento profundo cuando una decisión más plana sea más clara

Varios niveles de sentencias `if` anidadas pueden resultar difíciles de recorrer visualmente.

En esta etapa, prefiere:

- expresiones Booleanas claras;
- una cadena `if`/`elif` sensata;
- anidamiento moderado solo cuando comunique una dependencia real.

Las fases posteriores añadirán funciones y otras técnicas que pueden ayudar a organizar lógicas de decisión mayores.

## 31. Asignar nombres dentro de ramas requiere cuidado

Una rama puede no ejecutarse.

Este código es inseguro:

```python
score = 50

if score >= 70:
    result = "Passed"

print(result)
```

Como la condición es falsa, `result` nunca se asigna. El `print(result)` posterior genera `NameError`.

Una solución es asegurarse de que todos los caminos relevantes asignen el nombre:

```python
score = 50

if score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print(result)
```

Salida:

```text
Keep practicing
```

## 32. Una cadena exhaustiva puede producir un valor de forma segura

Cuando el `else` final cubre todos los casos restantes, un nombre de resultado puede asignarse en todas las ramas.

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Salida:

```text
Result: Passed
```

Este patrón es útil cuando una decisión elige un valor que el código posterior necesita.

## 33. Las condiciones largas pueden usar paréntesis para mejorar la legibilidad

Los paréntesis permiten que una expresión continúe por varias líneas físicas sin usar barra invertida.

```python
age = 22
has_ticket = True
is_blocked = False

if (
    age >= 18
    and has_ticket
    and not is_blocked
):
    print("Entry allowed")
```

Salida:

```text
Entry allowed
```

La indentación del cuerpo sigue siendo visualmente distinta de las líneas que continúan la condición.

No añadas paréntesis solo para hacer que toda condición parezca más grande. Úsalos cuando realmente mejoren la lectura.

## 34. Prefiere bloques normales de varias líneas en esta guía

La gramática de Python permite algunos bloques simples en la misma línea física que el encabezado, pero PEP 8 generalmente desaconseja las sentencias compuestas de una sola línea.

Esta guía prefiere:

```python
if is_ready:
    print("Start")
```

en lugar de comprimir el cuerpo en la línea del encabezado.

La forma de varias líneas hace que la estructura del bloque sea más fácil de ver y permite que la decisión crezca sin quedar apretada.

## 35. Cuándo usar cada forma

Usa un `if` independiente cuando:

- una acción sea opcional;
- no exista una acción alternativa especial.

Usa `if`/`else` cuando:

- exactamente uno de dos caminos deba ejecutarse.

Usa `if`/`elif`/`else` cuando:

- estés eligiendo entre varias alternativas;
- el orden de esas alternativas sea deliberado.

Usa sentencias `if` independientes cuando:

- más de una condición pueda necesitar activar su propia acción.

Usa anidamiento moderado cuando:

- una decisión posterior solo tenga sentido después de entrar en una rama anterior.

## 36. Cuándo evitar añadir más ramas

Una sentencia `if` no es automáticamente la mejor respuesta para toda variación en los datos.

Ten cuidado cuando:

- una cadena larga solo esté mapeando claves exactas a valores exactos;
- varias condiciones repitan el mismo trabajo;
- el anidamiento se vuelva difícil de seguir;
- las condiciones describan relaciones de datos que un diccionario o conjunto podría representar de forma más directa.

No necesitas refactorizar cada decisión pequeña. El objetivo es notar cuándo la lógica de ramas describe comportamiento y cuándo simplemente está recreando una estructura de datos.

## 37. Ejemplo práctico: clasificar una sesión de estudio

El siguiente ejemplo combina `not`, `elif`, orden de umbrales y un `else` final:

```python
completed = True
minutes = 50

if not completed:
    status = "In progress"
elif minutes >= 60:
    status = "Completed: extended"
elif minutes >= 30:
    status = "Completed: focused"
else:
    status = "Completed: short"

print("Status:", status)
```

Salida:

```text
Status: Completed: focused
```

La primera rama trata las sesiones no completadas. Una vez conocida la finalización, las ramas restantes clasifican la duración desde el umbral superior más específico hasta el inferior más amplio.

## 38. Ejemplo aprobado: `basic_if.py`

```python
temperature = 24

if temperature >= 20:
    print("Comfortable temperature")

print("Check complete")
```

Salida:

```text
Comfortable temperature
Check complete
```

Este ejemplo demuestra la forma básica de `if` y muestra que el código sin indentación continúa después de la decisión.

## 39. Ejemplo aprobado: `if_elif_else.py`

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Salida:

```text
Result: Passed
```

Este ejemplo demuestra una cadena mutuamente exclusiva y un orden deliberado de umbrales.

## 40. Ejemplo aprobado: `independent_conditions.py`

```python
minutes = 50
completed = True

if completed:
    print("Session completed")

if minutes >= 30:
    print("At least 30 minutes")

if minutes >= 60:
    session_type = "Extended"
elif minutes >= 30:
    session_type = "Focused"
else:
    session_type = "Short"

print("Session type:", session_type)
```

Salida:

```text
Session completed
At least 30 minutes
Session type: Focused
```

Las dos primeras sentencias `if` son independientes, así que ambas pueden ejecutarse. La cadena final elige exactamente un tipo de sesión.

## 41. Errores comunes

### Error 1: olvidar los dos puntos

Incorrecto:

```python
if score >= 70
    print("Passed")
```

Correcto:

```python
if score >= 70:
    print("Passed")
```

### Error 2: eliminar la indentación del bloque

Incorrecto:

```python
if score >= 70:
print("Passed")
```

Correcto:

```python
if score >= 70:
    print("Passed")
```

### Error 3: usar `=` en lugar de `==`

Incorrecto:

```python
if level = 2:
    print("Intermediate")
```

Correcto:

```python
if level == 2:
    print("Intermediate")
```

La asignación y la comparación de igualdad son operaciones diferentes.

### Error 4: esperar que todos los `elif` truthy se ejecuten

Una sola cadena `if`/`elif` se detiene después de su primera rama truthy.

Usa sentencias `if` separadas cuando puedan necesitarse varias acciones independientes.

### Error 5: colocar primero una condición amplia que se solapa

```python
if score >= 70:
    print("Passed")
elif score >= 90:
    print("Excellent")
```

Una puntuación de `95` nunca alcanza la segunda condición.

### Error 6: añadir una condición después de `else`

`else` no tiene condición. Usa `elif` cuando se necesite otra prueba.

### Error 7: asumir que un nombre fue asignado en una rama omitida

Si el código posterior necesita un nombre, asegúrate de que los caminos relevantes lo asignen.

### Error 8: comparar cada nombre de apariencia Booleana con `True`

Prefiere:

```python
if is_ready:
    print("Ready")
```

cuando la intención sea una prueba de verdad normal.

## 42. Ejercicio

Crea un archivo llamado `study_decision.py`.

Empieza con:

```python
minutes = 42
completed = True
has_notes = False
```

Tu programa debe:

1. imprimir `"Session completed"` solo cuando `completed` sea truthy;
2. de forma independiente, imprimir `"Notes available"` solo cuando `has_notes` sea truthy;
3. crear un nombre `duration` usando una sola cadena `if`/`elif`/`else`:
   - `"Long"` para 60 minutos o más;
   - `"Medium"` para 30 minutos o más;
   - `"Short"` en los demás casos;
4. imprimir la duración final;
5. mantener los identificadores del código y el texto de salida en inglés.

Salida esperada para los valores iniciales:

```text
Session completed
Duration: Medium
```

Después, cambia los tres valores iniciales y predice la salida antes de ejecutar el programa otra vez.

## 43. Autoevaluación

Sin ejecutar primero este código, predice su salida:

```python
score = 92
has_bonus = True

if score >= 90 and has_bonus:
    print("Top result")
elif score >= 90:
    print("High score")
else:
    print("Standard result")

if has_bonus:
    print("Bonus recorded")
```

Respuesta:

```text
Top result
Bonus recorded
```

¿Por qué?

La primera cadena selecciona su primera rama y omite las ramas restantes de esa cadena. El `if` final es una decisión separada, por lo que se evalúa de forma independiente.

## 44. Lista de revisión

Antes de continuar, asegúrate de poder explicar:

- [ ] qué significa la ejecución condicional;
- [ ] el papel de la condición, los dos puntos y el bloque indentado en una sentencia `if`;
- [ ] por qué la indentación es sintaxis mientras cuatro espacios son una recomendación de estilo de PEP 8;
- [ ] qué ocurre cuando una condición de `if` es falsy;
- [ ] cuándo basta un `if` independiente;
- [ ] cómo `else` crea el camino restante;
- [ ] cómo `elif` añade otra alternativa comprobada;
- [ ] por qué una cadena `if`/`elif` selecciona como máximo una rama;
- [ ] por qué importa el orden de las condiciones cuando las pruebas se solapan;
- [ ] por qué las condiciones posteriores de una cadena que ya coincidió no se evalúan;
- [ ] la diferencia entre sentencias `if` independientes y una sola cadena;
- [ ] cómo `and`, `or`, `not`, pertenencia, truthiness de colecciones e `is None` encajan en las condiciones;
- [ ] cuándo el anidamiento moderado comunica una dependencia real;
- [ ] por qué un nombre asignado solo dentro de una rama omitida puede quedar sin definir;
- [ ] por qué esta guía prefiere el formato de bloques de varias líneas.

## 45. Consulta rápida

| Necesidad | Forma típica |
|---|---|
| Acción opcional | `if condition:` |
| Dos alternativas | `if condition:` ... `else:` |
| Varias alternativas | `if` ... `elif` ... `else` |
| Exigir ambas | `if condition_a and condition_b:` |
| Aceptar una u otra | `if condition_a or condition_b:` |
| Negar una condición | `if not condition:` |
| Probar pertenencia | `if item in collection:` |
| Probar ausencia | `if item not in collection:` |
| Probar `None` | `if value is None:` |
| Comprobar una colección no vacía | `if collection:` |
| Comprobar una colección vacía | `if not collection:` |
| Varias decisiones independientes | sentencias `if` separadas |
| Una decisión exclusiva | una cadena `if`/`elif`/`else` |

Recuerda la progresión:

**condición → elegir una rama → ejecutar su bloque → continuar después de la decisión**

## Siguiente paso

El próximo capítulo es **`match` y `case`: Coincidencia de Patrones Estructurales**.

Ahora sabes cómo las condiciones eligen entre ramas. A continuación, aprenderás cómo `match` compara un valor analizado con patrones, incluidas alternativas literales y el comodín `_`, antes de que el curso avance hacia la repetición con `for` en el Capítulo 04.

## Referencias oficiales

- [Referencia del lenguaje Python 3.13: sentencias compuestas y la sentencia `if`](https://docs.python.org/3.13/reference/compound_stmts.html#if)
- [Tutorial de Python: sentencias `if`](https://docs.python.org/3.13/tutorial/controlflow.html#if-statements)
- [Referencia del lenguaje Python 3.13: indentación](https://docs.python.org/3.13/reference/lexical_analysis.html#indentation)
- [PEP 8: indentación y sentencias compuestas](https://peps.python.org/pep-0008/#indentation)
