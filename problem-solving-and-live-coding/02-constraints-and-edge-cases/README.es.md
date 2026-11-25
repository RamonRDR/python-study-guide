# Restricciones y casos límite

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../01-problem-solving-fundamentals/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../03-algorithmic-complexity/README.es.md)
<!-- /chapter-navigation:top -->

**Requisitos previos:** [Parameters](../../functions/02-parameters-and-arguments/README.es.md) · [Return values](../../functions/03-return-values/README.es.md) · [pytest](../../external-libraries/04-pytest/README.es.md) · [TDD](../../manual-programming-practices/03-test-driven-development/README.es.md)

## Objetivo

Convertir restricciones de entrada en comportamiento explícito y pruebas útiles (25–35 minutos).

## 1. Dominio y límites

Un taller ficticio acepta un grupo si su tamaño está entre 1 y la capacidad de la sala, inclusive. Ambos argumentos deben ser enteros exactos (no booleanos); la capacidad debe ser al menos 1 y el tamaño no negativo. Devuelve un booleano para argumentos válidos, lanza TypeError para tipos incorrectos antes de comprobar valores y ValueError para valores inválidos. No impongas límites arbitrarios ajenos al contrato.

| Grupo | Capacidad | Esperado |
| --- | --- | --- |
| 0 | 5 | False |
| 1 | 5 | True |
| 5 | 5 | True |
| 6 | 5 | False |
| -1 | 5 | ValueError |
| 2 | 0 | ValueError |
| True | 5 | TypeError |

Un caso límite es una frontera o condición válida poco usual; una entrada inválida viola el contrato. Prueba por debajo, en y por encima de cada límite relevante. Un error de tipo difiere de una reserva válida pero rechazada.

## 2. Convertir ejemplos en pruebas

Escribe el resultado esperado independientemente de la implementación. Usa igualdad exacta para booleanos y comprueba tipos de excepción para entradas inválidas. En Python, `isinstance(True, int)` es verdadero; el requisito de entero exacto exige `type(value) is int`. Usa una comparación inclusiva solo tras validar los argumentos. Consulta el [ejemplo](examples/capacity.py). Una solución con límite superior estricto fallaría cuando tamaño iguala capacidad; esto comprueba la capacidad de detectar errores. Evita probar el texto de excepciones salvo que el contrato lo exija.

## Práctica

Crea una tabla de límites para una taquilla ficticia que acepta pesos de 1 a 10 unidades enteras, inclusive. Especifica qué entradas lanzan errores y cuáles devuelven False antes de programar. Añade un caso que detecte cambiar `<=` por `<`. Explica por qué probar solo valores típicos es insuficiente.

**Referencia rápida:** define dominio válido, resultado esperado, política de entradas inválidas y pruebas de límites antes de programar.

Ejecuta desde el directorio de la lección (Python 3.13 como base):

```bash
python examples/capacity.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../01-problem-solving-fundamentals/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../03-algorithmic-complexity/README.es.md)
<!-- /chapter-navigation:bottom -->
