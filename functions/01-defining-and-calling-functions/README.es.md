<div align="center">

# Definir y Llamar Funciones

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Fase anterior: Flujo del Programa](../../program-flow/README.es.md)

Las funciones dan un nombre significativo a comportamientos que un programa puede necesitar ejecutar más de una vez.

Este capítulo inicia la Fase 5 con una distinción:

```text
definition = describe and name behavior
call       = execute that behavior now
```

Los parámetros, argumentos, el diseño de valores de retorno y el alcance vienen después.

**Tiempo estimado de estudio:** 75–100 minutos.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar por qué existen las funciones;
- definir una función simple con `def`;
- identificar el nombre, la lista de parámetros vacía, los dos puntos y el cuerpo indentado;
- llamar una función después de que su definición se haya ejecutado;
- explicar que definir una función no ejecuta su cuerpo;
- seguir la ejecución dentro y fuera de una llamada;
- llamar la misma función más de una vez;
- distinguir `name` de `name()`;
- usar nombres significativos en `snake_case`;
- usar `pass` para un cuerpo intencionalmente vacío;
- colocar estructuras de flujo conocidas dentro de una función;
- reconocer que una función sin `return` explícito produce `None`.

## 1. Por qué existen las funciones

Un programa ya puede guardar valores, elegir ramas y repetir trabajo.

A medida que crece, grupos de instrucciones empiezan a representar tareas reconocibles:

```text
show a heading
show a menu
print a separator
display a status
```

Una función permite dar nombre a una de esas tareas.

El primer modelo mental es:

> **Las funciones dan nombre al comportamiento.**

Una buena función también puede reducir duplicación y hacer más fácil de leer el flujo del programa.

## 2. Define primero, llama después

```python
def show_welcome():
    print("Welcome to Python functions.")


show_welcome()
```

La definición es:

```python
def show_welcome():
    print("Welcome to Python functions.")
```

La llamada es:

```python
show_welcome()
```

Son operaciones diferentes.

## 3. Anatomía de `def`

```python
def show_welcome():
    print("Welcome to Python functions.")
```

| Parte | Significado |
|---|---|
| `def` | inicia una definición de función |
| `show_welcome` | nombre de la función |
| `()` | lista de parámetros, vacía en este capítulo |
| `:` | inicia el bloque de la función |
| instrucción indentada | cuerpo de la función |

Este capítulo mantiene `()` vacío a propósito. El Capítulo 02 añadirá parámetros y argumentos.

## 4. Una definición no ejecuta el cuerpo

Cuando Python ejecuta una instrucción `def`, crea la función y la vincula con el nombre de la función.

El cuerpo queda preparado para ejecutarse después.

Por eso esto no imprime nada:

```python
def show_welcome():
    print("Welcome")
```

El cuerpo se ejecuta solo después de una llamada:

```python
show_welcome()
```

Piensa:

```text
def       → prepare behavior
name()    → execute behavior
```

## 5. Una llamada redirige temporalmente la ejecución

```python
def show_step():
    print("Inside function")


print("Before call")
show_step()
print("After call")
```

Salida:

```text
Before call
Inside function
After call
```

Seguimiento:

1. Python define `show_step`.
2. La ejecución de nivel principal imprime `Before call`.
3. `show_step()` llama la función.
4. La ejecución entra en el cuerpo.
5. El cuerpo imprime `Inside function`.
6. El cuerpo termina.
7. La ejecución continúa después de la llamada.
8. Python imprime `After call`.

El llamador no desaparece. La ejecución vuelve al punto siguiente a la llamada.

## 6. Una definición, muchas llamadas

```python
def show_separator():
    print("---")


print("Start")
show_separator()
print("Study")
show_separator()
print("Finish")
```

Salida:

```text
Start
---
Study
---
Finish
```

La función se define una vez y se llama dos veces.

Esa es la reutilización básica:

```text
define once
call when needed
```

## 7. Reutilizar es más que copiar y pegar

El código repetido puede funcionar, pero una función añade significado.

Compara la idea:

```text
print("---")
```

con:

```text
show_separator()
```

La segunda forma explica *por qué* existe esa línea.

Cuando cambia el comportamiento, una única definición puede actualizar todos los lugares que llaman la función.

## 8. Los nombres deben describir acciones

Prefiere nombres como:

```text
show_status
print_summary
validate_choice
calculate_total
```

Los nombres normales de funciones en Python usan `snake_case`.

Evita nombres como:

```text
x
thing
func1
do_it
```

salvo que el contexto realmente los haga claros.

Una llamada debería leerse como una acción significativa.

## 9. `name` y `name()` son diferentes

```python
def show_message():
    print("Hello")


print(show_message)
show_message()
```

`show_message` se refiere al objeto función.

`show_message()` llama la función.

Todavía no necesitas dominar los objetos función. Guarda esta regla:

```text
name   → reference
name() → call
```

## 10. La indentación define el cuerpo

Válido:

```python
def show_message():
    print("Hello")
```

Inválido:

```python
def show_message():
print("Hello")
```

Una definición de función introduce un bloque indentado, igual que otras instrucciones compuestas que ya conoces.

El encabezado también necesita dos puntos:

```python
def show_message():
```

## 11. El flujo del programa puede vivir dentro de una función

```python
def show_even_numbers():
    for number in range(1, 6):
        if number % 2 == 0:
            print(number)


show_even_numbers()
```

Salida:

```text
2
4
```

`for` e `if` mantienen su significado normal.

La función simplemente da un nombre reutilizable a ese comportamiento combinado.

Esto conecta las fases:

```text
program flow → controls what happens
functions    → name a unit of behavior
```

## 12. Un cuerpo puede contener varias instrucciones

```python
def show_study_plan():
    print("Read")
    print("Practice")
    print("Review")


show_study_plan()
```

Salida:

```text
Read
Practice
Review
```

Cada instrucción correctamente indentada pertenece al cuerpo.

## 13. El orden de definición importa

En el nivel principal, este orden falla:

```python
show_welcome()


def show_welcome():
    print("Welcome")
```

Python llega a la llamada antes de ejecutar la definición que vincula `show_welcome`.

Usa:

```python
def show_welcome():
    print("Welcome")


show_welcome()
```

La regla precisa es:

> La definición debe haberse ejecutado antes de que ocurra la llamada.

Después de que existan los nombres, el orden de las llamadas aún puede ser diferente del orden de las definiciones.

## 14. `pass` puede marcar un cuerpo intencionalmente vacío

```python
def planned_step():
    pass


planned_step()
```

`pass` es una instrucción válida que no hace nada.

Es útil cuando el cuerpo debe existir estructuralmente pero el comportamiento real todavía no se ha escrito.

No añadas `pass` a un cuerpo que ya tenga instrucciones reales.

## 15. Una función sin `return` explícito produce `None`

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

Este capítulo todavía no enseña diseño de valores de retorno.

Por ahora, observa solo que llegar al final de una función sin `return` explícito completa la llamada y el resultado de la llamada es `None`.

El Capítulo 03 tratará los valores de retorno como tema completo.

## 16. Imprimir no es devolver

Esta función:

```python
def show_ready():
    print("Ready")
```

muestra una salida.

No envía explícitamente un valor útil de vuelta al llamador.

Mantén los conceptos separados:

```text
print(...) → display something
return ... → send a result to the caller
```

La segunda idea viene después.

## 17. Las funciones deben representar tareas significativas

Una función normalmente debería responder:

```text
What job does this function perform?
```

Por ejemplo:

```python
def show_menu():
    print("1. Study")
    print("2. Practice")
```

La responsabilidad es clara.

No crees funciones solo porque funciones sea el tema actual. Wrappers pequeños sin un propósito significativo pueden dificultar la lectura.

## 18. Las llamadas y los bucles pueden trabajar juntos

Un bucle puede controlar la repetición:

```python
def show_tick():
    print("Tick")


for repetition in range(3):
    show_tick()
```

O la función puede controlar la repetición:

```python
def show_three_ticks():
    for repetition in range(3):
        print("Tick")


show_three_ticks()
```

Ambos imprimen tres ticks, pero distribuyen la responsabilidad de forma diferente.

El objetivo descriptivo del bucle mantiene familiar el modelo de iteración. Su valor no es necesario en estos cuerpos concretos; el bucle solo necesita repetir tres veces.

Capítulos posteriores darán más control al llamador mediante parámetros.

## 19. Sigue la ejecución antes de depurar

Cuando una función te sorprenda, escribe el camino de ejecución:

```text
define function
run top-level code
call function
enter body
run body
leave body
continue after call
```

Este seguimiento simple encuentra muchos errores de principiante.

## 20. Errores comunes

### Definir y nunca llamar

```python
def show_message():
    print("Hello")
```

Sin llamada, el cuerpo no se ejecuta.

### Olvidar los paréntesis

```python
show_message
```

se refiere a la función. Usa `show_message()` para llamarla.

### Llamar antes de que la definición se ejecute

```python
show_message()


def show_message():
    print("Hello")
```

En el nivel principal, coloca la definición antes de la llamada.

### Romper la indentación

```python
def show_message():
print("Hello")
```

El cuerpo debe estar indentado.

### Añadir conceptos posteriores demasiado pronto

Tal vez ya hayas visto:

```python
def greet(name):
    print(f"Hello, {name}")
```

Eso es útil, pero ahora la función recibe datos.

Primero haz confiable este modelo:

```text
define
call
trace
reuse
```

Después, los parámetros serán mucho más fáciles.

## 21. Ejemplo ejecutable: definir y llamar

Archivo: [`examples/define_and_call.py`](examples/define_and_call.py)

```python
def show_welcome():
    print("Welcome to Python functions.")


show_welcome()
```

Salida esperada:

```text
Welcome to Python functions.
```

## 22. Ejemplo ejecutable: llamadas repetidas

Archivo: [`examples/repeated_calls.py`](examples/repeated_calls.py)

```python
def show_separator():
    print("---")


print("Start")
show_separator()
print("Study")
show_separator()
print("Finish")
```

Salida esperada:

```text
Start
---
Study
---
Finish
```

## 23. Ejemplo ejecutable: orden de ejecución

Archivo: [`examples/execution_order.py`](examples/execution_order.py)

```python
def show_step():
    print("Inside function")


print("Before call")
show_step()
print("After call")
```

Salida esperada:

```text
Before call
Inside function
After call
```

## 24. Ejercicio: banner de estudio reutilizable

Crea una función llamada `show_study_banner`.

Requisitos:

1. defínela con `def`;
2. mantén vacía la lista de parámetros;
3. imprime exactamente:

```text
==========
STUDY TIME
==========
```

4. imprime `Before`;
5. llama la función;
6. imprime `After`;
7. llama la misma función otra vez.

Salida esperada:

```text
Before
==========
STUDY TIME
==========
After
==========
STUDY TIME
==========
```

No uses parámetros ni `return` todavía.

## 25. Preguntas de revisión

- ¿Qué líneas definen comportamiento?
- ¿Qué líneas llaman comportamiento?
- ¿Cuántas veces se define la función?
- ¿Cuántas veces se llama?
- ¿Por qué el cuerpo se ejecuta dos veces?
- ¿Qué pasa si se eliminan las dos llamadas?
- ¿Qué cambia si escribes el nombre de la función sin paréntesis?
- ¿Qué instrucciones están en el nivel principal?
- ¿Qué instrucciones pertenecen al cuerpo?

## 26. Lista de revisión

Antes de continuar, confirma que puedes:

- [ ] explicar por qué existen las funciones;
- [ ] escribir `def name():`;
- [ ] indentar el cuerpo;
- [ ] distinguir definición de llamada;
- [ ] llamar una función con `name()`;
- [ ] distinguir `name` de `name()`;
- [ ] seguir la ejecución dentro y fuera de una llamada;
- [ ] llamar la misma función más de una vez;
- [ ] explicar por qué importa el orden de ejecución de la definición;
- [ ] elegir un nombre significativo en `snake_case`;
- [ ] usar `pass` para un cuerpo intencionalmente vacío;
- [ ] colocar herramientas de flujo conocidas dentro de una función;
- [ ] reconocer `None` implícito cuando no hay `return` explícito.

## 27. Referencia rápida

| Necesidad | Forma | Significado |
|---|---|---|
| definir una función | `def name():` | crear y vincular una función a un nombre |
| escribir comportamiento | cuerpo indentado | instrucciones ejecutadas por una llamada |
| llamar | `name()` | ejecutar el cuerpo |
| referirse | `name` | acceder al objeto función |
| mantener cuerpo vacío temporalmente | `pass` | instrucción válida sin operación |
| estilo normal de nombre | `snake_case` | convención legible para funciones |
| sin `return` explícito | final del cuerpo | resultado de la llamada es `None` |

## 28. Límite de alcance

Este capítulo intencionalmente no enseña en profundidad:

- parámetros y argumentos;
- diseño de valores de retorno;
- alcance local y global;
- type hints;
- valores predeterminados;
- `*args` y `**kwargs`;
- funciones anidadas;
- lambdas;
- decoradores;
- generadores;
- recursión.

Esas ideas merecen modelos mentales separados.

## 29. Qué viene después

Ahora puedes definir comportamiento, llamarlo, reutilizarlo y seguir su ejecución.

La siguiente pregunta es:

> ¿Cómo puede una función trabajar con diferentes valores de entrada?

Eso lleva al **Capítulo 02: Parámetros y Argumentos**.

Vuelve a la [ruta de Funciones](../README.es.md) o a la [ruta completa](../../docs/learning-path.es.md).

## Referencias

Documentación primaria de Python:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Language Reference: Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13 Language Reference: Calls](https://docs.python.org/3.13/reference/expressions.html#calls)
