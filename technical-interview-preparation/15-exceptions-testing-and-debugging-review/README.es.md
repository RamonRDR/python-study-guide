# Repaso de excepciones, pruebas y depuración

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../14-concurrency-parallelism-and-the-gil/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../16-http-rest-and-backend-fundamentals/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.es.md)
- [external-libraries/04-pytest](../../external-libraries/04-pytest/README.es.md)
- [manual-programming-practices/01-manual-coding-and-debugging](../../manual-programming-practices/01-manual-coding-and-debugging/README.es.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.es.md)

## Fronteras de excepción

Las excepciones comunican fallos entre llamadas. Captura excepción específica esperada donde puedas recuperar o traducir; errores inesperados normalmente se propagan hasta una frontera externa apropiada. `raise` en handler relanza excepción activa; `raise NewError(...) from error` conserva causa explícita. `else` ejecuta tras trabajo protegido exitoso; `finally` gestiona salida, no éxito. No retornes desde finally para ocultar error. Gestores de contexto aclaran limpieza de recursos.

```python
try:
    value = int("unknown")
except ValueError as error:
    raise ValueError("invalid quantity") from error
```

Esto lanza una excepción intencionadamente con su causa; no es conversión exitosa. Ejemplo compartido acepta cadenas admitidas por int, incluyendo espacios externos, y exige resultado no negativo. No convierte entrada incorrecta silenciosamente en cero.

## Probar y depurar con evidencias

Pruebas unitarias verifican comportamiento pequeño con dependencias controladas; integración cruza fronteras reales; extremo a extremo ejercita flujo completo compatible. Usa Arrange/Act/Assert, aserciones significativas de igualdad o excepción, entradas límite y setup/teardown deterministas. Fake puede sustituir dependencia de red, pero prueba frontera real por separado. Parametrización varía entradas; fixtures suministran y liberan dependencias. Prueba verde en código intencionalmente incorrecto indica oráculo débil, no prueba corrección. Cobertura mide ejecución, no corrección.

Secuencia de depuración: reproduce con entrada mínima, lee traceback del frame que falló y sus llamadores, formula hipótesis, inspecciona estado relevante con debugger (`breakpoint()`) o logs estructurados, cambia una causa y añade prueba de regresión. Oculta secretos y payloads sensibles. Evita capturas amplias o reintentos sin entender fallo.

## Práctica

Predice salidas válidas e inválidas de parse_quantity, verifica cero y negativos y comprueba causa de excepción. Retorna cero temporalmente para texto inválido en tu copia; prueba negativa debe fallar. Explica qué prueba detecta cada defecto.

**Referencia rápida:** captura específica; conserva causa; reproduce; prueba comportamiento; verifica regresión.

## Ejemplo ejecutable compartido

[parse_quantity.py](examples/parse_quantity.py)

`python technical-interview-preparation/15-exceptions-testing-and-debugging-review/examples/parse_quantity.py`

## Referencias oficiales

- [docs.python.org/3.13/tutorial/errors.html](https://docs.python.org/3.13/tutorial/errors.html)
- [docs.python.org/3.13/library/unittest.html](https://docs.python.org/3.13/library/unittest.html)
- [docs.python.org/3.13/library/pdb.html](https://docs.python.org/3.13/library/pdb.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../14-concurrency-parallelism-and-the-gil/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../16-http-rest-and-backend-fundamentals/README.es.md)
<!-- /chapter-navigation:bottom -->
