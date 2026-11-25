# ADR 0001: Fonte única da verdade do conteúdo

[🇺🇸 English](0001-content-source-of-truth.md) · [🇧🇷 Português](0001-content-source-of-truth.pt-BR.md) · [🇪🇸 Español](0001-content-source-of-truth.es.md)

Status: proposto (direção aprovada em 25/11/2026; revisão do PR pendente).

## Contexto

O guia atual é utilizável independentemente em três idiomas. O futuro site necessita do mesmo material, sem manter cópias manualmente ou acoplar o guia ao site.

## Decisão

Manter o repositório GitHub como fonte oficial de Markdown, Python e dados estruturados. Importar revisões imutáveis e validadas durante o build do site. Preservar caminhos existentes e utilização pelo GitHub e localmente. Manter a implementação do site fora deste repositório.

## Alternativas

Conteúdo separado mantido manualmente no site (rejeitado: divergência); chamadas à API GitHub em tempo de execução para cada estudante (rejeitado como padrão: dependência de disponibilidade e limites); scraping do HTML GitHub (rejeitado: acoplamento frágil à apresentação).

## Consequências

O consumidor precisa de processo explícito de atualização/build, rastreamento de revisão, renderização segura e validação. Atualizações podem não aparecer até novo build. Não se prevê novo serviço pago.
