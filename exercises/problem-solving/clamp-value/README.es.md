# Limitar un valor

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.clamp-value` · **Dificultad:** Fácil · 10 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [02-if-elif-and-else](../../../program-flow/02-if-elif-and-else/README.es.md)

## Contrato

Dados enteros con lower <= upper, devuelve lower si value está por debajo, upper si por encima, si no value. Límites iguales son válidos.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Escribe pseudocódigo e implementa de forma independiente antes de abrir la referencia.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def clamp_value(value: int, lower: int, upper: int) -> int:
    raise NotImplementedError("Implement clamp_value")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[2,3,9]` | `3` |
| `[10,3,9]` | `9` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Compara valor con límite inferior.

</details>

<details>
<summary>Pista 2</summary>

Compara con límite superior si hace falta.

</details>

<details>
<summary>Pista 3</summary>

Devuelve el valor original si ninguna condición se cumple.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Retornos tempranos separan explícitamente los tres resultados mutuamente excluyentes.

- Tiempo: O(1)
- Espacio auxiliar: O(1)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.es.md) · [Índice de ejercicios](../../README.es.md)
