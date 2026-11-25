# Aplanar listas anidadas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.recursive-flatten` · **Dificultad:** Difícil · 35 min

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
- [05-type-and-isinstance](../../../fundamentals/05-type-and-isinstance/README.es.md)
- [04-recursion](../../../problem-solving-and-live-coding/04-recursion/README.es.md)
- [09-data-flow-between-functions](../../../functions/09-data-flow-between-functions/README.es.md)
- [10-functions-and-recursion](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.es.md)
- [04-scope](../../../functions/04-scope/README.es.md)
- [08-functions-working-together](../../../functions/08-functions-working-together/README.es.md)

## Contrato

Dada lista anidada finita con solo enteros y listas, con hasta 10 niveles de listas bajo la exterior, devuelve nueva lista plana de enteros en orden izquierda-derecha en profundidad. Conserva duplicados y entrada. Usa recursividad; no hay ciclos ni referencias mutables compartidas.

Solo se evalúan dominios declarados. Devuelve tipos y valores exactos; no imprimas, modifiques entradas ni añadas dependencias. Elección algorítmica y complejidad requieren revisión manual; pruebas funcionales no las demuestran.

Copia el inicial a directorio personal; Python 3.13 es la base. Ejecución en navegador sin verificar.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def flatten(values: list) -> list[int]:
    raise NotImplementedError("Implement flatten")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `[]` |
| `[[1,[2,[3]],4]]` | `[1,2,3,4]` |
| `[[[[]],[],[0]]]` | `[0]` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Usa una lista de resultado compartida por función auxiliar recursiva.

</details>

<details>
<summary>Pista 2</summary>

Por cada elemento, distingue lista de entero.

</details>

<details>
<summary>Pista 3</summary>

Visita lista interna inmediatamente; añade entero directamente.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Auxiliar recorre cada lista en orden y añade cada entero hoja una vez. Listas vacías no añaden nada. Un acumulador de salida evita copias repetidas; profundidad de pila es profundidad de anidamiento.

- Tiempo: O(n)
- Espacio auxiliar: O(h)

Modelo de coste fijo para enteros acotados y etiquetas de longitud acotada, comportamiento hash esperado cuando aplica. n/m son tamaños (en listas anidadas n cuenta elementos y nodos de lista visitados), k claves distintas, h profundidad. Salida requerida excluida de espacio auxiliar; recursividad usa O(h) marcos.

</details>

## Validación

Comprueba tus propias llamadas manualmente y añade casos límite. Desde raíz del repositorio, el comando siguiente prueba referencias e implementaciones incorrectas conocidas, no tu código personal. Soluciones públicas son visibles; sin evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.es.md) · [Índice de ejercicios](../../README.es.md)
