<div align="center">

# Conjuntos e Valores Únicos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Capítulo anterior: Dicionários: chaves e valores](../04-dictionaries-keys-and-values/README.pt-BR.md) · [Voltar ao índice de Coleções](../README.pt-BR.md) · [Próximo capítulo: Escolhendo a coleção certa →](../06-choosing-the-right-collection/README.pt-BR.md)

Listas e tuplas organizam valores por posição. Dicionários organizam valores por chaves. Conjuntos apresentam outro modelo: um valor **pertence à coleção ou não pertence**.

Esse modelo é especialmente útil quando unicidade importa, quando você quer testar pertencimento ou quando deseja comparar grupos de valores.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir os Capítulos 01 a 04 de Coleções |
| Tempo estimado de estudo | 120 a 150 minutos |
| Conceitos principais | `set`, elementos únicos, pertencimento, elementos hashable, `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`, união, interseção, diferença, diferença simétrica, subconjunto, superconjunto, conjuntos disjuntos, cópia |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que torna um conjunto diferente de listas, tuplas e dicionários;
- criar conjuntos vazios e preenchidos;
- explicar por que valores duplicados se reduzem a um único elemento do conjunto;
- converter outro iterável em um conjunto com `set()`;
- explicar por que conjuntos não suportam indexação posicional ou slicing;
- contar elementos com `len()`;
- testar pertencimento com `in` e `not in`;
- adicionar um elemento com `add()`;
- adicionar vários elementos com `update()`;
- distinguir `remove()` de `discard()`;
- explicar por que `pop()` não significa "remover o último item" em um conjunto;
- esvaziar um conjunto;
- reconhecer quais valores podem ser elementos de um conjunto;
- calcular união, interseção, diferença e diferença simétrica;
- testar relações de subconjunto, superconjunto e conjuntos disjuntos;
- distinguir outra referência ao mesmo conjunto de uma cópia rasa;
- escolher um conjunto quando unicidade ou pertencimento forem mais importantes do que posição.

## 1. De chaves para pertencimento

O capítulo anterior usou chaves significativas de dicionário:

```python
profile = {
    "name": "Ana",
    "track": "Python",
}

print("track" in profile)
```

```text
True
```

Em um dicionário, o pertencimento testa as chaves por padrão.

Um conjunto remove completamente a relação chave-valor:

```python
topics = {"strings", "lists", "dictionaries"}

print("lists" in topics)
print("files" in topics)
```

```text
True
False
```

Não existe um valor armazenado "sob" `"lists"`. O próprio valor `"lists"` é um elemento do conjunto.

Essa é a ideia central de um conjunto:

**valor → pertence ou não pertence**

## 2. O que é um conjunto

O tipo mutável de conjunto embutido do Python é `set`.

Um conjunto é uma coleção não ordenada de **elementos distintos e hashable**.

```python
skills = {"python", "sql", "git"}

print(type(skills))
print(len(skills))
```

```text
<class 'set'>
3
```

Três ideias importam imediatamente:

- **distintos:** elementos iguais não aparecem como duplicatas separadas;
- **não ordenado:** um conjunto não fornece ordenação posicional para busca;
- **elementos hashable:** cada elemento precisa ser adequado para busca de pertencimento em conjunto.

O capítulo de dicionários já apresentou o significado prático de *hashable*. Conjuntos reutilizam o mesmo requisito para seus elementos.

## 3. Sintaxe de literal de conjunto

Um literal de conjunto não vazio usa chaves com elementos separados por vírgulas:

```python
languages = {"Python", "JavaScript", "SQL"}
```

Isso lembra as chaves de um dicionário, mas não existem pares `key: value`.

Compare os formatos:

```python
mapping = {"language": "Python"}
collection = {"Python"}

print(type(mapping))
print(type(collection))
```

```text
<class 'dict'>
<class 'set'>
```

Os dois-pontos são a pista visual de que o primeiro objeto contém uma entrada de dicionário.

## 4. Um conjunto vazio usa `set()`

Chaves vazias criam um dicionário vazio, não um conjunto vazio:

```python
empty_braces = {}
empty_set = set()

print(type(empty_braces))
print(type(empty_set))
```

```text
<class 'dict'>
<class 'set'>
```

Essa é uma das diferenças de sintaxe mais importantes para lembrar neste capítulo.

Use:

```python
items = set()
```

quando precisar de um conjunto vazio.

## 5. Valores duplicados se reduzem

Um conjunto armazena elementos distintos. Repetir um valor igual não cria outro elemento separado:

```python
topics = {"lists", "sets", "lists", "sets", "tuples"}

print(len(topics))
print("lists" in topics)
print("tuples" in topics)
```

```text
3
True
True
```

O conjunto possui três elementos distintos, mesmo que cinco valores tenham sido escritos no literal.

Isso torna conjuntos úteis quando a pergunta é "quais valores únicos estão presentes?" em vez de "quantas vezes cada valor foi informado?".

## 6. Igualdade depende dos membros, não da ordem escrita

Dois conjuntos são iguais quando contêm os mesmos elementos:

```python
first = {"python", "sql", "git"}
second = {"git", "python", "sql"}

print(first == second)
```

```text
True
```

Não interprete isso como se conjuntos "lembrassem uma ordem diferente e a ignorassem depois". Um conjunto não fornece ordem posicional de sequência em primeiro lugar.

## 7. Conjuntos não suportam indexação

Listas e tuplas suportam busca por posição:

```python
items = ["python", "sql", "git"]
print(items[0])
```

```text
python
```

Um conjunto não suporta:

```python
items = {"python", "sql", "git"}
print(items[0])
```

O segundo exemplo gera `TypeError` porque conjuntos não são sequências subscritíveis.

Se seu programa precisa de um item "primeiro", "segundo" ou "terceiro" estável, um conjunto normalmente é o modelo de coleção errado.

## 8. Conjuntos não suportam slicing

Slicing descreve um intervalo posicional, então também não se aplica a conjuntos:

```python
items = {"python", "sql", "git"}
print(items[0:2])
```

O Python gera `TypeError` porque um conjunto não possui uma fatia posicional para recuperar.

Esse é um contraste importante com strings, listas e tuplas.

## 9. Não dependa da ordem exibida por um conjunto

Como conjuntos não definem posição nem ordem de inserção, o código não deve depender da ordem em que vários elementos aparecem quando o conjunto é exibido.

Por exemplo, isto cria um conjunto válido:

```python
skills = {"python", "sql", "git"}
```

Mas este guia não associa uma saída fixa de `print(skills)` com vários elementos a esse exemplo.

Quando os exemplos precisarem de verificação determinística, usarão pertencimento, comprimento, igualdade ou outro resultado cujo significado não dependa da ordem de exibição.

## 10. Criando um conjunto a partir de outro iterável

O construtor `set()` pode coletar elementos distintos de outro iterável.

A partir de uma lista:

```python
languages = ["Python", "SQL", "Python", "Git"]
unique_languages = set(languages)

print(len(unique_languages))
print(unique_languages == {"Python", "SQL", "Git"})
```

```text
3
True
```

A lista original continua contendo seus valores originais. `set(languages)` cria um novo conjunto.

## 11. Convertendo uma string para conjunto

Uma string é iterável, então `set()` pode ler seus caracteres:

```python
letters = set("banana")

print(len(letters))
print("b" in letters)
print("n" in letters)
print("z" in letters)
```

```text
3
True
True
False
```

Os caracteres distintos são `"b"`, `"a"` e `"n"`, mas o conjunto não deve ser tratado como uma sequência de caracteres com posições.

## 12. Usando `len()` com um conjunto

`len()` retorna a quantidade de elementos distintos armazenados no momento:

```python
permissions = {"read", "write", "export"}

print(len(permissions))
```

```text
3
```

Adicionar uma duplicata não aumenta essa quantidade.

## 13. Pertencimento é uma operação natural de conjuntos

Use `in` e `not in` para testar pertencimento:

```python
completed = {"strings", "lists", "tuples"}

print("lists" in completed)
print("sets" not in completed)
```

```text
True
True
```

Testar pertencimento é uma das principais razões pelas quais conjuntos são úteis.

## 14. Adicionando um elemento com `add()`

Conjuntos são mutáveis. Use `add()` para adicionar um elemento:

```python
skills = {"python", "sql"}

skills.add("git")

print("git" in skills)
print(len(skills))
```

```text
True
3
```

Chamar `add()` com um elemento que já está presente não altera o pertencimento:

```python
skills.add("python")
print(len(skills))
```

```text
3
```

`add()` altera o conjunto in-place e retorna `None`.

## 15. Adicionando vários elementos com `update()`

Use `update()` quando outro iterável contém vários valores que você deseja adicionar:

```python
skills = {"python"}

skills.update(["sql", "git", "python"])

print(len(skills))
print(skills == {"python", "sql", "git"})
```

```text
3
True
```

`update()` adiciona os elementos do iterável. Ele não adiciona a própria lista como um único elemento.

Assim como `dict.update()`, `set.update()` altera o objeto existente e retorna `None`.

## 16. `add()` e `update()` significam coisas diferentes

Compare estas intenções:

```python
skills = {"python"}
skills.add("sql")
```

`add()` recebe um elemento.

```python
skills = {"python"}
skills.update(["sql", "git"])
```

`update()` lê elementos de um iterável e os adiciona individualmente.

Com strings, essa diferença importa:

```python
letters = set()
letters.add("ab")

print("ab" in letters)
print(len(letters))
```

```text
True
1
```

Mas:

```python
letters = set()
letters.update("ab")

print("a" in letters)
print("b" in letters)
print(len(letters))
```

```text
True
True
2
```

O primeiro conjunto contém um elemento string, `"ab"`. O segundo recebe os dois caracteres da string iterável.

## 17. Removendo um elemento com `remove()`

`remove(element)` exclui um elemento que precisa estar presente:

```python
skills = {"python", "sql", "git"}

skills.remove("git")

print("git" in skills)
print(len(skills))
```

```text
False
2
```

Se o elemento solicitado estiver ausente, `remove()` gera `KeyError`.

Use `remove()` quando a ausência deve ser tratada como erro em vez de ser ignorada silenciosamente.

## 18. Removendo de forma tolerante com `discard()`

`discard(element)` remove o elemento se ele estiver presente, mas não gera `KeyError` quando estiver ausente:

```python
skills = {"python", "sql"}

skills.discard("git")
skills.discard("sql")

print(skills == {"python"})
```

```text
True
```

Isso torna `discard()` útil quando "já estar ausente" é um estado aceitável.

## 19. `remove()` versus `discard()`

Os dois métodos podem remover um elemento presente. O comportamento para elemento ausente é a diferença importante:

| Método | Elemento presente | Elemento ausente |
|---|---|---|
| `remove(value)` | remove | gera `KeyError` |
| `discard(value)` | remove | deixa o conjunto inalterado |

Os dois métodos alteram o conjunto in-place e retornam `None`; nenhum deles retorna o elemento removido.

Escolha com base em a ausência do valor dever ou não ser considerada excepcional naquela operação.

## 20. `pop()` remove um elemento arbitrário

`set.pop()` remove e retorna um elemento **arbitrário**.

Não transfira para conjuntos o significado de `pop()` das listas. Um conjunto não possui posição de "último elemento".

Um conjunto com um único elemento fornece um exemplo iniciante determinístico:

```python
status = {"ready"}
removed = status.pop()

print(removed)
print(len(status))
```

```text
ready
0
```

Em um conjunto com vários elementos, seu programa não deve depender de qual elemento `pop()` escolhe.

Chamar `pop()` em um conjunto vazio gera `KeyError`.

## 21. Esvaziando um conjunto

`clear()` remove todos os elementos mantendo o objeto conjunto:

```python
skills = {"python", "sql", "git"}

skills.clear()

print(skills)
print(len(skills))
```

```text
set()
0
```

Observe como o Python exibe um conjunto vazio como `set()`, reforçando também por que `{}` não pode representar um conjunto vazio.

`clear()` altera o conjunto in-place e retorna `None`.

## 22. Elementos de conjunto precisam ser hashable

A mesma regra prática das chaves de dicionário se aplica aos elementos de conjuntos.

Elementos comuns e seguros para iniciantes incluem:

- strings;
- inteiros;
- números de ponto flutuante;
- Booleanos;
- tuplas cujo conteúdo seja hashable.

Listas, dicionários e conjuntos comuns são mutáveis e unhashable, portanto não podem ser elementos de um conjunto.

Isto funciona:

```python
points = {(10, 20), (30, 40)}

print((10, 20) in points)
```

```text
True
```

Isto não funciona:

```python
invalid = {[10, 20]}
```

O Python gera `TypeError` ao tentar usar a lista como elemento de conjunto.

## 23. Um conjunto normalmente não pode conter outro conjunto

Um `set` comum é mutável e, por isso, unhashable:

```python
outer = set()
inner = {"python", "sql"}

outer.add(inner)
```

O Python gera `TypeError` porque `inner` é um conjunto comum.

O Python também fornece `frozenset`, um tipo de conjunto imutável e hashable. Ele pode ser usado quando um valor semelhante a conjunto e imutável precisa se tornar chave de dicionário ou elemento de outro conjunto:

```python
frozen_skills = frozenset({"python", "sql"})
groups = {frozen_skills}

print(frozen_skills in groups)
```

```text
True
```

Este capítulo se concentra em `set` mutável comum. Por enquanto, reconheça `frozenset` como a contraparte imutável, e não como uma nova coleção que você precisa dominar em profundidade.

## 24. União combina membros

A união de dois conjuntos contém todos os elementos que aparecem em qualquer um deles.

Use `union()`:

```python
backend = {"python", "sql"}
data = {"python", "pandas"}

combined = backend.union(data)

print(combined == {"python", "sql", "pandas"})
print(backend == {"python", "sql"})
```

```text
True
True
```

`union()` cria um novo conjunto. Ele não altera `backend` neste exemplo.

O operador `|` expressa a mesma união quando os dois operandos são conjuntos:

```python
combined = backend | data
```

## 25. Interseção mantém membros compartilhados

A interseção contém elementos presentes nos dois conjuntos:

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

shared = backend.intersection(data)

print(shared == {"python", "sql"})
```

```text
True
```

O operador `&` é a forma de operador de conjunto:

```python
shared = backend & data
```

Pense na interseção como a resposta para: **o que esses grupos têm em comum?**

## 26. Diferença mantém membros de apenas um lado

A diferença entre conjuntos é direcional.

`A - B` significa "elementos em A que não estão em B":

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

backend_only = backend.difference(data)
data_only = data.difference(backend)

print(backend_only == {"git"})
print(data_only == {"pandas"})
```

```text
True
True
```

A forma com operador é:

```python
backend_only = backend - data
```

Inverter os operandos pode alterar o resultado.

## 27. Diferença simétrica mantém membros não compartilhados

A diferença simétrica contém elementos que aparecem em um dos conjuntos, mas não nos dois:

```python
backend = {"python", "sql", "git"}
data = {"python", "sql", "pandas"}

exclusive = backend.symmetric_difference(data)

print(exclusive == {"git", "pandas"})
```

```text
True
```

A forma com operador usa `^`:

```python
exclusive = backend ^ data
```

Pense assim: **quais membros pertencem exatamente a um dos dois grupos?**

## 28. Um mapa compacto de operações

Para dois conjuntos `a` e `b`:

| Pergunta | Método | Operador |
|---|---|---|
| Tudo de qualquer conjunto | `a.union(b)` | `a | b` |
| Compartilhado pelos dois | `a.intersection(b)` | `a & b` |
| Em `a`, não em `b` | `a.difference(b)` | `a - b` |
| Em exatamente um conjunto | `a.symmetric_difference(b)` | `a ^ b` |

As formas com métodos costumam ser mais fáceis de ler durante o aprendizado inicial. Os operadores são compactos quando as relações já estão familiares.

## 29. Subconjuntos

Um conjunto é subconjunto de outro quando todos os seus elementos estão contidos no outro conjunto.

```python
core = {"python", "sql"}
all_skills = {"python", "sql", "git", "testing"}

print(core.issubset(all_skills))
print(core <= all_skills)
```

```text
True
True
```

`<=` permite igualdade também. `<` significa **subconjunto próprio**, portanto os conjuntos não podem ser iguais.

## 30. Superconjuntos

Um conjunto é superconjunto quando contém todos os elementos de outro conjunto:

```python
core = {"python", "sql"}
all_skills = {"python", "sql", "git", "testing"}

print(all_skills.issuperset(core))
print(all_skills >= core)
```

```text
True
True
```

`>` significa superconjunto próprio, exigindo que os conjuntos sejam diferentes.

Relações de subconjunto e superconjunto descrevem contenção, não apenas tamanho numérico.

## 31. Conjuntos disjuntos

Dois conjuntos são disjuntos quando não possuem elementos em comum:

```python
frontend = {"html", "css"}
backend = {"python", "sql"}

print(frontend.isdisjoint(backend))
```

```text
True
```

Se a interseção deles é vazia, os conjuntos são disjuntos.

Isso é útil quando você precisa perguntar se dois grupos se sobrepõem de alguma forma.

## 32. Métodos de conjunto versus operadores

As formas com métodos de união, interseção, diferença e diferença simétrica aceitam iteráveis apropriados como argumentos.

As formas com operadores como `|`, `&`, `-` e `^` exigem operandos semelhantes a conjuntos.

Para código iniciante, usar dois conjuntos reais dos dois lados mantém a intenção clara:

```python
first = {"python", "sql"}
second = {"sql", "git"}
shared = first & second

print(shared == {"sql"})
```

```text
True
```

Não memorize agora todas as variações de entrada aceitas. A ideia importante é a relação entre conjuntos que cada operação representa.

## 33. Outro nome não é uma cópia

Conjuntos são mutáveis, então o compartilhamento de referência funciona da mesma forma vista em listas e dicionários:

```python
original = {"python", "sql"}
alias = original

alias.add("git")

print("git" in original)
print(original is alias)
```

```text
True
True
```

As duas variáveis se referem ao mesmo objeto conjunto.

## 34. Criando uma cópia rasa

Use `copy()` quando precisar de um objeto conjunto externo separado:

```python
original = {"python", "sql"}
copied = original.copy()

copied.add("git")

print("git" in original)
print("git" in copied)
print(original is copied)
```

```text
False
True
False
```

`set.copy()` é uma cópia rasa. Em conjuntos comuns para iniciantes, os próprios elementos já precisam ser hashable, então a lição principal aqui é que o objeto conjunto externo é separado.

## 35. Removendo duplicatas de outra coleção

Converter para conjunto é uma forma compacta de obter valores únicos:

```python
entries = ["python", "sql", "python", "git", "sql"]
unique_entries = set(entries)

print(len(unique_entries))
print(unique_entries == {"python", "sql", "git"})
```

```text
3
True
```

Mas converter para conjunto também abandona posições de sequência e não preserva um contrato de ordenação no estilo de listas.

Se a ordem original ou a contagem de duplicatas importarem, não substitua a coleção original por um conjunto apenas porque existem duplicatas.

## 36. Quando um conjunto é uma boa escolha

Um conjunto costuma ser uma boa escolha quando:

- cada elemento deve aparecer no máximo uma vez;
- pertencimento é uma pergunta central;
- você precisa comparar grupos por união ou interseção;
- precisa encontrar valores presentes em um grupo e ausentes em outro;
- busca posicional não faz parte do problema.

Por exemplo, um conjunto pode representar nomes de tópicos concluídos:

```python
completed_topics = {"strings", "lists", "tuples"}
```

O significado é "esses tópicos pertencem ao grupo concluído", e não "strings é o item 0".

## 37. Quando um conjunto não é uma boa escolha

Evite escolher um conjunto quando:

- posição ou slicing importam;
- ocorrências duplicadas carregam informação;
- você precisa de relações chave-valor;
- seus elementos necessários são objetos mutáveis e unhashable, como listas;
- seu programa depende de uma ordem de sequência estável.

A coleção deve representar a relação entre os valores, não apenas usar a sintaxe mais curta.

## 38. Exemplo prático: comparar tópicos de aprendizagem

Suponha que duas trilhas fictícias de estudo compartilhem alguns tópicos e sejam diferentes em outros:

```python
python_track = {"python", "sql", "git", "testing"}
data_track = {"python", "sql", "pandas", "statistics"}

shared = python_track & data_track
python_only = python_track - data_track
data_only = data_track - python_track
all_topics = python_track | data_track

print("Shared is correct:", shared == {"python", "sql"})
print("Python-only is correct:", python_only == {"git", "testing"})
print("Data-only is correct:", data_only == {"pandas", "statistics"})
print("Total unique topics:", len(all_topics))
print("Python is shared:", "python" in shared)
```

```text
Shared is correct: True
Python-only is correct: True
Data-only is correct: True
Total unique topics: 6
Python is shared: True
```

O exemplo verifica deliberadamente pertencimento e igualdade em vez de depender da ordem exibida pelo conjunto.

## 39. Erros comuns

### Usar `{}` para um conjunto vazio

`{}` cria um dicionário vazio. Use `set()` para um conjunto vazio.

### Esperar que duplicatas permaneçam

Um conjunto armazena elementos distintos. Duplicatas iguais se reduzem a uma única entrada de pertencimento.

### Tentar ler `set[0]`

Conjuntos não suportam indexação posicional.

### Tentar fazer slicing em um conjunto

Slicing exige posições de sequência. Conjuntos não as possuem.

### Depender da ordem de exibição

A ordem exibida por um conjunto não é um contrato posicional nem de inserção. Não escreva lógica que dependa dela.

### Usar `add()` quando você quer `update()`

`add()` adiciona um elemento. `update()` lê elementos de um iterável.

### Assumir que `remove()` ignora silenciosamente valores ausentes

`remove()` gera `KeyError` quando o elemento está ausente. `discard()` não gera.

### Tratar `pop()` como `list.pop()`

`set.pop()` remove um elemento arbitrário, não o "último".

### Adicionar uma lista ou conjunto como elemento

Elementos de conjunto precisam ser hashable. Listas e conjuntos comuns não são.

### Assumir que converter para `set` só remove duplicatas

Isso também muda o modelo da coleção. Você perde o comportamento posicional de sequência.

### Confundir a direção da diferença

`a - b` significa "membros de `a` que não estão em `b`". Inverter os operandos pode alterar o resultado.

### Esquecer que atribuição compartilha o mesmo conjunto

`alias = original` não copia um conjunto mutável.

## 40. Conexões com conceitos anteriores e posteriores

Este capítulo reutiliza ideias que você já conhece:

- operadores de pertencimento de strings, listas, tuplas e dicionários;
- mutabilidade de listas e dicionários;
- hashabilidade das chaves de dicionário;
- `len()` para tamanho de coleções;
- aliases e cópias rasas;
- comparações de igualdade.

Ele também prepara o próximo capítulo:

- listas representarão sequências mutáveis e ordenadas;
- tuplas representarão estruturas de sequência ordenadas e imutáveis;
- dicionários representarão mapeamentos chave-valor;
- conjuntos representarão grupos distintos orientados a pertencimento.

O capítulo final de Coleções comparará diretamente esses quatro modelos e ajudará você a escolher pela intenção.

## 41. Exercício: comparar dois grupos de habilidades

Crie `skill_groups.py` com estes conjuntos iniciais:

```python
backend = {"python", "sql", "git"}
automation = {"python", "testing", "git"}
```

Sem usar loops ou condicionais:

1. imprima a quantidade de elementos distintos de cada conjunto;
2. imprima se `"python"` pertence aos dois conjuntos testando cada expressão de pertencimento;
3. crie `shared` usando interseção;
4. crie `backend_only` usando diferença;
5. crie `automation_only` usando diferença na direção oposta;
6. crie `combined` usando união;
7. crie `exclusive` usando diferença simétrica;
8. verifique `shared == {"python", "git"}`;
9. verifique `backend_only == {"sql"}`;
10. verifique `automation_only == {"testing"}`;
11. verifique `exclusive == {"sql", "testing"}`;
12. adicione `"apis"` a `backend`;
13. descarte `"testing"` de `automation`;
14. imprima se `"apis"` agora está em `backend`;
15. imprima se `"testing"` ainda está em `automation`;
16. crie `backend_copy = backend.copy()`;
17. adicione `"linux"` somente à cópia;
18. verifique que `"linux"` não está no original, mas está na cópia.

Um possível formato de saída determinística é:

```text
Backend count: 3
Automation count: 3
Python in backend: True
Python in automation: True
Shared correct: True
Backend-only correct: True
Automation-only correct: True
Exclusive correct: True
APIs in backend: True
Testing in automation: False
Linux in original: False
Linux in copy: True
```

Tente prever cada resultado Booleano antes de executar o programa.

## 42. Autoavaliação

Antes de avançar, confirme se consegue responder estas perguntas:

1. Por que um conjunto é diferente de uma lista mesmo quando ambos contêm vários valores?
2. Por que `{}` não cria um conjunto vazio?
3. O que acontece com elementos duplicados iguais em um conjunto?
4. Por que você não pode usar `set[0]` ou slicing em conjuntos?
5. O que `in` e `not in` testam?
6. Qual é a diferença entre `add()` e `update()`?
7. Qual é a diferença entre `remove()` e `discard()`?
8. Por que `set.pop()` não deve ser descrito como remoção do último item?
9. Qual requisito todo elemento de conjunto precisa cumprir?
10. Por que uma tupla às vezes pode ser elemento de conjunto enquanto uma lista não pode?
11. O que a união contém?
12. O que a interseção contém?
13. Por que a diferença entre conjuntos é direcional?
14. O que a diferença simétrica contém?
15. O que significa um conjunto ser subconjunto de outro?
16. O que `isdisjoint()` informa?
17. Por que converter uma lista para conjunto pode alterar mais do que o tratamento de duplicatas?
18. Por que mutações feitas por um alias podem afetar o conjunto original?

Se alguma resposta parecer incerta, volte à seção correspondente e altere um dos exemplos por conta própria.

## 43. Referência rápida

- Conjunto vazio: `values = set()`
- Conjunto não vazio: `values = {"a", "b"}`
- Converter um iterável: `values = set(source)`
- Contar elementos distintos: `len(values)`
- Pertencimento: `item in values`
- Não pertencimento: `item not in values`
- Adicionar um elemento: `values.add(item)`
- Adicionar vários elementos: `values.update(iterable)`
- Remover, erro se ausente: `values.remove(item)`
- Remover se presente: `values.discard(item)`
- Remover e retornar um elemento arbitrário: `item = values.pop()`
- Remover todos os elementos: `values.clear()`
- União: `a.union(b)` ou `a | b`
- Interseção: `a.intersection(b)` ou `a & b`
- Diferença: `a.difference(b)` ou `a - b`
- Diferença simétrica: `a.symmetric_difference(b)` ou `a ^ b`
- Subconjunto: `a.issubset(b)` ou `a <= b`
- Superconjunto: `a.issuperset(b)` ou `a >= b`
- Disjuntos: `a.isdisjoint(b)`
- Cópia rasa: `other = values.copy()`

Lembre do modelo:

- elementos de conjuntos são distintos;
- elementos de conjuntos precisam ser hashable;
- conjuntos comuns são mutáveis;
- conjuntos não fornecem indexação posicional ou slicing;
- não dependa da ordem de exibição de conjuntos com vários elementos;
- pertencimento e relações entre grupos são os principais pontos fortes de conjuntos.

## 44. Para onde ir agora

Agora você conhece os quatro principais modelos de coleção usados nesta fase:

1. **Lista:** sequência ordenada e mutável.
2. **Tupla:** estrutura de sequência ordenada e imutável.
3. **Dicionário:** mapeamento chave-valor.
4. **Conjunto:** coleção não ordenada de membros distintos e hashable.

O capítulo final de Coleções reunirá tudo em **Escolhendo a coleção certa**. Em vez de aprender outra família de sintaxe, você praticará decidir qual modelo melhor representa a relação entre seus valores.

---

Referências oficiais usadas para verificação técnica:

- [Tutorial do Python: Conjuntos](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Tipos embutidos do Python: Tipos de conjunto — `set`, `frozenset`](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Glossário do Python: hashable](https://docs.python.org/3/glossary.html#term-hashable)
