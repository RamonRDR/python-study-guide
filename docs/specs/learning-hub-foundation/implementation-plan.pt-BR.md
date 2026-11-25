# Plano de implementação

[🇺🇸 English](implementation-plan.md) · [🇧🇷 Português](implementation-plan.pt-BR.md) · [🇪🇸 Español](implementation-plan.es.md)

Status: proposta para revisão. Executar somente após aprovação e merge do PR de especificação.

## Sequência de entrega

| Sprint | Branch proposta | Entrega / dependência |
| --- | --- | --- |
| 00 | docs/learning-hub-specification | Auditoria, constituição, especificação, plano, tarefas, critérios, contratos preliminares e ADRs. |
| 01 | feat/chapter-navigation | Inventariar idiomas de capítulos/projetos, definir navegação ordenada, validar links recíprocos e entre módulos; currículo existente primeiro. |
| 02 | feat/getting-started | Onboarding localizado e conexão a Fundamentals; ampliar testes de navegação e índices. Adicionar aulas de venv local ao projeto e gerenciamento de pip/dependências; documentar candidatos à expansão de bibliotecas separadamente da Fase 9 concluída, com revisão de pré-requisitos e PRs futuros separados. Adicionar sexta aula de Git básico e registrar links recíprocos futuros entre guias no registro de integração; manter Git avançado e automação específica de plataformas no guia separado. |
| 03 | docs/readme-and-badges | Atualizar três READMEs, trilhas, roadmap e estrutura; badges somente com evidências. |
| 04 | feat/manual-programming-practices | Ensinar prática manual e SDD/TDD; referenciar orientação existente de manutenção por IA. Aplicar fluxo pequeno de branch/PR/teste/revisão específico de Python, sem duplicar o curso independente de Git. |
| 05 | feat/problem-solving-live-coding | Auditar pré-requisitos de todos os tópicos FR-05; ensinar conceitos ausentes nos três idiomas antes da prática correspondente; depois pilotar desafio conforme contrato preliminar e expandir por conceito/dificuldade com testes. |
| 06A1 | feat/interview-foundations | Aulas 01–08, mapa de pré-requisitos, OOP |
| 06A2 | feat/interview-python-internals | Aulas 09–14, internals e memória |
| 06A3 | feat/interview-backend-and-databases | Aulas 15–21, backend, SQL, engenharia; gate T06-01 |
| 06B | feat/technical-interview-pilot | Aula 22, nove perguntas piloto e validação |
| 06C | feat/technical-interview-question-bank | 48 perguntas técnicas adicionais |
| 06D | feat/mock-and-international-interviews | Aulas 23–24, três perguntas comportamentais/internacionais e três simulados; AC-06 |
| 07 | feat/quiz-and-exercise-bank | Materializar registros e schemas versionados; validar IDs, traduções, pontuação, soluções e implementações incorretas representativas. |
| 08 | feat/learning-hub-content-contract | Finalizar manifesto, validação do consumidor, fixtures, versionamento e compatibilidade. |
| 09 | docs/learning-hub-handoff | QA completo, revisão final, evidências e handoff de revisão aprovada. |

Dividir sprints grandes em PRs focados com sufixos descritivos. Criar cada branch da main atual após merge das dependências. Não fazer merge sem aprovação. Usar squash merge conforme AGENTS.md.

## Estratégia de validação

Reutilizar scripts/check_internal_links.py, scripts/validate_repository_structure.py, scripts/run_examples.py, scripts/example_manifest.txt, tests/ e workflow de qualidade. O manifesto de exemplos continua sendo lista de execução autorizada, não fonte curricular. Adicionar testes determinísticos de navegação, restrições de schema, unicidade, referências e correção na sprint correspondente. Usar biblioteca padrão quando suficiente; avaliar validador gratuito de schema na implementação. Manter código inicial sintaticamente válido ou trechos incompletos como dados para não quebrar compileall.

Usar jobs Linux e Windows existentes; não transformar exemplos dependentes de SO ou rede em execução incondicional no navegador. Compatibilidade do navegador é obrigação de teste do consumidor; estados explícitos local-only e unverified.

## Integração

Usar snapshot de conteúdo fixado por revisão no build do site, caminhos relativos normalizados e renderização Markdown segura. Sem dependência da API GitHub por estudante. O site controla ciclo de vida Pyodide/worker, UI, progresso e limites de recursos; o guia controla conteúdo e testes determinísticos. Ver [contrato](integration-contract.pt-BR.md) e [ADRs](../../adr/README.pt-BR.md).

## Controle de mudanças

Para cada PR: consultar especificações, registrar escopo, revisar diffs, executar verificações aplicáveis, informar omissões, solicitar Codex Review, corrigir findings, revalidar e obter aprovação explícita. Atualizar tarefas no mesmo PR quando possível; histórico Git evidencia merge. Manter roadmap educacional separado. Toda documentação pública deve ter EN, PT-BR e ES no mesmo PR; verificar estruturalmente e revisar equivalência humana.

Após CI e Codex Review aprovarem o head exato, conclua a Final Pre-Merge Audit definida em AGENTS.md e registre evidências no PR. Qualquer alteração do head invalida verificações e auditoria; repita antes da aprovação do mantenedor.

[Registro de integração de guias relacionados](related-guides.pt-BR.md)
