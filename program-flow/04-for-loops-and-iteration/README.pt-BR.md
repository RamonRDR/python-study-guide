<div align="center">

# Loops `for` e Iteração

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Fluxo do Programa](../README.pt-BR.md) · [← Anterior: `match` e `case`](../03-match-and-case/README.pt-BR.md)

Os capítulos anteriores ensinaram Python a **escolher** o que deve ser executado. Um loop `for` introduz um tipo diferente de controle de fluxo: **repetir um bloco uma vez para cada item fornecido por um iterável**.

É aqui que coleções deixam de ser apenas valores que você inspeciona e passam a funcionar como fluxos de trabalho que o programa pode processar um item de cada vez.

**Tempo estimado de estudo:** 105–130 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar a diferença entre seleção e repetição;
- explicar o que significa iteração;
- escrever um loop `for` básico com sintaxe e indentação corretas;
- identificar o alvo do loop e o iterável em uma instrução `for`;
- explicar o que é um iterável em um nível apropriado para iniciantes;
- reconhecer que Python cria e consome automaticamente um iterador para um loop `for`;
- iterar sobre listas, tuplas, strings, dicionários e conjuntos;
- explicar as garantias de ordem, ou a ausência delas, nesses tipos iteráveis;
- iterar sobre chaves, valores e pares chave-valor de dicionários;
- desempacotar itens com múltiplas partes diretamente no alvo de um `for`;
- combinar `for` com uma instrução `if`;
- construir uma nova coleção a partir de itens selecionados sem usar comprehension;
- usar loops aninhados quando uma tarefa repetida realmente pertence dentro de outra;
- explicar o que acontece quando um iterável está vazio;
- evitar depender do alvo do loop como variável de resultado depois do loop;
- evitar modificar a estrutura da mesma coleção enquanto itera sobre ela;
- reconhecer quando `for` é apropriado e quando uma ferramenta de fluxo posterior expressará melhor a intenção.

## 1. Da seleção para a repetição

Uma instrução `if` escolhe se um bloco será executado. Uma instrução `match` escolhe um bloco de acordo com um padrão.

Um loop `for` responde a outra pergunta:

**O que Python deve fazer para cada item?**

Suponha que uma lista contenha três tópicos:

```python
topics = ["conditions", "patterns", "loops"]
```

Sem um loop, você poderia escrever:

```python
print(topics[0])
print(topics[1])
print(topics[2])
```

Isso funciona apenas porque você já conhece exatamente o tamanho e as posições.

Um loop `for` expressa diretamente a relação:

```python
for topic in topics:
    print(topic)
```

Saída:

```text
conditions
patterns
loops
```

O loop diz: para cada item fornecido por `topics`, chame temporariamente esse item de `topic` e execute o bloco indentado.

## 2. Sintaxe básica

A forma para iniciantes é:

```python
for item in iterable:
    statement
```

Ela tem quatro partes importantes:

1. `for` inicia o loop;
2. `item` é o alvo que recebe cada valor;
3. `in` conecta o alvo à fonte de itens;
4. `iterable` é o objeto capaz de fornecer itens um de cada vez.

Os dois-pontos encerram o cabeçalho do loop. O bloco indentado é o corpo do loop.

Um exemplo real:

```python
colors = ["blue", "green", "orange"]

for color in colors:
    print(f"Color: {color}")
```

Saída:

```text
Color: blue
Color: green
Color: orange
```

## 3. Um loop, passo a passo

Considere:

```python
levels = ["beginner", "intermediate", "advanced"]

for level in levels:
    print(level)
```

Um rastreamento mental útil é:

```text
first item  -> level = "beginner"     -> run the body
second item -> level = "intermediate" -> run the body
third item  -> level = "advanced"     -> run the body
no more items -> leave the loop
```

Python não executa a coleção inteira de uma vez. Cada iteração atribui um item ao alvo e então executa o corpo.

## 4. O `for` do Python é orientado por itens

Um loop `for` em Python é fundamentalmente sobre **itens vindos de um iterável**.

Isso é diferente da ideia clássica de loop no estilo C, cujo cabeçalho contém manualmente:

- um contador inicial;
- uma condição;
- uma expressão de incremento.

Neste capítulo, não pense:

```text
repeat three times
```

Pense:

```text
for each item supplied by this iterable
```

Quando o objetivo real for produzir uma progressão numérica ou acompanhar posições explicitamente, o próximo capítulo introduzirá `range()` e `enumerate()`.

## 5. O que é um iterável

Um **iterável** é um objeto capaz de fornecer seus membros um de cada vez.

Você já conhece vários tipos iteráveis:

- `list`;
- `tuple`;
- `str`;
- `dict`;
- `set`.

Isso significa que todos eles podem aparecer depois de `in` em um loop `for`.

A palavra iterável **não** significa "lista". Uma lista é apenas um tipo de iterável.

Essa distinção importa porque a mesma sintaxe de `for` funciona com muitos tipos diferentes de objetos.

## 6. Iterável versus iterador

A terminologia do Python distingue um **iterável** de um **iterador**.

Para um iniciante, um bom modelo mental prático é:

```text
iterable = source that can provide items
iterator = object Python uses to obtain the next item from that source
```

Quando um loop `for` começa, Python obtém um iterador para o iterável e continua pedindo o próximo item até que nenhum item reste.

Normalmente você **não** precisa chamar `iter()` ou `next()` por conta própria para escrever um loop `for`. A instrução lida com esse protocolo para você.

Tópicos posteriores poderão explorar iteradores diretamente. Por enquanto, entenda por que a palavra **iterável** é mais ampla do que coleção ou sequência.

## 7. O alvo do loop é um alvo de atribuição

Neste loop:

```python
scores = [72, 81, 90]

for score in scores:
    print(score)
```

`score` recebe um novo item em cada iteração.

Conceitualmente:

```text
score = 72
run body
score = 81
run body
score = 90
run body
```

Isso conecta loops a um conceito que você já conhece: atribuição.

O alvo do loop não é um placeholder mágico e somente para leitura. É um alvo normal de atribuição que Python atualiza conforme a iteração avança.

## 8. A indentação define o corpo do loop

Assim como em `if` e `match`, indentação faz parte da sintaxe.

```python
names = ["Ana", "Mina"]

for name in names:
    print(f"Hello, {name}")
    print("Inside the loop")

print("After the loop")
```

Saída:

```text
Hello, Ana
Inside the loop
Hello, Mina
Inside the loop
After the loop
```

As duas chamadas `print()` indentadas são executadas para cada nome. O `print()` final é executado uma vez depois que a iteração termina.

O guia usa quatro espaços por nível de indentação, seguindo a PEP 8.

## 9. Iterando sobre uma lista

Listas são um primeiro caso de uso natural porque contêm uma sequência de itens:

```python
topics = ["strings", "collections", "flow"]

for topic in topics:
    print(f"Review: {topic}")
```

Saída:

```text
Review: strings
Review: collections
Review: flow
```

A iteração sobre uma lista segue a ordem da lista.

Você não precisa de índices quando o objetivo é simplesmente processar cada valor.

## 10. Iterando sobre uma tupla

Tuplas também são iteráveis:

```python
coordinates = (4, -2)

for coordinate in coordinates:
    print(coordinate)
```

Saída:

```text
4
-2
```

A imutabilidade da tupla não impede a iteração. Imutabilidade significa que a estrutura da tupla não pode ser alterada por atribuição de item; não significa que seus itens não possam ser lidos um de cada vez.

A iteração sobre uma tupla segue a ordem da tupla.

## 11. Iterando sobre uma string

Uma string é uma sequência iterável de caracteres:

```python
word = "loop"

for letter in word:
    print(letter)
```

Saída:

```text
l
o
o
p
```

Os dois caracteres `o` aparecem porque a iteração processa posições da string, não apenas valores distintos.

A iteração de uma string segue a ordem dos caracteres da string.

## 12. Valores repetidos continuam sendo itens repetidos

Um loop não remove duplicatas automaticamente.

```python
scores = [80, 90, 80]

for score in scores:
    print(score)
```

Saída:

```text
80
90
80
```

O primeiro e o terceiro itens têm valores iguais, mas ainda são itens separados na sequência da lista.

Se unicidade for a relação importante, um conjunto pode ser uma coleção mais apropriada. Essa é uma decisão de modelagem dos dados, não um comportamento especial de `for`.

## 13. Um iterável vazio executa o corpo zero vezes

Um loop `for` não exige pelo menos uma iteração.

```python
topics = []

for topic in topics:
    print(topic)

print("Finished")
```

Saída:

```text
Finished
```

Não havia itens para atribuir a `topic`, então o corpo do loop nunca foi executado.

Essa é uma propriedade importante: **zero iterações é normal**.

## 14. Iterar sobre um dicionário fornece chaves por padrão

Um dicionário é iterável, mas sua iteração padrão produz as chaves:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic in lesson_minutes:
    print(topic)
```

Saída:

```text
conditions
patterns
loops
```

Isso é equivalente em intenção a iterar sobre `lesson_minutes.keys()`.

No Python 3.7 e versões posteriores, a ordem de inserção dos dicionários é garantida pela linguagem. Portanto, as chaves acima aparecem na ordem em que essas entradas foram inseridas.

## 15. Iterando sobre valores de um dicionário

Se as chaves não forem necessárias, `.values()` fornece os valores:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for minutes in lesson_minutes.values():
    print(minutes)
```

Saída:

```text
25
35
40
```

Escolha o iterável de acordo com o que o corpo precisa.

## 16. Iterando sobre pares chave-valor de um dicionário

`.items()` fornece pares chave-valor:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic, minutes in lesson_minutes.items():
    print(f"{topic}: {minutes} min")
```

Saída:

```text
conditions: 25 min
patterns: 35 min
loops: 40 min
```

O alvo do loop tem dois nomes porque cada item fornecido por `.items()` é um par com dois itens.

## 17. Um alvo de `for` pode desempacotar itens

O exemplo anterior se conecta diretamente ao desempacotamento de tuplas e sequências da Fase 3.

```python
records = [
    ("conditions", 25),
    ("patterns", 35),
]

for topic, minutes in records:
    print(topic, minutes)
```

Saída:

```text
conditions 25
patterns 35
```

Para cada par, Python atribui o primeiro componente a `topic` e o segundo a `minutes`.

A quantidade e a estrutura dos nomes do alvo precisam ser compatíveis com os itens que serão desempacotados.

## 18. Iterando sobre um conjunto

Conjuntos são iteráveis:

```python
topics = {"strings", "collections", "flow"}

for topic in topics:
    print(topic)
```

Porém, um conjunto não possui um contrato de ordenação posicional no qual você deva confiar.

Não escreva código para iniciantes que dependa de uma ordem específica de iteração de conjuntos.

Por isso, este capítulo não documenta uma ordem exata de saída para esse exemplo.

## 19. O iterável determina a ordem significativa

`for` por si só não promete uma única regra universal de ordenação.

O iterável fornece itens de acordo com sua própria semântica:

| Iterável | Ordem em que se pode confiar |
|---|---|
| `list` | ordem da sequência da lista |
| `tuple` | ordem da sequência da tupla |
| `str` | ordem da sequência de caracteres |
| `dict` | ordem de inserção das chaves no Python 3.7+ |
| `dict.values()` | ordem de inserção correspondente |
| `dict.items()` | ordem de inserção correspondente |
| `set` | sem contrato de ordem posicional |

Uma boa regra é:

**Pergunte qual ordem o iterável define, não qual ordem `for` define.**

## 20. Combinando `for` com `if`

As ferramentas de fluxo dos capítulos anteriores podem trabalhar dentro de um loop:

```python
scores = [52, 81, 67, 90]

for score in scores:
    if score >= 70:
        print(f"Passing: {score}")
```

Saída:

```text
Passing: 81
Passing: 90
```

O loop controla **qual item é o atual**. O `if` controla **o que acontece para esse item**.

Essa combinação é uma das bases mais comuns para processamento de dados.

## 21. Construindo uma nova lista durante a iteração

Você já conhece `list.append()`, então pode coletar resultados selecionados de forma explícita:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)

print(passing_scores)
```

Saída:

```text
[81, 90]
```

Esse padrão tem três etapas claras:

```text
create destination
    ↓
iterate over source
    ↓
append selected result
```

List comprehensions podem expressar algumas transformações de forma mais compacta, mas são intencionalmente adiadas até que loops estejam completamente compreendidos.

## 22. Acumulando um resultado

Um loop também pode atualizar um acumulador separado:

```python
minutes = [20, 35, 15]
total = 0

for value in minutes:
    total = total + value

print(total)
```

Saída:

```text
70
```

A distinção importante é:

- `value` é o item atual;
- `total` é um estado que sobrevive de uma iteração para a próxima.

Para uma soma simples de valores numéricos, `sum()` normalmente é mais claro e você já o aprendeu na Fase 2. Este exemplo manual existe para mostrar como o estado pode mudar entre iterações, não para substituir `sum()`.

## 23. Loops aninhados

O corpo de um loop pode conter outro loop:

```python
groups = [
    ["A", "B"],
    ["C", "D"],
]

for group in groups:
    for item in group:
        print(item)
```

Saída:

```text
A
B
C
D
```

Para cada `group`, o loop interno conclui sua iteração sobre aquele grupo.

A indentação mostra a relação:

```text
outer item
    ↓
run the complete inner loop
    ↓
move to the next outer item
```

Loops aninhados são úteis quando os próprios dados têm estrutura aninhada. Evite aninhar apenas porque é possível; cada nível aumenta a quantidade de fluxo que o leitor precisa acompanhar.

## 24. Tenha cuidado ao modificar a coleção que está sendo percorrida

Alterar a estrutura da mesma coleção enquanto itera sobre ela pode produzir comportamento confuso ou erros, dependendo da coleção e da alteração.

Para código de iniciantes, prefira uma destas estratégias:

- iterar sobre a coleção original e construir uma nova coleção;
- quando a mutação for realmente necessária, iterar sobre uma cópia apropriada.

Um padrão claro de filtragem é:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)
```

Aqui o loop lê `scores`, enquanto as mutações acontecem apenas em `passing_scores`.

Essa separação é mais fácil de raciocinar do que excluir ou inserir itens em `scores` enquanto ela está sendo percorrida.

## 25. O alvo do loop pode continuar existindo depois de um loop não vazio

Python não exclui automaticamente o nome do alvo depois de um loop `for`.

```python
values = [10, 20, 30]

for value in values:
    print(value)

print(f"Last assigned value: {value}")
```

Saída:

```text
10
20
30
Last assigned value: 30
```

Esse é um comportamento real da linguagem, mas depender do alvo do loop como resultado final do programa costuma ser pouco claro.

Há também um caso de borda importante: se o iterável estiver vazio, o loop não fará nenhuma atribuição ao alvo.

Prefira uma variável de resultado separada e inicializada deliberadamente quando o código depois do loop precisar de um resultado.

## 26. Reatribuir o alvo dentro do corpo não controla a iteração

Como Python atribui o próximo item ao alvo do loop em cada iteração, alterar esse nome dentro do corpo não diz ao loop qual deve ser o próximo item.

```python
values = [1, 2, 3]

for value in values:
    value = value * 10
    print(value)
```

Saída:

```text
10
20
30
```

O corpo altera a associação atual, mas a próxima iteração atribui novamente a `value` o próximo item de `values`.

Se você precisa de um valor transformado, um nome separado pode tornar a intenção mais clara:

```python
values = [1, 2, 3]

for value in values:
    transformed = value * 10
    print(transformed)
```

## 27. Quando `for` é uma boa escolha

Use `for` quando a ideia central for:

- processar todos os itens de uma coleção;
- inspecionar caracteres de um texto;
- processar chaves, valores ou pares de um dicionário;
- filtrar itens com um `if` dentro do loop;
- construir um novo resultado a partir de itens existentes;
- percorrer estruturas iteráveis aninhadas.

O sinal mais forte é que você já possui, ou consegue obter naturalmente, um iterável cujos itens definem a repetição.

## 28. Quando outra ferramenta pode expressar melhor a intenção

Não escolha `for` apenas porque há repetição envolvida.

Capítulos posteriores oferecem ferramentas para intenções diferentes:

- `range()` para progressões aritméticas e iteração orientada por contagem;
- `enumerate()` quando posição e item são necessários;
- `zip()` quando múltiplos iteráveis devem avançar juntos;
- `while` quando a repetição é controlada por uma condição que muda, e não pelo esgotamento de um iterável;
- `break` e `continue` quando o fluxo do loop precisa de saída antecipada ou salto deliberado.

Essa separação mantém o primeiro modelo mental limpo: **`for` consome itens de um iterável**.

## 29. Escolha nomes singulares para o alvo quando possível

Se o nome de uma coleção está no plural, um alvo no singular costuma deixar a relação óbvia:

```python
topics = ["strings", "collections", "flow"]

for topic in topics:
    print(topic)
```

Da mesma forma:

```python
students = ["Ana", "Diego"]

for student in students:
    print(student)
```

Nomes como `x` ou `item` são válidos, mas um nome singular específico do domínio normalmente ensina melhor a intenção do código.

## 30. Erros comuns

### Erro 1: esquecer os dois-pontos

Incorreto:

```python
for topic in topics
    print(topic)
```

Correto:

```python
for topic in topics:
    print(topic)
```

### Erro 2: esquecer a indentação

Incorreto:

```python
for topic in topics:
print(topic)
```

Correto:

```python
for topic in topics:
    print(topic)
```

### Erro 3: iterar sobre a parte errada de um dicionário

Isto fornece chaves:

```python
for item in settings:
    print(item)
```

Se o corpo precisa tanto da chave quanto do valor, use `.items()`:

```python
for key, value in settings.items():
    print(key, value)
```

### Erro 4: assumir ordem de conjunto

Não dependa de isto produzir uma ordem posicional escolhida:

```python
for topic in {"strings", "collections", "flow"}:
    print(topic)
```

### Erro 5: assumir que o corpo será executado pelo menos uma vez

Um iterável vazio produz zero execuções do corpo.

### Erro 6: alterar a coleção de origem enquanto a percorre

Prefira construir uma nova coleção ou iterar deliberadamente sobre uma cópia adequada.

### Erro 7: esperar que reatribuir o alvo controle o loop

A próxima iteração atribui novamente o próximo item do iterador.

### Erro 8: recorrer a índices quando apenas os valores são necessários

Se o corpo precisa somente de cada valor, itere diretamente sobre os valores. Ferramentas que lidam com posição chegam no próximo capítulo.

## 31. Limite de escopo deste capítulo

Este capítulo se concentra em iteração direta, item por item.

Ele não exige:

- `range()`;
- `enumerate()`;
- `zip()`;
- loops `while`;
- `break`;
- `continue`;
- `else` de loop;
- comprehensions;
- funções definidas pelo usuário;
- tratamento de exceções;
- bibliotecas externas.

A gramática de `for` do Python oferece uma cláusula `else` opcional, mas este guia ensina intencionalmente o `else` de loop junto com `break` mais adiante, porque seu significado fica mais claro quando término normal do loop e encerramento antecipado podem ser comparados diretamente.

## 32. Exemplo trabalhado: iterando sobre coleções

O arquivo [`examples/collection_iteration.py`](examples/collection_iteration.py) contém:

```python
topics = ["conditions", "patterns", "loops"]

for topic in topics:
    print(f"Study: {topic}")

coordinates = (4, -2)

for coordinate in coordinates:
    print(f"Coordinate: {coordinate}")

word = "loop"
letters = []

for letter in word:
    letters.append(letter.upper())

print("Letters:", letters)
```

Saída:

```text
Study: conditions
Study: patterns
Study: loops
Coordinate: 4
Coordinate: -2
Letters: ['L', 'O', 'O', 'P']
```

Este exemplo conecta iteração sobre lista, tupla e string à mutação de listas já aprendida nas fases anteriores.

## 33. Exemplo trabalhado: iteração de dicionário

O arquivo [`examples/dictionary_iteration.py`](examples/dictionary_iteration.py) contém:

```python
lesson_minutes = {
    "conditions": 25,
    "patterns": 35,
    "loops": 40,
}

for topic in lesson_minutes:
    print(f"Topic: {topic}")

for topic, minutes in lesson_minutes.items():
    print(f"{topic}: {minutes} min")
```

Saída:

```text
Topic: conditions
Topic: patterns
Topic: loops
conditions: 25 min
patterns: 35 min
loops: 40 min
```

O primeiro loop usa chaves do dicionário. O segundo usa `.items()` e desempacotamento no alvo.

## 34. Exemplo trabalhado: filtrar e coletar

O arquivo [`examples/filter_and_collect.py`](examples/filter_and_collect.py) contém:

```python
scores = [52, 81, 67, 90]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)

print("Passing scores:", passing_scores)
print("Passing count:", len(passing_scores))
```

Saída:

```text
Passing scores: [81, 90]
Passing count: 2
```

Este exemplo combina diretamente as quatro primeiras fases:

```text
list of values
    ↓
for each value
    ↓
if the condition is true
    ↓
append the value to a result list
```

## 35. Exercício

Crie uma lista chamada `study_minutes` contendo:

```python
[25, 40, 15, 50]
```

Depois:

1. crie uma lista vazia chamada `long_sessions`;
2. itere sobre `study_minutes` com `for`;
3. se um valor for pelo menos `30`, adicione-o a `long_sessions`;
4. depois do loop, imprima `long_sessions`;
5. imprima seu comprimento.

Valores finais esperados:

```text
[40, 50]
2
```

Depois explique com suas próprias palavras:

- qual é o iterável;
- qual é o alvo do loop;
- quantas iterações acontecem;
- por que o bloco `if` é executado menos vezes do que o corpo do loop é acessado.

### Prática extra

Dado:

```python
course = {
    "title": "Python",
    "phase": 4,
    "chapter": 4,
}
```

Escreva um loop que imprima apenas as chaves e depois outro que imprima cada chave e seu valor correspondente usando `.items()`.

Ainda não use `range()`, `enumerate()`, `zip()` nem comprehension.

## 36. Checklist de revisão

Antes de avançar, confirme que você consegue explicar cada afirmação sem executar o código:

- [ ] `for` repete um bloco para itens fornecidos por um iterável.
- [ ] um iterável pode fornecer itens um de cada vez.
- [ ] Python gerencia automaticamente o iterador usado por um loop `for` normal.
- [ ] o alvo do loop recebe um novo item em cada iteração.
- [ ] um iterável vazio causa zero execuções do corpo.
- [ ] listas, tuplas e strings iteram na ordem da sequência.
- [ ] a iteração de dicionário produz chaves por padrão.
- [ ] `.values()` fornece valores do dicionário.
- [ ] `.items()` fornece pares chave-valor que podem ser desempacotados.
- [ ] a iteração de conjunto não deve ser tratada como ordenação posicional.
- [ ] um `if` dentro de um loop pode tomar uma decisão para cada item atual.
- [ ] uma lista de destino separada pode coletar resultados selecionados com segurança.
- [ ] loops aninhados são apropriados quando o trabalho repetido acompanha uma estrutura de dados aninhada.
- [ ] modificar a mesma coleção enquanto a percorre costuma ser uma estratégia ruim para iniciantes.
- [ ] o alvo do loop pode continuar existindo depois de um loop não vazio, mas não deve ser tratado como variável confiável de resultado.
- [ ] `range()`, `enumerate()` e `zip()` pertencem ao próximo capítulo.

## 37. Referência rápida

| Necessidade | Forma típica |
|---|---|
| Iterar sobre valores | `for item in iterable:` |
| Iterar sobre uma lista | `for item in items:` |
| Iterar sobre caracteres de texto | `for character in text:` |
| Iterar sobre chaves de dicionário | `for key in mapping:` |
| Iterar sobre valores de dicionário | `for value in mapping.values():` |
| Iterar sobre pares chave-valor | `for key, value in mapping.items():` |
| Decidir por item | `for item in items:` com um `if` interno |
| Construir lista filtrada | inicialize `result = []` e use `append()` para os itens selecionados |
| Percorrer coleções aninhadas | loops `for` aninhados |
| Nenhum item disponível | o corpo do loop executa zero vezes |

Lembre-se da progressão:

**iterable → next item → assign target → run body → repeat until exhausted**

## Próximo passo

O próximo capítulo é **`range()`, `enumerate()` e `zip()`**.

Agora você sabe processar itens diretamente. Em seguida, o guia adiciona ferramentas para gerar progressões numéricas, manter posições ao lado dos itens e avançar por múltiplos iteráveis em conjunto.

## Referências oficiais

- [Python 3.13 tutorial: `for` Statements](https://docs.python.org/3.13/tutorial/controlflow.html#for-statements)
- [Python 3.13 language reference: The `for` statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-for-statement)
- [Python 3.13 glossary: iterable](https://docs.python.org/3.13/glossary.html#term-iterable)
- [Python 3.13 glossary: iterator](https://docs.python.org/3.13/glossary.html#term-iterator)
- [Python 3.13 tutorial: Looping Techniques](https://docs.python.org/3.13/tutorial/datastructures.html#looping-techniques)
- [PEP 8: Indentation](https://peps.python.org/pep-0008/#indentation)
