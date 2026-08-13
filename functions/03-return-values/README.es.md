<div align="center">

# Valores de Retorno

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Anterior: Parámetros y Argumentos](../02-parameters-and-arguments/README.es.md)

El Capítulo 01 dio nombre al comportamiento. El Capítulo 02 permitió que quien llama enviara valores a ese comportamiento. Este capítulo completa el primer recorrido de ida y vuelta de los datos:

```text
caller → arguments → function → return value → caller
```

**Tiempo estimado de estudio:** 75–100 minutos.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- escribir `return expression`;
- explicar que `return` termina la llamada actual de la función;
- almacenar y reutilizar valores retornados;
- distinguir `print()` de `return`;
- usar valores retornados en expresiones y condiciones;
- retornar valores normales de Python, tuplas y `None`;
- usar distintos `return` en distintas ramas;
- distinguir `return` de `break`;
- seguir entrada, transformación, retorno y uso por parte del llamador.

## 1. Envía un valor de vuelta con `return`

```python
def double(number):
    return number * 2


result = double(6)
print(result)
```

Salida:

```text
12
```

Seguimiento:

```text
6 binds to number
→ number * 2 becomes 12
→ return sends 12 back
→ double(6) becomes 12
→ result receives 12
```

Una función no asigna directamente a una variable del llamador. Retorna un valor, y quien llama decide qué ocurre después.

## 2. Una llamada que retorna valor es una expresión

```python
def square(number):
    return number * number


answer = square(5)
print(answer)
```

Salida:

```text
25
```

Piensa:

```text
square(5) → 25
```

Como la llamada produce un valor, puede participar en otra expresión:

```python
def double(number):
    return number * 2


final_score = double(7) + 3
print(final_score)
```

Salida:

```text
17
```

## 3. `print()` y `return` son diferentes

```python
def show_total(price, quantity):
    print(price * quantity)


def calculate_total(price, quantity):
    return price * quantity
```

La primera función muestra un valor. La segunda envía un valor al llamador.

```text
print(...) → display something
return ... → send a value to the caller
```

Al retornar el resultado, la función puede reutilizarse y el llamador decide qué hacer con ese valor: mostrarlo, compararlo, guardarlo o combinarlo.

## 4. Guarda o usa directamente un valor retornado

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(8, 3)
print(total)
print(calculate_total(5, 4))
```

Salida:

```text
24
20
```

## 5. Las funciones pueden retornar valores normales de Python

```python
def get_status():
    return "ready"


def is_passing(score):
    return score >= 60


def get_topics():
    return ["strings", "loops", "functions"]
```

Un valor de retorno puede ser una string, un número, un booleano, una colección, una tupla, `None` u otro valor normal de Python.

## 6. Los booleanos retornados funcionan con condiciones

```python
def is_passing(score):
    return score >= 60


if is_passing(75):
    print("Passed")
```

Salida:

```text
Passed
```

`is_passing(75)` se evalúa como `True`, así que las reglas de booleanos e `if` aprendidas antes siguen aplicando.

## 7. `return` termina la llamada actual de la función

```python
def get_message():
    return "Ready"
    print("This line never runs")
```

Cuando se ejecuta `return`:

```text
evaluate expression
→ obtain value
→ leave function
→ continue at caller
```

El trabajo necesario no debe aparecer después de un `return` incondicional en el mismo camino.

## 8. Ramas distintas pueden retornar valores distintos

```python
def classify_score(score):
    if score >= 90:
        return "excellent"

    if score >= 60:
        return "passing"

    return "needs review"
```

Llamadas:

```python
print(classify_score(95))
print(classify_score(72))
print(classify_score(40))
```

Salida:

```text
excellent
passing
needs review
```

Solo un `return` se ejecuta en cada llamada. Cuando uno de ellos se ejecuta, esa llamada termina.

## 9. Los retornos anticipados pueden simplificar un caso especial

```python
def describe_quantity(quantity):
    if quantity <= 0:
        return "invalid quantity"

    return "quantity accepted"
```

El caso especial sale primero y deja claro el camino normal.

## 10. `return` dentro de un bucle termina toda la función

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None
```

```python
print(find_first_even([3, 7, 8, 10]))
```

Salida:

```text
8
```

`return number` termina la función, no solo el bucle.

## 11. `return` y `break` abandonan límites distintos

```text
break  → leave the current loop
return → leave the current function call
```

`break` puede continuar con instrucciones posteriores en la misma función. `return` devuelve el control al llamador.

## 12. Llegar al final retorna `None`

```python
def show_ready():
    print("Ready")


result = show_ready()
print(result)
```

Salida:

```text
Ready
None
```

Si la ejecución llega al final sin un `return` explícito, el resultado de la llamada es `None`.

## 13. `return` sin expresión y `return None`

```python
def show_if_nonnegative(number):
    if number < 0:
        return

    print(number)
```

`return` sin expresión termina inmediatamente y produce `None`.

Todas estas formas pueden producir `None`:

```text
reach end of function → None
bare return           → None
return None           → None
```

Un `return None` explícito puede comunicar intención:

```python
def find_positive(numbers):
    for number in numbers:
        if number > 0:
            return number

    return None
```

Aquí `None` significa que no se encontró ningún valor positivo.

## 14. `None` y `False` son valores diferentes

```python
def is_empty(items):
    return len(items) == 0
```

Esta función retorna un booleano. Una función de búsqueda puede retornar `None` para significar “no encontrado”.

Ambos son falsy, pero no significan lo mismo. Cuando la distinción importe, comprueba deliberadamente cuál valor recibiste, por ejemplo comparando el resultado con `None`.

## 15. La expresión de retorno se evalúa primero

```python
def calculate_area(width, height):
    return width * height
```

Para `calculate_area(4, 6)`:

```text
evaluate width * height
→ obtain 24
→ return 24
→ leave function
```

El valor resultante se convierte en el valor de la expresión de llamada.

## 16. Retornando una colección

```python
def get_even_numbers(numbers):
    evens = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)

    return evens
```

```python
result = get_even_numbers([1, 2, 3, 4, 5, 6])
print(result)
```

Salida:

```text
[2, 4, 6]
```

## 17. Expresiones separadas por comas en `return` producen una tupla

```python
def get_dimensions():
    return 1920, 1080


dimensions = get_dimensions()
print(dimensions)
```

Salida:

```text
(1920, 1080)
```

La función retorna una sola tupla. Como el desempaquetado de tuplas ya es conocido:

```python
width, height = get_dimensions()

print(width)
print(height)
```

Salida:

```text
1920
1080
```

Se retorna una sola tupla.

## 18. Error común: imprimir en lugar de retornar

```python
def calculate_total(price, quantity):
    print(price * quantity)


total = calculate_total(8, 3)
print(total)
```

Salida:

```text
24
None
```

La función mostró `24`, pero el resultado de la llamada es `None`.

Corrección:

```python
def calculate_total(price, quantity):
    return price * quantity
```

## 19. Error común: retornar demasiado pronto en un bucle

Incorrecto para contar todos los números pares:

```python
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

        return count
```

La función termina en la primera iteración.

Correcto:

```python
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count
```

## 20. Error común: un `None` implícito accidental

```python
def get_level(score):
    if score >= 90:
        return "high"

    if score >= 60:
        return "medium"
```

Las puntuaciones menores que `60` retornan `None` implícitamente.

Si cada puntuación debe tener una categoría:

```python
def get_level(score):
    if score >= 90:
        return "high"

    if score >= 60:
        return "medium"

    return "low"
```

## 21. Sigue el recorrido completo de ida y vuelta

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(12, 4)
```

```text
caller has 12 and 4
↓
arguments bind to price and quantity
↓
function evaluates price * quantity
↓
result is 48
↓
return sends 48 back
↓
call expression becomes 48
↓
total receives 48
```

Este es el modelo central del capítulo.

## 22. Ejemplos ejecutables

### Calcular un total

Archivo: [`examples/calculate_total.py`](examples/calculate_total.py)

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(12, 4)

print(total)
print(total + 5)
```

Salida esperada:

```text
48
53
```

### Retornar por rama

Archivo: [`examples/classify_score.py`](examples/classify_score.py)

```python
def classify_score(score):
    if score >= 90:
        return "excellent"

    if score >= 60:
        return "passing"

    return "needs review"


print(classify_score(95))
print(classify_score(72))
print(classify_score(40))
```

Salida esperada:

```text
excellent
passing
needs review
```

### Búsqueda con `None`

Archivo: [`examples/find_first_even.py`](examples/find_first_even.py)

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


print(find_first_even([3, 7, 8, 10]))
print(find_first_even([1, 3, 5]))
```

Salida esperada:

```text
8
None
```

## 23. Ejercicio: categoría de temperatura

Crea `classify_temperature(temperature)`.

Requisitos:

1. retorna `"hot"` para valores de al menos `30`;
2. retorna `"mild"` para valores de al menos `18` pero menores que `30`;
3. retorna `"cold"` en los demás casos;
4. llama con `34`, `22` y `10`;
5. guarda cada resultado antes de imprimirlo.

Salida esperada:

```text
hot
mild
cold
```

No uses type hints, valores predeterminados, `*args` ni `**kwargs`.

## 24. Lista de revisión

Antes de continuar, confirma que puedes:

- [ ] escribir `return expression`;
- [ ] explicar que la expresión se evalúa antes de que termine la función;
- [ ] guardar y reutilizar valores retornados;
- [ ] usar un booleano retornado en `if`;
- [ ] distinguir `print()` de `return`;
- [ ] usar distintos retornos en distintas ramas;
- [ ] distinguir `return` de `break`;
- [ ] explicar `None` implícito, `return` sin expresión y `return None`;
- [ ] explicar que `return a, b` retorna una sola tupla;
- [ ] reconocer un `return` colocado demasiado pronto en un bucle;
- [ ] seguir valores desde los argumentos de vuelta al llamador.

## 25. Referencia rápida

| Necesidad | Forma | Significado |
|---|---|---|
| retornar valor | `return expression` | evaluar, salir de la función y enviar valor al llamador |
| guardar resultado | `result = function()` | asociar valor retornado en el llamador |
| usar resultado | `print(function())` | usar valor retornado en otra llamada |
| retornar booleano | `return condition` | llamador recibe `True` o `False` |
| retornar `None` | `return` / `return None` | salir de la función con `None` |
| `None` implícito | llegar al final | resultado de la llamada es `None` |
| retornar tupla | `return a, b` | retornar una sola tupla |
| detener bucle | `break` | salir del bucle actual |
| detener función | `return value` | terminar la llamada actual de la función |

## 26. Límite de alcance

Este capítulo pospone intencionalmente:

- reglas de alcance local/global;
- type hints y anotaciones de retorno;
- valores predeterminados;
- `*args` y `**kwargs`;
- sintaxis positional-only y keyword-only;
- desempaquetado de argumentos;
- funciones anidadas y lambdas;
- decoradores, generadores, `yield` y recursión;
- manejo de excepciones;
- diseño avanzado de propiedad y mutación.

## 27. Qué viene después

Ahora puedes seguir:

```text
caller → arguments → parameters → function body → return value → caller
```

La siguiente pregunta es:

> ¿Dónde existen los nombres dentro y fuera de una función, y cuándo son visibles?

Eso conduce al **Capítulo 04: Alcance**.

Vuelve a la [ruta de Funciones](../README.es.md) o a la [ruta completa de aprendizaje](../../docs/learning-path.es.md).

## Referencias

Documentación primaria de Python:

- [Tutorial de Python 3.13: Definir Funciones](https://docs.python.org/es/3.13/tutorial/controlflow.html#defining-functions)
- [Referencia del Lenguaje Python 3.13: La sentencia `return`](https://docs.python.org/es/3.13/reference/simple_stmts.html#the-return-statement)
