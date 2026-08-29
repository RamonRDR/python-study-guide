<div align="center">

# Fase 9: Bibliotecas Externas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao repositório](../docs/localized/README.pt-BR.md)

A Fase 9 introduz pacotes de terceiros depois que as bases da linguagem Python e da biblioteca padrão estão concluídas.

Bibliotecas externas acrescentam uma nova responsabilidade de engenharia: **contratos de dependência**. Um programa passa a depender não apenas do Python, mas também de versões de pacotes, estado de instalação, release notes e limites de compatibilidade.

## Status

> 🚧 **Em andamento**

## Trilha de aprendizagem

1. ✅ [`pandas`: Trabalhando com Dados Tabulares](01-pandas/README.pt-BR.md)
2. ⏳ `openpyxl`: automação de workbooks do Excel
3. ⏳ `requests`: clientes HTTP e consumo de APIs
4. ⏳ `pytest`: testes automatizados

## Contrato de dependências

Os exemplos executáveis publicados nesta fase usam as dependências declaradas em [`requirements-external.txt`](../requirements-external.txt). O CI do repositório instala esse arquivo antes de executar os exemplos aprovados de bibliotecas externas.

O capítulo de pandas tem como alvo **pandas 3.0.x**. O pandas 3.0 suporta Python 3.11+, enquanto este repositório continua validando os exemplos em Python 3.13.

## Por que esta fase vem agora

As fases anteriores estabeleceram coleções, funções, erros, arquivos, módulos, CSV/JSON, datas, caminhos, logging, iteração, aritmética decimal e contratos de filesystem. Bibliotecas externas devem construir sobre essas habilidades, não substituí-las.

O próximo capítulo planejado é **`openpyxl`**.
