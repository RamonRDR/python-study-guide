<div align="center">

# Comentarios en Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Los comentarios ayudan a quien lee a comprender decisiones, restricciones y contextos que no son evidentes solamente a partir del código. Son valiosos cuando conservan un razonamiento. Se convierten en ruido cuando solo repiten lo que el código ya dice.

> **Principio orientador:** El código debe explicar qué sucede. Los comentarios deben explicar por qué sucede cuando la razón no es evidente.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante |
| Requisitos previos | Una familiaridad básica con variables y condicionales ayuda, pero no es obligatoria |
| Tiempo estimado de estudio | 35 a 50 minutos |
| Conceptos principales | `#`, comentarios de bloque, comentarios en línea, contexto útil, comentarios desactualizados, `TODO`, `FIXME`, `NOTE` |

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías ser capaz de:

- reconocer la sintaxis de los comentarios en Python;
- diferenciar comentarios, cadenas y docstrings;
- explicar cuándo un comentario aporta información útil;
- identificar comentarios que solo narran código evidente;
- escribir comentarios sobre decisiones, restricciones, límites y reglas de negocio ficticias;
- utilizar `TODO`, `FIXME` y `NOTE` como convenciones claras de un proyecto;
- elegir entre un comentario, un nombre mejor, una docstring, documentación o logging;
- revisar comentarios considerando exactitud, claridad, privacidad y vigencia.

## 1. Qué es un comentario

Un comentario en Python comienza con el carácter de almohadilla (`#`) que no esté dentro de un literal de cadena y continúa hasta el final de la línea física.

```python
# This entire line is a comment.
message = "Hello"  # This is an inline comment.
```

Los comentarios normalmente son ignorados por la sintaxis de Python y no cambian el resultado del programa. Los comentarios con formatos especiales todavía pueden ser leídos por el decodificador del código fuente o por herramientas externas, como se explica más adelante.

```python
score = 80
# score = 100
print(score)
```

Salida:

```text
80
```

La asignación comentada no se ejecuta.

### Una almohadilla dentro de una cadena no es un comentario

```python
label = "Ticket #42"
print(label)
```

El carácter `#` forma parte de la cadena porque aparece entre comillas.

### Comentarios con una finalidad especial

Algunos comentarios siguen convenciones que proporcionan información al decodificador del código fuente de Python, al sistema operativo o a herramientas de desarrollo. Algunos ejemplos:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
value = load_value()  # type: ignore[assignment]
```

- Un *shebang* en la primera línea puede ayudar a los sistemas operativos similares a Unix a elegir un intérprete cuando el archivo se ejecuta directamente.
- Una declaración de codificación válida en la primera o segunda línea indica a Python cómo decodificar el archivo fuente. Python 3 utiliza UTF-8 de forma predeterminada cuando no existe una declaración.
- Directivas como `# type: ignore`, `# noqa` o marcadores de formato pueden ser consumidas por verificadores de tipos, linters o formateadores. El comportamiento exacto pertenece a la herramienta correspondiente, no a la ejecución común de comentarios.

Utiliza directivas de herramientas solamente cuando sean necesarias, específicas y comprensibles. Explica o enlaza la razón cuando una supresión pueda ocultar un problema real.

## 2. Por qué existen los comentarios

El código puede expresar operaciones con precisión, pero no siempre puede conservar la razón detrás de una decisión.

Considera esta condición:

```python
if days_before_event >= 14:
    apply_discount()
```

El código muestra la regla, pero no responde preguntas como:

- ¿Por qué el límite es de 14 días?
- ¿El decimocuarto día está incluido de manera intencional?
- ¿Se trata de una limitación técnica o de una regla ficticia?
- ¿El operador podría cambiarse de `>=` a `>` de manera segura?

Un comentario útil puede conservar ese contexto ausente:

```python
# The fictional policy includes the fourteenth day in the discount window.
if days_before_event >= 14:
    apply_discount()
```

El comentario protege la razón detrás de la comparación. Ayuda a evitar un cambio futuro que parezca inofensivo, pero modifique la regla prevista.

## 3. Sintaxis y formas

### Comentarios de una línea

Un comentario puede ocupar una línea completa:

```python
# Convert the temperature only after validating the selected scale.
temperature_celsius = convert_temperature(user_value)
```

PEP 8 recomienda un espacio después de `#` en los comentarios normales escritos como texto.

```python
# Clear and conventional.
```

Evita:

```python
#Harder to read.
```

### Comentarios en línea

Un comentario en línea aparece junto a una instrucción:

```python
remaining_attempts -= 1  # The first attempt was already recorded.
```

PEP 8 recomienda utilizar este formato con moderación, separar el comentario de la instrucción con al menos dos espacios y escribir `# ` antes del texto.

Los comentarios en línea son más útiles cuando una razón breve pertenece directamente a una instrucción. Cuando la explicación sea larga, utiliza un comentario de bloque encima del código correspondiente.

### Comentarios de bloque

Un comentario de bloque está formado por líneas consecutivas de comentarios y normalmente explica el código que aparece a continuación.

```python
# The data source returns an empty value for days with no measurements.
# Treat that value as missing data instead of converting it to zero, because
# zero is a valid measurement in this fictional example.
measurement = read_measurement()
```

Mantén el comentario en el mismo nivel de indentación que el código que describe:

```python
if measurement is None:
    # Missing measurements are reported separately from valid zero values.
    record_missing_measurement()
```

### Python no posee una sintaxis específica para comentarios de varias líneas

Python no tiene un delimitador separado como `/* ... */` para comentarios de varias líneas. Utiliza varias líneas que comiencen con `#`:

```python
# This is a block comment.
# Each physical line begins with a hash.
```

Las cadenas con comillas triples son literales de cadena, no comentarios de varias líneas:

```python
"""This is a string literal, not comment syntax."""
```

Cuando un literal de cadena es la primera instrucción de un módulo, función, clase o método, se convierte en una docstring y queda disponible por medio de `__doc__`. Las docstrings se explicarán por separado en esta sección de la guía.

## 4. Cuándo utilizar comentarios

### Explica una razón que no sea evidente

```python
# Retry once because the fictional simulator may need one cycle to become ready.
max_retries = 1
```

La asignación es sencilla. La razón del límite no lo es.

### Conserva una regla de negocio ficticia

```python
# The fictional policy includes the registration date in the seven-day window.
if elapsed_days <= 7:
    allow_change = True
```

El comentario explica la interpretación prevista del límite. No afirma que la regla pertenezca a una organización real.

### Documenta una restricción técnica

```python
# Keep the file name in ASCII because the external teaching tool used in this
# example rejects non-ASCII paths.
output_name = "summary.txt"
```

El comentario registra una restricción que puede no ser visible solamente a partir de la asignación.

### Explica una solución temporal o alternativa

```python
# Iterate over a copy because approved items are removed from the original.
for item in pending_items.copy():
    if is_approved(item):
        pending_items.remove(item)
```

Un comentario sobre una solución alternativa debe explicar el riesgo que se evita. Siempre que sea posible, incluye un enlace a una issue pública o a una página de documentación que permita verificar en el futuro si la solución continúa siendo necesaria.

### Aclara unidades o interpretaciones cuando el nombre no sea suficiente

```python
poll_interval = 30  # Seconds required by the fictional simulator.
```

Un nombre mejor puede eliminar la necesidad del comentario:

```python
poll_interval_seconds = 30
```

Prefiere el nombre más claro, a menos que la razón del valor todavía necesite una explicación.

## 5. Cuándo evitar comentarios

### No narres código evidente

```python
# Add one to the counter.
counter += 1
```

El comentario repite la operación sin aportar contexto.

Una versión útil explicaría una razón que el código no revela:

```python
# Count the restored session as an attempt so retry limits remain consistent.
counter += 1
```

### No utilices comentarios para reparar nombres poco claros

Evita:

```python
x = 14  # Number of days required for the early-registration discount.
```

Prefiere:

```python
early_registration_days = 14
```

Utiliza un comentario solamente cuando el nombre todavía no pueda explicar la razón o el límite:

```python
early_registration_days = 14

# The fictional policy includes the fourteenth day in the discount window.
if days_before_event >= early_registration_days:
    apply_discount()
```

### No conserves código desactivado sin una razón

Evita dejar bloques grandes de código comentado:

```python
# old_total = subtotal * 1.15
# print(old_total)
```

El control de versiones ya conserva implementaciones anteriores. Elimina el código obsoleto, excepto cuando exista una razón específica, temporal y documentada para conservarlo.

### No escribas comentarios que puedan volverse falsos silenciosamente

```python
# Retry three times.
max_retries = 5
```

La contradicción es más peligrosa que no tener comentario. Actualiza o elimina los comentarios siempre que cambie el código relacionado.

### Nunca coloques secretos o información privada en comentarios

Los comentarios se almacenan en los archivos fuente y pueden ser versionados, copiados, indexados o publicados.

Nunca incluyas:

- contraseñas, tokens, claves de API o URL privadas;
- datos personales o de clientes;
- reglas o flujos confidenciales;
- detalles privados de empleadores, clientes, proyectos personales o familiares;
- código propietario copiado o explicaciones internas.

Crea ejemplos ficticios y originales desde el principio.

## 6. Comentarios y código autoexplicativo

Los comentarios no son la primera solución para todos los problemas de legibilidad.

Compara:

```python
# Check whether the user can access the event.
if a and not b and c:
    grant_access()
```

Con nombres más claros:

```python
has_ticket = True
is_blocked = False
event_is_open = True

if has_ticket and not is_blocked and event_is_open:
    grant_access()
```

La segunda versión reduce la necesidad de explicación porque los nombres exponen las condiciones.

Un orden útil para tomar decisiones es:

1. ¿Puede simplificarse el código?
2. ¿Puede un nombre expresar el significado?
3. ¿Puede una función pequeña expresar la intención?
4. ¿Todavía falta un razonamiento importante?
5. Añade un comentario para ese razonamiento restante.

Un comentario debe complementar código claro, no servir como excusa para código confuso.

## 7. Comentarios, docstrings, documentación y logging

Estas herramientas resuelven problemas diferentes.

| Recurso | Objetivo principal | Público habitual | ¿Está disponible durante la ejecución? |
|---|---|---|---|
| Comentario | Explicar decisiones o contextos no evidentes en el código fuente | Personas que mantienen o estudian el código fuente | No por medio de la documentación normal de objetos |
| Docstring | Describir el propósito y el uso público de un módulo, función, clase o método | Personas que utilizan el código y responsables del mantenimiento | Sí, por medio de `__doc__` y herramientas como `help()` |
| README o guía | Explicar instalación, conceptos, flujos y usos más amplios | Estudiantes, colaboradores y usuarios | No forma parte del comportamiento del programa |
| Logging | Registrar eventos, advertencias, fallos y contexto de diagnóstico durante la ejecución | Operaciones, desarrollo y soporte | Sí |
| Type hint | Expresar tipos esperados y ayudar a lectores y herramientas de análisis | Desarrolladores, estudiantes, editores y verificadores de tipos | En muchos casos se almacena en las anotaciones, pero Python no lo aplica automáticamente |

### Comentario frente a docstring

Utiliza un comentario para explicar una decisión de implementación:

```python
# Preserve input order because the teaching report compares rows visually.
ordered_names = list(names)
```

Utiliza una docstring para explicar qué ofrece una función reutilizable:

```python
def calculate_average(values):
    """Return the arithmetic mean of the provided values."""
```

### Comentario frente a logging

Un comentario no puede registrar lo que ocurrió durante una ejecución específica:

```python
# The file failed to open.
```

Esa frase no observa el comportamiento durante la ejecución. El logging puede registrar el evento cuando ocurra:

```python
logger.error("Could not open the configuration file")
```

No reemplaces los diagnósticos de ejecución con comentarios.

## 8. Ejemplo básico

Comentario innecesario:

```python
# Multiply the price by the quantity.
total = price * quantity
```

Mejor sin el comentario:

```python
total = price * quantity
```

Comentario útil:

```python
# The fictional exercise stores prices in cents to keep all calculations in
# integers and avoid introducing decimal arithmetic in this beginner chapter.
total_cents = price_cents * quantity
```

El último comentario explica una decisión didáctica y de diseño, no la multiplicación en sí.

## 9. Ejemplo práctico

```python
from datetime import date

EARLY_REGISTRATION_DAYS = 14
EARLY_DISCOUNT_PERCENT = 10


def calculate_registration_fee(
    base_fee_cents,
    event_date,
    registration_date,
):
    days_before_event = (event_date - registration_date).days

    # The fictional policy includes the fourteenth day in the discount window,
    # so this comparison must remain inclusive.
    if days_before_event >= EARLY_REGISTRATION_DAYS:
        discount_cents = base_fee_cents * EARLY_DISCOUNT_PERCENT // 100
        return base_fee_cents - discount_cents

    return base_fee_cents
```

El comentario es útil porque:

- el código ya muestra que se utiliza `>=`;
- el comentario explica por qué importa el caso de igualdad;
- la palabra *ficticia* evita que el ejemplo se confunda con una política real;
- quien mantenga el código en el futuro sabrá que cambiar `>=` por `>` modificaría la regla prevista.

Consulta el ejemplo ejecutable completo en [`examples/business_rule_comments.py`](examples/business_rule_comments.py).

## 10. `TODO`, `FIXME` y `NOTE`

Python no asigna un comportamiento incorporado a estas etiquetas. Son convenciones humanas y de herramientas utilizadas por muchos proyectos.

### `TODO`

Utiliza `TODO` para una mejora específica que todavía debe completarse.

Débil:

```python
# TODO: Improve this.
```

Mejor:

```python
# TODO: Replace the linear search after the catalog exceeds 10,000 items.
```

Un buen `TODO` explica qué debe cambiar y, cuando sea útil, la condición que vuelve necesario el cambio. Los proyectos también pueden incluir un número de issue o una persona responsable, según su propia política.

### `FIXME`

Utiliza `FIXME` para un comportamiento conocido que sea incorrecto, inseguro o incompleto y requiera una corrección.

```python
# FIXME: Preserve leading zeros when postal codes are loaded from CSV.
```

Un `FIXME` no sustituye el registro de un defecto serio. Sigue el proceso de issues y seguridad del proyecto cuando el impacto lo requiera.

### `NOTE`

Utiliza `NOTE` para un contexto importante que podría pasar desapercibido para quien mantiene el código.

```python
# NOTE: The sample data is intentionally unsorted for the ordering exercise.
```

No conviertas cada observación en una `NOTE`. Reserva el marcador para información que afecte de manera significativa la comprensión o el mantenimiento.

## 11. Errores comunes

### Explicar qué sucede en lugar de explicar por qué

```python
# Check whether the value is greater than zero.
if value > 0:
    process(value)
```

La condición ya explica la operación.

### Escribir una novela junto a código simple

Un comentario largo puede ocultar un problema de diseño. Cuando la explicación sea extensa, considera extraer una función, simplificar el código o mover la documentación más amplia a una guía.

### Referirse al código por una posición frágil

Evita:

```python
# The loop below changes the list used on line 42.
```

Los números de línea y las posiciones cambian. Haz referencia a nombres y conceptos estables.

### Utilizar un comentario como lista de tareas sin contexto

```python
# TODO: Later.
```

Esto no indica qué falta, por qué importa o cómo reconocer que la tarea se completó.

### Comentar cada línea

Los comentarios excesivos obligan a quien lee a procesar dos versiones de la misma lógica. Comenta solamente cuando la segunda voz aporte algo que la primera no pueda expresar con claridad.

### Confiar más en el comentario que en el código

El programa ejecuta el código, no la explicación. Cuando no coincidan, investiga el comportamiento previsto, las pruebas y los requisitos antes de modificar cualquiera de los dos.

## 12. Ejemplos en este repositorio

| Archivo | Objetivo |
|---|---|
| [`useful_comments.py`](examples/useful_comments.py) | Muestra un comentario que explica una decisión de programación no evidente |
| [`unnecessary_comments.py`](examples/unnecessary_comments.py) | Compara la narración línea por línea con código más claro |
| [`business_rule_comments.py`](examples/business_rule_comments.py) | Conserva el límite de una regla ficticia y original |

Ejecuta un ejemplo desde la raíz del repositorio:

```bash
python comments-and-documentation/01-comments/examples/useful_comments.py
```

En sistemas donde el comando se llama `python3`:

```bash
python3 comments-and-documentation/01-comments/examples/useful_comments.py
```

## 13. Ejercicio

Revisa este código:

```python
# Set the maximum number of attempts.
max_attempts = 3

# Set attempts to zero.
attempts = 0

# Loop while attempts is less than max attempts.
while attempts < max_attempts:
    # Print the attempt number.
    print(attempts + 1)

    # Add one to attempts.
    attempts += 1
```

Completa las siguientes tareas:

1. Elimina los comentarios que solo repiten el código.
2. Cambia los nombres de las variables solamente cuando un nombre más claro sea realmente necesario.
3. Añade una razón ficticia y útil para el límite de tres intentos.
4. Confirma que el código revisado produce la misma salida.
5. Explica con tus propias palabras por qué el comentario restante aporta información.

Una posible revisión:

```python
max_attempts = 3
attempts = 0

# The fictional practice terminal allows three tries before showing a hint.
while attempts < max_attempts:
    print(attempts + 1)
    attempts += 1
```

Esta no es la única respuesta válida. La pregunta importante es si el comentario conserva un contexto que el código no puede expresar por sí solo.

## 14. Lista de revisión de comentarios

Antes de conservar o añadir un comentario, pregunta:

- ¿La información es verdadera?
- ¿El código ya dice lo mismo con claridad?
- ¿Un nombre mejor o una función más pequeña podría eliminar la necesidad del comentario?
- ¿El comentario explica una razón, restricción, límite, riesgo o decisión?
- ¿Un cambio futuro podría hacer que este comentario sea fácil de olvidar o contradecir?
- ¿El lenguaje es claro para el público previsto?
- ¿Contiene información privada, propietaria, personal o identificable?
- Cuando sea necesario, ¿la explicación puede verificarse en una fuente o issue pública?

## 15. Resumen de consulta rápida

| Situación | Enfoque preferido |
|---|---|
| El código no es claro porque los nombres son vagos | Mejora primero los nombres |
| Una decisión no es evidente a partir del código | Añade un comentario breve que explique la razón |
| Una regla ficticia tiene un límite importante | Comenta la interpretación prevista |
| Una solución alternativa depende de una limitación externa | Explica la limitación y, cuando sea posible, enlaza una fuente pública |
| Un comentario repite la instrucción | Elimina el comentario |
| Código antiguo está comentado | Elimínalo y utiliza el control de versiones |
| Una función pública necesita documentación de uso | Escribe una docstring |
| Debe registrarse un comportamiento de ejecución | Utiliza logging |
| Un trabajo futuro es específico y accionable | Utiliza un `TODO` claro según la política del proyecto |
| Un comportamiento conocido es incorrecto | Utiliza `FIXME` y sigue el proceso de defectos del proyecto |
| Un contexto puede pasar desapercibido | Utiliza `NOTE` con moderación |

## Referencias oficiales

- [Análisis léxico de Python: comentarios](https://docs.python.org/es/3/reference/lexical_analysis.html#comments)
- [PEP 8: comentarios](https://peps.python.org/pep-0008/#comments)
- [PEP 257: convenciones de docstrings](https://peps.python.org/pep-0257/)

## Principio final

Un comentario útil deja el código más fácil de comprender después de que la persona procesa ambos. Si eliminar el comentario no cambia nada en la comprensión, probablemente el código no lo necesitaba.
