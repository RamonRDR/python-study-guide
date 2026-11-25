# Live coding cronometrado

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../15-mixed-challenges/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:top -->

## Preparación antes de comenzar

Repasa [fundamentos](../01-problem-solving-fundamentals/README.es.md), [casos límite](../02-constraints-and-edge-cases/README.es.md), [complejidad](../03-algorithmic-complexity/README.es.md) y [patrones](../07-problem-solving-patterns/README.es.md). Usa temporizador personal y Python 3.13 local; no hay ejecutor en navegador. Practica un reto a la vez. Lee enunciado y herramientas permitidas; sin IA, pistas ni soluciones en primer intento. Puedes ejecutar código y pruebas propios. No sacrifiques claridad ni corrección por velocidad.

## Dos planes de práctica

| Actividad | 10 min | 20 min |
| --- | ---: | ---: |
| Leer y aclarar contrato, ejemplos | 2 | 3 |
| Planear y rastrear | 2 | 4 |
| Implementar | 4 | 9 |
| Probar y explicar | 2 | 4 |

Si te bloqueas, declara supuesto necesario o escribe paso mínimo comprobable. Al límite registra estado (no iniciado, parcial, completo), tiempo y fallos conocidos; para reloj. Termina sin presión, revela pistas/referencia y vuelve a intentar más tarde. Tiempo autorregistrado, no nota ni medida de preparación laboral.

## Rachas contiguas

Contar todos válidos difiere de contar racha contigua. Guarda longitud actual y máxima. Extiende contador actual al cumplir; ponlo a cero al fallar. Para condición >= 2 y [2, 3, 0, 2], longitudes 1, 2, 0, 1; mejor 2. Actual describe sufijo válido, no total. Combina acumulador y condición con variables auxiliares constantes.

## Autoevaluación tras intento

Registra un punto por criterio cumplido: contrato/casos límite claros, plan justificado, comportamiento correcto en tus casos, implementación legible y explicación tiempo/espacio. Usa 0–5 solo para retroalimentación personal; sin evaluación automática de explicaciones o tiempo. Registra mejora y próximo paso.

## Retos disponibles

- [Cronometrado: contar por límite](../../exercises/problem-solving/timed-threshold-count/README.es.md) · Fácil · 10 min
- [Cronometrado: mayor racha válida](../../exercises/problem-solving/timed-longest-streak/README.es.md) · Media · 20 min

<!-- chapter-navigation:bottom -->
[← Anterior](../15-mixed-challenges/README.es.md) · [Índice del módulo](../README.es.md)
<!-- /chapter-navigation:bottom -->
