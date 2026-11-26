# Simulados de entrevistas e autoavaliação

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../23-behavioral-and-international-interviews/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Como usar os simulados

Estude pré-requisitos das perguntas e do exercício selecionados antes da tentativa; feche respostas e referências durante sessão. Use cronômetro, Python 3.13 local e cópia nova do starter fora do repositório. Trabalhe sozinho ou peça a colega para ler perguntas, não resolver. Sem IA ou dicas na tentativa independente. Estes são tempos de prática, não critérios universais de contratação. Se acabar o tempo, pare e documente o realmente concluído. Dificuldade de exercício e senioridade de entrevista são distintas; exercícios escolhidos apenas oferecem desafio progressivo. Execução no navegador permanece não verificada.

## Pontuação manual

Cinco dimensões somam 100 pontos: conhecimento técnico 25, resolução de problemas 25, comunicação 20, testes e bordas 15, julgamento de engenharia 15. Cada dimensão lista indicadores observáveis e três faixas permitidas: atribua pontos totais se todos indicadores forem demonstrados, parciais se ao menos um mas não todos forem demonstrados, ou zero se nenhum for demonstrado. Não atribua pontos por execução meramente planejada quando indicador exige execução real. Registre evidências e dicas, e não conte sotaque, velocidade de fala ou métricas inventadas. Pontuações são feedback de prática, não certificação ou avaliação semântica automática. Notas individuais do banco são separadas. Após cronômetro, revise respostas e compare com referência existente do exercício e testes confiáveis. Testes funcionais sozinhos não provam algoritmo ou complexidade.

O [índice canônico de simulados](../../interviews/mocks/mock-index.json) e registros geram as seções abaixo.

<!-- interview-mocks:start -->
## Simulado Junior

`mock.junior-30` · `junior`

**Duração (minutos):** 30

Use pergunta 1 na apresentação (STAR breve); responda 2–4 em voz alta sem abrir respostas. Em diretório pessoal novo, implemente exercício vinculado com starter e contrato original. Separe tempos de código e testes; execute assertions próprias para rótulos normais, vazios e repetidos/sensíveis a maiúsculas e confira preservação da entrada. Na discussão, explique complexidade, alternativa e comportamento incompleto. Pare aos 30 minutos; não abra dicas, soluções ou respostas até terminar.

| Etapa | Minutos |
| --- | ---: |
| Apresentação | 3 |
| Perguntas técnicas | 7 |
| Live coding | 13 |
| Testes | 4 |
| Discussão | 3 |

**Sequência de perguntas**

1. [`behavioral.star-evidence`](../22-technical-interview-question-bank/README.pt-BR.md#behavioralstar-evidence)
2. [`python.mutable-default`](../22-technical-interview-question-bank/README.pt-BR.md#pythonmutable-default)
3. [`algorithms.frequency-map`](../22-technical-interview-question-bank/README.pt-BR.md#algorithmsfrequency-map)
4. [`testing.specific-catch`](../22-technical-interview-question-bank/README.pt-BR.md#testingspecific-catch)

**Exercício:** [`problem-solving.label-counts`](../../exercises/problem-solving/label-counts/README.pt-BR.md)

### Rubrica de pontuação

**Conhecimento técnico (0 / 12 / 25)**

- Prevê ambas saídas do padrão mutável e dá correção com None.
- Explica por que dicionário preserva contagens e ValueError é tratado especificamente.

**Resolução de problemas (0 / 12 / 25)**

- Reformula contagem de rótulo exato e simula exemplo duplicado.
- Implementa acumulação correta e retorna dicionário sem mutar entrada ou imprimir.

**Comunicação (0 / 10 / 20)**

- Dá STAR conciso verdadeiro ou explicitamente fictício com ação e resultado pessoal.
- Explica abordagem em voz alta e distingue concluído, falho e não testado.

**Testes e casos de borda (0 / 7 / 15)**

- Executa assertions de caso duplicado normal e entrada vazia com valores exatos.
- Confere rótulos sensíveis a maiúsculas e confirma entrada mutável intacta; informa resultados reais.

**Julgamento de engenharia (0 / 7 / 15)**

- Explica tempo esperado O(n) sob hipóteses de rótulos limitados/hash e distingue espaço de saída exigida.
- Compara conjunto ou varreduras repetidas com mapa de frequências e declara limitação/próximo passo.

**Autoavaliação:** Após cronômetro, marque cada indicador demonstrado com evidência (explicação falada, código ou saída real de teste). Atribua uma faixa por dimensão pela regra acima; some de 100. Mantenha trabalho incompleto visível. Registre dicas separadamente. Pontos do banco são apenas diagnósticos e não somam à nota do simulado.

**Melhoria:** Escolha dimensão de menor pontuação; revise pré-requisito, reimplemente contagem de rótulos com exemplos novos e reexecute entradas vazia, repetida e sensível a maiúsculas. Repita depois com exercício comparável diferente; compare evidência real, não só pontos.

## Simulado Mid-level

`mock.mid-45` · `mid`

**Duração (minutos):** 45

Comece pergunta 1 em inglês, incluindo requisito alterado e status honesto de teste. Responda 2–4 no tempo técnico. Implemente exercício de índice de inserção pelo starter, mantendo contrato de entrada ordenada; 20 minutos de código são menos que estimativa individual de 22. Nos testes, execute assertions próprias para vazio, duplicados, alvos ausentes abaixo/entre/acima e entrada intacta. Discuta invariante do intervalo semiaberto, hipóteses de complexidade e comportamento não verificado. Pare aos 45 minutos; sem dicas, soluções ou respostas durante tentativa.

| Etapa | Minutos |
| --- | ---: |
| Apresentação | 5 |
| Perguntas técnicas | 10 |
| Live coding | 20 |
| Testes | 5 |
| Discussão | 5 |

**Sequência de perguntas**

1. [`behavioral.international-clarification`](../22-technical-interview-question-bank/README.pt-BR.md#behavioralinternational-clarification)
2. [`python.parameter-rebinding`](../22-technical-interview-question-bank/README.pt-BR.md#pythonparameter-rebinding)
3. [`sql.zero-child-count`](../22-technical-interview-question-bank/README.pt-BR.md#sqlzero-child-count)
4. [`api.idempotent-retry`](../22-technical-interview-question-bank/README.pt-BR.md#apiidempotent-retry)

**Exercício:** [`problem-solving.binary-insertion-index`](../../exercises/problem-solving/binary-insertion-index/README.pt-BR.md)

### Rubrica de pontuação

**Conhecimento técnico (0 / 12 / 25)**

- Distingue reatribuição de parâmetro de mutação compartilhada.
- Explica filtro/contagem de LEFT JOIN inclusive zero e identidade estável do grupo.
- Distingue risco de retry POST de idempotência de efeito PUT/DELETE e propõe política limitada.

**Resolução de problemas (0 / 12 / 25)**

- Reformula primeira posição de inserção inclusive duplicados e simula intervalo semiaberto.
- Implementa busca binária logarítmica com limites corretos sem mutação ou validação por varredura.

**Comunicação (0 / 10 / 20)**

- Esclarece requisito alterado em inglês compreensível e dá exemplo discriminante.
- Narra invariante e comunica status real de testes e limitações sem alegar testes não executados.

**Testes e casos de borda (0 / 7 / 15)**

- Executa assertions de valores exatos para vazio e duplicados.
- Executa casos ausentes abaixo, entre e acima e verifica preservação da entrada.

**Julgamento de engenharia (0 / 7 / 15)**

- Justifica O(log n) comparações e O(1) extra para acesso aleatório ordenado e comparações limitadas.
- Explica ordenação como pré-condição do chamador e identifica custo de varredura de validação ou próximo passo de verificação.

**Autoavaliação:** Após cronômetro, marque cada indicador demonstrado com evidência (explicação falada, código ou saída real de teste). Atribua uma faixa por dimensão pela regra acima; some de 100. Mantenha trabalho incompleto visível. Registre dicas separadamente. Pontos do banco são apenas diagnósticos e não somam à nota do simulado.

**Melhoria:** Escolha dimensão mais fraca; simule intervalo semiaberto com alvos duplicados e ausentes, escreva caso de regressão que falhe pela lacuna e repita com lista ordenada nova. Ensaie esclarecimento em inglês sem decorar exemplo.

## Simulado Senior

`mock.senior-60` · `senior`

**Duração (minutos):** 60

Use pergunta 1 como apresentação fictícia de decisão colaborativa; responda 2–4 no tempo técnico. Implemente exercício de dois ponteiros agrupados em diretório pessoal novo, preservando contrato original. Estimativa individual de 40 minutos é deliberadamente comprimida em 25 de código; solução parcial correta e limitações precisas são evidência útil, não motivo para ocultar incompletude. Execute assertions próprias para vazio, sem par, grupos duplicados distintos, grupo todo igual e preservação de entrada no tempo de testes. Na discussão, justifique contagem agrupada, complexidade, escolhas de verificação de transação/autorização e risco mensurável. Pare aos 60 minutos; sem dicas, soluções ou respostas até terminar.

| Etapa | Minutos |
| --- | ---: |
| Apresentação | 5 |
| Perguntas técnicas | 15 |
| Live coding | 25 |
| Testes | 5 |
| Discussão | 10 |

**Sequência de perguntas**

1. [`behavioral.evidence-disagreement`](../22-technical-interview-question-bank/README.pt-BR.md#behavioralevidence-disagreement)
2. [`internals.gil-workload`](../22-technical-interview-question-bank/README.pt-BR.md#internalsgil-workload)
3. [`api.object-authorization`](../22-technical-interview-question-bank/README.pt-BR.md#apiobject-authorization)
4. [`sql.atomic-transfer`](../22-technical-interview-question-bank/README.pt-BR.md#sqlatomic-transfer)

**Exercício:** [`problem-solving.sorted-pair-multiplicity`](../../exercises/problem-solving/sorted-pair-multiplicity/README.pt-BR.md)

### Rubrica de pontuação

**Conhecimento técnico (0 / 12 / 25)**

- Distingue CPython 3.13 com GIL de free-threaded experimental e propõe concorrência adequada com sincronização.
- Exige autorização por objeto com identidade verificada e política de negação consistente sem dados protegidos.
- Explica ACID e transação com débito condicional, rollback e evidência de commit entre conexões.

**Resolução de problemas (0 / 12 / 25)**

- Reformula contagem de pares de índices distintos e explica invariante de dois ponteiros agrupados e regra de eliminação.
- Implementa multiplicação de grupos distintos e contagem combinatória dos iguais sem dupla contagem, mutação ou armazenamento extra proporcional a n.

**Comunicação (0 / 10 / 20)**

- Explica divergência fictícia por objetivos comuns, alternativas e evidências sem resultados inventados.
- Comunica invariantes, riscos, resultados verificados e solução parcial honestamente.

**Testes e casos de borda (0 / 7 / 15)**

- Executa testes de contagem exata para grupos duplicados distintos e todos iguais.
- Executa testes vazio/sem par e verifica entrada intacta; propõe comparação com oráculo independente para validar mais.

**Julgamento de engenharia (0 / 7 / 15)**

- Justifica tempo linear e espaço extra constante sob aritmética limitada, sem alegar testes provam complexidade.
- Propõe validação mensurável e rollback ou mitigação para risco de engenharia, com limites da verificação.

**Autoavaliação:** Após cronômetro, marque cada indicador demonstrado com evidência (explicação falada, código ou saída real de teste). Atribua uma faixa por dimensão pela regra acima; some de 100. Mantenha trabalho incompleto visível. Registre dicas separadamente. Pontos do banco são apenas diagnósticos e não somam à nota do simulado.

**Melhoria:** Escolha dimensão mais fraca; compare solução de dois ponteiros agrupados com oráculo de força bruta pequeno em duplicados e entradas todas iguais. Revise GIL, autorização ou decisões conforme evidências. Repita com outro problema difícil e documente risco que verificaria.

<!-- interview-mocks:end -->

<!-- chapter-navigation:bottom -->
[← Anterior](../23-behavioral-and-international-interviews/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
