# Banco de perguntas de entrevistas técnicas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../21-software-engineering-and-technical-decisions/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../23-behavioral-and-international-interviews/README.pt-BR.md)
<!-- /chapter-navigation:top -->

60 perguntas de entrevista: 24 Junior, 24 Mid-level e 12 Senior, incluindo nove perguntas piloto originais e três comportamentais/internacionais. Navegue por tema e nível; IDs permanecem estáveis ao reordenar. Nível indica profundidade esperada, não padrão universal de contratação. Estude primeiro a seção de pré-requisito, responda em voz alta sem abrir referência e depois abra resposta. Atribua a cada critério seus pontos somente se sua resposta o demonstrar; senão zero. Use pontuação para identificar lacunas, não como certificação ou avaliação semântica automática. Perguntas complementares são prática opcional, sem pontuação separada. Registros JSON canônicos e índice em [interviews](../../interviews/README.pt-BR.md); esta seção é gerada a partir deles. Estude [entrevistas comportamentais e internacionais](../23-behavioral-and-international-interviews/README.pt-BR.md) antes dessas perguntas e depois tente os [simulados cronometrados](../24-mock-interviews-and-self-assessment/README.pt-BR.md).

<!-- interview-questions:start -->
## Distribuição

| Tema | Junior | Mid-level | Senior | Total |
| --- | ---: | ---: | ---: | ---: |
| Fundamentos de entrevistas | 3 | 2 | 1 | 6 |
| Fundamentos de Python | 4 | 3 | 1 | 8 |
| Estruturas de dados e algoritmos | 3 | 3 | 1 | 7 |
| Programação orientada a objetos | 3 | 3 | 2 | 8 |
| Internals de Python | 2 | 4 | 2 | 8 |
| Testes e debugging | 3 | 3 | 1 | 7 |
| Backend e APIs | 2 | 2 | 1 | 5 |
| Bancos de dados e SQL | 2 | 2 | 1 | 5 |
| Engenharia de software | 1 | 1 | 1 | 3 |
| Entrevistas comportamentais e internacionais | 1 | 1 | 1 | 3 |

## Fundamentos de entrevistas

### interview.allowed-tools

`junior` · `interview-fundamentals`

Antes de um take-home, o que confirmar sobre escopo, entrega e ferramentas de IA? E se IA for proibida?

<details>
<summary>Resposta esperada</summary>

Confirme prazo, escopo, formato, critérios e ferramentas permitidas. Se IA for proibida, não use; se permitida, declare conforme exigido.

**Explicação:** Regras variam entre empresas; pergunte em vez de inferir.

**Intenção do entrevistador:** Avaliar respeito às regras da avaliação.

**Erros comuns**

- Supor que vale a política de ferramentas da empresa anterior.

**Perguntas complementares**

- O que perguntaria se a documentação permitida não estiver clara?

**Exemplo**

Se as instruções permitem documentação da biblioteca padrão mas proíbem IA, consulte apenas a documentação.

**Rubrica de autoavaliação**

- 1 — Identifica prazo, escopo, formato, critérios e política de ferramentas.
- 1 — Respeita proibição ou obrigação de declarar uso.

Máximo: 2

</details>

**Pré-requisitos**

- [Finalidade e processo](../../technical-interview-preparation/01-understanding-technical-interviews/README.pt-BR.md)
- [Tarefas take-home](../../technical-interview-preparation/02-live-coding-and-take-home/README.pt-BR.md)

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

### interview.live-coding-start

`junior` · `interview-fundamentals`

Como iniciar tarefa cronometrada antes de digitar solução? Descreva uma simulação pequena e como se comunica.

<details>
<summary>Resposta esperada</summary>

Leia e reformule o contrato, simule um exemplo pequeno, escolha abordagem direta, implemente e teste explicando decisões.

**Explicação:** Uma simulação expõe hipóteses antes da implementação; narre decisões, não teclas.

**Intenção do entrevistador:** Avaliar processo sob pressão de tempo.

**Erros comuns**

- Digitar solução otimizada antes de conferir contrato.

**Perguntas complementares**

- E se a simulação contrariar o contrato declarado?

**Exemplo**

Para soma de quantidades não negativas, simule [2, 0, 3] até 5 após confirmar que zero é permitido.

**Rubrica de autoavaliação**

- 1 — Reformula contrato e simula exemplo concreto.
- 1 — Escolhe abordagem simples e explica decisões de implementação/teste em voz alta.

Máximo: 2

</details>

**Pré-requisitos**

- [Live coding](../../technical-interview-preparation/02-live-coding-and-take-home/README.pt-BR.md)

### interview.incomplete-live-task

`mid` · `interview-fundamentals`

O tempo está acabando; solução atende entradas típicas mas falha num caso de borda. Como informar status e priorizar trabalho restante?

<details>
<summary>Resposta esperada</summary>

Informe qual comportamento foi verificado e qual falha; isole caso mínimo, tente correção pequena verificável se houver tempo e explique próximo teste e limitação.

**Explicação:** Resultado parcial preciso é evidência melhor que alegação de conclusão sem suporte.

**Intenção do entrevistador:** Avaliar priorização e evidência honesta.

**Erros comuns**

- Dizer que todos os testes passam porque fluxo principal funciona.

**Perguntas complementares**

- Como comunicaria uma correção que falhou?

**Exemplo**

Função passa [2,3] mas falha em []; informe a falha e teste o resultado acordado para vazio.

**Rubrica de autoavaliação**

- 1 — Distingue comportamento verificado, falha e trabalho não verificado.
- 1 — Propõe caso mínimo reproduzível e próximo passo de verificação.

Máximo: 2

</details>

**Pré-requisitos**

- [Live coding](../../technical-interview-preparation/02-live-coding-and-take-home/README.pt-BR.md)

### interview.take-home-evidence

`mid` · `interview-fundamentals`

Para take-home pequeno, o que README de entrega e testes devem demonstrar? Explique como evitar alegações sem suporte.

<details>
<summary>Resposta esperada</summary>

Documente requisitos, hipóteses, comandos de setup/execução, testes realmente executados e limitações. Inclua entradas normal, vazia e inválida segundo contrato e explique complexidade.

**Explicação:** Revisor deve conseguir reproduzir evidências sem segredos ou código proprietário.

**Intenção do entrevistador:** Avaliar reprodutibilidade e disciplina de entrega.

**Erros comuns**

- Adicionar funcionalidades especulativas e deixar setup sem documentação.

**Perguntas complementares**

- O que registraria se teste de integração não puder rodar localmente?

**Exemplo**

Para soma de inteiros não negativos, registre política do zero, teste de entrada inválida e comando real de teste.

**Rubrica de autoavaliação**

- 1 — Inclui instruções reproduzíveis, hipóteses explícitas e evidência real de teste.
- 1 — Descreve bordas, complexidade e limitações sem alegações falsas.

Máximo: 2

</details>

**Pré-requisitos**

- [Tarefas take-home](../../technical-interview-preparation/02-live-coding-and-take-home/README.pt-BR.md)

### interview.scope-prioritization

`senior` · `interview-fundamentals`

Take-home pede serviço pequeno funcional em duas horas; opcionais são ambíguos. Como acordar prioridades, escolher entrega e comunicar risco?

<details>
<summary>Resposta esperada</summary>

Confirme critérios de aceite, prazo e ferramentas; separe obrigatório de opcional. Entregue implementação pequena testada com hipóteses, evidências e riscos adiados explícitos em vez de ampliar escopo.

**Explicação:** Entrega restrita troca abrangência por comportamento verificado; entrevistador deve saber o que não foi implementado.

**Intenção do entrevistador:** Avaliar julgamento sobre escopo e evidências.

**Erros comuns**

- Prometer arquitetura completa sem validar comportamento central.

**Perguntas complementares**

- Como responderia a requisito novo no meio do tempo?

**Exemplo**

Priorize cálculo validado e instruções de execução em vez de UI não solicitada; adie UI explicitamente.

**Rubrica de autoavaliação**

- 1 — Prioriza critérios de aceite explícitos e acorda hipóteses com avaliador.
- 1 — Justifica trade-off de escopo e comunica resultados testados e riscos adiados.

Máximo: 2

</details>

**Pré-requisitos**

- [Finalidade e processo](../../technical-interview-preparation/01-understanding-technical-interviews/README.pt-BR.md)
- [Tarefas take-home](../../technical-interview-preparation/02-live-coding-and-take-home/README.pt-BR.md)

## Fundamentos de Python

### python.binding-vs-copy

`junior` · `python-fundamentals`

Dado a = [1]; b = a; b.append(2), quais são a e b? Explique se atribuição copia lista.

<details>
<summary>Resposta esperada</summary>

Ambos são [1, 2]; a e b nomeiam a mesma lista mutável. Atribuição vincula nome e não copia objeto.

**Explicação:** Mutar por uma referência é visível pela outra.

**Intenção do entrevistador:** Avaliar aliases e mutação de listas.

**Erros comuns**

- Tratar b = a como lista independente.

**Perguntas complementares**

- O que muda se depois b for vinculado a []?

**Exemplo**

Após `a = [1]; b = a`, a expressão `a is b` resulta em `True` antes de reatribuir `b`.

**Rubrica de autoavaliação**

- 1 — Prevê valores das duas listas.
- 1 — Explica identidade compartilhada e mutação, não cópia.

Máximo: 2

</details>

**Pré-requisitos**

- [Revisão pelo raciocínio](../../technical-interview-preparation/03-python-fundamentals-review/README.pt-BR.md)
- [Identidade, igualdade e vinculação](../../technical-interview-preparation/09-object-identity-references-and-copying/README.pt-BR.md)

### python.conversion-contract

`junior` · `python-fundamentals`

O que acontece com int("12") e int("twelve")? Explique por que tipo e conteúdo importam.

<details>
<summary>Resposta esperada</summary>

O primeiro retorna inteiro 12; o segundo gera ValueError porque texto não representa inteiro aceito por int.

**Explicação:** Conversão tem contrato de entrada, não garantia de sucesso para toda string.

**Intenção do entrevistador:** Avaliar conversão de tipos e raciocínio sobre falha.

**Erros comuns**

- Supor que conversão inválida retorna zero ou None.

**Perguntas complementares**

- O que testaria para string vazia?

**Exemplo**

int("0") retorna 0; int("") gera ValueError.

**Rubrica de autoavaliação**

- 1 — Prevê valor e tipo da conversão bem-sucedida.
- 1 — Identifica ValueError e explica restrição de entrada.

Máximo: 2

</details>

**Pré-requisitos**

- [Revisão pelo raciocínio](../../technical-interview-preparation/03-python-fundamentals-review/README.pt-BR.md)

### python.immutable-string

`junior` · `python-fundamentals`

Dado s = "python"; s.upper(); print(s), o que é exibido? Como guardar o valor em maiúsculas?

<details>
<summary>Resposta esperada</summary>

Exibe python. Strings são imutáveis; upper retorna string resultante. Use s = s.upper() para vincular s ao resultado maiúsculo.

**Explicação:** Chamar método não implica mutação; confira contrato.

**Intenção do entrevistador:** Avaliar valores de retorno e imutabilidade.

**Erros comuns**

- Esperar que upper modifique string original no lugar.

**Perguntas complementares**

- O que permanece vinculado a um alias da string original?

**Exemplo**

s = "hi"; t = s.upper() deixa s igual a "hi" e t igual a "HI".

**Rubrica de autoavaliação**

- 1 — Prevê saída original e explica imutabilidade.
- 1 — Mostra atribuição do resultado retornado.

Máximo: 2

</details>

**Pré-requisitos**

- [Revisão pelo raciocínio](../../technical-interview-preparation/03-python-fundamentals-review/README.pt-BR.md)

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

### python.identity-none

`mid` · `python-fundamentals`

Compare x == y e x is y para duas listas [1] criadas independentemente. Por que is None é adequado mas is não é confiável para comparar valor de strings?

<details>
<summary>Resposta esperada</summary>

Igualdade é True e identidade False. == compara semântica de igualdade; is compara identidade. None é singleton, então identidade é teste pretendido; cache de strings não é contrato de igualdade por valor.

**Explicação:** Dois objetos distintos podem ser iguais. Identidade de valores em cache depende da implementação.

**Intenção do entrevistador:** Avaliar identidade versus igualdade.

**Erros comuns**

- Usar is para comparar valores inteiros ou strings.

**Perguntas complementares**

- O que ocorre quando y recebe x?

**Exemplo**

Dado `x = [1]; y = [1]`, a expressão `x == y` resulta em `True`, enquanto `x is y` resulta em `False`.

**Rubrica de autoavaliação**

- 1 — Prevê identidade e igualdade para listas separadas.
- 1 — Explica singleton None e regra de comparação de valor.

Máximo: 2

</details>

**Pré-requisitos**

- [Prática independente](../../technical-interview-preparation/03-python-fundamentals-review/README.pt-BR.md)
- [Identidade, igualdade e vinculação](../../technical-interview-preparation/09-object-identity-references-and-copying/README.pt-BR.md)

### python.parameter-rebinding

`mid` · `python-fundamentals`

Função recebe items=[1] de chamador, depois atribui items = [9] localmente. Compare com items.append(9). O que chamador vê?

<details>
<summary>Resposta esperada</summary>

Reatribuir parâmetro local não muda lista nem vinculação do chamador; ele ainda vê [1]. Fazer append na lista compartilhada muda para [1, 9].

**Explicação:** Parâmetros são nomes locais vinculados aos objetos fornecidos; distinga vinculação de mudança do objeto.

**Intenção do entrevistador:** Avaliar fronteira de função e ownership.

**Erros comuns**

- Descrever argumentos Python simplesmente como valores copiados ou referências à variável do chamador.

**Perguntas complementares**

- Como retornaria lista nova preservando original?

**Exemplo**

def f(items): items = [9] deixa lista original inalterada.

**Rubrica de autoavaliação**

- 1 — Prevê resultado de reatribuição local.
- 1 — Prevê mutação compartilhada e explica diferença.

Máximo: 2

</details>

**Pré-requisitos**

- [Revisão pelo raciocínio](../../technical-interview-preparation/03-python-fundamentals-review/README.pt-BR.md)
- [Identidade, igualdade e vinculação](../../technical-interview-preparation/09-object-identity-references-and-copying/README.pt-BR.md)

### python.scope-lookup

`mid` · `python-fundamentals`

Explique busca LEGB e o que nonlocal muda quando função interna atualiza contador envolvente. Compare com reatribuir variável local independente.

<details>
<summary>Resposta esperada</summary>

LEGB busca local, funções envolventes, global do módulo e builtins para nome não qualificado comum. nonlocal permite reatribuir vinculação existente em função envolvente; atribuição local comum não atualiza essa vinculação.

**Explicação:** Closure pode manter estado envolvente entre chamadas. nonlocal não é declaração global.

**Intenção do entrevistador:** Avaliar escopo e semântica de vinculação.

**Erros comuns**

- Usar global quando contador pertence à função envolvente.

**Perguntas complementares**

- Por que duas chamadas de fábrica podem ter contadores separados?

**Exemplo**

Incremento interno com nonlocal count atualiza count mantido por sua própria chamada externa.

**Rubrica de autoavaliação**

- 1 — Nomeia quatro escopos LEGB em ordem.
- 1 — Explica vinculação envolvente existente e contrasta reatribuição local.

Máximo: 2

</details>

**Pré-requisitos**

- [Revisão pelo raciocínio](../../technical-interview-preparation/03-python-fundamentals-review/README.pt-BR.md)
- [Closures e escopo](../../technical-interview-preparation/12-closures-and-decorators/README.pt-BR.md)

### python.hash-equality-contract

`senior` · `python-fundamentals`

Você projeta classe de igualdade por valor para chaves de dicionário. Qual contrato hash/igualdade deve valer, qual risco se estado relevante mudar e como testaria?

<details>
<summary>Resposta esperada</summary>

Objetos iguais devem ter hashes iguais e hashes devem permanecer estáveis durante vida como objetos hashable; diferentes podem colidir. Prefira estado de igualdade imutável estável para chaves ou torne objetos mutáveis de igualdade por valor não hashable. Teste instâncias distintas iguais, busca por chave igual e política de mutação suportada.

**Explicação:** Mudar hash de chave pode invalidar busca; definir __eq__ sem __hash__ normalmente torna classe Python não hashable.

**Intenção do entrevistador:** Avaliar design de invariantes e testes, não unicidade de hash.

**Erros comuns**

- Exigir hashes diferentes para todo par desigual.

**Perguntas complementares**

- Por que tupla contendo lista não é chave utilizável?

**Exemplo**

Dois objetos-chave imutáveis distintos e iguais devem recuperar mesmo valor associado; teste sem supor hashes distintos para desiguais.

**Rubrica de autoavaliação**

- 1 — Declara regras de hash igual e estabilidade durante vida, permitindo colisões.
- 1 — Explica risco de chave mutável e propõe testes de igualdade, busca e política de mutação.

Máximo: 2

</details>

**Pré-requisitos**

- [Igualdade e hashing](../../technical-interview-preparation/09-object-identity-references-and-copying/README.pt-BR.md)

## Estruturas de dados e algoritmos

### algorithms.binary-precondition

`junior` · `data-structures-algorithms`

Por que busca binária é inadequada para lista desordenada arbitrária? Compare com linear e declare custo em acesso aleatório ordenado.

<details>
<summary>Resposta esperada</summary>

Busca binária elimina metade das posições usando ordem crescente. Sem ordem, pode descartar alvo. Busca linear funciona sem ordenação em O(n) no pior caso; binária em entrada ordenada com acesso aleatório usa O(log n) comparações.

**Explicação:** Invariante de dados ordenados justifica eliminação.

**Intenção do entrevistador:** Avaliar pré-condições de algoritmos.

**Erros comuns**

- Supor busca binária válida em qualquer lista.

**Perguntas complementares**

- Validar ordenação a cada busca preservaria custo total logarítmico?

**Exemplo**

Em [9,1,3], comparar com valor central não permite eliminar lado esquerdo com segurança ao buscar 9.

**Rubrica de autoavaliação**

- 1 — Declara ordenação e explica eliminação segura.
- 1 — Compara custos no pior caso linear e binário sob hipóteses declaradas.

Máximo: 2

</details>

**Pré-requisitos**

- [Escolha pelo contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.pt-BR.md)
- [2. Busca binária](../../problem-solving-and-live-coding/05-searching-algorithms/README.pt-BR.md)

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

### algorithms.frequency-map

`junior` · `data-structures-algorithms`

Como contaria ocorrências de cada rótulo hashable numa lista? Mostre resultado para [a,a,b] e explique escolha da estrutura.

<details>
<summary>Resposta esperada</summary>

Use dicionário de rótulo para contagem, atualizando com get(label, 0) + 1. Resultado {"a": 2, "b": 1}.

**Explicação:** Conjunto perde multiplicidade; mapeamento preserva contador por chave.

**Intenção do entrevistador:** Avaliar escolha de coleção e acumulação.

**Erros comuns**

- Usar conjunto esperando manter contagens.

**Perguntas complementares**

- O que entrada vazia deve retornar?

**Exemplo**

Para ["b","b","b"], mapeamento é {"b":3}.

**Rubrica de autoavaliação**

- 1 — Escolhe dicionário e descreve incremento por chave.
- 1 — Prevê ambas contagens e explica insuficiência do conjunto.

Máximo: 2

</details>

**Pré-requisitos**

- [Escolha pelo contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.pt-BR.md)
- [1. Acumulador e mapa de frequências](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)

### algorithms.recursion-stack

`mid` · `data-structures-algorithms`

Para somar inteiros de 0 a n com n não negativo, dê caso base e recorrência. Compare tempo/espaço auxiliar recursivo e iterativo sob aritmética de custo fixo.

<details>
<summary>Resposta esperada</summary>

S(0)=0; S(n)=n+S(n-1). Ambas varreduras usam O(n) tempo; recursiva usa O(n) pilha e acumulador O(1) espaço extra.

**Explicação:** Progresso ao caso base importa; limite de recursão Python restringe profundidade prática.

**Intenção do entrevistador:** Avaliar término e análise de recursos.

**Erros comuns**

- Ignorar frames da pilha ao informar espaço auxiliar.

**Perguntas complementares**

- Por que rejeitar negativos antes de recursar?

**Exemplo**

S(3) = 3 + 2 + 1 + 0 = 6.

**Rubrica de autoavaliação**

- 1 — Fornece base, recorrência e progresso ao zero.
- 1 — Informa tempo e espaço de pilha/acumulador corretamente.

Máximo: 2

</details>

**Pré-requisitos**

- [Escolha pelo contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.pt-BR.md)
- [2. Implementação Python](../../problem-solving-and-live-coding/04-recursion/README.pt-BR.md)

### algorithms.stable-insertion

`mid` · `data-structures-algorithms`

Defina estabilidade ao ordenar registros por nota. Como insertion sort a preserva e qual tempo no pior caso? Ilustre com registros de notas iguais.

<details>
<summary>Resposta esperada</summary>

Registros de chaves iguais mantêm ordem relativa original. No insertion sort desloque só chaves estritamente maiores e insira após iguais no prefixo ordenado. Pior tempo O(n²).

**Explicação:** Deslocar iguais pode inverter ordem mesmo com notas ordenadas corretamente.

**Intenção do entrevistador:** Avaliar estabilidade além de saída ordenada.

**Erros comuns**

- Verificar só notas numéricas e ignorar identidade do registro.

**Perguntas complementares**

- Que entrada revelaria implementação instável?

**Exemplo**

[(A,2),(B,1),(C,2)] vira [(B,1),(A,2),(C,2)] com ordenação estável por nota.

**Rubrica de autoavaliação**

- 1 — Define estabilidade e regra de deslocamento estritamente maior.
- 1 — Declara O(n²) no pior caso e ilustra ordem de chaves iguais.

Máximo: 2

</details>

**Pré-requisitos**

- [Escolha pelo contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.pt-BR.md)
- [4. Insertion sort](../../problem-solving-and-live-coding/06-sorting-algorithms/README.pt-BR.md)

### algorithms.two-pointer-pair

`mid` · `data-structures-algorithms`

Para inteiros ordenados crescentes, decida se dois índices distintos somam alvo. Explique movimentos, término e custos.

<details>
<summary>Resposta esperada</summary>

Comece left=0, right=n-1. Enquanto left < right compare soma: igual tem sucesso, menor incrementa left, maior decrementa right. Se se encontrarem, falha. Ordenação justifica pares descartados. O(n) tempo, O(1) extra sob aritmética de custo fixo.

**Explicação:** Cada movimento reduz intervalo e nunca usa mesmo índice duas vezes.

**Intenção do entrevistador:** Avaliar invariante, correção e complexidade.

**Erros comuns**

- Usar left <= right permitindo contar elemento único duas vezes.

**Perguntas complementares**

- Por que [3,3] funciona para alvo 6 mas [3] não?

**Exemplo**

[1,3,4,7] com alvo 7 tem sucesso pelos índices 1 e 2.

**Rubrica de autoavaliação**

- 1 — Descreve movimentos, justificativa da ordem e separação estrita de índices.
- 1 — Declara tempo linear e espaço extra constante com término.

Máximo: 2

</details>

**Pré-requisitos**

- [Escolha pelo contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.pt-BR.md)
- [2. Dois ponteiros](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)

### algorithms.window-tradeoff

`senior` · `data-structures-algorithms`

Encontre soma máxima de k inteiros consecutivos, inclusive entrada toda negativa. Compare recalcular cada janela com soma móvel, declare hipóteses e proponha testes de borda.

<details>
<summary>Resposta esperada</summary>

Exija 1 <= k <= n. Some primeiros k, inicialize best com essa soma, depois subtraia saída e adicione entrada. Recalcular custa O((n-k+1)k); móvel custa O(n) tempo e O(1) extra para acesso aleatório sob aritmética de custo fixo. Teste k=1, k=n, negativos e k inválido.

**Explicação:** Atualização móvel reaproveita trabalho; iniciar best em zero admite janela inexistente para negativos.

**Intenção do entrevistador:** Avaliar otimização ligada a contrato preciso e oráculo de teste.

**Erros comuns**

- Alegar O(nk) inevitável ou iniciar best em zero.

**Perguntas complementares**

- Que resultado [-4,-2,-5] com k=2 deve produzir?

**Exemplo**

[-4,-2,-5], k=2 dá max(-6,-7) = -6.

**Rubrica de autoavaliação**

- 1 — Define k válido, invariante móvel e inicialização correta.
- 1 — Compara custos com hipóteses e propõe testes de borda/negativos.

Máximo: 2

</details>

**Pré-requisitos**

- [Escolha pelo contrato](../../technical-interview-preparation/04-data-structures-and-algorithms-review/README.pt-BR.md)
- [3. Janela deslizante fixa](../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)

## Programação orientada a objetos

### oop.class-list-sharing

`junior` · `oop`

Classe define members=[] no nível de classe. Por que instâncias podem compartilhar adições inesperadamente? Mostre como tornar listas independentes.

<details>
<summary>Resposta esperada</summary>

Atributo mutável de classe é compartilhado salvo se sombreado por atributo de instância. Inicialize self.members=[] em __init__ para criar lista distinta por instância.

**Explicação:** Append muta objeto compartilhado, enquanto atribuir atributo de instância muda busca dessa instância.

**Intenção do entrevistador:** Avaliar atributos mutáveis de classe.

**Erros comuns**

- Manter lista na classe e supor self cria cópia.

**Perguntas complementares**

- Que atributo de classe poderia ser compartilhado?

**Exemplo**

Dois grupos novos devem ter listas vazias separadas; adicionar membro a um deixa outro vazio.

**Rubrica de autoavaliação**

- 1 — Explica atributo mutável compartilhado e mutação.
- 1 — Inicializa lista independente e prevê isolamento.

Máximo: 2

</details>

**Pré-requisitos**

- [Atributos e vinculação](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.pt-BR.md)

### oop.independent-state

`junior` · `oop`

Duas instâncias Counter inicializam self.value=0. Só first.increment() executa. Quais valores e por quê?

<details>
<summary>Resposta esperada</summary>

Primeira 1 e segunda 0; cada instância possui seu atributo e método vinculado recebe instância em self.

**Explicação:** Classe define comportamento; objetos podem manter estado independente.

**Intenção do entrevistador:** Avaliar estado de instância e vinculação de método.

**Erros comuns**

- Tratar todas instâncias como compartilhando self.value.

**Perguntas complementares**

- Como testaria instâncias independentes?

**Exemplo**

first.increment(); assert second.value == 0.

**Rubrica de autoavaliação**

- 1 — Prevê ambos valores.
- 1 — Explica estado por instância e vinculação de self.

Máximo: 2

</details>

**Pré-requisitos**

- [O que é e por quê](../../technical-interview-preparation/05-classes-and-objects/README.pt-BR.md)

### oop.initialization

`junior` · `oop`

Para que serve __init__ e como difere de __new__? O que __init__ pode retornar?

<details>
<summary>Resposta esperada</summary>

__new__ é hook de criação; __init__ inicializa instância já criada. __init__ deve retornar None, normalmente implicitamente.

**Explicação:** Chamada normal da classe coordena criação e inicialização.

**Intenção do entrevistador:** Avaliar fundamentos do ciclo de vida de objetos.

**Erros comuns**

- Retornar self de __init__ ou chamá-lo de hook de alocação.

**Perguntas complementares**

- Onde inicializaria lista por instância?

**Exemplo**

def __init__(self): self.value = 0 inicializa estado sem retornar valor.

**Rubrica de autoavaliação**

- 1 — Distingue criação de inicialização.
- 1 — Declara contrato de retorno None.

Máximo: 2

</details>

**Pré-requisitos**

- [O que é e por quê](../../technical-interview-preparation/05-classes-and-objects/README.pt-BR.md)

### oop.constructor-binding

`mid` · `oop`

Compare métodos de instância, classe e estático. Por que construtor alternativo herdado deve usar cls(...) em vez de nome da classe base? Declare hipótese de compatibilidade do construtor da subclasse.

<details>
<summary>Resposta esperada</summary>

Métodos de instância recebem self; de classe recebem cls; estáticos não recebem nenhum implicitamente. Usar cls(...) permite subclasse compatível construir instância própria em vez de forçar tipo base.

**Explicação:** Vinculação determina argumento implícito, não ausência de efeitos colaterais.

**Intenção do entrevistador:** Avaliar escolha de método e extensibilidade de subclasse.

**Erros comuns**

- Supor método estático automaticamente puro.

**Perguntas complementares**

- E se subclasse exigir argumentos adicionais?

**Exemplo**

SubGroup.from_label("A") compatível deve retornar SubGroup se fábrica usa cls.

**Rubrica de autoavaliação**

- 1 — Identifica vinculação implícita nos três tipos.
- 1 — Explica construção com cls e restrição de compatibilidade.

Máximo: 2

</details>

**Pré-requisitos**

- [Atributos e vinculação](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.pt-BR.md)

### oop.length-and-repr

`mid` · `oop`

StudyGroup precisa de len(group), str(group) amigável e repr(group) para debugging. Quais métodos implementam e o que comprimento deve retornar?

<details>
<summary>Resposta esperada</summary>

Implemente __len__, __str__, __repr__. __len__ retorna inteiro não negativo representando tamanho; __str__ é para usuário, __repr__ ajuda debugging e não precisa ser Python executável.

**Explicação:** Use protocolos documentados em vez de inventar nomes dunder.

**Intenção do entrevistador:** Avaliar integração com protocolos Python.

**Erros comuns**

- Retornar contagem negativa ou supor que repr precisa reconstruir objeto.

**Perguntas complementares**

- O que len retornaria para grupo vazio?

**Exemplo**

__len__ pode retornar len(self.members); grupo vazio tem comprimento zero.

**Rubrica de autoavaliação**

- 1 — Mapeia três operações aos métodos corretos.
- 1 — Explica comprimento inteiro não negativo e finalidades das strings.

Máximo: 2

</details>

**Pré-requisitos**

- [Métodos especiais](../../technical-interview-preparation/06-attributes-methods-and-object-behavior/README.pt-BR.md)

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

### oop.invariant-boundary

`senior` · `oop`

Projete retirada de estoque para quantidade nunca ficar negativa pelo contrato público. Explique ordem de validação, leitura e testes; underscore é fronteira de segurança?

<details>
<summary>Resposta esperada</summary>

Exponha remove com validação antes de mutação; rejeite quantidade fora do domínio documentado ou acima do estoque sem alterar saldo. Exponha property de leitura se útil. Teste retirada válida, estoque insuficiente e estado intacto na falha. Underscore é convenção; name mangling/property não é segurança.

**Explicação:** Encapsulamento protege invariantes nas operações suportadas; não impõe controle de acesso contra chamadores arbitrários.

**Intenção do entrevistador:** Avaliar design de invariante de domínio e testes negativos.

**Erros comuns**

- Subtrair primeiro e levantar exceção deixando estado corrompido.

**Perguntas complementares**

- Como demonstraria que validação falha não tem efeitos?

**Exemplo**

Com quantidade 5, rejeitar retirada de 6 deve manter quantidade 5.

**Rubrica de autoavaliação**

- 1 — Projeta validação antes da mutação e contrato de leitura explícito.
- 1 — Propõe testes de estado intacto e distingue convenção de segurança.

Máximo: 2

</details>

**Pré-requisitos**

- [Encapsulamento e abstração](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.pt-BR.md)

### oop.solid-contracts

`senior` · `oop`

Política de saldo depende de leitor de banco concreto com métodos de escrita alheios. Redesenhe dependência usando DIP e ISP, com teste fake e trade-off.

<details>
<summary>Resposta esperada</summary>

Dependa de contrato pequeno available, opcionalmente ABC com método abstrato, e injete leitor que o implemente. DIP separa política de infraestrutura; ISP evita exigir operações não usadas. Teste fake que retorna saldo fixo. Adicione abstração só se substituição justificar indireção.

**Explicação:** Chamador precisa de comportamento, não detalhes de armazenamento; type hints sozinhos não impõem semântica em runtime.

**Intenção do entrevistador:** Avaliar SOLID como trade-offs de design.

**Erros comuns**

- Criar cinco classes apenas para corresponder a cinco princípios.

**Perguntas complementares**

- Quando função simples seria mais adequada?

**Exemplo**

Injete fake apenas available retornando 7 e confira política sem banco.

**Rubrica de autoavaliação**

- 1 — Explica DIP e ISP por contrato pequeno substituível.
- 1 — Propõe teste com fake e pondera indireção adicional.

Máximo: 2

</details>

**Pré-requisitos**

- [Encapsulamento e abstração](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.pt-BR.md)
- [SOLID como perguntas de design](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.pt-BR.md)

## Internals de Python

### internals.del-binding

`junior` · `python-internals`

Dado first=[]; second=first; del first; second.append(3), qual second? del garante destruição?

<details>
<summary>Resposta esperada</summary>

second é [3]. del remove vinculação first, não objeto enquanto second ainda o referencia fortemente. Python não garante destruição imediata.

**Explicação:** Alcançabilidade e ownership, não nome específico, determinam se referência ainda mantém objeto vivo.

**Intenção do entrevistador:** Avaliar raciocínio sobre vida do objeto.

**Erros comuns**

- Supor que del first esvazia lista.

**Perguntas complementares**

- E se contêiner global ainda guarda lista?

**Exemplo**

Lista armazenada em dois nomes permanece utilizável pelo nome restante.

**Rubrica de autoavaliação**

- 1 — Prevê second e distingue remoção da vinculação de destruição.
- 1 — Explica referência forte e ausência de garantia de finalização imediata.

Máximo: 2

</details>

**Pré-requisitos**

- [Vida e alcançabilidade de objetos](../../technical-interview-preparation/10-python-memory-management/README.pt-BR.md)

### internals.iterator-exhaustion

`junior` · `python-internals`

Dado it=iter([1,2,3]); next(it); print(list(it)); print(list(it)), o que exibe e por quê?

<details>
<summary>Resposta esperada</summary>

Exibe [2,3] depois []. next consumiu 1; primeira chamada list consumiu restante, logo iterador esgotou. iter(it) retorna esse iterador, não nova travessia.

**Explicação:** Lista é iterável e fornece novos iteradores; iterador guarda estado da travessia.

**Intenção do entrevistador:** Avaliar consumo único.

**Erros comuns**

- Supor list(it) reinicia iterador.

**Perguntas complementares**

- Que exceção next(it) gera quando esgotado?

**Exemplo**

iter([1,2]) e outro iter([1,2]) são travessias separadas.

**Rubrica de autoavaliação**

- 1 — Prevê ambas listas impressas.
- 1 — Explica estado, esgotamento e diferença de iterável.

Máximo: 2

</details>

**Pré-requisitos**

- [Protocolo de iteração](../../technical-interview-preparation/11-iterators-generators-and-comprehensions/README.pt-BR.md)

### internals.context-exit

`mid` · `python-internals`

Gerenciador abre recurso e corpo gera RuntimeError. Explique __enter__, __exit__, supressão e o que muda se própria entrada falhar.

<details>
<summary>Resposta esperada</summary>

__enter__ retorna valor de as. Após entrada bem-sucedida, __exit__ recebe detalhes de exceção e libera recurso; false/None propaga exceção do corpo, truthy suprime. Se entrada falhar, exit daquele gerenciador não é chamado automaticamente; entrada trata aquisição parcial.

**Explicação:** Limpeza e supressão são decisões separadas; retorno truthy acidental oculta erros.

**Intenção do entrevistador:** Avaliar gerenciamento de recursos e semântica de falha.

**Erros comuns**

- Supor exit executa mesmo se enter gerar exceção.

**Perguntas complementares**

- Como testaria limpeza exatamente uma vez?

**Exemplo**

Entrada bem-sucedida seguida de falha do corpo registra open e close uma vez, com RuntimeError propagado se exit retorna False.

**Rubrica de autoavaliação**

- 1 — Descreve entrada, detalhes de saída e contrato de supressão truthy.
- 1 — Distingue falha do corpo de entrada e aquisição parcial.

Máximo: 2

</details>

**Pré-requisitos**

- [Protocolo with](../../technical-interview-preparation/13-context-managers/README.pt-BR.md)
- [Decisões práticas](../../technical-interview-preparation/13-context-managers/README.pt-BR.md)

### internals.decorator-contract

`mid` · `python-internals`

Decorator de log deve registrar cada tentativa, inclusive chamadas que geram exceção, sem alterar contrato do cálculo. Como implementaria e testaria registro de tentativas, retorno, argumentos, metadados e propagação de falha?

<details>
<summary>Resposta esperada</summary>

Supondo que o registro funcione, registre cada tentativa antes de invocar a função decorada. Encaminhe `*args` e `**kwargs`, retorne resultado, preserve metadados com `functools.wraps` e deixe exceções propagar. Teste chamadas posicionais e nomeadas, resultado, nome e exceção deliberada; confira exatamente um registro por tentativa, inclusive falha.

**Explicação:** Wrapper transversal não deve alterar comportamento central silenciosamente.

**Intenção do entrevistador:** Avaliar decorators e testes de preservação de comportamento.

**Erros comuns**

- Esquecer retorno do resultado ou engolir exceções.
- Registrar apenas retornos bem-sucedidos, omitindo tentativas com falha.

**Perguntas complementares**

- Quando decorators empilhados são aplicados?

**Exemplo**

Usando `record_calls(records)` com lista inicialmente vazia, `divide(8, denominator=2)` decorada retorna `4`; `divide(8, denominator=0)` gera `ZeroDivisionError`. Depois, `records` é igual a `['divide', 'divide']`.

**Rubrica de autoavaliação**

- 1 — Especifica um registro por tentativa antes da chamada, encaminhamento, retorno, metadados e preservação de exceção.
- 1 — Propõe testes para cada contrato nomeado, conferindo registro das tentativas em sucesso e falha.

Máximo: 2

</details>

**Pré-requisitos**

- [Decorators](../../technical-interview-preparation/12-closures-and-decorators/README.pt-BR.md)

### internals.late-binding

`mid` · `python-internals`

Dentro de fábrica, crie três lambdas em loop range(3), cada retornando i. Se chamadas só depois do loop, o que retornam? Mostre correção para índices imutáveis.

<details>
<summary>Resposta esperada</summary>

Todas retornam 2 porque closures compartilham vinculação envolvente variável. Use lambda i=i: i para vincular valor imutável atual como padrão na definição, ou fábrica separada.

**Explicação:** Captura de closure não é snapshot automático; padrão é avaliado na criação da função.

**Intenção do entrevistador:** Avaliar momento de vinculação e comportamento de closure.

**Erros comuns**

- Esperar 0, 1, 2 sem vincular valores individuais.

**Perguntas complementares**

- Vincular lista mutável como padrão faria cópia profunda?

**Exemplo**

[lambda i=i: i for i in range(3)] produz funções retornando 0, 1, 2 respectivamente.

**Rubrica de autoavaliação**

- 1 — Prevê resultados tardios e explica vinculação compartilhada.
- 1 — Demonstra correção válida por snapshot/fábrica para imutáveis.

Máximo: 2

</details>

**Pré-requisitos**

- [Closures e escopo](../../technical-interview-preparation/12-closures-and-decorators/README.pt-BR.md)

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

### internals.cache-retention

`senior` · `python-internals`

Serviço CPython cresce memória retendo cache global. Explique retenção alcançável versus ciclos inalcançáveis, o que gc.collect pode fazer e como mediria e limitaria problema.

<details>
<summary>Resposta esperada</summary>

Valores alcançáveis de cache permanecem vivos; contagem de referências convencional mais GC de ciclos recupera muitos objetos/ciclos inalcançáveis, mas gc.collect não libera alcançáveis nem garante RSS menor. Inspecione ownership e compare snapshots tracemalloc junto com métricas de memória do processo; limite por orçamento de quantidade/bytes, expulse referências e confira aliases externos.

**Explicação:** Snapshots de alocação Python não medem toda alocação nativa ou RSS. Limite de quantidade não limita bytes.

**Intenção do entrevistador:** Avaliar diagnóstico de memória antes da otimização.

**Erros comuns**

- Forçar GC periodicamente mantendo mesmo cache alcançável ilimitado.

**Perguntas complementares**

- Por que limpar cache pode deixar valores vivos?

**Exemplo**

Limite de 100 entradas não implica 100 bytes; compare alocações antes/depois de expulsões com carga representativa.

**Rubrica de autoavaliação**

- 1 — Explica alcançabilidade, GC de ciclos e limites de coleta.
- 1 — Propõe retenção limitada e medição distinguindo tracemalloc de memória do processo.

Máximo: 2

</details>

**Pré-requisitos**

- [Vida e alcançabilidade de objetos](../../technical-interview-preparation/10-python-memory-management/README.pt-BR.md)
- [Retenção e medição](../../technical-interview-preparation/10-python-memory-management/README.pt-BR.md)

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

## Testes e debugging

### testing.else-finally

`junior` · `testing-debugging`

Quais papéis de else e finally em try? Explique comportamento quando operação protegida gera exceção inesperada.

<details>
<summary>Resposta esperada</summary>

else executa quando bloco try termina normalmente sem exceção; finally executa na saída para limpeza. Exceção não capturada propaga após finally salvo se limpeza alterar resultado.

**Explicação:** Não retorne de finally para esconder falha.

**Intenção do entrevistador:** Avaliar fluxo estruturado de exceções.

**Erros comuns**

- Tratar finally como código só de sucesso.

**Perguntas complementares**

- Quando with pode ser mais claro?

**Exemplo**

Após RuntimeError não capturado, limpeza em finally ainda roda antes de propagar.

**Rubrica de autoavaliação**

- 1 — Distingue else de conclusão normal de finally de limpeza.
- 1 — Explica propagação de exceção inesperada e ressalva de limpeza.

Máximo: 2

</details>

**Pré-requisitos**

- [Fronteiras de exceção](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)

### testing.specific-catch

`junior` · `testing-debugging`

Ao converter texto para int, por que capturar ValueError especificamente em vez de ocultar toda exceção? O que texto inválido deve fazer?

<details>
<summary>Resposta esperada</summary>

Capture falha esperada de conversão na fronteira que pode tratar ou traduzir. Informe ou levante erro acordado de entrada inválida; deixe exceções inesperadas alheias propagar.

**Explicação:** Retornar zero para texto ruim confunde entrada inválida com zero válido.

**Intenção do entrevistador:** Avaliar escopo de exceção e contratos de dados.

**Erros comuns**

- Capturar tudo e retornar zero incondicionalmente.

**Perguntas complementares**

- O que distingue "0" de "abc" em testes?

**Exemplo**

int("0") funciona, int("abc") gera ValueError.

**Rubrica de autoavaliação**

- 1 — Escolhe exceção específica esperada e explica propagação.
- 1 — Distingue texto inválido de zero válido no contrato.

Máximo: 2

</details>

**Pré-requisitos**

- [Fronteiras de exceção](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)

### testing.test-levels

`junior` · `testing-debugging`

Diferencie testes unitários, integração e ponta a ponta para serviço de relatório. Dê exemplo de cada.

<details>
<summary>Resposta esperada</summary>

Unitário: conte IDs únicos usando loader fake controlado. Integração: exercite loader real contra banco de teste. Ponta a ponta: solicite relatório pela interface suportada e confira resposta no fluxo completo.

**Explicação:** Níveis diferem pelas fronteiras exercitadas, não só quantidade de assertions.

**Intenção do entrevistador:** Avaliar escopo de testes e fronteiras de dependência.

**Erros comuns**

- Chamar teste com todas dependências mockadas de ponta a ponta.

**Perguntas complementares**

- Por que manter teste de integração real se unitários passam?

**Exemplo**

Loader fake retornando [1,1,2] apoia assertion unitária de duas conclusões únicas.

**Rubrica de autoavaliação**

- 1 — Identifica fronteiras unitária e integração com exemplos distintos.
- 1 — Descreve fluxo completo suportado para ponta a ponta.

Máximo: 2

</details>

**Pré-requisitos**

- [Testar e depurar por evidências](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)
- [Decisões começam no requisito](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.pt-BR.md)

### testing.boundary-oracle

`mid` · `testing-debugging`

parse_quantity aceita texto inteiro não negativo, inclusive espaços suportados por int, e rejeita inválidos ou negativos. Dê testes com saídas/erros esperados que detectem versão retornando zero em entrada ruim.

<details>
<summary>Resposta esperada</summary>

Afirme "0" retorna 0 e " 12 " retorna 12; exija InvalidQuantity documentada para "abc", "-1" e "". Conferir exceção específica em vez de só execução detecta zero silencioso.

**Explicação:** Assertions positivas e negativas precisam distinguir contrato pretendido de implementações erradas plausíveis.

**Intenção do entrevistador:** Avaliar precisão do oráculo e cobertura de bordas.

**Erros comuns**

- Afirmar só que função foi chamada ou retornou int.

**Perguntas complementares**

- Qual caso detecta rejeição do zero válido?

**Exemplo**

Teste exigindo InvalidQuantity para "abc" falha quando implementação retorna 0 silenciosamente.

**Rubrica de autoavaliação**

- 1 — Especifica resultados exatos para normal e borda zero.
- 1 — Especifica comportamento de erro exato para inválidos e negativos.

Máximo: 2

</details>

**Pré-requisitos**

- [Fronteiras de exceção](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)
- [Testar e depurar por evidências](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)
- [Prática](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)

### testing.debugging-evidence

`mid` · `testing-debugging`

Parser antes funcional falha numa entrada. Descreva sequência de debugging e evidências a registrar sem expor payloads privados.

<details>
<summary>Resposta esperada</summary>

Reproduza com entrada mínima sanitizada, inspecione traceback e estado relevante, formule hipótese, altere uma causa, rode reprodução e adicione teste de regressão. Registre contexto seguro e resultados reais, ocultando segredos.

**Explicação:** Mudanças controladas facilitam interpretar evidência causal.

**Intenção do entrevistador:** Avaliar debugging disciplinado e privacidade.

**Erros comuns**

- Registrar credenciais brutas e mudar várias condições de uma vez.

**Perguntas complementares**

- E se não conseguir reproduzir falha?

**Exemplo**

Substitua entrada privada por string fictícia mínima malformada que reproduza mesma exceção.

**Rubrica de autoavaliação**

- 1 — Descreve sequência de reprodução, hipótese e verificação controlada.
- 1 — Propõe evidência de regressão com logs sanitizados e resultados reais.

Máximo: 2

</details>

**Pré-requisitos**

- [Testar e depurar por evidências](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)

### testing.exception-cause

`mid` · `testing-debugging`

Na fronteira de conversão, traduza ValueError para InvalidQuantity sem perder causa. Mostre sintaxe e distinga de raise sem argumento.

<details>
<summary>Resposta esperada</summary>

Em except ValueError as error, use raise InvalidQuantity("invalid quantity") from error. Causa explícita é preservada. raise sem argumento relança exceção ativa em vez de traduzir.

**Explicação:** Tradução oferece contrato de domínio estável mantendo evidência diagnóstica.

**Intenção do entrevistador:** Avaliar encadeamento de exceções e diagnóstico.

**Erros comuns**

- Substituir erro por valor de sucesso.

**Perguntas complementares**

- Qual assertion verifica tipo da causa original?

**Exemplo**

assert isinstance(caught.exception.__cause__, ValueError) em contexto assertRaises do unittest.

**Rubrica de autoavaliação**

- 1 — Mostra sintaxe raise-from explícita com erro capturado.
- 1 — Distingue relançar de traduzir e explica preservação de causa.

Máximo: 2

</details>

**Pré-requisitos**

- [Fronteiras de exceção](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)

### testing.coverage-vs-discrimination

`senior` · `testing-debugging`

Parser tem alta cobertura de linhas mas implementação mutada retornando zero para texto inválido ainda passa. Explique significado e proponha estratégia mais forte sem alegar testes provam toda correção.

<details>
<summary>Resposta esperada</summary>

Cobertura mede execução, não correção. Defeito plausível sobrevivente mostra oráculo insuficiente nesse comportamento. Adicione assertions precisas de valor/exceção, bordas e regressão; execute versões correta e errada intencional. Teste fronteiras reais separadamente, com setup determinístico. Passar fortalece evidência, não prova todo comportamento.

**Explicação:** Teste negativo útil rejeita defeito representativo enquanto referência passa.

**Intenção do entrevistador:** Avaliar qualidade de testes e limites de garantia.

**Erros comuns**

- Tratar percentual de cobertura como prova de correção.

**Perguntas complementares**

- Por que manter assertions sobre estado intacto após operação rejeitada?

**Exemplo**

Exija saída zero correta para "0" e exceção específica para "abc"; variante zero silencioso deve falhar.

**Rubrica de autoavaliação**

- 1 — Explica defeito sobrevivente e distinção cobertura/oráculo.
- 1 — Propõe testes discriminantes determinísticos, verificação de fronteiras e limites honestos.

Máximo: 2

</details>

**Pré-requisitos**

- [Testar e depurar por evidências](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)
- [Prática](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)

## Backend e APIs

### api.http-request-response

`junior` · `backend-apis`

Descreva elementos principais de requisição e resposta HTTP. Dê exemplo GET e explique qual lado escolhe status.

<details>
<summary>Resposta esperada</summary>

Requisição tem método, alvo, headers e conteúdo opcional. Servidor responde status, headers e conteúdo opcional. Cliente envia GET /lessons; servidor determina status e representação segundo contrato.

**Explicação:** Status HTTP descreve resultado, não ação escolhida pelo cliente.

**Intenção do entrevistador:** Avaliar fundamentos de requisição/resposta HTTP.

**Erros comuns**

- Supor que toda requisição ou resposta HTTP precisa conter JSON.

**Perguntas complementares**

- Qual header de resposta pode descrever formato do conteúdo?

**Exemplo**

GET /lessons → 200 com Content-Type: application/json e representação de aulas.

**Rubrica de autoavaliação**

- 1 — Identifica método/alvo versus status e ambos conjuntos de headers.
- 1 — Dá exemplo GET coerente e distingue conteúdo opcional.

Máximo: 2

</details>

**Pré-requisitos**

- [Contratos cliente, servidor e recurso](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.pt-BR.md)

### api.status-contract

`junior` · `backend-apis`

Endpoint /lessons só GET recebe GET /missing e POST /lessons. Quais status adequados e qual header acompanha método não suportado?

<details>
<summary>Resposta esperada</summary>

Retorne 404 para recurso ausente e 405 para alvo conhecido com método não suportado. Inclua Allow: GET sob contrato somente GET. GET bem-sucedido pode retornar 200.

**Explicação:** Alvos ausentes e métodos não suportados são falhas distintas.

**Intenção do entrevistador:** Avaliar semântica de status e contratos.

**Erros comuns**

- Retornar 200 para todo resultado ou confundir 404 com 405.

**Perguntas complementares**

- O que corpo de erro estável evitaria revelar?

**Exemplo**

GET /missing → 404; POST /lessons → 405 e Allow: GET.

**Rubrica de autoavaliação**

- 1 — Escolhe ambos status corretos para casos distintos.
- 1 — Inclui Allow e explica relação com alvo conhecido.

Máximo: 2

</details>

**Pré-requisitos**

- [Design de resposta](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.pt-BR.md)

### api.idempotent-retry

`mid` · `backend-apis`

POST de criação dá timeout após possível sucesso. Compare retry de POST com semântica PUT e DELETE; proponha contrato seguro e explique por que respostas iguais não são necessárias.

<details>
<summary>Resposta esperada</summary>

POST não tem idempotência garantida, logo retry cego pode duplicar criação. PUT e DELETE têm efeitos pretendidos idempotentes pela semântica HTTP, não respostas necessariamente idênticas. Para criação repetível use contrato explícito com chave de idempotência persistida, tentativas limitadas, timeouts e respeito a Retry-After quando aplicável.

**Explicação:** Timeout não determina se servidor confirmou efeito colateral.

**Intenção do entrevistador:** Avaliar incerteza de requisição distribuída e design de contrato.

**Erros comuns**

- Repetir todo POST sem semântica de deduplicação.

**Perguntas complementares**

- Por que DELETE repetido pode retornar 204 e depois 404?

**Exemplo**

Mesma requisição de criação com chave persistida não deve criar segundo recurso sob contrato explícito.

**Rubrica de autoavaliação**

- 1 — Distingue risco de retry POST de idempotência de efeito PUT/DELETE.
- 1 — Propõe contrato explícito de retry e comportamento de rede limitado.

Máximo: 2

</details>

**Pré-requisitos**

- [Contratos cliente, servidor e recurso](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.pt-BR.md)

### api.payload-boundary

`mid` · `backend-apis`

API aceita exatamente campo title, string de 1–80 caracteres após trim. Explique parsing versus validação; proponha entradas aceitas/rejeitadas e limites de transporte.

<details>
<summary>Resposta esperada</summary>

Parsing decodifica JSON; validação confere formato objeto, campo permitido, tipo string e tamanho após trim. Aceite {"title":" SQL "} como SQL; rejeite campos ausentes/extras, booleanos, branco e título longo. Limite corpo antes de parsing quando possível e defina tratamento de chaves duplicadas separadamente.

**Explicação:** JSON sintaticamente válido pode violar regras de domínio. Dict decodificado não revela confiavelmente chaves duplicadas na entrada bruta.

**Intenção do entrevistador:** Avaliar validação em camadas e testes de fronteira.

**Erros comuns**

- Tratar parsing JSON bem-sucedido como prova de entrada de negócio válida.

**Perguntas complementares**

- Por que rejeitar campo owner extra neste contrato?

**Exemplo**

Título de exatamente 80 caracteres após trim é aceito; 81 rejeitado.

**Rubrica de autoavaliação**

- 1 — Separa parsing de validação de formato/tipo/tamanho com exemplos positivos e negativos.
- 1 — Identifica limites de transporte e chaves duplicadas brutas como preocupações distintas.

Máximo: 2

</details>

**Pré-requisitos**

- [Validar a fronteira](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.pt-BR.md)

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

## Bancos de dados e SQL

### sql.keys-and-constraints

`junior` · `databases-sql`

Tabela lessons exige títulos únicos não nulos e minutos positivos não nulos. Quais restrições expressam regras e para que chave primária? Explique a ressalva da tipagem INTEGER no SQLite se minutes precisar ser inteiro.

<details>
<summary>Resposta esperada</summary>

Use title TEXT NOT NULL UNIQUE e minutes INTEGER NOT NULL CHECK(minutes > 0); chave primária identifica linha. Em SQLite, INTEGER declarado sozinho não impõe tipo estrito; use verificação adequada de tipo armazenado e validação de aplicação para domínio inteiro.

**Explicação:** CHECK sozinho não rejeita NULL; combine com NOT NULL.

**Intenção do entrevistador:** Avaliar restrições de integridade relacional.

**Erros comuns**

- Supor CHECK(minutes > 0) sozinho proíbe NULL ou fracionários.

**Perguntas complementares**

- O que inserir título duplicado deve fazer?

**Exemplo**

SQLite pode usar CHECK(typeof(minutes) = 'integer' AND minutes > 0) junto com NOT NULL.

**Rubrica de autoavaliação**

- 1 — Seleciona restrições corretas UNIQUE, NOT NULL e CHECK positivo.
- 1 — Explica chave primária e por que tipagem inteira SQLite exige cuidado.

Máximo: 2

</details>

**Pré-requisitos**

- [Modelo relacional e restrições](../../technical-interview-preparation/18-relational-databases-and-sql/README.pt-BR.md)

### sql.null-and-order

`junior` · `databases-sql`

Dada lessons(id, title, minutes) com minutes anulável, escreva consulta para linhas sem minutes ordenadas por id. Explique por que = NULL e omitir ORDER BY são inadequados.

<details>
<summary>Resposta esperada</summary>

SELECT id, title FROM lessons WHERE minutes IS NULL ORDER BY id; comparação com NULL normalmente resulta desconhecido, não verdadeiro, e WHERE mantém verdadeiros. Sem ORDER BY, ordem não é garantida.

**Explicação:** NULL representa informação ausente/desconhecida, não zero.

**Intenção do entrevistador:** Avaliar filtro SQL com valor desconhecido e ordem explícita.

**Erros comuns**

- Usar minutes = NULL ou supor ordem de inserção.

**Perguntas complementares**

- minutes=0 corresponderia à consulta?

**Exemplo**

Com minutes NULL, 0, 20, só linha NULL corresponde.

**Rubrica de autoavaliação**

- 1 — Usa IS NULL e ORDER BY id explícito.
- 1 — Explica comparação desconhecida e ausência de ordem padrão.

Máximo: 2

</details>

**Pré-requisitos**

- [Modelo relacional e restrições](../../technical-interview-preparation/18-relational-databases-and-sql/README.pt-BR.md)

### sql.bound-values

`mid` · `databases-sql`

Em sqlite3 Python, busca aceita título e coluna de ordenação selecionada. Como vincular título com segurança e restringir coluna? Explique por que placeholders não vinculam identificadores.

<details>
<summary>Resposta esperada</summary>

Passe title como parâmetro de valor, ex. db.execute("SELECT id FROM lessons WHERE title = ?", (title,)). Use consulta fixa ou mapeamento allowlist de opções para identificadores SQL confiáveis; não interpole entrada arbitrária. Placeholders representam valores, não sintaxe SQL como identificadores de colunas.

**Explicação:** Entrada vinculada permanece dado mesmo com aspas. Vírgula forma tupla de um elemento.

**Intenção do entrevistador:** Avaliar construção SQL segura e fronteira de identificadores.

**Erros comuns**

- Concatenar título ou nome de coluna bruto no SQL.

**Perguntas complementares**

- Como testaria títulos com aspas e opções de ordenação não suportadas?

**Exemplo**

Mapeie "duration" ao identificador fixo minutes; rejeite opções desconhecidas. Vincule "O'Reilly" como dado title.

**Rubrica de autoavaliação**

- 1 — Mostra valor title vinculado com tupla correta.
- 1 — Explica limite de identificadores e abordagem consulta fixa/allowlist.

Máximo: 2

</details>

**Pré-requisitos**

- [Conectar com Python](../../technical-interview-preparation/18-relational-databases-and-sql/README.pt-BR.md)
- [Segurança SQL](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.pt-BR.md)

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

### sql.atomic-transfer

`senior` · `databases-sql`

Transferência de créditos debita conta e credita outra. Projete ownership da transação, checagem condicional de saldo e verificação de falha. Explique ACID e se índice novo sozinho garante desempenho melhor.

<details>
<summary>Resposta esperada</summary>

Use transação dedicada sem escritas alheias pendentes; valide contas distintas e quantia inteira positiva, debite apenas se saldo suficiente, confira linhas afetadas, credite destino e confirme só após ambas; rollback se destino ausente ou qualquer falha. ACID significa atomicidade, consistência de invariantes, regras de visibilidade do isolamento e durabilidade conforme garantias de armazenamento. Confira saldos após sucesso/falha e em conexão separada após commit. Índices custam armazenamento/escritas; inspecione planos e meça antes de alegar melhoria.

**Explicação:** Atomicidade impede débito parcial; banco em memória não é durável após saída do processo. Isolamento depende do motor.

**Intenção do entrevistador:** Avaliar garantias de integridade, testes de falha e otimização medida.

**Erros comuns**

- Confirmar débito antes de crédito ou supor todo índice ajuda.

**Perguntas complementares**

- Por que observar saldo novo na conexão de escrita não basta para provar commit?

**Exemplo**

Saldos 10 e 2 viram 7 e 5 após transferir 3; transferência posterior falha para destino inexistente deixa ambos intactos.

**Rubrica de autoavaliação**

- 1 — Projeta ownership atômico, updates condicionais e verificações entre conexões/de falha.
- 1 — Explica quatro propriedades ACID e propõe medir benefício do índice contra custo.

Máximo: 2

</details>

**Pré-requisitos**

- [Transações e integridade](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.pt-BR.md)
- [Índices e plano de consulta](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.pt-BR.md)

## Engenharia de software

### engineering.sdd-tdd

`junior` · `software-engineering`

Diferencie SDD de TDD para função contando aulas concluídas únicas. Que evidência é necessária antes de alegar Red e Green?

<details>
<summary>Resposta esperada</summary>

SDD define requisito, plano, tarefas e critérios de aceite observáveis. TDD escreve teste de comportamento, observa falha pela razão pretendida, implementa e observa testes passando antes de refatorar. Registre resultados reais; só escrever teste não estabelece Red.

**Explicação:** Especificações definem o que entregar; testes fornecem evidência de execução de comportamento.

**Intenção do entrevistador:** Avaliar disciplina de desenvolvimento e honestidade de evidência.

**Erros comuns**

- Alegar Red porque arquivo de teste foi commitado primeiro.

**Perguntas complementares**

- Que caso de aceite rejeitaria contagem duplicada?

**Exemplo**

Entrada [1,2,2] tem contagem esperada 2; execute teste antes e após implementação.

**Rubrica de autoavaliação**

- 1 — Distingue artefatos de especificação do ciclo TDD.
- 1 — Exige evidência observada de falha/sucesso antes de alegar Red/Green.

Máximo: 2

</details>

**Pré-requisitos**

- [Decisões começam no requisito](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.pt-BR.md)

### engineering.dependency-boundary

`mid` · `software-engineering`

Regra de relatório de progresso abre banco diretamente. Redesenhe fronteira para testes unitários sem armazenamento; explique integração e como registrar decisão em ADR.

<details>
<summary>Resposta esperada</summary>

Injete callable loader retornando IDs concluídos para aluno; mantenha contagem de IDs únicos e validação na regra. Use fake para duplicados, vazio, IDs inválidos e falha de dependência propagada. Integração verifica consulta/mapeamento real separadamente. Registre contexto, alternativas (consulta direta vs loader injetado), decisão, consequências e critérios de aceite.

**Explicação:** Injeção isola testes de política mas não verifica fronteira real; abstração adiciona indireção.

**Intenção do entrevistador:** Avaliar manutenibilidade, fronteiras de teste e decisões documentadas.

**Erros comuns**

- Substituir todo teste de integração por testes de loader fake.

**Perguntas complementares**

- Quando código direto seria mais simples que nova abstração?

**Exemplo**

progress_report("learner-a", lambda _: [1,2,2]) deve retornar {"completed":2}.

**Rubrica de autoavaliação**

- 1 — Propõe loader substituível e distingue responsabilidades unitária/integração.
- 1 — Registra contexto, alternativas, decisão e consequências incluindo evidência de teste.

Máximo: 2

</details>

**Pré-requisitos**

- [Decisões começam no requisito](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.pt-BR.md)
- [Trade-offs e operação](../../technical-interview-preparation/21-software-engineering-and-technical-decisions/README.pt-BR.md)

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

## Entrevistas comportamentais e internacionais

### behavioral.star-evidence

`junior` · `behavioral-international`

Descreva um bug ou desafio de aprendizado usando STAR. Use exemplo verdadeiro não confidencial (estudo ou projeto pessoal é válido), ou identifique ensaio fictício explicitamente. Distinga sua ação, resultado observável, aprendizado e limitação.

<details>
<summary>Resposta esperada</summary>

Declare situação breve, tarefa sob sua responsabilidade, ações específicas que realizou e resultado observável mais aprendizado. Descreva limitação honestamente; não invente métricas, atribua trabalho alheio a si ou exponha material confidencial.

**Explicação:** STAR organiza evidências sem exigir experiência profissional ou impacto numérico.

**Intenção do entrevistador:** Avaliar responsabilidade, evidência concreta e aprendizado.

**Erros comuns**

- Apresentar sucesso fictício como emprego real ou atribuir resultado coletivo a trabalho individual.

**Perguntas complementares**

- O que melhoraria depois e como verificaria?

**Exemplo**

Ensaio fictício: script de estudos contava IDs duplicados (S); eu respondia pela regra (T); esclareci requisito, escrevi teste de regressão e corrigi regra (A); teste passou, integração com banco ficou sem verificação (R). Aprendi a distinguir evidência unitária de integração.

**Rubrica de autoavaliação**

- 1 — Apresenta situação, tarefa e ação pessoal concreta, identificando material fictício.
- 1 — Declara resultado observável, aprendizado e limitação sem alegações sem suporte ou dados confidenciais.

Máximo: 2

</details>

**Pré-requisitos**

- [Evidências comportamentais com STAR](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.pt-BR.md)

### behavioral.international-clarification

`mid` · `behavioral-international`

Em entrevista em inglês, requisito muda de retornar primeira ocorrência do alvo (ou -1) para primeira posição de inserção em lista ordenada. Dê esclarecimento curto em inglês, exemplo discriminante e atualização honesta incluindo teste que adicionaria.

<details>
<summary>Resposta esperada</summary>

Reconheça mudança de contrato, esclareça se iguais inserem antes do primeiro igual e reformule requisito. Para [2,4,7], alvo 5, resultado antigo -1 e índice de inserção 2. Proponha teste desse caso e duplicados; distinga testes planejados de executados. Use inglês compreensível, não jargão decorado.

**Explicação:** Exemplo concreto torna contrato alterado observável; qualidade da comunicação é compreensão compartilhada, não sotaque.

**Intenção do entrevistador:** Avaliar esclarecimento, inglês técnico e resposta a feedback.

**Erros comuns**

- Continuar implementando contrato antigo ou afirmar que testes não executados passaram.

**Perguntas complementares**

- Como pediria ao entrevistador que repetisse frase desconhecida?

**Exemplo**

Ensaio em inglês: "Let me restate the requirement. Should the insertion position be before equal values? For [2,4,7] and 5, I expect index 2. I would add this test; I have not run it yet."

**Rubrica de autoavaliação**

- 1 — Usa inglês compreensível para esclarecer e reformular contrato alterado.
- 1 — Dá exemplo discriminante e atualização honesta de teste/status.

Máximo: 2

</details>

**Pré-requisitos**

- [Entrevistas internacionais e inglês técnico](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.pt-BR.md)
- [2. Busca binária](../../problem-solving-and-live-coding/05-searching-algorithms/README.pt-BR.md)

### behavioral.evidence-disagreement

`senior` · `behavioral-international`

Colega prefere dividir serviço lento de relatórios; você prefere investigar cache. Neste cenário fictício, explique como resolveria divergência usando objetivo comum, evidências, trade-offs, decisão documentada e comunicação de riscos. Distinga trabalho proposto de resultados reais.

<details>
<summary>Resposta esperada</summary>

Acorde meta de latência/confiabilidade e investigue evidências de baseline antes de escolher. Ouça restrições do colega; compare defasagem, invalidação e memória de cache com deploy/escala independentes e custo de rede. Acorde experimento pequeno e registro de decisão com critérios, riscos e rollback. Declare sua função e decisão da equipe separadamente; sem resultados, relate experimento como planejado, não ganho verificado.

**Explicação:** Objetivo é decisão fundamentada e acompanhamento colaborativo, não vencer discussão.

**Intenção do entrevistador:** Avaliar liderança técnica, responsabilidade e comunicação transparente de riscos.

**Erros comuns**

- Desconsiderar colega ou inventar melhorias antes da medição.

**Perguntas complementares**

- Se equipe escolher outra opção, como apoiaria e monitoraria plano acordado?

**Exemplo**

Plano fictício: meça custos de leituras repetidas, acorde defasagem aceitável, teste cache limitado contra baseline e documente quando rejeitá-lo. Nenhuma melhoria é alegada até medição.

**Rubrica de autoavaliação**

- 1 — Declara objetivo comum, ouve alternativas e compara trade-offs mensuráveis.
- 1 — Propõe experimento/decisão documentado com critérios, risco e rollback, distinguindo papéis individual/equipe e resultados planejados/verificados.

Máximo: 2

</details>

**Pré-requisitos**

- [Divergências, responsabilidade e trade-offs](../../technical-interview-preparation/23-behavioral-and-international-interviews/README.pt-BR.md)

<!-- interview-questions:end -->

<!-- chapter-navigation:bottom -->
[← Anterior](../21-software-engineering-and-technical-decisions/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../23-behavioral-and-international-interviews/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
