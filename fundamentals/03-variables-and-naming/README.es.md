<div align="center">

# Variables y Nombres

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: `print()` e `input()`](../02-print-and-input/README.es.md)

Los programas se vuelven más útiles cuando pueden conservar información bajo nombres comprensibles y reutilizarla después. La asignación en Python conecta un nombre con un valor, permitiendo que instrucciones posteriores lean ese valor sin repetirlo.

Este capítulo presenta variables, asignación, reasignación, identificadores válidos y convenciones prácticas de nombres. Los tipos de datos en detalle, las comparaciones y el alcance se dejan deliberadamente para capítulos posteriores.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Prerrequisitos | Completar los Capítulos 01 y 02 |
| Tiempo estimado de estudio | 50 a 70 minutos |
| Conceptos principales | Variable, nombre, asignación, identificador, reasignación, palabra clave, `snake_case` |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- asignar un valor a un nombre con `=`;
- leer un valor almacenado usando su nombre;
- explicar que el lado derecho se evalúa antes de la asignación;
- reasignar un nuevo valor a un nombre;
- reconocer identificadores válidos e inválidos;
- explicar por qué las palabras clave de Python no pueden ser nombres de variables;
- elegir nombres claros en `snake_case`;
- evitar ocultar funciones incorporadas como `print` e `input`;
- distinguir las reglas de sintaxis de Python de las convenciones de nombres del proyecto.

## 1. Por qué los programas almacenan valores

Sin nombres, un programa debe repetir el mismo valor cada vez que lo necesita:

```python
print("Python Study Guide")
print("Current course:", "Python Study Guide")
```

Un nombre permite almacenar el valor una vez y reutilizarlo:

```python
course_name = "Python Study Guide"

print(course_name)
print("Current course:", course_name)
```

Esto reduce repeticiones y facilita cambios posteriores.

## 2. La asignación usa `=`

Una instrucción básica de asignación tiene un objetivo a la izquierda y una expresión que produce un valor a la derecha:

```python
learner_name = "Ada"
```

Léela así:

> Asigna el texto `"Ada"` al nombre `learner_name`.

Para una persona principiante, es razonable llamar variable a `learner_name`. De forma más precisa, Python vincula el nombre `learner_name` con el valor resultante.

El símbolo `=` realiza una asignación. No pregunta si dos valores son iguales. Las comparaciones con `==` pertenecen a un capítulo posterior.

## 3. Usa el nombre para leer el valor

Después de la asignación, usar el nombre recupera el valor asociado actualmente:

```python
learner_name = "Ada"

print(learner_name)
print("Learner:", learner_name)
```

Salida esperada:

```text
Ada
Learner: Ada
```

Las comillas crean texto literal. Un nombre sin comillas le pide a Python su valor almacenado.

## 4. El lado derecho se evalúa primero

Python evalúa la expresión de la derecha antes de asignar su resultado al nombre de la izquierda:

```python
topic = input("Topic: ")
```

El orden es:

1. `input("Topic: ")` muestra el prompt y retorna texto;
2. el texto retornado se asigna a `topic`.

El mismo patrón funciona con otras expresiones:

```python
full_title = "Python" + " Study Guide"
print(full_title)
```

La expresión crea el texto final antes de que `full_title` lo reciba.

## 5. La reasignación actualiza lo que referencia un nombre

Un nombre puede recibir un nuevo valor más adelante:

```python
current_topic = "Output and input"
print("Before:", current_topic)

current_topic = "Variables and naming"
print("After:", current_topic)
```

Salida esperada:

```text
Before: Output and input
After: Variables and naming
```

La segunda asignación sustituye el valor recuperado mediante `current_topic` desde ese punto.

Python no exige una declaración especial antes de la primera asignación.

## 6. Los nombres distinguen mayúsculas y minúsculas

Python trata las letras mayúsculas y minúsculas como diferentes:

```python
topic = "Variables"
Topic = "Naming"

print(topic)
print(Topic)
```

`topic` y `Topic` son dos nombres diferentes. Evita nombres que solo se diferencien por las mayúsculas porque son fáciles de confundir.

## 7. Una regla segura para identificadores principiantes

El nombre de una variable es un **identificador**. Para código principiante portátil con identificadores en inglés, sigue esta regla segura:

- comienza con una letra inglesa o guion bajo;
- continúa con letras inglesas, dígitos o guiones bajos;
- no incluye espacios ni guiones;
- no comienza con un dígito.

Ejemplos válidos:

```python
name = "Ada"
learner_name = "Ada"
topic_2 = "Variables"
_private_note = "Draft"
```

Ejemplos inválidos:

```text
2topic = "Variables"
learner-name = "Ada"
learner name = "Ada"
```

Python acepta una gama más amplia de letras Unicode en los identificadores. Aun así, este proyecto usa identificadores descriptivos en inglés como convención del repositorio.

## 8. Las palabras clave no pueden ser nombres de variables

Las palabras clave tienen significados gramaticales reservados en Python. No pueden reutilizarse como identificadores ordinarios:

```text
class = "beginner"
for = "practice"
```

Ambas líneas son inválidas porque `class` y `for` son palabras clave.

No necesitas memorizar todas de inmediato. Los editores normalmente las resaltan, y el módulo `keyword` de la biblioteca estándar puede verificarlas más adelante.

## 9. Prefiere `snake_case`

PEP 8 recomienda palabras en minúsculas separadas por guiones bajos para nombres de variables y funciones:

```python
learner_name = "Ada"
study_topic = "Variables and naming"
practice_minutes = "30"
```

Este estilo se llama `snake_case`.

Compara:

```text
learnername
LearnerName
learner-name
learner_name
```

Para variables ordinarias en este proyecto, `learner_name` es la forma preferida.

## 10. Elige nombres que revelen significado

Un nombre debe ayudar a la persona lectora a entender la función del valor:

```python
x = "45"
```

El nombre `x` casi no ofrece contexto.

```python
practice_minutes = "45"
```

El nombre más claro revela tanto el propósito como la unidad.

Preguntas útiles al nombrar una variable:

- ¿Qué información representa este valor?
- ¿Por qué usará el programa este valor?
- ¿Importa una unidad como minutos, kilogramos o reales?
- ¿El nombre seguirá teniendo sentido varias líneas después?

## 11. Evita abreviaturas sin explicación

Los nombres cortos ahorran teclas, pero pueden costar comprensión:

```python
nm = "Ada"
tp = "Variables"
mins = "30"
```

Prefiere nombres completos y legibles:

```python
learner_name = "Ada"
study_topic = "Variables"
practice_minutes = "30"
```

Las abreviaturas ampliamente comprendidas pueden ser apropiadas, pero inventar abreviaturas locales normalmente crea un rompecabezas de descifrado.

## 12. Evita ocultar funciones incorporadas

Python permite reasignar algunos nombres de funciones incorporadas, pero eso oculta la función original bajo ese nombre:

```python
print = "not a function anymore"
```

Después de esa asignación, esta llamada falla porque `print` ahora referencia texto:

```text
print("Hello")
```

Evita nombres de variables como:

- `print`;
- `input`;
- `str`;
- `int`;
- `list`;
- `sum`.

No todos son palabras clave, pero conservar los nombres incorporados evita fallos confusos.

## 13. Los identificadores en inglés son una convención del proyecto

Python acepta identificadores de muchos sistemas de escritura. Python Study Guide utiliza identificadores en inglés en el código compartido:

```python
learner_name = "Ada"
study_goal = "Build useful programs"
```

Esta es una convención del repositorio, no un requisito universal de Python. Las explicaciones siguen siendo multilingües, mientras que el código compartido permanece idéntico entre las traducciones.

## 14. Las constantes usan una convención en mayúsculas

Un valor que se pretende mantener sin cambios durante el programa suele escribirse con palabras en mayúsculas:

```python
COURSE_NAME = "Python Study Guide"
DEFAULT_TOPIC = "Fundamentals"
```

Este estilo comunica intención a las personas lectoras. Python no impide la reasignación, por lo que las mayúsculas son una convención y no una garantía.

## 15. Almacena y reutiliza entradas

El Capítulo 02 usó la asignación como un puente. Ahora puedes describir las partes con mayor precisión:

```python
learner_name = input("Name: ")
study_topic = input("Topic: ")

print("Learner:", learner_name)
print("Topic:", study_topic)
```

Cada prompt retorna texto. Cada asignación le da un nombre significativo a ese texto y cada `print()` posterior lee el valor almacenado.

## 16. Un nombre no es igual a un texto con la misma escritura

Compara estas llamadas:

```python
learner_name = "Ada"

print(learner_name)
print("learner_name")
```

Salida esperada:

```text
Ada
learner_name
```

La primera llamada lee la variable. La segunda imprime texto literal porque los caracteres están dentro de las comillas.

## 17. Usar un nombre antes de la asignación causa un error

Python debe encontrar una asignación antes de que el nombre pueda leerse en el flujo actual del programa:

```text
print(current_topic)
current_topic = "Variables"
```

Ejecutar este ejemplo en el nivel principal genera `NameError` porque `current_topic` todavía no está asignado cuando se ejecuta la primera línea.

Mueve la asignación antes de la lectura:

```python
current_topic = "Variables"
print(current_topic)
```

## 18. Ejemplos del repositorio

| Archivo | Finalidad | Ejecución automática |
|---|---|---|
| [`variable_basics.py`](examples/variable_basics.py) | Demuestra asignación, reutilización, nombres claros y reasignación | Sí |
| [`learning_profile.py`](examples/learning_profile.py) | Recopila y muestra un pequeño perfil de aprendizaje | No; espera entrada en la terminal |

El ejemplo interactivo se excluye deliberadamente del manifiesto de ejemplos ejecutados sin supervisión.

## 19. Ejemplo práctico: perfil de aprendizaje

Crea `learning_profile.py`:

```python
learner_name = input("Name: ")
current_topic = input("Current topic: ")
study_goal = input("Study goal: ")

print()
print("LEARNING PROFILE")
print("Name:", learner_name)
print("Topic:", current_topic)
print("Goal:", study_goal)
```

Una posible sesión es:

```text
Name: Ada
Current topic: Variables
Study goal: Build useful programs

LEARNING PROFILE
Name: Ada
Topic: Variables
Goal: Build useful programs
```

Los nombres explican lo que representa cada respuesta y facilitan la construcción de la salida final.

## 20. Ejercicio

Crea `study_session.py` que:

1. almacene el nombre de la guía en `GUIDE_NAME`;
2. pregunte el nombre de la persona estudiante;
3. pregunte el tema;
4. pregunte el tiempo de práctica planificado como texto;
5. imprima una línea en blanco;
6. imprima un resumen etiquetado de la sesión;
7. reasigne el tema a `"Review completed"`;
8. imprima el tema actualizado.

Usa exactamente estos nombres:

```python
GUIDE_NAME
learner_name
study_topic
practice_minutes
```

Ejecuta el programa dos veces con respuestas diferentes. Después, sustituye un nombre claro por un nombre vago como `x`, lee el programa y restaura el nombre más claro.

## 21. Errores comunes

### Leer antes de la asignación

```text
print(city)
city = "London"
```

Asigna primero y lee después.

### Colocar el nombre de la variable entre comillas

```python
city = "London"
print("city")
```

Esto imprime `city`, no `London`.

### Comenzar un nombre con un dígito

```text
1st_topic = "Variables"
```

Usa un identificador válido como `first_topic`.

### Usar espacios o guiones

```text
learner name = "Ada"
learner-name = "Ada"
```

Usa `learner_name`.

### Usar una palabra clave

```text
class = "beginner"
```

Elige una alternativa descriptiva como `course_level`.

### Reutilizar un nombre incorporado

```text
input = "stored text"
```

Elige un nombre que describa el valor, como `user_response`.

### Usar mayúsculas incompatibles

```text
study_topic = "Variables"
print(Study_Topic)
```

Los nombres distinguen mayúsculas y minúsculas.

## 22. Autoevaluación

Estás listo para el siguiente capítulo cuando puedas responder:

- ¿Qué hace `=`?
- ¿Qué lado de una asignación se evalúa primero?
- ¿Qué sucede durante una reasignación?
- ¿Por qué `topic` y `Topic` son diferentes?
- ¿Qué caracteres son seguros para un identificador en inglés?
- ¿Por qué `class` no puede ser un nombre de variable?
- ¿Cómo se ve `snake_case`?
- ¿Por qué una variable no debería llamarse `print`?
- ¿Python impone la escritura de constantes en mayúsculas?
- ¿Cuál es la diferencia entre `print(name)` y `print("name")`?

## 23. Resumen de consulta rápida

| Objetivo | Ejemplo |
|---|---|
| Asignar un valor | `topic = "Variables"` |
| Leer un valor | `print(topic)` |
| Reasignar un nombre | `topic = "Naming"` |
| Estilo claro de variable | `practice_minutes` |
| Convención de constante | `COURSE_NAME` |
| Almacenar entrada | `name = input("Name: ")` |
| Texto literal | `print("name")` |
| Valor almacenado | `print(name)` |
| Evitar ocultar nombres incorporados | No asignes a `print` ni `input` |
| Sensibilidad a mayúsculas | `name` y `Name` son diferentes |

## 24. Ejecuta los ejemplos del repositorio

Desde la raíz del repositorio, ejecuta el ejemplo automático:

```bash
python fundamentals/03-variables-and-naming/examples/variable_basics.py
```

Ejecuta el ejemplo interactivo y responde sus prompts:

```bash
python fundamentals/03-variables-and-naming/examples/learning_profile.py
```

## 25. Ejecuta las verificaciones del repositorio

Desde la raíz del repositorio:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

El ejecutor de ejemplos aprobados ejecuta `variable_basics.py`, pero no ejecuta `learning_profile.py`, porque las verificaciones sin supervisión no deben esperar entrada del teclado.

## Referencias oficiales

- [Referencia del lenguaje Python — Instrucciones de asignación](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)
- [Referencia del lenguaje Python — Identificadores y palabras clave](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
- [Biblioteca estándar de Python — Verificación de palabras clave](https://docs.python.org/3/library/keyword.html)
- [PEP 8 — Convenciones de nombres](https://peps.python.org/pep-0008/#naming-conventions)

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: `print()` e `input()`](../02-print-and-input/README.es.md)
