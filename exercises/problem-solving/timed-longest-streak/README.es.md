# Cronometrado: mayor racha válida

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.timed-longest-streak` · **Dificultad:** Media · 20 min

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
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)
- [16-timed-live-coding](../../../problem-solving-and-live-coding/16-timed-live-coding/README.es.md)

## Contrato

Devuelve longitud de mayor racha contigua de enteros mayores o iguales al límite. Entrada vacía o sin válidos devuelve cero. Valor inferior rompe racha; conserva entrada.

Solo se evalúan dominios declarados. Devuelve tipos y valores exactos; no imprimas, modifiques entradas ni añadas dependencias. Elección algorítmica y complejidad requieren revisión manual; pruebas funcionales no las demuestran.

Usa temporizador personal. Trabaja de forma independiente, sin pistas, referencia ni IA en el primer intento. Al límite registra progreso, para el reloj, termina y compara. Tiempo es autorregistrado, no evaluado por CI.

Copia el inicial a directorio personal; Python 3.13 es la base. Ejecución en navegador sin verificar.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def longest_streak(values: list[int], threshold: int) -> int:
    raise NotImplementedError("Implement longest_streak")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],2]` | `0` |
| `[[2,2,0,3,4,2],2]` | `3` |
| `[[0,0],1]` | `0` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Mantén longitud actual y mejor separadas.

</details>

<details>
<summary>Pista 2</summary>

Pon longitud actual a cero en valor no válido.

</details>

<details>
<summary>Pista 3</summary>

Actualiza mejor tras extender racha; no sumes rachas separadas.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Contador actual describe sufijo válido que termina en posición actual. Reiniciar al fallar conserva contigüidad. Guardar máximo trata racha al inicio, medio o final.

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
