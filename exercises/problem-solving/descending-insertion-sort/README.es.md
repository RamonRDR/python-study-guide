# Insertion sort descendente

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.descending-insertion-sort` · **Dificultad:** Media · 25 min

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
- [02-modifying-lists-and-methods](../../../collections/02-modifying-lists-and-methods/README.es.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.es.md)
- [06-sorting-algorithms](../../../problem-solving-and-live-coding/06-sorting-algorithms/README.es.md)

## Contrato

Devuelve lista nueva de los mismos enteros en orden descendente usando insertion sort. Conserva duplicados y entrada; no uses sorted ni list.sort.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Escribe pseudocódigo e implementa de forma independiente antes de abrir la referencia.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def descending_sort(values: list[int]) -> list[int]:
    raise NotImplementedError("Implement descending_sort")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `[]` |
| `[[3,1,2]]` | `[3,2,1]` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Copia lista y trata primer elemento como prefijo ordenado.

</details>

<details>
<summary>Pista 2</summary>

Guarda cada valor siguiente y desplaza valores menores del prefijo a la derecha.

</details>

<details>
<summary>Pista 3</summary>

Inserta en el hueco resultante; iguales no necesitan desplazarse.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Cambiar comparación de mayor a menor invierte orden del prefijo manteniendo invariante de insertion sort. La copia protege entrada.

- Tiempo: O(n²)
- Espacio auxiliar: O(1) excluyendo salida

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.es.md) · [Índice de ejercicios](../../README.es.md)
