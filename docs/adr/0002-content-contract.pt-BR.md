# ADR 0002: Contrato de conteúdo versionado

[🇺🇸 English](0002-content-contract.md) · [🇧🇷 Português](0002-content-contract.pt-BR.md) · [🇪🇸 Español](0002-content-contract.es.md)

Status: direção arquitetural aceita ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)); execução no navegador permanece não verificada.

## Contexto

Markdown proporciona boa experiência de leitura, mas sozinho é insuficiente para navegação programática confiável, correção de quizzes e associação de exercícios.

## Decisão

Usar registros JSON e manifesto curricular versionado que referencie arquivos existentes, com IDs estáveis independentes da ordem, campos localizados e referências validadas. Manter scripts/example_manifest.txt como lista de execução autorizada. Definir registros preliminares antes dos pilotos; finalizar schemas com exemplos reais e testes nas Sprints 07–08.

## Alternativas

Inferir metadados de nomes/Markdown (frágil); duplicar Python por idioma (custo de manutenção); substituir Markdown por JSON exclusivo (prejudica uso no GitHub).

## Consequências

Validadores devem detectar erros de schema, referências órfãs, caminhos inseguros, duplicatas e idiomas ausentes. Conteúdo educacional segue disponível no GitHub; registros estruturados são canônicos quando aplicável, preferindo visualizações geradas ou referências à duplicação manual de texto.
