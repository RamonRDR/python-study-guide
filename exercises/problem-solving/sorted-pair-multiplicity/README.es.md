# Contar pares objetivo con duplicados

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.sorted-pair-multiplicity` · **Dificultad:** Difícil · 40 min

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
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.es.md)
- [12-algorithms-and-complexity](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.es.md)

## Contrato

Dada lista ascendente de enteros, cuenta pares de índices i < j cuyos valores suman objetivo. Valores iguales en índices distintos son apariciones distintas; conserva entrada. Usa dos punteros agrupados en O(n) y espacio auxiliar constante.

Solo se evalúan dominios declarados. Devuelve tipos y valores exactos; no imprimas, modifiques entradas ni añadas dependencias. Elección algorítmica y complejidad requieren revisión manual; pruebas funcionales no las demuestran.

Copia el inicial a directorio personal; Python 3.13 es la base. Ejecución en navegador sin verificar.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def count_target_pairs(values: list[int], target: int) -> int:
    raise NotImplementedError("Implement count_target_pairs")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],4]` | `0` |
| `[[1,1,3,3,3],4]` | `6` |
| `[[2,2,2,2],4]` | `6` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Compara suma de valores extremos con objetivo.

</details>

<details>
<summary>Pista 2</summary>

En igualdad con extremos distintos, cuenta cada grupo de iguales y multiplica conteos.

</details>

<details>
<summary>Pista 3</summary>

Si extremos iguales, todas posiciones restantes tienen ese valor: suma k(k-1)//2 y termina.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

El orden permite descartar extremo imposible. Grupos distintos coincidentes de tamaños a y b generan a*b pares cruzados. Con extremos iguales, todo par de las k posiciones restantes cuenta una vez. Cada puntero avanza monótonamente.

- Tiempo: O(n)
- Espacio auxiliar: O(1)

Modelo de coste fijo para enteros acotados y etiquetas de longitud acotada, comportamiento hash esperado cuando aplica. n/m son tamaños (en listas anidadas n cuenta elementos y nodos de lista visitados), k claves distintas, h profundidad. Salida requerida excluida de espacio auxiliar; recursividad usa O(h) marcos.

</details>

## Validación

Comprueba tus propias llamadas manualmente y añade casos límite. Desde raíz del repositorio, el comando siguiente prueba referencias e implementaciones incorrectas conocidas, no tu código personal. Soluciones públicas son visibles; sin evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.es.md) · [Índice de ejercicios](../../README.es.md)
