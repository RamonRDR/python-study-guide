<div align="center">

# Engenharia de Testes Automatizados com `pytest`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Bibliotecas Externas](../README.pt-BR.md) · [← Anterior: `requests`](../03-requests/README.pt-BR.md)

Software fica mais fácil de alterar quando o comportamento esperado pode ser verificado repetidamente e de forma automática. O `pytest` fornece um modelo de testes conciso baseado em funções Python normais, instruções `assert`, fixtures reutilizáveis, parametrização, relatórios de falha ricos e um sistema extensível de plugins.

Este capítulo tem como alvo **pytest 9.1.x** e foi pesquisado com base na documentação e nos metadados da versão estável atual, **pytest 9.1.1**. O pytest 9.1.1 exige Python 3.10 ou mais recente; este repositório valida os exemplos em Python 3.13.

**Tempo estimado de estudo:** 300–390 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar o que um teste automatizado comprova e o que ele não comprova;
- organizar testes para que o pytest os descubra de forma previsível;
- escrever assertions legíveis e interpretar a introspecção de assertions;
- testar valores de ponto flutuante, exceções e warnings de forma deliberada;
- reduzir duplicação com parametrização;
- modelar setup, teardown e dependências com fixtures;
- isolar filesystem e ambiente com `tmp_path` e `monkeypatch`;
- capturar saída padrão e logs com `capsys` e `caplog`;
- usar marks, skips, falhas esperadas e seleção de testes intencionalmente;
- configurar pytest sem esconder warnings ou omissões acidentais de testes;
- distinguir fronteiras de testes unitários, de integração e end-to-end;
- evitar testes flaky causados por tempo, aleatoriedade, rede, estado compartilhado ou dependência de ordem;
- integrar pytest ao CI como um contrato executável de qualidade.

## 1. Por que testes automatizados existem

Uma verificação manual responde a uma pergunta uma vez. Um teste automatizado transforma essa pergunta em código executável que pode ser repetido depois de alterações futuras.

Um bom teste descreve um comportamento, fornece entradas controladas, observa uma saída ou efeito colateral e falha quando o comportamento observado viola o contrato esperado.

Testes reduzem incerteza. Eles não provam que o software não possui bugs.

## 2. O que o `pytest` acrescenta

Python inclui `unittest` na biblioteca padrão. O `pytest` é um framework externo capaz de executar funções de teste simples e acrescentar recursos como:

- introspecção de assertions;
- fixtures;
- parametrização;
- marks e seleção de testes;
- caminhos temporários;
- monkeypatch de ambiente;
- captura de saída, warnings e logs;
- plugins e hooks.

O objetivo não é deixar os testes sofisticados. O objetivo é tornar a intenção visível e a repetição barata.

## 3. Bibliotecas externas precisam de contrato de versão

Este repositório declara as dependências da Fase 9 em `requirements-external.txt`.

Para este capítulo, o contrato é:

```text
pytest >= 9.1 and < 9.2
```

O limite superior importa porque o changelog do pytest já contém um draft não lançado da versão 9.2 com mudanças incompatíveis. Um currículo publicado deve descrever comportamento lançado, e não seguir silenciosamente uma versão futura.

## 4. Instale o conjunto de dependências do repositório

Crie e ative um ambiente virtual e então instale:

```bash
python -m pip install -r requirements-external.txt
```

Para experimentação isolada:

```bash
python -m pip install pytest
```

Mesmo assim, um projeto deve registrar qual faixa de pytest suporta.

## 5. Prefira `python -m pytest` quando a identidade do interpretador importa

Uma invocação comum é:

```bash
python -m pytest
```

Usar `python -m` torna o interpretador explícito. Isso é especialmente útil quando existem várias instalações do Python ou ambientes virtuais na mesma máquina.

O comando `pytest` também é válido quando o ambiente não é ambíguo.

## 6. Um teste é especificação executável, não código de produção

Considere uma função pequena:

```python
def calculate_total(unit_price: int, quantity: int) -> int:
    return unit_price * quantity
```

Um teste pode declarar um comportamento esperado:

```python
def test_calculate_total_multiplies_price_by_quantity() -> None:
    assert calculate_total(12, 3) == 36
```

O nome do teste comunica o contrato antes mesmo da leitura da assertion.

## 7. pytest descobre testes por convenção

Por padrão, o pytest descobre módulos e funções de teste por convenções de nome.

Uma estrutura comum é:

```text
project/
├── src/
│   └── calculator.py
└── tests/
    └── test_calculator.py
```

Dentro de `test_calculator.py`, funções chamadas `test_*` são coletadas como testes.

## 8. Coleta é uma fase da execução

Antes de executar os testes, o pytest primeiro os descobre e coleta.

Você pode inspecionar a coleta sem executar nada:

```bash
python -m pytest --collect-only
```

Isso é útil quando um teste esperado não aparece.

Uma suíte verde que coletou os testes errados não é um sinal confiável.

## 9. Mantenha nomes de testes orientados a comportamento

Prefira nomes que expliquem uma regra observável:

```python
def test_discount_is_zero_for_empty_cart() -> None:
    ...
```

Evite nomes que apenas espelham detalhes de implementação:

```python
def test_function_2() -> None:
    ...
```

Bons nomes facilitam a triagem de falhas no CI.

## 10. `assert` simples é o estilo normal de assertion no pytest

```python
def test_status_is_ready() -> None:
    status = "ready"
    assert status == "ready"
```

O pytest reescreve assertions durante a coleta para produzir diagnósticos mais ricos do que um `AssertionError` puro normalmente forneceria.

## 11. A introspecção de assertion ajuda a explicar falhas

Uma comparação como:

```python
def test_summary() -> None:
    actual = {"count": 2, "status": "ready"}
    expected = {"count": 3, "status": "ready"}
    assert actual == expected
```

pode mostrar os valores diferentes quando falha.

Por isso, expressões diretas costumam ser melhores do que mensagens vagas construídas manualmente em toda assertion.

## 12. Adicione mensagem apenas quando ela trouxer contexto de domínio

```python
def test_inventory_never_becomes_negative() -> None:
    remaining = 4
    assert remaining >= 0, "inventory contract requires a non-negative balance"
```

A mensagem deve explicar por que a condição importa, e não apenas repetir `remaining >= 0`.

## 13. Use Arrange, Act, Assert quando isso deixar o teste mais claro

Um teste legível costuma ter três etapas conceituais:

```python
def test_normalize_name_removes_outer_whitespace() -> None:
    raw_name = "  Nova  "

    normalized = raw_name.strip()

    assert normalized == "Nova"
```

Nem todo teste pequeno precisa de comentários nomeando as etapas. A própria estrutura pode deixá-las evidentes.

## 14. Teste um comportamento coerente

Um teste pode ter várias assertions quando elas descrevem um único resultado, mas evite transformar um único teste em um passeio por comportamentos não relacionados.

Testes menores tornam falhas mais locais e fáceis de diagnosticar.

## 15. Testes determinísticos são repetíveis

Um teste determinístico produz o mesmo resultado quando o código e as entradas relevantes não mudaram.

Ameaças comuns incluem:

- horário atual;
- valores aleatórios sem controle;
- serviços de rede;
- arquivos ou bancos compartilhados;
- variáveis de ambiente;
- locale e timezone;
- dependência da ordem de execução.

Isolamento é uma habilidade de design, não apenas uma funcionalidade do framework.

## 16. Compare resultados de ponto flutuante com tolerância explícita

Valores de ponto flutuante binário muitas vezes não são adequados para igualdade exata depois de cálculos.

O pytest fornece `approx()`:

```python
import pytest


def test_ratio() -> None:
    result = 1 / 3
    assert result == pytest.approx(0.333333, rel=1e-5)
```

Escolha tolerâncias de acordo com o domínio, em vez de copiar valores arbitrários.

## 17. Valores exatos devem continuar usando assertions exatas

Não use `pytest.approx()` quando o contrato é exato.

```python
def test_item_count() -> None:
    assert len(["a", "b", "c"]) == 3
```

Ferramentas de teste devem tornar contratos mais claros, não mais vagos.

## 18. Teste exceções esperadas com `pytest.raises`

```python
import pytest


def parse_positive(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise ValueError("value must be positive")
    return number


def test_zero_is_rejected() -> None:
    with pytest.raises(ValueError):
        parse_positive("0")
```

O teste passa somente se o tipo de exceção esperado for levantado dentro do context manager.

## 19. Faça match da mensagem quando ela faz parte do contrato

```python
def test_zero_has_clear_message() -> None:
    with pytest.raises(ValueError, match="must be positive"):
        parse_positive("0")
```

`match` é interpretado como expressão regular. Escape caracteres especiais quando quiser correspondência literal.

## 20. Inspecione informações da exceção capturada quando necessário

```python
def test_invalid_value_context() -> None:
    with pytest.raises(ValueError) as exc_info:
        parse_positive("-4")

    assert "positive" in str(exc_info.value)
```

Faça isso quando o detalhe adicional importar. Não inspecione internals apenas porque o pytest os expõe.

## 21. Teste warnings explicitamente com `pytest.warns`

```python
import warnings

import pytest


def old_api() -> None:
    warnings.warn("old API", DeprecationWarning, stacklevel=2)


def test_old_api_warns() -> None:
    with pytest.warns(DeprecationWarning, match="old API"):
        old_api()
```

Warnings podem representar contratos de migração que merecem testes próprios.

## 22. pytest 9.1 pode impor um orçamento de warnings

O pytest 9.1 adicionou `--max-warnings`.

Por exemplo:

```bash
python -m pytest --max-warnings=10
```

Se todos os testes passarem, mas a quantidade de warnings não filtrados ultrapassar o limite, o pytest retorna um status dedicado diferente de zero.

Um orçamento de warnings ajuda um projeto a reduzir dívida gradualmente em vez de simplesmente esconder tudo.

## 23. Parametrização transforma variação de dados em casos de teste

Quando o mesmo comportamento deve valer para várias entradas, use `@pytest.mark.parametrize`:

```python
import pytest


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(-5, 0), (40, 40), (130, 100)],
)
def test_normalize_score(raw: int, expected: int) -> None:
    result = max(0, min(raw, 100))
    assert result == expected
```

O pytest cria um caso coletado separado para cada conjunto de parâmetros.

## 24. Separe lógica de teste de dados de teste

Parametrização funciona melhor quando o corpo do teste expressa uma regra e os dados representam casos interessantes.

Inclua fronteiras significativas, e não apenas muitos exemplos aleatórios.

Uma tabela com dez linhas não é automaticamente melhor que três casos de fronteira bem escolhidos.

## 25. Dê IDs úteis aos parâmetros quando o relatório precisar deles

```python
@pytest.mark.parametrize(
    ("value", "expected"),
    [(0, "empty"), (1, "single"), (2, "many")],
    ids=["zero", "one", "multiple"],
)
def test_classification(value: int, expected: str) -> None:
    result = "empty" if value == 0 else "single" if value == 1 else "many"
    assert result == expected
```

IDs legíveis melhoram relatórios para valores de parâmetro complexos.

## 26. Use `pytest.param` para metadados por caso

```python
@pytest.mark.parametrize(
    "value",
    [
        1,
        pytest.param(-1, marks=pytest.mark.xfail(reason="known limitation")),
    ],
)
def test_positive_only(value: int) -> None:
    assert value > 0
```

Marks por caso mantêm exceções visíveis sem duplicar o teste inteiro.

## 27. pytest 9.1 deprecia iteráveis que não são collections na parametrização

A documentação atual de pytest deprecia passar diretamente um iterável que não seja `Collection`, como um generator, em `argvalues`.

Prefira uma lista ou tupla concreta em testes publicados:

```python
cases = [(1, 2), (2, 4), (3, 6)]
```

Isso também facilita a inspeção e revisão dos dados de teste.

## 28. Fixtures modelam dependências de teste

Uma fixture é um valor ou recurso que o pytest fornece a um teste pelo nome.

```python
import pytest


@pytest.fixture
def sample_user() -> dict[str, str]:
    return {"name": "Nova", "role": "reader"}


def test_user_role(sample_user: dict[str, str]) -> None:
    assert sample_user["role"] == "reader"
```

O teste solicita a fixture declarando um parâmetro com o nome dela.

## 29. Fixtures podem retornar objetos

Fixtures podem retornar valores simples, estruturas, clientes configurados, repositórios temporários, conexões ou outros recursos.

Mantenha fixtures focadas. Uma fixture gigante que prepara a aplicação inteira pode esconder dependências em vez de esclarecê-las.

## 30. Fixtures podem fazer teardown com `yield`

```python
import pytest


@pytest.fixture
def opened_resource():
    resource = {"open": True}
    yield resource
    resource["open"] = False
```

Código antes de `yield` faz setup. Código depois de `yield` faz teardown quando o pytest finaliza a fixture.

Use context managers reais quando o recurso de produção já oferecer um.

## 31. O scope da fixture controla seu tempo de vida

Scopes comuns são:

```text
function -> one test invocation
class    -> one test class
module   -> one test module
package  -> one test package
session  -> the whole pytest session
```

O padrão é scope `function`.

## 32. Scope mais amplo troca isolamento por reutilização

Um recurso de scope `session` pode ser mais rápido por ser criado uma vez, mas também vive mais tempo e pode carregar estado mutável compartilhado entre testes.

Não amplie scope apenas para acelerar a suíte. Primeiro entenda se a vida compartilhada preserva independência.

## 33. Fixtures podem depender de outras fixtures

```python
import pytest


@pytest.fixture
def base_url() -> str:
    return "https://example.invalid"


@pytest.fixture
def endpoint(base_url: str) -> str:
    return f"{base_url}/items"
```

Composição de dependências costuma ser mais clara que uma fixture que conhece todo o setup.

## 34. Evite dependências escondidas com excesso de `autouse`

Uma fixture `autouse=True` roda sem aparecer na assinatura de cada teste.

Isso pode servir para uma invariante real da suíte, mas uso excessivo torna o comportamento difícil de rastrear.

Prefira parâmetros explícitos de fixture, salvo quando a aplicação automática fizer parte genuína do contrato do ambiente.

## 35. `conftest.py` compartilha configuração local e fixtures

Uma estrutura comum é:

```text
tests/
├── conftest.py
├── test_api.py
└── test_reports.py
```

Fixtures definidas em `tests/conftest.py` podem ser descobertas por testes abaixo desse diretório sem importar `conftest` diretamente.

## 36. `conftest.py` segue regras de visibilidade por diretório

Para um teste, o pytest consulta arquivos `conftest.py` relevantes no diretório do teste e em diretórios pais.

Isso torna a visibilidade hierárquica.

Coloque fixtures compartilhadas no nível mais estreito que precisa delas.

## 37. Não importe de `conftest.py`

Trate `conftest.py` como configuração do pytest, não como módulo da aplicação.

Se helpers precisarem de imports normais, coloque-os em módulo ou pacote regular e importe esse módulo dos testes e fixtures.

## 38. `tmp_path` fornece um `Path` temporário para cada teste

```python
from pathlib import Path


def test_export(tmp_path: Path) -> None:
    report = tmp_path / "report.txt"
    report.write_text("ready\n", encoding="utf-8")

    assert report.read_text(encoding="utf-8") == "ready\n"
```

`tmp_path` é um `pathlib.Path` único por invocação de teste.

Isso evita poluir o repositório com artefatos de teste.

## 39. `tmp_path_factory` serve para scopes mais amplos

Uma fixture de scope `session` ou `module` não pode depender de `tmp_path`, que tem scope de função.

Para recursos temporários mais duradouros, pytest oferece `tmp_path_factory`.

Escolha uma vida mais ampla somente quando fizer parte do design.

## 40. `monkeypatch` altera estado e o restaura automaticamente

A fixture `monkeypatch` pode modificar temporariamente:

- atributos de objetos;
- itens de dicionários;
- variáveis de ambiente;
- `sys.path`;
- diretório de trabalho atual.

As mudanças são desfeitas depois que o teste ou fixture solicitante termina.

## 41. Faça patch de variáveis de ambiente com `setenv` e `delenv`

```python
import os


def read_mode() -> str:
    return os.getenv("STUDY_MODE", "default")


def test_configured_mode(monkeypatch) -> None:
    monkeypatch.setenv("STUDY_MODE", "focused")
    assert read_mode() == "focused"
```

Código dependente de ambiente fica determinístico quando o teste controla o ambiente explicitamente.

## 42. Faça patch onde o código procura a dependência

Suponha que `service.py` contenha:

```python
from client import fetch_status


def is_ready() -> bool:
    return fetch_status() == "ready"
```

O teste normalmente precisa fazer patch de `service.fetch_status`, pois é esse nome que `is_ready()` resolve em runtime.

Fazer patch da definição original em `client` pode não substituir uma referência já importada em `service`.

## 43. `monkeypatch.context()` pode limitar ainda mais a duração do patch

Quando um teste precisa do patch apenas em um bloco pequeno, `monkeypatch.context()` cria um contexto aninhado cujas alterações são desfeitas ao sair do bloco.

Tempos menores de patch reduzem interações surpreendentes em testes complexos.

## 44. Use test doubles para substituir fronteiras, não tudo

Um test double pode representar um colaborador lento, não determinístico, destrutivo ou indisponível.

Categorias informais comuns incluem:

```text
stub  -> returns controlled values
fake  -> lightweight working implementation
spy   -> records how it was used
mock  -> verifies expected interactions
```

O vocabulário importa menos do que deixar claro o propósito da substituição.

## 45. `unittest.mock` da biblioteca padrão funciona com pytest

pytest não exige um estilo separado de mocking.

Você pode combinar assertions e fixtures do pytest com `unittest.mock.Mock`, `MagicMock` ou `patch` quando forem adequados.

Não faça mock de cálculos puros apenas porque a ferramenta existe.

## 46. `capsys` captura stdout e stderr no nível Python

```python
def announce(topic: str) -> None:
    print(f"Studying: {topic}")


def test_announce(capsys) -> None:
    announce("pytest")
    captured = capsys.readouterr()
    assert captured.out == "Studying: pytest\n"
    assert captured.err == ""
```

Isso é útil para interfaces de linha de comando e funções cuja saída faz parte do contrato.

## 47. `capfd` captura no nível de file descriptor

`capsys` foca nos objetos `sys.stdout` e `sys.stderr` do Python.

`capfd` captura os file descriptors 1 e 2, útil quando a saída vem de código de nível mais baixo que contorna streams normais do Python.

Use o mecanismo mais estreito que corresponde ao comportamento testado.

## 48. `caplog` captura registros de logging

```python
import logging


def test_log_message(caplog) -> None:
    logger = logging.getLogger("study")

    with caplog.at_level(logging.INFO, logger="study"):
        logger.info("session ready")

    assert "session ready" in caplog.text
```

Os testes também podem inspecionar registros estruturados em vez de apenas texto renderizado.

## 49. Cuidado ao reconfigurar o root logger durante `caplog`

A documentação do pytest alerta que alterar handlers do root logger durante um teste pode interferir na captura de logs.

Prefira configuração de logger direcionada e evite substituir o conjunto inteiro de handlers, salvo se o teste validar justamente essa configuração.

## 50. Marks adicionam metadados aos testes

Marks podem classificar ou alterar comportamento.

```python
import pytest


@pytest.mark.slow
def test_large_report() -> None:
    assert True
```

Custom marks devem representar categorias úteis, e não substituir organização clara da suíte.

## 51. Registre custom marks

Marks não registradas podem gerar warnings, e erros de digitação podem criar categorias indesejadas silenciosamente.

Um `pyproject.toml` pode registrá-las:

```toml
[tool.pytest.ini_options]
markers = [
    "slow: tests that intentionally take longer",
    "integration: tests that cross component boundaries",
]
```

O registro transforma nomes de marks em contrato documentado do projeto.

## 52. `strict_markers` pode transformar marks desconhecidas em erros

```toml
[tool.pytest.ini_options]
strict_markers = true
```

Isso é útil quando uma mark digitada incorretamente deve falhar imediatamente em vez de ser tratada como nova mark.

## 53. pytest 9 introduziu um strict mode mais amplo

O pytest 9 fornece a opção de configuração `strict`, que ativa em conjunto verificações de configuração, markers, xfail e IDs de parametrização.

A documentação alerta que versões futuras podem adicionar novas opções de strictness. Use o modo global com uma versão de pytest controlada ou quando o projeto quiser adotar novas verificações proativamente.

## 54. Pule testes somente por uma razão ambiental real

```python
import sys

import pytest


@pytest.mark.skipif(sys.platform == "win32", reason="POSIX-only contract")
def test_posix_behavior() -> None:
    assert True
```

Um teste pulado não verifica o comportamento. Muitos skips podem criar pontos cegos.

## 55. `xfail` registra uma falha esperada conhecida

```python
import pytest


@pytest.mark.xfail(reason="known parser limitation", strict=True)
def test_future_case() -> None:
    assert False
```

Com `strict=True`, um passe inesperado falha a suíte, obrigando o time a perceber que a limitação conhecida pode ter sido corrigida.

Não use `xfail` como estacionamento permanente de testes quebrados.

## 56. Selecione testes com `-k`

`-k` filtra testes coletados por expressão de nome:

```bash
python -m pytest -k "report and not slow"
```

Isso é conveniente no desenvolvimento local, mas o CI ainda deve executar a suíte completa pretendida ou partições documentadas explicitamente.

## 57. Selecione grupos marcados com `-m`

```bash
python -m pytest -m "integration"
```

ou:

```bash
python -m pytest -m "not slow"
```

Marks tornam partições explícitas quando são registradas e mantidas consistentemente.

## 58. Pare cedo com `-x` ou `--maxfail`

```bash
python -m pytest -x
```

para após a primeira falha.

```bash
python -m pytest --maxfail=3
```

para após três falhas.

São opções úteis para velocidade de feedback, mas não substituem a suíte completa antes de um release.

## 59. Reexecute falhas anteriores com `--lf`

```bash
python -m pytest --lf
```

O pytest pode usar o cache para selecionar testes que falharam na execução anterior.

Trate isso como acelerador local. Um job limpo de CI não deve depender do estado de uma execução anterior do desenvolvedor.

## 60. Verbosidade muda o relatório, não a correção

Opções comuns incluem:

```bash
python -m pytest -q
python -m pytest -v
```

Saída quiet pode ajudar em logs automatizados; saída verbose pode ajudar a identificar casos parametrizados.

O contrato de teste não deve depender da decoração do terminal.

## 61. Configuração deve ficar no controle de versão

pytest suporta configuração de projeto em arquivos suportados como `pyproject.toml`, `pytest.ini` e outros documentados pelo projeto.

Uma configuração mínima em `pyproject.toml` pode ser:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
strict_markers = true
```

Configuração deve tornar a suíte previsível, não esconder comportamento que falha.

## 62. `testpaths` restringe a descoberta padrão

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

Quando pytest é chamado sem caminhos explícitos, isso indica onde o projeto espera encontrar testes.

Se houver testes em outros locais, configure ou invoque-os intencionalmente.

## 63. Tenha cautela com `addopts` global

Um projeto pode configurar opções padrão, por exemplo:

```toml
[tool.pytest.ini_options]
addopts = "-ra"
```

Evite defaults que silenciosamente pulem categorias importantes ou escondam diagnósticos necessários.

## 64. Entenda o root selecionado pelo pytest

pytest determina um diretório raiz e um contexto de configuração para a coleta.

Executar pytest de um diretório inesperado pode alterar quais configurações e arquivos `conftest.py` ficam visíveis.

Ao investigar problemas de descoberta, inspecione o rootdir e o arquivo de configuração reportados.

## 65. Mantenha imports previsíveis

Testes continuam sendo módulos Python, então regras de import importam.

Um projeto deve usar layout de pacote deliberado e testar o código que pretende distribuir, em vez de depender de imports acidentais pelo diretório de trabalho.

O layout comum `src/` pode ajudar a separar código instalado de caminhos locais do repositório.

## 66. Não dê `__init__` customizado a classes de teste do pytest

Classes de teste do pytest são coletadas por convenção e não devem se comportar como objetos de aplicação que exigem argumentos de construtor.

Use fixtures para dependências de testes em vez de construção customizada da classe.

Funções de teste simples costumam ser o melhor ponto de partida.

## 67. Valores de fixtures devem corresponder ao nome declarado

Se uma fixture se chama `authenticated_client`, ela deve fornecer esse estado de forma confiável.

Evite fixtures cujo resultado muda inesperadamente por configurações globais não relacionadas. Fixtures ambíguas transformam testes em enigmas.

## 68. Evite florestas de fixtures

Composição de fixtures é poderosa, mas um teste dependente de uma fixture que depende de mais seis pode ficar difícil de entender.

Se o setup virar um labirinto, considere builders simples, helper functions ou fronteiras de integração menores.

## 69. Testes unitários isolam uma pequena unidade de comportamento

Um teste unitário normalmente exercita função, classe ou componente pequeno com colaboradores controlados.

São valiosos para feedback rápido, mas a definição exata de “unidade” depende da arquitetura.

Não transforme o rótulo em regra doutrinária.

## 70. Testes de integração cruzam fronteiras reais de componentes

Um teste de integração pode exercitar combinações como:

```text
application code + database adapter
application code + local HTTP server
parser + real file format
repository + temporary filesystem
```

Esses testes validam contratos que mocks não conseguem provar completamente.

## 71. Testes end-to-end validam fluxos maiores

Testes end-to-end exercitam um caminho amplo pelo sistema e podem detectar problemas que testes menores não enxergam.

Também costumam ser mais lentos, caros para diagnosticar e sensíveis ao ambiente.

Uma suíte saudável normalmente usa várias camadas.

## 72. Teste comportamento observável antes de detalhes de implementação

Se um refactor preserva o comportamento público, bons testes normalmente continuam passando.

Testes que verificam cada chamada de helper privado tornam limpeza interna desnecessariamente cara.

Assertions de interação são adequadas quando a própria interação faz parte do contrato, como “não envie a requisição duas vezes”.

## 73. Faça mock de serviços externos na fronteira correta

Um teste unitário não deve chamar uma API pública real.

Para código HTTP, estratégias úteis incluem:

- fazer patch da sua própria abstração de cliente;
- usar servidor de teste local;
- usar plugin específico de testes HTTP quando o projeto adotar um.

Testes não devem depender da internet pública, salvo quando forem testes deliberados de sistema externo.

## 74. Mantenha segredos fora dos dados de teste

Nunca coloque tokens, senhas, cookies, URLs privadas ou dados pessoais reais nos testes.

Use valores fictícios como:

```python
fake_token = "test-token-not-a-secret"
```

Fixtures de teste frequentemente aparecem em logs e relatórios de falha, então merecem a mesma disciplina de privacidade do código de produção.

## 75. Controle o tempo em vez de competir com o relógio

Evite testes como:

```python
import time


def test_waits() -> None:
    time.sleep(2)
    assert True
```

Se o comportamento depende do tempo, injete um clock ou faça patch da fonte de tempo estreita usada pelo código.

`sleep` deixa a suíte lenta e não garante que um estado assíncrono esteja pronto.

## 76. Controle aleatoriedade

Para código aleatório, opções incluem:

- injetar um gerador de números aleatórios;
- usar seed conhecido quando o contrato permitir;
- testar invariantes com entradas controladas.

Um teste que falha apenas em algumas execuções aleatórias é difícil de reproduzir e diagnosticar.

## 77. Testes não devem depender da ordem de execução

Um teste não deve precisar que outro rode primeiro.

Estado mutável compartilhado em módulo ou sessão é uma causa comum de dependência de ordem.

Se testes falham apenas quando a ordem muda, a suíte revelou um problema real de isolamento.

## 78. Um teste flaky é um defeito de confiabilidade

Um teste flaky alterna entre passar e falhar sem mudança relevante de código.

Causas comuns incluem:

- corridas de timing;
- serviços externos;
- estado compartilhado;
- ordenação não determinística;
- limpeza insuficiente;
- esgotamento de recursos.

Reexecutar até ficar verde esconde o sinal em vez de reparar o problema.

## 79. Coverage e correção são métricas diferentes

Cobertura de código pode revelar código que testes nunca executam.

Ela não prova que assertions são significativas, casos de fronteira estão representados ou requisitos estão corretos.

Trate coverage como evidência de execução, não substituto do design de testes.

## 80. Plugins estendem pytest

pytest possui um grande ecossistema de plugins para coverage, código assíncrono, frameworks, execução paralela e testes HTTP.

Plugins também são dependências. Limite versões importantes, revise compatibilidade e evite adicionar plugin quando o core já resolve o problema claramente.

## 81. pytest core não faz todo `async def` funcionar automaticamente

Funções de teste assíncronas normalmente exigem plugin ou integração de framework apropriado.

Não assuma que instalar pytest sozinho define a política de event loop necessária pela aplicação.

O plugin passa a fazer parte do contrato de dependências de teste.

## 82. `required_plugins` pode exigir a presença de plugins

A configuração do pytest pode declarar plugins obrigatórios para que a execução falhe cedo quando um deles estiver ausente.

Isso é útil quando a suíte poderia coletar incorretamente ou falhar depois com erros confusos de fixture ausente.

Use requisitos reais do projeto, não listas copiadas de repositórios alheios.

## 83. pytest pode executar muitos testes no estilo `unittest`

Adotar pytest não exige necessariamente reescrever uma suíte existente de `unittest` imediatamente.

pytest suporta muitos testes escritos com `unittest.TestCase` e permite uma migração gradual.

Migração deve melhorar manutenção, não criar churn por si só.

## 84. Trate códigos de saída como contratos de CI

Um sistema de CI deve falhar quando o runner de testes reporta falha.

Não escreva wrappers de shell que descartem o exit status do pytest.

Os exemplos executáveis deste capítulo convertem o código de saída programático para inteiro apenas para apresentar o resultado de forma determinística.

## 85. Exemplo executável: assertions e parametrização

[`examples/assertions_and_parametrize.py`](examples/assertions_and_parametrize.py) cria um módulo pytest temporário, executa-o com o runner real e reporta somente um resumo determinístico.

Saída esperada:

```text
exit code: 0
passed: 4
```

A suíte temporária demonstra uma assertion normal e três casos de fronteira parametrizados.

## 86. Exemplo executável: fixtures e `tmp_path`

[`examples/fixtures_and_tmp_path.py`](examples/fixtures_and_tmp_path.py) demonstra uma fixture que depende da fixture built-in `tmp_path`.

Saída esperada:

```text
exit code: 0
passed: 2
```

Cada teste recebe sua própria invocação de fixture e fronteira temporária de filesystem.

## 87. Exemplo executável: `monkeypatch`

[`examples/monkeypatch_environment.py`](examples/monkeypatch_environment.py) controla uma variável de ambiente sem deixar estado global do processo para trás.

Saída esperada:

```text
exit code: 0
passed: 2
```

O exemplo verifica tanto o fallback quanto um estado configurado explicitamente.

## 88. Exemplo executável: exceções e warnings

[`examples/exceptions_and_warnings.py`](examples/exceptions_and_warnings.py) usa `pytest.raises` e `pytest.warns` para tornar comportamento de falha e migração explícito.

Saída esperada:

```text
exit code: 0
passed: 2
```

São verificados tipo/mensagem da exceção e categoria/mensagem do warning.

## 89. Exemplo executável: captura de saída e logs

[`examples/capture_output_and_logs.py`](examples/capture_output_and_logs.py) demonstra `capsys` e `caplog`.

Saída esperada:

```text
exit code: 0
passed: 2
```

A suíte valida saída de linha de comando e mensagem de logger direcionado.

## 90. Erros comuns

### Erro 1: tratar uma suíte verde como prova de ausência de bugs

Testes cobrem apenas comportamentos e entradas que realmente exercitam.

### Erro 2: testar trivia de implementação

Testes acoplados demais tornam refactors inofensivos caros.

### Erro 3: compartilhar estado mutável entre testes

Isso cria dependência de ordem e flakiness.

### Erro 4: chamar serviços públicos em testes unitários

Disponibilidade de rede e mudanças remotas tornam a suíte não determinística.

### Erro 5: esconder todos os warnings

Warnings frequentemente revelam migrações necessárias.

### Erro 6: usar mocks em excesso

Uma suíte de mocks pode provar que os mocks se comportam exatamente como configurados e ainda perder erros reais de integração.

### Erro 7: criar fixtures gigantes

Grafos enormes de setup escondem o que cada teste realmente precisa.

### Erro 8: aceitar reruns flaky como normais

Um teste flaky é um defeito no sistema de feedback.

## 91. Tabela de decisão

| Necessidade | Ferramenta útil | Principal cuidado |
| --- | --- | --- |
| Comparar valores normais | `assert` | mantenha explícito o contrato esperado |
| Comparar floats | `pytest.approx()` | escolha tolerância apropriada ao domínio |
| Esperar uma exceção | `pytest.raises()` | não capture falhas não relacionadas |
| Esperar um warning | `pytest.warns()` | teste categoria/mensagem deliberadamente |
| Repetir uma regra em vários casos | `@pytest.mark.parametrize` | escolha dados de fronteira significativos |
| Reutilizar setup | fixture | evite grafos ocultos e gigantes |
| Arquivos temporários | `tmp_path` | não dependa de artefatos no repositório |
| Alterações temporárias de ambiente | `monkeypatch` | faça patch onde o código procura o nome |
| Capturar stdout/stderr | `capsys` | verifique apenas saída que faz parte do contrato |
| Capturar logs | `caplog` | evite bagunçar handlers do root logger |
| Classificar testes | marks registradas | evite erros silenciosos de digitação |
| Falha conhecida esperada | `xfail` | prefira tratamento strict e remova quando corrigido |

## 92. Referência rápida

```bash
python -m pytest
python -m pytest -q
python -m pytest -v
python -m pytest --collect-only
python -m pytest -k "name_expression"
python -m pytest -m "marker_expression"
python -m pytest -x
python -m pytest --maxfail=3
python -m pytest --lf
python -m pytest --max-warnings=10
```

Padrões Python principais:

```python
assert actual == expected

with pytest.raises(ValueError, match="message"):
    operation()

with pytest.warns(DeprecationWarning):
    old_operation()
```

## 93. Checklist de revisão

Antes de chamar uma suíte de confiável, pergunte:

- Os testes pretendidos estão realmente sendo coletados?
- Os nomes explicam comportamentos?
- As assertions são específicas o bastante para falhar pela razão certa?
- Casos de fronteira e erro estão representados?
- Arquivos são escritos em caminhos temporários?
- Mudanças de ambiente são restauradas automaticamente?
- Rede, relógio e aleatoriedade estão controlados?
- Os testes rodam de forma independente e em qualquer ordem?
- Warnings são visíveis e intencionais?
- Custom marks estão registradas?
- Falhas esperadas são revisadas e temporárias?
- O CI preserva o exit status de falha do pytest?
- Dados e logs de teste estão livres de segredos e dados pessoais?

## 94. Exercício prático

Crie um pequeno pacote fictício que valida registros de sessões de estudo.

Requisitos:

1. Crie uma função que receba um tópico e duração em minutos.
2. Rejeite tópico vazio com `ValueError`.
3. Rejeite duração zero ou negativa com `ValueError`.
4. Retorne um dicionário normalizado para entrada válida.
5. Escreva testes de sucesso usando `assert` simples.
6. Parametrize pelo menos três durações inválidas.
7. Use `pytest.raises(..., match=...)` para um erro de validação.
8. Escreva uma fixture que retorne dados válidos de exemplo.
9. Adicione uma função que salve uma sessão como texto ou JSON e teste com `tmp_path`.
10. Adicione uma função que leia uma configuração de variável de ambiente e teste com `monkeypatch`.
11. Adicione uma função estilo CLI e valide saída com `capsys`.
12. Adicione um logger e valide com `caplog`.
13. Registre uma custom marker para testes de integração.
14. Execute `python -m pytest --collect-only` e confirme os casos esperados.
15. Execute a suíte completa em um processo limpo.

Desafios de extensão:

- mova fixtures compartilhadas para um `conftest.py` cuidadosamente escopado;
- adicione um warning para uma forma de entrada deprecada e teste com `pytest.warns`;
- use `pytest.approx` para uma razão calculada com tolerância documentada;
- construa um teste de integração HTTP local usando conceitos do capítulo anterior de `requests`;
- adicione CI que instale dependências declaradas e execute a suíte do zero.

## 95. Conexões com conceitos anteriores

`pytest` conecta quase todas as fases anteriores:

- **funções:** teste comportamento por entradas e saídas explícitas;
- **coleções:** construa tabelas de parâmetros e valores esperados estruturados;
- **fluxo de programa:** exercite branches e condições de fronteira;
- **exceções:** valide contratos de falha deliberada;
- **arquivos:** isole filesystem com caminhos temporários;
- **módulos e pacotes:** organize código e imports previsivelmente;
- **`pathlib`:** trabalhe naturalmente com `tmp_path`;
- **`datetime`:** injete ou faça patch de tempo em vez de disputar com o relógio real;
- **logging:** valide sinais operacionais com `caplog`;
- **`decimal`:** teste regras monetárias exatas sem tolerância de float inadequada;
- **pandas/openpyxl/requests:** transforme comportamento de bibliotecas externas em regressões repetíveis.

## 96. Referências primárias

- [pytest documentation](https://docs.pytest.org/)
- [Get Started](https://docs.pytest.org/en/stable/getting-started.html)
- [How to invoke pytest](https://docs.pytest.org/en/stable/how-to/usage.html)
- [Assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
- [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Temporary directories](https://docs.pytest.org/en/stable/how-to/tmp_path.html)
- [Monkeypatching](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [Logging](https://docs.pytest.org/en/stable/how-to/logging.html)
- [Warnings](https://docs.pytest.org/en/stable/how-to/capture-warnings.html)
- [Skip and xfail](https://docs.pytest.org/en/stable/how-to/skipping.html)
- [API reference](https://docs.pytest.org/en/stable/reference/reference.html)
- [pytest changelog](https://docs.pytest.org/en/stable/changelog.html)
- [pytest on PyPI](https://pypi.org/project/pytest/)

No momento em que este capítulo foi preparado, o PyPI listava pytest 9.1.1 como release estável mais recente. O currículo mira a série 9.1.x em vez do draft não lançado 9.2 ou de uma versão futura sem limite.

## 97. Fase 9 concluída

A Fase 9 agora conecta quatro fronteiras importantes de terceiros:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
requests -> communicate with HTTP services
pytest   -> verify behavior repeatedly and automatically
```

Isso encerra a **Fase 9: Bibliotecas Externas**.

A próxima fase sai de habilidades isoladas de bibliotecas e entra em trabalho integrado de portfólio: **Fase 10: Projetos Práticos**.

Antes de avançar, pratique escrevendo testes que tornem falhas informativas. Uma suíte é mais valiosa quando dá confiança para alterar o código, e não quando apenas produz um número verde.
