# Índice de inserción binaria

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.binary-insertion-index` · **Dificultad:** Media · 22 min

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
- [06-while-loops-and-state-driven-repetition](../../../program-flow/06-while-loops-and-state-driven-repetition/README.es.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.es.md)

## Contrato

Dada lista ordenada ascendente de enteros, devuelve primer índice donde insertar objetivo sin romper orden, antes de iguales. Devuelve len(values) si todos son menores. Usa búsqueda binaria; no modifiques ni valides orden recorriendo.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Escribe pseudocódigo e implementa de forma independiente antes de abrir la referencia.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def insertion_index(values: list[int], target: int) -> int:
    raise NotImplementedError("Implement insertion_index")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],3]` | `0` |
| `[[2,4,4,7],4]` | `1` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Usa intervalo semiabierto de cero a len(values).

</details>

<details>
<summary>Pista 2</summary>

Descarta hasta mid solo si valor central es estrictamente menor.

</details>

<details>
<summary>Pista 3</summary>

Cuando límites coincidan, devuelve índice sin acceder otra vez a lista.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

El intervalo decreciente mantiene primera posición cuyo valor no es menor, o centinela final. A diferencia de búsqueda exacta, valor ausente tiene índice de inserción.

- Tiempo: O(log n)
- Espacio auxiliar: O(1)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.es.md) · [Índice de ejercicios](../../README.es.md)
