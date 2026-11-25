# Mayor subcadena sin repetición

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.longest-distinct-substring` · **Dificultad:** Difícil · 35 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [01-string-creation-and-indexing](../../../strings-and-numbers/01-string-creation-and-indexing/README.es.md)
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.es.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.es.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)
- [08-strings-and-numbers](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.es.md)

## Contrato

Devuelve la longitud de la mayor subcadena contigua sin caracteres exactos repetidos. Entrada vacía devuelve 0. Compara caracteres Python originales, sin normalizar. Busca tiempo lineal esperado.

Solo se evalúan dominios declarados. Devuelve tipos y valores exactos; no imprimas, modifiques entradas ni añadas dependencias. Elección algorítmica y complejidad requieren revisión manual; pruebas funcionales no las demuestran.

Copia el inicial a directorio personal; Python 3.13 es la base. Ejecución en navegador sin verificar.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def longest_distinct_length(text: str) -> int:
    raise NotImplementedError("Implement longest_distinct_length")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[""]` | `0` |
| `["abba"]` | `2` |
| `["abcabcbb"]` | `3` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Registra última posición de cada carácter.

</details>

<details>
<summary>Pista 2</summary>

Si repetición está dentro de ventana actual, mueve límite izquierdo tras última aparición.

</details>

<details>
<summary>Pista 3</summary>

Nunca muevas left hacia atrás; actualiza mejor longitud tras registrar posición actual.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

La ventana actual tiene caracteres únicos. Repetición invalida solo posiciones hasta aparición anterior dentro de ventana. max(left, previous + 1) conserva progreso monótono. Cada extremo derecho se visita una vez.

- Tiempo: O(n) esperado
- Espacio auxiliar: O(k)

Modelo de coste fijo para enteros acotados y etiquetas de longitud acotada, comportamiento hash esperado cuando aplica. n/m son tamaños (en listas anidadas n cuenta elementos y nodos de lista visitados), k claves distintas, h profundidad. Salida requerida excluida de espacio auxiliar; recursividad usa O(h) marcos.

</details>

## Validación

Comprueba tus propias llamadas manualmente y añade casos límite. Desde raíz del repositorio, el comando siguiente prueba referencias e implementaciones incorrectas conocidas, no tu código personal. Soluciones públicas son visibles; sin evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.es.md) · [Índice de ejercicios](../../README.es.md)
