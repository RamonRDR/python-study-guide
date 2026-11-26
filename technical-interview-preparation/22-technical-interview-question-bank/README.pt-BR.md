# Banco de perguntas de entrevistas técnicas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../21-software-engineering-and-technical-decisions/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:top -->

Nove perguntas piloto: três Junior, três Mid-level e três Senior. Nível indica profundidade esperada, não padrão universal de contratação. Estude primeiro a seção de pré-requisito, responda em voz alta sem abrir referência e depois abra resposta. Atribua a cada critério seus pontos somente se sua resposta o demonstrar; senão zero. Use pontuação para identificar lacunas, não como certificação ou avaliação semântica automática. Perguntas complementares são prática opcional, sem pontuação separada. Registros JSON canônicos e índice em [interviews](../../interviews/README.pt-BR.md); esta seção é gerada a partir deles. Banco técnico completo e simulados estão planejados.

## Perguntas piloto

<!-- interview-questions:start -->
### interview.clarify-contract

`junior` · `interview-fundamentals`

Um entrevistador pede que você conte cadastros elegíveis. Elegibilidade, duplicados e entrada vazia não foram definidos. O que faz antes de programar?

<details>
<summary>Resposta esperada</summary>

Pergunte o que qualifica, se duplicados contam e qual resultado para entrada vazia. Reformule o contrato acordado, dê exemplo concreto e explique como testará antes de implementar.

**Explicação:** Esclarecer evita resolver outro problema. Se uma regra continuar desconhecida, declare hipótese e peça confirmação.

**Intenção do entrevistador:** Avaliar comunicação, raciocínio sobre contrato e planejamento de testes, não só velocidade.

**Erros comuns**

- Começar a programar sem definir elegibilidade.
- Inventar política de duplicados e apresentá-la como dada.

**Perguntas complementares**

- Como mudar de contagem de linhas para IDs distintos afetaria seus testes?

**Exemplo**

Se a regra acordada conta IDs elegíveis distintos, duas linhas elegíveis com ID 7 contam como uma e entrada vazia retorna zero se acordado.

**Rubrica de autoavaliação**

- 1 — Pergunta explicitamente sobre elegibilidade, duplicados e entrada vazia.
- 1 — Reformula contrato e distingue hipóteses de fatos.
- 1 — Fornece exemplo concreto e ao menos um teste relevante.

Máximo: 3

</details>

**Pré-requisitos**

- [Uma conversa prática](../../technical-interview-preparation/01-understanding-technical-interviews/README.pt-BR.md)

### python.mutable-default

`junior` · `python-fundamentals`

Dado `def add(x, items=[]): items.append(x); return items`, o que `print(add(1)); print(add(2))` exibem em chamadas consecutivas? Corrija o comportamento quando a lista é omitida. Preserve a mutação das listas fornecidas explicitamente, inclusive uma lista vazia.

<details>
<summary>Resposta esperada</summary>

As impressões são `[1]` e `[1, 2]`. A lista padrão é criada na definição da função e reutilizada. Use None como padrão e crie lista nova somente quando items for None.

**Explicação:** Atribuição vincula objetos; padrão compartilhado é mutado. Listas fornecidas explicitamente ainda são mutadas nesse contrato.

**Intenção do entrevistador:** Avaliar momento de avaliação, mutabilidade e ownership pretendido.

**Erros comuns**

- Supor lista nova a cada chamada.
- Usar `if not items` e substituir lista vazia fornecida.

**Perguntas complementares**

- O que muda se o chamador fornece lista vazia?

**Exemplo**

```python
def add(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
```

**Rubrica de autoavaliação**

- 1 — Prevê corretamente as duas listas impressas.
- 1 — Explica avaliação única do padrão e mutação compartilhada.
- 1 — Usa None e teste de identidade sem substituir lista vazia fornecida.

Máximo: 3

</details>

**Pré-requisitos**

- [Revisão pelo raciocínio](../../technical-interview-preparation/03-python-fundamentals-review/README.pt-BR.md)

### algorithms.duplicate-membership

`junior` · `data-structures-algorithms`

Detecte se uma lista de IDs hashable contém duplicado. Qual estrutura escolheria e quais custos de tempo e espaço auxiliar?

<details>
<summary>Resposta esperada</summary>

Mantenha conjunto de IDs vistos. Para cada ID, retorne True se já visto, senão insira. Retorne False ao final. Sob hipóteses usuais de hashing no caso médio e hash/igualdade de custo constante, tempo O(n), espaço extra O(n) no pior tamanho de entrada.

**Explicação:** Conjunto permite pertinência sem varrer prefixo repetidamente. Colisões no pior caso podem degradar tempo; hashability é pré-requisito.

**Intenção do entrevistador:** Avaliar escolha da representação, correção e hipóteses de complexidade.

**Erros comuns**

- Alegar busca O(1) garantida no pior caso.
- Esquecer entrada vazia ou tratar IDs iguais como diferentes pela posição.

**Perguntas complementares**

- E se IDs não forem hashable?

**Exemplo**

`[3, 8, 3]` → True; `[]` → False; `[3, 8]` → False.

**Rubrica de autoavaliação**

- 1 — Descreve algoritmo de conjunto de vistos com término correto.
- 1 — Declara tempo médio O(n) com hipóteses de hashing e espaço extra O(n).
- 1 — Confere entrada vazia e repetida e declara requisito hashable.

Máximo: 3

</details>

**Pré-requisitos**

- [Escolha pelo contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.pt-BR.md)

### oop.replaceable-collaborator

`mid` · `oop`

Um notificador de relatórios deve suportar canais de texto e email, depois canal fake em testes. Compare herança e composição; proponha design sem alterar notificador a cada canal. Explique um trade-off e como um fake testaria o contrato.

<details>
<summary>Resposta esperada</summary>

Injete colaborador com contrato send definido; notificador delega a ele. Canais compatíveis podem herdar base ou atender comportamento via duck typing. Herança serve a subtipos reais que respeitam contrato base, não só reutilização.

**Explicação:** Composição torna dependências explícitas e substituíveis, ao custo de indireção. Nomes de métodos sozinhos não asseguram substituição.

**Intenção do entrevistador:** Avaliar contratos comportamentais e decisões de design testável.

**Erros comuns**

- Exigir hierarquia profunda só para reutilizar código.
- Supor que todo método send tem mesma semântica.

**Perguntas complementares**

- O que canal fake deve demonstrar sobre contrato?

**Exemplo**

`Notifier(channel).notify('Ready')` delega ao `send('Ready')` do canal fake, retornando `test: Ready` sem acessar rede.

**Rubrica de autoavaliação**

- 1 — Propõe injeção explícita de colaborador e delegação.
- 1 — Distingue contrato de subtipo de composição e duck typing.
- 1 — Explica teste com fake e ao menos um trade-off.

Máximo: 3

</details>

**Pré-requisitos**

- [Polimorfismo e composição](../../technical-interview-preparation/07-inheritance-polymorphism-and-composition/README.pt-BR.md)

### internals.nested-copy

`mid` · `python-internals`

Dicionário contém duas chaves referenciando mesma lista mutável. Você precisa de grafo independente preservando relação de alias dentro da cópia. Compare atribuição, cópia rasa e profunda. Explique limites da cópia e como testaria isolamento e preservação do alias.

<details>
<summary>Resposta esperada</summary>

Atribuição compartilha dicionário original; cópia rasa cria dicionário externo novo mas compartilha lista. Para esses contêineres nativos, deepcopy copia lista aninhada uma vez e reutiliza cópia para duas chaves via memo.

**Explicação:** Cópia profunda pode preservar referências repetidas e ciclos; não garante clonar cada objeto ou recurso externo. Escolha por ownership e custo.

**Intenção do entrevistador:** Avaliar identidade, aliases aninhados e semântica de cópia.

**Erros comuns**

- Supor cópia rasa isolando valores mutáveis internos.
- Afirmar deepcopy criando objeto novo para cada referência.

**Perguntas complementares**

- Como testaria que mutar lista copiada não afeta original?

**Exemplo**

```python
from copy import deepcopy
shared = [1]
original = {"a": shared, "b": shared}
cloned = deepcopy(original)
assert cloned["a"] is cloned["b"]
assert cloned["a"] is not shared
```

**Rubrica de autoavaliação**

- 1 — Contrasta corretamente atribuição e cópia rasa.
- 1 — Explica memo de deepcopy e identidade de alias preservada.
- 1 — Propõe testes de identidade/mutação e declara limites de cópia.

Máximo: 3

</details>

**Pré-requisitos**

- [Identidade, igualdade e vinculação](../../technical-interview-preparation/09-object-identity-references-and-copying/README.pt-BR.md)

### sql.zero-child-count

`mid` · `databases-sql`

Dadas groups(id, name) e tasks(id, group_id, done), retorne contagem de tarefas concluídas por grupo, incluindo grupos sem concluídas. Como ON, WHERE e COUNT afetam correção? Considere ambas as colunas id chaves primárias, tasks.group_id referenciando groups.id e done igual a 0 ou 1. Explique por que agrupar apenas por nome é insuficiente.

<details>
<summary>Resposta esperada</summary>

Faça LEFT JOIN tasks pelo ID do grupo com done = 1 em ON; agrupe por ID e nome, conte tasks.id (não nulo para tarefas reais). WHERE tasks.done = 1 descartaria linhas estendidas com NULL; COUNT(*) contaria linha sem correspondência.

**Explicação:** Agrupe por identidade estável mesmo com nomes repetidos. Filtro em ON controla correspondências sem excluir grupos esquerdos.

**Intenção do entrevistador:** Avaliar semântica de joins, granularidade e casos zero.

**Erros comuns**

- Usar INNER JOIN ou filtrar concluídas em WHERE.
- Agrupar apenas por nome não único ou contar todas linhas.

**Perguntas complementares**

- O que acontece se dois grupos têm mesmo nome?

**Exemplo**

```sql
SELECT g.id, g.name, COUNT(t.id)
FROM groups AS g LEFT JOIN tasks AS t
ON g.id = t.group_id AND t.done = 1
GROUP BY g.id, g.name
ORDER BY g.id;
```

**Rubrica de autoavaliação**

- 1 — Usa LEFT JOIN por chaves e filtro de concluídas em ON.
- 1 — Conta ID não nulo do filho e explica contagem zero.
- 1 — Agrupa por identidade estável e explica por que só nome falha.

Máximo: 3

</details>

**Pré-requisitos**

- [Relacionamentos e cardinalidade de joins](../../technical-interview-preparation/19-joins-aggregations-and-data-relationships/README.pt-BR.md)

### internals.gil-workload

`senior` · `python-internals`

Serviço CPython 3.13 executa muitas operações I/O bloqueantes, transformações pesadas em Python puro e incrementa contador compartilhado. Proponha escolhas de concorrência e plano de verificação; considere builds convencional e experimental free-threaded.

<details>
<summary>Resposta esperada</summary>

CPython convencional com GIL permite uma thread executar bytecode Python por vez num interpretador. Threads servem a I/O bloqueante; asyncio a I/O cooperativo com APIs compatíveis; processos podem beneficiar Python CPU-bound ao custo de serialização/memória. Build experimental free-threaded pode permitir threads Python paralelas; algumas extensões podem reativar GIL. Sincronize contador com lock compartilhado e meça throughput, custos de recursos e correção no build real.

**Explicação:** GIL depende da implementação e não garante ausência de races na aplicação. Total correto isolado sem sincronização é evidência fraca; teste contrato do lock e propagação de falhas separadamente de desempenho.

**Intenção do entrevistador:** Avaliar raciocínio arquitetural condicional, consciência de versão e validação de invariantes.

**Erros comuns**

- Afirmar threads nunca ajudam ou GIL torna atualizações seguras.
- Supor free-threading padrão ou ganho garantido.

**Perguntas complementares**

- Por que total correto em uma execução sem sincronização não prova segurança?

**Exemplo**

Compare baseline sequencial, threads limitadas para I/O bloqueante e processos para CPU; registre tempo e memória separadamente de teste de correção do contador com lock.

**Rubrica de autoavaliação**

- 1 — Distingue GIL convencional de free-threading experimental com ressalva de extensões.
- 1 — Escolhe estratégias I/O/CPU com trade-off e propõe medição na carga real.
- 1 — Protege invariante compartilhado e distingue testes de correção de benchmarks.

Máximo: 3

</details>

**Pré-requisitos**

- [GIL em Python 3.13](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.pt-BR.md)
- [Concorrência e paralelismo](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.pt-BR.md)
- [Exemplo de estado compartilhado](../../technical-interview-preparation/14-concurrency-parallelism-and-the-gil/README.pt-BR.md)

### api.object-authorization

`senior` · `backend-apis`

Aluno autenticado pode solicitar nota por ID. Projete verificações de acesso e política de resposta para impedir leitura de nota alheia; explique vazamento de existência e testes de regressão.

<details>
<summary>Resposta esperada</summary>

Autentique por identidade confiável verificada, depois autorize ação no objeto específico por propriedade ou política controlada pelo servidor antes de retornar conteúdo. Ausência de credenciais válidas resulta 401 com desafio. Acesso proibido pode resultar 403, ou 404 sob política consistente de ocultação. Não confie em proprietário fornecido ou token não verificado. Teste ausência de credenciais, proprietário autorizado, não proprietário autenticado, ID inexistente e corpo de negação sem dados protegidos.

**Explicação:** 403 versus 404 pode revelar existência. Ocultação exige política consistente; não substitui autorização. Exemplo local modela fronteira pós-autenticação, não verificação de tokens.

**Intenção do entrevistador:** Avaliar controle de acesso em nível de objeto, contrato de erro e testes negativos de segurança.

**Erros comuns**

- Verificar apenas se chamador está logado.
- Retornar conteúdo com negação ou confiar no proprietário informado pelo cliente.

**Perguntas complementares**

- Como mudaria testes se política oculta existência intencionalmente?

**Exemplo**

Para nota 7 de aluno A, B autenticado recebe 403 (ou 404 definido pela política) sem conteúdo; A recebe 200; anônimos recebem 401.

**Rubrica de autoavaliação**

- 1 — Exige identidade verificada no servidor mais autorização por objeto.
- 1 — Explica 401/403/404 e política consistente de divulgação de existência.
- 1 — Especifica testes positivos e negativos incluindo confidencialidade do corpo negado.

Máximo: 3

</details>

**Pré-requisitos**

- [Autenticação versus autorização](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.pt-BR.md)

### engineering.architecture-tradeoffs

`senior` · `software-engineering`

Serviço pequeno de relatórios tem requisições lentas. Colega propõe dividir em serviços e adicionar cache. Como decidiria, mediria e implantaria mudanças com segurança?

<details>
<summary>Resposta esperada</summary>

Defina metas de latência/confiabilidade e meça baseline com logs, métricas e traces para localizar gargalo. Compare monólito modular e serviços por escala/deploy independentes e custo de rede/operação. Considere cache só com restrições explícitas de defasagem, invalidação e memória. Registre alternativas e consequências em ADR, teste critérios de aceite, use mudanças focadas revisadas e planeje implantação medida e rollback, incluindo compatibilidade de dados.

**Explicação:** Rótulos de arquitetura não estabelecem desempenho. Evidências e restrições de qualidade determinam se complexidade adicional se justifica.

**Intenção do entrevistador:** Avaliar julgamento técnico, decisões mensuráveis e risco operacional.

**Erros comuns**

- Supor microsserviços ou caches melhorarem latência automaticamente.
- Ignorar defasagem do cache ou supor rollback de código desfaz migrações.

**Perguntas complementares**

- Que evidência justificaria manter design atual?

**Exemplo**

Se medição localiza leituras caras repetidas e contrato permite defasagem limitada, avalie cache pequeno contra baseline; rejeite se invalidação ou custo de memória exceder orçamento acordado.

**Rubrica de autoavaliação**

- 1 — Define baseline mensurável e investiga gargalo antes de escolher.
- 1 — Compara trade-offs de serviços e cache frente a restrições.
- 1 — Propõe decisão documentada, testes de aceite e rollback incluindo dados.

Máximo: 3

</details>

**Pré-requisitos**

- [Trade-offs e operação](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.pt-BR.md)
- [Decisões começam no requisito](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.pt-BR.md)

<!-- interview-questions:end -->

<!-- chapter-navigation:bottom -->
[← Anterior](../21-software-engineering-and-technical-decisions/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
