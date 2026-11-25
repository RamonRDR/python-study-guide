# Programación manual y depuración

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../../practical-projects/08-simulated-automation-flow/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../02-specification-driven-development/README.es.md)
<!-- /chapter-navigation:top -->

## Objetivo y requisitos previos

**Nivel:** principiante tras el currículo central. **Tiempo estimado:** 35–50 minutos. Repasa [funciones](../../functions/README.es.md), [excepciones](../../errors-files-and-modules/01-try-except-else-finally/README.es.md) y [Git básico](../../getting-started/06-git-and-version-control/README.es.md) si hace falta. Aprende a reproducir, diagnosticar y corregir un error pequeño por tu cuenta. Usa una carpeta de práctica separada, no los archivos fuente del repositorio.

## 1. Piensa antes de escribir

Anota entrada, salida y un pequeño ejemplo a mano. Un registro de lectura debe informar páginas restantes: total 20, leídas 7, esperado 13. Predice antes de ejecutar. Divide en pasos, escribe el código más simple, ejecútalo, observa y explica. Registra intentos; un intento fallido aporta evidencia.

## 2. Reproduce un defecto

Crea `practice.py` y escribe este ejemplo intencionalmente incorrecto (no es una solución ejecutable publicada):

```python
def remaining_pages(total_pages, pages_read):
    return total_pages + pages_read

print(remaining_pages(20, 7))
```

Ejecuta `python practice.py` con el intérprete comprobado. Lo esperado es 13; el código imprime 27. Es un error lógico: la ejecución terminó, pero el comportamiento es incorrecto. Inspecciona operandos, sigue la expresión en papel y corrige el operador por tu cuenta. Prueba (20, 0) y (20, 20). Un caso correcto no demuestra corrección.

## 3. Lee errores de abajo hacia arriba

Un error de sintaxis impide analizar; una excepción durante la ejecución interrumpe el flujo; un error lógico puede producir una salida plausible pero incorrecta. En un archivo desechable, cambia la llamada a `remaining_pages(20, "7")` tras corregir el operador. Lee el traceback: empieza por tipo y mensaje de excepción al final, después encuentra el frame relevante y la línea de código. Mensajes y números de línea dependen del intérprete y archivo. Comprueba valores y tipos en vez de suprimir la excepción.

Usa `print(repr(value), type(value).__name__)` con un nombre de variable real para inspeccionar un valor; elimina diagnósticos temporales tras corregir. Opcionalmente, coloca un breakpoint en VS Code, usa el depurador Python e inspecciona variables locales. El depurador ayuda a investigar; no decide el comportamiento deseado.

## 4. Consulta documentación y prueba una hipótesis

Lee el [tutorial Python sobre errores y excepciones](https://docs.python.org/3.13/tutorial/errors.html) o usa `help()` para un objeto conocido. Identifica primero la pregunta exacta. Cambia una cosa a la vez; compara esperado y obtenido. Si te bloqueas, busca una pista o explicación, no una respuesta completa. Intenta de nuevo sin mirar la referencia. Nunca envíes código privado, credenciales o datos a un servicio público.

## 5. Práctica independiente

- Predice resultados para (0, 0), (20, 0), (20, 20).
- Identifica el comportamiento faltante para valores negativos, excesivos y no enteros; no inventes la regla. Registra preguntas para la siguiente lección.
- En otro archivo, reproduce un error de sintaxis (por ejemplo, paréntesis sin cerrar) y corrígelo.
- Explica la diferencia entre errores de sintaxis, ejecución y lógica sin leer la respuesta.

**Referencia rápida:** reproducir, predecir, inspeccionar, formular hipótesis, cambiar una cosa, volver a ejecutar, probar límites, explicar. Después especifica qué significa el comportamiento válido.

<!-- chapter-navigation:bottom -->
[← Anterior](../../practical-projects/08-simulated-automation-flow/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../02-specification-driven-development/README.es.md)
<!-- /chapter-navigation:bottom -->
