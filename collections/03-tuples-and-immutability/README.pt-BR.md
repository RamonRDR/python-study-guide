<div align="center">

# Tuplas e Imutabilidade

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Modificando listas e métodos comuns de listas](../02-modifying-lists-and-methods/README.pt-BR.md) · [Voltar ao índice de Coleções](../README.pt-BR.md) · [Próximo capítulo: Dicionários: chaves e valores](../04-dictionaries-keys-and-values/README.pt-BR.md)

As listas ensinaram o que significa uma coleção ser mutável. As tuplas apresentam a ideia oposta: uma sequência ordenada cujas posições não podem ser substituídas, adicionadas ou removidas depois que a tupla é criada.

Essa diferença é útil porque a forma de alguns dados deve permanecer fixa. Uma tupla pode comunicar essa intenção diretamente.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir os Capítulos 01 e 02 de Coleções |
| Tempo estimado de estudo | 80 a 100 minutos |
| Conceitos principais | literais de tupla, sequências imutáveis, indexação, slicing, tuplas unitárias, `tuple()`, `count()`, `index()`, empacotamento, desempacotamento, objetos mutáveis aninhados |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar o que torna uma tupla uma sequência imutável;
- criar tuplas vazias, de um item e de vários itens;
- reconhecer por que a vírgula é importante na sintaxe de tuplas;
- ler itens de uma tupla com índices positivos e negativos;
- fatiar tuplas sem alterar a original;
- usar `len()`, `in` e `not in` com tuplas;
- criar tuplas com `tuple()`;
- usar `count()` e `index()`;
- explicar por que métodos de mutação de listas não existem em tuplas;
- reconhecer o erro causado por uma atribuição a uma posição da tupla;
- empacotar vários valores em uma tupla;
- desempacotar uma sequência de tamanho fixo em variáveis;
- explicar por que uma tupla ainda pode conter um objeto mutável;
- escolher uma tupla quando uma sequência fixa comunica melhor a intenção dos dados do que uma lista.

## 1. O que é uma tupla?

Uma tupla é uma **sequência ordenada e imutável**.

Ordenada significa que cada item possui uma posição. Imutável significa que a tupla não pode ter suas posições alteradas depois da criação.

```python
course_info = ("Python", "Beginner", 90)

print(course_info)
print(type(course_info))
```

```text
('Python', 'Beginner', 90)
<class 'tuple'>
```

A tupla contém três itens em uma ordem definida.

## 2. Tupla versus lista

Listas e tuplas compartilham muitas operações de sequência, mas diferem em um comportamento central.

```python
topics_list = ["strings", "numbers", "lists"]
topics_tuple = ("strings", "numbers", "lists")

print(type(topics_list))
print(type(topics_tuple))
print(topics_list[0])
print(topics_tuple[0])
```

```text
<class 'list'>
<class 'tuple'>
strings
strings
```

As duas são ordenadas e permitem acesso por índice. A lista pode depois alterar suas posições e seu tamanho. A tupla não pode.

Use essa diferença como um sinal de design, e não como uma disputa sobre qual tipo é "melhor".

## 3. Criando uma tupla

Um literal comum de tupla usa valores separados por vírgulas dentro de parênteses:

```python
dimensions = (1920, 1080)
languages = ("Python", "SQL", "JavaScript")
```

Os parênteses facilitam reconhecer a tupla, mas há um detalhe importante de sintaxe a seguir: é a vírgula que cria uma tupla não vazia.

## 4. A vírgula importa

Estas duas expressões não são iguais:

```python
grouped_value = ("Python")
single_item_tuple = ("Python",)

print(type(grouped_value))
print(type(single_item_tuple))
```

```text
<class 'str'>
<class 'tuple'>
```

`("Python")` é apenas uma expressão string entre parênteses.

`("Python",)` é uma tupla contendo um item.

Esta é uma das regras de sintaxe de tuplas mais importantes para iniciantes.

## 5. Tuplas vazias

Uma tupla vazia é escrita com parênteses vazios:

```python
empty_tuple = ()

print(empty_tuple)
print(len(empty_tuple))
print(type(empty_tuple))
```

```text
()
0
<class 'tuple'>
```

Diferentemente de uma tupla de um item, a tupla vazia não precisa de vírgula.

## 6. Os parênteses frequentemente são opcionais

Em uma tupla não vazia, as vírgulas podem criar a tupla mesmo sem parênteses ao redor:

```python
coordinates = 10, 20

print(coordinates)
print(type(coordinates))
```

```text
(10, 20)
<class 'tuple'>
```

Em código para iniciantes, os parênteses normalmente deixam mais clara a intenção de escrever uma tupla:

```python
coordinates = (10, 20)
```

Há contextos em que os parênteses são exigidos pela sintaxe ao redor. A ideia útil aqui é apenas que as vírgulas, e não os parênteses sozinhos, definem uma tupla não vazia.

## 7. Lendo itens por índice

A indexação de tuplas segue o mesmo modelo iniciado em zero usado por strings e listas:

```python
record = ("Ana", "Python", 3)

print(record[0])
print(record[1])
print(record[2])
```

```text
Ana
Python
3
```

O primeiro item está no índice `0`.

## 8. Índices negativos

Índices negativos funcionam da mesma forma que em strings e listas:

```python
record = ("Ana", "Python", 3)

print(record[-1])
print(record[-2])
```

```text
3
Python
```

`-1` significa o último item.

## 9. Fatiando uma tupla

Slices de tuplas criam outra tupla:

```python
steps = ("study", "understand", "practice", "review", "repeat")

print(steps[:2])
print(steps[1:4])
print(steps[-2:])
```

```text
('study', 'understand')
('understand', 'practice', 'review')
('review', 'repeat')
```

O slicing lê um intervalo. Ele não modifica a tupla original.

## 10. Passos de slicing também funcionam

O modelo comum de slicing de sequências continua valendo:

```python
steps = ("study", "understand", "practice", "review", "repeat")

print(steps[::2])
print(steps[::-1])
```

```text
('study', 'practice', 'repeat')
('repeat', 'review', 'practice', 'understand', 'study')
```

O slice invertido cria uma nova tupla. A original permanece inalterada.

## 11. Comprimento e pertencimento

`len()`, `in` e `not in` funcionam com tuplas:

```python
topics = ("strings", "numbers", "lists", "tuples")

print(len(topics))
print("tuples" in topics)
print("sets" not in topics)
```

```text
4
True
True
```

Essas operações inspecionam a tupla sem alterá-la.

## 12. Imutabilidade na prática

Uma posição da tupla não pode ser substituída:

```python
topics = ("strings", "numbers", "lists")

topics[1] = "numeric tools"
```

```text
TypeError: 'tuple' object does not support item assignment
```

Isso é diferente de uma lista, na qual o mesmo estilo de atribuição por índice é permitido.

Não use o erro como técnica normal de fluxo do programa. O objetivo aqui é apenas tornar a regra visível.

## 13. Tuplas não possuem métodos de mutação de listas

Uma tupla não possui os métodos `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `reverse()` ou `sort()`.

Essa ausência é coerente com a imutabilidade: esses métodos precisariam alterar a sequência existente.

Se os dados precisam crescer, diminuir, se reorganizar no próprio objeto ou substituir posições ao longo do tempo, uma lista normalmente é a escolha mais clara.

## 14. Concatenação cria uma nova tupla

Duas tuplas podem ser concatenadas com `+`:

```python
core_topics = ("strings", "numbers")
collection_topics = ("lists", "tuples")

all_topics = core_topics + collection_topics

print(all_topics)
print(core_topics)
```

```text
('strings', 'numbers', 'lists', 'tuples')
('strings', 'numbers')
```

As tuplas originais permanecem inalteradas. `+` produz uma nova tupla.

## 15. Repetição cria uma nova tupla

A repetição de sequências também funciona:

```python
pattern = ("study", "practice")

repeated = pattern * 2

print(repeated)
print(pattern)
```

```text
('study', 'practice', 'study', 'practice')
('study', 'practice')
```

Novamente, a tupla existente não é modificada.

## 16. Criando tuplas com `tuple()`

A função embutida `tuple()` pode criar uma tupla a partir de outro iterável. Uma lista é um exemplo já familiar:

```python
topics_list = ["strings", "numbers", "lists"]
topics_tuple = tuple(topics_list)

print(topics_tuple)
print(type(topics_tuple))
```

```text
('strings', 'numbers', 'lists')
<class 'tuple'>
```

A nova tupla contém, na mesma ordem, os itens fornecidos pela lista.

Você ainda não precisa explorar todos os tipos de iterável. Os loops da Fase 4 tornarão esse conceito geral mais concreto.

## 17. `count()` responde quantos

Tuplas oferecem `count()`:

```python
scores = (8, 10, 9, 10, 8, 10)

print(scores.count(10))
print(scores.count(7))
```

```text
3
0
```

`count(value)` retorna quantos itens são iguais ao valor solicitado.

Ele não altera a tupla.

## 18. `index()` encontra a primeira posição correspondente

Tuplas também oferecem `index()`:

```python
topics = ("strings", "numbers", "lists", "numbers")

print(topics.index("numbers"))
```

```text
1
```

Apenas a primeira correspondência igual é retornada.

Se o valor não existir, `index()` gera `ValueError`, assim como ocorre em listas.

## 19. Empacotamento de tupla

Python pode empacotar valores separados por vírgulas em uma tupla:

```python
study_record = "tuples", 45, True

print(study_record)
print(type(study_record))
```

```text
('tuples', 45, True)
<class 'tuple'>
```

Isso é chamado de **empacotamento de tupla**.

Os três valores se tornam um único valor do tipo tupla.

## 20. Desempacotamento de sequência

Uma sequência de tamanho fixo pode ser desempacotada em variáveis separadas:

```python
study_record = ("tuples", 45, True)

topic, minutes, completed = study_record

print(topic)
print(minutes)
print(completed)
```

```text
tuples
45
True
```

Cada variável recebe o item da posição correspondente.

Embora tuplas tornem esse padrão especialmente comum, o desempacotamento também funciona com outras sequências.

## 21. A quantidade de destinos deve corresponder

No desempacotamento básico, a quantidade de variáveis à esquerda precisa corresponder à quantidade de itens da sequência à direita:

```python
study_record = ("tuples", 45, True)

topic, minutes = study_record
```

```text
ValueError: too many values to unpack (expected 2)
```

Materiais posteriores poderão explorar desempacotamento estendido. Por enquanto, mantenha os formatos com o mesmo tamanho.

## 22. Empacotamento e desempacotamento explicam atribuição múltipla

Esta atribuição aparentemente especial:

```python
left = "A"
right = "B"

left, right = right, left

print(left)
print(right)
```

```text
B
A
```

funciona por meio de empacotamento e desempacotamento.

O lado direito produz os valores, e o lado esquerdo os recebe por posição. Python não precisa de uma variável temporária para essa troca.

## 23. Imutabilidade trata das posições da tupla

Uma regra sutil, mas importante: uma tupla pode conter objetos mutáveis.

```python
profile = ("Ana", ["Python"])

profile[1].append("SQL")

print(profile)
```

```text
('Ana', ['Python', 'SQL'])
```

A tupla continua com as mesmas duas posições:

1. a string `"Ana"`;
2. o mesmo objeto lista.

A tupla não substituiu seu segundo item. A lista armazenada naquela posição mudou internamente.

Portanto, "a tupla é imutável" **não** significa que "todo objeto alcançável a partir da tupla é imutável".

## 24. O que ainda falha com um item mutável dentro?

Mesmo quando uma tupla contém uma lista, você ainda não pode substituir essa posição da tupla:

```python
profile = ("Ana", ["Python"])

profile[1] = ["SQL"]
```

```text
TypeError: 'tuple' object does not support item assignment
```

Esse contraste separa duas ideias:

- alterar as posições da tupla;
- alterar um objeto mutável que já está armazenado em uma dessas posições.

A primeira é proibida. A segunda pode ser possível dependendo do próprio tipo do objeto contido.

## 25. Quando uma tupla comunica bem a intenção

Uma tupla é útil quando uma sequência representa uma forma fixa.

Exemplos incluem:

- um par de largura e altura;
- uma coordenada `(x, y)`;
- um resumo fixo como `(topic, minutes, completed)`;
- valores que são naturalmente desempacotados em uma quantidade conhecida de variáveis.

Isso é uma recomendação de design, não uma exigência do Python. Uma lista tecnicamente pode armazenar muitos dos mesmos valores.

Escolha o tipo que melhor comunica como os dados devem se comportar.

## 26. Quando uma lista é mais clara

Prefira uma lista quando se espera que a coleção mude como parte normal do trabalho:

- novos itens serão adicionados;
- itens serão removidos;
- posições serão substituídas;
- a coleção será ordenada ou invertida no próprio objeto;
- a quantidade de itens cresce ou diminui naturalmente.

O capítulo anterior apresentou as ferramentas para essas tarefas.

## 27. Exemplo prático: configurações fixas de exibição

```python
display_size = (1920, 1080)

width, height = display_size

print("Width:", width)
print("Height:", height)
print("Pixels:", width * height)
```

```text
Width: 1920
Height: 1080
Pixels: 2073600
```

O par possui um significado fixo: primeiro largura, depois altura. O desempacotamento dá nomes descritivos a essas posições.

## 28. Exemplo prático: resumo de estudo

```python
study_summary = ("tuples", 50, True)

topic, minutes, completed = study_summary

print("Topic:", topic)
print("Minutes:", minutes)
print("Completed:", completed)
print("Fields:", len(study_summary))
```

```text
Topic: tuples
Minutes: 50
Completed: True
Fields: 3
```

Este é um exemplo compacto de registro com formato fixo sem introduzir dicionários antes da hora. O próximo capítulo mostrará por que chaves frequentemente são mais claras quando os registros ficam mais descritivos.

## 29. Erros comuns

### Esquecer a vírgula em uma tupla de um item

`("Python")` é uma expressão string. `("Python",)` é uma tupla de um item.

### Tentar modificar uma tupla como uma lista

Atribuição por índice e métodos de mutação de listas não estão disponíveis em tuplas.

### Pensar que apenas os parênteses criam qualquer tupla

Em tuplas não vazias, as vírgulas são a sintaxe que define a tupla. Parênteses frequentemente melhoram a clareza e são obrigatórios em alguns contextos.

### Supor que a imutabilidade é profunda

Uma tupla pode conter um objeto mutável, como uma lista, e esse objeto contido ainda pode mudar.

### Esperar que `+` modifique uma tupla existente

A concatenação de tuplas retorna uma nova tupla.

### Desempacotar para a quantidade errada de variáveis

O desempacotamento básico exige que a quantidade de destinos corresponda ao comprimento da sequência.

### Usar uma tupla para uma coleção que naturalmente cresce e diminui

A imutabilidade pode se tornar atrito quando a mutação realmente faz parte do ciclo de vida normal dos dados. Uma lista pode comunicar melhor essa intenção.

## 30. Conexões com conceitos anteriores e posteriores

Este capítulo reutiliza ideias anteriores:

- indexação e slicing funcionam como as operações de sequência aprendidas com strings e listas;
- `len()`, testes de pertencimento, `count()` e `index()` inspecionam o conteúdo da coleção;
- a mutação de listas fornece o contraste que torna a imutabilidade das tuplas concreta;
- conversão de tipos fornece o modelo para `tuple()`.

Ele também prepara materiais posteriores:

- dicionários substituirão o significado baseado em posição por significado baseado em chaves;
- conjuntos focarão unicidade em vez de acesso posicional;
- o último capítulo de Coleções comparará as quatro escolhas;
- loops da Fase 4 percorrerão tuplas assim como outros iteráveis;
- funções da Fase 5 tornarão empacotamento, desempacotamento e formatos imutáveis de dados cada vez mais úteis.

## 31. Exercício: desempacote um registro fixo de aprendizagem

Crie `tuple_practice.py`.

Comece com:

```python
learning_record = ("collections", "tuples", 60, True)
```

Sem usar loops ou condicionais:

1. imprima a tupla;
2. imprima seu comprimento;
3. imprima o primeiro item;
4. imprima o último item;
5. imprima o slice contendo `"tuples"` e `60`;
6. imprima se `"tuples"` está na tupla;
7. desempacote os quatro itens em `phase`, `topic`, `minutes` e `completed`;
8. imprima cada valor desempacotado com um rótulo;
9. crie uma tupla de um item chamada `next_topic` contendo `"dictionaries"`;
10. imprima `next_topic` e seu tipo;
11. concatene `learning_record` e `next_topic` em `extended_record`;
12. imprima as duas tuplas para confirmar que a original não mudou.

Um possível formato de saída final é:

```text
Record: ('collections', 'tuples', 60, True)
Length: 4
First: collections
Last: True
Middle: ('tuples', 60)
Contains tuples: True
Phase: collections
Topic: tuples
Minutes: 60
Completed: True
Next: ('dictionaries',)
Next type: <class 'tuple'>
Extended: ('collections', 'tuples', 60, True, 'dictionaries')
Original: ('collections', 'tuples', 60, True)
```

Tente prever o valor e o tipo de cada expressão antes de executar o arquivo.

## 32. Autoavaliação

Antes de avançar, confirme se você consegue responder estas perguntas:

1. O que torna uma tupla uma sequência?
2. O que imutável significa para uma tupla?
3. Por que `("Python")` não é uma tupla de um item?
4. Como escrever uma tupla vazia?
5. Tuplas podem ser indexadas e fatiadas?
6. O que `count()` e `index()` retornam?
7. O que acontece ao atribuir a `items[0]` se `items` for uma tupla?
8. O que é empacotamento de tupla?
9. O que é desempacotamento de sequência?
10. Por que uma lista armazenada dentro de uma tupla ainda pode mudar?
11. `tuple_a + tuple_b` modifica alguma das tuplas originais?
12. Quando uma lista comunicaria a intenção de forma mais clara do que uma tupla?

Se alguma resposta parecer incerta, altere um dos exemplos e observe o que permanece fixo e o que pode mudar.

## 33. Referência rápida

- Tupla com vários itens: `items = ("a", "b", "c")`
- Tupla vazia: `items = ()`
- Tupla de um item: `items = ("a",)`
- Criar a partir de outro iterável: `items = tuple(values)`
- Ler um item: `items[index]`
- Ler um slice: `items[start:stop]`
- Comprimento: `len(items)`
- Pertencimento: `value in items`
- Contar valores iguais: `items.count(value)`
- Primeira posição igual: `items.index(value)`
- Concatenar em uma nova tupla: `combined = first + second`
- Repetir em uma nova tupla: `repeated = items * 2`
- Empacotar valores: `record = value_a, value_b`
- Desempacotar valores: `value_a, value_b = record`

Lembre-se:

- tuplas são ordenadas;
- tuplas são imutáveis;
- posições de tuplas não podem receber atribuição nem ser excluídas;
- concatenação e repetição de tuplas criam novas tuplas;
- uma vírgula é necessária para uma tupla de um item;
- objetos mutáveis contidos ainda podem sofrer suas próprias alterações internas.

## 34. Para onde ir agora

Agora você consegue comparar os dois tipos posicionais de coleção apresentados até aqui:

1. **Lista:** ordenada e mutável.
2. **Tupla:** ordenada e imutável.

O próximo capítulo de Coleções apresenta **dicionários**, nos quais as posições deixam de ser o principal modelo de consulta. Em vez de pedir o item `0` ou o item `1`, você recuperará valores usando chaves significativas.

---

Referências oficiais usadas para verificação técnica:

- [Python Tutorial: Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Built-in Types: Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Built-in Types: Tuples](https://docs.python.org/3/library/stdtypes.html#tuples)
- [Python Data Model: Tuples](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)
