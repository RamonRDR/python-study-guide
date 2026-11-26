# Revisão de exceções, testes e debugging

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../14-concurrency-parallelism-and-the-gil/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../16-http-rest-and-backend-fundamentals/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.pt-BR.md)
- [external-libraries/04-pytest](../../external-libraries/04-pytest/README.pt-BR.md)
- [manual-programming-practices/01-manual-coding-and-debugging](../../manual-programming-practices/01-manual-coding-and-debugging/README.pt-BR.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.pt-BR.md)

## Fronteiras de exceção

Exceções comunicam falhas entre chamadas. Capture exceção específica esperada onde possa recuperar ou traduzir; erros inesperados normalmente propagam até fronteira externa apropriada. `raise` no handler relança exceção ativa; `raise NewError(...) from error` preserva causa explícita. `else` executa após trabalho protegido bem-sucedido; `finally` cuida de saída, não de sucesso. Não retorne de finally para esconder erro. Gerenciadores de contexto tornam limpeza de recursos mais clara.

```python
try:
    value = int("unknown")
except ValueError as error:
    raise ValueError("invalid quantity") from error
```

Isso levanta exceção intencionalmente com sua causa; não é conversão bem-sucedida. Exemplo compartilhado aceita strings suportadas por int, incluindo espaços externos, e exige resultado não negativo. Não transforma entrada ruim silenciosamente em zero.

## Testar e depurar por evidências

Testes unitários verificam comportamento pequeno com dependências controladas; integração cruza fronteiras reais; ponta a ponta exercita fluxo completo suportado. Use Arrange/Act/Assert, assertions significativas de igualdade ou exceção, entradas de limite e setup/teardown determinísticos. Fake pode substituir dependência de rede, mas teste fronteira real separadamente. Parametrização varia entradas; fixtures fornecem e liberam dependências. Teste verde em código intencionalmente incorreto indica oráculo fraco, não prova correção. Cobertura mede execução, não correção.

Sequência de debugging: reproduzir com entrada mínima, ler traceback do frame que falhou e seus chamadores, formular hipótese, inspecionar estado relevante com debugger (`breakpoint()`) ou logs estruturados, mudar uma causa e adicionar teste de regressão. Oculte segredos e payloads sensíveis. Evite capturas amplas ou retries sem entender a falha.

## Prática

Preveja saídas válidas e inválidas de parse_quantity, verifique zero e negativos e confira causa da exceção. Retorne zero temporariamente para texto inválido em sua cópia; teste negativo deve falhar. Explique qual teste detecta cada defeito.

**Referência rápida:** captura específica; preserve causa; reproduza; teste comportamento; verifique regressão.

## Exemplo executável compartilhado

[parse_quantity.py](examples/parse_quantity.py)

`python technical-interview-preparation/15-exceptions-testing-and-debugging-review/examples/parse_quantity.py`

## Referências oficiais

- [docs.python.org/3.13/tutorial/errors.html](https://docs.python.org/3.13/tutorial/errors.html)
- [docs.python.org/3.13/library/unittest.html](https://docs.python.org/3.13/library/unittest.html)
- [docs.python.org/3.13/library/pdb.html](https://docs.python.org/3.13/library/pdb.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../14-concurrency-parallelism-and-the-gil/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../16-http-rest-and-backend-fundamentals/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
