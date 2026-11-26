# Gerenciadores de contexto

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../12-closures-and-decorators/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../14-concurrency-parallelism-and-the-gil/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [errors-files-and-modules/03-open-and-with](../../errors-files-and-modules/03-open-and-with/README.pt-BR.md)
- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.pt-BR.md)
- [technical-interview-preparation/11-iterators-generators-and-comprehensions](../../technical-interview-preparation/11-iterators-generators-and-comprehensions/README.pt-BR.md)
- [technical-interview-preparation/12-closures-and-decorators](../../technical-interview-preparation/12-closures-and-decorators/README.pt-BR.md)

## Protocolo with

Gerenciador de contexto empacota aquisição e liberação ao redor de bloco. Instrução `with manager as value:` chama `__enter__()`; retorno vira value. Após entrada bem-sucedida, `__exit__(exc_type, exc_value, traceback)` recebe detalhes da exceção ou três None. Retorno truthy suprime exceção do corpo; false ou None deixa propagar. Se entrada falhar, exit daquele gerenciador não é chamado. Falha na limpeza também pode levantar exceção. Não trate `with` como supressor automático.

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

Saída open, work, close em linhas separadas. Classe pode gerenciar recurso por esses métodos especiais. Alternativamente `contextlib.contextmanager` converte função geradora com exatamente um yield em fábrica de gerenciadores. Ponha limpeza em finally ao redor do yield. Exceção do corpo é injetada no ponto do yield; se capturada apenas para log, relance-a salvo se supressão for contrato intencional.

## Decisões práticas

Exemplo compartilhado registra open/work/close numa lista em vez de acessar recurso externo. Teste conclusão normal e falha do corpo. Gerenciador produzido por contextmanager normalmente é de uso único; chame fábrica novamente. Use `ExitStack` quando quantidade variável de gerenciadores precisar ser administrada. Evite gerenciador personalizado quando os de arquivo ou lock nativos já expressam contrato.

## Prática

Levante RuntimeError dentro do exemplo e verifique limpeza exatamente uma vez enquanto exceção propaga. Explique o que muda se entrada falhar antes de terminar aquisição. Compare try/finally explícito com gerenciador reutilizável.

**Referência rápida:** enter retorna vínculo; exit limpa; exit truthy suprime exceção do corpo; entrada bem-sucedida é fronteira.

## Exemplo executável compartilhado

[managed_session.py](examples/managed_session.py)

`python technical-interview-preparation/13-context-managers/examples/managed_session.py`

## Referências oficiais (Python 3.13)

- [Python 3.13: reference/compound_stmts.html#the-with-statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-with-statement)
- [Python 3.13: library/contextlib.html](https://docs.python.org/3.13/library/contextlib.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../12-closures-and-decorators/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../14-concurrency-parallelism-and-the-gil/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
