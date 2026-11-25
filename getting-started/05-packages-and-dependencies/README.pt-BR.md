# Pacotes e gerenciamento de dependências

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../04-virtual-environments/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../fundamentals/01-how-python-runs-a-program/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Nível:** iniciante absoluto. **Tempo estimado:** 30–45 minutos. Use o ambiente criado no capítulo 04. Dependência é um software de que seu projeto precisa para funcionar. Python já oferece biblioteca padrão (por exemplo, pathlib); pacotes externos são instalados separadamente. pip é o instalador de pacotes Python e normalmente obtém pacotes do Python Package Index (PyPI). Instale apenas o necessário.

## 1. Instale um pacote

Ative a .venv do projeto e confirme que `python -m pip --version` aponta para ela. Se não puder ativar, substitua python pelo executável direto do ambiente indicado no capítulo 04 em todos os comandos abaixo. Com acesso à internet, instale o pacote oficial Requests:

```shell
python -m pip install requests
python -m pip show requests
python -m pip list
python -m pip check
```

pip também pode instalar dependências do Requests. O comando check detecta requisitos instalados inconsistentes; não comprova segurança do pacote. Confira nome exato, publicador, documentação oficial e versão Python suportada antes de instalar. Evite comandos não confiáveis, instalação global e sudo pip.

Crie `check_package.py` ao lado de first_program.py (não dentro da .venv):

```python
from importlib.metadata import version

print(version("requests"))
```

Execute `python check_package.py`. Deve exibir a versão instalada (o número varia). Não faz requisição HTTP. Você estudará imports e HTTP depois. O nome de instalação nem sempre é o nome importado no código (beautifulsoup4 usa bs4, por exemplo).

## 2. Registre as dependências

No ambiente de prática limpo, capture as versões instaladas em um novo arquivo:

```shell
python -m pip freeze > requirements.txt
```

Isso sobrescreve requirements.txt; revise antes de versionar. No Windows PowerShell 5.1 use `python -m pip freeze | Out-File -Encoding ascii requirements.txt` para esta lista simples ASCII, evitando saída UTF-16. Não sobrescreva às cegas um contrato mantido manualmente. O freeze registra versões instaladas, inclusive dependências indiretas; não é lockfile multiplataforma completo. Registre a versão Python separadamente. Não inclua URLs privadas de pacotes, segredos nem caminhos da máquina.

Um projeto pode manter requirements.txt com apenas dependências diretas e faixas de versões suportadas, e depois resolver ou travar o conjunto completo com ferramentas adequadas. O [requirements-external.txt](../../requirements-external.txt) do guia é um contrato separado e mantido para os exemplos existentes; não o substitua pelo freeze da prática.

## 3. Recrie e compare

Saia do shell ativado com deactivate. Crie uma segunda pasta de prática pelo gerenciador de arquivos. Copie apenas código-fonte e requirements.txt, não .venv. Abra a pasta, crie e ative seu próprio ambiente conforme capítulo 04 com a mesma versão Python, confirme o executável e instale:

```shell
python -m pip install -r requirements.txt
python -m pip check
python check_package.py
```

Compare as versões exibidas nos dois ambientes. Isso demonstra recriação na sua máquina; compatibilidade pode variar em outro SO ou versão Python. Para remover, use `python -m pip uninstall requests` apenas no ambiente desejado; dependências não são removidas automaticamente. Não desinstale de projeto real só para praticar.

## 4. Mapa de bibliotecas

| Pacote | Finalidade | Guia |
| --- | --- | --- |
| `pandas` | Análise de dados | [Capítulo](../../external-libraries/01-pandas/README.pt-BR.md) |
| `openpyxl` | Automação de arquivos Excel | [Capítulo](../../external-libraries/02-openpyxl/README.pt-BR.md) |
| `requests` | HTTP e APIs | [Capítulo](../../external-libraries/03-requests/README.pt-BR.md) |
| `pytest` | Testes automatizados | [Capítulo](../../external-libraries/04-pytest/README.pt-BR.md) |
| `numpy` | Arrays numéricos | Candidato futuro |
| `playwright` | Automação de navegadores | Candidato futuro |
| `selenium` | Automação de navegadores | Candidato futuro |
| `beautifulsoup4` | Análise de HTML | Candidato futuro |
| `httpx` | Clientes HTTP, inclusive assíncronos | Candidato futuro |
| `fastapi` | Desenvolvimento de APIs | Candidato futuro |
| `pydantic` | Validação de dados | Candidato futuro |
| `sqlalchemy` | Acesso a bancos e ORM | Candidato futuro |
| `matplotlib` | Visualização de dados | Candidato futuro |
| `python-dotenv` | Leitura de configuração de arquivos .env | Candidato futuro |

Os quatro capítulos existentes são o currículo testado. Os demais são candidatos a aulas futuras, não instalações obrigatórias ou contratos testados. Alguns precisam de recursos adicionais: Playwright, por exemplo, baixa binários de navegadores separadamente do pacote Python. Para um experimento opcional e autorizado em ambiente separado, o [guia oficial da biblioteca](https://playwright.dev/python/docs/library) descreve:

```shell
python -m pip install playwright
python -m playwright install chromium
```

Downloads dos navegadores exigem rede, armazenamento e às vezes dependências do SO. Podem ficar em cache fora da .venv. Não execute isso para o exercício obrigatório e não adicione Playwright ao arquivo de dependências do repositório só por estar listado aqui.

## 5. Prática e referência rápida

- [ ] Verificar interpretador ativo e caminho do pip.
- [ ] Instalar Requests no ambiente de prática e verificar versão.
- [ ] Salvar requirements.txt e recriar ambiente em segunda pasta.
- [ ] Explicar por que código e requirements são versionados, mas .venv não.

Se a instalação falhar, leia o erro, confira compatibilidade Python e acesso à internet e verifique o ambiente. Não contorne verificações de certificados ou segurança. Se um import falhar, compare interpretadores usados para instalar e executar.

**Referência rápida:** instalar com python -m pip install PACKAGE, inspecionar com show/list, verificar com check, registrar com freeze, recriar com install -r requirements.txt. Siga para Fundamentos para entender o código Python.

## Referências oficiais

- [Python Packaging User Guide](https://packaging.python.org/pt-br/latest/guides/installing-using-pip-and-virtual-environments/)
- [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
- [Python Package Index](https://pypi.org/)
- [Navegadores Playwright](https://playwright.dev/python/docs/browsers)

<!-- chapter-navigation:bottom -->
[← Anterior](../04-virtual-environments/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../fundamentals/01-how-python-runs-a-program/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
