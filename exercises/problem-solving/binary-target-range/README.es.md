# Intervalo del objetivo por búsqueda binaria

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.binary-target-range` · **Dificultad:** Difícil · 32 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.es.md)
- [06-while-loops-and-state-driven-repetition](../../../program-flow/06-while-loops-and-state-driven-repetition/README.es.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.es.md)
- [11-searching-and-sorting](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.es.md)

## Contrato

Dada lista ascendente de enteros, devuelve índices inclusivos [first, last] del objetivo, o [-1, -1] si falta. Usa dos búsquedas binarias de frontera, no recorrido lineal; conserva entrada. Orden garantizado.

Solo se evalúan dominios declarados. Devuelve tipos y valores exactos; no imprimas, modifiques entradas ni añadas dependencias. Elección algorítmica y complejidad requieren revisión manual; pruebas funcionales no las demuestran.

Copia el inicial a directorio personal; Python 3.13 es la base. Ejecución en navegador sin verificar.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def target_range(values: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement target_range")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],3]` | `[-1,-1]` |
| `[[2,4,4,4,7],4]` | `[1,3]` |
| `[[1,1,1],1]` | `[0,2]` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Encuentra primera posición cuyo valor es al menos objetivo.

</details>

<details>
<summary>Pista 2</summary>

Si falta o está fuera de lista, devuelve par de ausencia.

</details>

<details>
<summary>Pista 3</summary>

Encuentra primera posición estrictamente mayor; resta uno para última coincidencia.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Las dos búsquedas semiabiertas encuentran fronteras del bloque contiguo de iguales. Frontera derecha es exclusiva. Comprobar izquierda evita informar objetivo inexistente.

- Tiempo: O(log n)
- Espacio auxiliar: O(1)

Modelo de coste fijo para enteros acotados y etiquetas de longitud acotada, comportamiento hash esperado cuando aplica. n/m son tamaños (en listas anidadas n cuenta elementos y nodos de lista visitados), k claves distintas, h profundidad. Salida requerida excluida de espacio auxiliar; recursividad usa O(h) marcos.

</details>

## Validación

Comprueba tus propias llamadas manualmente y añade casos límite. Desde raíz del repositorio, el comando siguiente prueba referencias e implementaciones incorrectas conocidas, no tu código personal. Soluciones públicas son visibles; sin evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.es.md) · [Índice de ejercicios](../../README.es.md)
