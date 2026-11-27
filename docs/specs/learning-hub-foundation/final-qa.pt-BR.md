# QA final e evidências de aceite (09A)

[EN](final-qa.md) · [PT-BR](final-qa.pt-BR.md) · [ES](final-qa.es.md)

Evidências da baseline, não aprovação final do AC-09. O mantenedor aprovou o plano em dois PRs. A fonte é o commit exato da main pós-merge abaixo; o próprio PR de QA exige novo CI, Codex, auditoria final, autorização explícita de squash e CI de push. 09B validará o commit de conteúdo resultante usando lock externo e completará o handoff.

## Baseline verificada e governança

`a8a264f9f36ec276f0ad8e35f10f2d76f82fe211`

[PR #112](https://github.com/RamonRDR/python-study-guide/pull/112) · [CI #46053604048](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048) · [Linux job](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048/job/140690676913) · [Windows job](https://github.com/RamonRDR/python-study-guide/actions/runs/46053604048/job/140690677260) · [AC-08](https://github.com/RamonRDR/python-study-guide/pull/112#issuecomment-7226219176)

A main correspondia à árvore auditada `ef3b153ceae4eb98e97c124510e7962ff5969a90`, sem PR aberto na consulta inicial. Ruleset 20301083 ativo, checks strict, PR e resolução de threads obrigatórios, histórico linear, somente squash, proteção de exclusão/non-fast-forward, sem bypass. Sem mínimo de aprovações humanas exigido; aprovação do mantenedor e Codex continuam gates operacionais. Licença MIT, autoria e política de contribuição inspecionadas. Árvore recursiva com 1.236 blobs, sem symlinks/submodules ou nomes de arquivos compatíveis com padrões comuns de chaves privadas/credenciais/.env; triagem de nomes não equivale a scanner de segredos ou auditoria integral de privacidade histórica. Sem certificação de segurança.

## Resultados do CI (suítes separadas)

| Suíte | Aprovados | Skipped |
| --- | ---: | ---: |
| Quality unittest | 180 | 0 |
| Engineering unittest | 7 | 0 |
| Practical pytest (Linux) | 406 | 1 |
| File Organizer pytest (Windows) | 63 | 17 |

A mesma execução Linux completou 210 exemplos autorizados, 9.273 links internos em 580 documentos Markdown, estrutura de idiomas, 345 documentos de navegação, compileall, estrutura do repositório, inventários de avaliações e currículo e fixture histórica de consumidor fixada. A suíte Windows é subconjunto dos testes práticos Linux; não somar contagens. Disponibilidade de URLs externas e execução de exemplos fora da lista não foram comprovadas.

## Rastreabilidade de aceite

| Critério | Evidência integrada | Verificação da baseline / limite residual |
| --- | --- | --- |
| AC-00 | [PR #87](https://github.com/RamonRDR/python-study-guide/pull/87) | Constituição, especificações, ADRs e workflow presentes; merge histórico verificado. |
| AC-01 | [PR #88](https://github.com/RamonRDR/python-study-guide/pull/88) | Validador de navegação e testes negativos; 345 documentos localizados. |
| AC-02 | [PR #89](https://github.com/RamonRDR/python-study-guide/pull/89) | Seis aulas de onboarding e escopo Git/ambientes estabelecido; instalação/download/rede não reexecutados em cada SO. |
| AC-03 | [PR #90](https://github.com/RamonRDR/python-study-guide/pull/90) | Três READMEs e trilhas mestras inspecionados; badges atualizados na 09A, checks estruturais repetidos no PR. |
| AC-04 | [PR #91](https://github.com/RamonRDR/python-study-guide/pull/91) | Orientação de prática manual e SDD/TDD; sete testes de engenharia; introdução amostrada. |
| AC-05 | [PR #95](https://github.com/RamonRDR/python-study-guide/pull/95) | Mapa de pré-requisitos, testes de desafios e migração; 30 exercícios canônicos, testes de referências confiáveis e soluções incorretas. |
| AC-06 | [PR #101](https://github.com/RamonRDR/python-study-guide/pull/101) | Mapa de pré-requisitos, validadores de perguntas/simulados; 60 perguntas e três simulados, autoavaliação humana. |
| AC-07 | [PR #107](https://github.com/RamonRDR/python-study-guide/pull/107) | 160 quizzes e 30 exercícios cobertos por testes de validação/fixtures existentes; JSON/tipos estritos, respostas incorretas e implementações de referência/negativas. |
| AC-08 | [PR #112](https://github.com/RamonRDR/python-study-guide/pull/112) | Manifesto/relacionamentos completos; evidências fixadas 08C e temporárias 08D, snapshots Git semanticamente inválidos e fixtures de rollback. |
| AC-09 | 09A / 09B | Evidências e docs da 09A em revisão; handoff final 09B, validação do pin candidato e gates de HEAD exato/pós-merge pendentes. |

## Inventário curricular e de avaliações

Contagem direta do manifesto e quatro índices: 14 módulos, 115 entradas únicas (107 aulas + oito projetos), 345 caminhos de conteúdo localizado, 42 índices de módulos localizados, 243 recursos de capítulos e seis assets globais. Quatro bancos: 160 quizzes, 30 exercícios, 60 perguntas de entrevista e três simulados (253 registros distintos; 268 associações: 160/30/75/3). Os 75 links de entrevista são referências a pré-requisitos, não 75 perguntas. Manifesto completo, versão 1.0.0. Quiz/exercício 1.0.0; índices entrevista/simulado preliminares 0.1.0; lock externo da fixture 1.0.0. Cinco schemas Draft 2020-12. Testes existentes aprovados verificam dificuldade dos quizzes 64/67/29 e 2.850 XP, exercícios 12/12/6 e 192 casos, entrevistas 24/24/12 e simulados 30/45/60 minutos. Estes últimos valores têm evidência dos testes, não recontagem manual de cada registro.

Revisados campos selecionados dos registros reais `quiz.absolute-distance-zero` (abs(-11) = 11, resposta exata `abs`), `problem-solving.ascii-digit-counter` (dígitos ASCII literais, não dígitos Unicode arbitrários), `interview.allowed-tools` (respeito às regras e declaração de ferramentas), `mock.junior-30` (tempos, perguntas/exercício e rubrica manual). Os textos EN/PT-BR/ES revisados são conceitualmente alinhados. Sem releitura semântica exaustiva dos 253 registros.

## Revisão direcionada de idiomas

Consultada a primeira entrada curricular de cada módulo nos três idiomas (42 documentos). Comparados conceitos introdutórios, títulos de seções e blocos Python cercados por marcadores de código de forma programática; todos os blocos correspondentes são idênticos em bytes entre idiomas (314 por idioma, não todos os exemplos do repositório). Inspeção direcionada assistida por IA, não revisão semântica integral ou humana de cada página; sem certificação de tradução. Cobertura estrutural dos 345 documentos vem do CI. PRs focados anteriores e mapas de pré-requisitos são evidências adicionais, não substitutos de revisão independente.

| Diretório da entrada (README.md, README.pt-BR.md, README.es.md) | Blocos Python por idioma |
| --- | ---: |
| `getting-started/01-install-python` | 0 |
| `fundamentals/01-how-python-runs-a-program` | 9 |
| `strings-and-numbers/01-string-creation-and-indexing` | 25 |
| `collections/01-list-creation-and-indexing` | 22 |
| `program-flow/01-conditions-comparisons-and-boolean-logic` | 46 |
| `functions/01-defining-and-calling-functions` | 30 |
| `comments-and-documentation/01-comments` | 46 |
| `errors-files-and-modules/01-try-except-else-finally` | 39 |
| `standard-library/01-pathlib` | 37 |
| `external-libraries/01-pandas` | 52 |
| `practical-projects/01-expense-tracker` | 7 |
| `manual-programming-practices/01-manual-coding-and-debugging` | 1 |
| `problem-solving-and-live-coding/01-problem-solving-fundamentals` | 0 |
| `technical-interview-preparation/01-understanding-technical-interviews` | 0 |

## Limites e próximo gate

Sem execução local: acesso de rede do container local não resolveu GitHub; evidência de execução da baseline é o GitHub Actions real. Sem Red isolado ou novo comportamento de produção; sem testes artificiais para aumentar contagens. Sem revisão independente integral de prosa, código inline, links externos, credenciais no conteúdo/histórico ou instalações em todas as plataformas. PRs anteriores revisados permanecem evidência; mantenedor deve avaliar risco residual da revisão semântica. Somente fixture de consumidor em Linux e File Organizer em Windows executados. 114 entradas e 30 exercícios não verificados no navegador; File Organizer local_only. Quatro aulas externas declaram requirements-external.txt; sem versão mínima Python inventada para capítulos. Web Worker não é fronteira de segurança; runtime, timeouts, cancelamento, isolamento de saída/rede/armazenamento/credenciais e deploy real são trabalho do consumidor. Testes não comprovam complexidade/refatoração ou mutação transitória; identidade Git não equivale a assinatura. Banco Git/validador confiáveis e staging isolado são premissas, não proteção concorrente do filesystem. Sem rollback atômico real em produção, site, release/tag ou alterações de links entre guias. 09B deve validar o squash real aprovado da 09A; fixture histórica 08C não é pin de produção.
