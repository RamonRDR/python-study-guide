# Primera etiqueta repetida

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.first-repeated-label` · **Dificultad:** Media · 18 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [05-sets-and-unique-values](../../../collections/05-sets-and-unique-values/README.es.md)
- [07-break-continue-and-loop-else](../../../program-flow/07-break-continue-and-loop-else/README.es.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)

## Contrato

Devuelve la etiqueta cuya segunda aparición se encuentra primero al recorrer de izquierda a derecha. Devuelve None si no hay repetición; cadena vacía es válida. Conserva la entrada.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Escribe pseudocódigo e implementa de forma independiente antes de abrir la referencia.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def first_repeated_label(labels: list[str]) -> str | None:
    raise NotImplementedError("Implement first_repeated_label")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `null` |
| `[["a","b","b","a"]]` | `"b"` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Registra etiquetas ya vistas.

</details>

<details>
<summary>Pista 2</summary>

Comprueba pertenencia antes de añadir etiqueta actual.

</details>

<details>
<summary>Pista 3</summary>

Devuelve inmediatamente en la primera repetición; si no, devuelve None tras el bucle.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

El conjunto representa etiquetas de posiciones anteriores. El primer acierto es la segunda aparición más temprana, no la primera posición original.

- Tiempo: O(n) esperado
- Espacio auxiliar: O(k)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/09-collections/README.es.md) · [Índice de ejercicios](../../README.es.md)
