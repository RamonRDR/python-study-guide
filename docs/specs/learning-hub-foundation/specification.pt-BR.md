# Phase II: Learning Hub Foundation — especificação

[🇺🇸 English](specification.md) · [🇧🇷 Português](specification.pt-BR.md) · [🇪🇸 Español](specification.es.md)

Status: proposta para revisão. Direção aprovada em 25/11/2026. Baseline: main em 86f1c8517ef8e0e51d97e03388075a4d3fe41386.

## Finalidade

Aprimorar o Python Study Guide independente e permitir consumo de seu conteúdo pelo futuro Learning Hub do site pessoal, sem implementar o site aqui. Apoiar prática manual, entrevistas técnicas internacionais e estudo independente no GitHub.

## Baseline

A fundação original e as fases educacionais 1–10 estão concluídas conforme o roadmap existente. A auditoria encontrou 57 diretórios de capítulos e 8 projetos, cada um com READMEs EN/PT-BR/ES (195 arquivos), 498 arquivos versionados e 221 arquivos Python. Presença dos arquivos não comprova equivalência das traduções. O workflow de qualidade da main de 10/11/2026 foi aprovado (execução 42921078332); não houve nova execução durante a auditoria. Os números históricos dos badges referem-se à execução 34731456104, não a contagens atuais.

Recursos visuais existentes, [trilha](../../learning-path.pt-BR.md), [roadmap](../../roadmap.pt-BR.md), [estrutura](../../project-structure.pt-BR.md), [instruções dos agentes](../../../docs/localized/AGENTS.pt-BR.md), [template de PR](../../../.github/pull_request_template.pt-BR.md) e scripts de qualidade permanecem oficiais em seus escopos.

## Requisitos funcionais

| ID | Requisito |
| --- | --- |
| FR-01 | Navegação anterior/índice/próximo em posições consistentes, incluindo transições entre módulos e limites inicial/final nos três idiomas. |
| FR-02 | Introduzir Getting Started (ordem curricular 00), antes de Fundamentals, sem renumerar caminhos existentes. Cobrir downloads oficiais Python e VS Code, Windows/macOS/Linux, PATH quando aplicável, verificação no terminal, extensão Python, seleção de interpretador, pastas, arquivos .py, terminal integrado, primeira execução manual e troubleshooting. VS Code recomendado, não obrigatório. Reutilizar Fundamentals para instrução conceitual de Hello World. Ensinar criação, ativação (ou uso do executável direto), verificação, seleção no VS Code, desativação e recriação de .venv por projeto no Windows/macOS/Linux; instalação com pip, inspeção, registro e restauração de dependências, exclusão do Git e panorama de bibliotecas distinguindo capítulos existentes de candidatos futuros. Nenhuma dependência obrigatória nova de Playwright ou outros pacotes no CI. |
| FR-03 | Atualizar os três READMEs, trilhas, roadmap, estrutura e pré-requisitos conforme necessário; preservar banner, slogan, autoria e orientações técnicas relevantes. Números de badges devem vir de validações bem-sucedidas identificadas. |
| FR-04 | Ensinar programação manual, interpretação de erros, documentação oficial, testes, tentativas independentes, requisitos, especificações, planos, tarefas, critérios de aceite, ADRs e review. Explicar complementaridade entre SDD e TDD; escolher posição após verificar sobreposição. |
| FR-05 | Adicionar fase curricular 11, Problem Solving & Live Coding: raciocínio, strings/números, coleções, funções/recursão, busca/ordenação, algoritmos/complexidade, debugging, refactoring, desafios mistos e prática cronometrada. Easy/Medium/Hard; dicas progressivas, soluções de referência, complexidade e testes incluindo casos de borda. Antes de qualquer desafio afetado, mapear pré-requisitos às aulas existentes e ensinar conceitos ausentes (incluindo recursão, busca/ordenação e complexidade de algoritmos) nos três idiomas; vincular a instrução antes da prática. |
| FR-06 | Adicionar fase curricular 12, Technical Interview Preparation: processo de entrevista, fundamentos, estruturas de dados, OOP, internals, memória, exceções, testes/debugging, APIs/backend, bancos/SQL, engenharia, comportamental, take-home, simulações junior/mid/senior, entrevistas internacionais e inglês técnico. Incluir respostas esperadas, explicações, objetivos, erros comuns, perguntas complementares, exemplos, simulações de 30/45/60 minutos e rubricas objetivas de autoavaliação. |
| FR-07 | Disponibilizar quizzes e contratos de exercícios legíveis por máquinas, IDs estáveis, três idiomas, correção objetiva dos tipos suportados, código Python original compartilhado e soluções testadas contra respostas incorretas representativas. Preservar uso no GitHub e local. |
| FR-08 | Disponibilizar manifesto versionado, schemas, relações, títulos traduzidos, caminhos, recursos, associações de exercícios/quizzes/simulações e compatibilidade no navegador. Consumir revisão imutável validada, sem scraping do HTML GitHub. |
| FR-09 | Validar todo conteúdo novo e afetado, entregando handoff com revisão aprovada, contratos, registros de exemplo, resultados, limitações e pendências. |

## Requisitos não funcionais

- NFR-01: nenhum custo financeiro adicional, servidor/serviço/API pago ou implementação web neste repositório.
- NFR-02: sem duplicação desnecessária; código compartilhado em inglês; toda documentação pública em três idiomas, inclusive arquitetura e engenharia. Documentação privada fica fora do repositório público, preferencialmente em inglês.
- NFR-03: preservar caminhos e funcionalidades; validar links, navegação, exemplos e testes.
- NFR-04: IDs estáveis independentes da ordem, caminhos relativos confinados ao repositório, schema versionado e rastreabilidade de revisão.
- NFR-05: sem correção por IA; respostas públicas somente ocultas visualmente; respostas abertas usam referências e autoavaliação.
- NFR-06: execução no navegador opcional por exercício, sujeita a verificação do runtime; Python local suportado. Sem segredos ou exemplos confidenciais.
- NFR-07: nunca reportar teste não executado como aprovado. Reutilizar CI e adicionar verificações incrementalmente.

## Limites de escopo

Incluídos: conteúdo, metadados, validação e handoff. Excluídos: UI do site, autenticação, sincronização em nuvem, execução em servidor, pagamento, certificação, deploy de produção e avaliação semântica automatizada.

OOP, SQL, algoritmos e internals não são todos ensinados em módulos próprios hoje. Introduzir pré-requisitos antes de avaliar; não presumir domínio nem renumerar fases. A Phase 0 histórica continua Project Foundation; ordem curricular 00 é Getting Started.

## Referências

- [Constituição](../constitution.pt-BR.md)
- [Plano](implementation-plan.pt-BR.md)
- [Tarefas](tasks.pt-BR.md)
- [Critérios de aceite](acceptance-criteria.pt-BR.md)
- [Contrato](integration-contract.pt-BR.md)
- [Decisões arquiteturais](../../adr/README.pt-BR.md)
- [Handoff](handoff.pt-BR.md)
