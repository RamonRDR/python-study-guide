<div align="center">

# `range()`, `enumerate()` e `zip()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Fluxo do Programa](../README.pt-BR.md) · [← Anterior: Loops `for` e Iteração](../04-for-loops-and-iteration/README.pt-BR.md)

Um loop `for` simples costuma ser suficiente quando você precisa apenas de cada item. Às vezes, porém, o loop também precisa de **números, posições ou itens de mais de um iterável**.

Este capítulo apresenta três funções embutidas que tornam essas intenções explícitas: `range()`, `enumerate()` e `zip()`.

**Tempo estimado de estudo:** 105–130 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar quando a iteração direta é mais clara do que usar um auxiliar de iteração;
- criar progressões numéricas com `range()`;
- explicar por que o valor `stop` de `range()` não é incluído;
- usar `start`, `stop` e `step` de forma deliberada;
- criar ranges decrescentes com passo negativo;
- reconhecer ranges vazios e o caso inválido de passo zero;
- explicar por que um objeto `range` não é uma lista materializada;
- usar `enumerate()` quando posição e item são necessários;
- escolher um valor de `start` apropriado para `enumerate()`;
- desempacotar diretamente no loop `for` os pares produzidos por `enumerate()`;
- usar `zip()` para percorrer vários iteráveis em paralelo;
- explicar o comportamento padrão de `zip()` com o iterável mais curto;
- usar `strict=True` quando comprimentos iguais fazem parte da expectativa do programa;
- reconhecer que `zip(strict=True)` foi adicionado no Python 3.10;
- distinguir a sequência reutilizável `range` dos iteradores retornados por `enumerate()` e `zip()`;
- combinar auxiliares de iteração sem esconder a intenção do loop;
- escolher entre iteração direta, `range()`, `enumerate()` e `zip()` conforme a informação de que o loop realmente precisa.

## 1. Por que auxiliares de iteração existem

O capítulo anterior estabeleceu o padrão básico:

```python
for item in iterable:
    statement
```

Essa ainda é a forma preferida quando o corpo precisa apenas de cada item.

Mas alguns loops precisam de informações adicionais:

- uma progressão numérica → `range()`;
- posição + item → `enumerate()`;
- itens paralelos → `zip()`.

Essas ferramentas não substituem `for`. Elas fornecem um iterável mais adequado para o loop `for` consumir.

## 2. Comece com a ferramenta mais simples que corresponde à intenção

Suponha que você precise apenas dos nomes dos tópicos:

```python
topics = ["conditions", "loops", "helpers"]

for topic in topics:
    print(topic)
```

Não adicione índices apenas porque eles existem.

Uma regra útil para este capítulo é:

**Pergunte de quais informações o corpo do loop precisa e então escolha o iterável que fornece exatamente essas informações.**

## 3. O que é `range()`

`range()` representa uma sequência imutável de inteiros que seguem uma progressão regular.

A forma mais simples é:

```python
range(stop)
```

Por exemplo:

```python
for number in range(5):
    print(number)
```

Saída:

```text
0
1
2
3
4
```

A progressão começa em `0` por padrão.

## 4. O valor `stop` não é incluído

Em:

```python
range(5)
```

`5` é o limite de parada, não um item incluído.

Os valores representados são:

```text
0, 1, 2, 3, 4
```

Esse desenho de intervalo semiaberto se conecta naturalmente à indexação começando em zero. Uma sequência com cinco itens tem índices válidos de `0` a `4`.

## 5. `range(start, stop)`

Você pode fornecer um valor inicial diferente:

```python
for number in range(2, 7):
    print(number)
```

Saída:

```text
2
3
4
5
6
```

O início é incluído quando pertence à progressão. O limite de parada continua excluído.

## 6. `range(start, stop, step)`

O terceiro argumento controla o passo entre os valores:

```python
for number in range(0, 10, 3):
    print(number)
```

Saída:

```text
0
3
6
9
```

O passo padrão é `1`.

## 7. Um passo negativo cria uma progressão decrescente

Para avançar para baixo, o passo precisa ser negativo:

```python
for number in range(5, 0, -1):
    print(number)
```

Saída:

```text
5
4
3
2
1
```

Novamente, o limite `0` fica de fora.

## 8. Direção e passo precisam concordar

Um passo positivo avança para cima. Um passo negativo avança para baixo.

Com passo positivo, o range fica vazio quando `start >= stop`. Com passo negativo, o range fica vazio quando `start <= stop`. A progressão não precisa cair exatamente em `stop`; esse limite continua excluído.

```python
print(list(range(5, 0)))
print(list(range(0, 5, -1)))
```

Saída:

```text
[]
[]
```

Esse é um comportamento normal, não um erro.

## 9. Passo zero é inválido

Um passo igual a zero nunca poderia avançar em direção a um limite, então Python o rejeita:

```python
range(0, 5, 0)
```

Isso levanta `ValueError`.

Tratamento de exceções é ensinado mais adiante no guia. Por enquanto, lembre-se da regra:

**`step` pode ser positivo ou negativo, mas não zero.**

## 10. `range()` espera argumentos semelhantes a inteiros

Para código de iniciante, trate os valores `start`, `stop` e `step` como inteiros.

Isto é válido:

```python
range(0, 10, 2)
```

Isto não é uma ferramenta de progressão em ponto flutuante:

```python
range(0, 1, 0.1)
```

Passar valores `float` comuns dessa forma levanta `TypeError`.

## 11. Um objeto `range` não é uma lista

Imprimir um range diretamente deixa isso visível:

```python
numbers = range(5)

print(numbers)
print(type(numbers))
```

Saída:

```text
range(0, 5)
<class 'range'>
```

`range()` não cria antecipadamente uma lista contendo todos os inteiros.

## 12. `range` é uma sequência imutável e um iterável

Um objeto `range` pode ser usado diretamente em `for` porque é iterável:

```python
for number in range(3):
    print(number)
```

Ele também se comporta como uma sequência em aspectos úteis:

```python
numbers = range(10, 20, 2)

print(len(numbers))
print(numbers[0])
print(numbers[-1])
print(14 in numbers)
```

Saída:

```text
5
10
18
True
```

Você não precisa converter um range em lista apenas para iterar sobre ele.

## 13. Converta para lista quando você realmente precisa de uma lista

A conversão pode ser útil para inspeção ou quando o código posterior realmente precisa de uma lista mutável:

```python
numbers = list(range(1, 6))
print(numbers)
```

Saída:

```text
[1, 2, 3, 4, 5]
```

Não materialize uma lista automaticamente quando o próprio objeto `range` já expressa a progressão de que você precisa.

## 14. Use `range()` quando os números em si importam

Um bom caso de uso é uma progressão fixa de números de tentativa:

```python
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
```

Saída:

```text
Attempt 1
Attempt 2
Attempt 3
```

Aqui os números são uma parte significativa da saída, então `range()` comunica bem a intenção.

## 15. Iteração direta é mais clara quando apenas os valores importam

Suponha que você tenha:

```python
topics = ["conditions", "loops", "helpers"]
```

Isto é direto e claro:

```python
for topic in topics:
    print(topic)
```

Esta versão adiciona uma indireção desnecessária quando o índice não é usado para mais nada:

```python
for index in range(len(topics)):
    print(topics[index])
```

As duas formas podem funcionar, mas a primeira diz mais diretamente o que o programa quer fazer: processar cada tópico.

## 16. `range(len(sequence))` ainda tem usos legítimos

Às vezes o índice em si é necessário, como ao atribuir de volta a uma posição específica:

```python
scores = [70, 80, 90]

for index in range(len(scores)):
    scores[index] = scores[index] + 5

print(scores)
```

Saída:

```text
[75, 85, 95]
```

A pergunta importante não é se `range(len(...))` é proibido. É se o índice realmente faz parte da tarefa.

## 17. O que é `enumerate()`

Quando você precisa tanto da posição quanto do item, `enumerate()` normalmente expressa essa intenção de forma mais direta.

```python
topics = ["conditions", "loops", "helpers"]

for index, topic in enumerate(topics):
    print(index, topic)
```

Saída:

```text
0 conditions
1 loops
2 helpers
```

`enumerate()` produz pares contendo uma contagem e um item.

## 18. `enumerate()` começa em zero por padrão

A contagem padrão segue a convenção familiar de base zero:

```python
letters = ["A", "B", "C"]

for index, letter in enumerate(letters):
    print(index, letter)
```

Saída:

```text
0 A
1 B
2 C
```

Use esse padrão quando a contagem representar índices normais do Python.

## 19. Use `start=` quando a numeração exibida tem outro significado

Numeração voltada para pessoas costuma começar em um:

```python
topics = ["conditions", "loops", "helpers"]

for position, topic in enumerate(topics, start=1):
    print(f"{position}. {topic}")
```

Saída:

```text
1. conditions
2. loops
3. helpers
```

Os itens não mudaram de posição dentro da lista. Apenas o contador produzido por `enumerate()` começa em `1`.

## 20. `enumerate()` funciona com iteráveis, não apenas listas

Uma string também pode ser enumerada:

```python
for position, letter in enumerate("loop", start=1):
    print(position, letter)
```

Saída:

```text
1 l
2 o
3 o
4 p
```

A mesma ideia se aplica a vários outros iteráveis.

## 21. Os pares de `enumerate()` são desempacotados pelo alvo do loop

Este loop:

```python
for index, topic in enumerate(["conditions", "loops"]):
    print(index, topic)
```

usa o comportamento de desempacotamento que você já aprendeu.

Cada item produzido possui dois componentes: `(contagem, item)`.

O alvo do loop atribui o primeiro componente a `index` e o segundo a `topic`.

## 22. Prefira `enumerate()` a um contador manual quando ele corresponde à tarefa

Um contador manual pode funcionar:

```python
position = 1

for topic in ["conditions", "loops", "helpers"]:
    print(position, topic)
    position = position + 1
```

Mas quando o objetivo é simplesmente associar cada item a uma contagem, isto é mais direto:

```python
for position, topic in enumerate(
    ["conditions", "loops", "helpers"],
    start=1,
):
    print(position, topic)
```

`enumerate()` mantém a responsabilidade da contagem na ferramenta de iteração, em vez de espalhá-la pelo corpo do loop.

## 23. O que é `zip()`

`zip()` combina itens de vários iteráveis em paralelo.

```python
topics = ["conditions", "loops", "helpers"]
minutes = [25, 40, 30]

for topic, duration in zip(topics, minutes):
    print(topic, duration)
```

Saída:

```text
conditions 25
loops 40
helpers 30
```

O primeiro tópico é associado à primeira duração, o segundo à segunda e assim por diante.

## 24. `zip()` produz tuplas

Você pode inspecionar os itens associados convertendo o resultado em lista:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

print(list(zip(names, scores)))
```

Saída:

```text
[('Ari', 82), ('Mina', 91)]
```

Cada item produzido por `zip()` é uma tupla.

Por isso um loop consegue desempacotá-lo naturalmente:

```python
for name, score in zip(names, scores):
    print(name, score)
```

## 25. `zip()` aceita mais de dois iteráveis

Iteração paralela não se limita a pares:

```python
names = ["Ari", "Mina"]
scores = [82, 91]
levels = ["review", "advance"]

for name, score, level in zip(names, scores, levels):
    print(name, score, level)
```

Saída:

```text
Ari 82 review
Mina 91 advance
```

Use tantas fontes paralelas quanto a tarefa realmente precisar, mas lembre-se de que muitas listas paralelas podem ficar difíceis de manter. Um dicionário ou registro estruturado pode às vezes modelar os dados com mais clareza.

## 26. Por padrão, `zip()` para no iterável mais curto

Este comportamento é importante:

```python
names = ["Ari", "Mina", "Leo"]
scores = [82, 91]

print(list(zip(names, scores)))
```

Saída:

```text
[('Ari', 82), ('Mina', 91)]
```

`"Leo"` não aparece porque o iterável de pontuações terminou primeiro.

A truncagem padrão pode ser intencional, mas também pode esconder um erro de alinhamento de dados.

## 27. Use `strict=True` quando comprimentos iguais forem obrigatórios

Se o programa espera que todos os iteráveis de entrada tenham comprimentos correspondentes, torne essa expectativa explícita:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

for name, score in zip(names, scores, strict=True):
    print(name, score)
```

Saída:

```text
Ari 82
Mina 91
```

Se um iterável terminar antes de outro, `zip(..., strict=True)` levanta `ValueError` em vez de truncar silenciosamente.

O argumento `strict` foi adicionado no Python 3.10.

## 28. Este capítulo não exige tratamento de exceções

Você deve entender o que `strict=True` garante sem precisar capturar o erro ainda.

Por enquanto, use esta orientação:

- diferença de comprimento é aceitável → `zip()` padrão pode ser intencional;
- os comprimentos precisam ser iguais → prefira `zip(..., strict=True)`.

Fases posteriores ensinam `try` e `except` para programas que precisam se recuperar de exceções de forma deliberada.

## 29. `zip()` funciona com iteráveis em geral

Os argumentos não precisam ser listas:

```python
letters = "ABC"
numbers = range(1, 4)

for letter, number in zip(letters, numbers, strict=True):
    print(letter, number)
```

Saída:

```text
A 1
B 2
C 3
```

Isso funciona porque tanto `str` quanto `range` são iteráveis.

## 30. `range` é reutilizável; `enumerate()` e `zip()` retornam iteradores

Esta é uma conexão importante com o capítulo anterior.

Um objeto `range` é uma sequência, então iterar sobre ele não consome o objeto permanentemente:

```python
numbers = range(3)

print(list(numbers))
print(list(numbers))
```

Saída:

```text
[0, 1, 2]
[0, 1, 2]
```

Em contraste, os objetos retornados por `enumerate()` e `zip()` são iteradores. Depois de esgotados, o mesmo iterador não reinicia automaticamente:

```python
pairs = zip(["A", "B"], [1, 2])

print(list(pairs))
print(list(pairs))
```

Saída:

```text
[('A', 1), ('B', 2)]
[]
```

Se você precisar de outra passagem, crie um novo objeto `enumerate()` ou `zip()` a partir dos iteráveis originais.

## 31. Combine auxiliares quando a intenção combinada continuar clara

Às vezes você precisa tanto de uma posição exibida quanto de dados alinhados de vários iteráveis:

```python
names = ["Ari", "Mina"]
scores = [82, 91]

for position, (name, score) in enumerate(
    zip(names, scores, strict=True),
    start=1,
):
    print(position, name, score)
```

Saída:

```text
1 Ari 82
2 Mina 91
```

Isso funciona porque:

1. `zip()` produz tuplas `(name, score)`;
2. `enumerate()` associa cada tupla a uma contagem;
3. o alvo do loop desempacota as duas camadas.

Use combinações assim somente quando permanecerem legíveis para o público esperado.

## 32. Escolha o auxiliar pela intenção

| Necessidade | Prefira |
|---|---|
| Apenas cada valor | `for item in iterable` direto |
| Progressão numérica | `range()` |
| Posição e valor | `enumerate()` |
| Valores paralelos | `zip()` |
| Valores paralelos que precisam se alinhar exatamente | `zip(..., strict=True)` |

Essas são orientações de clareza, não restrições da linguagem Python.

## 33. Erros comuns

### Erro 1: esperar que `stop` seja incluído

```python
print(list(range(1, 5)))
```

Saída:

```text
[1, 2, 3, 4]
```

### Erro 2: usar um passo com a direção errada

```python
print(list(range(5, 0, 1)))
```

Saída:

```text
[]
```

### Erro 3: usar `range(len(...))` quando o índice é desnecessário

```python
for index in range(len(topics)):
    print(topics[index])
```

Se o corpo precisa apenas de cada tópico, iteração direta é mais clara.

### Erro 4: confundir `enumerate(start=1)` com alteração dos índices da lista

O contador pode começar em `1`, mas a lista subjacente continua usando seus índices normais começando em zero.

### Erro 5: assumir que `zip()` padrão valida comprimentos iguais

Não valida. `zip()` padrão para no iterável mais curto.

### Erro 6: reutilizar um iterador `zip()` ou `enumerate()` já esgotado

Crie um novo objeto auxiliar quando outra passagem completa for necessária.

## 34. Exemplo trabalhado: `range_progressions.py`

```python
print(list(range(5)))
print(list(range(2, 7)))
print(list(range(0, 10, 3)))
print(list(range(5, 0, -1)))
```

Saída:

```text
[0, 1, 2, 3, 4]
[2, 3, 4, 5, 6]
[0, 3, 6, 9]
[5, 4, 3, 2, 1]
```

Exemplo no repositório: [`examples/range_progressions.py`](examples/range_progressions.py)

## 35. Exemplo trabalhado: `enumerate_positions.py`

```python
topics = ["conditions", "loops", "helpers"]

for position, topic in enumerate(topics, start=1):
    print(f"{position}. {topic}")
```

Saída:

```text
1. conditions
2. loops
3. helpers
```

Exemplo no repositório: [`examples/enumerate_positions.py`](examples/enumerate_positions.py)

## 36. Exemplo trabalhado: `zip_parallel_iteration.py`

```python
topics = ["conditions", "loops", "helpers"]
minutes = [25, 40, 30]

for topic, duration in zip(topics, minutes, strict=True):
    print(f"{topic}: {duration} min")
```

Saída:

```text
conditions: 25 min
loops: 40 min
helpers: 30 min
```

Exemplo no repositório: [`examples/zip_parallel_iteration.py`](examples/zip_parallel_iteration.py)

## 37. Exercício

Crie uma pequena agenda de estudos com estas duas listas alinhadas:

```python
topics = ["strings", "collections", "flow"]
minutes = [20, 35, 30]
```

Seu programa deve:

1. usar `zip(..., strict=True)` para manter cada tópico alinhado à sua duração;
2. usar `enumerate(..., start=1)` para numerar as linhas a partir de um;
3. imprimir uma linha para cada bloco de estudo neste formato:

```text
1. strings - 20 min
2. collections - 35 min
3. flow - 30 min
```

Depois crie separadamente uma contagem regressiva com `range()` que imprima:

```text
3
2
1
Start
```

Não use `while`, `break`, `continue` nem comprehension.

## 38. Checklist de revisão

Antes de avançar, confirme que você consegue explicar cada afirmação sem executar o código:

- [ ] `range(stop)` começa em zero por padrão.
- [ ] o limite `stop` não é incluído.
- [ ] `range(start, stop, step)` suporta passos positivos e negativos.
- [ ] passo zero levanta `ValueError`.
- [ ] `range` representa uma sequência imutável em vez de uma lista pré-construída.
- [ ] iteração direta é mais clara quando apenas o valor do item é necessário.
- [ ] `enumerate()` fornece uma contagem junto com cada item.
- [ ] `enumerate(..., start=1)` altera o contador, não os índices da coleção subjacente.
- [ ] `zip()` combina itens de iteráveis em paralelo.
- [ ] `zip()` padrão para quando o iterável mais curto se esgota.
- [ ] `zip(..., strict=True)` levanta `ValueError` quando os comprimentos diferem.
- [ ] o argumento `strict` existe no Python 3.10 e posteriores.
- [ ] `range` é reutilizável como sequência.
- [ ] `enumerate()` e `zip()` retornam iteradores que podem se esgotar.
- [ ] auxiliares de iteração podem ser combinados quando o resultado continuar legível.

## 39. Referência rápida

| Necessidade | Forma típica |
|---|---|
| Contar de zero até antes de `stop` | `range(stop)` |
| Escolher início e fim | `range(start, stop)` |
| Escolher um passo | `range(start, stop, step)` |
| Contar para baixo | `range(start, stop, -1)` ou outro passo negativo |
| Posição e item | `enumerate(iterable)` |
| Numeração voltada para pessoas | `enumerate(iterable, start=1)` |
| Iteração paralela | `zip(first, second)` |
| Exigir comprimentos iguais | `zip(first, second, strict=True)` |
| Apenas cada item | `for item in iterable` direto |

Lembre-se da progressão:

**iteração de itens → progressão numérica → posição + item → itens paralelos → regra explícita de alinhamento**

## Próximo passo

O próximo capítulo é **Loops `while` e Repetição Guiada por Estado**.

Agora você sabe repetir trabalho para itens e moldar a iteração quando o loop precisa de números, posições ou valores alinhados. Em seguida, o guia apresenta repetição controlada por uma **condição Booleana**, em vez de pelo esgotamento de um iterável.

## Referências oficiais

- [Tutorial do Python 3.13: A função `range()`](https://docs.python.org/3.13/tutorial/controlflow.html#the-range-function)
- [Tutorial do Python 3.13: Técnicas de iteração](https://docs.python.org/3.13/tutorial/datastructures.html#looping-techniques)
- [Funções embutidas do Python 3.13: `enumerate()` e `zip()`](https://docs.python.org/3.13/library/functions.html)
- [Tipos embutidos do Python 3.13: Ranges](https://docs.python.org/3.13/library/stdtypes.html#typesseq-range)
