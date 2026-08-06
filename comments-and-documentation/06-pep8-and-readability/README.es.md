<div align="center">

# PEP 8 y Legibilidad en Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Comentarios frente a logging](../05-comments-vs-logging/README.es.md)

PEP 8 es la guía de estilo del código Python de la biblioteca estándar y una referencia ampliamente utilizada en proyectos Python. Su objetivo no es hacer que todos los archivos sean visualmente idénticos. Busca mejorar la legibilidad y la coherencia para que el lector dedique menos esfuerzo a descifrar la presentación y más a comprender el comportamiento.

> **Principio orientador:** la coherencia favorece la legibilidad, pero el contexto del proyecto y la corrección tienen prioridad.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante a intermedio |
| Requisitos previos | Sintaxis básica de Python; se recomiendan los capítulos de comentarios y nombres significativos |
| Tiempo estimado | 60 a 85 minutos |
| Conceptos principales | PEP 8, indentación, longitud de línea, imports, espacios, nombres, comparaciones, excepciones, herramientas y convenciones del proyecto |

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- explicar qué es PEP 8 y qué no es;
- aplicar convenciones de indentación, espacios, saltos y líneas en blanco;
- organizar imports y elegir nombres convencionales;
- escribir comparaciones comunes y manejo de excepciones de forma legible;
- distinguir formateador, linter, verificador de tipos y pruebas;
- seguir las convenciones del proyecto sin realizar reformas de estilo fuera del alcance;
- reconocer cuándo una excepción deliberada es más clara o segura que la conformidad rígida.

## 1. PEP 8 es orientación, no sintaxis de Python

Un programa puede ser Python válido aunque ignore varias recomendaciones de estilo. Del mismo modo, un código muy bien formateado puede contener lógica incorrecta.

PEP 8 se ocupa principalmente de la disposición, los nombres, los comentarios, los imports y algunas recomendaciones de programación. Un formateador o linter puede aplicar el subconjunto elegido por el proyecto, pero Python no rechaza una función solo porque falten dos líneas en blanco.

Las reglas específicas del proyecto prevalecen dentro de él. Compatibilidad, corrección y claridad son más importantes que la conformidad cosmética.

## 2. La coherencia tiene niveles

Un orden de prioridad útil es:

1. preservar corrección y compatibilidad;
2. seguir las convenciones documentadas del proyecto;
3. mantener coherencia con el módulo circundante;
4. usar PEP 8 como valor predeterminado cuando no exista una regla local más fuerte.

No reformatees un archivo no relacionado solo porque observaste una diferencia. Los diffs cosméticos extensos ocultan cambios de comportamiento y dificultan la revisión.

## 3. Usa cuatro espacios por nivel de indentación

Python utiliza la indentación como sintaxis, por lo que la estructura visual y la del programa están conectadas. PEP 8 recomienda cuatro espacios por nivel.

```python
def calculate_total(amount: float, tax_rate: float) -> float:
    tax_amount = amount * tax_rate
    return amount + tax_amount
```

No mezcles tabulaciones y espacios. Configura el editor para insertar espacios y mostrar caracteres invisibles al diagnosticar problemas.

## 4. Divide expresiones largas dentro de delimitadores

Prefiere la continuación implícita dentro de paréntesis, corchetes o llaves:

```python
total = calculate_total(
    amount=1250.00,
    tax_rate=0.18,
)
```

Evita barras invertidas cuando los delimitadores hagan la estructura más clara. Alinea las líneas continuadas para distinguir argumentos del bloque exterior.

## 5. Divide antes de los operadores binarios

En expresiones multilínea, colocar el operador antes del operando continuado mantiene visualmente unidos los elementos relacionados:

```python
total_amount = (
    subtotal
    - discount_amount
    + shipping_amount
)
```

No dividas una expresión solo para satisfacer un número. Considera primero un nombre claro, una variable intermedia o una función menor.

## 6. Trata la longitud de línea como presupuesto de lectura

PEP 8 recomienda 79 caracteres para código y 72 para comentarios corridos y docstrings. También reconoce que los equipos pueden acordar límites mayores, normalmente hasta 99 caracteres para código.

La regla debe reducir el desplazamiento horizontal y mejorar los diffs. No debe crear una escalera de fragmentos artificiales. URLs, textos generados, identificadores externos largos y datos de prueba pueden requerir criterio.

## 7. Usa líneas en blanco para revelar estructura

Usa dos líneas en blanco alrededor de funciones y clases del módulo. Dentro de una clase, separa métodos con una línea. Dentro de una función, úsalas con moderación para separar pasos lógicos.

Muy pocas líneas convierten el código en una pared. Demasiadas desconectan pasos relacionados.

## 8. Organiza imports deliberadamente

Los imports suelen estar cerca del inicio y se agrupan en biblioteca estándar, paquetes de terceros e imports locales, separados por líneas en blanco:

```python
import json
from pathlib import Path

import requests

from project.reports import build_report
```

Coloca un `import` común por línea. Evita imports comodín porque ocultan el origen de los nombres. La ubicación puede variar cuando dependencias opcionales, costo inicial o ciclos exijan una excepción documentada.

## 9. Los espacios deben aclarar, no decorar

Usa espacios alrededor de asignaciones, comparaciones y operadores binarios, y después de comas. Evita espacios inmediatamente dentro de delimitadores o antes de los paréntesis de llamada:

```python
result = calculate_total(amount, tax_rate=0.18)
coordinates = (10, 20)
mapping["account"] = account_code
```

Los argumentos con nombre y los valores predeterminados sin anotación normalmente no usan espacios alrededor de `=`, como en `tax_rate=0.18` y `def calculate(tax_rate=0.18):`. Cuando una anotación de parámetro se combina con un valor predeterminado, usa espacios alrededor de `=`, como en `def calculate(tax_rate: float = 0.18):`.

## 10. Usa estilos de nombres convencionales

Convenciones comunes:

- `snake_case` para funciones, métodos y variables;
- `PascalCase` para clases y excepciones;
- `UPPER_SNAKE_CASE` para constantes;
- guion bajo inicial para detalles internos;
- `self` como primer parámetro de instancia y `cls` en métodos de clase.

```python
MAX_RETRY_COUNT = 3


class InvoiceProcessor:
    def process_invoice(self, invoice_id: str) -> None:
        is_ready = self._validate_invoice(invoice_id)
        if is_ready:
            self._save_invoice(invoice_id)
```

Las convenciones no sustituyen nombres significativos. `processed_invoice_count` comunica más que una variable perfectamente estilizada llamada `x`.

## 11. Escribe comparaciones idiomáticas y explícitas

Usa identidad para `None`, booleanos directamente en condiciones y pruebas de valor verdadero para contenedores vacíos cuando la pregunta sea sobre vacío:

```python
if result is None:
    handle_missing_result()

if is_active:
    start_worker()

if not records:
    return []
```

Usa `isinstance()` cuando la verificación de tipo sea realmente necesaria. No uses `is` para comparar números o textos.

## 12. Prefiere flujo de control legible

Las cláusulas de guarda pueden mantener visible el camino principal:

```python
def calculate_discount(customer: Customer) -> float:
    if not customer.is_eligible:
        return 0.0

    if customer.is_premium:
        return 0.15

    return 0.05
```

El anidamiento profundo suele indicar condiciones, responsabilidades o nombres que necesitan refactorización. No aplanes mecánicamente si los retornos tempranos ocultan limpieza o límites transaccionales.

## 13. Maneja excepciones de forma limitada

Captura las excepciones que puedas manejar o traducir con sentido:

```python
try:
    report = load_report(path)
except OSError as error:
    raise ReportLoadError(path) from error
```

Evita `except:` sin tipo en código común, porque también captura `KeyboardInterrupt` y `SystemExit`. Mantén el bloque `try` enfocado para mostrar qué operación puede fallar.

## 14. La legibilidad es mayor que el formato

Este código es compacto pero vago:

```python
def f(x):
    if x and len(x)>0:
        return sum(x)/len(x)
    return 0
```

Una versión legible revela intención:

```python
def calculate_average(values: list[float]) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)
```

El formato no repara una abstracción confusa, un nombre engañoso, un efecto lateral oculto o una función enorme. PEP 8 trabaja junto con diseño, comentarios, docstrings, pruebas y type hints.

## 15. Formateadores, linters, verificadores de tipos y pruebas son distintos

Un formateador reescribe la presentación. Un linter informa problemas de estilo y patrones sospechosos. Un verificador de tipos analiza contratos. Las pruebas verifican comportamientos definidos por el proyecto.

Las herramientas se superponen, pero ninguna prueba que el código sea correcto o comprensible. Configúralas en archivos versionados y no las introduzcas sin documentar su alcance y versión de Python.

## 16. Refactoriza el estilo con seguridad

Antes de una refactorización de estilo:

1. confirma si el comportamiento debe permanecer igual;
2. limita el diff al alcance declarado;
3. ejecuta pruebas antes y después;
4. separa formato mecánico de cambios lógicos cuando sea posible;
5. conserva nombres e interfaces públicas salvo cambio intencional;
6. trata código generado, migraciones, código incorporado y snapshots con reglas propias.

Un diff menor es más fácil de comprender, revisar, revertir y confiar.

## 17. Aprende cuándo desviarte

Una excepción deliberada puede justificarse cuando la conformidad rígida reduzca la legibilidad, rompa compatibilidad, choque con una convención establecida o exija cambios no relacionados.

Cuando la razón no sea obvia y siga siendo relevante, documéntala en la configuración o junto al código. Evita preferencias personales que hagan que un archivo se comporte distinto del resto.

## 18. Ejemplos de este repositorio

| Archivo | Propósito |
|---|---|
| [`readable_layout.py`](examples/readable_layout.py) | Muestra indentación, división de líneas, espacios y un pequeño punto de entrada |
| [`imports_and_names.py`](examples/imports_and_names.py) | Demuestra imports de biblioteca estándar, constantes y nombres descriptivos |
| [`refactor_for_readability.py`](examples/refactor_for_readability.py) | Sustituye lógica densa por funciones enfocadas que revelan intención |

Ejecuta desde la raíz:

```bash
python comments-and-documentation/06-pep8-and-readability/examples/readable_layout.py
```

## 19. Ejercicio

Refactoriza el siguiente código sin cambiar su resultado:

```python
def calc(x,y,z=False):
    if x!=None:
        if len(x)>0:
            r=sum(x)/len(x)
            if z==True:r=r-(r*y)
            return r
    return 0
```

Tu revisión debe:

1. elegir nombres descriptivos;
2. usar comprobaciones idiomáticas de `None`, booleanos y vacío;
3. reducir anidamiento innecesario;
4. añadir type hints compatibles con las entradas;
5. dividir líneas con claridad;
6. preservar el comportamiento original, incluida la entrada vacía;
7. explicar cualquier desviación deliberada de las reglas del proyecto.

## 20. Errores comunes

- tratar PEP 8 como sintaxis;
- reformatear código no relacionado dentro de un PR de comportamiento;
- respetar la longitud haciendo expresiones menos legibles;
- usar un formateador como sustituto del diseño;
- mezclar tabs y espacios;
- agrupar imports sin considerar restricciones opcionales o locales;
- renombrar interfaces públicas solo por estética;
- añadir `# noqa` o supresiones sin comprender la advertencia;
- asumir que todos los proyectos usan la misma configuración.

## 21. Lista de revisión

Antes de aprobar un cambio de legibilidad, verifica:

- indentación y continuación son inequívocas;
- los nombres revelan intención y siguen el proyecto;
- los imports son comprensibles y mínimos;
- espacios y líneas en blanco revelan estructura;
- comparaciones y excepciones expresan la semántica prevista;
- los comentarios explican decisiones, no formato;
- ninguna interfaz pública cambió accidentalmente;
- el diff no contiene limpieza fuera del alcance;
- herramientas y pruebas pasaron;
- supresiones y desviaciones tienen una razón duradera.

## 22. Resumen de consulta rápida

| Situación | Predeterminado |
|---|---|
| Indentación | Cuatro espacios |
| Continuación | Paréntesis, corchetes o llaves |
| Longitud de código | 79 en PEP 8; el proyecto puede definir otra |
| Definiciones del módulo | Dos líneas en blanco |
| Métodos de clase | Una línea en blanco |
| Funciones y variables | `snake_case` |
| Clases y excepciones | `PascalCase` |
| Constantes | `UPPER_SNAKE_CASE` |
| Comparar con `None` | `is None` / `is not None` |
| Contenedor vacío | `if not items:` cuando se pregunta por vacío |
| Orden de imports | Biblioteca estándar, terceros, local |
| Máxima prioridad | Corrección, compatibilidad y coherencia del proyecto |

## 23. Ejecuta las verificaciones del repositorio

Desde la raíz:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

Un resultado limpio del formateador o linter es evidencia útil, no un sustituto de la revisión humana.

## Referencias oficiales

- [PEP 8 — Guía de Estilo para Código Python](https://peps.python.org/pep-0008/)
- [Tutorial de Python — Estilo de programación](https://docs.python.org/es/3/tutorial/controlflow.html#intermezzo-coding-style)

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Comentarios frente a logging](../05-comments-vs-logging/README.es.md)
