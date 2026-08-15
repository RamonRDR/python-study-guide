<div align="center">

# Manejo de Excepciones con `try`, `except`, `else` y `finally`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Errores, Archivos y Módulos](../README.es.md) · [← Fase anterior: Comentarios y Documentación](../../comments-and-documentation/README.es.md)

Los programas no siempre siguen el camino ideal. Una conversión puede recibir texto inválido, una división puede usar cero, una consulta en un diccionario puede no encontrar una clave o una futura operación con archivos puede fallar.

Python representa muchos de estos fallos de runtime mediante **excepciones**. Una instrucción `try` permite que el programa defina qué debe ocurrir cuando una excepción específica interrumpe la ejecución normal.

Este capítulo se concentra en **manejar excepciones que ya ocurren**. El Capítulo 02 explicará cómo crear excepciones deliberadamente con `raise` y cómo definir clases simples de excepciones personalizadas.

**Tiempo estimado de estudio:** 90–120 minutos.

**Requisito de Python:** Python 3.10 o posterior. Los ejemplos reutilizan sintaxis moderna de type hints, como `int | None`, presentada en la fase de Funciones.

## Objetivos de aprendizaje

Al terminar este capítulo, deberías poder:

- explicar la diferencia entre un error de sintaxis y una excepción de runtime;
- describir cómo una excepción interrumpe el flujo normal de control;
- usar `try` y una cláusula `except` específica;
- manejar distintos tipos de excepción con handlers separados;
- acceder a una excepción capturada con `as` cuando sus detalles sean útiles;
- explicar por qué importa el orden de los handlers;
- usar `else` para código que debe ejecutarse solo cuando el bloque `try` termina normalmente;
- usar `finally` para tareas de limpieza que deben ocurrir en todas las rutas de salida;
- explicar qué ocurre cuando ninguna cláusula `except` coincide con la excepción;
- mantener bloques `try` suficientemente pequeños para mostrar qué operación puede fallar;
- evitar ocultar fallos no relacionados con handlers demasiado amplios;
- distinguir manejar una excepción de prevenir todos los posibles estados inválidos;
- seguir la ruta de ejecución a través de `try`, `except`, `else` y `finally`.

## 1. Flujo normal y flujo excepcional

La mayor parte del código sigue una secuencia normal:

```text
instrucción 1
    ↓
instrucción 2
    ↓
instrucción 3
```

Una excepción cambia esa ruta:

```text
instrucción 1
    ↓
operación con fallo
    ↓ excepción lanzada
buscar un handler coincidente
```

Si existe un handler coincidente, la ejecución puede continuar desde la estructura de manejo. Si no existe, la excepción continúa hacia afuera a través del código circundante y las llamadas de función.

Este es un mecanismo de flujo de control diferente de `if`, los bucles y los valores retornados normalmente.

## 2. Los errores de sintaxis y las excepciones no son lo mismo

Un **error de sintaxis** significa que Python no puede analizar el código fuente de acuerdo con la gramática del lenguaje.

Por ejemplo, este código fuente es inválido:

```python
if score > 70
    print("Ready")
```

La ausencia de los dos puntos impide que el archivo se analice normalmente.

Una **excepción de runtime** ocurre después de que Python ya tiene código válido para ejecutar, pero una operación no puede terminar normalmente.

```python
number = int("seven")
```

La sintaxis es válida. La conversión falla en runtime y lanza `ValueError`.

Este capítulo trata principalmente sobre excepciones de runtime.

## 3. Cómo pensar en una excepción no manejada

Considera:

```python
number = int("seven")
print(number)
```

`int("seven")` no puede producir el entero solicitado. Python lanza `ValueError` antes de que `print(number)` pueda ejecutarse.

Cuando una excepción permanece sin manejar en un script normal, la ejecución se detiene y Python muestra un traceback que describe por dónde se propagó el fallo.

El modelo inicial importante es:

```text
la operación no puede completarse
        ↓
se lanza el objeto excepción
        ↓
se interrumpe la ruta normal
        ↓
Python busca un handler coincidente
```

## 4. El `try` y `except` útil más pequeño

```python
try:
    number = int("seven")
except ValueError:
    print("Invalid integer")
```

Salida:

```text
Invalid integer
```

El bloque `try` contiene código que puede lanzar una excepción.

El bloque `except ValueError` describe qué hacer si un `ValueError` llega a esta instrucción `try`.

## 5. Lee la estructura como dos rutas posibles

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

Un seguimiento útil es:

```text
try int(text)
    ├─ éxito → continuar después de la instrucción try
    └─ ValueError → ejecutar except ValueError
```

El bloque `except` no se ejecuta cuando la operación protegida tiene éxito.

## 6. Captura la excepción que esperas

Prefiere nombrar el fallo que el código sabe manejar:

```python
try:
    score = int("ninety")
except ValueError:
    print("Score must be an integer")
```

Esto comunica al lector que un texto numérico inválido es un caso de fallo esperado aquí.

Los handlers específicos también permiten que los errores de programación no relacionados sigan apareciendo en lugar de convertirse silenciosamente en la misma respuesta alternativa.

## 7. Un `try` exitoso omite sus handlers `except`

```python
try:
    score = int("90")
except ValueError:
    print("Invalid score")

print(score)
```

Salida:

```text
90
```

No ocurrió ningún `ValueError`, por lo que el handler se omitió.

## 8. El resto de un bloque `try` se omite después de una excepción

```python
try:
    number = int("seven")
    print("Conversion succeeded")
except ValueError:
    print("Conversion failed")
```

Salida:

```text
Conversion failed
```

Cuando `int("seven")` lanza `ValueError`, Python no continúa con la siguiente instrucción dentro de ese mismo bloque `try`.

El control pasa al handler coincidente.

## 9. Accede al objeto excepción con `as`

Un handler puede vincular la excepción capturada a un nombre local:

```python
try:
    number = int("seven")
except ValueError as error:
    print(type(error).__name__)
```

Salida:

```text
ValueError
```

El nombre después de `as` se refiere al objeto excepción mientras el handler está ejecutándose.

Úsalo cuando el tipo o los detalles de la excepción ayuden realmente con logging, diagnóstico o una explicación para el usuario.

## 10. No construyas lógica basada en el mensaje exacto de la excepción

El texto de una excepción es útil para las personas, pero su redacción exacta puede cambiar entre versiones de Python o detalles de implementación.

Prefiere ramificar según el **tipo** de excepción:

```python
try:
    number = int("seven")
except ValueError:
    print("Invalid integer")
```

en lugar de comprobar si el mensaje contiene una frase concreta.

## 11. Fallos distintos pueden necesitar handlers distintos

Un cálculo puede fallar al convertir el texto o al dividir:

```python
try:
    numerator = float("12")
    denominator = float("0")
    result = numerator / denominator
except ValueError:
    print("Invalid numeric text")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Salida:

```text
Cannot divide by zero
```

Python busca los handlers en orden y ejecuta el primero que coincide con la excepción lanzada.

## 12. El orden de los handlers importa

Las clases de excepción forman una jerarquía. Un handler para una clase base más general también puede coincidir con sus subclases.

Cuando existe un handler específico y otro más amplio, coloca primero el específico:

```python
try:
    value = int(text)
except ValueError:
    print("Invalid integer")
except Exception:
    print("Unexpected application error")
```

Colocar `except Exception` primero haría que el posterior `except ValueError` no pudiera manejar un `ValueError`, porque el handler más amplio ya coincide con él.

## 13. Un handler puede coincidir con una tupla de tipos de excepción

Si varios fallos necesitan realmente la misma respuesta, una cláusula `except` puede nombrar una tupla:

```python
try:
    result = int(text) / divisor
except (ValueError, ZeroDivisionError):
    print("Could not calculate the result")
```

Esto es útil solo cuando el mismo comportamiento de recuperación tiene sentido para todas las excepciones listadas.

Los handlers separados son más claros cuando fallos distintos necesitan explicaciones o rutas de recuperación diferentes.

## 14. `else` describe la ruta exclusiva de éxito

Una instrucción `try` puede incluir `else`:

```python
try:
    score = int("90")
except ValueError:
    print("Invalid score")
else:
    print(f"Parsed score: {score}")
```

Salida:

```text
Parsed score: 90
```

El bloque `else` se ejecuta cuando el bloque `try` termina normalmente sin una excepción y sin una salida anticipada del flujo como `return`, `break` o `continue`.

## 15. ¿Por qué no colocar todo el código de éxito dentro de `try`?

Esto funciona:

```python
try:
    score = int(text)
    print(f"Parsed score: {score}")
except ValueError:
    print("Invalid score")
```

Pero la llamada `print()` no es la operación que esperamos que lance `ValueError`.

Usar `else` puede mantener más pequeña la región protegida:

```python
try:
    score = int(text)
except ValueError:
    print("Invalid score")
else:
    print(f"Parsed score: {score}")
```

Ahora la estructura comunica con más precisión qué operación pertenece al límite de fallo esperado.

## 16. Mantén el bloque `try` pequeño

Un bloque `try` grande puede dificultar saber qué instrucción produjo la excepción.

Prefiere:

```python
try:
    quantity = int(text)
except ValueError:
    print("Invalid quantity")
else:
    total = quantity * unit_price
    print(total)
```

cuando solo se espera que la conversión falle con `ValueError`.

Los bloques `try` pequeños hacen que los límites de excepción sean más fáciles de inspeccionar y reducen la posibilidad de manejar accidentalmente un fallo no relacionado.

## 17. `finally` describe la limpieza que debe ocurrir

Un bloque `finally` se ejecuta cuando se está abandonando la instrucción `try`, tanto si el trabajo protegido tuvo éxito como si se ejecutó un handler coincidente o una excepción no manejada continúa propagándose.

```python
try:
    number = int("12")
except ValueError:
    print("Invalid integer")
finally:
    print("Finished conversion attempt")
```

Salida:

```text
Finished conversion attempt
```

El bloque `finally` trata sobre limpieza y finalización garantizada, no sobre decidir si la operación original tuvo éxito.

## 18. `finally` también se ejecuta después de una excepción manejada

```python
try:
    number = int("twelve")
except ValueError:
    print("Invalid integer")
finally:
    print("Finished conversion attempt")
```

Salida:

```text
Invalid integer
Finished conversion attempt
```

El handler responde al `ValueError`. El bloque `finally` sigue ejecutándose después.

## 19. `finally` también se ejecuta cuando una excepción permanece sin manejar

Conceptualmente:

```python
try:
    result = 10 / 0
finally:
    print("Cleanup runs")
```

`ZeroDivisionError` no se maneja aquí, por lo que sigue propagándose después de que `finally` termina.

La limpieza se ejecuta, pero la excepción no se convierte mágicamente en éxito.

## 20. Combina `try`, `except`, `else` y `finally`

```python
try:
    score = int("90")
except ValueError:
    print("except: invalid score")
else:
    print(f"else: parsed {score}")
finally:
    print("finally: attempt finished")
```

Salida:

```text
else: parsed 90
finally: attempt finished
```

La estructura separa cuatro responsabilidades:

| Cláusula | Responsabilidad |
|---|---|
| `try` | ejecutar trabajo que puede lanzar una excepción esperada |
| `except` | manejar un fallo coincidente |
| `else` | continuar por la ruta exclusiva de éxito |
| `finally` | ejecutar limpieza en todas las rutas de salida |

## 21. Sigue un fallo manejado a través de todas las cláusulas

```python
try:
    score = int("ninety")
except ValueError:
    print("except: invalid score")
else:
    print(f"else: parsed {score}")
finally:
    print("finally: attempt finished")
```

Salida:

```text
except: invalid score
finally: attempt finished
```

Seguimiento:

```text
entrar en try
    ↓
int("ninety") lanza ValueError
    ↓
se ejecuta el except coincidente
    ↓
else se omite
    ↓
finally se ejecuta
    ↓
continuar después de la instrucción try
```

## 22. Si ningún handler coincide, la excepción se propaga

```python
try:
    result = "12" + 3
except ValueError:
    print("Invalid value")
```

La operación lanza `TypeError`, no `ValueError`.

Como el handler no coincide, el `TypeError` continúa hacia afuera en busca de handlers circundantes o, si no existe ninguno, llega al intérprete.

Este comportamiento es útil. Un handler no debe fingir que se recuperó de un fallo que no entiende.

## 23. Las excepciones pueden cruzar límites de funciones

```python
def parse_score(text: str) -> int:
    return int(text)


try:
    score = parse_score("ninety")
except ValueError:
    print("Invalid score")
```

Salida:

```text
Invalid score
```

`parse_score()` no maneja la excepción. El `ValueError` se propaga de vuelta al llamador, donde el llamador decide manejarlo.

Esto conecta el flujo de excepciones directamente con la pila de llamadas estudiada en la Fase 5.

## 24. Decide dónde puede manejarse una excepción de forma significativa

No toda función debe capturar toda excepción que pueda encontrar.

Una pregunta de diseño útil es:

```text
¿Esta capa sabe qué recuperación o explicación tiene sentido?
    sí → el manejo puede pertenecer aquí
    no → deja que la excepción se propague
```

Un helper de parsing de bajo nivel puede dejar simplemente que `ValueError` se propague. Una función coordinadora orientada al usuario puede saber cómo convertir ese fallo en un mensaje útil.

Esto es una recomendación de diseño, no una regla de sintaxis de Python.

## 25. Evita `except:` sin tipo en el manejo normal de aplicaciones

Un handler sin tipo se ve así:

```python
try:
    value = int(text)
except:
    print("Something failed")
```

Captura excepciones derivadas de `BaseException`, directa o indirectamente, incluidas excepciones de control como `KeyboardInterrupt` y `SystemExit` que las aplicaciones normalmente no deberían ocultar accidentalmente.

Para fallos normales de aplicación, captura los tipos específicos de excepción que esperas.

## 26. `except Exception` también es amplio

Esto es más estrecho que un `except:` sin tipo:

```python
try:
    value = int(text)
except Exception:
    print("Operation failed")
```

`Exception` es la clase base común de la mayoría de las excepciones built-in de nivel de aplicación, por lo que todavía puede ocultar muchos bugs no relacionados si se usa sin cuidado.

Un handler amplio puede ser apropiado en un límite deliberado, como una capa superior de logging, pero el código para principiantes normalmente debería comenzar con excepciones específicas esperadas.

## 27. Excepciones built-in comunes que encontrarás

| Excepción | Situación típica para principiantes |
|---|---|
| `ValueError` | un valor tiene el tipo general correcto, pero un valor inválido, como `int("seven")` |
| `TypeError` | una operación recibe un tipo inapropiado, como sumar un string y un entero |
| `ZeroDivisionError` | una división o módulo usa cero como divisor |
| `KeyError` | una consulta de diccionario solicita una clave ausente con `mapping[key]` |
| `IndexError` | un índice de secuencia está fuera del rango disponible |
| `FileNotFoundError` | la ruta solicitada no existe al abrir un archivo |

El objetivo no es memorizar ahora todas las excepciones built-in. Aprende a leer el tipo de excepción y entender qué operación lo produjo.

## 28. Las excepciones y la validación son herramientas diferentes

A veces una condición simple puede evitar una operación inválida:

```python
if denominator == 0:
    print("Cannot divide by zero")
else:
    print(numerator / denominator)
```

Otras veces una API señala naturalmente el fallo lanzando una excepción:

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

No conviertas esto en una regla rígida de que las excepciones son siempre mejores o siempre peores que la validación.

Elige el límite más claro para la operación y la API que estés usando.

## 29. Un handler debe definir una ruta real de recuperación

Este código captura un error, pero no proporciona información útil al llamador:

```python
try:
    number = int(text)
except ValueError:
    pass
```

La excepción desaparece silenciosamente.

El manejo silencioso es peligroso cuando el programa continúa con un estado incompleto o incorrecto.

Prefiere un handler que retorne deliberadamente un fallback, solicite nueva entrada en un programa interactivo, registre el fallo o comunique lo ocurrido.

## 30. Retornar un fallback puede ser un contrato explícito

```python
def parse_integer(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None
```

Aquí `None` significa explícitamente que el parsing no produjo un entero.

El llamador debe manejar entonces ambos resultados posibles:

```python
result = parse_integer("seven")

if result is None:
    print("Invalid integer")
else:
    print(result)
```

Esto combina el manejo de excepciones con el modelo de flujo de datos con `None` de la Fase 5.

## 31. Ejemplo práctico: división segura a partir de texto

```python
def safe_divide(numerator_text: str, denominator_text: str) -> str:
    try:
        numerator = float(numerator_text)
        denominator = float(denominator_text)
        result = numerator / denominator
    except ValueError:
        return "invalid number"
    except ZeroDivisionError:
        return "division by zero"
    else:
        return f"result: {result:.2f}"
```

Llamadas de ejemplo:

```python
print(safe_divide("12", "4"))
print(safe_divide("twelve", "4"))
print(safe_divide("12", "0"))
```

Salida:

```text
result: 3.00
invalid number
division by zero
```

La función distingue un fallo de conversión de un fallo aritmético y retorna un resultado determinista para cada ruta esperada.

## 32. Los bucles pueden manejar un elemento malo sin descartar todos los buenos

```python
values = ["10", "twenty", "30"]
parsed_values = []

for text in values:
    try:
        parsed_values.append(int(text))
    except ValueError:
        print(f"Skipped invalid value: {text}")

print(parsed_values)
```

Salida:

```text
Skipped invalid value: twenty
[10, 30]
```

El handler está dentro del bucle porque cada elemento es un intento independiente de conversión.

Esto es diferente de envolver todo el bucle en un gran bloque `try`, donde el primer elemento inválido podría interrumpir las iteraciones restantes.

## 33. Mantén los efectos secundarios después del trabajo riesgoso exitoso cuando sea posible

Supón que una operación puede fallar durante el parsing. Suele ser más claro hacer el parsing primero y actualizar el estado compartido solo después del éxito:

```python
try:
    quantity = int(text)
except ValueError:
    print("Invalid quantity")
else:
    quantities.append(quantity)
```

Esto reduce la posibilidad de dejar un estado parcialmente actualizado después de un fallo.

## 34. `finally` no es un buen lugar para `return`

Un `return` dentro de `finally` puede reemplazar un valor de retorno anterior e incluso suprimir una excepción que se estaba propagando.

Evita este patrón:

```python
def calculate() -> int:
    try:
        return 10 // 0
    finally:
        return 0
```

El `return` de `finally` oculta el `ZeroDivisionError`.

Usa `finally` para limpieza. Mantén las decisiones normales de retorno en las rutas normal, manejada o de éxito.

## 35. El futuro manejo de archivos normalmente preferirá `with`

`finally` es una herramienta general de limpieza. En el capítulo de archivos aprenderás que la instrucción `with` empaqueta patrones comunes de gestión de recursos en una interfaz más clara.

Por ejemplo, los archivos normalmente se gestionan mediante un context manager en lugar de reproducir manualmente todas las rutas de limpieza.

Ese capítulo posterior se apoya directamente en la idea de limpieza introducida aquí.

## 36. Error común: capturar el tipo de excepción equivocado

```python
try:
    result = 10 / 0
except ValueError:
    print("Invalid value")
```

Esto no maneja el fallo porque dividir por cero lanza `ZeroDivisionError`.

Lee el traceback y haz que el handler corresponda al fallo real del que quieres recuperarte.

## 37. Error común: hacer enorme el bloque `try`

```python
try:
    quantity = int(text)
    total = quantity * unit_price
    report = build_report(total)
    save_result(report)
except ValueError:
    print("Invalid quantity")
```

Si una operación posterior también puede lanzar `ValueError`, el handler podría tratar accidentalmente otro bug como si fuera una entrada inválida del usuario.

Protege la región práctica más pequeña cuyas fallas esperadas comprendas.

## 38. Error común: ocultar todas las excepciones

```python
try:
    process_data()
except Exception:
    pass
```

Esto puede ocultar errores de programación, suposiciones inválidas e información importante de diagnóstico.

El manejo solo es útil cuando el programa tiene una respuesta deliberada al fallo.

## 39. Error común: usar excepciones como ramificación invisible

El manejo de excepciones debería hacer más claros los límites de fallo, no convertir decisiones ordinarias en un laberinto.

Si una condición ya es conocida y sencilla de comprobar, un `if` normal puede comunicar mejor la decisión.

Si una operación informa naturalmente el fallo mediante una excepción, manejar esa excepción puede ser el diseño más claro.

## 40. Error común: asumir que `finally` significa éxito

`finally` significa que la ruta de limpieza se ejecuta. No dice nada sobre el éxito.

```text
éxito                 → finally se ejecuta
excepción manejada     → finally se ejecuta
excepción no manejada  → finally se ejecuta y luego la excepción continúa
```

Mantén el trabajo exclusivo de éxito en `else` o después de una operación completada correctamente.

## 41. Ejercicio

Construye un pequeño parser de puntuaciones que maneje texto inválido de forma segura.

Requisitos:

1. Crea `parse_score(text: str) -> int | None`.
2. Dentro de la función, intenta convertir `text` con `int()`.
3. Captura `ValueError` y retorna `None`.
4. Usa una cláusula `else` para retornar el entero convertido correctamente.
5. Crea una lista con al menos tres strings, incluyendo un entero inválido.
6. Recorre la lista y llama a `parse_score()` para cada elemento.
7. Imprime un mensaje claro para valores inválidos e imprime el entero para valores válidos.
8. Añade un bloque `finally` dentro de `parse_score()` que imprima un mensaje corto y determinista de limpieza para cada intento.
9. Antes de ejecutar el código, dibuja las rutas posibles a través de `try`, `except`, `else` y `finally`.

Desafío adicional: decide si imprimir desde `finally` pertenece al diseño final o si debería eliminarse después de terminar el seguimiento del ejercicio.

## 42. Lista de revisión

Ahora deberías poder responder:

- ¿Cuál es la diferencia entre sintaxis Python inválida y una excepción de runtime?
- ¿Qué ocurre con las instrucciones restantes de un bloque `try` después de que se lanza una excepción?
- ¿Por qué normalmente debe preferirse `except ValueError` a un `except:` sin tipo cuando `ValueError` es el fallo esperado?
- ¿Cuándo se ejecuta una cláusula `else`?
- ¿Cuándo se ejecuta una cláusula `finally`?
- ¿Qué ocurre cuando ninguna cláusula `except` coincide?
- ¿Por qué un bloque `try` grande puede ocultar el origen real de un fallo?
- ¿Por qué importa el orden de los handlers?
- ¿Qué captura ampliamente `except Exception` y por qué debe usarse deliberadamente?
- ¿Por qué el código debería evitar depender de la redacción exacta de los mensajes de excepción?
- ¿Cómo puede una función dejar que una excepción se propague hacia un llamador que sabe manejarla?
- ¿Cómo se conecta el flujo de excepciones con la pila de llamadas de función?

## 43. Resumen de consulta rápida

| Situación | Enfoque útil |
|---|---|
| Una operación puede lanzar una excepción esperada | `try` pequeño + `except` específico |
| Fallos distintos necesitan respuestas diferentes | cláusulas `except` separadas |
| Varios tipos de excepción comparten una respuesta | tupla en una cláusula `except` |
| Necesitas el objeto de excepción capturado | `except SomeError as error` |
| El trabajo debe ejecutarse solo después de un `try` exitoso | `else` |
| La limpieza debe ocurrir en todas las rutas de salida | `finally` |
| Ningún handler entiende el fallo | deja que la excepción se propague |
| El handler captura demasiado | reduce el tipo de excepción o el bloque `try` |
| Necesitas ramificar por el texto exacto del error | evítalo; ramifica por el tipo de excepción |
| Necesitas crear una excepción deliberadamente | Capítulo 02: `raise` y excepciones personalizadas |

## 44. Límite de alcance de este capítulo

Este capítulo deliberadamente **no** enseña todavía en profundidad:

- `raise` y creación explícita de excepciones;
- clases de excepción personalizadas;
- encadenamiento de excepciones con `raise ... from ...`;
- grupos de excepciones y `except*`;
- apertura de archivos y context managers;
- logging de tracebacks de excepciones;
- estrategias avanzadas de retry.

Estas ideas resultan más fáciles cuando el modelo básico de handlers ya está firme.

## 45. Hacia dónde continúa la Fase 7

La secuencia comienza así:

```text
operación en runtime
        ↓
puede ocurrir una excepción
        ↓
try / except / else / finally
        ↓
siguiente: lanzar excepciones deliberadamente con raise
        ↓
archivos y datos estructurados
        ↓
módulos y paquetes
```

Próximo capítulo planificado: **Lanzar Excepciones y Excepciones Personalizadas**.

## Referencias oficiales

- [Python 3.13 Tutorial: Errors and Exceptions](https://docs.python.org/3.13/tutorial/errors.html)
- [Python 3.13 Language Reference: The `try` statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-try-statement)
- [Python 3.13 Execution Model: Exceptions](https://docs.python.org/3.13/reference/executionmodel.html#exceptions)
- [Python 3.13 Built-in Exceptions](https://docs.python.org/3.13/library/exceptions.html)