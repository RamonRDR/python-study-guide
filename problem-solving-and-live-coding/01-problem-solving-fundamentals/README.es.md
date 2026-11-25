# Fundamentos de resolución de problemas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../../manual-programming-practices/04-professional-workflow/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../02-constraints-and-edge-cases/README.es.md)
<!-- /chapter-navigation:top -->

**Requisitos previos:** [Program Flow](../../program-flow/08-choosing-and-combining-program-flow/README.es.md) · [Functions](../../functions/08-functions-working-together/README.es.md) · [SDD](../../manual-programming-practices/02-specification-driven-development/README.es.md)

## Objetivo

Convertir una petición en un programa pequeño y comprobable antes de abrir el editor (25–35 minutos).

## 1. Leer, reformular y modelar

Un club de lectura ficticio registra minutos enteros de estudio por día. Dada una lista de enteros no negativos, devuelve el total de los días que alcanzaron la meta de 20 minutos. Aquí “total” significa **suma de minutos**, no cantidad de días. La entrada vacía da cero; la lista original no cambia. Aclara requisitos ambiguos antes de programar. Para `[12, 20, 25]`, los valores que cumplen son 20 y 25, así que la respuesta es 45.

## 2. Descomponer y rastrear

Divide en identificar un valor válido, acumular los minutos que cumplen y devolver el resultado. Escribe pseudocódigo independiente del lenguaje: iniciar total en cero; para cada valor, si alcanza la meta, sumarlo; devolver total tras iterar. El rastreo del ejemplo es 0 → 0 → 20 → 45. El acumulador representa la suma de los valores válidos ya procesados. Usa un bucle en vez de tres índices fijos y una función en vez de imprimir dentro del bucle para poder comprobar el retorno.

## 3. Implementar y verificar

El ejemplo compartido usa una meta configurable, 20 por defecto. Intenta escribirlo primero; después compara con el [ejemplo](examples/study_minutes.py). El contrato supone entradas y meta enteras no negativas; no exige validación adicional. Prueba entrada vacía, justo el límite, ausencia de coincidencias y valores repetidos. Si devolver demasiado pronto produce 0, rastrea la indentación y mueve el retorno fuera del bucle.

## Práctica

Cambia el requisito ficticio: devuelve la **cantidad** de días válidos, no los minutos. Escribe dos ejemplos calculados a mano, pseudocódigo y una función antes de consultar una solución. Explica por qué difieren los contratos. Para el ejemplo original, la nueva respuesta es 2.

**Referencia rápida:** contrato → ejemplos → descomposición → rastreo → código → pruebas → explicación.

Ejecuta desde el directorio de la lección (Python 3.13 como base):

```bash
python examples/study_minutes.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../../manual-programming-practices/04-professional-workflow/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../02-constraints-and-edge-cases/README.es.md)
<!-- /chapter-navigation:bottom -->
