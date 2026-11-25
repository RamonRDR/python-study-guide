# Depurar contador de positivos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.debug-positive-count` · **Dificultad:** Fácil · 12 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [01-conditions-comparisons-and-boolean-logic](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.es.md)
- [01-manual-coding-and-debugging](../../../manual-programming-practices/01-manual-coding-and-debugging/README.es.md)

## Contrato

Corrige la implementación suministrada para devolver cantidad de enteros estrictamente positivos de una lista. Cero no es positivo. Conserva entrada; devuelve cero para lista vacía.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Reproduce el defecto, rastrea estado, haz corrección mínima y repite casos.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def count_positive(values: list[int]) -> int:
    count = 0
    for value in values:
        if value >= 0:
            count += 1
    return count
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `0` |
| `[[0]]` | `0` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Reproduce el fallo con lista de un elemento que contiene cero.

</details>

<details>
<summary>Pista 2</summary>

Rastrea condición para negativos, cero y positivos.

</details>

<details>
<summary>Pista 3</summary>

Cambia comparación para incrementar solo positivos estrictos.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

El original incluye cero por >=. Cambio mínimo a > satisface especificación; caso solo con cero distingue implementaciones.

- Tiempo: O(n)
- Espacio auxiliar: O(1)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/13-debugging-challenges/README.es.md) · [Índice de ejercicios](../../README.es.md)
