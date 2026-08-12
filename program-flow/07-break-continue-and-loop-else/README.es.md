<div align="center">

# `break`, `continue` y `else` de Bucles

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Flujo del Programa](../README.es.md) · [← Anterior: Bucles `while` y Repetición Guiada por Estado](../06-while-loops-and-state-driven-repetition/README.es.md)

Los bucles normalmente siguen su regla natural de repetición: un bucle `for` consume su iterable y un bucle `while` continúa mientras su condición siga siendo verdadera. A veces, sin embargo, un programa necesita **detenerse antes del final, saltar el resto de una iteración o distinguir la finalización normal de una salida anticipada**.

Este capítulo presenta las tres herramientas que Python ofrece para esas situaciones: `break`, `continue` y la cláusula opcional `else` de los bucles.

**Tiempo estimado de estudio:** 110–135 minutos.

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- explicar qué significa la finalización normal tanto en `for` como en `while`;
- usar `break` para terminar anticipadamente el bucle envolvente más cercano;
- reconocer que el código posterior a `break` en la misma iteración no se ejecuta;
- usar `continue` para saltar las instrucciones restantes de la iteración actual;
- explicar el siguiente paso diferente después de `continue` en `for` y `while`;
- actualizar de forma segura el estado de un `while` cuando `continue` sea posible;
- usar `while True` deliberadamente cuando `break` exprese con mayor claridad la regla real de parada;
- explicar que el `else` de un bucle pertenece al bucle, no a un `if` interno;
- predecir cuándo se ejecuta el `else` del bucle y cuándo un `break` lo impide;
- usar `for ... else` en búsquedas donde `break` significa que se encontró una coincidencia;
- usar `while ... else` cuando la finalización normal de la condición tenga un camino de cierre significativo;
- reconocer que un `for` vacío y una condición inicialmente falsa en `while` todavía pueden alcanzar el `else` del bucle;
- explicar que `break` afecta solo al bucle envolvente más cercano en bucles anidados;
- elegir entre `break`, `continue`, `else` de bucle y condiciones normales según la intención;
- evitar saltos innecesarios de control que dificulten la lectura del bucle.

## 1. Empieza por la finalización normal del bucle

Antes de cambiar un bucle, define qué ocurriría sin ninguna instrucción especial de control.

Un bucle `for` normalmente termina cuando su iterador se agota:

```python
for number in [1, 2, 3]:
    print(number)
```

Un bucle `while` normalmente termina cuando su condición se vuelve falsa:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

`break`, `continue` y el `else` del bucle solo tienen sentido cuando primero entiendes ese camino normal.

## 2. Qué hace `break`

`break` termina inmediatamente el bucle `for` o `while` envolvente más cercano.

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

Salida:

```text
1
2
```

Cuando `number` pasa a ser `3`, el bucle termina antes de que `print(number)` pueda ejecutarse en esa iteración.

## 3. `break` sale del bucle, no solo del `if`

Considera:

```python
for item in ["pen", "book", "mug"]:
    if item == "book":
        break
    print(item)

print("Done")
```

Salida:

```text
pen
Done
```

El `if` decide si se ejecuta `break`. El propio `break` transfiere el control fuera del bucle.

## 4. El código después de `break` en el mismo cuerpo del bucle se omite

Este código nunca imprime `"After break"`:

```python
for number in [1, 2, 3]:
    if number == 2:
        break
        print("After break")
```

En cuanto `break` se ejecuta, el control abandona inmediatamente el bucle.

Las instrucciones inalcanzables después de un `break` incondicional no deben permanecer en código real.

## 5. `break` es útil cuando la respuesta ya se conoce

Supón que estás buscando un único objetivo:

```python
codes = ["PEN", "BOOK", "MUG", "CABLE"]
target = "MUG"

for code in codes:
    if code == target:
        print("Found")
        break
```

Después de encontrar el objetivo, examinar elementos posteriores no cambiaría la respuesta.

## 6. Una búsqueda puede detenerse en la primera coincidencia

Si puede haber duplicados pero solo importa la primera coincidencia, `break` comunica esa política directamente:

```python
values = [4, 7, 7, 9]

for value in values:
    if value == 7:
        print("First match found")
        break
```

El segundo `7` nunca es examinado por el cuerpo del bucle.

## 7. No uses `break` cuando todos los elementos deban procesarse

Esto no encaja bien si la tarea debe examinar todos los valores:

```python
scores = [82, 47, 91, 58]
```

Si necesitas clasificar cada puntuación, terminar el bucle en el primer valor reprobado perdería información.

La instrucción de control debe corresponder al requisito real, no limitarse a acortar el código.

## 8. `break` también funciona en `while`

```python
count = 1

while count <= 10:
    print(count)
    if count == 3:
        break
    count += 1
```

Salida:

```text
1
2
3
```

La condición original del `while` todavía podría ser verdadera, pero `break` termina el bucle de todos modos.

## 9. `while True` puede expresar un bucle sin límite definido en la cabecera

Un bucle cuya regla natural de parada aparece dentro del cuerpo puede escribirse así:

```python
while True:
    command = input("Command: ")

    if command == "quit":
        break

    print(command)
```

`True` mantiene el bucle apto para repetirse. La regla significativa de terminación es el `break` activado por `"quit"`.

Esto no es automáticamente mejor que colocar una condición en la cabecera de `while`. Úsalo cuando la condición interna de parada sea realmente más clara.

## 10. `while True` necesita una ruta de salida creíble

Este bucle no tiene ninguna ruta visible de terminación:

```python
while True:
    print("Running")
```

Eso puede ser intencional en programas especializados, pero en código de aplicación para principiantes debería hacerte preguntar:

**¿Qué evento o cambio de estado detendrá este bucle?**

Si no hay respuesta, quizá hayas creado un bucle infinito accidental.

## 11. Qué hace `continue`

`continue` omite el resto de la ejecución actual del cuerpo del bucle e inicia el siguiente ciclo del bucle envolvente más cercano.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Salida:

```text
1
2
4
5
```

El bucle continúa. Solo se omite el resto de la iteración correspondiente a `3`.

## 12. `continue` no es `break`

Compara las intenciones:

```text
break    -> stop this loop
continue -> skip the rest of this iteration and keep looping
```

Confundirlos cambia por completo la forma del flujo de control.

## 13. `continue` es útil para filtrar dentro de un bucle

```python
scores = [82, 47, 91, 58, 76]

for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

Salida:

```text
Passing score: 82
Passing score: 91
Passing score: 76
```

Las puntuaciones reprobadas se omiten, mientras que los valores restantes todavía llegan a la acción principal.

## 14. `continue` puede reducir el anidamiento

Sin `continue`:

```python
for score in scores:
    if score >= 60:
        print(f"Passing score: {score}")
```

Con `continue`:

```python
for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

Ambas formas pueden ser claras. La segunda suele ser útil cuando varias verificaciones iniciales descartan un elemento antes de un camino principal más largo.

Es una elección de legibilidad, no una regla que diga que `continue` siempre es superior.

## 15. En un bucle `for`, `continue` avanza hacia el siguiente elemento

```python
for letter in "ABC":
    if letter == "B":
        continue
    print(letter)
```

Salida:

```text
A
C
```

Después de omitir el resto de la iteración de `B`, el bucle `for` solicita el siguiente elemento a su iterador.

## 16. En un bucle `while`, `continue` vuelve a probar la condición

```python
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

Salida:

```text
1
2
4
5
```

Después de `continue`, Python vuelve a la condición del `while` antes de otra ejecución del cuerpo.

## 17. Actualiza el estado de `while` antes de un posible `continue`

Este patrón es peligroso:

```python
number = 0

while number < 5:
    if number == 2:
        continue
    number += 1
```

Cuando `number` llega a `2`, `continue` se ejecuta antes de la actualización. La condición sigue siendo verdadera y `number` permanece en `2`, por lo que el bucle se repite para siempre.

Una pregunta útil de revisión es:

**¿Puede cada ruta por este cuerpo de `while` seguir avanzando hacia la terminación?**

## 18. Las condiciones a veces son más claras que `continue`

No añadas un salto solo porque Python lo ofrece.

```python
for number in range(1, 6):
    if number != 3:
        print(number)
```

puede ser perfectamente legible frente a:

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Elige la forma que comunique con mayor claridad el camino principal del bucle.

## 19. Qué es el `else` de un bucle

Tanto `for` como `while` pueden tener una cláusula opcional `else`.

Para un bucle `for`:

```python
for item in iterable:
    statement
else:
    normal_completion_statement
```

Para un bucle `while`:

```python
while condition:
    statement
else:
    normal_completion_statement
```

La regla principal no es “la condición se volvió falsa”. La regla general es:

**El `else` del bucle se ejecuta cuando ese bucle termina sin ejecutar un `break`.**

## 20. `for ... else` después del agotamiento normal

```python
for number in [1, 2, 3]:
    print(number)
else:
    print("Finished normally")
```

Salida:

```text
1
2
3
Finished normally
```

El iterable se agotó y no ocurrió ningún `break`, por lo que se ejecuta el bloque `else`.

## 21. `break` impide el `else` del bucle

```python
for number in [1, 2, 3]:
    if number == 2:
        break
else:
    print("Finished normally")
```

No hay salida del `else` porque `break` terminó ese bucle.

## 22. `continue` no impide el `else` del bucle

```python
for number in [1, 2, 3]:
    if number == 2:
        continue
    print(number)
else:
    print("Finished without break")
```

Salida:

```text
1
3
Finished without break
```

`continue` cambia una iteración, no la categoría final de terminación del bucle.

## 23. El `else` del bucle pertenece al bucle

Observa con atención la indentación:

```python
for name in names:
    if name == target:
        print("Found")
        break
else:
    print("Not found")
```

El `else` está alineado con `for`, no con `if`.

Esa relación visual es esencial para leer correctamente esta sintaxis.

## 24. La búsqueda es el caso clásico de `for ... else`

```python
names = ["Ari", "Mina", "Leo"]
target = "Nora"

for name in names:
    if name == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} was not found")
```

Salida:

```text
Nora was not found
```

El significado es compacto:

```text
match found -> break -> skip else
no match     -> no break -> run else
```

## 25. El `else` del bucle puede reemplazar una bandera manual

Una búsqueda basada en una bandera puede funcionar:

```python
found = False

for name in names:
    if name == target:
        found = True
        break

if not found:
    print("Not found")
```

La forma con `else` del bucle representa directamente el mismo hecho de control:

```python
for name in names:
    if name == target:
        break
else:
    print("Not found")
```

Usa la versión que tus lectores puedan comprender de forma fiable. El `else` de bucle es una característica real de Python, pero puede resultar poco familiar para algunos equipos.

## 26. Un `for` vacío todavía puede ejecutar `else`

```python
for item in []:
    print(item)
else:
    print("No break occurred")
```

Salida:

```text
No break occurred
```

El cuerpo del bucle se ejecutó cero veces, pero el bucle terminó sin `break`.

## 27. `while ... else` se ejecuta después de que la condición se vuelve falsa

```python
count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Condition became false")
```

Salida:

```text
1
2
3
Condition became false
```

Esa es la finalización normal de ese bucle `while`.

## 28. `break` también impide `while ... else`

```python
count = 1

while count <= 5:
    if count == 3:
        break
    count += 1
else:
    print("Condition became false")
```

El bloque `else` no se ejecuta porque `break` terminó el bucle primero.

## 29. Un `while` inicialmente falso todavía puede ejecutar `else`

```python
count = 5

while count < 3:
    print(count)
else:
    print("Loop completed without break")
```

Salida:

```text
Loop completed without break
```

El cuerpo se ejecutó cero veces, pero no ocurrió ningún `break`.

## 30. Piensa “sin break”, no “algo falló”

A veces el `else` de bucle se describe informalmente como un bloque de “no encontrado”, porque las búsquedas son un caso de uso común.

Esa descripción es demasiado limitada.

El hecho real de control es:

```text
loop ended without break -> else runs
loop ended through break -> else is skipped
```

El significado de “éxito”, “fallo”, “encontrado” o “no encontrado” proviene de tu programa, no de Python en sí.

## 31. `break` afecta solo al bucle envolvente más cercano

```python
rows = [[1, 2], [3, 4]]

for row in rows:
    for value in row:
        if value == 2:
            break
        print(value)
```

Salida:

```text
1
3
4
```

El `break` termina solo el bucle interno. El bucle externo continúa con la siguiente fila.

## 32. `continue` también apunta al bucle envolvente más cercano

En bucles anidados, `continue` avanza el bucle más cercano que lo contiene sintácticamente.

Eso puede resultar difícil de leer si varios niveles anidados contienen saltos de control.

Cuando aumenta el anidamiento, prefiere hacer explícito el flujo en lugar de apilar muchos `break` y `continue`.

## 33. El `else` pertenece a un bucle específico

Los bucles anidados pueden tener cada uno su propio `else`, pero la indentación determina qué bucle posee cada cláusula.

Para principiantes, evita combinaciones densas hasta que la forma simple esté completamente clara.

Un bucle, un objetivo de búsqueda y un `else` significativo suelen ser más fáciles de estudiar.

## 34. Error común: esperar que `break` salga de varios bucles

Esto no termina ambos bucles:

```python
for row in rows:
    for value in row:
        if value == target:
            break
```

Solo termina el bucle interno.

Fases posteriores presentan funciones, que a menudo ofrecen formas más claras de organizar búsquedas grandes sin un control complicado de bucles anidados.

## 35. Error común: colocar actualizaciones importantes de estado después de `continue`

```python
while condition:
    if skip_this_cycle:
        continue
    update_state()
```

Si `update_state()` es necesaria para la terminación, la ruta omitida puede no avanzar nunca.

Al revisar un bucle `while`, recorre mentalmente cada rama que pueda llegar a `continue`.

## 36. Error común: leer el `else` de bucle como `if ... else`

Esta indentación:

```python
for item in items:
    if condition:
        break
else:
    statement
```

significa que el `else` pertenece a `for`.

Mover el `else` debajo del `if` crearía un programa diferente con otro comportamiento.

## 37. Error común: usar `else` de bucle cuando basta una instrucción normal

Si un código debe ejecutarse siempre después de un bucle, haya ocurrido `break` o no, colócalo después del bucle:

```python
for item in items:
    if should_stop:
        break

print("Cleanup message")
```

No uses `else` de bucle para trabajo posterior incondicional, porque `break` haría que se omita.

## 38. Error común: abusar de `break` y `continue`

Un bucle con muchos saltos de control puede convertirse en un laberinto:

```text
condition -> continue
condition -> break
condition -> continue
condition -> nested break
```

Estas instrucciones son útiles porque son precisas, no porque usar más haga mejor el código.

Prefiere una cantidad pequeña de salidas y saltos claramente motivados.

## 39. Ejemplo completo: `break_search.py`

```python
codes = ["PEN", "BOOK", "MUG", "CABLE"]
target = "MUG"

for code in codes:
    print(f"Checking {code}")
    if code == target:
        print(f"Found {target}")
        break
```

Salida:

```text
Checking PEN
Checking BOOK
Checking MUG
Found MUG
```

Ejemplo del repositorio: [`examples/break_search.py`](examples/break_search.py)

## 40. Ejemplo completo: `continue_filtering.py`

```python
scores = [82, 47, 91, 58, 76]

for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

Salida:

```text
Passing score: 82
Passing score: 91
Passing score: 76
```

Ejemplo del repositorio: [`examples/continue_filtering.py`](examples/continue_filtering.py)

## 41. Ejemplo completo: `loop_else_search.py`

```python
names = ["Ari", "Mina", "Leo"]
target = "Nora"

for name in names:
    if name == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} was not found")
```

Salida:

```text
Nora was not found
```

Ejemplo del repositorio: [`examples/loop_else_search.py`](examples/loop_else_search.py)

## 42. Ejercicio

Crea una lista de códigos ficticios de tareas:

```python
task_codes = ["A10", "B20", "SKIP", "C30", "STOP", "D40"]
```

Escribe un bucle que:

1. use `continue` cuando el valor sea `"SKIP"`;
2. use `break` cuando el valor sea `"STOP"`;
3. imprima todos los demás códigos alcanzados;
4. añada un `else` de bucle que imprima `"All tasks processed"` solo si el bucle termina sin `break`.

Con la lista anterior, la salida esperada es:

```text
A10
B20
C30
```

Después elimina `"STOP"` de la lista y predice qué cambia antes de ejecutar el programa.

## 43. Lista de revisión

Antes de avanzar, confirma que puedes explicar cada afirmación sin ejecutar el código:

- [ ] `break` termina el bucle `for` o `while` envolvente más cercano.
- [ ] las instrucciones posteriores de la misma iteración se omiten después de `break`.
- [ ] `continue` omite el resto de la iteración actual sin terminar el bucle.
- [ ] en `for`, `continue` avanza hacia el siguiente elemento.
- [ ] en `while`, `continue` vuelve a la prueba de la condición.
- [ ] un bucle `while` todavía debe actualizar el estado relevante en las rutas que pueden alcanzar `continue`.
- [ ] `while True` es apropiado cuando un `break` interno expresa claramente la regla real de parada.
- [ ] el `else` de bucle se alinea con el bucle y pertenece a él.
- [ ] el `else` de bucle se ejecuta cuando ese bucle termina sin `break`.
- [ ] `break` impide el `else` asociado al bucle.
- [ ] `continue` por sí solo no impide el `else` del bucle.
- [ ] un `for` vacío todavía puede ejecutar su `else`.
- [ ] un `while` inicialmente falso todavía puede ejecutar su `else`.
- [ ] en bucles anidados, `break` y `continue` afectan al bucle envolvente más cercano.
- [ ] las instrucciones de control del bucle deben aclarar la intención, no crear saltos innecesarios.

## 44. Referencia rápida

| Necesidad | Herramienta típica |
|---|---|
| Detener el bucle actual inmediatamente | `break` |
| Omitir el resto de una iteración | `continue` |
| Repetir indefinidamente hasta una regla interna de parada | `while True` + `break` |
| Ejecutar un bloque solo cuando ningún `break` terminó el bucle | `else` de bucle |
| Buscar hasta encontrar una coincidencia | `for` + condición + `break` |
| Tratar “no encontrado” después de una búsqueda completa | `for ... else` |
| Omitir elementos rechazados manteniendo los posteriores | `continue` |
| Ejecutar siempre código después de un bucle | instrucción normal después del bucle |

Recuerda la progresión:

**repetición normal → salida anticipada → omitir un ciclo → distinguir finalización normal de `break`**

## Siguiente paso

El próximo capítulo es **Elegir y Combinar el Flujo del Programa**.

Ahora ya conoces las principales herramientas de selección y repetición de la Fase 4: condiciones, `if`, `match`, `for`, ayudas de iteración, `while`, `break`, `continue` y `else` de bucle. El capítulo final de la fase se centrará en elegir entre ellas y combinarlas sin convertir el flujo de control en un laberinto.

## Referencias oficiales

- [Referencia del lenguaje Python 3.13: `break`](https://docs.python.org/3.13/reference/simple_stmts.html#the-break-statement)
- [Referencia del lenguaje Python 3.13: `continue`](https://docs.python.org/3.13/reference/simple_stmts.html#the-continue-statement)
- [Referencia del lenguaje Python 3.13: `while`](https://docs.python.org/3.13/reference/compound_stmts.html#the-while-statement)
- [Referencia del lenguaje Python 3.13: `for`](https://docs.python.org/3.13/reference/compound_stmts.html#the-for-statement)
- [Tutorial de Python 3.13: `break`, `continue` y `else` de bucles](https://docs.python.org/3.13/tutorial/controlflow.html#break-and-continue-statements)