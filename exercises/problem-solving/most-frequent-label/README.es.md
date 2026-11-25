# Etiqueta más frecuente

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.most-frequent-label` · **Dificultad:** Media · 25 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.es.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.es.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)

## Contrato

Devuelve etiqueta exacta de mayor frecuencia total. En empate elige etiqueta que apareció primero en lista original. Entrada vacía devuelve None; cadena vacía es válida. Conserva entrada y busca tiempo lineal esperado.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Escribe pseudocódigo e implementa de forma independiente antes de abrir la referencia.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def most_frequent_label(labels: list[str]) -> str | None:
    raise NotImplementedError("Implement most_frequent_label")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `null` |
| `[["b","a","a","b"]]` | `"b"` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Construye mapa final de frecuencias antes de elegir ganador.

</details>

<details>
<summary>Pista 2</summary>

Recorre etiquetas originales otra vez comparando conteos finales.

</details>

<details>
<summary>Pista 3</summary>

Cambia ganador solo con frecuencia estrictamente mayor, no igual.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Una pasada completa de frecuencias seguida de selección de izquierda a derecha respeta empates por primera aparición. Mejora estricta conserva ganador anterior.

- Tiempo: O(n) esperado
- Espacio auxiliar: O(k)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/15-mixed-challenges/README.es.md) · [Índice de ejercicios](../../README.es.md)
