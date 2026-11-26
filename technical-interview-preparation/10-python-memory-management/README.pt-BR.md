# Gerenciamento de memória em Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../09-object-identity-references-and-copying/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../11-iterators-generators-and-comprehensions/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [technical-interview-preparation/09-object-identity-references-and-copying](../../technical-interview-preparation/09-object-identity-references-and-copying/README.pt-BR.md)

## Vida e alcançabilidade de objetos

Gerenciamento de memória é como uma implementação aloca e recupera armazenamento. Um objeto vivo pode ser alcançável por nomes, contêineres, closures ou outros objetos. `del name` remove uma vinculação; não necessariamente destrói o objeto. Python não promete finalização imediata. No CPython 3.13 convencional, contagem de referências recupera muitos objetos quando referências fortes desaparecem, complementada por coletor de ciclos. Um ciclo pode manter contagens acima de zero mesmo após ficar inalcançável. Outras implementações e builds free-threaded podem diferir; não dependa do instante exato da coleta.

```python
first = []
second = first
del first
second.append("still alive")
print(second)
```

Referência fraca não mantém por si só o objeto vivo; `weakref.ref(obj)()` pode retornar o objeto ou None após sua destruição. Nem todos os objetos aceitam referências fracas (listas comuns não aceitam). Use somente quando a relação não deve manter o objeto vivo. Use `with` para arquivos e recursos similares; não dependa da coleta para limpeza no tempo certo.

## Retenção e medição

Cache alcançável, coleção global ou closure podem reter objetos indefinidamente sem defeito no coletor. Limite caches por quantidade ou orçamento de recursos adequado; remova referências desnecessárias. O exemplo compartilhado expulsa a chave inserida ou atualizada há mais tempo usando ordem de inserção do dicionário. Ler snapshot não renova ordem: não é cache LRU completo. Limite de quantidade não limita bytes, e snapshot raso não isola valores mutáveis.

`tracemalloc` permite comparar snapshots de alocações Python; não mede toda memória do processo ou alocações nativas. `gc.collect()` solicita coleta; não libera objetos alcançáveis nem promete reduzir RSS. Evite forçar coleta como solução padrão.

## Prática

Execute o cache, atualize chave antiga, insira outra e confira expulsão. Limpe cache e explique por que aliases externos ainda podem reter valores. Esboce ciclo entre dois contêineres e diferencie ciclos inalcançáveis de retenção alcançável.

**Referência rápida:** alcançabilidade e ownership primeiro; tempo da coleta não é contrato de recurso; meça antes de otimizar.

## Exemplo executável compartilhado

[bounded_cache.py](examples/bounded_cache.py)

`python technical-interview-preparation/10-python-memory-management/examples/bounded_cache.py`

## Referências oficiais (Python 3.13)

- [Python 3.13: reference/datamodel.html](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13: library/gc.html](https://docs.python.org/3.13/library/gc.html)
- [Python 3.13: library/weakref.html](https://docs.python.org/3.13/library/weakref.html)
- [Python 3.13: library/tracemalloc.html](https://docs.python.org/3.13/library/tracemalloc.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../09-object-identity-references-and-copying/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../11-iterators-generators-and-comprehensions/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
