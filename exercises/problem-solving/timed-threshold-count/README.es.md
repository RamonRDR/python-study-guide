# Cronometrado: contar por límite

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.timed-threshold-count` · **Dificultad:** Fácil · 10 min

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
- [01-conditions-comparisons-and-boolean-logic](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.es.md)
- [16-timed-live-coding](../../../problem-solving-and-live-coding/16-timed-live-coding/README.es.md)

## Contrato

Devuelve cantidad de enteros mayores o iguales al límite. Conserva lista; entrada vacía devuelve cero. Cuenta apariciones repetidas, no valores distintos.

Solo se evalúan dominios declarados. Devuelve tipos y valores exactos; no imprimas, modifiques entradas ni añadas dependencias. Elección algorítmica y complejidad requieren revisión manual; pruebas funcionales no las demuestran.

Usa temporizador personal. Trabaja de forma independiente, sin pistas, referencia ni IA en el primer intento. Al límite registra progreso, para el reloj, termina y compara. Tiempo es autorregistrado, no evaluado por CI.

Copia el inicial a directorio personal; Python 3.13 es la base. Ejecución en navegador sin verificar.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def count_at_least(values: list[int], threshold: int) -> int:
    raise NotImplementedError("Implement count_at_least")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],2]` | `0` |
| `[[2,2,3,1],2]` | `3` |
| `[[-3,-2,0],-2]` | `2` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Inicializa contador antes de iterar.

</details>

<details>
<summary>Pista 2</summary>

Usa comparación inclusiva.

</details>

<details>
<summary>Pista 3</summary>

Devuelve tras procesar toda lista.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Contador cuenta exactamente elementos válidos procesados. Comparación inclusiva trata igualdad y bucle vacío deja cero.

- Tiempo: O(n)
- Espacio auxiliar: O(1)

Modelo de coste fijo para enteros acotados y etiquetas de longitud acotada, comportamiento hash esperado cuando aplica. n/m son tamaños (en listas anidadas n cuenta elementos y nodos de lista visitados), k claves distintas, h profundidad. Salida requerida excluida de espacio auxiliar; recursividad usa O(h) marcos.

</details>

## Validación

Comprueba tus propias llamadas manualmente y añade casos límite. Desde raíz del repositorio, el comando siguiente prueba referencias e implementaciones incorrectas conocidas, no tu código personal. Soluciones públicas son visibles; sin evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/16-timed-live-coding/README.es.md) · [Índice de ejercicios](../../README.es.md)
