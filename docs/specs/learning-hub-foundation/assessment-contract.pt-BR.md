# Contrato de avaliações e plano de entrega

[EN](assessment-contract.md) · [PT-BR](assessment-contract.pt-BR.md) · [ES](assessment-contract.es.md)

Sprint 07A: somente fundação. O mantenedor aprovou a distribuição de 160 questões e o piloto. Este PR não publica questões, migra exercícios, implementa execução no navegador nem finaliza o manifesto curricular.

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
Baseline: `bf56305f42d10ab7c5b31c2b70f6c38140353db4`. Ver [encerramento da Sprint 06](https://github.com/RamonRDR/python-study-guide/pull/101#issuecomment-7193467128). Os 30 exercícios existentes têm 192 casos e nenhuma dependência externa declarada; execução no navegador não verificada. Piloto de vogais antigo não possui practice_mode e assumptions de complexidade; normalizar explicitamente na migração. Preservar índice legado de 29 entradas até migração aprovada. Revisar evidência pedagógica por questão e soluções por exercício nos PRs correspondentes. CI no head exato, Codex Review, Final Pre-Merge Audit e autorização do mantenedor seguem obrigatórios.
