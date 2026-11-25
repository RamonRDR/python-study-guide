# Refactorizar resumen de notas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.refactor-score-summary` · **Dificultad:** Media · 22 min

## Requisitos previos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.es.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.es.md)
- [03-return-values](../../../functions/03-return-values/README.es.md)
- [05-type-hints](../../../functions/05-type-hints/README.es.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.es.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.es.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.es.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.es.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.es.md)
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.es.md)
- [06-pep8-and-readability](../../../comments-and-documentation/06-pep8-and-readability/README.es.md)
- [03-test-driven-development](../../../manual-programming-practices/03-test-driven-development/README.es.md)

## Contrato

Refactoriza inicial funcional para notas enteras 0–100. Devuelve diccionario con conteos total, passed y failed; nota >= 60 aprueba. Conserva entrada. Usa nombres descriptivos y una pasada de clasificación; revisa claridad manualmente.

Solo se evalúa el dominio declarado; devuelve valor y tipos exactos, sin imprimir, dependencias externas ni modificar argumentos mutables. No uses la referencia durante el intento independiente.

El inicial ya pasa pruebas funcionales. Conserva comportamiento, haz cambio estructural solicitado e inspecciona el diff. Pruebas de salida no evalúan legibilidad ni elección de algoritmo.

Copia el código inicial a un directorio personal de práctica. Python 3.13 es la base; ejecución en navegador no verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def summarize_scores(scores: list[int]) -> dict[str, int]:
    a = 0
    for x in scores:
        if x >= 60:
            a += 1
    b = 0
    for x in scores:
        if x < 60:
            b += 1
    return {"total": len(scores), "passed": a, "failed": b}
```

## Ejemplos (argumentos posicionales)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `{"total":0,"passed":0,"failed":0}` |
| `[[59,60,61]]` | `{"total":3,"passed":2,"failed":1}` |

## Pistas progresivas

<details>
<summary>Pista 1</summary>

Conserva contrato y escribe pruebas límite alrededor de 60.

</details>

<details>
<summary>Pista 2</summary>

Cuenta aprobados en un bucle con variable descriptiva.

</details>

<details>
<summary>Pista 3</summary>

Calcula failed como total menos passed; verifica casos originales.

</details>

## Referencia y explicación

<details>
<summary>Mostrar tras intentar</summary>

[Solución de referencia](solution.py)

Cada nota aprueba o falla, así que failed es total menos passed. Un bucle de clasificación evita trabajo repetido. Pruebas comprueban comportamiento, no legibilidad.

- Tiempo: O(n)
- Espacio auxiliar: O(1)

Complejidad usa modelo de coste fijo para enteros acotados y etiquetas de longitud acotada; n es longitud de entrada, m longitud de segunda, k valores distintos, d dígitos decimales, e exponente, según corresponda. Se excluye almacenamiento de salida del espacio auxiliar. Tiempos con hash son esperados, no cotas de peor caso.

</details>

## Validación

Comprueba tus propias llamadas manualmente con los casos declarados y añade al menos dos casos límite. El comando siguiente en la raíz prueba solo referencias e implementaciones incorrectas conocidas, no tu archivo personal. Respuestas públicas son visibles; no se usa evaluación por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de prueba](test_solution.py) · [Volver a la lección](../../../problem-solving-and-live-coding/14-refactoring-challenges/README.es.md) · [Índice de ejercicios](../../README.es.md)
