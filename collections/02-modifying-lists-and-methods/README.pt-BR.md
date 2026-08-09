<div align="center">

# Modificando Listas e Métodos Comuns de Listas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Criação, indexação e fatiamento de listas](../01-list-creation-and-indexing/README.pt-BR.md) · [Voltar ao índice de Coleções](../README.pt-BR.md) · Próximo capítulo: Tuplas e imutabilidade

O capítulo anterior ensinou a criar e ler listas. Agora a outra metade do modelo de listas se torna importante: uma lista é **mutável**, o que significa que seu conteúdo pode ser alterado depois que a lista é criada.

Este capítulo transforma essa ideia em operações concretas. Você vai substituir itens, adicionar itens, remover itens, reorganizar itens, consultar posições e contagens e entender por que alguns métodos alteram uma lista, mas retornam `None` de forma intencional.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir o Capítulo 01 de Coleções |
| Tempo estimado de estudo | 100 a 125 minutos |
| Conceitos principais | mutabilidade, atribuição por índice, atribuição por slice, `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `del`, `index()`, `count()`, `reverse()`, `sort()`, `copy()` |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar a mutabilidade de listas por meio de mudanças observáveis;
- substituir um item existente pelo índice;
- substituir um slice por outros valores;
- adicionar um item com `append()`;
- adicionar vários itens com `extend()`;
- inserir um item em uma posição escolhida com `insert()`;
- remover por valor com `remove()`;
- remover e recuperar por posição com `pop()`;
- remover itens com `del` e esvaziar uma lista com `clear()`;
- localizar o primeiro valor correspondente com `index()`;
- contar valores correspondentes com `count()`;
- inverter ou ordenar uma lista no próprio objeto;
- reconhecer quais métodos comuns de listas retornam `None`;
- diferenciar atribuir outro nome à mesma lista de criar uma cópia rasa com `copy()`;
- escolher uma operação de modificação pela intenção, e não por hábito.

## 1. O que mutabilidade significa

Um objeto mutável pode mudar enquanto continua sendo o valor referenciado pela mesma variável.

```python
topics = ["strings", "numbers", "lists"]

topics[1] = "numeric tools"

print(topics)
```

```text
['strings', 'numeric tools', 'lists']
```

A variável continua se chamando `topics` e continua referenciando uma lista. O conteúdo dessa lista mudou.

Essa é a diferença central em relação às strings. Posições de uma string podem ser lidas, mas não substituídas no próprio objeto. Posições de uma lista podem ser lidas e também substituídas.

## 2. Substituindo um item pelo índice

Use um alvo de atribuição com colchetes para substituir uma posição que já existe:

```python
languages = ["Python", "Java", "SQL"]

languages[1] = "JavaScript"

print(languages)
```

```text
['Python', 'JavaScript', 'SQL']
```

O lado direito fornece o novo valor. A posição indexada no lado esquerdo identifica onde esse valor deve ficar.

Índices negativos também funcionam:

```python
steps = ["study", "practice", "draft"]

steps[-1] = "review"

print(steps)
```

```text
['study', 'practice', 'review']
```

Use o mesmo modelo de índices aprendido no capítulo anterior.

## 3. A atribuição não cria uma posição ausente

A atribuição a um item substitui uma posição que precisa existir.

```python
topics = ["strings", "numbers", "lists"]

topics[3] = "tuples"
```

```text
IndexError: list assignment index out of range
```

A lista tem três itens, então seus índices positivos válidos são `0`, `1` e `2`.

Se a intenção for adicionar um novo item em vez de substituir um existente, use uma operação de adição como `append()` ou `insert()`.

## 4. Substituindo um intervalo com atribuição por slice

Um slice pode aparecer no lado esquerdo de uma atribuição:

```python
steps = ["study", "practice", "review", "repeat"]

steps[1:3] = ["understand", "practice"]

print(steps)
```

```text
['study', 'understand', 'practice', 'repeat']
```

O slice selecionado é substituído pelos valores do lado direito.

Diferentemente da atribuição a um único índice direto, a atribuição comum por slice também pode mudar a quantidade de itens:

```python
steps = ["study", "review", "repeat"]

steps[1:2] = ["understand", "practice", "review"]

print(steps)
```

```text
['study', 'understand', 'practice', 'review', 'repeat']
```

Você ainda não precisa de padrões avançados de atribuição por slice. A ideia útil para o iniciante é que um alvo em forma de slice pode substituir um intervalo, e não apenas uma posição.

## 5. Adicionando um item com `append()`

`append()` adiciona um valor ao final da lista existente:

```python
topics = ["strings", "numbers"]

topics.append("lists")

print(topics)
```

```text
['strings', 'numbers', 'lists']
```

A lista é modificada no próprio objeto.

Use `append()` quando o valor inteiro passado ao método deve se tornar um único novo item.

## 6. `append()` adiciona exatamente um item

Se o valor passado para `append()` for uma lista, essa lista inteira se torna um único item aninhado:

```python
topics = ["strings", "numbers"]

topics.append(["lists", "tuples"])

print(topics)
print(len(topics))
```

```text
['strings', 'numbers', ['lists', 'tuples']]
3
```

Isso é Python válido. Se essa é a estrutura que você pretendia criar é uma pergunta diferente.

Se você quer que os valores de outra lista se tornem itens separados, use `extend()`.

## 7. Adicionando vários itens com `extend()`

`extend()` adiciona ao final da lista os itens de outro iterável. Neste capítulo para iniciantes, outra lista é o exemplo mais claro:

```python
topics = ["strings", "numbers"]

topics.extend(["lists", "tuples"])

print(topics)
```

```text
['strings', 'numbers', 'lists', 'tuples']
```

Compare a intenção:

- `append(value)` adiciona `value` como um único item.
- `extend(values)` adiciona os itens fornecidos por `values`.

O termo geral do Python *iterable* representa objetos capazes de fornecer itens um após o outro. Os loops tornarão esse conceito mais concreto na Fase 4. Por enquanto, usar outra lista com `extend()` é suficiente.

## 8. Inserindo em uma posição com `insert()`

`insert(index, value)` coloca um valor antes do item que atualmente está naquele índice:

```python
steps = ["study", "review", "repeat"]

steps.insert(1, "practice")

print(steps)
```

```text
['study', 'practice', 'review', 'repeat']
```

Use `insert()` quando a posição em si tiver significado.

Diferentemente da atribuição direta por índice, `insert()` não exige que o índice indique um item que já existe. O Python ajusta um índice de inserção fora dos limites para uma das extremidades: `items.insert(len(items), value)` e índices positivos maiores inserem no final, enquanto índices negativos suficientemente pequenos inserem no início. Portanto, um índice de inserção fora dos limites não gera `IndexError` apenas por estar fora do intervalo atual.

Se o novo item simplesmente pertence ao final, `append()` comunica essa intenção de forma mais direta.

## 9. Removendo por valor com `remove()`

`remove(value)` exclui o primeiro valor igual que encontrar:

```python
topics = ["lists", "strings", "lists", "tuples"]

topics.remove("lists")

print(topics)
```

```text
['strings', 'lists', 'tuples']
```

Apenas o primeiro item `"lists"` correspondente foi removido.

Use `remove()` quando você sabe qual valor quer remover e não precisa receber o valor removido como retorno.

## 10. Valores ausentes fazem `remove()` gerar `ValueError`

`remove()` espera que exista um valor correspondente:

```python
topics = ["strings", "numbers", "lists"]

topics.remove("tuples")
```

```text
ValueError: list.remove(x): x not in list
```

Mais adiante, o fluxo de programa permitirá decidir condicionalmente o que fazer quando um valor pode estar presente ou não. Neste capítulo, a regra importante é simplesmente que um valor ausente causa `ValueError`.

## 11. Removendo e recuperando com `pop()`

`pop()` remove um item e retorna o valor removido.

Sem argumento, ele usa a última posição:

```python
topics = ["strings", "numbers", "lists"]

removed_topic = topics.pop()

print("Removed:", removed_topic)
print("Remaining:", topics)
```

```text
Removed: lists
Remaining: ['strings', 'numbers']
```

Você também pode fornecer um índice:

```python
topics = ["strings", "numbers", "lists"]

removed_topic = topics.pop(0)

print("Removed:", removed_topic)
print("Remaining:", topics)
```

```text
Removed: strings
Remaining: ['numbers', 'lists']
```

Use `pop()` quando as duas ações importam: alterar a lista e manter o valor removido para uso posterior.

## 12. Posições inválidas em `pop()` geram `IndexError`

Um índice inválido não pode ser removido com `pop()`. Chamar `pop()` em uma lista vazia também não oferece nenhum item para remover.

```python
topics = []

topics.pop()
```

```text
IndexError: pop from empty list
```

Isso é diferente de `remove()`: um valor ausente leva a `ValueError`, enquanto uma posição inválida ou indisponível para `pop()` leva a `IndexError`.

## 13. Removendo com `del`

`del` é uma instrução que pode remover um item pelo índice:

```python
topics = ["strings", "numbers", "lists", "tuples"]

del topics[1]

print(topics)
```

```text
['strings', 'lists', 'tuples']
```

Ela também pode remover um slice:

```python
topics = ["variables", "strings", "numbers", "lists", "tuples"]

del topics[1:3]

print(topics)
```

```text
['variables', 'lists', 'tuples']
```

Ao contrário de `pop()`, `del` não devolve o item removido como resultado de método.

## 14. Esvaziando uma lista com `clear()`

`clear()` remove todos os itens enquanto mantém a própria lista disponível:

```python
topics = ["strings", "numbers", "lists"]

topics.clear()

print(topics)
print(len(topics))
```

```text
[]
0
```

A variável continua referenciando uma lista, mas essa lista agora contém zero itens.

## 15. Encontrando a primeira posição correspondente com `index()`

`index(value)` procura o primeiro valor igual e retorna seu índice baseado em zero:

```python
topics = ["lists", "strings", "lists", "tuples"]

print(topics.index("lists"))
print(topics.index("tuples"))
```

```text
0
3
```

`index()` não modifica a lista.

Se o valor estiver ausente, `index()` gera `ValueError`.

## 16. Contando valores correspondentes com `count()`

`count(value)` retorna quantos itens iguais aparecem:

```python
topics = ["lists", "strings", "lists", "tuples"]

print(topics.count("lists"))
print(topics.count("numbers"))
```

```text
2
0
```

Um valor ausente não é erro para `count()`. Sua contagem é simplesmente `0`.

Isso torna `count()` diferente tanto de `index()` quanto de `remove()`.

## 17. Invertendo a ordem atual com `reverse()`

`reverse()` inverte a ordem existente no próprio objeto:

```python
steps = ["study", "practice", "review"]

steps.reverse()

print(steps)
```

```text
['review', 'practice', 'study']
```

`reverse()` não ordena pelos valores. Ele apenas inverte qualquer ordem que a lista já tenha.

## 18. Ordenando no próprio objeto com `sort()`

`sort()` reorganiza uma lista no próprio objeto quando seus itens suportam as comparações necessárias:

```python
scores = [9, 7, 10, 8]

scores.sort()

print(scores)
```

```text
[7, 8, 9, 10]
```

Uma lista simples de strings também pode ser ordenada de acordo com as regras de ordenação do Python:

```python
topics = ["tuples", "lists", "dictionaries"]

topics.sort()

print(topics)
```

```text
['dictionaries', 'lists', 'tuples']
```

Personalizações avançadas de ordenação com `key=` ficam fora deste capítulo. Primeiro aprenda a distinção importante: `sort()` altera a lista existente.

## 19. Nem toda mistura pode ser ordenada

Uma lista pode conter legalmente tipos diferentes, mas isso não garante que esses valores tenham uma relação de ordenação significativa entre si.

```python
values = ["Python", 3, None]

values.sort()
```

```text
TypeError: '<' not supported between instances of 'int' and 'str'
```

Não interprete isso como uma regra de que listas com tipos mistos são inválidas. O problema é mais específico: `sort()` precisa de comparações que os valores contidos suportem.

## 20. Métodos mutadores in-place normalmente retornam `None`

Este é um dos hábitos mais importantes para aprender cedo sobre listas.

Métodos cuja finalidade principal é modificar uma lista no próprio objeto, como `append()`, `extend()`, `insert()`, `remove()`, `clear()`, `reverse()` e `sort()`, retornam `None` em vez da lista alterada.

```python
topics = ["strings", "numbers"]

result = topics.append("lists")

print("Topics:", topics)
print("Result:", result)
```

```text
Topics: ['strings', 'numbers', 'lists']
Result: None
```

O resultado útil de `append()` é a própria lista `topics` alterada. O valor de retorno do método é `None`.

`pop()` é intencionalmente diferente porque recuperar o item removido faz parte de sua finalidade.

## 21. O erro comum `items = items.append(...)`

Como `append()` retorna `None`, este padrão destrói a referência útil da variável para a lista:

```python
items = ["strings", "numbers"]

items = items.append("lists")

print(items)
```

```text
None
```

Use o método mutador como uma instrução própria:

```python
items = ["strings", "numbers"]

items.append("lists")

print(items)
```

```text
['strings', 'numbers', 'lists']
```

O mesmo cuidado se aplica a outros métodos in-place, como `sort()` e `reverse()`.

## 22. A atribuição pode criar outro nome para a mesma lista

Esta linha não copia uma lista:

```python
original = ["strings", "numbers"]
alias = original

alias.append("lists")

print("Original:", original)
print("Alias:", alias)
```

```text
Original: ['strings', 'numbers', 'lists']
Alias: ['strings', 'numbers', 'lists']
```

Os dois nomes de variáveis referenciam a mesma lista mutável, então uma mutação observada por um nome fica visível pelo outro.

É por isso que mutabilidade importa para além de uma única linha de código.

## 23. Criando uma lista separada com `copy()`

`copy()` cria uma nova lista contendo referências aos mesmos itens atuais:

```python
original = ["strings", "numbers"]
independent = original.copy()

independent.append("lists")

print("Original:", original)
print("Copy:", independent)
```

```text
Original: ['strings', 'numbers']
Copy: ['strings', 'numbers', 'lists']
```

Alterar a lista externa copiada não altera mais a lista externa original.

O termo oficial é **shallow copy**, ou cópia rasa. Se uma lista contiver objetos mutáveis dentro dela, esses objetos internos ainda podem ser compartilhados entre as duas listas externas. A cópia de objetos aninhados é um assunto mais profundo; por enquanto, lembre que `copy()` fornece uma lista externa separada.

## 24. Uma comparação: alias versus cópia

```python
original = ["strings", "numbers"]
alias = original
independent = original.copy()

alias.append("lists")
independent.append("tuples")

print("Original:", original)
print("Alias:", alias)
print("Copy:", independent)
```

```text
Original: ['strings', 'numbers', 'lists']
Alias: ['strings', 'numbers', 'lists']
Copy: ['strings', 'numbers', 'tuples']
```

Vale a pena executar e modificar este exemplo. Ele torna o compartilhamento de referência visível sem exigir terminologia avançada sobre modelo de memória.

## 25. Escolhendo a operação pela intenção

Várias operações podem alterar uma lista, mas elas comunicam intenções diferentes.

| Intenção | Operação |
|---|---|
| Substituir uma posição existente | `items[index] = value` |
| Substituir um intervalo | `items[start:stop] = values` |
| Adicionar um item ao final | `append()` |
| Adicionar vários itens ao final | `extend()` |
| Adicionar um item em uma posição específica | `insert()` |
| Remover o primeiro valor correspondente | `remove()` |
| Remover e recuperar um item por posição | `pop()` |
| Remover por índice ou slice sem recuperar | `del` |
| Remover todos os itens | `clear()` |
| Encontrar a primeira posição correspondente | `index()` |
| Contar valores correspondentes | `count()` |
| Inverter a ordem existente | `reverse()` |
| Ordenar a lista existente | `sort()` |
| Criar uma cópia rasa externa separada | `copy()` |

Prefira a operação cujo nome ou sintaxe melhor corresponda ao trabalho que você está realizando.

## 26. Exemplo prático: atualizar uma fila de estudos

```python
study_queue = ["strings", "numbers"]

study_queue.append("lists")
study_queue.insert(1, "variables")
study_queue.remove("numbers")
completed_topic = study_queue.pop(0)

print("Completed:", completed_topic)
print("Queue:", study_queue)
```

```text
Completed: strings
Queue: ['variables', 'lists']
```

O exemplo usa operações diferentes porque as intenções são diferentes: adicionar ao final, inserir em uma posição, remover por valor e depois remover e recuperar por posição.

## 27. Exemplo prático: corrigir e resumir pontuações

```python
scores = [8, 10, 7, 9, 10]

scores[2] = 8
scores.append(9)

print("Tens:", scores.count(10))
print("First ten index:", scores.index(10))

scores.sort()

print("Sorted:", scores)
print("Lowest:", min(scores))
print("Highest:", max(scores))
print("Total:", sum(scores))
```

```text
Tens: 2
First ten index: 1
Sorted: [8, 8, 9, 9, 10, 10]
Lowest: 8
Highest: 10
Total: 54
```

Isso combina ferramentas numéricas da Fase 2 com a nova capacidade de alterar e reorganizar uma lista.

## 28. Erros comuns

### Atribuir o resultado de um método mutador

`items.append(value)`, `items.sort()` e métodos in-place semelhantes retornam `None`. Não substitua sua variável de lista por esse valor de retorno.

### Usar `append()` quando queria `extend()`

`append(["lists", "tuples"])` adiciona um único item que é uma lista aninhada. `extend(["lists", "tuples"])` adiciona dois itens separados.

### Confundir remoção por valor com remoção por posição

`remove(value)` procura por igualdade. `pop(index)` e `del items[index]` trabalham por posição.

### Esperar que `remove()` exclua todas as duplicatas

`remove(value)` exclui somente a primeira correspondência igual.

### Esperar que `pop()` retorne a lista alterada

`pop()` retorna o item que foi removido, e não a lista.

### Presumir que uma atribuição copia uma lista

`second = first` cria outra referência para a mesma lista. Use `copy()` quando precisar de uma lista externa separada.

### Tratar `reverse()` como ordenação

`reverse()` inverte a ordem atual. Ele não decide qual valor deve vir primeiro por tamanho ou ordem alfabética.

### Ordenar valores que não suportam ordenação entre si

Uma lista pode armazenar tipos mistos mesmo quando `sort()` não consegue comparar aqueles valores específicos.

## 29. Mutação e código legível

Mutação é útil, mas um programa fica mais difícil de raciocinar quando uma lista muda em muitos lugares sem relação entre si.

Para código de iniciante, prefira um hábito simples:

- use nomes de variáveis descritivos;
- faça uma mudança por um motivo claro;
- escolha uma operação que expresse a intenção;
- inspecione a lista depois de experimentar uma mutação;
- evite cadeias espertas de operações quando instruções separadas forem mais fáceis de entender.

Fases posteriores fornecerão funções, loops e testes que tornam fluxos maiores de mutação mais fáceis de organizar.

## 30. Conexões com conceitos anteriores e posteriores

Este capítulo se apoia diretamente no material anterior:

- índices e slices vieram da leitura de strings e listas;
- atribuição já conectava nomes a valores;
- `None` já foi apresentado como um valor embutido;
- `IndexError` já apareceu ao ler uma posição inválida de lista;
- ferramentas Booleanas e numéricas continuam funcionando com conteúdos de lista apropriados.

Ele também prepara ideias posteriores:

- o Capítulo 03 vai contrastar listas mutáveis com tuplas imutáveis;
- dicionários e conjuntos possuem suas próprias operações e regras de mutação;
- a Fase 4 usará condicionais e loops para decidir quando e como mudanças repetidas em coleções acontecem;
- as funções da Fase 5 tornarão importante entender quando um objeto mutável pode ser alterado por uma referência passada para outro lugar.

## 31. Exercício: gerencie um backlog de aprendizagem

Crie `learning_backlog.py` com esta lista inicial:

```python
backlog = ["strings", "numbers", "lists"]
```

Sem usar loops ou condicionais:

1. substitua `"numbers"` por `"numeric tools"` pelo índice;
2. adicione `"tuples"` com `append()`;
3. estenda a lista com `"dictionaries"` e `"sets"`;
4. insira `"variables"` no índice `0`;
5. imprima quantas vezes `"lists"` aparece;
6. imprima o índice de `"tuples"`;
7. remova `"numeric tools"` pelo valor;
8. remova o último item com `pop()` e armazene em `removed_topic`;
9. imprima o tópico removido;
10. imprima o backlog resultante;
11. crie uma cópia rasa chamada `backlog_copy`;
12. inverta somente `backlog_copy`;
13. imprima as duas listas para confirmar que inverter a cópia não inverteu a original.

Um possível formato de saída final é:

```text
Lists count: 1
Tuples index: 4
Removed: sets
Backlog: ['variables', 'strings', 'lists', 'tuples', 'dictionaries']
Copy: ['dictionaries', 'tuples', 'lists', 'strings', 'variables']
```

Tente prever cada lista intermediária antes de executar o arquivo.

## 32. Autoavaliação

Antes de seguir adiante, confira se você consegue responder a estas perguntas sem adivinhar:

1. Por que um item de lista pode ser substituído enquanto um caractere de string não pode?
2. Qual é a diferença entre `append()` e `extend()`?
3. Qual é a diferença entre `remove()` e `pop()`?
4. O que `pop()` retorna?
5. Por que `items = items.append(value)` costuma quebrar código de iniciante?
6. O que `clear()` altera?
7. `reverse()` ordena valores?
8. O que `index()` e `count()` retornam?
9. Por que `second = first` pode tornar mutações visíveis pelos dois nomes?
10. O que `copy()` separa, e sobre o que a palavra *shallow* alerta?

Se alguma resposta ainda estiver nebulosa, volte à seção correspondente e altere um dos exemplos por conta própria.

## 33. Referência rápida

- Substituir um item: `items[index] = value`
- Substituir um intervalo: `items[start:stop] = values`
- Adicionar um item ao final: `items.append(value)`
- Adicionar vários itens: `items.extend(values)`
- Inserir antes de uma posição: `items.insert(index, value)`
- Remover o primeiro valor igual: `items.remove(value)`
- Remover e retornar um item: `removed = items.pop()` ou `removed = items.pop(index)`
- Excluir por posição ou intervalo: `del items[index]` ou `del items[start:stop]`
- Remover todos os itens: `items.clear()`
- Encontrar o primeiro valor igual: `position = items.index(value)`
- Contar valores iguais: `quantity = items.count(value)`
- Inverter no próprio objeto: `items.reverse()`
- Ordenar no próprio objeto: `items.sort()`
- Criar uma cópia rasa externa: `other = items.copy()`

Lembre do padrão de valores de retorno:

- `append()`, `extend()`, `insert()`, `remove()`, `clear()`, `reverse()` e `sort()` alteram a lista e retornam `None`.
- `pop()` altera a lista e retorna o item removido.
- `index()` e `count()` não alteram a lista e retornam informações.
- `copy()` não altera a lista original e retorna uma nova lista rasa.

## 34. Para onde seguir

Agora você conhece as duas metades do modelo de listas para iniciantes:

1. Crie e leia uma lista.
2. Altere uma lista de forma deliberada.
3. Compare listas mutáveis com tuplas imutáveis.

O próximo capítulo de Coleções apresenta **tuplas e imutabilidade**. Essa comparação tornará muito mais clara a escolha de design por trás da mutabilidade das listas.

---

Referências oficiais usadas para verificação técnica:

- [Python Tutorial: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Built-in Types: Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
- [Python Built-in Types: Lists](https://docs.python.org/3/library/stdtypes.html#lists)
