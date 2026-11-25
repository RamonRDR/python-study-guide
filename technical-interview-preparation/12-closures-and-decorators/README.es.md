# Cierres y decoradores

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../11-iterators-generators-and-comprehensions/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../13-context-managers/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [functions/04-scope](../../functions/04-scope/README.es.md)
- [functions/06-default-values](../../functions/06-default-values/README.es.md)
- [technical-interview-preparation/06-attributes-methods-and-object-behavior](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.es.md)

## Cierres y ámbito

Un cierre es una función que conserva acceso a enlaces de una función envolvente. La búsqueda LEGB explica cómo los encuentra. `nonlocal` permite reasignar variable existente de función envolvente, no global de módulo. Cada llamada a la fábrica externa puede crear estado independiente.

```python
def make_multiplier(factor):
    def multiply(value):
        return factor * value
    return multiply

double = make_multiplier(2)
print(double(5))
```

Salida: 10. Los cierres capturan enlaces, no instantáneas automáticas de valores. Un bucle creando lambdas referentes al índice cambiante puede hacer que todas lean el índice final. Para instantánea, enlaza argumento predeterminado (para valores inmutables) o usa llamada separada a fábrica. Los cierres pueden mantener vivos objetos referenciados.

## Decoradores

Un decorador transforma función o clase al definirla. Para decorador único de función, `@decorate` sobre definición equivale aproximadamente a reasignar `function = decorate(function)` tras creación. Una fábrica de decoradores acepta configuración y devuelve decorador; apilados se aplican desde el más cercano a la definición hacia arriba. En el ejemplo compartido, `record_calls(records)` devuelve decorador cuyo wrapper reenvía argumentos posicionales y nombrados, registra cada intento y devuelve resultado original o propaga excepción. `functools.wraps` conserva metadatos útiles y expone `__wrapped__`; no conserva automáticamente todo comportamiento ni hace adecuado un wrapper síncrono para funciones async.

## Práctica

Crea dos contadores y confirma estado independiente. Decora cálculo y prueba llamadas posicionales y nombradas, retorno, metadatos y excepción lanzada. Explica por qué wrapper no debe ocultar errores por defecto. Usa decoradores para comportamiento transversal consistente; evita ocultar flujo o efectos secundarios cuando llamadas explícitas sean más claras.

**Referencia rápida:** cierre conserva enlaces externos; nonlocal reasigna; decorador transforma; wrapper reenvía.

## Ejemplo ejecutable compartido

[call_counter.py](examples/call_counter.py)

`python technical-interview-preparation/12-closures-and-decorators/examples/call_counter.py`

## Referencias oficiales (Python 3.13)

- [Python 3.13: tutorial/classes.html#python-scopes-and-namespaces](https://docs.python.org/3.13/tutorial/classes.html#python-scopes-and-namespaces)
- [Python 3.13: reference/compound_stmts.html#function-definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13: library/functools.html#functools.wraps](https://docs.python.org/3.13/library/functools.html#functools.wraps)

<!-- chapter-navigation:bottom -->
[← Anterior](../11-iterators-generators-and-comprehensions/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../13-context-managers/README.es.md)
<!-- /chapter-navigation:bottom -->
