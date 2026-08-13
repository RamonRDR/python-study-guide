<div align="center">

# Elegir y Combinar el Flujo del Programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Flujo del Programa](../README.es.md) · [← Anterior: `break`, `continue` y `else` de Bucles](../07-break-continue-and-loop-else/README.es.md)

Conocer cada herramienta de flujo del programa por separado es solo el comienzo. Los programas reales normalmente necesitan que **la selección y la repetición trabajen juntas**.

Este capítulo cierra la Fase 4 convirtiendo las herramientas anteriores en un sistema de decisión. El objetivo no es usar más sintaxis. El objetivo es elegir la **estructura de control de flujo más simple que corresponda al motivo real por el que el programa necesita ramificarse o repetir**.

**Tiempo estimado de estudio:** 120–150 minutos.

**Requisito de Python:** Python 3.10 o posterior. Este capítulo combina `match` / `case` y `zip(..., strict=True)`, ambos introducidos en Python 3.10.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- elegir `if`, `elif` y `else` cuando condiciones booleanas decidan qué se ejecuta;
- elegir `match` cuando un único valor se compare con patrones claros;
- elegir `for` cuando elementos de un iterable guíen la repetición;
- elegir `while` cuando un estado cambiante o una condición reevaluada guíe la repetición;
- elegir `range()`, `enumerate()` y `zip()` según la necesidad de la iteración;
- usar `break`, `continue` y `else` de bucles solo cuando expresen una necesidad real de control de flujo;
- combinar decisiones y bucles sin crear anidamiento innecesario;
- distinguir ramas mutuamente excluyentes de condiciones independientes;
- preferir iteración directa en vez de gestión manual de índices cuando el iterable sea el verdadero controlador;
- rastrear flujos combinados una capa a la vez;
- explicar la intención de una estructura de control de flujo en lenguaje común;
- reconocer cuándo un flujo mayor debería dividirse en funciones más adelante;
- revisar toda la Fase de Flujo del Programa como una caja de herramientas conectada.

## 1. Empieza por la pregunta de control

No empieces preguntando:

> ¿Qué palabra clave de Python puedo usar aquí?

Empieza preguntando:

> ¿Qué determina el siguiente paso de este programa?

Esa pregunta normalmente apunta hacia la herramienta correcta.

| Pregunta real | Primera herramienta a considerar |
|---|---|
| ¿Debe ejecutarse este bloque? | `if` |
| ¿Cuál de varias alternativas booleanas es verdadera? | `if` / `elif` / `else` |
| ¿Con qué patrón coincide un único valor? | `match` / `case` |
| ¿Qué debe ocurrir para cada elemento? | `for` |
| ¿Cuántos pasos numéricos deben ejecutarse? | `range()` con `for` |
| ¿Cuál es la posición de este elemento? | `enumerate()` |
| ¿Qué elementos correspondientes pertenecen juntos? | `zip()` |
| ¿Debe continuar la repetición mientras una condición siga siendo verdadera? | `while` |
| ¿El resultado ya es conocido y el bucle puede detenerse? | `break` |
| ¿Debe omitirse esta única iteración? | `continue` |
| ¿El bucle terminó sin `break`? | `else` del bucle |

Este es un punto de partida, no una ley. Varias estructuras pueden ser técnicamente válidas. Prefiere aquella cuya forma explique la intención con mayor claridad.

## 2. Elige por intención, no por hábito

Después de aprender una característica nueva, es tentador usarla en todas partes.

Eso invierte el proceso de diseño.

Compara:

```text
Process each order in this list.
```

con:

```text
Keep trying while the balance is below the target.
```

La primera frase sugiere naturalmente `for`.

La segunda sugiere naturalmente `while`.

Una estructura de control de flujo útil debería hacer que el programa sea más fácil de describir.

## 3. Usa `if` para reglas booleanas

Usa `if` cuando la pregunta importante pueda expresarse como una condición booleana.

```python
temperature = 31

if temperature >= 30:
    print("Hot")
else:
    print("Mild")
```

`if` es especialmente natural para:

- rangos y desigualdades;
- condiciones combinadas con `and`, `or` y `not`;
- pruebas de pertenencia;
- condiciones que involucran varios valores.

Ejemplo:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

Este es un problema de condición booleana.

## 4. Ramas mutuamente excluyentes frente a condiciones independientes

Una cadena `if` / `elif` / `else` representa alternativas donde, como máximo, una rama debería ejecutarse.

```python
score = 82

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Ready")
else:
    print("Review")
```

Las instrucciones `if` independientes hacen preguntas independientes:

```python
number = 12

if number > 0:
    print("Positive")

if number % 2 == 0:
    print("Even")
```

Ambas instrucciones pueden ejecutarse.

Pregunta:

> ¿Puede ser verdadera más de una respuesta al mismo tiempo?

Si es así, instrucciones `if` independientes pueden ser apropiadas.

## 5. El orden importa en `if` / `elif`

Considera:

```python
score = 95

if score >= 70:
    print("Ready")
elif score >= 90:
    print("Excellent")
```

`95` imprime `"Ready"` porque la primera condición ya tuvo éxito.

Un orden mejor es:

```python
score = 95

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Ready")
```

Cuando las condiciones se superponen, colócalas en un orden que preserve las categorías previstas.

## 6. Usa `match` para patrones alrededor de un único valor

`match` es útil cuando un valor se compara con varios patrones significativos.

```python
status = "running"

match status:
    case "queued":
        print("Waiting")
    case "running":
        print("Working")
    case "done":
        print("Finished")
    case _:
        print("Unknown")
```

El modelo mental es:

```text
Take this subject and determine which pattern it matches.
```

Un fallback comodín como `case _:` normalmente va después de los patrones más específicos.

## 7. `match` no reemplaza `if`

Esto es naturalmente booleano:

```python
amount = 125

if amount > 100:
    print("High amount")
```

Esto es naturalmente basado en patrones:

```python
command = ["move", 3]

match command:
    case ["move", steps]:
        print(f"Move {steps} steps")
    case ["stop"]:
        print("Stop")
    case _:
        print("Unknown command")
```

Usa `match` porque los patrones mejoran el modelo, no porque la sintaxis sea más nueva.

## 8. Usa `for` cuando un iterable guía la repetición

Si el requisito dice:

> Para cada elemento de esta colección...

empieza considerando `for`.

```python
names = ["Ana", "Leo", "Mia"]

for name in names:
    print(name)
```

El iterable controla la repetición.

## 9. Prefiere iteración directa a la gestión manual de índices

Esto normalmente es innecesario:

```python
names = ["Ana", "Leo", "Mia"]
index = 0

while index < len(names):
    print(names[index])
    index += 1
```

La propia lista es el verdadero controlador, así que esto es más claro:

```python
names = ["Ana", "Leo", "Mia"]

for name in names:
    print(name)
```

Usa índices solo cuando los índices formen realmente parte del problema.

## 10. Usa `while` cuando una condición o un estado cambiante guía la repetición

```python
balance = 0
target = 100

while balance < target:
    balance += 25
    print(balance)
```

El programa está diciendo:

```text
keep going while this condition remains true
```

Ese es el modelo que `while` expresa.

## 11. `for` frente a `while`

Pregunta qué crea la siguiente iteración.

| La repetición está controlada por... | Prefiere considerar... |
|---|---|
| elementos de un iterable | `for` |
| una progresión numérica | `for` + `range()` |
| estado cambiante o una condición | `while` |
| un proceso indefinido con una regla interna clara de parada | `while True` deliberado + `break` |

Usa la descripción verdadera más simple.

## 12. Elige la ayuda de iteración según la información que falta

### `range()` para una progresión numérica

```python
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
```

### `enumerate()` para elemento más posición

```python
tasks = ["read", "practice", "review"]

for position, task in enumerate(tasks, start=1):
    print(position, task)
```

### `zip()` para elementos correspondientes

```python
names = ["Ana", "Leo"]
scores = [92, 81]

for name, score in zip(names, scores, strict=True):
    print(name, score)
```

Las ayudas responden preguntas diferentes:

```text
range()      → which numeric progression?
enumerate()  → which item and which position?
zip()        → which corresponding items?
```

Apoyan un bucle `for` en vez de reemplazar su modelo guiado por iterable.

## 13. Usa `zip(strict=True)` cuando longitudes iguales sean una regla

Por defecto, `zip()` se detiene cuando se agota el iterable más corto.

Cuando longitudes iguales sean una regla de los datos, usa:

```python
for name, score in zip(names, scores, strict=True):
    print(name, score)
```

Si un iterable tiene inesperadamente un elemento extra, `strict=True` genera un error en vez de truncar silenciosamente los pares.

Si longitudes diferentes y truncamiento son intencionales, `zip()` normal puede ser la elección correcta.

## 14. Combina un bucle con una decisión cuando cada elemento necesite clasificación

Una estructura común es:

```text
for each item
    decide what this item means
```

Ejemplo:

```python
scores = [92, 67, 81, 45]

for score in scores:
    if score >= 90:
        label = "excellent"
    elif score >= 70:
        label = "ready"
    else:
        label = "review"

    print(f"{score}: {label}")
```

La estructura exterior responde **cómo ocurre la repetición**.

La estructura interior responde **qué ocurre con este elemento**.

## 15. Construye el flujo combinado de fuera hacia dentro

Requisito:

> Para cada medición, imprime solo los valores positivos.

Primero pregunta qué se repite.

Respuesta:

```text
each measurement
```

Entonces empieza con `for`.

Después pregunta qué mediciones deben imprimirse.

```python
measurements = [3, -1, 5, 0]

for measurement in measurements:
    if measurement > 0:
        print(measurement)
```

Elige primero el controlador exterior y después añade las decisiones necesarias dentro de él.

## 16. Usa `continue` cuando saltar temprano aclare el camino principal

El mismo requisito puede escribirse:

```python
measurements = [3, -1, 5, 0]

for measurement in measurements:
    if measurement <= 0:
        continue

    print(measurement)
```

Esto dice:

```text
reject items that should not continue through the body
then keep the normal path less indented
```

Ambas versiones son válidas.

Usa `continue` solo cuando mejore la legibilidad.

## 17. No añadas `continue` cuando el final natural de la iteración ya diga lo mismo

Esto es innecesario:

```python
for number in [1, 2, 3]:
    if number != 2:
        print(number)
        continue
```

La iteración terminaría naturalmente después de `print()`.

Una instrucción de control debería comunicar un cambio real en el flujo.

## 18. Usa `break` cuando más iteraciones no puedan mejorar la respuesta

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for item in items:
    if item == target:
        print("Found")
        break
```

Una vez encontrada la primera coincidencia necesaria, examinar elementos posteriores no cambiaría la respuesta.

Ese es un motivo sólido para `break`.

## 19. Usa `else` de bucle cuando terminar sin `break` tenga significado

```python
items = ["pen", "book", "cable"]
target = "mug"

for item in items:
    if item == target:
        print("Found")
        break
else:
    print("Not found")
```

El `else` del bucle significa:

```text
the loop completed without executing break
```

No significa que la última condición `if` fuera falsa.

## 20. Un patrón de búsqueda útil combina varias herramientas con claridad

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for position, item in enumerate(items, start=1):
    if item == target:
        print(f"Found {target} at position {position}")
        break
else:
    print(f"{target} not found")
```

Cada capa tiene una responsabilidad:

```text
enumerate() → expose position and item
for         → inspect items
if          → test for the target
break       → stop after the first match
else        → handle no-match completion
```

Esta es una combinación sana porque las herramientas no compiten por el mismo trabajo.

## 21. `while` se combina naturalmente con decisiones

```python
progress = 0

while progress < 3:
    progress += 1

    if progress == 2:
        print("Checkpoint")
    else:
        print("Progress", progress)
```

`while` decide si existe otro ciclo.

`if` decide qué ocurre durante el ciclo actual.

## 22. `while` y `match` pueden modelar estados explícitos

```python
state = "queued"

while state != "done":
    match state:
        case "queued":
            print("Preparing")
            state = "running"
        case "running":
            print("Processing")
            state = "done"
        case _:
            print("Unknown state")
            break
```

Las funciones son distintas:

```text
while → continue until the workflow reaches its final state
match → choose the action for the current state
```

## 23. Mantén visible el progreso de `while`

El lector debería poder responder:

> ¿Qué hace que este bucle avance hacia su final?

Prefiere actualizaciones de estado fáciles de localizar:

```python
attempt = 0

while attempt < 3:
    attempt += 1
    print(attempt)
```

Ten cuidado cuando el estado que controla la condición cambia solo dentro de algunas ramas profundamente anidadas.

## 24. Ten cuidado con `continue` dentro de `while`

Esto puede entrar en un bucle infinito:

```python
count = 0

while count < 3:
    if count == 1:
        continue

    count += 1
```

Cuando `count` se convierte en `1`, `continue` vuelve a la condición antes de que `count` cambie.

Una forma más segura es:

```python
count = 0

while count < 3:
    count += 1

    if count == 2:
        continue

    print(count)
```

La actualización ocurre antes del posible `continue`.

La organización exacta puede variar, pero todos los caminos deben preservar el progreso.

## 25. Usa `while True` solo cuando la regla interna de parada sea más clara

Una condición infinita deliberada puede tener sentido cuando la verdadera regla de parada está dentro del cuerpo:

```python
attempt = 0

while True:
    attempt += 1
    print(attempt)

    if attempt >= 3:
        break
```

Pero cuando la propia condición ya expresa la regla claramente:

```python
attempt = 0

while attempt < 3:
    attempt += 1
    print(attempt)
```

la condición directa normalmente es más fácil de entender.

No uses `while True` como plantilla predeterminada.

## 26. Prefiere un controlador principal claro por bucle

Una directriz útil de legibilidad es:

> Cada bucle debería tener un motivo principal para continuar.

En un bucle `for`, ese motivo normalmente es:

```text
there is another item
```

En un bucle `while`, normalmente es:

```text
the condition is still true
```

`if`, `break` y `continue` pueden refinar el comportamiento, pero el controlador principal debería seguir siendo visible.

Esta es una recomendación de legibilidad, no una regla de sintaxis de Python.

## 27. Aplana el flujo solo cuando la versión más plana sea más clara

Condiciones anidadas:

```python
values = [3, -1, 5, 0]

for value in values:
    if value > 0:
        if value % 2 == 1:
            print(value)
```

Condición combinada:

```python
values = [3, -1, 5, 0]

for value in values:
    if value > 0 and value % 2 == 1:
        print(value)
```

Saltos tempranos:

```python
values = [3, -1, 5, 0]

for value in values:
    if value <= 0:
        continue

    if value % 2 == 0:
        continue

    print(value)
```

Todas son posibles.

Prefiere la que haga más fáciles de explicar el camino exitoso y las reglas de rechazo.

## 28. Evita ayudas superpuestas cuando una herramienta exprese directamente la intención

Esto funciona:

```python
items = ["pen", "book", "mug"]

for index in range(len(items)):
    item = items[index]
    print(index, item)
```

Pero si la necesidad real es posición más elemento:

```python
items = ["pen", "book", "mug"]

for index, item in enumerate(items):
    print(index, item)
```

la segunda versión comunica la intención más directamente.

## 29. Explica el flujo en lenguaje común antes de defender la sintaxis

Ejemplo:

```text
For each score:
    classify it into exactly one category;
    then print the score and category.
```

Eso se corresponde naturalmente con:

```text
for
    if / elif / else
```

Otro ejemplo:

```text
Keep processing while the workflow is not done.
For the current state, choose the matching action.
```

Eso se corresponde naturalmente con:

```text
while
    match
```

Si la explicación en lenguaje común es confusa, el código puede estar haciendo demasiado.

## 30. Rastrea el flujo combinado una capa a la vez

Considera:

```python
values = [2, 5, 8]

for value in values:
    if value % 2 == 0:
        print(value)
```

Rastrea primero el bucle exterior:

| Iteración | `value` |
|---|---:|
| 1 | 2 |
| 2 | 5 |
| 3 | 8 |

Después evalúa la condición interior:

| `value` | `value % 2 == 0` | ¿Impreso? |
|---:|---|---|
| 2 | `True` | sí |
| 5 | `False` | no |
| 8 | `True` | sí |

Para un bucle `while`, rastrea el estado que controla la condición.

Rastrear por capas es más fácil que ejecutar mentalmente todas las líneas a la vez.

## 31. Ejemplo 1: iterar y clasificar

Archivo: [`examples/select_and_classify.py`](examples/select_and_classify.py)

```python
scores = [92, 67, 81, 45]

for score in scores:
    if score >= 90:
        label = "excellent"
    elif score >= 70:
        label = "ready"
    else:
        label = "review"

    print(f"{score}: {label}")
```

Salida:

```text
92: excellent
67: review
81: ready
45: review
```

¿Por qué estas herramientas?

- `for` porque cada nota debe procesarse;
- `if` / `elif` / `else` porque cada nota pertenece exactamente a una categoría booleana.

## 32. Ejemplo 2: búsqueda con posición y manejo de finalización

Archivo: [`examples/search_with_position.py`](examples/search_with_position.py)

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for position, item in enumerate(items, start=1):
    if item == target:
        print(f"Found {target} at position {position}")
        break
else:
    print(f"{target} not found")
```

Salida:

```text
Found cable at position 3
```

¿Por qué estas herramientas?

- `enumerate()` porque importan tanto el elemento como la posición amigable para una persona;
- `for` porque el iterable guía la búsqueda;
- `if` porque la igualdad decide si el objetivo fue encontrado;
- `break` porque la primera coincidencia es suficiente;
- `else` del bucle porque agotar el iterable sin `break` significa "no encontrado".

## 33. Ejemplo 3: flujo guiado por estado

Archivo: [`examples/state_driven_workflow.py`](examples/state_driven_workflow.py)

```python
state = "queued"
processed_steps = 0

while state != "done":
    match state:
        case "queued":
            print("Preparing")
            state = "running"
        case "running":
            print("Processing")
            processed_steps += 1

            if processed_steps >= 2:
                state = "done"
        case _:
            print("Unknown state")
            break

print(f"Final state: {state}")
```

Salida:

```text
Preparing
Processing
Processing
Final state: done
```

¿Por qué estas herramientas?

- `while` porque la finalización depende de un estado de workflow que evoluciona;
- `match` porque un estado selecciona una acción específica de ese estado;
- `if` porque el estado en ejecución tiene una regla de umbral adicional;
- `break` porque un estado desconocido invalidaría el flujo normal.

## 34. Compara formas válidas antes de elegir

Requisito:

> Imprime valores positivos.

Una forma directa:

```python
values = [3, -1, 5]

for value in values:
    if value > 0:
        print(value)
```

Una forma con salto temprano:

```python
values = [3, -1, 5]

for value in values:
    if value <= 0:
        continue

    print(value)
```

Una forma con índice manual:

```python
values = [3, -1, 5]
index = 0

while index < len(values):
    value = values[index]
    index += 1

    if value > 0:
        print(value)
```

Todas pueden producir la salida requerida.

La primera normalmente es la más clara porque:

- la colección guía la repetición;
- la condición es simple;
- no se necesita un salto temprano;
- no se necesita estado manual de índice.

La corrección es necesaria, pero la claridad también importa.

## 35. Una receta de decisión para el flujo del programa

Al enfrentarte a un problema nuevo, pregunta:

1. **¿Selección o repetición?**
2. Si es selección, ¿la regla es **booleana** o **basada en patrones**?
3. Si es repetición, ¿el siguiente ciclo proviene de un **iterable** o de una **condición**?
4. ¿El bucle `for` necesita `range()`, `enumerate()` o `zip()`?
5. ¿El camino normal del bucle realmente necesita `break` o `continue`?
6. ¿Terminar sin `break` tiene un resultado significativo que el `else` del bucle pueda expresar?

No elijas todas las herramientas a la vez.

Construye la estructura desde el requisito hacia afuera.

## 36. Errores comunes

### Elegir la sintaxis antes de modelar el requisito

Débil:

```text
I need to use match somewhere.
```

Mejor:

```text
I have one value with several meaningful patterns.
match may fit this model.
```

### Recorrer una colección normal con indexación manual en `while`

Si solo necesitas cada elemento, `for` normalmente lo expresa directamente.

### Usar `range(len(...))` cuando solo se necesitan los elementos

No fabriques índices automáticamente.

### Usar `match` para rangos numéricos ordenados

La lógica de umbrales normalmente queda más clara con `if` / `elif`.

### Olvidar el orden de las ramas

El primer `elif` verdadero o `case` coincidente cambia qué ramas posteriores siguen siendo alcanzables.

### Ocultar el progreso de `while`

Verifica que todo camino pueda mover el estado hacia la finalización.

### Añadir demasiados `break` y `continue`

Si el lector pregunta repetidamente adónde va la ejecución después, simplifica el bucle.

### Confundir `else` del bucle con `else` de `if`

La indentación muestra a qué instrucción pertenece la cláusula.

### Suponer que menos líneas siempre significan código más claro

Compacidad y legibilidad no son el mismo objetivo.

## 37. Ejercicio: diseña un flujo combinado

Dado:

```python
events = ["ready", "skip", "running", "done", "running"]
```

Escribe un programa que:

1. procese los eventos con `for`;
2. use `enumerate(..., start=1)` para posiciones amigables para una persona;
3. use `continue` cuando el evento sea `"skip"`;
4. use `match` para distinguir `"ready"`, `"running"`, `"done"` y eventos desconocidos;
5. imprima la posición y el evento para `"ready"` y `"running"`;
6. imprima `Done at position X` y use `break` para `"done"`;
7. use `else` del bucle para imprimir `No done event` solo si el bucle termina sin `"done"`.

Salida esperada:

```text
1: ready
3: running
Done at position 4
```

Antes de programar, escribe una frase explicando la responsabilidad de cada herramienta elegida.

## 38. Preguntas de revisión del ejercicio

Después de completar el ejercicio, responde:

- ¿Por qué `for` es más natural que `while` para la repetición exterior?
- ¿Por qué `enumerate()` es más directo que `range(len(events))`?
- ¿Qué cambia `continue` para el evento `"skip"`?
- ¿Por qué `break` impide el `else` del bucle?
- ¿Por qué `match` es razonable para los estados de los eventos?
- ¿Parte de la lógica podría expresarse con `if`?
- ¿Qué versión sería más fácil de explicar a otra persona que está empezando?

La última pregunta importa. La legibilidad forma parte de la calidad técnica.

## 39. Lista de revisión

Antes de continuar, confirma que puedes:

- [ ] explicar la diferencia entre selección y repetición;
- [ ] elegir `if` para reglas booleanas;
- [ ] elegir `match` para patrones alrededor de un único valor;
- [ ] distinguir ramas mutuamente excluyentes de condiciones independientes;
- [ ] elegir `for` para repetición guiada por iterable;
- [ ] elegir `while` para repetición guiada por estado o condición;
- [ ] elegir `range()`, `enumerate()` y `zip()` según la intención;
- [ ] decidir cuándo `zip(strict=True)` expresa una regla importante;
- [ ] usar `break` solo para una salida temprana significativa;
- [ ] usar `continue` solo para un final temprano significativo de la iteración actual;
- [ ] explicar `else` del bucle como finalización sin `break`;
- [ ] combinar bucles y decisiones manteniendo clara cada responsabilidad;
- [ ] rastrear flujos combinados una capa a la vez;
- [ ] identificar el estado que controla un bucle `while`;
- [ ] reconocer indexación manual innecesaria;
- [ ] reconocer anidamiento innecesario;
- [ ] explicar una estructura de control de flujo en lenguaje común;
- [ ] reconocer que flujos mayores se beneficiarán de funciones más adelante.

## 40. Referencia rápida

| Necesidad | Herramienta a considerar | Idea principal |
|---|---|---|
| Probar una regla booleana | `if` | ejecutar un bloque condicionalmente |
| Elegir una rama booleana ordenada | `if` / `elif` / `else` | gana la primera condición verdadera |
| Comparar un valor con patrones | `match` / `case` | gana el primer `case` coincidente |
| Procesar elementos de un iterable | `for` | el iterable guía la repetición |
| Generar progresión de enteros | `range()` | producir secuencia aritmética de enteros |
| Procesar elemento más posición | `enumerate()` | emparejar posiciones con elementos |
| Procesar iterables correspondientes | `zip()` | emparejar elementos por posición de iteración |
| Exigir entradas de igual longitud en `zip` | `zip(..., strict=True)` | convertir la igualdad de longitud en una regla |
| Repetir mientras el estado cumpla una regla | `while` | la condición guía la repetición |
| Detener ahora el bucle más cercano | `break` | finalización temprana |
| Saltar el resto de esta iteración | `continue` | finalización temprana de la iteración |
| Manejar finalización sin `break` | `else` del bucle | no ocurrió salida temprana por `break` |

## 41. El modelo mental completo de la Fase 4

Flujo del Programa ahora forma una progresión conectada:

```text
Build a trustworthy condition
        ↓
Choose a branch with if / elif / else
        ↓
Match structured alternatives with match / case
        ↓
Repeat for each iterable item with for
        ↓
Use range / enumerate / zip when iteration needs structure
        ↓
Repeat according to changing state with while
        ↓
Use break / continue / loop else when normal loop flow needs refinement
        ↓
Choose and combine only the tools that match the real requirement
```

El paso final no es otra característica de sintaxis.

Es criterio.

## 42. Finalización de la Fase 4 y qué viene después

Al completar este capítulo, has terminado la fase Flujo del Programa de Python Study Guide.

Ahora puedes razonar sobre:

- condiciones y lógica booleana;
- ramas condicionales;
- coincidencia de patrones estructurales;
- bucles guiados por iterables;
- ayudas de iteración numérica, con posición y paralela;
- bucles guiados por estado;
- finalización temprana y salto de iteraciones;
- finalización normal de bucles;
- combinaciones de estas herramientas.

Esta fase intencionalmente todavía no requiere:

- funciones definidas por el usuario con `def`;
- parámetros y valores de retorno;
- alcance de funciones;
- manejo de excepciones;
- manejo de archivos;
- comprehensions;
- módulos y paquetes;
- bibliotecas externas.

A medida que el flujo de control crece, las funciones se convierten en la siguiente herramienta natural porque permiten **nombrar y separar responsabilidades**.

La siguiente fase de aprendizaje planificada es la **Fase 5: Funciones**.

Vuelve a la [ruta completa de aprendizaje](../../docs/learning-path.es.md) o al [roadmap](../../docs/roadmap.es.md) para continuar cuando se publique la Fase 5.

## Referencias

Referencias primarias utilizadas en este capítulo:

- [Python 3.13 Tutorial: More Control Flow Tools](https://docs.python.org/3.13/tutorial/controlflow.html)
- [Python 3.13 Language Reference: Compound Statements](https://docs.python.org/3.13/reference/compound_stmts.html)
- [Python 3.13 Built-in Functions](https://docs.python.org/3.13/library/functions.html)
- [Python 3.13 Built-in Types: `range`](https://docs.python.org/3.13/library/stdtypes.html#ranges)
