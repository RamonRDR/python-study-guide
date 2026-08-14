<div align="center">

# Funciones Trabajando Juntas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Funciones](../README.es.md) · [← Anterior: `*args` y `**kwargs`](../07-args-and-kwargs/README.es.md)

Un programa útil rara vez depende de una sola función gigante. Con más frecuencia, varias funciones pequeñas **dividen el trabajo, se llaman entre sí y conectan sus resultados**.

Este capítulo convierte los recursos de funciones de los capítulos anteriores en un modelo de composición. El objetivo no es crear tantas funciones como sea posible. El objetivo es dar a cada parte significativa del trabajo un papel claro y después conectar esos papeles de forma deliberada.

**Tiempo estimado de estudio:** 90–120 minutos.

## Objetivos de aprendizaje

Al final de este capítulo deberías poder:

- llamar una función definida por el usuario desde otra;
- usar un valor retornado como entrada de la siguiente función;
- explicar qué ocurre con la función llamadora mientras otra función ordinaria se está ejecutando;
- distinguir una función auxiliar enfocada de una función coordinadora;
- separar cálculo de presentación cuando eso mejora la reutilización;
- mantener las dependencias visibles mediante parámetros y valores de retorno;
- reconocer cuándo una variable global está ocultando el flujo de datos;
- usar variables intermedias para que una cadena de llamadas sea más fácil de seguir;
- leer un grafo simple de llamadas;
- combinar funciones con condiciones y bucles;
- reconocer lógica duplicada que debería convertirse en una función auxiliar reutilizable;
- evitar dividir una operación sencilla en funciones diminutas innecesarias;
- identificar efectos secundarios ocultos que dificultan razonar sobre la colaboración;
- prepararte para el tratamiento más profundo del flujo de datos entre llamadas del siguiente capítulo.

## 1. Por qué las funciones necesitan colaborar

Los capítulos anteriores aislaron habilidades individuales de funciones:

```text
define behavior
receive inputs
return outputs
control scope
describe types
provide defaults
collect flexible arguments
```

Los programas reales conectan esas habilidades.

Una tarea mayor, como preparar un resumen de estudio, puede contener naturalmente tareas más pequeñas:

```text
session durations
      ↓
calculate total minutes
      ↓
classify workload
      ↓
build readable summary
```

Cada etapa puede convertirse en una función cuando separarla hace que el programa sea más fácil de entender, probar, reutilizar o modificar.

## 2. Una función puede llamar a otra

Una llamada de función puede aparecer dentro de otra función igual que otras expresiones e instrucciones.

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


def build_greeting(name: str) -> str:
    clean_name = normalize_name(name)
    return f"Welcome, {clean_name}!"


print(build_greeting("  ava stone  "))
```

Salida:

```text
Welcome, Ava Stone!
```

La relación importante es:

```text
build_greeting()
      ↓ calls
normalize_name()
      ↓ returns
clean_name
```

`build_greeting()` no necesita repetir la lógica de normalización. Delega esa parte a `normalize_name()`.

## 3. La función llamadora espera a que termine la función llamada

Para una llamada de función ordinaria en este capítulo, la ejecución entra en la función llamada. Cuando esa llamada termina, la ejecución continúa en la función llamadora.

Sigue este ejemplo:

```python
def double(number: int) -> int:
    return number * 2


def add_one_after_doubling(number: int) -> int:
    doubled = double(number)
    return doubled + 1


print(add_one_after_doubling(5))
```

El orden es:

```text
1. call add_one_after_doubling(5)
2. enter add_one_after_doubling()
3. call double(5)
4. enter double()
5. return 10
6. continue inside add_one_after_doubling()
7. return 11
8. print 11
```

La función externa no continúa más allá de `double(number)` hasta que esa llamada haya producido su resultado.

## 4. Los valores de retorno son puntos naturales de conexión

Un valor de retorno permite que una función termine su responsabilidad y entregue un resultado a otra parte del programa.

```python
def calculate_area(width: int, height: int) -> int:
    return width * height


def format_area(area: int) -> str:
    return f"Area: {area}"


area = calculate_area(6, 4)
message = format_area(area)
print(message)
```

Salida:

```text
Area: 24
```

Las dos funciones tienen trabajos diferentes:

```text
calculate_area() → produce a number
format_area()    → turn a number into text
```

Esa separación hace que cada resultado sea más fácil de reutilizar.

## 5. Usa nombres intermedios cuando mejoren la historia

Python permite llamadas anidadas:

```python
def calculate_area(width: int, height: int) -> int:
    return width * height


def format_area(area: int) -> str:
    return f"Area: {area}"


print(format_area(calculate_area(6, 4)))
```

Esto es válido. Antes de que `format_area()` pueda ejecutarse, Python evalúa `calculate_area(6, 4)` para obtener el valor del argumento.

Para principiantes, esta versión puede ser más fácil de seguir:

```python
area = calculate_area(6, 4)
message = format_area(area)
print(message)
```

Prefiere la versión que haga más fácil entender el movimiento de los datos. Menos líneas no significa automáticamente código más claro.

## 6. Piensa en responsabilidades

Imagina una función que recibe una puntuación, decide su categoría, formatea una frase y la imprime.

Eso puede ser aceptable en un script pequeño de un solo uso. Pero si la lógica de categoría o el formato se reutilizarán, separar responsabilidades puede ayudar.

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"
```

Ahora cada función responde una pregunta clara:

```text
classify_score()      → What category does this score belong to?
format_score_report() → How should these already-known values be displayed?
```

## 7. Una función coordinadora puede conectar auxiliares

Una función más grande puede coordinar funciones más pequeñas sin duplicar su trabajo.

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"


def build_score_report(student: str, score: int) -> str:
    status = classify_score(score)
    return format_score_report(student, score, status)


print(build_score_report("Ava", 84))
```

Salida:

```text
Ava: 84 points - ready
```

En esta guía podemos llamar a `classify_score()` y `format_score_report()` **funciones auxiliares**, mientras `build_score_report()` actúa como **coordinadora** u **orquestadora**.

Esas palabras describen papeles de diseño. No son sintaxis especial de Python.

## 8. Una responsabilidad es una guía de diseño, no una regla de Python

Python no exige que cada función realice exactamente una acción diminuta.

Esta función no es inválida:

```python
def build_label(name: str, quantity: int) -> str:
    clean_name = name.strip().title()
    return f"{clean_name} x{quantity}"
```

La pregunta útil no es:

> ¿Esta función tiene más de una línea?

Pregunta:

> ¿Esta función representa una responsabilidad comprensible al nivel que necesita este programa?

Dividir código debería mejorar claridad, reutilización, pruebas o mantenimiento. Dividir solo para crear más nombres de funciones puede hacer el programa más difícil de seguir.

## 9. Separa cálculo de presentación cuando la reutilización importe

Imprimir es útil, pero un valor que solo se imprime no puede ser reutilizado directamente por la función llamadora.

Menos reutilizable:

```python
def show_total(values: list[int]) -> None:
    total = sum(values)
    print(f"Total: {total}")
```

Más reutilizable cuando quien llama necesita el número:

```python
def calculate_total(values: list[int]) -> int:
    return sum(values)


def format_total(total: int) -> str:
    return f"Total: {total}"
```

Ahora una parte del programa puede imprimir el resultado formateado mientras otra puede usar el total numérico en otro cálculo.

Esta es una recomendación de diseño, no una regla que diga que imprimir dentro de funciones siempre está mal.

## 10. Haz visibles las dependencias mediante parámetros

Si una función necesita datos de otra parte del programa, los parámetros hacen visible esa dependencia.

```python
def calculate_bonus(points: int) -> int:
    return points // 10


def build_result(name: str, points: int) -> str:
    bonus = calculate_bonus(points)
    return f"{name}: {points} points + {bonus} bonus"
```

Quien lea `build_result(name, points)` puede ver inmediatamente qué valores necesita.

Las entradas visibles hacen que las funciones sean más fáciles de entender de forma aislada.

## 11. Evita usar variables globales como coordinación oculta

Esto funciona, pero la dependencia queda oculta:

```python
points = 80


def calculate_bonus() -> int:
    return points // 10
```

Una interfaz más clara es:

```python
def calculate_bonus(points: int) -> int:
    return points // 10
```

La segunda versión declara directamente lo que necesita.

Las variables globales pueden ser apropiadas para algunas constantes a nivel del programa y otros diseños deliberados. La advertencia aquí se refiere específicamente a usar estado global compartido como sustituto invisible de parámetros y valores de retorno ordinarios.

## 12. Reutiliza auxiliares en lugar de copiar lógica

Imagina que varios informes necesitan la misma clasificación de puntuación.

Duplicar las condiciones crea varios lugares que pueden alejarse unos de otros con el tiempo.

Prefiere una función auxiliar reutilizable:

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"
```

Entonces distintas funciones coordinadoras pueden llamar a la misma auxiliar.

```text
student report ─┐
                ├─→ classify_score()
team summary ───┘
```

La reutilización es más valiosa cuando la función extraída representa un concepto realmente compartido, no solo una línea trivial de sintaxis repetida.

## 13. El orden de las llamadas importa cuando los resultados dependen de trabajo anterior

Si una función necesita el resultado de otra, el resultado necesario debe existir primero.

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


sessions = [30, 45, 60]
total_minutes = calculate_total_minutes(sessions)
workload = classify_workload(total_minutes)
print(total_minutes, workload)
```

Salida:

```text
135 deep
```

La clasificación depende del total, por lo que primero se calcula el total.

## 14. Construye pipelines simples paso a paso

Un pipeline es un modelo mental útil cuando un resultado se convierte en la entrada del siguiente paso.

```text
raw value
   ↓
normalize
   ↓
classify
   ↓
format
   ↓
final result
```

Por ejemplo:

```python
def normalize_code(code: str) -> str:
    return code.strip().upper()


def classify_code(code: str) -> str:
    if code.startswith("A"):
        return "priority"
    return "standard"


def build_code_summary(code: str) -> str:
    clean_code = normalize_code(code)
    category = classify_code(clean_code)
    return f"{clean_code}: {category}"


print(build_code_summary(" a-17 "))
```

Salida:

```text
A-17: priority
```

La función coordinadora hace visible la secuencia sin contener los detalles de cada paso.

## 15. Las condiciones pueden vivir dentro de auxiliares enfocadas

La composición no reemplaza el flujo del programa. Le da a la lógica de flujo un lugar con significado.

```python
def is_passing(score: int) -> bool:
    return score >= 70


def build_result(score: int) -> str:
    if is_passing(score):
        return "Pass"
    return "Review"


print(build_result(78))
```

Salida:

```text
Pass
```

`is_passing()` responde una pregunta booleana. `build_result()` decide qué resultado producir usando esa respuesta.

## 16. Los bucles pueden llamar auxiliares para cada elemento

Un bucle puede delegar el trabajo específico de cada elemento a una función.

```python
def format_name(name: str) -> str:
    return name.strip().title()


names = [" ava ", "LEO", " mia"]

for name in names:
    print(format_name(name))
```

Salida:

```text
Ava
Leo
Mia
```

Esto suele mantener el bucle enfocado en la repetición mientras la auxiliar se enfoca en transformar un elemento.

## 17. Las funciones coordinadoras deberían describir la historia mayor

Una buena función coordinadora suele leerse como un pequeño resumen de la tarea.

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


def build_study_summary(subject: str, sessions: list[int]) -> str:
    total_minutes = calculate_total_minutes(sessions)
    workload = classify_workload(total_minutes)
    return f"{subject}: {total_minutes} minutes ({workload})"
```

Sin leer los detalles internos de las auxiliares, ya puedes describir `build_study_summary()`:

```text
calculate total → classify workload → build summary
```

Eso es una buena señal de que la colaboración está comunicando bien la intención.

## 18. Un grafo simple de llamadas muestra quién llama a quién

Un **grafo de llamadas** es un diagrama de las relaciones de llamada.

Para el ejemplo anterior:

```text
build_study_summary()
├── calculate_total_minutes()
└── classify_workload()
```

Un grafo de llamadas no muestra todas las variables ni todos los detalles de runtime. Responde una pregunta estructural más simple:

> ¿Qué función llama a qué otra función?

El siguiente capítulo profundizará exactamente en cómo se mueven los datos por esas llamadas.

## 19. El anidamiento profundo puede ocultar la secuencia

Esto es válido:

```python
result = format_total(calculate_total(values))
```

Pero una cadena más larga puede resultar difícil de inspeccionar:

```python
result = finalize(format_total(calculate_total(normalize_values(values))))
```

Los nombres intermedios pueden exponer las etapas:

```python
clean_values = normalize_values(values)
total = calculate_total(clean_values)
message = format_total(total)
result = finalize(message)
```

La segunda forma es más larga, pero suele ser más fácil de depurar, explicar y cambiar.

## 20. Error común: imprimir cuando otra función necesita el valor

Considera:

```python
def calculate_total(values: list[int]) -> None:
    print(sum(values))
```

Esto imprime un número, pero devuelve `None`.

Por lo tanto, esto no transmite el número impreso:

```python
total = calculate_total([10, 20, 30])
print(total)
```

Salida:

```text
60
None
```

Cuando otra función necesita el resultado, devuelve el valor:

```python
def calculate_total(values: list[int]) -> int:
    return sum(values)
```

Imprimir y retornar resuelven problemas diferentes.

## 21. Error común: duplicar la misma regla en varias funciones

Las reglas repetidas de negocio o clasificación pueden separarse con el tiempo.

En lugar de copiar:

```python
def student_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"


def course_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

Extrae el concepto compartido cuando la regla sea realmente la misma:

```python
def classify_readiness(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

No extraigas solo porque dos fragmentos sin relación se parecen por casualidad hoy. Las funciones compartidas deberían representar significado compartido.

## 22. Error común: crear funciones demasiado pequeñas para aclarar algo

Esto es técnicamente válido:

```python
def add_one(number: int) -> int:
    return number + 1


def add_two(number: int) -> int:
    return add_one(add_one(number))
```

Pero no toda expresión necesita una función separada.

Una auxiliar merece existir cuando su nombre o reutilización hace que el programa sea más fácil de entender o mantener.

Pregunta:

1. ¿El nombre de esta función explica un concepto significativo?
2. ¿El comportamiento se reutiliza?
3. ¿La extracción elimina detalles que distraen de una función mayor?
4. ¿La función puede entenderse y probarse de forma independiente?

Si la respuesta es no a las cuatro, la división puede ser innecesaria.

## 23. Error común: ocultar efectos secundarios dentro de auxiliares

Un **efecto secundario** es una acción observable más allá de simplemente devolver un valor, como imprimir o modificar un objeto que existe fuera de la función.

Esta auxiliar transforma e imprime:

```python
def normalize_name(name: str) -> str:
    clean_name = name.strip().title()
    print("Normalized")
    return clean_name
```

Eso puede ser intencional, pero quienes reutilicen la auxiliar también recibirán esa salida adicional.

Para una transformación reutilizable, una auxiliar más silenciosa puede ser más fácil de combinar:

```python
def normalize_name(name: str) -> str:
    return name.strip().title()
```

Los efectos secundarios no están prohibidos. Lo importante es que sean deliberados y no sorprendan a quien use la función.

## 24. Ejemplos ejecutables

### Preparar un saludo mediante una auxiliar

Archivo: [`examples/prepare_greeting.py`](examples/prepare_greeting.py)

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


def build_greeting(name: str) -> str:
    clean_name = normalize_name(name)
    return f"Welcome, {clean_name}!"


print(build_greeting("  ava stone  "))
```

Salida esperada:

```text
Welcome, Ava Stone!
```

`build_greeting()` delega la normalización y usa el texto retornado.

### Construir un informe de puntuación con dos auxiliares

Archivo: [`examples/build_score_report.py`](examples/build_score_report.py)

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"


def build_score_report(student: str, score: int) -> str:
    status = classify_score(score)
    return format_score_report(student, score, status)


print(build_score_report("Ava", 84))
```

Salida esperada:

```text
Ava: 84 points - ready
```

La función coordinadora conecta clasificación y formato sin duplicar ninguna responsabilidad.

### Construir un resumen de estudio como un pequeño pipeline

Archivo: [`examples/build_study_summary.py`](examples/build_study_summary.py)

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


def build_study_summary(subject: str, sessions: list[int]) -> str:
    total_minutes = calculate_total_minutes(sessions)
    workload = classify_workload(total_minutes)
    return f"{subject}: {total_minutes} minutes ({workload})"


print(build_study_summary("Python", [30, 45, 60]))
```

Salida esperada:

```text
Python: 135 minutes (deep)
```

La función mayor se lee como un pequeño esquema: calcular, clasificar, resumir.

## 25. Ejercicio: compón un resumen de lectura

Crea estas funciones:

```python
def calculate_total_pages(chapters: list[int]) -> int:
    pass


def classify_reading(total_pages: int) -> str:
    pass


def build_reading_summary(book: str, chapters: list[int]) -> str:
    pass
```

Requisitos:

1. `calculate_total_pages()` devuelve la suma de las cantidades de páginas de los capítulos;
2. `classify_reading()` devuelve `"long"` para 100 páginas o más y `"short"` en caso contrario;
3. `build_reading_summary()` llama a las dos auxiliares;
4. la cadena final usa la forma `Book: 120 pages (long)`;
5. prueba con `"Python Notes"` y `[35, 40, 45]`;
6. mantén la impresión fuera de las auxiliares de cálculo.

Salida esperada:

```text
Python Notes: 120 pages (long)
```

Intenta seguir las llamadas en papel antes de ejecutar el programa.

## 26. Checklist de repaso

Antes de continuar, confirma que puedes:

- [ ] llamar una función definida por el usuario desde otra;
- [ ] explicar adónde vuelve la ejecución después de que termina una auxiliar;
- [ ] almacenar el valor retornado por una función y pasarlo al siguiente paso;
- [ ] explicar por qué las variables intermedias pueden mejorar la trazabilidad;
- [ ] distinguir papeles auxiliares y coordinadores sin tratarlos como palabras clave de Python;
- [ ] separar cálculo de formato cuando la reutilización se beneficia de ello;
- [ ] exponer dependencias mediante parámetros en lugar de globales ocultas;
- [ ] reutilizar una auxiliar desde más de una función llamadora;
- [ ] explicar por qué las llamadas dependientes deben ocurrir en el orden necesario;
- [ ] combinar auxiliares con `if` y bucles;
- [ ] dibujar un grafo simple de llamadas;
- [ ] reconocer cuándo imprimir impide reutilizar un valor;
- [ ] reconocer lógica duplicada que representa un concepto compartido;
- [ ] evitar fragmentación innecesaria en funciones diminutas;
- [ ] identificar un efecto secundario sorprendente dentro de una auxiliar.

## 27. Referencia rápida

| Necesidad | Patrón útil |
|---|---|
| reutilizar una parte del comportamiento | llamar una función auxiliar |
| pasar un resultado hacia adelante | `result = helper(...)` |
| hacer visible una secuencia de varios pasos | usar variables intermedias |
| coordinar varias auxiliares | usar una función coordinadora mayor |
| reutilizar un cálculo separado de la salida | retornar el cálculo y formatear o imprimir después |
| mostrar claramente los datos necesarios | usar parámetros |
| evitar coordinación oculta | preferir parámetros y retornos explícitos frente a estado global temporal |
| mostrar relaciones de llamada | dibujar un grafo simple de llamadas |
| mantener consistentes las reglas repetidas | extraer una auxiliar realmente compartida |
| evitar fragmentación excesiva | dividir solo cuando la función aporte significado, reutilización o claridad |

## 28. Límite de alcance

Este capítulo no profundiza en:

- aliasing e identidad de objetos entre varias llamadas de función;
- propiedad de mutaciones entre funciones llamadoras y auxiliares;
- copias defensivas entre límites de funciones;
- propagación de excepciones por cadenas de llamadas;
- recursión;
- funciones pasadas como argumentos;
- closures;
- decoradores;
- módulos e imports como estrategia de organización;
- funciones asíncronas y concurrencia;
- inspección avanzada de la pila de llamadas.

Esos temas necesitan tratamiento separado. El siguiente capítulo se enfoca específicamente en seguir **el flujo de datos entre funciones**, incluyendo de dónde vienen los valores, adónde van y qué función es responsable de cambiarlos.

## 29. Qué viene después

Ahora puedes dividir una tarea mayor en funciones que cooperan y leer las relaciones básicas de llamada entre ellas.

La siguiente pregunta es más precisa:

> Cuando varias funciones intercambian valores, ¿cómo podemos seguir exactamente de dónde vinieron los datos, qué los cambió y quién es responsable de cada cambio?

Eso lleva al **Capítulo 09: Flujo de Datos Entre Funciones**.

Vuelve a la [ruta de Funciones](../README.es.md) o a la [ruta completa](../../docs/learning-path.es.md).

## Referencias

Documentación primaria de Python:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Tutorial: More on Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Python 3.13 Language Reference: The `return` statement](https://docs.python.org/3.13/reference/simple_stmts.html#the-return-statement)
