# Closures e decorators

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../11-iterators-generators-and-comprehensions/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../13-context-managers/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [functions/04-scope](../../functions/04-scope/README.pt-BR.md)
- [functions/06-default-values](../../functions/06-default-values/README.pt-BR.md)
- [technical-interview-preparation/06-attributes-methods-and-object-behavior](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.pt-BR.md)

## Closures e escopo

Closure é função que mantém acesso a vinculações de função envolvente. Busca LEGB explica como as encontra. `nonlocal` permite reatribuir variável existente da função envolvente, não global do módulo. Cada chamada à fábrica externa pode criar estado independente.

```python
def make_multiplier(factor):
    def multiply(value):
        return factor * value
    return multiply

double = make_multiplier(2)
print(double(5))
```

Saída: 10. Closures capturam vinculações, não snapshots automáticos de valores. Loop criando lambdas referentes ao índice mutável pode fazer todas lerem o índice final. Para snapshot, vincule argumento padrão (para valores imutáveis) ou use chamada separada à fábrica. Closures podem manter objetos referenciados vivos.

## Decorators

Decorator transforma função ou classe no momento da definição. Para decorator único de função, `@decorate` sobre definição é aproximadamente reatribuição `function = decorate(function)` após criação. Fábrica de decorator aceita configuração e retorna decorator; empilhados aplicam-se do mais próximo da definição para cima. No exemplo compartilhado, `record_calls(records)` retorna decorator cujo wrapper encaminha argumentos posicionais e nomeados, registra cada tentativa e retorna resultado original ou propaga exceção. `functools.wraps` preserva metadados úteis e expõe `__wrapped__`; não preserva automaticamente todo comportamento nem torna wrapper síncrono adequado a funções async.

## Prática

Crie dois contadores e confirme estado independente. Decore cálculo e teste chamadas posicionais e nomeadas, retorno, metadados e exceção levantada. Explique por que wrapper não deve engolir erros por padrão. Use decorators para comportamento transversal consistente; evite ocultar fluxo ou efeitos colaterais quando chamadas explícitas forem mais claras.

**Referência rápida:** closure retém vinculações externas; nonlocal reatribui; decorator transforma; wrapper encaminha.

## Exemplo executável compartilhado

[call_counter.py](examples/call_counter.py)

`python technical-interview-preparation/12-closures-and-decorators/examples/call_counter.py`

## Referências oficiais (Python 3.13)

- [Python 3.13: tutorial/classes.html#python-scopes-and-namespaces](https://docs.python.org/3.13/tutorial/classes.html#python-scopes-and-namespaces)
- [Python 3.13: reference/compound_stmts.html#function-definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13: library/functools.html#functools.wraps](https://docs.python.org/3.13/library/functools.html#functools.wraps)

<!-- chapter-navigation:bottom -->
[← Anterior](../11-iterators-generators-and-comprehensions/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../13-context-managers/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
