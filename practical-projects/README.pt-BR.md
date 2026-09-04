<div align="center">

# Projetos Práticos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para a página inicial do repositório](../docs/localized/README.pt-BR.md)

A Fase 10 combina conceitos das fases anteriores em fluxos completos e testáveis. Os projetos enfatizam requisitos, decisões de design, implementação, validação, caminhos de extensão e comunicação de portfólio.

## Status

> 🚧 **Em andamento**

## Trilha de projetos

1. ✅ [Controle de Despesas](01-expense-tracker/README.pt-BR.md)
2. ✅ [Calculadora de Notas](02-grade-calculator/README.pt-BR.md)
3. ✅ [Cadastro de Usuários](03-user-registration/README.pt-BR.md)
4. ✅ [Analisador CSV](04-csv-analyzer/README.pt-BR.md)
5. ✅ [Gerador de Relatórios](05-report-generator/README.pt-BR.md)
6. ✅ [Organizador de Arquivos](06-file-organizer/README.pt-BR.md)
7. 🚧 [Fluxo Fictício de Conciliação](07-fictional-reconciliation-workflow/README.pt-BR.md)
8. ⏳ Fluxo Simulado de Automação

## Contrato dos projetos

Cada projeto deve incluir:

- requisitos explícitos;
- notas de design e trade-offs;
- implementação funcional;
- demonstração determinística quando apropriado;
- testes automatizados dos comportamentos importantes;
- explicação de caminhos de falha;
- desafios de extensão;
- discussão de portfólio.

O Projeto 01 estabelece o padrão de integração com registros monetários validados e persistência. O Projeto 02 amplia esse padrão com políticas de notas configuráveis, agregação ponderada exata, estados parcial/final explícitos, relatório estruturado e cobertura pytest focada em fronteiras. O Projeto 03 adiciona dados de identidade canônicos, prevenção de duplicidade, índices secundários de lookup, atualizações seguras de campos indexados e transições explícitas de ciclo de vida sem introduzir autenticação. O Projeto 04 adiciona schemas CSV exatos, conversão tipada, separação entre falhas estruturais e falhas de linha, parsing com sucesso parcial, identificadores duplicados, filtros determinísticos e agregação sem esconder a ingestão atrás de pandas. O Projeto 05 transforma registros operacionais validados em artefatos de relatório determinísticos com janelas explícitas de datas, métricas exatas de resumo, renderizadores TXT/Markdown e escrita UTF-8, mantendo agregação, apresentação e persistência separadas. O Projeto 06 adiciona descoberta rasa no filesystem, classificação por sufixo, planejamento imutável de movimentos, políticas explícitas de colisão, fronteiras de symlink, revalidação no momento da execução e proteção exata no-replace do destino antes da organização em pastas por categoria. O Projeto 07 adiciona registros de conciliação validados, comparação monetária exata com `Decimal`, rejeição de chaves duplicadas, classificação determinística em quatro estados, diferenças com sinal, resumos imutáveis e resultados de domínio separados da apresentação.
