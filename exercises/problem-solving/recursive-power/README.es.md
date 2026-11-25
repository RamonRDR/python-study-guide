# Potencia entera recursiva

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.recursive-power` · **Dificultad:** Media · 20 min

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
- [04-recursion](../../../problem-solving-and-live-coding/04-recursion/README.es.md)

## Contrato

Dados base entera de -10 a 10 y exponente de 0 a 10, calcula base elevada al exponente por multiplicación recursiva, sin ** ni pow. Define exponente cero como 1, incluido 0**0.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

Escribe pseudocódigo e implementa de forma independiente antes de abrir la referencia.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def integer_power(base: int, exponent: int) -> int:
    raise NotImplementedError("Implement integer_power")
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[2,3]` | `8` |
| `[0,0]` | `1` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Usa el exponente como argumento decreciente.

</details>

<details>
<summary>Pista 2</summary>

Cuando exponente sea cero, devuelve uno.

</details>

<details>
<summary>Pista 3</summary>

Multiplica base por el resultado para exponente menos uno.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

El paso recursivo reduce el exponente, no la base; bases negativas funcionan porque cada paso multiplica por la base original.

- Tiempo: O(e)
- Espacio auxiliar: O(e)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.es.md) · [Índice de ejercicios](../../README.es.md)
