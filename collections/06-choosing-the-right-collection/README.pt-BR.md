<div align="center">

# Escolhendo a Coleção Certa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Conjuntos e valores únicos](../05-sets-and-unique-values/README.pt-BR.md) · [Voltar ao índice de Coleções](../README.pt-BR.md) · [Ver o roadmap](../../docs/roadmap.pt-BR.md)

Agora você conhece quatro modelos importantes de coleções embutidas: listas, tuplas, dicionários e conjuntos.

A habilidade final desta fase não é memorizar outro método. É aprender a olhar para um problema e perguntar:

**Qual relação existe entre esses valores?**

Essa pergunta é mais útil do que escolher uma coleção apenas porque sua sintaxe parece familiar.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir os Capítulos 01 a 05 de Coleções |
| Tempo estimado de estudo | 90 a 120 minutos |
| Conceitos principais | escolha de coleção, dados posicionais, mutabilidade, mapeamentos chave-valor, unicidade, pertencimento, decisões semânticas, coleções aninhadas |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- comparar listas, tuplas, dicionários e conjuntos pelo propósito;
- identificar quando a posição faz parte do significado dos dados;
- decidir se a própria coleção precisa ser alterada;
- reconhecer quando chaves significativas são mais claras do que posições numéricas;
- reconhecer quando unicidade e pertencimento são centrais;
- explicar por que a ordem de inserção de um dicionário não o transforma em uma sequência posicional;
- explicar por que converter entre tipos de coleção pode alterar o modelo dos dados;
- combinar diferentes tipos de coleção quando relações diferentes existirem em níveis diferentes;
- justificar uma escolha de coleção em linguagem simples;
- entrar na Fase 4 preparado para usar fluxo de programa com coleções que você já compreende.

## 1. Comece pela relação, não pelos colchetes

Estes valores poderiam ser escritos em vários tipos de coleção:

```python
values = ["python", "sql", "git"]
```

```python
values = ("python", "sql", "git")
```

```python
values = {"python", "sql", "git"}
```

Os valores parecem semelhantes, mas os modelos de coleção não são equivalentes.

Antes de escolher, pergunte o que os valores significam em conjunto.

Eles formam uma série ordenada? Uma estrutura posicional fixa? Campos nomeados? Um grupo de membros únicos?

A resposta deve orientar a escolha da coleção.

## 2. Os quatro modelos de coleção

Um resumo útil para iniciantes é:

| Coleção | Modelo principal |
|---|---|
| `list` | posições ordenadas que podem mudar |
| `tuple` | posições ordenadas cuja estrutura da tupla não pode mudar |
| `dict` | chaves mapeadas para valores |
| `set` | membros distintos sem busca posicional |

Essa tabela descreve a relação principal comunicada por cada coleção.

## 3. Um primeiro mapa de decisão

Use estas perguntas em ordem:

```text
Do meaningful keys identify the values?
    yes -> dict
    no
     |
     v
Is uniqueness or membership the central idea?
    yes -> set
    no
     |
     v
Do positions and order matter?
    yes
     |
     v
Should the sequence structure change later?
    yes -> list
    no  -> tuple
```

Isso é um auxílio de aprendizagem, não uma lei completa para todo programa Python. Software real pode ter restrições adicionais.

Para problemas de nível iniciante, porém, essas perguntas fornecem um ponto de partida forte.

Vale explicitar um caso limite: se chaves significativas, pertencimento distinto e ordem posicional receberem resposta não, nenhum desses quatro modelos representa exatamente "ocorrências duplicadas sem ordem". Se ocorrências repetidas precisarem ser preservadas, uma lista é um contêiner prático para iniciantes mesmo quando sua ordem for incidental; deixe claro que a ordem não faz parte do significado dos dados. Se ocorrências repetidas não importarem, reconsidere se um conjunto representa o problema.

## 4. Pergunta um: chaves significativas identificam os valores?

Suponha que você queira representar o nome, a trilha e o nível de uma pessoa estudante.

Uma lista consegue armazenar os valores:

```python
learner = ["Mina", "Python", "beginner"]
```

Mas o significado de cada posição precisa ser lembrado separadamente.

Um dicionário torna os rótulos parte do modelo:

```python
learner = {
    "name": "Mina",
    "track": "Python",
    "level": "beginner",
}
```

Se a pergunta natural for "qual é o valor deste campo?", um dicionário costuma ser a escolha mais clara.

## 5. Ordem de dicionário não é busca posicional

A partir do Python 3.7, preservar a ordem de inserção dos dicionários é uma garantia da linguagem, mas isso não os transforma em listas.

```python
profile = {
    "name": "Mina",
    "track": "Python",
}

print(profile["track"])
```

```text
Python
```

A busca funciona porque `"track"` é uma chave.

`profile[0]` não significa "a primeira entrada", a menos que `0` seja literalmente uma chave naquele dicionário.

Escolha um dicionário pela **relação chave-valor**, não porque deseja posições numeradas.

## 6. Pergunta dois: unicidade é a ideia central?

Suponha que você queira representar nomes de tópicos concluídos e que cada tópico deva aparecer no máximo uma vez.

Um conjunto comunica essa relação diretamente:

```python
completed = {"strings", "lists", "tuples"}

print("lists" in completed)
```

```text
True
```

A pergunta importante é pertencimento: um tópico pertence ao grupo concluído?

Se ocorrências duplicadas ou posições importarem, um conjunto não é o modelo correto.

## 7. Pergunta três: as posições importam?

Uma lista e uma tupla são sequências posicionais.

```python
steps = ["read", "practice", "review"]
checkpoint = (3, 4)

print(steps[0])
print(checkpoint[1])
```

```text
read
4
```

Aqui, a posição possui significado.

Em `steps`, a posição descreve a ordem das atividades. Em `checkpoint`, as duas posições formam uma pequena estrutura fixa semelhante a uma coordenada.

## 8. Pergunta quatro: a estrutura da sequência deve mudar?

Quando posição importa, mutabilidade ajuda a diferenciar listas de tuplas.

Use uma lista quando adicionar, remover ou substituir elementos da sequência fizer parte do trabalho normal:

```python
steps = ["read", "practice"]
steps.append("review")

print(steps)
```

```text
['read', 'practice', 'review']
```

Use uma tupla quando a própria estrutura da sequência deva permanecer fixa:

```python
checkpoint = (3, 4)

print(checkpoint)
```

```text
(3, 4)
```

A imutabilidade da tupla se aplica à estrutura da tupla. Uma tupla ainda pode conter um objeto mutável, como você aprendeu no Capítulo 03.

## 9. Lista versus tupla

Use esta comparação quando as duas opções parecerem razoáveis:

| Pergunta | `list` | `tuple` |
|---|---|---|
| Sequência posicional? | sim | sim |
| Suporta indexação e slicing? | sim | sim |
| A estrutura da sequência pode ser alterada? | sim | não |
| Valores duplicados são permitidos? | sim | sim |
| Intenção típica para iniciante | série ordenada que muda | formato ordenado fixo |

A diferença importante não é colchetes versus parênteses. É se alterar a estrutura da sequência pertence ao modelo.

## 10. Lista versus conjunto

Essas duas coleções aparecem com frequência quando vários valores semelhantes precisam ser armazenados.

Escolha uma lista quando:

- a ordem da sequência importa;
- duplicatas podem carregar informação;
- busca posicional importa;
- a sequência pode mudar.

Escolha um conjunto quando:

- cada membro deve ser distinto;
- pertencimento é central;
- relações de conjunto como interseção ou diferença são úteis;
- posições não fazem parte do significado.

Não substitua uma lista por um conjunto apenas porque a lista contém duplicatas.

## 11. Tupla versus dicionário

Os dois podem representar um pequeno grupo estruturado, mas comunicam significados diferentes.

Uma tupla enfatiza posições:

```python
version = (3, 13)

print(version[0])
```

```text
3
```

Um dicionário enfatiza rótulos:

```python
version = {
    "major": 3,
    "minor": 13,
}

print(version["major"])
```

```text
3
```

Se quem lê precisa lembrar o que a posição `0` significa, chaves significativas podem tornar um dicionário mais claro.

Se o formato posicional em si for significativo e compacto, uma tupla pode ser apropriada.

## 12. Dicionário versus conjunto

Os dois usam chaves em formas literais comuns, mas seus modelos são muito diferentes.

Um dicionário armazena relações chave-valor:

```python
permissions = {
    "read": True,
    "write": False,
}
```

Um conjunto armazena membros:

```python
permissions = {"read", "export"}
```

Pergunte se cada item precisa de um valor associado.

Se sim, um dicionário pode servir. Se o item em si apenas pertence ou não pertence, um conjunto pode servir.

## 13. O comportamento de duplicatas importa

Listas e tuplas preservam posições duplicadas:

```python
items = ["python", "python", "sql"]

print(len(items))
```

```text
3
```

Conjuntos reduzem membros duplicados iguais:

```python
items = {"python", "python", "sql"}

print(len(items))
```

```text
2
```

Dicionários não podem conter duas chaves iguais separadas ao mesmo tempo, embora seus valores possam se repetir.

Se ocorrências repetidas carregarem informação, modele isso deliberadamente em vez de escolher um conjunto automaticamente.

## 14. Hashability importa para dicionários e conjuntos

Chaves de dicionário e elementos de conjunto precisam ser hashable.

Exemplos comuns e seguros para iniciantes incluem strings, inteiros e tuplas cujo conteúdo seja hashable.

Listas não podem ser chaves de dicionário nem elementos de conjuntos comuns porque listas são mutáveis e unhashable.

Esse requisito pode afetar o desenho da coleção, mas não transforme hashing na primeira pergunta de decisão. Comece pela relação entre os valores e depois confira se o modelo escolhido aceita os valores necessários.

## 15. Mutabilidade diz respeito ao objeto coleção

Listas, dicionários e conjuntos comuns são mutáveis.

Tuplas são sequências imutáveis.

Mas objetos aninhados mantêm seu próprio comportamento.

Por exemplo:

```python
record = (
    "Mina",
    ["strings", "lists"],
)

record[1].append("tuples")

print(record)
```

```text
('Mina', ['strings', 'lists', 'tuples'])
```

A estrutura da tupla não mudou. A lista armazenada dentro dela mudou.

Por isso, "tupla significa que nada dentro pode mudar" é um modelo mental incorreto.

## 16. Um programa pode precisar das quatro coleções

Relações diferentes podem existir em níveis diferentes do mesmo problema.

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
}
planned_topics = ["lists", "tuples", "dictionaries", "sets"]
checkpoint = (3, 4)
completed_topics = {"lists", "tuples"}
```

Cada coleção comunica algo diferente:

- `course` usa campos nomeados;
- `planned_topics` é uma série ordenada que pode crescer;
- `checkpoint` é um par posicional fixo;
- `completed_topics` é um grupo de membros distintos.

Usar vários tipos de coleção juntos é normal quando as relações entre os dados são diferentes.

## 17. Coleções aninhadas não são automaticamente avançadas

Uma coleção pode conter outra coleção quando isso representa bem os dados.

```python
student = {
    "name": "Mina",
    "topics": ["strings", "lists"],
}
```

O dicionário externo responde "qual campo?".

A lista interna responde "quais itens de tópicos ordenados?".

Escolha cada nível separadamente. Não force um único tipo de coleção a representar todas as relações de uma estrutura maior.

## 18. Os mesmos valores podem justificar modelos diferentes

Considere os valores `"python"`, `"sql"` e `"git"`.

Se eles representarem uma sequência de estudos:

```python
skills = ["python", "sql", "git"]
```

Se representarem um snapshot posicional fixo de três partes:

```python
skills = ("python", "sql", "git")
```

Se representarem habilidades concluídas e únicas:

```python
skills = {"python", "sql", "git"}
```

Os valores sozinhos não determinam a coleção. A **relação e as operações pretendidas** determinam.

## 19. Converter tipos altera o modelo

O Python permite converter entre formas de coleção compatíveis, mas a conversão não é apenas cosmética.

```python
entries = ["python", "sql", "python"]
unique_entries = set(entries)

print(len(entries))
print(len(unique_entries))
```

```text
3
2
```

O conjunto não representa mais as posições duplicadas da lista.

Converter novamente para uma lista não recria a informação que foi descartada.

Não converta tipos de coleção apenas para obter colchetes diferentes na saída.

## 20. Não escolha pela familiaridade da sintaxe

Um hábito comum de iniciante é usar listas para tudo porque listas são aprendidas primeiro.

Outro é usar a coleção que tiver o literal mais curto.

Os dois hábitos escondem o significado dos dados.

Prefira este raciocínio:

- "Preciso de posições ordenadas que irão mudar, então escolhi uma lista."
- "Preciso de uma estrutura posicional fixa, então escolhi uma tupla."
- "Preciso de valores identificados por nomes, então escolhi um dicionário."
- "Preciso de pertencimento distinto, então escolhi um conjunto."

Uma explicação curta assim é um ótimo hábito de desenho.

## 21. Não escolha apenas por um método que você lembra

Suponha que você lembre bem de `append()`. Isso não torna uma lista automaticamente apropriada.

Suponha que você lembre que conjuntos removem duplicatas. Isso não significa que toda entrada com duplicatas deva virar conjunto.

Métodos são operações disponíveis **depois** que um modelo de dados foi escolhido.

Escolha primeiro a relação e depois use as operações pertencentes àquela coleção.

## 22. Uma tabela prática de comparação

| Necessidade | Primeiro candidato forte |
|---|---|
| Série ordenada que vai mudar | `list` |
| Sequência posicional fixa | `tuple` |
| Campos ou identificadores nomeados | `dict` |
| Membros distintos e testes de pertencimento | `set` |
| Ocorrências duplicadas precisam permanecer | `list` ou `tuple` |
| Chave associada a um valor | `dict` |
| União/interseção/diferença entre grupos | `set` |
| Posição numérica faz parte do significado | `list` ou `tuple` |

"Primeiro candidato forte" é uma escolha de palavras deliberada. O desenho de software pode envolver mais contexto do que uma única tabela consegue representar.

## 23. Cenário: etapas de compra

Imagine estas etapas:

1. escolher itens;
2. revisar carrinho;
3. pagar.

Se o programa precisa preservar essa ordem e talvez inserir outra etapa depois, uma lista é um modelo natural:

```python
steps = ["choose items", "review cart", "pay"]
```

A posição e a capacidade de alterar a sequência importam.

## 24. Cenário: uma coordenada

Uma coordenada de duas partes possui um pequeno formato posicional fixo:

```python
point = (10, 20)
```

A primeira e a segunda posições possuem papéis definidos, e alterar a quantidade de partes da coordenada não é a operação normal.

Uma tupla comunica bem esse formato fixo de sequência.

## 25. Cenário: um perfil

Um perfil possui campos nomeados:

```python
profile = {
    "name": "Mina",
    "level": "beginner",
}
```

Os rótulos são mais significativos do que dizer que o nome deve sempre ser lembrado como item `0`.

Um dicionário torna explícita a relação entre campos.

## 26. Cenário: recursos suportados

Suponha que a pergunta importante seja se um recurso pertence a um grupo suportado:

```python
supported = {"export", "search", "sync"}

print("search" in supported)
```

```text
True
```

Um conjunto comunica pertencimento distinto diretamente.

## 27. Exemplo prático: quatro modelos juntos

O exemplo aprovado `collection_models.py` usa uma coleção para cada relação:

```python
tasks = ["read", "practice", "review"]
checkpoint = (3, 4)
profile = {"name": "Mina", "track": "Python"}
completed = {"strings", "lists", "tuples"}

print(tasks[0])
print(checkpoint[1])
print(profile["track"])
print("lists" in completed)
```

```text
read
4
Python
True
```

A sintaxe difere porque as perguntas diferem.

## 28. Exemplo prático: decisões de mutabilidade

`collection_tradeoffs.py` reforça quais estruturas externas de coleção podem mudar:

```python
planned_topics = ["strings", "lists", "tuples"]
fixed_version = (3, 13)
student = {"name": "Mina", "active": False}
skills = {"python", "git"}

planned_topics.append("dictionaries")
student["active"] = True
skills.add("sql")

print(len(planned_topics))
print(fixed_version[0])
print(student["active"])
print("sql" in skills)
```

```text
4
3
True
True
```

A tupla é lida por posição, mas sua estrutura não é alterada.

## 29. Exemplo prático: um pequeno espaço de estudos

`study_workspace.py` combina os modelos de coleção em um programa fictício:

```python
course = {
    "title": "Python Study Guide",
    "phase": 3,
}
planned_topics = ["lists", "tuples", "dictionaries", "sets"]
checkpoint = (3, 4)
completed_topics = {"lists", "tuples"}

planned_topics.append("collection choices")
course["status"] = "in progress"
completed_topics.add("dictionaries")

print(course["title"])
print(planned_topics[0])
print(checkpoint)
print("dictionaries" in completed_topics)
print(len(completed_topics))
```

```text
Python Study Guide
lists
(3, 4)
True
3
```

Nenhuma coleção está competindo com as outras. Cada uma cuida de uma relação diferente.

## 30. Erros comuns

### Usar uma lista para todo problema

Listas são flexíveis, mas flexibilidade não as torna o modelo mais claro para campos nomeados ou pertencimento único.

### Usar uma tupla apenas porque os dados são curtos

O comprimento sozinho não determina se uma tupla é adequada. A pergunta importante é se uma sequência posicional fixa faz sentido.

### Tratar a ordem de inserção do dicionário como indexação de lista

Dicionários preservam ordem de inserção, mas a busca direta é por chave.

### Usar um conjunto quando ocorrências duplicadas importam

Um conjunto remove pertencimento duplicado igual. Isso pode descartar informação.

### Escolher um conjunto porque seus testes de pertencimento parecem atraentes

Primeiro confirme se pertencimento distinto e não posicional corresponde ao próprio problema.

### Assumir que a imutabilidade da tupla congela objetos aninhados

A estrutura da tupla é imutável. Objetos mutáveis armazenados dentro dela mantêm seu próprio comportamento.

### Converter coleções sem considerar o significado perdido

Alterar o tipo pode mudar o tratamento de duplicatas, o comportamento posicional, a mutabilidade ou a forma de busca.

### Forçar um tipo de coleção em todos os níveis de aninhamento

Escolha cada nível conforme a relação existente naquele nível.

## 31. Checklist para escolher uma coleção

Antes de escrever o literal da coleção, pergunte:

1. Os valores são identificados por nomes ou chaves significativas?
2. Pertencimento distinto é a relação principal?
3. Posições numéricas importam?
4. A ordem da sequência importa?
5. A coleção externa deve mudar depois?
6. Ocorrências duplicadas precisam ser preservadas?
7. As chaves de dicionário ou elementos de conjunto desejados atendem aos requisitos de hashability?
8. Outra pessoa entenderia a relação observando o tipo escolhido?

Você nem sempre precisará das oito perguntas, mas elas tornam suposições escondidas visíveis.

## 32. Exercício: escolha antes de programar

Para cada cenário, escolha `list`, `tuple`, `dict` ou `set` e escreva uma frase explicando o motivo.

1. Uma fila de leitura ordenada que receberá novos livros.
2. Um par fixo `(width, height)`.
3. Um tema de interface com configurações nomeadas como `"font_size"` e `"dark_mode"`.
4. Um grupo de nomes únicos de recursos habilitados.
5. Os resultados ordenados de três tentativas em que pontuações repetidas precisam permanecer.
6. Um trio RGB fixo como `(255, 128, 0)`.
7. Um registro de produto identificado por campos como `"name"`, `"price"` e `"available"`.
8. Dois grupos cujos membros compartilhados precisam ser comparados com interseção.
9. Uma sequência de títulos de aulas que poderá ser reordenada depois.
10. Um pequeno par fixo representando uma posição inicial e final.

Depois, crie `collection_choice_practice.py` contendo um exemplo original de cada tipo de coleção. Não use loops nem condicionais.

Para cada variável, acrescente uma breve explicação escrita abaixo do código dizendo por que aquela coleção corresponde à relação.

## 33. Extensão do exercício: combine os modelos

Crie um planejador fictício de estudos com:

- um dicionário para informações nomeadas do curso;
- uma lista para tópicos planejados em ordem;
- uma tupla para um checkpoint fixo de dois números;
- um conjunto para tópicos concluídos únicos.

Execute pelo menos uma operação segura para iniciantes e apropriada a cada coleção.

Exemplos de operações apropriadas incluem:

- ler um valor de dicionário por chave;
- adicionar um item à lista;
- ler uma posição da tupla;
- testar pertencimento no conjunto.

O objetivo não é usar todos os métodos. O objetivo é deixar evidente o papel de cada coleção.

## 34. Autoavaliação

Antes de concluir a Fase 3, confirme se você consegue responder estas perguntas:

1. Qual relação uma lista comunica melhor?
2. Qual diferença estrutural importante separa uma tupla de uma lista?
3. Quando chaves de dicionário são mais claras do que posições numéricas?
4. Qual relação é central em um conjunto?
5. Dicionários preservam a ordem de inserção?
6. Isso transforma dicionários em sequências indexadas por posição?
7. Quais tipos de coleção preservam ocorrências duplicadas naturalmente?
8. Por que converter uma lista para conjunto pode descartar informação?
9. O que chaves de dicionário e elementos de conjunto precisam satisfazer?
10. Uma tupla pode conter um objeto mutável?
11. Por que um programa pode usar os quatro tipos de coleção?
12. O que você deve perguntar antes de escolher pela sintaxe?

Se alguma resposta estiver incerta, volte ao capítulo que apresentou aquela coleção e altere um exemplo por conta própria.

## 35. Referência rápida

- Sequência ordenada que muda: `list`
- Estrutura de sequência posicional fixa: `tuple`
- Relações chave-valor significativas: `dict`
- Grupo de pertencimento com membros distintos: `set`
- Listas, tuplas e strings suportam operações posicionais de sequência.
- Dicionários usam chaves para busca direta.
- Conjuntos não oferecem indexação posicional nem slicing.
- Listas, dicionários e conjuntos comuns são mutáveis.
- A estrutura da tupla é imutável.
- Chaves de dicionário e elementos de conjunto precisam ser hashable.
- Ocorrências duplicadas continuam significativas em listas e tuplas.
- Membros de conjuntos são distintos.
- Chaves de dicionário são únicas, enquanto valores de dicionário podem se repetir.
- Conversão entre tipos de coleção pode alterar o modelo dos dados.
- Estruturas aninhadas podem usar tipos de coleção diferentes em níveis diferentes.

## 36. Modelo mental da Fase 3

Toda a fase de Coleções agora pode ser resumida assim:

```text
list  -> ordered positions that can change
tuple -> ordered positions with an immutable tuple structure
dict  -> key -> value relationships
set   -> distinct membership without positional lookup
```

E a regra final de desenho é:

**Escolha a coleção que torna a relação entre os valores mais fácil de entender.**

## 37. Para onde ir agora

Você concluiu os principais modelos de coleção da Fase 3.

A Fase 4 apresenta **fluxo de programa**: `if`, `elif`, `else`, `for`, `while` e ferramentas relacionadas.

Essa próxima fase ficará muito mais fácil porque loops e condições atuarão sobre estruturas de coleção cujo significado você já compreende.

Em vez de aprender "como fazer loop sobre colchetes misteriosos", você saberá o que a coleção representa antes de controlar como o programa se move por ela.

---

Referências oficiais usadas para verificação técnica:

- [Tutorial do Python: Estruturas de Dados](https://docs.python.org/pt-br/3/tutorial/datastructures.html)
- [Tipos embutidos do Python](https://docs.python.org/pt-br/3/library/stdtypes.html)
