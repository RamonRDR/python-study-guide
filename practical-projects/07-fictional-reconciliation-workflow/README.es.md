# Flujo Ficticio de Conciliación

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Volver a Proyectos Prácticos](../README.es.md)

Este es el **Proyecto 07 de la Fase 10: Proyectos Prácticos**. Convierte dos colecciones ficticias de registros en un informe de conciliación explícito y determinista.

El ejemplo es original y ficticio. No reproduce ninguna empresa real, cliente, sistema contable ni flujo privado.

## Qué vas a practicar

Este proyecto combina conceptos de fases anteriores:

- modelado inmutable con `dataclass`;
- estados controlados con `StrEnum`;
- dinero exacto con `Decimal`;
- diccionarios como índices de consulta;
- sets para la unión de claves de conciliación;
- orden determinista;
- validación y excepciones deliberadas;
- funciones con fronteras claras de entrada y salida;
- cobertura con pytest;
- separación entre lógica de dominio y presentación.

## Escenario ficticio

Dos fuentes imaginarias deberían contener las mismas referencias e importes.

Fuente Norte:

| Referencia | Importe |
|---|---:|
| `REF-001` | `150.00` |
| `REF-002` | `275.50` |
| `REF-003` | `100.00` |

Fuente Sur:

| Referencia | Importe |
|---|---:|
| `REF-001` | `150.00` |
| `REF-002` | `270.50` |
| `REF-004` | `100.00` |

Las clasificaciones esperadas son:

```text
REF-001 -> matched
REF-002 -> amount_mismatch
REF-003 -> left_only
REF-004 -> right_only
```

Para registros encontrados en ambos lados, la diferencia con signo es:

```text
difference = left.amount - right.amount
```

Así, `275.50 - 270.50` produce `5.00`.

## Requisitos

El flujo debe:

1. aceptar dos iterables de `ReconciliationRecord`;
2. rechazar identificadores de referencia vacíos;
3. exigir importes `Decimal` finitos;
4. aceptar solo importes exactamente representables con precisión de centavos y con un máximo de 100 dígitos en la parte entera;
5. eliminar espacios alrededor de los identificadores;
6. canonicalizar los importes aceptados a dos decimales;
7. rechazar referencias duplicadas dentro de cualquiera de las fuentes;
8. comparar identificadores de forma exacta y sensible a mayúsculas/minúsculas;
9. clasificar cada referencia como `matched`, `amount_mismatch`, `left_only` o `right_only`;
10. conservar la diferencia con signo en divergencias de importe;
11. ordenar la salida por identificador;
12. generar conteos de resumen deterministas;
13. calcular la magnitud absoluta total de las divergencias;
14. renderizar un informe de texto estable.

El límite de 100 dígitos enteros es un contrato explícito de seguridad de recursos para este proyecto educativo. Está muy por encima de los valores realistas de los ejemplos, pero impide que notaciones científicas compactas como `1e1000000` se expandan a enteros gigantescos en Python.

## Alcance deliberado

La primera versión comienza **después de la ingestión**.

No procesa CSV, hojas de cálculo, APIs, bases de datos ni datos privados. Esas capas pueden añadirse después como extensiones.

Separar la ingestión mantiene visible la pregunta principal:

> Dadas dos colecciones ya validadas, ¿cómo debería comportarse la conciliación?

## Estructura

```text
07-fictional-reconciliation-workflow/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── demo.py
├── reconciliation.py
└── tests/
    ├── conftest.py
    ├── test_decimal_precision.py
    ├── test_reconciliation.py
    └── test_text_safety.py
```

## Modelo principal

### `ReconciliationRecord`

```python
ReconciliationRecord(
    reference_id="REF-001",
    amount=Decimal("150.00"),
)
```

El registro:

- elimina espacios alrededor del identificador;
- rechaza identificadores vacíos;
- exige un `Decimal` real;
- rechaza `NaN` e infinitos;
- rechaza valores más allá de la precisión de centavos;
- rechaza importes cuya parte entera supere 100 dígitos;
- almacena los importes aceptados en forma canónica de dos decimales.

Los importes negativos están permitidos porque un flujo genérico puede representar reversiones o ajustes.

### `ReconciliationStatus`

Los estados controlados son:

```python
MATCHED
AMOUNT_MISMATCH
LEFT_ONLY
RIGHT_ONLY
```

### `ReconciliationItem`

Cada clave conciliada tiene una forma válida:

| Estado | Izquierda | Derecha | Diferencia |
|---|---|---|---|
| `MATCHED` | sí | sí | cero |
| `AMOUNT_MISMATCH` | sí | sí | distinta de cero |
| `LEFT_ONLY` | sí | no | ausente |
| `RIGHT_ONLY` | no | sí | ausente |

La dataclass valida estas invariantes en lugar de confiar en que el llamador construya un resultado coherente.

### `ReconciliationSummary`

El resumen almacena:

- total de elementos;
- elementos conciliados;
- divergencias de importe;
- elementos exclusivos de la izquierda;
- elementos exclusivos de la derecha;
- diferencia absoluta total de las divergencias.

Las diferencias individuales conservan su signo. El agregado usa valores absolutos para que una divergencia de `+5.00` y otra de `-5.00` no se cancelen incorrectamente.

### `ReconciliationReport`

El informe agrupa los nombres de las fuentes, los elementos ordenados y el resumen. El renderizado sucede después, por lo que la lógica de comparación no queda ligada al texto.

## Pipeline de conciliación

```text
validar etiquetas de las fuentes
        ↓
indexar fuente izquierda
        ↓
indexar fuente derecha
        ↓
rechazar duplicados
        ↓
unir todos los identificadores
        ↓
ordenar identificadores
        ↓
clasificar cada identificador
        ↓
calcular diferencias
        ↓
construir resumen
        ↓
devolver informe inmutable
```

Los diccionarios son útiles porque permiten consulta directa por clave de conciliación y hacen explícita la detección de duplicados.

## Contrato de matching

Los identificadores se comparan después de eliminar los espacios alrededor.

El matching es exacto y sensible a mayúsculas/minúsculas:

```text
REF-001 != ref-001
```

Esta es una decisión del proyecto, no una regla universal. Si un dominio requiere normalización de caja, claves compuestas u otra regla, debe declararse antes de iniciar la conciliación.

## ¿Por qué `Decimal`?

Para importes monetarios, el proyecto usa:

```python
Decimal("275.50")
```

en lugar de `float`.

Crear `Decimal` a partir de texto conserva el valor decimal deseado. El registro aplica después la frontera monetaria de dos decimales y el máximo de 100 dígitos enteros antes de cualquier expansión a centavos enteros.

## Ejemplo básico

```python
from decimal import Decimal

from reconciliation import ReconciliationRecord, reconcile

left = (
    ReconciliationRecord("REF-001", Decimal("150.00")),
    ReconciliationRecord("REF-002", Decimal("275.50")),
)

right = (
    ReconciliationRecord("REF-001", Decimal("150.00")),
    ReconciliationRecord("REF-002", Decimal("270.50")),
)

report = reconcile(left, right)

for item in report.items:
    print(item.reference_id, item.status)
```

Salida lógica:

```text
REF-001 matched
REF-002 amount_mismatch
```

## Demostración

Ejecuta desde esta carpeta:

```bash
python demo.py
```

La demo es determinista, no interactiva, sin red y usa únicamente datos ficticios en memoria.

Produce los cuatro estados importantes y un resumen.

## Caminos de fallo

El flujo falla deliberadamente cuando su contrato de entrada es ambiguo o inválido.

Ejemplos:

```python
ReconciliationRecord("", Decimal("10.00"))
```

genera `ValueError`.

```python
ReconciliationRecord("REF-001", 10.00)
```

genera `TypeError` porque los floats no se convierten silenciosamente.

```python
ReconciliationRecord("REF-001", Decimal("10.001"))
```

genera `ValueError` porque el importe supera la precisión de centavos.

```python
ReconciliationRecord("REF-001", Decimal("1e100"))
```

genera `ValueError` porque el importe requeriría 101 dígitos enteros, por encima del límite documentado de 100 dígitos.

Las referencias duplicadas dentro de una fuente también generan `ValueError`. El flujo no intenta adivinar si debería prevalecer el primer o el último duplicado.

## Errores comunes

### Comparar filas por posición

Los mismos registros lógicos pueden llegar en órdenes distintos. Concilia mediante una clave estable, no mediante la posición en la lista.

### Sobrescribir duplicados silenciosamente

Una asignación normal en un diccionario puede ocultar registros duplicados. Este proyecto detecta el duplicado antes de que la inserción lo sobrescriba silenciosamente.

### Usar valor absoluto demasiado pronto

`abs(left - right)` elimina la dirección. Conserva la diferencia con signo en cada elemento y usa valores absolutos solo en la métrica de resumen.

### Mezclar comparación e impresión

Devolver resultados estructurados facilita las pruebas y permite otros renderizadores en el futuro.

### Añadir normalización sin contrato

Cambiar la caja, usar fuzzy matching, eliminar puntuación o ceros iniciales puede fusionar identificadores distintos. Trata la normalización como una decisión explícita de dominio.

## Pruebas

Ejecuta la suite enfocada desde la raíz del repositorio:

```bash
python -m pytest -q practical-projects/07-fictional-reconciliation-workflow/tests
```

Las pruebas iniciales cubren validación, duplicados, los cuatro estados, diferencias positivas y negativas, generators, orden determinista, etiquetas de fuentes, sensibilidad a caja, invariantes de elementos, entrada vacía, límites de precisión monetaria, límites de magnitud, resúmenes y renderizado determinista.

## Ejercicio

Añade `REF-005` a ambas fuentes de la demo con importes diferentes.

Antes de ejecutar, predice:

1. el estado;
2. la diferencia con signo;
3. la nueva cantidad de divergencias;
4. la nueva diferencia absoluta total.

Después ejecuta la demo y compara tu predicción con el informe real.

## Desafíos de extensión

Después de que el contrato base esté claro, prueba una extensión a la vez:

1. Añade una tolerancia `Decimal` configurable y prueba exactamente su límite.
2. Añade una capa de ingestión CSV que produzca registros validados antes de la conciliación.
3. Sustituye la referencia simple por una clave compuesta como `(reference_id, period)`.
4. Añade un renderer Markdown sin modificar `reconcile()`.
5. Exporta solo elementos no resueltos, conservando el informe canónico completo.
6. Introduce un objeto de política de conciliación en lugar de muchos flags booleanos no relacionados.

## Discusión de portafolio

Este proyecto demuestra cómo transformar un problema genérico de comparación en contratos explícitos de software.

Puntos útiles para explicar en un portafolio:

- claves de dominio estables;
- importes monetarios exactos;
- límites explícitos de magnitud;
- rechazo de duplicados;
- consulta indexada;
- estados y orden deterministas;
- diferencias con signo y métricas agregadas;
- resultados inmutables;
- separación entre conciliación y renderizado;
- pruebas automatizadas enfocadas en límites.

## Referencia rápida

```text
Entrada:      dos iterables de ReconciliationRecord
Clave:        reference_id normalizado
Matching:     exacto y sensible a mayúsculas/minúsculas
Dinero:       Decimal finito, precisión de centavos, <= 100 dígitos enteros
Estados:      matched / amount_mismatch / left_only / right_only
Diferencia:   left.amount - right.amount
Orden:        reference_id ascendente
Duplicados:   rechazados dentro de cada fuente
Salida:       ReconciliationReport inmutable
```

## Próximo proyecto

Después de que este proyecto sea revisado, la Fase 10 continúa con el **Proyecto 08: Flujo Simulado de Automatización**.
