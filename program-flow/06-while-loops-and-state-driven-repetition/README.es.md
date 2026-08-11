<div align="center">

# Bucles `while` y Repetición Guiada por Estado

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Flujo del Programa](../README.es.md) · [← Anterior: `range()`, `enumerate()` y `zip()`](../05-range-enumerate-and-zip/README.es.md)

Un bucle `for` repite trabajo consumiendo elementos de un iterable. Un bucle `while` responde a una pregunta diferente:

**¿Debe este trabajo ocurrir otra vez según el estado actual del programa?**

Este capítulo introduce la repetición controlada por una condición que vuelve a evaluarse antes de cada iteración.

**Tiempo estimado de estudio:** 105–130 minutos.

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- explicar qué es un bucle `while` y por qué existe;
- escribir la sintaxis básica `while condition:` con la indentación correcta;
- explicar que la condición se evalúa antes de cada iteración;
- reconocer que el cuerpo de un `while` puede ejecutarse cero veces;
- conectar las condiciones de `while` con las pruebas de valor de verdad de capítulos anteriores;
- describir el ciclo de estado inicial, condición, cuerpo, actualización del estado y nueva evaluación;
- actualizar el estado deliberadamente para que un bucle finito avance hacia su finalización;
- usar contadores, acumuladores y límites con `while`;
- explicar por qué un bucle no necesita llegar exactamente a un límite numérico para terminar;
- distinguir bucles `for` guiados por iterables de bucles `while` guiados por estado;
- reconocer causas comunes de bucles infinitos;
- comprobar si una actualización mueve el estado hacia o lejos de la condición de parada;
- entender que más de una variable puede participar en la condición del bucle;
- reconocer que modificar una colección también puede cambiar el estado evaluado por el bucle;
- entender qué significa `while True` sin usarlo todavía como ejemplo ejecutable seguro;
- mantener `break`, `continue` y `else` de bucle separados hasta el próximo capítulo;
- elegir `while` solo cuando su modelo guiado por estado comunique la tarea con mayor claridad que `for`.

## 1. Por qué existe `while`

Los dos capítulos anteriores se concentraron en repetición guiada por iterables:

```python
for item in iterable:
    statement
```

Ese modelo es excelente cuando el programa ya tiene algo que recorrer, como una lista, string, diccionario, `range`, objeto `enumerate` u objeto `zip`.

Pero algunas tareas no se describen naturalmente como “para cada elemento”.

En cambio, suenan así:

```text
mientras quede trabajo, continúa
mientras un valor esté por debajo de un límite, sigue actualizándolo
mientras una condición permanezca verdadera, repite el bloque
```

Ese es el papel de `while`.

## 2. La sintaxis básica

La forma básica es:

```python
while condition:
    statement
```

Los dos puntos terminan el encabezado de `while`, y el bloque indentado es el cuerpo del bucle.

Por ejemplo:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

Salida:

```text
3
2
1
```

El bucle sigue ejecutándose mientras `remaining > 0` sea verdadero.

## 3. Un bucle `while` evalúa antes de ejecutar el cuerpo

Un bucle `while` es un **bucle de preprueba**: Python evalúa la condición antes de entrar en el cuerpo en cada vuelta.

El flujo es:

```text
evaluar condición
    ↓
verdadera -> ejecutar cuerpo -> evaluar condición otra vez
falsa     -> salir del bucle
```

Este detalle explica varios comportamientos importantes del resto del capítulo.

## 4. El cuerpo puede ejecutarse cero veces

Como la condición se evalúa primero, el cuerpo se omite cuando ya es falsa.

```python
remaining = 0

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Done")
```

Salida:

```text
Done
```

El propio bucle realizó cero iteraciones.

## 5. `while` usa pruebas de valor de verdad

La condición no tiene que ser un valor escrito literalmente como `True` o `False`.

Python evalúa el valor de verdad de la expresión, igual que en una condición `if`.

Eso significa que las ideas booleanas del Capítulo 01 siguen aplicándose:

```python
attempts = 2

while attempts:
    print(attempts)
    attempts = attempts - 1
```

Como los enteros distintos de cero son verdaderos y cero es falso, esto imprime:

```text
2
1
```

En código para principiantes, una comparación explícita como `while attempts > 0:` suele ser más fácil de leer porque expresa directamente la regla prevista.

## 6. El modelo mental central: el estado cambia con el tiempo

Una forma útil de razonar sobre un bucle `while` finito es:

```text
1. establecer el estado inicial
2. evaluar la condición
3. ejecutar el cuerpo si la condición es verdadera
4. actualizar el estado relevante
5. volver a la condición
6. detenerse cuando la condición sea falsa
```

La nueva idea importante es **estado**: información cuyo valor actual afecta si debe ocurrir otra iteración.

## 7. El estado es aquello de lo que depende la condición

En este bucle:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

`remaining` es estado del bucle porque la condición depende de él.

El estado empieza en `3`, después pasa a `2`, `1` y finalmente `0`.

Cuando Python evalúa `remaining > 0` con `remaining == 0`, la condición es falsa y el bucle termina.

## 8. Un bucle finito necesita un camino hacia la finalización

Si un bucle debe terminar normalmente, algo tiene que hacer falsa su condición en algún momento.

Para la cuenta regresiva:

```text
estado inicial: 3
condición:      remaining > 0
actualización:  remaining = remaining - 1
```

La actualización mueve el estado hacia el punto donde la condición falla.

Una pregunta práctica al leer un `while` es:

**¿Qué cambia y cómo puede ese cambio hacer falsa la condición eventualmente?**

## 9. Contar hacia arriba con `while`

El estado también puede aumentar:

```python
number = 1

while number <= 3:
    print(number)
    number = number + 1
```

Salida:

```text
1
2
3
```

La condición se vuelve falsa después de que `number` cambia de `3` a `4`.

## 10. Contar hacia abajo con `while`

Una cuenta regresiva usa la dirección opuesta:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

Salida:

```text
3
2
1
Start
```

El `print()` final está fuera del bucle porque debe ejecutarse solo después de que termine la repetición.

## 11. La indentación decide qué se repite

Compara estas dos formas:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

y:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
    print("Still inside the loop")
```

Solo las instrucciones indentadas bajo el encabezado `while` pertenecen al cuerpo del bucle.

Por lo tanto, la indentación forma parte tanto de la sintaxis de Python como del significado del programa.

## 12. La inicialización ocurre antes de la primera evaluación

La condición normalmente depende de un estado que ya debe existir:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

La asignación `remaining = 3` ocurre antes de que Python llegue a la primera evaluación de la condición.

Un orden útil de lectura es:

```text
inicializar -> evaluar -> trabajar -> actualizar -> evaluar otra vez
```

## 13. La actualización no tiene que ser la última instrucción

No existe una regla de Python que obligue a que la actualización del estado sea la última línea del cuerpo.

Sin embargo, colocar la actualización importante donde sea fácil verla suele mejorar la legibilidad:

```python
progress = 0

while progress < 3:
    progress = progress + 1
    print(f"Progress: {progress}")
```

El requisito clave es semántico: el estado del bucle cambia de una forma coherente con la condición y el comportamiento deseado.

## 14. Repetición controlada por límite

Un bucle `while` es útil cuando la repetición depende de alcanzar o superar un límite mediante un estado que cambia.

```python
studied_minutes = 0
session_minutes = 20
target_minutes = 60

while studied_minutes < target_minutes:
    studied_minutes = studied_minutes + session_minutes
    print(f"Study total: {studied_minutes} min")
```

Salida:

```text
Study total: 20 min
Study total: 40 min
Study total: 60 min
```

El número de iteraciones surge del estado cambiante y de la condición.

## 15. Un acumulador también puede controlar el bucle

Un acumulador guarda un resultado en curso.

En el ejemplo anterior, `studied_minutes` es a la vez:

- un acumulador que guarda el total actual;
- estado utilizado por la condición del `while`.

Una variable puede cumplir más de un papel cuando esos papeles describen claramente el mismo valor en evolución.

## 16. El estado no tiene que llegar exactamente al límite

Considera:

```python
value = 1
limit = 20

while value < limit:
    print(value)
    value = value * 2

print(value)
```

Salida:

```text
1
2
4
8
16
32
```

El bucle se detiene porque `32 < 20` es falso en la siguiente evaluación.

Nada exige que el estado llegue exactamente a `20`.

La regla de parada es el valor de verdad de la condición, no que un valor límite haya sido visitado exactamente.

## 17. La condición se vuelve a evaluar con el estado actual

Python no calcula la condición una vez para reutilizar ese resultado indefinidamente.

Cada vuelta regresa al encabezado y evalúa de nuevo la expresión usando los valores actuales.

Para:

```python
value = 1

while value < 5:
    value = value * 2
```

Python observa efectivamente:

```text
1 < 5 -> True
2 < 5 -> True
4 < 5 -> True
8 < 5 -> False
```

Esa reevaluación repetida es el motor de un bucle `while`.

## 18. `for` y `while` resuelven formas distintas de repetición

Una primera distinción útil es:

```text
for   -> repetir para elementos de un iterable
while -> repetir mientras una condición permanezca verdadera
```

Por ejemplo, cuando la tarea consiste simplemente en imprimir `1`, `2` y `3`, un bucle `for` suele ser más claro:

```python
for number in range(1, 4):
    print(number)
```

Una versión con `while` puede funcionar:

```python
number = 1

while number <= 3:
    print(number)
    number = number + 1
```

Pero introduce estado manual que `range()` podría proporcionar directamente.

## 19. Prefiere `for` cuando el iterable ya expresa la tarea

Si ya tienes una colección:

```python
topics = ["conditions", "loops", "functions"]
```

esto es directo:

```python
for topic in topics:
    print(topic)
```

Reconstruir el mismo recorrido manualmente con índices y `while` añadiría gestión de estado sin mejorar el significado.

Usa `while` porque la condición de continuación sea el modelo natural, no solo porque pueda imitar a `for`.

## 20. Prefiere `while` cuando la siguiente repetición depende del estado actual

Una tarea guiada por estado puede no conocer de antemano su cantidad útil de iteraciones.

Por ejemplo:

```python
value = 1
limit = 100

while value < limit:
    value = value * 2
```

La idea importante no es “repite exactamente siete veces”.

La idea importante es “sigue duplicando mientras el valor permanezca por debajo del límite”.

Esa intención encaja naturalmente con `while`.

## 21. Bucle infinito: olvidar actualizar el estado

Este bucle nunca cambia el valor utilizado por su condición:

```python
remaining = 3

while remaining > 0:
    print(remaining)
```

`remaining > 0` permanece verdadero para siempre.

Si se ejecuta, el bucle sigue imprimiendo `3` salvo que algo externo a la finalización normal del bucle interrumpa el programa.

Este ejemplo se muestra para explicar el error. Intencionalmente no forma parte del manifiesto de ejemplos ejecutables del repositorio.

## 22. Bucle infinito: actualizar en la dirección equivocada

Puede existir una actualización y aun así alejar el estado de la finalización:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining + 1
```

Los valores pasan a ser `3`, `4`, `5` y así sucesivamente, por lo que `remaining > 0` no se vuelve falso.

No preguntes solamente si el estado cambia. Pregunta si cambia **hacia un estado capaz de detener el bucle**.

## 23. Bucle infinito: restablecer el estado dentro del cuerpo

Un error menos evidente consiste en restaurar repetidamente el mismo estado:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = 2
```

Después de la primera vuelta, `remaining` permanece en `2` para siempre.

El progreso exige más que una asignación. La secuencia de estados debe permitir la finalización.

## 24. Las condiciones pueden combinar varias partes del estado

Una condición `while` puede usar los operadores booleanos aprendidos anteriormente:

```python
remaining = 5
energy = 3

while remaining > 0 and energy > 0:
    print(remaining, energy)
    remaining = remaining - 1
    energy = energy - 1
```

Salida:

```text
5 3
4 2
3 1
```

La siguiente evaluación falla porque `energy > 0` se vuelve falso.

Cuando participen varias variables, revisa cómo cambia cada una y qué parte de la condición puede terminar el bucle.

## 25. Las colecciones pueden formar parte del estado del bucle

El estado no se limita a números.

Una colección mutable puede cambiar de forma que afecte una condición `while`:

```python
tasks = ["review", "practice", "recap"]

while tasks:
    current = tasks.pop()
    print(current)
```

Salida:

```text
recap
practice
review
```

La lista se hace más corta después de cada `pop()`. Cuando queda vacía, es falsa y el bucle termina.

Esto es válido, pero la iteración directa con `for` suele ser más clara cuando el objetivo es únicamente leer cada elemento sin consumir ni modificar la colección.

## 26. La mutación puede ser la actualización del estado

En el ejemplo anterior no hay contador numérico.

La actualización relevante es:

```python
current = tasks.pop()
```

`pop()` modifica `tasks`, y esa mutación cambia el valor de verdad evaluado por `while tasks:`.

La regla más amplia es:

**Encuentra el estado utilizado por la condición y después encuentra qué cambia ese estado.**

## 27. Las condiciones explícitas pueden facilitar la auditoría de la intención

Python permite usar directamente valores verdaderos y falsos:

```python
while tasks:
    ...
```

A veces, una condición explícita comunica la regla con mayor precisión:

```python
while remaining_attempts > 0:
    ...
```

Ningún estilo es obligatorio en todos los casos. Elige la forma que haga más fácil entender la regla de parada.

## 28. Adelanto: qué significa `while True`

Esta sintaxis es Python válido:

```python
while True:
    statement
```

Como la condición literal `True` nunca se vuelve falsa por sí sola, la propia condición no proporciona un punto normal de parada.

Los programas reales suelen combinar `while True` con otro mecanismo de control de flujo que sale del bucle cuando se cumple una condición.

Ese mecanismo se aplaza deliberadamente hasta el próximo capítulo, donde `break`, `continue` y `else` de bucle se enseñan juntos.

## 29. Por qué este capítulo no usa `while True` en los ejemplos seguros

Un bucle `while True` aislado es intencionalmente ilimitado salvo que otro mecanismo lo termine.

Los ejemplos ejecutables seguros del repositorio deben finalizar de forma determinística, así que este capítulo no registra un ejemplo ilimitado con `while True`.

Por ahora, recuerda solamente el significado:

```text
while True -> seguir repitiendo porque la propia condición del bucle nunca se vuelve falsa
```

El próximo capítulo muestra cómo interactúan las instrucciones explícitas de control de bucle con este patrón.

## 30. `break`, `continue` y `else` de bucle vienen después

La sintaxis completa de los bucles de Python incluye recursos de control de flujo que pueden cambiar o interpretar la finalización normal.

No son prerrequisitos para comprender bucles `while` normales guiados por condición.

Por eso, este capítulo mantiene el modelo deliberadamente simple:

```text
condición verdadera -> ejecutar cuerpo
actualizar estado    -> evaluar otra vez
condición falsa      -> el bucle termina
```

El Capítulo 07 añade los caminos adicionales de control.

## 31. Una auditoría práctica de finalización

Antes de ejecutar un nuevo bucle `while`, responde cuatro preguntas:

1. ¿Cuál es el estado inicial?
2. ¿Qué condición exacta controla la repetición?
3. ¿Qué cambia el estado utilizado por esa condición?
4. ¿Por qué ese cambio puede hacer falsa la condición eventualmente?

Si la cuarta respuesta no está clara, inspecciona cuidadosamente el bucle antes de ejecutarlo.

Esta pequeña auditoría detecta muchos bucles infinitos accidentales.

## 32. Errores comunes

### Error 1: olvidar los dos puntos

Incorrecto:

```python
while remaining > 0
    print(remaining)
```

El encabezado de `while` debe terminar con `:`.

### Error 2: indentación incorrecta

Las instrucciones repetidas deben estar indentadas bajo el encabezado `while`.

### Error 3: olvidar la actualización del estado

Si la condición permanece verdadera y nada relevante cambia, el bucle puede no terminar nunca.

### Error 4: actualizar en la dirección equivocada

Una actualización que aleja el estado de la condición de parada también puede crear un bucle infinito.

### Error 5: asumir que el cuerpo siempre se ejecuta una vez

La condición se evalúa primero, por lo que son posibles cero iteraciones.

### Error 6: usar `while` para recorrer directamente una colección

Cuando la tarea es simplemente “para cada elemento”, la iteración directa con `for` suele ser más clara.

### Error 7: asumir que un límite debe alcanzarse exactamente

Un bucle termina cuando su condición se vuelve falsa. El estado puede cruzar un límite numérico sin ser nunca igual a él.

## 33. Ejemplo trabajado: `countdown_state.py`

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

Salida:

```text
3
2
1
Start
```

Ejemplo en el repositorio: [`examples/countdown_state.py`](examples/countdown_state.py)

## 34. Ejemplo trabajado: `study_target.py`

```python
studied_minutes = 0
session_minutes = 20
target_minutes = 60

while studied_minutes < target_minutes:
    studied_minutes = studied_minutes + session_minutes
    print(f"Study total: {studied_minutes} min")
```

Salida:

```text
Study total: 20 min
Study total: 40 min
Study total: 60 min
```

Ejemplo en el repositorio: [`examples/study_target.py`](examples/study_target.py)

## 35. Ejemplo trabajado: `doubling_until_limit.py`

```python
value = 1
limit = 20

while value < limit:
    print(value)
    value = value * 2

print(f"Stopped at {value}")
```

Salida:

```text
1
2
4
8
16
Stopped at 32
```

Ejemplo en el repositorio: [`examples/doubling_until_limit.py`](examples/doubling_until_limit.py)

## 36. Ejercicio

Crea un pequeño rastreador de progreso con este estado inicial:

```python
completed = 0
target = 4
```

Tu programa debe:

1. usar un bucle `while` cuya condición compare `completed` con `target`;
2. imprimir el siguiente paso completado en cada iteración;
3. actualizar `completed` para que el bucle avance hacia la finalización;
4. después del bucle, imprimir `Target reached`.

Salida esperada:

```text
Completed: 1
Completed: 2
Completed: 3
Completed: 4
Target reached
```

Después responde, sin ejecutar el programa:

- ¿Cuál es el estado inicial?
- ¿Qué expresión se vuelve a evaluar antes de cada iteración?
- ¿Qué instrucción cambia el estado del bucle?
- ¿Qué valor hace falsa la condición?
- ¿Se ejecutaría el cuerpo si `completed` comenzara en `4`?

No uses `break`, `continue`, `else` de bucle ni `while True` en este ejercicio.

## 37. Lista de comprobación

Antes de continuar, confirma que puedes explicar cada afirmación sin ejecutar el código:

- [ ] `while` repite un bloque mientras su condición sea verdadera.
- [ ] la condición se evalúa antes de cada iteración.
- [ ] el cuerpo puede ejecutarse cero veces.
- [ ] el estado del bucle es información que afecta si la repetición continúa.
- [ ] un bucle finito guiado por condición necesita un camino que haga falsa su condición.
- [ ] el estado puede aumentar, disminuir, multiplicarse, acumularse o mutar de otras formas deliberadas.
- [ ] un estado numérico no tiene que igualar exactamente un límite para que el bucle termine.
- [ ] olvidar una actualización puede crear un bucle infinito.
- [ ] actualizar en la dirección equivocada también puede impedir la finalización.
- [ ] `for` suele ser más claro para recorrer directamente un iterable.
- [ ] `while` es útil cuando la continuación depende naturalmente del estado actual.
- [ ] varias variables pueden participar en la condición.
- [ ] una colección mutable puede formar parte del estado cambiante.
- [ ] `while True` tiene una condición que nunca se vuelve falsa por sí sola.
- [ ] `break`, `continue` y `else` de bucle se aplazan deliberadamente al Capítulo 07.

## 38. Referencia rápida

| Necesidad | Forma típica |
|---|---|
| Repetir mientras una comparación sea verdadera | `while value < limit:` |
| Contar hacia arriba hasta un límite | inicializar, evaluar, incrementar |
| Contar hacia abajo hasta un límite | inicializar, evaluar, decrementar |
| Acumular hasta una meta | actualizar acumulador dentro de `while accumulator < target:` |
| Repetir mientras una colección no esté vacía | `while collection:` cuando consumir/modificar sea intencional |
| Recorrer cada elemento de un iterable | normalmente `for item in iterable` |
| Auditar la finalización | identificar estado inicial, condición, actualización y camino hacia falso |
| Adelanto de condición ilimitada | `while True:`; el control de bucles viene en el próximo capítulo |

Recuerda la progresión:

**estado inicial → condición → cuerpo → actualización del estado → condición otra vez → finalización**

## Próximo paso

El próximo capítulo es **`break`, `continue` y `else` de Bucles**.

Ahora conoces el ciclo de vida normal de un bucle `while` guiado por condición. A continuación, la guía añade instrucciones que pueden salir de un bucle antes de su finalización normal, saltar directamente a su siguiente iteración y distinguir la finalización normal de la terminación mediante `break`.

## Referencias oficiales

- [Referencia de Python 3.13: la instrucción `while`](https://docs.python.org/3.13/reference/compound_stmts.html#the-while-statement)
- [Tipos incorporados de Python 3.13: pruebas de valor de verdad](https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing)
- [Tutorial de Python 3.13: primeros pasos hacia la programación](https://docs.python.org/3.13/tutorial/introduction.html#first-steps-towards-programming)
