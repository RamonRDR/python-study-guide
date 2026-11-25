# Conciliar registros de inventario

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.inventory-reconciliation` · **Dificultad:** Difícil · 40 min

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
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.es.md)
- [02-modifying-lists-and-methods](../../../collections/02-modifying-lists-and-methods/README.es.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)
- [09-data-flow-between-functions](../../../functions/09-data-flow-between-functions/README.es.md)
- [15-mixed-challenges](../../../problem-solving-and-live-coding/15-mixed-challenges/README.es.md)

- [05-sets-and-unique-values](../../../collections/05-sets-and-unique-values/README.es.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.es.md)
- [03-tuples-and-immutability](../../../collections/03-tuples-and-immutability/README.es.md)

## Contrato

Cada entrada es lista de filas [label, quantity], con etiquetas exactas y cantidades enteras no negativas. Agrega duplicados por separado y devuelve filas [label, expected_total, actual_total, actual_total - expected_total] solo para totales distintos. Ordena por primera aparición en expected seguida de primera aparición de etiquetas exclusivas de actual. Cantidades ausentes son cero; conserva entradas.

Solo se evalúan dominios declarados. Devuelve tipos y valores exactos; no imprimas, modifiques entradas ni añadas dependencias. Elección algorítmica y complejidad requieren revisión manual; pruebas funcionales no las demuestran.

Copia el inicial a directorio personal; Python 3.13 es la base. Ejecución en navegador sin verificar.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def reconcile(expected: list[list], actual: list[list]) -> list[list]:
    raise NotImplementedError("Implement reconcile")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],[]]` | `[]` |
| `[[["a",2],["a",3]],[["a",4]]]` | `[["a",5,4,-1]]` |
| `[[["b",2],["a",1]],[["a",1],["c",3]]]` | `[["b",2,0,-2],["c",0,3,3]]` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Construye dos diccionarios independientes de totales.

</details>

<details>
<summary>Pista 2</summary>

Construye secuencia ordenada de etiquetas únicas en ambas entradas.

</details>

<details>
<summary>Pista 3</summary>

Compara totales con cero por defecto y añade solo diferencias no cero.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Separa agregación de orden y comparación. Conjunto de vistos evita filas duplicadas; conservar primera aparición no requiere ordenar. Cero por defecto equivale a ausencia y cantidad explícitamente cero.

- Tiempo: O(n+m) esperado
- Espacio auxiliar: O(k)

Modelo de coste fijo para enteros acotados y etiquetas de longitud acotada, comportamiento hash esperado cuando aplica. n/m son tamaños (en listas anidadas n cuenta elementos y nodos de lista visitados), k claves distintas, h profundidad. Salida requerida excluida de espacio auxiliar; recursividad usa O(h) marcos.

</details>

## Validación

Comprueba tus propias llamadas manualmente y añade casos límite. Desde raíz del repositorio, el comando siguiente prueba referencias e implementaciones incorrectas conocidas, no tu código personal. Soluciones públicas son visibles; sin evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/15-mixed-challenges/README.es.md) · [Índice de ejercicios](../../README.es.md)
