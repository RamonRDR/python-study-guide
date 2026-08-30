<div align="center">

# Fase 9: Bibliotecas Externas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao repositório](../docs/localized/README.pt-BR.md)

A Fase 9 introduz pacotes de terceiros depois que as bases da linguagem Python e da biblioteca padrão estão concluídas.

Bibliotecas externas acrescentam uma nova responsabilidade de engenharia: **contratos de dependência**. Um programa passa a depender não apenas do Python, mas também de versões de pacotes, estado de instalação, release notes e limites de compatibilidade.

## Status

> ✅ **Concluída**

## Trilha de aprendizagem

1. ✅ [`pandas`: Trabalhando com Dados Tabulares](01-pandas/README.pt-BR.md)
2. ✅ [`openpyxl`: Automatizando Workbooks do Excel](02-openpyxl/README.pt-BR.md)
3. ✅ [`requests`: Consumindo APIs HTTP](03-requests/README.pt-BR.md)
4. ✅ [`pytest`: Engenharia de Testes Automatizados](04-pytest/README.pt-BR.md)

## Contrato de dependências

Os exemplos executáveis publicados nesta fase usam as dependências declaradas em [`requirements-external.txt`](../requirements-external.txt). O CI do repositório instala esse arquivo antes de executar os exemplos aprovados de bibliotecas externas.

Os contratos publicados têm como alvo **pandas 3.0.x**, **openpyxl 3.1.x**, **Requests 2.34.x** e **pytest 9.1.x**. O pandas 3.0 suporta Python 3.11+, o PyPI declara Python 3.8+ para openpyxl 3.1.5, e Requests 2.34.2 e pytest 9.1.1 exigem Python 3.10+. Este repositório valida os exemplos em Python 3.13.

## O que esta fase estabeleceu

A Fase 9 saiu da biblioteca padrão e entrou em quatro fronteiras de engenharia com terceiros: transformação de dados tabulares, automação de workbooks do Excel, clientes HTTP/API e testes automatizados. Cada capítulo trata a biblioteca como uma dependência versionada com contratos explícitos de comportamento, segurança e validação.

A próxima fase é **Fase 10: Projetos Práticos**.
