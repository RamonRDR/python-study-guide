# Gestores de contexto

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../12-closures-and-decorators/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../14-concurrency-parallelism-and-the-gil/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [errors-files-and-modules/03-open-and-with](../../errors-files-and-modules/03-open-and-with/README.es.md)
- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.es.md)
- [technical-interview-preparation/11-iterators-generators-and-comprehensions](../../technical-interview-preparation/11-iterators-generators-and-comprehensions/README.es.md)
- [technical-interview-preparation/12-closures-and-decorators](../../technical-interview-preparation/12-closures-and-decorators/README.es.md)

## Protocolo with

Un gestor de contexto encapsula adquisición y liberación alrededor de un bloque. La instrucción `with manager as value:` llama `__enter__()`; su retorno se convierte en value. Tras entrada exitosa, `__exit__(exc_type, exc_value, traceback)` recibe detalles de excepción o tres None. Un retorno truthy suprime excepción del cuerpo; false o None deja propagar. Si entrada falla, exit de ese gestor no se llama. El fallo de limpieza también puede lanzar. No trates `with` como supresor automático.

```python
class Marker:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("close")
        return False

with Marker():
    print("work")
```

Salida open, work, close en líneas separadas. Una clase puede gestionar recurso mediante esos métodos especiales. Alternativamente `contextlib.contextmanager` convierte función generadora con exactamente un yield en fábrica de gestores. Pon limpieza en finally alrededor del yield. Excepción del cuerpo se inyecta en el punto del yield; si se captura solo para registro, relánzala salvo que supresión sea contrato intencional.

## Decisiones prácticas

Ejemplo compartido registra open/work/close en lista en vez de acceder a recurso externo. Prueba finalización normal y fallo del cuerpo. Gestor producido por contextmanager normalmente es de uso único; llama fábrica otra vez. Usa `ExitStack` cuando debas gestionar cantidad variable de gestores. Evita gestor personalizado cuando los de archivo o lock incorporados ya expresan contrato.

## Práctica

Lanza RuntimeError dentro del ejemplo y verifica limpieza exactamente una vez mientras excepción se propaga. Explica qué cambia si entrada falla antes de terminar adquisición. Compara try/finally explícito con gestor reutilizable.

**Referencia rápida:** enter devuelve enlace; exit limpia; exit truthy suprime excepción del cuerpo; entrada exitosa es frontera.

## Ejemplo ejecutable compartido

[managed_session.py](examples/managed_session.py)

`python technical-interview-preparation/13-context-managers/examples/managed_session.py`

## Referencias oficiales (Python 3.13)

- [Python 3.13: reference/compound_stmts.html#the-with-statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-with-statement)
- [Python 3.13: library/contextlib.html](https://docs.python.org/3.13/library/contextlib.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../12-closures-and-decorators/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../14-concurrency-parallelism-and-the-gil/README.es.md)
<!-- /chapter-navigation:bottom -->
