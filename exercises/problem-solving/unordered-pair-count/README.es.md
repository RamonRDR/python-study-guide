# Contar pares no ordenados

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.unordered-pair-count` · **Dificultad:** Fácil · 12 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [03-int-float-and-bool](../../../strings-and-numbers/03-int-float-and-bool/README.es.md)
- [04-numeric-builtins](../../../strings-and-numbers/04-numeric-builtins/README.es.md)

## Contrato

Dado entero no negativo size <= 10**6, devuelve cantidad de pares distintos de posiciones diferentes, sin considerar orden. Cada posición combina con size-1 otras; esto cuenta cada par dos veces. Usa aritmética, no bucles.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Escribe pseudocódigo e implementa de forma independiente antes de abrir la referencia.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def pair_count(size: int) -> int:
    raise NotImplementedError("Implement pair_count")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[0]` | `0` |
| `[1]` | `0` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Cuenta primero pares ordenados de posiciones distintas.

</details>

<details>
<summary>Pista 2</summary>

Cada par no ordenado aparece dos veces; divide por dos.

</details>

<details>
<summary>Pista 3</summary>

Usa división entera para devolver entero, incluidos tamaños cero y uno.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

El producto n(n-1) cuenta pares ordenados; división exacta por dos elimina orientaciones duplicadas. No hay iteración bajo el modelo de enteros acotados declarado.

- Tiempo: O(1)
- Espacio auxiliar: O(1)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.es.md) · [Índice de ejercicios](../../README.es.md)
