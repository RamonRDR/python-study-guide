# Combinar inventarios

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.merge-inventory` · **Dificultad:** Media · 18 min

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
- [09-data-flow-between-functions](../../../functions/09-data-flow-between-functions/README.es.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.es.md)

## Contrato

Dados dos diccionarios de etiquetas exactas y cantidades enteras no negativas, devuelve uno nuevo sumando cantidades de claves compartidas. Conserva cantidades cero y ambas entradas.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Escribe pseudocódigo e implementa de forma independiente antes de abrir la referencia.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def merge_inventory(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    raise NotImplementedError("Implement merge_inventory")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[{},{}]` | `{}` |
| `[{"a":2},{"a":3,"b":1}]` | `{"a":5,"b":1}` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Crea una copia del primer diccionario.

</details>

<details>
<summary>Pista 2</summary>

Recorre claves y valores del segundo diccionario.

</details>

<details>
<summary>Pista 3</summary>

Usa cero como valor por defecto para clave ausente y suma la cantidad.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Copiar evita modificar los datos del llamador. Acumular en lugar de sobrescribir conserva totales de claves compartidas.

- Tiempo: O(n+m) esperado
- Espacio auxiliar: O(1) excluyendo salida

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/09-collections/README.es.md) · [Índice de ejercicios](../../README.es.md)
