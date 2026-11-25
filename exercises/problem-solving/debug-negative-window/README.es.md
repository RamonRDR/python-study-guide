# Depurar ventana negativa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.debug-negative-window` · **Dificultad:** Media · 22 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.es.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.es.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)
- [01-manual-coding-and-debugging](../../../manual-programming-practices/01-manual-coding-and-debugging/README.es.md)

## Contrato

Corrige algoritmo de ventana fija suministrado. Dados lista de enteros y size válido 1 <= size <= len(values), devuelve mayor suma de exactamente size elementos consecutivos. Listas solo negativas son válidas. Conserva entrada y usa una ventana móvil.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Reproduce el defecto, rastrea estado, haz corrección mínima y repite casos.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def max_window_sum(values: list[int], size: int) -> int:
    total = 0
    for index in range(size):
        total += values[index]
    best = max(0, total)
    for index in range(size, len(values)):
        total += values[index] - values[index - size]
        best = max(best, total)
    return best
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[-4,-2,-3],2]` | `-5` |
| `[[4,-1,3,2],2]` | `5` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Ejecuta inicial con [-4, -2, -3] y size 2.

</details>

<details>
<summary>Pista 2</summary>

Cero no es suma de ninguna ventana válida en ese caso.

</details>

<details>
<summary>Pista 3</summary>

Inicializa best con suma de primera ventana real y actualiza al mover.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Inicializar best en cero inventa ventana inexistente si todas sumas son negativas. Primera suma real establece base válida.

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
