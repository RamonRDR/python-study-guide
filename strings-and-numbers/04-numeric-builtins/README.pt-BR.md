<div align="center">

# Funções Numéricas Embutidas: `round()`, `abs()`, `min()`, `max()` e `sum()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

A Fase 2 já apresentou textos, operações com strings, inteiros, valores de ponto flutuante e valores booleanos. Este capítulo encerra a fase combinando esse conhecimento com cinco funções embutidas que resolvem tarefas numéricas comuns sem exigir importações.

Essas funções parecem pequenas, mas várias delas possuem detalhes importantes em programas reais. Em especial, `round()` nem sempre se comporta como a regra cotidiana de que "5 sempre arredonda para cima", a representação de ponto flutuante pode influenciar resultados arredondados e `min()` e `max()` exigem cuidado com entradas vazias.

## Informações do capítulo

- **Nível:** Iniciante
- **Pré-requisito:** concluir os Capítulos 01 a 03 da Fase 2
- **Tempo estimado de estudo:** 70 a 90 minutos
- **Conceitos principais:** `round()`, `abs()`, `min()`, `max()`, `sum()`, `ndigits`, iteráveis vazios, agregação numérica, arredondamento de ponto flutuante

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- usar `abs()` para obter a magnitude numérica sem alterar o valor original;
- usar `min()` e `max()` com vários argumentos ou com um iterável;
- explicar por que iteráveis vazios exigem cuidado com `min()` e `max()`;
- usar `sum()` para agregar valores numéricos e compreender seu argumento `start`;
- usar `round()` com `ndigits` omitido, positivo, zero e negativo;
- explicar a regra de desempate usada pelo Python no arredondamento de números embutidos;
- reconhecer por que a representação de ponto flutuante pode afetar um resultado arredondado;
- escolher essas funções embutidas para expressar intenção claramente em vez de reproduzir manualmente seu comportamento;
- reconhecer quando ferramentas posteriores, como `math.fsum()` ou aritmética decimal, podem ser mais adequadas.

---

## 1. Funções embutidas estão disponíveis sem importações

Python fornece um conjunto de funções embutidas disponíveis diretamente no código comum.

Você já conhece exemplos como:

```python
print("Python")
length = len("Python")
number = int("42")
```

As funções deste capítulo funcionam da mesma forma do ponto de vista de uso:

```python
print(abs(-8))
print(round(3.14159, 2))
```

Você não precisa disto:

```python
import builtins
```

O uso direto é a abordagem normal.

### Modelo mental

Pense nessas funções como pequenas ferramentas padrão que comunicam intenção:

```text
abs()    -> magnitude
round()  -> rounded numeric value
min()    -> smallest item
max()    -> largest item
sum()    -> accumulated total
```

A clareza de intenção é importante. `min(values)` informa ao leitor o que você quer de forma muito mais direta do que comparar manualmente cada valor.

---

## 2. `abs()` retorna um valor absoluto

Para inteiros e números de ponto flutuante comuns, `abs()` retorna a distância até zero sem sinal negativo.

```python
print(abs(-12))
print(abs(12))
print(abs(-3.5))
```

```text
12
12
3.5
```

O sinal da entrada não determina o sinal do resultado. O resultado representa magnitude.

### `abs()` não modifica o valor original

```python
temperature_change = -7
magnitude = abs(temperature_change)

print(temperature_change)
print(magnitude)
```

```text
-7
7
```

A variável original continua apontando para `-7`. `abs()` calculou e retornou outro valor.

Isso segue um padrão que você já viu em Python:

```text
input value -> operation -> result value
```

### Uso prático: distância de um alvo

Suponha que um valor-alvo seja `100`, enquanto o valor observado seja `93`.

```python
observed = 93
target = 100
difference = observed - target
absolute_difference = abs(difference)

print(absolute_difference)
```

```text
7
```

Quando a direção não importa e apenas o tamanho da diferença interessa, `abs()` comunica essa intenção claramente.

---

## 3. `min()` encontra o menor item

`min()` pode receber dois ou mais argumentos posicionais:

```python
print(min(8, 3, 12, -2))
```

```text
-2
```

Também pode receber um único iterável contendo os valores.

O próximo exemplo usa uma lista apenas como recipiente simples. Listas serão ensinadas adequadamente na Fase 3.

```python
values = [8, 3, 12, -2]
print(min(values))
```

```text
-2
```

As duas formas respondem ao mesmo tipo de pergunta, mas são úteis em situações diferentes:

```text
min(a, b, c)   -> values already exist as separate arguments
min(values)    -> values are already grouped in an iterable
```

### `min()` retorna um item existente

Com números comuns, isso parece óbvio:

```python
smallest = min(10, 4, 7)
print(smallest)
```

```text
4
```

Mais adiante, quando você estudar objetos mais ricos e o argumento `key`, essa ideia ficará ainda mais importante. Por enquanto, concentre-se em comparações numéricas.

---

## 4. `max()` encontra o maior item

`max()` espelha `min()`.

Com argumentos separados:

```python
print(max(8, 3, 12, -2))
```

```text
12
```

Com um único iterável:

```python
values = [8, 3, 12, -2]
print(max(values))
```

```text
12
```

Essa simetria torna o par fácil de lembrar:

```text
min(...) -> smallest
max(...) -> largest
```

### Uso prático: amplitude de um intervalo

Se a menor medição for `min(values)` e a maior for `max(values)`, a diferença entre elas descreve a amplitude do intervalo observado.

```python
values = [8, 3, 12, -2]
range_width = max(values) - min(values)
print(range_width)
```

```text
14
```

Esse cálculo combina vários conceitos sem esconder a intenção.

---

## 5. Entradas vazias são importantes para `min()` e `max()`

Um iterável vazio não possui menor nem maior elemento.

```python
values = []
```

Chamar qualquer uma dessas funções sem valor alternativo gera `ValueError`:

```python
min(values)
```

```text
ValueError: min() iterable argument is empty
```

E, de forma semelhante:

```python
max(values)
```

```text
ValueError: max() iterable argument is empty
```

Ao usar a forma com um único iterável, você pode fornecer `default=`:

```python
values = []
print(min(values, default=0))
print(max(values, default=0))
```

```text
0
0
```

### O valor alternativo precisa fazer sentido para o domínio

`default=0` não é automaticamente a escolha correta.

Por exemplo, se um conjunto vazio significar "não existe medição", retornar zero pode sugerir incorretamente que zero foi realmente medido.

A lição importante é:

```text
default is a domain decision, not merely an error-suppression trick
```

Você tomará essas decisões de forma mais deliberada depois de aprender fluxo do programa e tratamento de `None` nas fases posteriores.

---

## 6. Valores comparáveis são necessários

`min()` e `max()` comparam itens.

Valores numéricos compatíveis normalmente podem participar juntos:

```python
print(min(4, 2.5, 9))
print(max(4, 2.5, 9))
```

```text
2.5
9
```

Mas tipos sem relação entre si podem não possuir uma relação de ordenação:

```python
min(4, "2")
```

```text
TypeError: '<' not supported between instances of 'str' and 'int'
```

Não converta valores apenas para silenciar o erro. Primeiro decida o que os dados deveriam significar.

---

## 7. `sum()` acumula valores numéricos

`sum()` recebe um iterável e soma conceitualmente seus itens da esquerda para a direita, retornando o total.

```python
values = [10, 20, 5]
print(sum(values))
```

```text
35
```

Um iterável vazio possui soma bem definida porque o valor inicial padrão é zero:

```python
print(sum([]))
```

```text
0
```

Esse comportamento difere de `min()` e `max()`, em que uma entrada vazia não possui um menor ou maior item natural.

---

## 8. `sum()` possui um argumento `start`

O segundo argumento de `sum()` fornece o valor inicial.

```python
values = [10, 20, 5]
print(sum(values, 100))
```

```text
135
```

Um modelo mental útil é:

```text
total = start + all iterable items
```

O padrão equivale a:

```python
sum(values, 0)
```

### `start` não é um índice

Um engano comum entre iniciantes é interpretar o segundo argumento como "comece a somar a partir desta posição".

Não significa isso.

```python
values = [10, 20, 5]
print(sum(values, 2))
```

```text
37
```

O `2` é adicionado ao total. Ele não diz ao Python para ignorar os dois primeiros itens.

---

## 9. Não use `sum()` para concatenar strings

Isto não é suportado:

```python
sum(["Py", "thon"])
```

A chamada gera `TypeError`.

Para strings, o padrão adequado é `join()`, estudado anteriormente nesta fase:

```python
parts = ["Py", "thon"]
print("".join(parts))
```

```text
Python
```

As funções comunicam intenções diferentes:

```text
sum()  -> numeric accumulation
join() -> string concatenation from an iterable
```

Manter essas responsabilidades separadas produz código mais claro.

---

## 10. Totais de ponto flutuante ainda podem ser aproximados

O capítulo anterior explicou que muitas frações decimais não podem ser representadas exatamente como valores binários de ponto flutuante.

`sum()` não transforma aritmética com `float` em aritmética decimal exata.

```python
values = [0.1, 0.2]
print(sum(values))
```

```text
0.30000000000000004
```

Isso é uma questão de representação de ponto flutuante, não uma falha de `sum()`.

A biblioteca padrão do Python contém ferramentas para casos que exigem garantias numéricas diferentes. Por exemplo, `math.fsum()` foi projetado para somas de ponto flutuante mais precisas, enquanto aritmética decimal é útil quando semântica decimal é necessária.

Essas ferramentas pertencem a partes posteriores do roadmap. A ideia importante agora é não assumir que uma agregação elimina a aproximação do ponto flutuante.

---

## 11. `round()` retorna um valor numérico arredondado

Com apenas um argumento, `round()` retorna o inteiro mais próximo para tipos numéricos embutidos como `float`.

```python
print(round(3.2))
print(round(3.8))
```

```text
3
4
```

Quando `ndigits` é omitido ou vale `None`, o resultado para valores numéricos embutidos é um `int`:

```python
result = round(3.8)
print(type(result))
```

```text
<class 'int'>
```

---

## 12. `ndigits` controla a posição do arredondamento

Um segundo argumento controla a precisão solicitada.

```python
print(round(3.14159, 2))
print(round(3.14159, 4))
```

```text
3.14
3.1416
```

Para números embutidos, fornecer `ndigits` altera um detalhe importante de tipo:

```python
print(round(2.5))
print(type(round(2.5)))
print(round(2.5, 0))
print(type(round(2.5, 0)))
```

```text
2
<class 'int'>
2.0
<class 'float'>
```

Sem `ndigits`, o resultado demonstrado com `float` é inteiro. Nos casos de `int` e `float` abordados aqui, fornecer `ndigits` mantém um resultado `int` como `int` e um resultado `float` como `float`; isso não é uma regra para todo tipo numérico embutido.

---

## 13. `ndigits` pode ser zero ou negativo

Zero solicita arredondamento na posição das unidades. Para os tipos embutidos usados neste capítulo, um `int` permanece `int` e um `float` permanece `float` quando `ndigits` é fornecido explicitamente:

```python
print(round(12.7, 0))
```

```text
13.0
```

Valores negativos arredondam para posições à esquerda do separador decimal:

```python
print(round(1234, -1))
print(round(1234, -2))
print(round(1234, -3))
```

```text
1230
1200
1000
```

Uma representação posicional útil é:

```text
ndigits =  2 -> hundredths
ndigits =  1 -> tenths
ndigits =  0 -> units
ndigits = -1 -> tens
ndigits = -2 -> hundreds
```

`ndigits` negativo é especialmente útil quando valores precisam ser agrupados ou apresentados em escala mais ampla.

---

## 14. Python não usa a regra "5 sempre arredonda para cima"

Para tipos numéricos embutidos, quando dois múltiplos candidatos estão igualmente próximos, Python escolhe o valor par.

Observe:

```python
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))
```

```text
2
4
4
6
```

O resultado não é baseado em sempre subir.

As opções pares mais próximas são escolhidas:

```text
2.5 -> 2
3.5 -> 4
4.5 -> 4
5.5 -> 6
```

A mesma ideia aparece com valores negativos:

```python
print(round(-0.5))
print(round(-1.5))
print(round(-2.5))
```

```text
0
-2
-2
```

Essa regra costuma ser chamada de arredondamento de empates para o par.

---

## 15. O desempate para o par também importa com `ndigits` negativo

Inteiros fornecem uma forma limpa de observar a regra porque seus valores são exatos.

```python
print(round(125, -1))
print(round(135, -1))
```

```text
120
140
```

`125` está à mesma distância de `120` e `130`, então a opção de dezena par é `120`.

`135` está à mesma distância de `130` e `140`, então a opção de dezena par é `140`.

Esse exemplo evita misturar a regra de desempate com questões de representação de ponto flutuante.

---

## 16. `round()` e representação de ponto flutuante são ideias separadas

Um exemplo famoso é:

```python
print(round(2.675, 2))
```

```text
2.67
```

Alguém esperando aritmética decimal comum pode prever `2.68`.

O resultado surpreendente vem da forma como o literal decimal `2.675` é representado como `float` binário. O valor armazenado é uma aproximação, e `round()` opera sobre esse valor efetivamente armazenado.

Isso não é um bug do Python.

Um modelo mental prático é:

```text
source decimal text
        ↓
nearest representable binary float
        ↓
round() operates on that stored value
```

O capítulo anterior apresentou esse problema de representação. Aqui você está vendo uma de suas consequências.

---

## 17. `round()` não torna a aritmética de ponto flutuante exata

Considere:

```python
print(0.1 + 0.1 + 0.1 == 0.3)
```

```text
False
```

Arredondar previamente os valores individuais não transforma magicamente sua representação interna em frações decimais exatas.

```python
print(round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1))
```

```text
False
```

Use `round()` quando um valor arredondado for realmente o que o programa precisa. Não o use como ferramenta universal para "consertar" aritmética de ponto flutuante.

Mais adiante, você encontrará ferramentas como `math.isclose()` para comparações aproximadas e aritmética decimal para requisitos baseados em decimais.

---

## 18. Arredondar um valor e formatar uma exibição são objetivos diferentes

Suponha que você queira exibir duas casas decimais.

`round()` altera o resultado numérico:

```python
value = 3.1
rounded = round(value, 2)
print(rounded)
```

```text
3.1
```

Ele não promete que a impressão mostrará zeros finais como `3.10`.

Isso é uma questão de formatação, não de arredondamento numérico.

A formatação de strings é introduzida em outra parte da trilha. Mantenha a distinção em mente:

```text
rounding   -> numeric value
formatting -> textual presentation
```

---

## 19. Combinando as cinco funções embutidas

Essas funções ficam especialmente úteis em conjunto.

```python
values = [12, -4, 7.5, 3]

print(abs(-12))
print(min(values))
print(max(values))
print(sum(values))
print(round(sum(values), 1))
```

```text
12
-4
12
18.5
18.5
```

O código é quase um pequeno relatório legível:

```text
magnitude
minimum
maximum
total
rounded total
```

Essa legibilidade é uma das razões para preferir funções embutidas a laços manuais desnecessários ou comparações repetidas.

---

## 20. Uma prévia de iteráveis sem antecipar o ensino de coleções

`min()`, `max()` e `sum()` frequentemente recebem iteráveis.

Este capítulo usa literais de lista como:

```python
values = [10, 20, 30]
```

Você ainda não precisa dominar listas.

Por enquanto, trate a lista como um recipiente ordenado simples de valores que pode ser passado para uma função.

A Fase 3 ensinará listas, tuplas, conjuntos, dicionários, comportamento de indexação em coleções, mutabilidade, iteração e operações comuns com coleções em seu contexto adequado.

Essa pequena prévia existe porque seria difícil ensinar `sum()` de maneira significativa sem nenhum conjunto de valores.

---

## 21. Erro comum: recriar `abs()` manualmente

Um iniciante pode escrever uma lógica conceitualmente equivalente a:

```python
value = -8

if value < 0:
    magnitude = -value
else:
    magnitude = value
```

Isso pode ser útil ao estudar condicionais mais adiante, mas se a intenção real for apenas valor absoluto, isto é mais claro:

```python
magnitude = abs(value)
```

Use ferramentas padrão quando elas expressarem diretamente o requisito.

---

## 22. Erro comum: chamar `min()` ou `max()` com iterável vazio

Isto falha:

```python
values = []
minimum = min(values)
```

Antes de escolher uma solução, pergunte o que uma coleção vazia significa no programa.

Projetos possíveis mais adiante podem incluir:

- usar um valor `default=` semanticamente adequado;
- verificar se existem dados antes de chamar a função;
- tratar entrada vazia como dado inválido;
- representar ausência de dados explicitamente.

Não escolha um valor alternativo apenas porque ele impede uma exceção.

---

## 23. Erro comum: confundir `sum(..., start)` com slicing

Isto:

```python
sum([10, 20, 30], 5)
```

significa:

```text
5 + 10 + 20 + 30
```

Não significa:

```text
start at index 5
```

O resultado é:

```text
65
```

O nome do parâmetro `start` se refere ao total inicial.

---

## 24. Erro comum: usar `sum()` para strings

Não escreva:

```python
sum(["A", "B", "C"])
```

Use a operação de string criada para essa finalidade:

```python
print("".join(["A", "B", "C"]))
```

```text
ABC
```

Esse é um bom exemplo de escolha da operação com base na semântica dos dados, e não apenas na ideia de que as duas tarefas parecem "combinar" valores.

---

## 25. Erro comum: assumir que `round()` sempre arredonda metades para cima

Esta expectativa está errada no arredondamento numérico embutido do Python:

```text
2.5 -> expected by some beginners: 3
```

Resultado real:

```python
print(round(2.5))
```

```text
2
```

Lembre-se da regra de desempate para o par quando os candidatos estão igualmente próximos.

---

## 26. Erro comum: usar `round()` para esconder toda surpresa com `float`

Se um cálculo depende de semântica decimal exata, aplicar `round()` repetidamente em etapas intermediárias arbitrárias pode criar um novo problema em vez de resolver o original.

A ferramenta correta depende do domínio.

Exemplos de considerações futuras incluem:

```text
approximate scientific comparison -> math.isclose()
more accurate float summation      -> math.fsum()
decimal arithmetic requirements    -> decimal.Decimal
textual decimal display             -> formatting
```

Essas são conexões com o roadmap, não requisitos deste capítulo iniciante.

---

## 27. Erro comum: esquecer que funções retornam valores

Este código calcula um resultado, mas não o salva:

```python
round(9.876, 2)
```

Em um script, nada visível acontece se você não usar o valor retornado.

Você pode imprimi-lo:

```python
print(round(9.876, 2))
```

Ou atribuí-lo:

```python
rounded_value = round(9.876, 2)
```

O mesmo princípio vale para todas as cinco funções embutidas deste capítulo.

---

## 28. Conexões com capítulos anteriores

### Variáveis

Valores retornados podem ser atribuídos a nomes:

```python
maximum_value = max(4, 8, 2)
```

### Tipos

Essas funções operam sobre valores cujos tipos importam.

```python
print(type(round(2.5)))
print(type(round(2.5, 0)))
```

```text
<class 'int'>
<class 'float'>
```

### Conversão de tipos

Não confunda arredondamento com conversão.

```python
print(int(3.9))
print(round(3.9))
```

```text
3
4
```

`int()` converte truncando em direção a zero para um `float` finito. `round()` realiza arredondamento conforme suas regras.

### Comportamento de ponto flutuante

A explicação do capítulo anterior sobre aproximação binária é essencial para entender casos como `round(2.675, 2)`.

### Métodos de strings

`sum()` é agregação numérica; `join()` é a ferramenta adequada para combinar strings.

Essas conexões são exatamente o motivo pelo qual o guia ensina conceitos em sequência, e não como cartões de sintaxe isolados.

---

## 29. Exercício prático: relatório numérico

Crie um arquivo chamado `numeric_report.py`.

Comece com:

```python
measurements = [12.5, -3.2, 8.75, 4.0]
```

Produza estes resultados usando as funções embutidas deste capítulo:

1. a menor medição;
2. a maior medição;
3. o total;
4. o valor absoluto da menor medição;
5. o total arredondado para uma casa decimal;
6. a amplitude do intervalo, calculada como máximo menos mínimo.

Sua saída deve ter este formato:

```text
Minimum: -3.2
Maximum: 12.5
Total: 22.05
Minimum magnitude: 3.2
Rounded total: 22.1
Range width: 15.7
```

Não ordene nem compare os valores manualmente um por um.

### Exercício extra

Adicione:

```python
empty_measurements = []
```

Use `min()` e `max()` com um `default=` explícito e explique em um comentário por que o valor escolhido faria ou não sentido semântico em um sistema real de medições.

A parte importante é o raciocínio, não apenas evitar `ValueError`.

---

## 30. Autoavaliação

Tente responder sem executar Python primeiro.

1. O que `abs(-9)` retorna?
2. `abs()` modifica a variável original?
3. O que acontece quando `min([])` é chamado sem `default=`?
4. O que `sum([], 10)` retorna?
5. O que significa o segundo argumento de `sum()`?
6. Por que strings normalmente devem usar `join()` em vez de `sum()`?
7. O que `round(2.5)` retorna?
8. Por que `round(2.675, 2)` pode produzir `2.67`?
9. O que `round(1234, -2)` faz?
10. Qual é a diferença de tipo entre `round(2.5)` e `round(2.5, 0)`?
11. Por que `min()` e `max()` conseguem comparar valores `int` e `float`, mas podem rejeitar um `int` e uma `str` sem relação?
12. `round()` torna todos os cálculos de ponto flutuante exatos?

### Respostas sugeridas

1. `9`.
2. Não. Ela retorna um valor de resultado.
3. `ValueError` é gerado.
4. `10`.
5. É o total inicial que será somado aos itens do iterável.
6. `sum()` é para agregação numérica, enquanto `join()` foi criado para combinar strings.
7. `2`, porque um empate exato é resolvido em direção ao candidato par.
8. Porque o `float` binário armazenado é uma aproximação do literal decimal.
9. Ele arredonda para a posição das centenas, produzindo `1200`.
10. O primeiro é `int`; com `ndigits` explícito, o resultado do `float` embutido permanece `float`.
11. Tipos numéricos possuem semântica de ordenação compatível, enquanto tipos sem relação podem não definir uma relação de ordenação.
12. Não.

---

## 31. Referência rápida

| Objetivo | Ferramenta | Exemplo | Resultado |
|---|---|---|---|
| Magnitude absoluta | `abs()` | `abs(-8)` | `8` |
| Menor argumento | `min()` | `min(8, 2, 5)` | `2` |
| Maior argumento | `max()` | `max(8, 2, 5)` | `8` |
| Menor item de iterável | `min()` | `min([8, 2, 5])` | `2` |
| Maior item de iterável | `max()` | `max([8, 2, 5])` | `8` |
| Alternativa para iterável vazio | `min()` | `min([], default=0)` | `0` |
| Total numérico | `sum()` | `sum([8, 2, 5])` | `15` |
| Total com valor inicial | `sum()` | `sum([8, 2, 5], 10)` | `25` |
| Inteiro mais próximo | `round()` | `round(3.6)` | `4` |
| Arredondamento decimal | `round()` | `round(3.14159, 2)` | `3.14` |
| Arredondamento para dezenas | `round()` | `round(125, -1)` | `120` |

---

## 32. Exemplos do repositório

Execute os exemplos determinísticos a partir da raiz do repositório:

```bash
python strings-and-numbers/04-numeric-builtins/examples/numeric_summary.py
python strings-and-numbers/04-numeric-builtins/examples/rounding_behavior.py
```

Saída esperada de `numeric_summary.py`:

```text
Absolute: 12
Minimum: -4
Maximum: 12
Total: 18.5
Total with start: 28.5
```

Saída esperada de `rounding_behavior.py`:

```text
2.5: 2
3.5: 4
125 to tens: 120
135 to tens: 140
2.675 to two decimals: 2.67
Type without ndigits: <class 'int'>
Type with ndigits: <class 'float'>
```

---

## 33. Fase 2 concluída

Com este capítulo, a Fase 2 cobriu:

```text
string creation and indexing
        ↓
common string methods
        ↓
int, float, and bool behavior
        ↓
common numeric built-ins
```

Agora você possui uma base mais forte para trabalhar com valores individuais de texto e números.

A próxima fase curricular apresenta **Coleções**, em que vários valores passam a ser estruturas de primeira classe nos seus programas. Listas, tuplas, conjuntos e dicionários tornarão muito mais poderosos vários padrões antecipados nesta fase.

Antes de avançar, o repositório pode realizar uma auditoria entre capítulos para verificar se a Fase 2 funciona de forma fluida como uma única trilha de aprendizagem.

---

## Referências oficiais

- [Funções embutidas](https://docs.python.org/3/library/functions.html)
- [`abs()`](https://docs.python.org/3/library/functions.html#abs)
- [`max()`](https://docs.python.org/3/library/functions.html#max)
- [`min()`](https://docs.python.org/3/library/functions.html#min)
- [`round()`](https://docs.python.org/3/library/functions.html#round)
- [`sum()`](https://docs.python.org/3/library/functions.html#sum)
- [Aritmética de ponto flutuante: problemas e limitações](https://docs.python.org/3/tutorial/floatingpoint.html)

---

## Próximo passo

A Fase 2 está concluída. Continue para o ponto de revisão da Fase 2 e depois para a **Fase 3: Coleções** no roadmap principal.
