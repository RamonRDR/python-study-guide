# Contrato de avaliações e plano de entrega

[EN](assessment-contract.md) · [PT-BR](assessment-contract.pt-BR.md) · [ES](assessment-contract.es.md)

Sprints 07A e 07B integradas e CI pós-merge aprovado ([PR #102](https://github.com/RamonRDR/python-study-guide/pull/102), [PR #103](https://github.com/RamonRDR/python-study-guide/pull/103), [CI de B](https://github.com/RamonRDR/python-study-guide/actions/runs/45872609920)). C1 implementa 78 quizzes de fundamentos; migração além do piloto e runtime no navegador estão fora do escopo.

## Escopo e aceite
- Inventário: 115 entradas, 345 caminhos localizados, 64 quizzes easy / 67 medium / 29 hard (2.850 XP a 10/20/30). A [matriz de distribuição](assessment-matrix.json) é metadado de planejamento de engenharia, não manifesto do consumidor. Alocações zero preservam prática manual ou evitam avaliação repetida.
- Antes de criar cada questão, inspecionar as seções de origem nos três idiomas e registrar títulos exatos nos pré-requisitos; ensinar conceitos ausentes primeiro. A matriz estabelece caminhos por aula, não comprova revisão semântica completa das traduções. Não alegar que quiz mede senioridade.
- Usar JSON Schema Draft 2020-12 e verificações de relacionamentos em Python; versão 1.0.0. Preservar IDs, caminhos, soluções, restrições e testes existentes. Campos desconhecidos e versões não suportadas são rejeitados. Entrevistas mantêm seu contrato preliminar próprio.
- Respostas: ID estável de alternativa para multiple_choice/error_identification; booleano estrito para true_false; strings aceitas explícitas para output_prediction/objective_code_completion. Comparação exata, salvo normalização LF expressamente selecionada em output_prediction; sem eval ou correção semântica.
- Interface: somente function_call na v1, argumentos/resultados compatíveis com JSON, tipo e valor exatos recursivamente, valores de entrada preservados, silêncio e exigência declarada de novo contêiner quando aplicável. Testes funcionais não provam complexidade ou qualidade de refatoração. Timeout é limite declarado, não imposto pelo comparador puro. CI não executa código arbitrário do aluno.
- Decodificação JSON rejeita chaves duplicadas e números não finitos. Inteiros Python podem exceder a faixa segura JavaScript: preservar tokens inteiros canônicos, usar parsing sem perda ou correção em Python no consumidor futuro; nunca arredondar ou converter silenciosamente. Navegador permanece unverified; testes reais de runtime pertencem ao site.
- Validar índices, IDs únicos, mapas de idioma, caminhos existentes seguros, títulos de ensino, exemplos/casos e respostas. Código compartilhado. Testes usam fixtures, incluindo registros inválidos; registros publicados chegam em B–D. Sem novos serviços pagos.

## Entrega
A: contrato, matriz e validadores de fixtures; B: dez quizzes (dois por tipo) e três exercícios existentes (vowel-counter, binary-insertion-index, inventory-reconciliation); C1: completar 78 quizzes de fundamentos; C2: completar 160; D: outros 27 exercícios; E: encerramento AC-07. Dez pilotos contam nos 160. Nenhum PR posterior antes de integração e CI aprovado do anterior.

## Evidências e limitações
Baseline: `bf56305f42d10ab7c5b31c2b70f6c38140353db4`. Ver [encerramento da Sprint 06](https://github.com/RamonRDR/python-study-guide/pull/101#issuecomment-7193467128). Os 30 exercícios existentes têm 192 casos e nenhuma dependência externa declarada; execução no navegador não verificada. O piloto antigo de vogais não possuía practice_mode e assumptions de complexidade; foram normalizados em B. Preservar índice legado de 29 entradas até migração aprovada. Revisar evidência pedagógica por questão e soluções por exercício nos PRs correspondentes. CI no head exato, Codex Review, Final Pre-Merge Audit e autorização do mantenedor seguem obrigatórios.

## Aceite do piloto (07B)

- Publicar exatamente dez questões, duas por tipo, sete easy e três medium (130 XP), com três variantes de idioma e títulos exatos dos pré-requisitos. Contabilizá-las na matriz aprovada, sem duplicar código Python por idioma.
- Migrar somente vowel-counter, binary-insertion-index e inventory-reconciliation para 1.0.0, preservando os 24 casos canônicos e implementações existentes. Manter os outros 27 registros legados e índice de expansão intactos. Índice parcial versionado identifica os três registros migrados.
- Executar ambos os novos índices no CI, rejeitar registros versionados não indexados ou inesperados, testar limites de alocação e verificar soluções confiáveis e candidatos incorretos representativos. Rejeitar resultados esperados contraditórios para entradas de tipos e valores iguais. Quando novo contêiner for exigido, rejeitar aliases a contêineres mutáveis internos das entradas e aliases diretos. Detecção de mutação compara estado final, não cada operação intermediária.
- Sem execução de código do aluno, nova dependência paga ou alegação de runtime. Os 150 quizzes e 27 migrações restantes pertencem a C1/C2/D; AC-07 encerra somente em E.

## Aceite dos fundamentos (07C1)

- Completar todas as alocações aprovadas dos módulos 00–05, incluindo os dez quizzes piloto: 78 no total (37 easy, 30 medium, 11 hard; 1.300 XP). Adicionar somente 68 registros. Preservar os três exercícios versionados e banco legado. C2 cobre os outros 82 quizzes.
- Ler as seções de ensino em EN/PT-BR/ES antes de redigir; manter títulos localizados exatos, IDs estáveis, exemplos originais, código único compartilhado e respostas aceitas explícitas. Refinar os pré-requisitos de quebra de linha nas duas questões piloto de saída; preservar respostas. Equilibrar verdadeiro/falso no banco ampliado e variar posições das alternativas.
- Preservar regressões do piloto e exigir alocação exata por aula/dificuldade, cobertura do índice, paridade de idiomas e correção determinística. Testar exemplos literais confiáveis, não código arbitrário lido dos registros. Revisar ambiguidades, casos-limite, dificuldade, navegação e privacidade antes de solicitar aprovação do merge.
- Sem runtime, dependência paga, migração de exercícios ou encerramento AC-07 em C1. Todos os gates no head exato permanecem obrigatórios.
