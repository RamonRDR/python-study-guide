# Fusionar listas ordenadas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.merge-sorted-lists` · **Dificultad:** Difícil · 30 min

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
- [02-modifying-lists-and-methods](../../../collections/02-modifying-lists-and-methods/README.es.md)
- [06-while-loops-and-state-driven-repetition](../../../program-flow/06-while-loops-and-state-driven-repetition/README.es.md)
- [06-sorting-algorithms](../../../problem-solving-and-live-coding/06-sorting-algorithms/README.es.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)
- [11-searching-and-sorting](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.es.md)

## Contrato

Dadas dos listas ascendentes de enteros, devuelve nueva lista ascendente con cada aparición de ambas. Conserva entradas y duplicados; usa fusión con dos punteros en O(n+m), no ordenes concatenación.

Solo se evalúan dominios declarados. Devuelve tipos y valores exactos; no imprimas, modifiques entradas ni añadas dependencias. Elección algorítmica y complejidad requieren revisión manual; pruebas funcionales no las demuestran.

Copia el inicial a directorio personal; Python 3.13 es la base. Ejecución en navegador sin verificar.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    raise NotImplementedError("Implement merge_sorted")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],[]]` | `[]` |
| `[[1,3],[2,4]]` | `[1,2,3,4]` |
| `[[1,1],[1,2]]` | `[1,1,1,2]` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Mantén puntero al primer elemento no consumido de cada lista.

</details>

<details>
<summary>Pista 2</summary>

Añade menor elemento actual y avanza solo su puntero.

</details>

<details>
<summary>Pista 3</summary>

Cuando una lista se agote, añade elementos restantes de la otra.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Prefijo de salida siempre está ordenado y contiene exactamente elementos consumidos. Elegir menor cabeza conserva orden; consumir resto conserva multiplicidades. Cada posición avanza una vez.

- Tiempo: O(n+m)
- Espacio auxiliar: O(1)

Modelo de coste fijo para enteros acotados y etiquetas de longitud acotada, comportamiento hash esperado cuando aplica. n/m son tamaños (en listas anidadas n cuenta elementos y nodos de lista visitados), k claves distintas, h profundidad. Salida requerida excluida de espacio auxiliar; recursividad usa O(h) marcos.

</details>

## Validación

Comprueba tus propias llamadas manualmente y añade casos límite. Desde raíz del repositorio, el comando siguiente prueba referencias e implementaciones incorrectas conocidas, no tu código personal. Soluciones públicas son visibles; sin evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.es.md) · [Índice de ejercicios](../../README.es.md)
