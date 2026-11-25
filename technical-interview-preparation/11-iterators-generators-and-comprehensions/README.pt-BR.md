# Iteradores, geradores e comprehensions

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../10-python-memory-management/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../12-closures-and-decorators/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [program-flow/04-for-loops-and-iteration](../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [standard-library/07-itertools](../../standard-library/07-itertools/README.pt-BR.md)

## Protocolo de iteração

Um iterável fornece iterador por `iter()`. Um iterador retorna a si mesmo por `iter()`, produz valores com `next()` e sinaliza esgotamento com `StopIteration`. Uma lista pode fornecer novos iteradores; um iterador individual é consumido. Função geradora contém `yield`; chamá-la cria gerador sem executar o corpo. Cada avanço retoma até um yield ou conclusão. Mantém estado de execução entre avanços. Não levante StopIteration explicitamente no corpo para terminar; use return ou chegue ao fim.

```python
values = [1, 2, 3]
squares = [value ** 2 for value in values]
stream = (value ** 2 for value in values)
print(squares, next(stream), list(stream), list(stream))
```

Saída: `[1, 4, 9] 1 [4, 9] []`. Comprehensions de lista, conjunto e dicionário constroem contêineres imediatamente: `[x for x in values if x > 1]`, `{x for x in values}`, `{x: x ** 2 for x in values}`. Expressão geradora adia cálculo dos resultados (a expressão iterável mais à esquerda é avaliada imediatamente). Comprehensions aceitam filtros e loops aninhados, mas lógica complexa fica mais clara em funções nomeadas ou loops comuns.

## Quando usar streaming

Exemplo compartilhado filtra linhas sem materializar toda entrada. Usa estado extra constante excluindo entrada, saída e armazenamento do chamador; chamar list materializa resultados. Laziness pode reduzir pico de armazenamento e permitir parada antecipada, mas não garante menor tempo total ou memória em todo pipeline. Evite consumo repetido quando precisar de coleção reutilizável; não consuma silenciosamente iterador só para inspecioná-lo.

## Prática

Use fonte geradora registrando cada item consumido, chame next uma vez e consuma o restante. Teste entrada vazia e esgotamento. Compare comprehension imediata com gerador para fluxo grande; explique quando materializar é justificado.

**Referência rápida:** iterável fornece; iterador avança; gerador suspende; comprehension constrói; expressão geradora transmite.

## Exemplo executável compartilhado

[eligible_rows.py](examples/eligible_rows.py)

`python technical-interview-preparation/11-iterators-generators-and-comprehensions/examples/eligible_rows.py`

## Referências oficiais (Python 3.13)

- [Python 3.13: tutorial/classes.html#iterators](https://docs.python.org/3.13/tutorial/classes.html#iterators)
- [Python 3.13: tutorial/classes.html#generators](https://docs.python.org/3.13/tutorial/classes.html#generators)
- [Python 3.13: tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions)
- [Python 3.13: reference/expressions.html#generator-expressions](https://docs.python.org/3.13/reference/expressions.html#generator-expressions)

<!-- chapter-navigation:bottom -->
[← Anterior](../10-python-memory-management/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../12-closures-and-decorators/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
