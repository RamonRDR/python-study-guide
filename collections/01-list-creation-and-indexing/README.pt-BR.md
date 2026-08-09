<div align="center">

# Criação, Indexação e Fatiamento de Listas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice de Coleções](../README.pt-BR.md) · [Próximo capítulo: Modificando listas e métodos comuns de listas →](../02-modifying-lists-and-methods/README.pt-BR.md)

A Fase 2 ensinou como strings ordenadas expõem posições e fatias. A Fase 3 começa aplicando essa ideia familiar a um novo tipo de valor: uma **lista**, que pode manter vários valores relacionados juntos sob um único nome.

Uma lista do Python é uma sequência mutável. Neste capítulo, concentre-se primeiro na parte de sequência: listas preservam a ordem dos itens, aceitam indexação com inteiros e aceitam fatiamento. O próximo capítulo vai se concentrar na mutabilidade e nos métodos que alteram listas.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir as Fases 1 e 2 |
| Tempo estimado de estudo | 75 a 95 minutos |
| Conceitos principais | `list`, literais de lista, `len()`, indexação, índices negativos, fatiamento, pertencimento, `IndexError`, introdução à mutabilidade |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar por que uma lista é útil quando vários valores relacionados pertencem ao mesmo conjunto;
- criar listas vazias e preenchidas com colchetes;
- reconhecer que a ordem de uma lista é significativa;
- medir uma lista com `len()`;
- ler itens com índices positivos e negativos;
- ler intervalos com fatiamento;
- explicar por que um índice direto inválido gera `IndexError`;
- explicar por que limites amplos de uma fatia são permitidos;
- testar se um valor está presente com `in` e `not in`;
- relacionar indexação e fatiamento de listas ao comportamento de strings aprendido na Fase 2;
- explicar, em alto nível, o que significa uma lista ser mutável.

## 1. Por que listas existem

Antes das coleções, você pode armazenar valores relacionados em variáveis separadas:

```python
first_topic = "strings"
second_topic = "numbers"
third_topic = "lists"
```

Isso funciona para um exemplo pequeno e fixo, mas a relação entre os valores existe principalmente nos nomes das variáveis.

Uma lista permite que um único valor represente a coleção:

```python
topics = ["strings", "numbers", "lists"]

print(topics)
```

```text
['strings', 'numbers', 'lists']
```

Agora `topics` representa claramente uma coleção ordenada de itens relacionados.

## 2. Criando um literal de lista

Colchetes criam um literal de lista. Separe os itens com vírgulas:

```python
languages = ["Python", "JavaScript", "SQL"]
scores = [8, 9, 10]
prices = [12.50, 8.75, 21.00]

print(languages)
print(scores)
print(prices)
```

```text
['Python', 'JavaScript', 'SQL']
[8, 9, 10]
[12.5, 8.75, 21.0]
```

Os colchetes e as vírgulas fazem parte da sintaxe. Os itens dentro deles são os valores armazenados pela lista.

## 3. Criando uma lista vazia

Uma lista pode começar sem nenhum item:

```python
tasks = []

print(tasks)
print(len(tasks))
print(type(tasks))
```

```text
[]
0
<class 'list'>
```

Uma lista vazia continua sendo um valor `list` válido.

O próximo capítulo mostrará como uma lista pode ganhar, alterar e perder itens depois de criada.

## 4. Listas preservam a ordem

A ordem dos itens faz parte do valor de uma lista:

```python
first_order = ["study", "practice", "review"]
second_order = ["review", "practice", "study"]

print(first_order == second_order)
```

```text
False
```

As duas listas contêm as mesmas três strings, mas as posições são diferentes.

Essa estrutura ordenada é o que torna indexação e fatiamento significativos.

## 5. Listas podem conter diferentes tipos de valores

O Python permite que itens de uma lista tenham tipos diferentes:

```python
mixed_values = ["Python", 3, True, 9.5]

print(mixed_values)
```

```text
['Python', 3, True, 9.5]
```

Isso não significa que misturar valores sem relação seja sempre um bom design. Listas são mais fáceis de entender quando os itens pertencem a um conceito claro, mesmo que os tipos exatos nem sempre sejam iguais.

Por exemplo, uma lista de notas ou uma lista de nomes de tópicos comunica a intenção com mais clareza do que uma lista de fatos sem relação.

## 6. Medindo uma lista com `len()`

`len()` retorna a quantidade de itens:

```python
topics = ["strings", "numbers", "lists"]

print(len(topics))
```

```text
3
```

O resultado é um `int`, assim como acontecia ao medir uma string.

Para uma lista não vazia de tamanho `n`, os índices positivos vão de `0` até `n - 1`.

## 7. A indexação positiva começa em zero

Use colchetes depois do valor da lista ou do nome da variável para ler uma posição:

```python
topics = ["strings", "numbers", "lists"]

print(topics[0])
print(topics[1])
print(topics[2])
```

```text
strings
numbers
lists
```

Um mapa útil de posições é:

```text
Item:   strings  numbers  lists
Index:        0        1      2
```

Esse é o mesmo modelo de indexação iniciada em zero que você já usou com strings.

## 8. Índices negativos contam a partir do final

Índices negativos leem posições em relação ao final:

```python
topics = ["strings", "numbers", "lists"]

print(topics[-1])
print(topics[-2])
print(topics[-3])
```

```text
lists
numbers
strings
```

```text
Item:      strings  numbers  lists
Positive:        0        1      2
Negative:       -3       -2     -1
```

`-1` significa o último item.

## 9. A indexação retorna o item armazenado

Indexar uma string sempre retornava outra `str`, porque uma string armazena pontos de código de texto. Uma lista pode armazenar valores de vários tipos, então indexar uma lista retorna o item daquela posição com seu próprio tipo.

```python
values = ["Python", 42, True]

print(values[0])
print(type(values[0]))
print(values[1])
print(type(values[1]))
print(values[2])
print(type(values[2]))
```

```text
Python
<class 'str'>
42
<class 'int'>
True
<class 'bool'>
```

A lista é o contêiner. A indexação lê um valor contido nela.

## 10. Índices diretos inválidos geram `IndexError`

Um índice direto solicita uma posição exata:

```python
topics = ["strings", "numbers", "lists"]

print(topics[3])
```

```text
IndexError: list index out of range
```

A lista tem tamanho `3`, portanto seus índices positivos válidos são `0`, `1` e `2`.

Uma lista vazia não possui nenhum índice direto válido.

## 11. Fatiamento lê um intervalo

O fatiamento de listas usa a mesma sintaxe básica do fatiamento de strings:

```text
items[start:stop]
```

O limite inicial é incluído e o limite final é excluído.

```python
topics = ["strings", "numbers", "lists", "tuples", "dictionaries"]

print(topics[1:4])
```

```text
['numbers', 'lists', 'tuples']
```

Os índices `1`, `2` e `3` são incluídos. O índice `4` marca onde a fatia termina.

## 12. Uma fatia de lista produz uma lista

Fatiar uma lista produz outra lista:

```python
topics = ["strings", "numbers", "lists", "tuples"]

selected_topics = topics[1:3]

print(selected_topics)
print(type(selected_topics))
```

```text
['numbers', 'lists']
<class 'list'>
```

Isso é diferente da indexação direta:

```text
topics[1]    -> one stored item
topics[1:3]  -> a new list containing a range of items
```

Uma fatia cria um novo objeto de lista. Se os próprios itens fizerem referência a objetos mutáveis, esses objetos internos ainda podem ser compartilhados; esse assunto mais profundo está fora deste capítulo introdutório.

## 13. Omitindo limites da fatia

Omita o limite inicial para começar no primeiro item:

```python
steps = ["study", "understand", "practice", "review"]

print(steps[:2])
print(steps[2:])
print(steps[:])
```

```text
['study', 'understand']
['practice', 'review']
['study', 'understand', 'practice', 'review']
```

Omitir o limite final continua até o fim. Omitir ambos seleciona o intervalo completo.

## 14. Índices negativos também funcionam em fatias

Limites negativos são úteis quando o final da lista é o ponto de referência natural:

```python
steps = ["study", "understand", "practice", "review", "repeat"]

print(steps[-2:])
print(steps[:-2])
```

```text
['review', 'repeat']
['study', 'understand', 'practice']
```

Prefira limites que deixem a intenção fácil de compreender.

## 15. Fatias toleram limites amplos

Assim como fatias de strings, fatias de listas podem ultrapassar as posições disponíveis:

```python
topics = ["strings", "numbers", "lists"]

print(topics[:100])
print(topics[100:])
```

```text
['strings', 'numbers', 'lists']
[]
```

Compare as duas ideias:

```text
topics[100]   -> one exact missing position -> IndexError
topics[:100]  -> available range            -> valid list
```

## 16. Passos em fatias

Uma fatia pode incluir um passo:

```text
items[start:stop:step]
```

Para um primeiro exemplo, omita início e fim e selecione um item a cada dois:

```python
steps = ["study", "understand", "practice", "review", "repeat"]

print(steps[::2])
```

```text
['study', 'practice', 'repeat']
```

Truques avançados de slicing não são o objetivo aqui. Use passos quando eles deixarem o código mais claro.

## 17. Verificando pertencimento com `in`

O operador `in` verifica se um item igual está presente:

```python
topics = ["strings", "numbers", "lists"]

print("lists" in topics)
print("tuples" in topics)
print("tuples" not in topics)
```

```text
True
False
True
```

Essas expressões produzem valores `bool`, conectando coleções diretamente aos conceitos booleanos da Fase 2.

Testes de pertencimento respondem se um valor está presente. Eles não informam em qual posição ele aparece.

## 18. Listas são mutáveis, mas este capítulo primeiro as lê

Uma diferença importante entre strings e listas é a **mutabilidade**.

- uma string não permite substituir uma de suas posições no próprio objeto;
- uma lista permite que seu conteúdo seja alterado depois da criação.

Este capítulo se concentra de propósito em criar e ler listas para que o modelo de sequência se torne familiar primeiro.

O próximo capítulo ensinará atribuição a itens, `append()`, `insert()`, `remove()`, `pop()`, `clear()` e `del`, deixando explícitas as regras de mutação.

## 19. Quando uma lista é uma boa escolha

Uma lista é uma boa escolha inicial quando:

- vários valores pertencem a uma coleção ordenada;
- as posições importam;
- a quantidade de itens pode mudar depois;
- valores duplicados são aceitáveis;
- você espera ler valores por índice ou separar intervalos com fatias.

Exemplos incluem uma sequência de tópicos de estudo, uma lista de compras, etapas ordenadas ou um conjunto de notas registradas em ordem.

## 20. Quando uma lista pode não ser a melhor escolha

Uma lista pode ser uma escolha ruim quando a relação principal entre os dados não é posicional.

Mais adiante nesta fase, você aprenderá alternativas:

- tuplas para dados sequenciais em que a imutabilidade comunica intenção;
- dicionários para relações entre chave e valor;
- conjuntos para valores únicos e operações de pertencimento próprias de conjuntos.

Não escolha uma coleção apenas porque sua sintaxe é familiar. Escolha a estrutura que melhor expressa a relação entre os valores.

## 21. Exemplo prático: inspecionando um plano de estudos

```python
study_plan = ["strings", "numbers", "lists", "tuples", "dictionaries"]

print("Plan:", study_plan)
print("Length:", len(study_plan))
print("Current:", study_plan[2])
print("Next:", study_plan[3])
print("Last two:", study_plan[-2:])
print("Lists included:", "lists" in study_plan)
```

```text
Plan: ['strings', 'numbers', 'lists', 'tuples', 'dictionaries']
Length: 5
Current: lists
Next: tuples
Last two: ['tuples', 'dictionaries']
Lists included: True
```

Este exemplo usa a coleção como um plano ordenado sem alterá-la ainda.

## 22. Exemplo prático: reutilizando ferramentas numéricas da Fase 2

Listas se tornam especialmente úteis quando ferramentas anteriores podem trabalhar com vários valores relacionados:

```python
scores = [8, 9, 10]

print("Lowest:", min(scores))
print("Highest:", max(scores))
print("Total:", sum(scores))
```

```text
Lowest: 8
Highest: 10
Total: 27
```

Você já aprendeu essas funções embutidas na Fase 2. A nova ideia é que uma única lista pode fornecer os valores relacionados como uma coleção.

## 23. Erros comuns

### Começar pelo índice `1`

```python
topics = ["strings", "numbers", "lists"]
print(topics[1])
```

Isso imprime `numbers`, e não `strings`. O primeiro índice é `0`.

### Usar `len(items)` como último índice válido

Se uma lista tem tamanho `3`, o índice `3` já está fora dela. O último índice positivo válido é `len(items) - 1`, e `items[-1]` costuma ser mais claro.

### Esperar que uma fatia retorne um único item

`items[1]` lê um item. `items[1:2]` retorna uma lista contendo no máximo um item.

### Esperar que o limite final da fatia seja incluído

`items[1:3]` inclui os índices `1` e `2`, não o índice `3`.

### Confundir uma lista vazia com um valor ausente

`[]` é uma lista real contendo zero itens. Ela não é o mesmo valor que `None`.

### Misturar valores sem relação e sem motivo

O Python permite tipos mistos de itens, mas uma coleção é mais fácil de compreender quando seus itens representam uma ideia clara.

## 24. Conexões com conceitos anteriores e posteriores

Este capítulo reutiliza várias ideias que você já conhece:

- variáveis dão nomes a valores;
- `type()` identifica a lista e os tipos dos itens indexados;
- `len()` retorna uma contagem inteira;
- índices são inteiros;
- o fatiamento segue o mesmo modelo de incluir o início e excluir o fim usado por strings;
- `in` e `not in` produzem resultados booleanos;
- `min()`, `max()` e `sum()` podem trabalhar com valores apropriados dentro de listas.

Ele também prepara os próximos passos:

- o Capítulo 02 altera o conteúdo de listas de forma deliberada;
- o Capítulo 03 compara listas com tuplas e apresenta imutabilidade como uma escolha de design para coleções;
- o Capítulo 04 substitui a busca por posição por chaves de dicionário;
- o Capítulo 05 apresenta conjuntos, nos quais indexação não é o modelo de organização;
- a Fase 4 usará loops para visitar repetidamente os itens de coleções.

## 25. Exercício: construa um inspetor de coleção

Crie `collection_inspector.py` com este valor inicial:

```python
topics = ["variables", "strings", "numbers", "lists", "tuples"]
```

Exiba:

1. a lista completa;
2. seu tamanho;
3. o primeiro item;
4. o último item;
5. os três itens do meio usando uma fatia;
6. os três primeiros itens usando uma fatia;
7. os dois últimos itens usando uma fatia;
8. um item a cada dois;
9. se `"lists"` está presente;
10. o tipo da coleção completa;
11. o tipo do primeiro item indexado.

Um formato possível de saída é:

```text
Topics: ['variables', 'strings', 'numbers', 'lists', 'tuples']
Length: 5
First: variables
Last: tuples
Middle three: ['strings', 'numbers', 'lists']
First three: ['variables', 'strings', 'numbers']
Last two: ['lists', 'tuples']
Every second: ['variables', 'numbers', 'tuples']
Contains lists: True
Collection type: <class 'list'>
First item type: <class 'str'>
```

Tente resolver sem loops. A Fase 4 apresentará iteração repetida mais adiante.

### Desafio extra

Crie uma segunda lista com cinco notas numéricas. Exiba o primeiro e o último valor, uma fatia com as notas do meio, o menor valor, o maior valor e o total.

Ainda não modifique nenhuma das listas. Esse é o trabalho do próximo capítulo.

## 26. Autoavaliação

Certifique-se de que consegue responder:

1. Que problema uma lista resolve em comparação com várias variáveis separadas?
2. Quais símbolos criam um literal de lista?
3. O que `len()` conta em uma lista?
4. Qual é o primeiro índice positivo?
5. O que significa o índice `-1`?
6. Qual é a diferença entre `items[1]` e `items[1:2]`?
7. O limite final de uma fatia é incluído?
8. O que acontece quando um índice direto está fora da lista?
9. Por que `items[:100]` pode funcionar quando `items[100]` falha?
10. Que tipo de resultado uma fatia de lista produz?
11. O que `in` e `not in` retornam?
12. Em alto nível, o que significa uma lista ser mutável?

## 27. Referência rápida

| Objetivo | Sintaxe | Exemplo |
|---|---|---|
| Lista vazia | `[]` | `items = []` |
| Criar itens | `[a, b, c]` | `topics = ["strings", "lists"]` |
| Quantidade de itens | `len(items)` | `len(topics)` |
| Primeiro item | `items[0]` | `topics[0]` |
| Último item | `items[-1]` | `topics[-1]` |
| Intervalo | `items[start:stop]` | `topics[1:3]` |
| A partir do início | `items[:stop]` | `topics[:2]` |
| Até o final | `items[start:]` | `topics[2:]` |
| Um item a cada dois | `items[::2]` | `topics[::2]` |
| Pertencimento | `value in items` | `"lists" in topics` |
| Ausência | `value not in items` | `"sets" not in topics` |
| Tipo | `type(items)` | `type(topics)` |

## 28. Referências oficiais

- [Documentação do Python: Lists](https://docs.python.org/3/library/stdtypes.html#lists)
- [Documentação do Python: Operações comuns de sequências](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

## Próximo passo

Continue com **Modificando Listas e Métodos Comuns de Listas** para aprender como a mutabilidade funciona na prática.
