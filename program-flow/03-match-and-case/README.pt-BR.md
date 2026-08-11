<div align="center">

# `match` e `case`: Correspondência de Padrões Estruturais

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Fluxo do Programa](../README.pt-BR.md) · [← Anterior: `if`, `elif` e `else`](../02-if-elif-and-else/README.pt-BR.md)

Uma instrução `if` pergunta se uma condição é verdadeira no contexto Booleano. Uma instrução `match` pergunta se um valor **corresponde a um padrão**.

Essa diferença começa pequena com valores literais e se torna mais útil quando o valor possui estrutura, como uma tupla ou um dicionário.

**Tempo estimado de estudo:** 110–140 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que significa correspondência de padrões estruturais;
- reconhecer que `match` e `case` foram adicionados no Python 3.10;
- diferenciar correspondência de padrões de condições Booleanas comuns;
- corresponder valores literais com `case`;
- usar `_` como curinga de fallback;
- combinar alternativas com um padrão OR usando `|`;
- explicar por que `case 1 | 2 | 3:` e `case 1, 2, 3:` significam coisas diferentes;
- explicar por que um nome simples como `case value:` captura em vez de comparar com uma variável existente;
- extrair valores de padrões de sequência;
- corresponder chaves selecionadas em padrões de mapping;
- usar um guard para acrescentar uma condição Booleana depois de uma correspondência de padrão bem-sucedida;
- escolher entre `if` e `match` de acordo com a intenção;
- evitar depender de class patterns antes de classes serem apresentadas mais adiante no guia.

## 1. O que é correspondência de padrões estruturais

Correspondência de padrões estruturais compara um valor sujeito com um ou mais padrões.

O modelo mental básico é:

```text
subject value
    ↓
try the first case pattern
    ↓
match succeeds or fails
    ↓
if needed, try the next case
```

Um padrão pode descrever mais do que um único valor exato. Ele também pode descrever o **formato** dos dados e capturar partes desses dados em nomes.

O Python adicionou a instrução `match` na versão 3.10.

## 2. Sintaxe básica

Uma instrução `match` contém uma expressão sujeito seguida por um ou mais blocos `case`:

```python
match subject:
    case pattern_a:
        statement
    case pattern_b:
        statement
```

O Python avalia o sujeito e tenta os padrões dos casos em ordem.

Quando um padrão é bem-sucedido, seu bloco é executado. Normalmente, os blocos `case` posteriores não são tentados depois que um caso é selecionado.

Não existe fallthrough automático de um caso selecionado para o caso seguinte.

## 3. Comece com padrões literais

O padrão mais simples corresponde a um valor literal:

```python
status = "ready"

match status:
    case "ready":
        print("Ready to begin")
    case "paused":
        print("Waiting")
```

Saída:

```text
Ready to begin
```

O sujeito é `status`.

Os padrões são os literais de string `"ready"` e `"paused"`.

Como o primeiro padrão é bem-sucedido, o Python executa esse bloco.

## 4. Adicione um fallback curinga com `_`

O sublinhado `_` é o padrão curinga.

Ele é bem-sucedido sem vincular o sujeito a um nome:

```python
status = "offline"

match status:
    case "ready":
        print("Ready to begin")
    case "paused":
        print("Waiting")
    case _:
        print("Unknown status")
```

Saída:

```text
Unknown status
```

Esse papel se parece com um ramo final de fallback, mas continua sendo um padrão, não uma cláusula `else`.

Como `_` corresponde a qualquer coisa, um caso curinga sem guard deve ficar por último.

## 5. A ordem dos casos importa

Os padrões são tentados de cima para baixo.

Coloque casos mais específicos antes de um fallback amplo:

```python
command = "stop"

match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
```

Saída:

```text
Stopping
```

Quando `"stop"` corresponde, o caso curinga não é selecionado.

## 6. Um `case` pode aceitar várias alternativas

Use `|` para criar um padrão OR:

```python
command = "resume"

match command:
    case "start" | "resume":
        print("Running")
    case "pause":
        print("Paused")
    case _:
        print("Unknown command")
```

Saída:

```text
Running
```

Leia isso como:

```text
match "start" OR "resume"
```

A barra vertical faz parte da sintaxe de padrões neste contexto.

## 7. `case 1 | 2 | 3` não é `case 1, 2, 3`

Essa é uma distinção importante.

Para corresponder a um entre três valores inteiros, use um padrão OR:

```python
option = 2

match option:
    case 1 | 2 | 3:
        print("Known option")
    case _:
        print("Unknown option")
```

Saída:

```text
Known option
```

Mas esta sintaxe significa outra coisa:

```python
case 1, 2, 3:
```

Ela descreve um **padrão de sequência** contendo três posições.

Ela pode corresponder a um sujeito como:

```python
coordinates = (1, 2, 3)

match coordinates:
    case 1, 2, 3:
        print("Exact sequence")
    case _:
        print("Different sequence")
```

Saída:

```text
Exact sequence
```

Então lembre:

```text
1 | 2 | 3  = alternatives
1, 2, 3    = sequence structure
```

## 8. `match` é mais do que um switch tradicional

No começo, casos literais podem parecer semelhantes a instruções `switch` encontradas em algumas linguagens.

Essa comparação é útil apenas como ponto de partida.

Padrões do Python também podem:

- descrever estrutura de sequências;
- descrever estrutura de mappings;
- capturar componentes correspondidos em nomes;
- combinar padrões;
- usar guards depois de uma correspondência estrutural bem-sucedida.

Esse comportamento estrutural é a razão de o recurso ser chamado de **correspondência de padrões estruturais**.

## 9. `match` e `case` são palavras reservadas contextuais

`match` e `case` são soft keywords, chamadas na documentação em português de palavras reservadas contextuais.

Elas têm significado especial nos contextos gramaticais que formam uma instrução match, mas não são reservadas em todos os lugares como palavras-chave comuns.

Para código iniciante, a recomendação prática é simples: ainda prefira nomes descritivos que não reutilizem `match` ou `case` sem necessidade.

Isso evita confusão visual mesmo quando determinado uso seria sintaticamente permitido.

## 10. Capture patterns

Um nome dentro de um padrão pode capturar parte do sujeito.

Considere uma tupla que representa um evento:

```python
event = ("move", 4, -2)

match event:
    case ("move", x, y):
        print(x)
        print(y)
```

Saída:

```text
4
-2
```

O literal `"move"` precisa corresponder ao primeiro item.

Os nomes `x` e `y` capturam o segundo e o terceiro itens.

Depois que o caso selecionado é bem-sucedido, esses nomes contêm os valores correspondidos.

## 11. Um nome simples não compara com uma variável existente

Essa é uma das armadilhas mais importantes para iniciantes em pattern matching.

Suponha que você já tenha:

```python
expected = "ready"
status = "paused"
```

Isto **não** significa "comparar status com expected":

```python
match status:
    case expected:
        print(expected)
```

Aqui `expected` é um capture pattern. Ele captura o valor sujeito.

Isso significa que um padrão com nome simples não é a forma normal de comparar com uma variável que já existe.

Para valores conhecidos diretamente no código, use padrões literais como:

```python
case "ready":
```

Quando sua intenção real é uma comparação Booleana arbitrária com valores de runtime, uma instrução `if` costuma ser mais clara.

## 12. Por que uma captura irrefutável precisa ser a última

Um capture pattern simples é bem-sucedido para qualquer sujeito que possa receber.

Por exemplo:

```python
match status:
    case captured:
        print(captured)
```

Esse caso é irrefutável: sem um guard, ele sempre é bem-sucedido.

Um caso irrefutável sem guard não pode ser seguido por outro bloco `case`, porque os casos posteriores nunca poderiam ser selecionados.

O curinga `_` também é irrefutável, mas, diferente de um nome de captura, ele não vincula o sujeito.

## 13. Padrões de sequência

Padrões de sequência permitem descrever posições dentro de dados com comportamento de sequência.

Por exemplo:

```python
point = (3, 7)

match point:
    case (x, y):
        print(f"x={x}, y={y}")
```

Saída:

```text
x=3, y=7
```

As duas posições são capturadas.

Um padrão de sequência com tamanho fixo exige o número esperado de elementos.

## 14. Combine literais e capturas em uma sequência

Padrões ficam mais descritivos quando algumas posições são fixas e outras são capturadas:

```python
event = ("message", "Hello")

match event:
    case ("move", x, y):
        print(f"Move to {x}, {y}")
    case ("message", text):
        print(text)
    case _:
        print("Unknown event")
```

Saída:

```text
Hello
```

Isso é mais do que comparar a tupla inteira por igualdade.

O padrão verifica a estrutura e extrai o componente relevante ao mesmo tempo.

## 15. Listas e tuplas podem corresponder a padrões de sequência

A sintaxe de padrão de sequência descreve uma estrutura de sequência, não necessariamente uma sintaxe visual exata do sujeito.

Por exemplo:

```python
point = [8, 5]

match point:
    case (x, y):
        print(f"Point: {x}, {y}")
```

Saída:

```text
Point: 8, 5
```

Um sujeito lista pode satisfazer esse padrão de sequência com dois itens.

Não leia os parênteses de um padrão como "o sujeito precisa ser uma tupla".

## 16. Strings não são tratadas como padrões de sequência aqui

Embora strings sejam sequências em muitas operações Python, padrões de sequência intencionalmente não tratam `str`, `bytes` ou `bytearray` como sujeitos de sequência.

Faça correspondência de texto usando padrões literais ou outra lógica apropriada em vez de esperar pattern matching caractere por caractere.

Por exemplo:

```python
word = "go"

match word:
    case "go":
        print("Go")
    case _:
        print("Other word")
```

Saída:

```text
Go
```

## 17. Padrões de sequência com estrela

Um padrão com estrela pode capturar uma parte intermediária ou restante de tamanho variável:

```python
values = [10, 20, 30, 40]

match values:
    case [first, *middle, last]:
        print(first)
        print(middle)
        print(last)
```

Saída:

```text
10
[20, 30]
40
```

A captura com estrela recebe uma lista contendo os itens intermediários não correspondidos.

Use isso quando a estrutura de tamanho variável fizer parte do significado dos dados, não apenas como uma forma esperta de desempacotar tudo.

## 18. Padrões de mapping

Padrões de mapping permitem corresponder chaves selecionadas em dados semelhantes a mappings.

Um dicionário é o exemplo mais familiar:

```python
request = {
    "action": "open",
    "resource": "chapter",
}

match request:
    case {"action": "open", "resource": resource}:
        print(resource)
    case _:
        print("Unsupported request")
```

Saída:

```text
chapter
```

A chave `"action"` precisa ter o valor literal `"open"`.

O valor associado a `"resource"` é capturado em `resource`.

## 19. Padrões de mapping não exigem que o mapping tenha apenas aquelas chaves

Um padrão de mapping pode corresponder mesmo quando o sujeito possui chaves adicionais não mencionadas pelo padrão:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "theme": "dark",
}

match request:
    case {"action": "open", "resource": resource}:
        print(resource)
```

Saída:

```text
chapter
```

A chave extra `"theme"` não impede esse padrão de ser bem-sucedido.

Isso difere de um padrão de sequência com tamanho fixo, em que o número de posições é significativo, a menos que seja usado um padrão com estrela.

## 20. Capture itens restantes de um mapping com `**rest`

Quando as chaves restantes importam, uma captura com duas estrelas pode coletá-las:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "theme": "dark",
}

match request:
    case {"action": "open", **rest}:
        print(rest)
```

Saída:

```text
{'resource': 'chapter', 'theme': 'dark'}
```

A captura recebe um dicionário contendo os itens de mapping não correspondidos.

## 21. Guards adicionam uma condição depois que um padrão é bem-sucedido

Um caso pode incluir um guard com `if`:

```python
request = {
    "action": "open",
    "level": 3,
}

match request:
    case {"action": "open", "level": level} if level >= 2:
        print("Advanced access")
    case {"action": "open"}:
        print("Basic access")
```

Saída:

```text
Advanced access
```

A ordem é:

```text
pattern succeeds
    ↓
evaluate the guard
    ↓
if the guard is truthy, select the case
otherwise try the next case
```

Guards conectam este capítulo diretamente à lógica Booleana e aos conceitos de `if` aprendidos anteriormente.

## 22. Um guard não faz parte do padrão estrutural

Mantenha os dois trabalhos separados no seu modelo mental:

```text
pattern = does the value have the required form?
guard   = does an additional condition hold?
```

Por exemplo:

```python
record = ("score", 82)

match record:
    case ("score", value) if value >= 70:
        print("Passing score")
    case ("score", value):
        print("Score below threshold")
```

Saída:

```text
Passing score
```

A estrutura da tupla corresponde primeiro. O limite numérico é verificado depois pelo guard.

## 23. `match` versus `if`

Nenhuma das ferramentas substitui a outra.

Use `if` quando a ideia principal for uma condição Booleana arbitrária:

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

Use `match` quando a ideia principal for selecionar comportamento de acordo com o padrão ou a estrutura de um valor:

```python
event = ("click", 10, 20)

match event:
    case ("click", x, y):
        print(f"Click at {x}, {y}")
    case _:
        print("Other event")
```

Pergunte qual das duas ideias descreve melhor o problema.

## 24. Quando um `if` simples pode ser mais claro

Não use `match` apenas porque ele é uma sintaxe mais nova.

Para uma comparação direta, isto é claro:

```python
if temperature > 30:
    print("Hot day")
```

Transformar cada pequena condição em pattern matching pode adicionar cerimônia sem adicionar significado.

Prefira a construção que torna a decisão mais fácil de entender.

## 25. Quando `match` se torna especialmente expressivo

`match` se torna útil quando vários casos compartilham um vocabulário estruturado.

Exemplos incluem dados fictícios como:

```text
("move", x, y)
("message", text)
("quit",)
```

ou mappings como:

```text
{"action": "open", "resource": ...}
{"action": "close", "resource": ...}
```

O próprio padrão documenta o formato esperado enquanto seleciona o comportamento.

## 26. Erro comum: esperar fallthrough

O Python seleciona o primeiro caso cujo padrão é bem-sucedido e cujo guard, se existir, seja truthy.

Ele não continua automaticamente para o próximo bloco `case` depois disso.

Você não precisa de um `break` no final de cada caso.

Isso difere do comportamento de algumas construções switch tradicionais de outras linguagens.

## 27. Erro comum: usar vírgulas para alternativas

Modelo mental incorreto:

```python
case 1, 2, 3:
```

Isso não significa "1 ou 2 ou 3".

Para alternativas, escreva:

```python
case 1 | 2 | 3:
```

Use vírgulas quando você realmente quiser representar estrutura de sequência.

## 28. Erro comum: usar um nome de variável simples como constante

Este padrão captura:

```python
case expected:
```

Ele normalmente não significa "comparar com o valor atual armazenado em `expected`".

Para código iniciante, prefira:

- padrões literais quando as alternativas forem valores literais;
- uma condição `if` quando estiver comparando com variáveis de runtime;
- técnicas mais avançadas de value patterns somente depois que os conceitos de apoio estiverem compreendidos.

## 29. Erro comum: colocar `_` cedo demais

Esta estrutura está conceitualmente errada porque o curinga tornaria as alternativas posteriores inalcançáveis:

```python
match command:
    case _:
        print("Anything")
    case "start":
        print("Start")
```

Coloque padrões amplos de fallback por último.

## 30. Erro comum: forçar padrões profundamente complexos

Padrões podem se tornar sofisticados, mas código iniciante não ganha nada transformando um `case` em um quebra-cabeça.

Se um padrão mistura estruturas aninhadas demais, capturas, alternativas OR e guards, considere se decisões menores comunicariam melhor a intenção.

Código legível continua sendo o objetivo.

## 31. Limite de escopo: class patterns ficam para depois

Correspondência de padrões estruturais também pode trabalhar com class patterns.

Este guia não exige isso aqui porque classes ainda não foram apresentadas na sequência para iniciantes.

Por enquanto, este capítulo permanece dentro de conceitos já disponíveis:

- literais;
- listas e tuplas;
- dicionários;
- nomes e atribuição;
- condições Booleanas;
- condições Booleanas usadas como guards.

Class patterns podem ser revisitados depois que conceitos de orientação a objetos fizerem parte do repertório do aluno.

## 32. Exemplo trabalhado: escolhas literais

O arquivo [`examples/literal_and_or_patterns.py`](examples/literal_and_or_patterns.py) contém:

```python
command = "pause"

match command:
    case "start" | "resume":
        message = "Session running"
    case "pause":
        message = "Session paused"
    case "stop":
        message = "Session stopped"
    case _:
        message = "Unknown command"

print(message)
```

Saída esperada:

```text
Session paused
```

Observe que `"start" | "resume"` agrupa duas alternativas literais em um único caso.

## 33. Exemplo trabalhado: estrutura de sequência

O arquivo [`examples/sequence_patterns.py`](examples/sequence_patterns.py) contém:

```python
event = ("move", 4, -2)

match event:
    case ("move", x, y):
        print(f"Move to: {x}, {y}")
    case ("message", text):
        print(f"Message: {text}")
    case _:
        print("Unknown event")
```

Saída esperada:

```text
Move to: 4, -2
```

O primeiro item identifica o tipo de evento. Os itens restantes são capturados como dados.

## 34. Exemplo trabalhado: padrão de mapping mais guard

O arquivo [`examples/mapping_patterns_and_guards.py`](examples/mapping_patterns_and_guards.py) contém:

```python
request = {
    "action": "open",
    "resource": "chapter",
    "level": 2,
    "theme": "dark",
}

match request:
    case {"action": "open", "resource": resource, "level": level} if level >= 2:
        print(f"Open advanced resource: {resource}")
    case {"action": "open", "resource": resource}:
        print(f"Open resource: {resource}")
    case _:
        print("Unsupported request")
```

Saída esperada:

```text
Open advanced resource: chapter
```

O mapping contém uma chave extra `"theme"`, mas o primeiro padrão ainda pode corresponder porque padrões de mapping não exigem que o sujeito contenha apenas as chaves listadas.

## 35. Exercício

Crie uma variável chamada `event` contendo um destes valores fictícios:

```python
("login", "Mina")
("logout", "Mina")
("move", 3, 8)
("unknown",)
```

Escreva uma única instrução `match` que:

1. capture e exiba o nome para `("login", name)`;
2. capture e exiba o nome para `("logout", name)`;
3. capture e exiba as duas coordenadas para `("move", x, y)`;
4. use `_` para qualquer outro valor.

Depois adicione um segundo exemplo pequeno em que uma variável inteira chamada `option` aceite `1`, `2` ou `3` em um único caso usando `|`.

Ainda não use `for`, `while`, funções, exceções ou comprehensions.

## 36. Extensão do exercício

Crie este dicionário:

```python
request = {
    "action": "download",
    "file": "guide.pdf",
    "size_mb": 8,
}
```

Use um padrão de mapping e um guard para que:

- um download com `size_mb <= 10` exiba `"Small download"`;
- outro pedido de download exiba `"Large download"`;
- qualquer outra ação chegue ao `_`.

Mantenha o exemplo determinístico e não interativo.

## 37. Checklist de revisão

Antes de avançar, confirme que você consegue explicar cada afirmação sem executar o código:

- [ ] `match` avalia um sujeito e o compara com padrões.
- [ ] os casos são considerados em ordem.
- [ ] apenas o primeiro bloco de caso selecionado é executado.
- [ ] `_` é um curinga e não vincula um nome.
- [ ] `|` cria alternativas de padrão.
- [ ] vírgulas podem descrever estrutura de sequência em vez de alternativas.
- [ ] um nome simples de captura não é uma comparação normal com constante.
- [ ] padrões de sequência podem extrair componentes posicionais.
- [ ] padrões de mapping podem extrair valores por chaves.
- [ ] chaves extras de mapping não impedem automaticamente uma correspondência.
- [ ] um guard adiciona uma condição Booleana depois que a correspondência estrutural é bem-sucedida.
- [ ] `if` continua útil para decisões Booleanas arbitrárias.
- [ ] class patterns são intencionalmente adiados nesta trilha de aprendizagem.

## 38. Referência rápida

| Necessidade | Forma típica |
|---|---|
| Corresponder um literal | `case "start":` |
| Corresponder várias alternativas | `case "start" | "resume":` |
| Fallback | `case _:` |
| Corresponder uma sequência de dois itens | `case (x, y):` |
| Corresponder uma sequência identificada | `case ("move", x, y):` |
| Capturar restante com tamanho variável | `case [first, *rest]:` |
| Corresponder chaves selecionadas de mapping | `case {"action": "open", "resource": resource}:` |
| Capturar itens extras de mapping | `case {"action": "open", **rest}:` |
| Adicionar uma condição | `case pattern if condition:` |
| Decisão Booleana arbitrária | geralmente `if condition:` |

Lembre da progressão:

**sujeito → padrão → capturas opcionais → guard opcional → bloco selecionado**

## Próximo passo

O próximo capítulo é **Loops `for` e Iteração**.

Agora você sabe como o Python pode selecionar comportamento a partir de condições e de padrões de dados. Em seguida, o guia passa de **seleção** para **repetição**, usando `for` para processar itens de um iterável um de cada vez.

## Referências oficiais

- [Referência da linguagem Python 3.13: a instrução `match`](https://docs.python.org/pt-br/3.13/reference/compound_stmts.html#the-match-statement)
- [Tutorial Python 3.13: instruções `match`](https://docs.python.org/pt-br/3.13/tutorial/controlflow.html#match-statements)
- [PEP 634: Structural Pattern Matching — Specification](https://peps.python.org/pep-0634/)
- [PEP 636: Structural Pattern Matching — Tutorial](https://peps.python.org/pep-0636/)
