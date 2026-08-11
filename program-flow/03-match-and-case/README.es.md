<div align="center">

# `match` y `case`: Coincidencia de Patrones Estructurales

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Flujo del Programa](../README.es.md) · [← Anterior: `if`, `elif` y `else`](../02-if-elif-and-else/README.es.md)

Una instrucción `if` pregunta si una condición es verdadera en contexto Booleano. Una instrucción `match` pregunta si un valor **coincide con un patrón**.

Esa diferencia empieza pequeña con valores literales y se vuelve más útil cuando el valor tiene estructura, como una tupla o un diccionario.

**Tiempo estimado de estudio:** 110–140 minutos.

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- explicar qué significa la coincidencia de patrones estructurales;
- reconocer que `match` y `case` se añadieron en Python 3.10;
- distinguir la coincidencia de patrones de las condiciones Booleanas normales;
- hacer coincidir valores literales con `case`;
- usar `_` como comodín de respaldo;
- combinar alternativas con un patrón OR usando `|`;
- explicar por qué `case 1 | 2 | 3:` y `case 1, 2, 3:` significan cosas diferentes;
- explicar por qué un nombre simple como `case value:` captura en lugar de comparar con una variable existente;
- extraer valores de patrones de secuencia;
- hacer coincidir claves seleccionadas en patrones de mapping;
- usar un guard para añadir una condición Booleana después de una coincidencia de patrón exitosa;
- elegir entre `if` y `match` según la intención;
- evitar depender de class patterns antes de que las clases se presenten más adelante en la guía.

## 1. Qué es la coincidencia de patrones estructurales

La coincidencia de patrones estructurales compara un valor sujeto con uno o más patrones.

El modelo mental básico es:

```text
subject value
    ↓
try the first case pattern
    ↓
match succeeds or fails
    ↓
if needed, try the next case
```

Un patrón puede describir más que un único valor exacto. También puede describir la **forma** de los datos y capturar partes de esos datos en nombres.

Python añadió la instrucción `match` en la versión 3.10.

## 2. Sintaxis básica

Una instrucción `match` contiene una expresión sujeto seguida de uno o más bloques `case`:

```python
match subject:
    case pattern_a:
        statement
    case pattern_b:
        statement
```

Python evalúa el sujeto y prueba los patrones de los casos en orden.

Cuando un patrón tiene éxito, se ejecuta su bloque. Normalmente, los bloques `case` posteriores no se prueban después de seleccionar un caso.

No existe fallthrough automático desde un caso seleccionado hacia el siguiente.

## 3. Empieza con patrones literales

El patrón más simple coincide con un valor literal:

```python
status = "ready"

match status:
    case "ready":
        print("Ready to begin")
    case "paused":
        print("Waiting")
```

Salida:

```text
Ready to begin
```

El sujeto es `status`.

Los patrones son los literales de cadena `"ready"` y `"paused"`.

Como el primer patrón tiene éxito, Python ejecuta ese bloque.

## 4. Añade un respaldo comodín con `_`

El guion bajo `_` es el patrón comodín.

Tiene éxito sin vincular el sujeto a un nombre:

```python
status = "offline"

match status:
    case "ready":
        print("Ready to begin")
    case "paused":
        print("Waiting")
    case _:
        print("Unknown status")
```

Salida:

```text
Unknown status
```

Este papel se parece a una rama final de respaldo, pero sigue siendo un patrón, no una cláusula `else`.

Como `_` coincide con cualquier cosa, un caso comodín sin guard debe ir al final.

## 5. El orden de los casos importa

Los patrones se prueban de arriba hacia abajo.

Coloca los casos más específicos antes de un respaldo amplio:

```python
command = "stop"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
```

Salida:

```text
Stopping
```

Cuando `"stop"` coincide, el caso comodín no se selecciona.

## 6. Un `case` puede aceptar varias alternativas

Usa `|` para crear un patrón OR:

```python
command = "resume"

match command:
    case "start" | "resume":
        print("Running")
    case "pause":
        print("Paused")
    case _:
        print("Unknown command")
```

Salida:

```text
Running
```

Léelo como:

```text
match "start" OR "resume"
```

La barra vertical forma parte de la sintaxis de patrones en este contexto.

## 7. `case 1 | 2 | 3` no es `case 1, 2, 3`

Esta es una distinción importante.

Para hacer coincidir uno de tres valores enteros, usa un patrón OR:

```python
option = 2

match option:
    case 1 | 2 | 3:
        print("Known option")
    case _:
        print("Unknown option")
```

Salida:

```text
Known option
```

Pero esta sintaxis significa algo diferente:

```python
case 1, 2, 3:
```

Describe un **patrón de secuencia** con tres posiciones.

Puede coincidir con un sujeto como:

```python
coordinates = (1, 2, 3)

match coordinates:
    case 1, 2, 3:
        print("Exact sequence")
    case _:
        print("Different sequence")
```

Salida:

```text
Exact sequence
```

Así que recuerda:

```text
1 | 2 | 3  = alternatives
1, 2, 3    = sequence structure
```

## 8. `match` es más que un switch tradicional

Al principio, los casos literales pueden parecerse a instrucciones `switch` de otros lenguajes.

Esa comparación solo sirve como punto de partida.

Los patrones de Python también pueden:

- describir estructura de secuencias;
- describir estructura de mappings;
- capturar componentes coincidentes en nombres;
- combinar patrones;
- usar guards después de una coincidencia estructural exitosa.

Ese comportamiento estructural es la razón por la que la funcionalidad se llama **coincidencia de patrones estructurales**.

## 9. `match` y `case` son palabras clave suaves

`match` y `case` son soft keywords.

Tienen significado especial en los contextos gramaticales que forman una instrucción match, pero no están reservadas en todas partes como las palabras clave ordinarias.

Para código de principiantes, la recomendación práctica es simple: sigue prefiriendo nombres descriptivos que no reutilicen `match` o `case` sin necesidad.

Eso evita confusión visual incluso cuando cierto uso sería sintácticamente válido.

## 10. Capture patterns

Un nombre dentro de un patrón puede capturar parte del sujeto.

Considera una tupla que representa un evento:

```python
event = ("move", 4, -2)

match event:
    case ("move", x, y):
        print(x)
        print(y)
```

Salida:

```text
4
-2
```

El literal `"move"` debe coincidir con el primer elemento.

Los nombres `x` e `y` capturan el segundo y el tercer elemento.

Después de que el caso seleccionado tiene éxito, esos nombres contienen los valores coincidentes.

## 11. Un nombre simple no compara con una variable existente

Esta es una de las trampas más importantes para principiantes en pattern matching.

Supón que ya tienes:

```python
expected = "ready"
status = "paused"
```

Esto **no** significa "comparar status con expected":

```python
match status:
    case expected:
        print(expected)
```

Aquí `expected` es un capture pattern. Captura el valor sujeto.

Eso significa que un patrón con nombre simple no es la forma normal de comparar con una variable que ya existe.

Para valores conocidos directamente en el código, usa patrones literales como:

```python
case "ready":
```

Cuando tu intención real sea una comparación Booleana arbitraria con valores de ejecución, una instrucción `if` suele ser más clara.

## 12. Por qué una captura irrefutable debe ir al final

Un capture pattern simple tiene éxito para cualquier sujeto que pueda recibir.

Por ejemplo:

```python
match status:
    case captured:
        print(captured)
```

Ese caso es irrefutable: sin un guard, siempre tiene éxito.

Un caso irrefutable sin guard no puede ir seguido de otro bloque `case`, porque los casos posteriores nunca podrían seleccionarse.

El comodín `_` también es irrefutable, pero, a diferencia de un nombre de captura, no vincula el sujeto.

## 13. Patrones de secuencia

Los patrones de secuencia permiten describir posiciones dentro de datos con comportamiento de secuencia.

Por ejemplo:

```python
point = (3, 7)

match point:
    case (x, y):
        print(f"x={x}, y={y}")
```

Salida:

```text
x=3, y=7
```

Se capturan ambas posiciones.

Un patrón de secuencia de longitud fija requiere el número esperado de elementos.

## 14. Combina literales y capturas en una secuencia

Los patrones se vuelven más descriptivos cuando algunas posiciones son fijas y otras se capturan:

```python
event = ("message", "Hello")

match event:
    case ("move", x, y):
        print(f"Move to {x}, {y}")
    case ("message", text):
        print(text)
    case _:
        print("Unknown event")
```

Salida:

```text
Hello
```

Esto es más que comparar la tupla completa por igualdad.

El patrón comprueba la estructura y extrae el componente relevante al mismo tiempo.

## 15. Listas y tuplas pueden coincidir con patrones de secuencia

La sintaxis de patrón de secuencia describe una estructura de secuencia, no necesariamente una sintaxis visual exacta del sujeto.

Por ejemplo:

```python
point = [8, 5]

match point:
    case (x, y):
        print(f"Point: {x}, {y}")
```

Salida:

```text
Point: 8, 5
```

Un sujeto lista puede satisfacer este patrón de secuencia de dos elementos.

No leas los paréntesis del patrón como "el sujeto debe ser una tupla".

## 16. Las cadenas no se tratan como patrones de secuencia aquí

Aunque las cadenas son secuencias en muchas operaciones de Python, los patrones de secuencia intencionalmente no tratan `str`, `bytes` o `bytearray` como sujetos de secuencia.

Haz coincidir texto con patrones literales u otra lógica apropiada en lugar de esperar pattern matching carácter por carácter.

Por ejemplo:

```python
word = "go"

match word:
    case "go":
        print("Go")
    case _:
        print("Other word")
```

Salida:

```text
Go
```

## 17. Patrones de secuencia con estrella

Un patrón con estrella puede capturar una parte intermedia o restante de longitud variable:

```python
values = [10, 20, 30, 40]

match values:
    case [first, *middle, last]:
        print(first)
        print(middle)
        print(last)
```

Salida:

```text
10
[20, 30]
40
```

La captura con estrella recibe una lista con los elementos intermedios no coincidentes.

Úsalo cuando la estructura de longitud variable forme parte del significado de los datos, no solo como una forma ingeniosa de desempaquetar todo.

## 18. Patrones de mapping

Los patrones de mapping permiten hacer coincidir claves seleccionadas en datos similares a mappings.

Un diccionario es el ejemplo más familiar:

```python
request = {
    "action": "open",
    "resource": "chapter",
}

match request:
    case {"action": "open", "resource": resource}:
        print(resource)
    case _:
        print("Unsupported request")
```

Salida:

```text
chapter
```

La clave `"action"` debe tener el valor literal `"open"`.

El valor asociado con `"resource"` se captura en `resource`.

## 19. Los patrones de mapping no exigen que el mapping tenga solo esas claves

Un patrón de mapping puede coincidir incluso cuando el sujeto tiene claves adicionales no mencionadas por el patrón:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "theme": "dark",
}

match request:
    case {"action": "open", "resource": resource}:
        print(resource)
```

Salida:

```text
chapter
```

La clave adicional `"theme"` no impide que este patrón tenga éxito.

Esto difiere de un patrón de secuencia de longitud fija, donde el número de posiciones es importante salvo que se use un patrón con estrella.

## 20. Captura elementos restantes de un mapping con `**rest`

Cuando importan las claves restantes, una captura con doble estrella puede recopilarlas:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "theme": "dark",
}

match request:
    case {"action": "open", **rest}:
        print(rest)
```

Salida:

```text
{'resource': 'chapter', 'theme': 'dark'}
```

La captura recibe un diccionario con los elementos de mapping no coincidentes.

## 21. Los guards añaden una condición después de que un patrón tiene éxito

Un caso puede incluir un guard con `if`:

```python
request = {
    "action": "open",
    "level": 3,
}

match request:
    case {"action": "open", "level": level} if level >= 2:
        print("Advanced access")
    case {"action": "open"}:
        print("Basic access")
```

Salida:

```text
Advanced access
```

El orden es:

```text
pattern succeeds
    ↓
evaluate the guard
    ↓
if the guard is truthy, select the case
otherwise try the next case
```

Los guards conectan este capítulo directamente con la lógica Booleana y los conceptos de `if` aprendidos anteriormente.

## 22. Un guard no forma parte del patrón estructural

Mantén separados ambos trabajos en tu modelo mental:

```text
pattern = does the value have the required form?
guard   = does an additional condition hold?
```

Por ejemplo:

```python
record = ("score", 82)

match record:
    case ("score", value) if value >= 70:
        print("Passing score")
    case ("score", value):
        print("Score below threshold")
```

Salida:

```text
Passing score
```

La estructura de la tupla coincide primero. El umbral numérico se comprueba después mediante el guard.

## 23. `match` versus `if`

Ninguna herramienta sustituye a la otra.

Usa `if` cuando la idea principal sea una condición Booleana arbitraria:

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

Usa `match` cuando la idea principal sea seleccionar comportamiento según el patrón o la estructura de un valor:

```python
event = ("click", 10, 20)

match event:
    case ("click", x, y):
        print(f"Click at {x}, {y}")
    case _:
        print("Other event")
```

Pregúntate cuál de las dos ideas describe mejor el problema.

## 24. Cuándo un `if` simple puede ser más claro

No uses `match` solo porque sea una sintaxis más nueva.

Para una comparación directa, esto es claro:

```python
if temperature > 30:
    print("Hot day")
```

Convertir cada pequeña condición en pattern matching puede añadir ceremonia sin añadir significado.

Prefiere la construcción que haga la decisión más fácil de entender.

## 25. Cuándo `match` se vuelve especialmente expresivo

`match` resulta útil cuando varios casos comparten un vocabulario estructurado.

Los ejemplos incluyen datos ficticios como:

```text
("move", x, y)
("message", text)
("quit",)
```

o mappings como:

```text
{"action": "open", "resource": ...}
{"action": "close", "resource": ...}
```

El propio patrón documenta la forma esperada mientras selecciona el comportamiento.

## 26. Error común: esperar fallthrough

Python selecciona el primer caso cuyo patrón tiene éxito y cuyo guard, si existe, es truthy.

No continúa automáticamente hacia el siguiente bloque `case` después.

No necesitas un `break` al final de cada caso.

Esto difiere del comportamiento de algunas construcciones switch tradicionales de otros lenguajes.

## 27. Error común: usar comas para alternativas

Modelo mental incorrecto:

```python
case 1, 2, 3:
```

Eso no significa "1 o 2 o 3".

Para alternativas, escribe:

```python
case 1 | 2 | 3:
```

Usa comas cuando realmente quieras representar estructura de secuencia.

## 28. Error común: usar un nombre de variable simple como constante

Este patrón captura:

```python
case expected:
```

Normalmente no significa "comparar con el valor actual almacenado en `expected`".

Para código de principiantes, prefiere:

- patrones literales cuando las alternativas sean valores literales;
- una condición `if` cuando compares con variables de ejecución;
- técnicas más avanzadas de value patterns solo después de comprender los conceptos de apoyo.

## 29. Error común: colocar `_` demasiado pronto

Esta estructura es conceptualmente incorrecta porque el comodín haría inalcanzables las alternativas posteriores:

```python
match command:
    case _:
        print("Anything")
    case "start":
        print("Start")
```

Coloca los patrones amplios de respaldo al final.

## 30. Error común: forzar patrones excesivamente complejos

Los patrones pueden volverse sofisticados, pero el código para principiantes no se beneficia de convertir un `case` en un rompecabezas.

Si un patrón mezcla demasiadas estructuras anidadas, capturas, alternativas OR y guards, considera si decisiones más pequeñas comunicarían mejor la intención.

El código legible sigue siendo el objetivo.

## 31. Límite de alcance: los class patterns quedan para más adelante

La coincidencia de patrones estructurales también puede trabajar con class patterns.

Esta guía no los exige aquí porque las clases todavía no se han presentado en la secuencia para principiantes.

Por ahora, este capítulo se mantiene dentro de conceptos ya disponibles:

- literales;
- listas y tuplas;
- diccionarios;
- nombres y asignación;
- condiciones Booleanas;
- condiciones Booleanas usadas como guards.

Los class patterns pueden revisitarse después de que los conceptos orientados a objetos formen parte del repertorio del estudiante.

## 32. Ejemplo trabajado: elecciones literales

El archivo [`examples/literal_and_or_patterns.py`](examples/literal_and_or_patterns.py) contiene:

```python
command = "pause"

match command:
    case "start" | "resume":
        message = "Session running"
    case "pause":
        message = "Session paused"
    case "stop":
        message = "Session stopped"
    case _:
        message = "Unknown command"

print(message)
```

Salida esperada:

```text
Session paused
```

Observa que `"start" | "resume"` agrupa dos alternativas literales en un solo caso.

## 33. Ejemplo trabajado: estructura de secuencia

El archivo [`examples/sequence_patterns.py`](examples/sequence_patterns.py) contiene:

```python
event = ("move", 4, -2)

match event:
    case ("move", x, y):
        print(f"Move to: {x}, {y}")
    case ("message", text):
        print(f"Message: {text}")
    case _:
        print("Unknown event")
```

Salida esperada:

```text
Move to: 4, -2
```

El primer elemento identifica el tipo de evento. Los elementos restantes se capturan como datos.

## 34. Ejemplo trabajado: patrón de mapping más guard

El archivo [`examples/mapping_patterns_and_guards.py`](examples/mapping_patterns_and_guards.py) contiene:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "level": 2,
    "theme": "dark",
}

match request:
    case {"action": "open", "resource": resource, "level": level} if level >= 2:
        print(f"Open advanced resource: {resource}")
    case {"action": "open", "resource": resource}:
        print(f"Open resource: {resource}")
    case _:
        print("Unsupported request")
```

Salida esperada:

```text
Open advanced resource: chapter
```

El mapping contiene una clave adicional `"theme"`, pero el primer patrón puede seguir coincidiendo porque los patrones de mapping no exigen que el sujeto contenga solo las claves enumeradas.

## 35. Ejercicio

Crea una variable llamada `event` que contenga uno de estos valores ficticios:

```python
("login", "Mina")
("logout", "Mina")
("move", 3, 8)
("unknown",)
```

Escribe una única instrucción `match` que:

1. capture y muestre el nombre para `("login", name)`;
2. capture y muestre el nombre para `("logout", name)`;
3. capture y muestre ambas coordenadas para `("move", x, y)`;
4. use `_` para cualquier otro valor.

Luego añade un segundo ejemplo pequeño en el que una variable entera llamada `option` acepte `1`, `2` o `3` en un único caso usando `|`.

Todavía no uses `for`, `while`, funciones, excepciones ni comprehensions.

## 36. Extensión del ejercicio

Crea este diccionario:

```python
request = {
    "action": "download",
    "file": "guide.pdf",
    "size_mb": 8,
}
```

Usa un patrón de mapping y un guard para que:

- una descarga con `size_mb <= 10` muestre `"Small download"`;
- otra solicitud de descarga muestre `"Large download"`;
- cualquier otra acción llegue a `_`.

Mantén el ejemplo determinista y no interactivo.

## 37. Lista de revisión

Antes de continuar, confirma que puedes explicar cada afirmación sin ejecutar el código:

- [ ] `match` evalúa un sujeto y lo compara con patrones.
- [ ] los casos se consideran en orden.
- [ ] solo se ejecuta el primer bloque de caso seleccionado.
- [ ] `_` es un comodín y no vincula un nombre.
- [ ] `|` crea alternativas de patrón.
- [ ] las comas pueden describir estructura de secuencia en lugar de alternativas.
- [ ] un nombre simple de captura no es una comparación normal con una constante.
- [ ] los patrones de secuencia pueden extraer componentes posicionales.
- [ ] los patrones de mapping pueden extraer valores mediante claves.
- [ ] las claves adicionales de mapping no impiden automáticamente una coincidencia.
- [ ] un guard añade una condición Booleana después de que la coincidencia estructural tiene éxito.
- [ ] `if` sigue siendo útil para decisiones Booleanas arbitrarias.
- [ ] los class patterns se posponen intencionalmente en esta ruta de aprendizaje.

## 38. Referencia rápida

| Necesidad | Forma típica |
|---|---|
| Hacer coincidir un literal | `case "start":` |
| Hacer coincidir varias alternativas | `case "start" | "resume":` |
| Respaldo | `case _:` |
| Hacer coincidir una secuencia de dos elementos | `case (x, y):` |
| Hacer coincidir una secuencia etiquetada | `case ("move", x, y):` |
| Capturar un resto de longitud variable | `case [first, *rest]:` |
| Hacer coincidir claves seleccionadas de mapping | `case {"action": "open", "resource": resource}:` |
| Capturar elementos adicionales de mapping | `case {"action": "open", **rest}:` |
| Añadir una condición | `case pattern if condition:` |
| Decisión Booleana arbitraria | normalmente `if condition:` |

Recuerda la progresión:

**sujeto → patrón → capturas opcionales → guard opcional → bloque seleccionado**

## Siguiente paso

El próximo capítulo es **Loops `for` e Iteración**.

Ahora sabes cómo Python puede seleccionar comportamiento a partir de condiciones y patrones de datos. A continuación, la guía pasa de **selección** a **repetición**, usando `for` para procesar elementos de un iterable uno por uno.

## Referencias oficiales

- [Referencia del lenguaje Python 3.13: la instrucción `match`](https://docs.python.org/3.13/reference/compound_stmts.html#the-match-statement)
- [Tutorial de Python 3.13: instrucciones `match`](https://docs.python.org/3.13/tutorial/controlflow.html#match-statements)
- [PEP 634: Structural Pattern Matching — Specification](https://peps.python.org/pep-0634/)
- [PEP 636: Structural Pattern Matching — Tutorial](https://peps.python.org/pep-0636/)
