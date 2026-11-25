# Refactorizar tarifa de envío

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.refactor-shipping-fee` · **Dificultad:** Fácil · 15 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [01-conditions-comparisons-and-boolean-logic](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.es.md)
- [02-if-elif-and-else](../../../program-flow/02-if-elif-and-else/README.es.md)
- [06-pep8-and-readability](../../../comments-and-documentation/06-pep8-and-readability/README.es.md)
- [03-test-driven-development](../../../manual-programming-practices/03-test-driven-development/README.es.md)

## Contrato

Refactoriza código inicial funcional sin cambiar comportamiento. Para totales no negativos en unidades ficticias, envío es gratis con total >= 100 o para miembros; si no cuesta 12. Usa condición combinada clara y evita retornos duplicados.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

El inicial ya pasa pruebas funcionales. Conserva comportamiento, haz cambio estructural solicitado e inspecciona el diff. Pruebas de salida no evalúan legibilidad ni elección de algoritmo.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def shipping_fee(total: int, member: bool) -> int:
    if total >= 100:
        return 0
    if member:
        return 0
    return 12
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[99,false]` | `12` |
| `[100,false]` | `0` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Escribe casos límite antes de editar.

</details>

<details>
<summary>Pista 2</summary>

Identifica dos ramas con mismo retorno.

</details>

<details>
<summary>Pista 3</summary>

Combina condiciones con or y conserva tarifa alternativa.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Las dos condiciones de gratuidad forman OR inclusivo. Consolidarlas conserva salida y hace visible la regla de negocio.

- Tiempo: O(1)
- Espacio auxiliar: O(1)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/14-refactoring-challenges/README.es.md) · [Índice de ejercicios](../../README.es.md)
