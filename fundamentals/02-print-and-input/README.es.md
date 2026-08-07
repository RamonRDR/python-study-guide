<div align="center">

# Salida con `print()` y Entrada con `input()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Cómo ejecuta Python un programa](../01-how-python-runs-a-program/README.es.md)

Un programa se vuelve más fácil de comprender cuando puede mostrar lo que está haciendo y recibir información de la persona que lo utiliza. Python proporciona dos funciones incorporadas para estas primeras conversaciones: `print()` muestra salidas, e `input()` lee una línea de texto desde la terminal.

Este capítulo construye un pequeño programa interactivo mientras mantiene clara la diferencia entre la salida del programa, la entrada escrita y el código fuente.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante absoluto |
| Prerrequisitos | Crear, guardar y ejecutar un archivo `.py` desde la terminal |
| Tiempo estimado de estudio | 45 a 65 minutos |
| Conceptos principales | Salida, entrada, llamada de función, argumento, prompt, `sep`, `end`, texto retornado |

## Objetivos de aprendizaje

Al final de este capítulo, deberías poder:

- usar `print()` para mostrar texto y otros valores;
- pasar más de un valor a `print()`;
- controlar el separador y el final de línea con `sep` y `end`;
- usar `input()` con un prompt claro;
- explicar por qué `input()` pausa el programa;
- almacenar bajo un nombre el texto retornado por `input()`;
- distinguir la salida del programa del texto escrito por la persona usuaria;
- reconocer cuándo la entrada interactiva no es apropiada para programas desatendidos.

## 1. La salida y la entrada siguen direcciones diferentes

La **salida** es información que el programa envía hacia afuera. Puede aparecer en una terminal, interfaz gráfica, archivo, log u otro destino.

La **entrada** es información que entra en el programa. Puede venir de un teclado, archivo, solicitud de red, sensor u otro sistema.

En este capítulo:

- `print()` envía texto a la terminal;
- `input()` recibe una línea escrita en la terminal.

```text
persona ──entrada──▶ programa ──salida──▶ terminal
```

## 2. `print()` e `input()` son funciones incorporadas

Una función es una operación reutilizable. Llamar una función significa escribir su nombre seguido de paréntesis.

```python
print("Hello, World!")
```

En esta llamada:

- `print` es el nombre de la función;
- los paréntesis llaman la función;
- `"Hello, World!"` es un argumento proporcionado a la función.

Tanto `print()` como `input()` están incorporadas en Python, por lo que estos primeros ejemplos no requieren una instrucción `import`.

## 3. Muestra un valor con `print()`

La forma más sencilla muestra un valor:

```python
print("Python is running.")
```

Salida esperada:

```text
Python is running.
```

Las comillas pertenecen al código fuente. Indican un valor de texto y no se muestran como parte de la salida.

## 4. Muestra varios valores

Separa varios argumentos con comas:

```python
print("Python", "Study", "Guide")
```

Salida esperada:

```text
Python Study Guide
```

De forma predeterminada, `print()` inserta un espacio entre los argumentos mostrados.

Una coma entre argumentos forma parte de la sintaxis de Python. Una coma escrita dentro de las comillas es texto normal:

```python
print("Hello,", "student!")
```

Salida esperada:

```text
Hello, student!
```

## 5. Cambia el separador con `sep`

El argumento `sep` controla lo que aparece entre varios valores mostrados:

```python
print("2026", "08", "06", sep="-")
```

Salida esperada:

```text
2026-08-06
```

Otro ejemplo:

```python
print("Python", "Study", "Guide", sep=" | ")
```

Salida esperada:

```text
Python | Study | Guide
```

`sep` solo produce una diferencia cuando `print()` recibe más de un valor.

## 6. Cambia el final de línea con `end`

De forma predeterminada, `print()` termina con un salto de línea, por lo que la siguiente salida comienza en la línea siguiente.

El argumento `end` reemplaza ese salto final:

```python
print("Loading", end="...")
print("done!")
```

Salida esperada:

```text
Loading...done!
```

Usa `end` de forma deliberada. Eliminar los saltos de línea en todas partes puede hacer que la salida de la terminal sea difícil de leer.

## 7. Imprime una línea en blanco

Llamar `print()` sin argumentos escribe únicamente su salto de línea predeterminado:

```python
print("First section")
print()
print("Second section")
```

Salida esperada:

```text
First section

Second section
```

Esto es útil para separar pequeños grupos de salida en la terminal.

## 8. Lee una línea con `input()`

`input()` puede mostrar un prompt y esperar a que la persona escriba una respuesta:

```python
name = input("What is your name? ")
```

El programa se pausa en esta línea. Después de que la persona escribe una respuesta y presiona Enter, `input()` retorna esa respuesta como texto.

El espacio antes de las comillas finales mantiene el cursor visualmente separado del prompt:

```text
What is your name? Ada
```

Sin ese espacio, la respuesta escrita puede verse pegada a la pregunta.

## 9. Almacena el texto retornado

Esta línea realiza dos operaciones conectadas:

```python
name = input("What is your name? ")
```

1. `input()` lee y retorna texto.
2. `name =` almacena ese texto retornado bajo el nombre `name`.

El próximo capítulo explica las variables y los nombres con detalle. Por ahora, considera `name` una etiqueta que permite al programa utilizar la respuesta más adelante.

## 10. Muestra la respuesta

Después de almacenar el resultado, pásalo a `print()`:

```python
name = input("What is your name? ")
print("Hello,", name)
```

Una posible sesión en la terminal es:

```text
What is your name? Ada
Hello, Ada
```

La primera línea contiene el prompt del programa y la respuesta escrita por la persona. Normalmente, la terminal muestra los caracteres a medida que se escriben. La segunda línea es producida por `print()`.

## 11. Haz más de una pregunta

Las instrucciones siguen ejecutándose en orden:

```python
name = input("What is your name? ")
city = input("Which city do you live in? ")

print("Name:", name)
print("City:", city)
```

Python espera la primera respuesta antes de mostrar el segundo prompt.

Una posible sesión es:

```text
What is your name? Ada
Which city do you live in? London
Name: Ada
City: London
```

## 12. `input()` retorna texto

Incluso cuando una persona escribe dígitos, `input()` retorna un valor de texto. La siguiente respuesta es un texto que contiene los caracteres `2` y `5`, todavía no un número:

```python
age = input("How old are you? ")
print("You entered:", age)
```

El capítulo posterior sobre conversión de tipos explicará cómo transformar texto compatible en valores numéricos. Hasta entonces, usa el resultado como texto.

## 13. Presionar Enter puede retornar texto vacío

Una persona puede presionar Enter sin escribir ningún carácter visible:

```python
answer = input("Press Enter without typing: ")
print("You entered:", answer)
```

En ese caso, `answer` contiene un valor de texto vacío. El programa no decide automáticamente que una entrada vacía sea inválida. La validación se presentará después de las condiciones y del flujo del programa.

## 14. `input()` elimina el salto final de Enter

Presionar Enter termina la respuesta. El carácter de final de línea utilizado para enviar la respuesta no se incluye en el texto retornado.

Por eso, la siguiente salida permanece en una sola línea:

```python
word = input("Type one word: ")
print("Received:", word)
```

La palabra escrita se retorna, pero se elimina el salto usado para enviarla.

## 15. Cuándo usar `input()`

`input()` es útil para:

- ejercicios para principiantes;
- pequeñas conversaciones en la terminal;
- utilidades manuales usadas por una persona a la vez;
- experimentos rápidos en los que se espera aguardar una respuesta.

Evita depender de `input()` cuando un programa debe ejecutarse sin una persona, por ejemplo en:

- tareas programadas;
- pruebas automatizadas;
- servicios en segundo plano;
- integración continua;
- pipelines de procesamiento de datos.

Un programa desatendido puede permanecer pausado indefinidamente o fallar cuando no hay una fuente de entrada disponible. Estos programas normalmente reciben configuración mediante argumentos, archivos, variables de entorno, APIs u otras interfaces explícitas.

## 16. Ejemplos del repositorio

| Archivo | Finalidad | Ejecución automática |
|---|---|---|
| [`output_basics.py`](examples/output_basics.py) | Demuestra varios valores, `sep`, `end` y líneas en blanco | Sí |
| [`interactive_greeting.py`](examples/interactive_greeting.py) | Lee un nombre y muestra un saludo | No; espera entrada en la terminal |

El ejemplo interactivo no se incluye deliberadamente en el manifiesto de ejemplos ejecutados sin supervisión.

## 17. Ejemplo práctico: una tarjeta de estudiante

Crea `student_card.py`:

```python
name = input("Name: ")
city = input("City: ")
learning_goal = input("Learning goal: ")

print()
print("STUDENT CARD")
print("Name:", name)
print("City:", city)
print("Goal:", learning_goal)
```

Una posible sesión es:

```text
Name: Ada
City: London
Learning goal: Build useful programs

STUDENT CARD
Name: Ada
City: London
Goal: Build useful programs
```

Este programa ya tiene un flujo de datos simple: las preguntas producen textos, los nombres conservan esos textos y `print()` los muestra con una nueva organización.

## 18. Ejercicio

Crea un archivo llamado `learning_check_in.py` que:

1. pregunte el nombre de la persona estudiante;
2. pregunte qué tema de Python desea estudiar;
3. pregunte cuántos minutos planea practicar, manteniendo la respuesta como texto;
4. imprima una línea en blanco;
5. imprima el encabezado `LEARNING CHECK-IN`;
6. muestre las tres respuestas en líneas separadas y etiquetadas;
7. imprima `Study`, `Understand` y `Practice` separados por ` -> `;
8. termine con `Ready!` en la misma línea que `Starting...`.

Usa exactamente estas llamadas finales:

```python
print("Study", "Understand", "Practice", sep=" -> ")
print("Starting", end="...")
print("Ready!")
```

Ejecuta el programa al menos dos veces con respuestas diferentes.

## 19. Errores comunes

### Olvidar los paréntesis

```text
print "Hello"
```

Python 3 requiere una llamada de función con paréntesis:

```python
print("Hello")
```

### Olvidar las comillas alrededor de texto literal

```text
print(Hello)
```

Sin comillas, Python trata `Hello` como un nombre y no como texto literal.

### Usar una sintaxis incorrecta para el separador

Escribe `sep` dentro de la llamada a `print()`:

```python
print("A", "B", sep="-")
```

### Esperar que `input()` continúe inmediatamente

`input()` espera hasta que se envía una línea. Un programa que parece detenido puede estar simplemente esperando una respuesta.

### Olvidar almacenar la respuesta

Llamar `input()` por sí solo lee texto, pero la respuesta se descarta si el programa no almacena ni utiliza el valor retornado.

### Tratar los dígitos escritos como un número

`input()` retorna texto. La conversión numérica pertenece a un capítulo posterior.

### Confundir el eco de la terminal con `print()`

La terminal puede mostrar lo que la persona escribe. Esa respuesta visible no es una llamada adicional a `print()`.

## 20. Autoverificación

Estás preparado para el próximo capítulo cuando puedas responder:

- ¿En qué dirección viaja la salida?
- ¿Qué coloca `print()` entre varios argumentos de forma predeterminada?
- ¿Qué reemplaza `end`?
- ¿Por qué `input()` pausa el programa?
- ¿Qué clase de valor retorna `input()`?
- ¿Qué sucede cuando la persona presiona Enter sin escribir?
- ¿Por qué un script desatendido normalmente debe evitar la entrada interactiva?
- ¿Qué texto visible en la terminal fue producido por el programa y cuál fue escrito por la persona?

## 21. Resumen de consulta rápida

| Objetivo | Ejemplo |
|---|---|
| Mostrar texto | `print("Hello")` |
| Mostrar varios valores | `print("Name:", name)` |
| Cambiar el separador | `print("A", "B", sep="-")` |
| Permanecer en la misma línea | `print("Loading", end="...")` |
| Imprimir una línea en blanco | `print()` |
| Hacer una pregunta | `input("Question: ")` |
| Almacenar una respuesta | `answer = input("Question: ")` |
| Tipo importante de la entrada | `input()` retorna texto |
| Respuesta vacía | Presionar Enter puede retornar texto vacío |
| Ejecución desatendida | Evita esperar `input()` |

## 22. Ejecuta los ejemplos del repositorio

Desde la raíz del repositorio, ejecuta el ejemplo automático:

```bash
python fundamentals/02-print-and-input/examples/output_basics.py
```

Ejecuta el ejemplo interactivo y responde a su prompt:

```bash
python fundamentals/02-print-and-input/examples/interactive_greeting.py
```

## 23. Ejecuta las verificaciones del repositorio

Desde la raíz del repositorio:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

El ejecutor de ejemplos aprobados ejecuta `output_basics.py`, pero no ejecuta `interactive_greeting.py`, porque las verificaciones desatendidas no deben esperar entrada del teclado.

## Referencias oficiales

- [Documentación de Python — Funciones incorporadas: `print()` e `input()`](https://docs.python.org/3/library/functions.html)
- [Tutorial de Python — Entrada y salida](https://docs.python.org/3/tutorial/inputoutput.html)

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Cómo ejecuta Python un programa](../01-how-python-runs-a-program/README.es.md)
