<div align="center">

# Escolhendo e Combinando o Fluxo do Programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Fluxo do Programa](../README.pt-BR.md) · [← Anterior: `break`, `continue` e `else` de Loops](../07-break-continue-and-loop-else/README.pt-BR.md)

Conhecer cada ferramenta de fluxo do programa separadamente é apenas o começo. Programas reais normalmente precisam que **seleção e repetição trabalhem juntas**.

Este capítulo encerra a Fase 4 transformando as ferramentas anteriores em um sistema de decisão. O objetivo não é usar mais sintaxe. O objetivo é escolher a **estrutura de controle de fluxo mais simples que corresponda ao motivo real pelo qual o programa precisa ramificar ou repetir**.

**Tempo estimado de estudo:** 120–150 minutos.

**Requisito de Python:** Python 3.10 ou posterior. Este capítulo combina `match` / `case` e `zip(..., strict=True)`, ambos introduzidos no Python 3.10.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- escolher `if`, `elif` e `else` quando condições booleanas decidirem o que é executado;
- escolher `match` quando um único valor for comparado com padrões claros;
- escolher `for` quando itens de um iterável guiarem a repetição;
- escolher `while` quando um estado em mudança ou uma condição reavaliada guiar a repetição;
- escolher `range()`, `enumerate()` e `zip()` de acordo com a necessidade da iteração;
- usar `break`, `continue` e `else` de loops apenas quando expressarem uma necessidade real de controle de fluxo;
- combinar decisões e loops sem criar aninhamento desnecessário;
- distinguir ramificações mutuamente exclusivas de condições independentes;
- preferir iteração direta em vez de gerenciamento manual de índices quando o iterável for o verdadeiro condutor;
- rastrear fluxos combinados uma camada de cada vez;
- explicar a intenção de uma estrutura de controle de fluxo em linguagem comum;
- reconhecer quando um fluxo maior deverá ser dividido em funções mais adiante;
- revisar toda a Fase de Fluxo do Programa como uma caixa de ferramentas conectada.

## 1. Comece pela pergunta de controle

Não comece perguntando:

> Qual palavra-chave do Python eu posso usar aqui?

Comece perguntando:

> O que determina o próximo passo deste programa?

Essa pergunta geralmente aponta para a ferramenta correta.

| Pergunta real | Primeira ferramenta a considerar |
|---|---|
| Este bloco deve ser executado? | `if` |
| Qual de várias alternativas booleanas é verdadeira? | `if` / `elif` / `else` |
| Com qual padrão um único valor corresponde? | `match` / `case` |
| O que deve acontecer para cada item? | `for` |
| Quantos passos numéricos devem ser executados? | `range()` com `for` |
| Qual é a posição deste item? | `enumerate()` |
| Quais itens correspondentes pertencem juntos? | `zip()` |
| A repetição deve continuar enquanto uma condição permanecer verdadeira? | `while` |
| O resultado já é conhecido e o loop pode parar? | `break` |
| Esta única iteração deve ser ignorada? | `continue` |
| O loop terminou sem `break`? | `else` do loop |

Isto é um ponto de partida, não uma lei. Várias estruturas podem ser tecnicamente válidas. Prefira aquela cujo formato explica a intenção com mais clareza.

## 2. Escolha pela intenção, não pelo hábito

Depois de aprender um recurso novo, é tentador usá-lo em todos os lugares.

Isso inverte o processo de projeto.

Compare:

```text
Process each order in this list.
```

com:

```text
Keep trying while the balance is below the target.
```

A primeira frase sugere naturalmente `for`.

A segunda sugere naturalmente `while`.

Uma estrutura de controle de fluxo útil deve tornar o programa mais fácil de descrever.

## 3. Use `if` para regras booleanas

Use `if` quando a pergunta importante puder ser expressa como uma condição booleana.

```python
temperature = 31

if temperature >= 30:
    print("Hot")
else:
    print("Mild")
```

`if` é especialmente natural para:

- faixas e desigualdades;
- condições combinadas com `and`, `or` e `not`;
- testes de pertencimento;
- condições envolvendo vários valores.

Exemplo:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

Este é um problema de condição booleana.

## 4. Ramificações mutuamente exclusivas versus condições independentes

Uma cadeia `if` / `elif` / `else` representa alternativas em que, no máximo, uma ramificação deve executar.

```python
score = 82

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Ready")
else:
    print("Review")
```

Instruções `if` independentes fazem perguntas independentes:

```python
number = 12

if number > 0:
    print("Positive")

if number % 2 == 0:
    print("Even")
```

As duas instruções podem executar.

Pergunte:

> Mais de uma resposta pode ser verdadeira ao mesmo tempo?

Se sim, instruções `if` independentes podem ser apropriadas.

## 5. A ordem importa em `if` / `elif`

Considere:

```python
score = 95

if score >= 70:
    print("Ready")
elif score >= 90:
    print("Excellent")
```

`95` imprime `"Ready"` porque a primeira condição já foi satisfeita.

Uma ordem melhor é:

```python
score = 95

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Ready")
```

Quando as condições se sobrepõem, coloque-as em uma ordem que preserve as categorias pretendidas.

## 6. Use `match` para padrões em torno de um único valor

`match` é útil quando um valor é comparado com vários padrões significativos.

```python
status = "running"

match status:
    case "queued":
        print("Waiting")
    case "running":
        print("Working")
    case "done":
        print("Finished")
    case _:
        print("Unknown")
```

O modelo mental é:

```text
Take this subject and determine which pattern it matches.
```

Um fallback curinga como `case _:` normalmente fica depois dos padrões mais específicos.

## 7. `match` não substitui `if`

Isto é naturalmente booleano:

```python
amount = 125

if amount > 100:
    print("High amount")
```

Isto é naturalmente baseado em padrões:

```python
command = ["move", 3]

match command:
    case ["move", steps]:
        print(f"Move {steps} steps")
    case ["stop"]:
        print("Stop")
    case _:
        print("Unknown command")
```

Use `match` porque os padrões melhoram o modelo, não porque a sintaxe é mais nova.

## 8. Use `for` quando um iterável guia a repetição

Se o requisito disser:

> Para cada item desta coleção...

comece considerando `for`.

```python
names = ["Ana", "Leo", "Mia"]

for name in names:
    print(name)
```

O iterável controla a repetição.

## 9. Prefira iteração direta ao gerenciamento manual de índices

Isto normalmente é desnecessário:

```python
names = ["Ana", "Leo", "Mia"]
index = 0

while index < len(names):
    print(names[index])
    index += 1
```

A própria lista é o verdadeiro condutor, então isto é mais claro:

```python
names = ["Ana", "Leo", "Mia"]

for name in names:
    print(name)
```

Use índices somente quando os índices realmente fizerem parte do problema.

## 10. Use `while` quando uma condição ou um estado em mudança guia a repetição

```python
balance = 0
target = 100

while balance < target:
    balance += 25
    print(balance)
```

O programa está dizendo:

```text
keep going while this condition remains true
```

Esse é o modelo que `while` expressa.

## 11. `for` versus `while`

Pergunte o que cria a próxima iteração.

| A repetição é controlada por... | Prefira considerar... |
|---|---|
| itens de um iterável | `for` |
| uma progressão numérica | `for` + `range()` |
| estado em mudança ou uma condição | `while` |
| um processo indefinido com uma regra interna clara de parada | `while True` deliberado + `break` |

Use a descrição verdadeira mais simples.

## 12. Escolha o auxiliar de iteração pela informação que está faltando

### `range()` para uma progressão numérica

```python
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
```

### `enumerate()` para item mais posição

```python
tasks = ["read", "practice", "review"]

for position, task in enumerate(tasks, start=1):
    print(position, task)
```

### `zip()` para itens correspondentes

```python
names = ["Ana", "Leo"]
scores = [92, 81]

for name, score in zip(names, scores, strict=True):
    print(name, score)
```

Os auxiliares respondem a perguntas diferentes:

```text
range()      → which numeric progression?
enumerate()  → which item and which position?
zip()        → which corresponding items?
```

Eles apoiam um loop `for` em vez de substituir seu modelo guiado por iterável.

## 13. Use `zip(strict=True)` quando comprimentos iguais forem uma regra

Por padrão, `zip()` para quando o menor iterável se esgota.

Quando comprimentos iguais forem uma regra dos dados, use:

```python
for name, score in zip(names, scores, strict=True):
    print(name, score)
```

Se um iterável tiver inesperadamente um item extra, `strict=True` gera um erro em vez de truncar silenciosamente os pares.

Se comprimentos diferentes e truncamento forem intencionais, `zip()` comum pode ser a escolha correta.

## 14. Combine um loop com uma decisão quando cada item precisar de classificação

Uma estrutura comum é:

```text
for each item
    decide what this item means
```

Exemplo:

```python
scores = [92, 67, 81, 45]

for score in scores:
    if score >= 90:
        label = "excellent"
    elif score >= 70:
        label = "ready"
    else:
        label = "review"

    print(f"{score}: {label}")
```

A estrutura externa responde **como a repetição acontece**.

A estrutura interna responde **o que acontece com este item**.

## 15. Construa o fluxo combinado de fora para dentro

Requisito:

> Para cada medição, imprima somente os valores positivos.

Primeiro pergunte o que se repete.

Resposta:

```text
each measurement
```

Então comece com `for`.

Depois pergunte quais medições devem ser impressas.

```python
measurements = [3, -1, 5, 0]

for measurement in measurements:
    if measurement > 0:
        print(measurement)
```

Escolha primeiro o condutor externo e depois adicione as decisões necessárias dentro dele.

## 16. Use `continue` quando pular cedo deixar o caminho principal mais claro

O mesmo requisito pode ser escrito:

```python
measurements = [3, -1, 5, 0]

for measurement in measurements:
    if measurement <= 0:
        continue

    print(measurement)
```

Isto diz:

```text
reject items that should not continue through the body
then keep the normal path less indented
```

As duas versões são válidas.

Use `continue` apenas quando ele melhorar a legibilidade.

## 17. Não adicione `continue` quando o fim natural da iteração já disser a mesma coisa

Isto é desnecessário:

```python
for number in [1, 2, 3]:
    if number != 2:
        print(number)
        continue
```

A iteração terminaria naturalmente depois de `print()`.

Uma instrução de controle deve comunicar uma mudança real no fluxo.

## 18. Use `break` quando mais iterações não puderem melhorar a resposta

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for item in items:
    if item == target:
        print("Found")
        break
```

Depois que a primeira correspondência necessária é encontrada, examinar itens posteriores não mudaria a resposta.

Esse é um motivo forte para `break`.

## 19. Use `else` de loop quando terminar sem `break` tiver significado

```python
items = ["pen", "book", "cable"]
target = "mug"

for item in items:
    if item == target:
        print("Found")
        break
else:
    print("Not found")
```

O `else` do loop significa:

```text
the loop completed without executing break
```

Ele não significa que a última condição `if` foi falsa.

## 20. Um padrão de busca útil combina várias ferramentas com clareza

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for position, item in enumerate(items, start=1):
    if item == target:
        print(f"Found {target} at position {position}")
        break
else:
    print(f"{target} not found")
```

Cada camada tem uma responsabilidade:

```text
enumerate() → expose position and item
for         → inspect items
if          → test for the target
break       → stop after the first match
else        → handle no-match completion
```

Esta é uma combinação saudável porque as ferramentas não competem pelo mesmo trabalho.

## 21. `while` combina naturalmente com decisões

```python
progress = 0

while progress < 3:
    progress += 1

    if progress == 2:
        print("Checkpoint")
    else:
        print("Progress", progress)
```

`while` decide se existe outro ciclo.

`if` decide o que acontece durante o ciclo atual.

## 22. `while` e `match` podem modelar estados explícitos

```python
state = "queued"

while state != "done":
    match state:
        case "queued":
            print("Preparing")
            state = "running"
        case "running":
            print("Processing")
            state = "done"
        case _:
            print("Unknown state")
            break
```

As funções são distintas:

```text
while → continue until the workflow reaches its final state
match → choose the action for the current state
```

## 23. Mantenha o progresso do `while` visível

O leitor deve conseguir responder:

> O que faz este loop avançar em direção ao fim?

Prefira atualizações de estado fáceis de localizar:

```python
attempt = 0

while attempt < 3:
    attempt += 1
    print(attempt)
```

Tenha cuidado quando o estado que controla a condição muda apenas dentro de algumas ramificações profundamente aninhadas.

## 24. Tenha cuidado com `continue` dentro de `while`

Isto pode entrar em loop infinito:

```python
count = 0

while count < 3:
    if count == 1:
        continue

    count += 1
```

Quando `count` se torna `1`, `continue` retorna para a condição antes de `count` mudar.

Uma forma mais segura é:

```python
count = 0

while count < 3:
    count += 1

    if count == 2:
        continue

    print(count)
```

A atualização acontece antes do possível `continue`.

A organização exata pode variar, mas todo caminho deve preservar o progresso.

## 25. Use `while True` somente quando a regra interna de parada for mais clara

Uma condição infinita deliberada pode fazer sentido quando a verdadeira regra de parada fica dentro do corpo:

```python
attempt = 0

while True:
    attempt += 1
    print(attempt)

    if attempt >= 3:
        break
```

Mas quando a própria condição já expressa a regra claramente:

```python
attempt = 0

while attempt < 3:
    attempt += 1
    print(attempt)
```

a condição direta normalmente é mais fácil de entender.

Não use `while True` como modelo padrão.

## 26. Prefira um condutor principal claro por loop

Uma diretriz útil de legibilidade é:

> Cada loop deve ter um motivo principal para continuar.

Em um loop `for`, esse motivo normalmente é:

```text
there is another item
```

Em um loop `while`, normalmente é:

```text
the condition is still true
```

`if`, `break` e `continue` podem refinar o comportamento, mas o condutor principal deve continuar visível.

Isto é uma recomendação de legibilidade, não uma regra de sintaxe do Python.

## 27. Achate o fluxo somente quando a versão mais plana for mais clara

Condições aninhadas:

```python
values = [3, -1, 5, 0]

for value in values:
    if value > 0:
        if value % 2 == 1:
            print(value)
```

Condição combinada:

```python
values = [3, -1, 5, 0]

for value in values:
    if value > 0 and value % 2 == 1:
        print(value)
```

Pulos antecipados:

```python
values = [3, -1, 5, 0]

for value in values:
    if value <= 0:
        continue

    if value % 2 == 0:
        continue

    print(value)
```

Todas são possíveis.

Prefira aquela que torna o caminho de sucesso e as regras de rejeição mais fáceis de explicar.

## 28. Evite auxiliares sobrepostos quando uma ferramenta expressar a intenção diretamente

Isto funciona:

```python
items = ["pen", "book", "mug"]

for index in range(len(items)):
    item = items[index]
    print(index, item)
```

Mas se a necessidade real for posição mais item:

```python
items = ["pen", "book", "mug"]

for index, item in enumerate(items):
    print(index, item)
```

a segunda versão comunica a intenção de forma mais direta.

## 29. Explique o fluxo em linguagem comum antes de defender a sintaxe

Exemplo:

```text
For each score:
    classify it into exactly one category;
    then print the score and category.
```

Isso se mapeia naturalmente para:

```text
for
    if / elif / else
```

Outro exemplo:

```text
Keep processing while the workflow is not done.
For the current state, choose the matching action.
```

Isso se mapeia naturalmente para:

```text
while
    match
```

Se a explicação em linguagem comum estiver confusa, o código pode estar fazendo coisas demais.

## 30. Rastreie o fluxo combinado uma camada de cada vez

Considere:

```python
values = [2, 5, 8]

for value in values:
    if value % 2 == 0:
        print(value)
```

Rastreie primeiro o loop externo:

| Iteração | `value` |
|---|---:|
| 1 | 2 |
| 2 | 5 |
| 3 | 8 |

Depois avalie a condição interna:

| `value` | `value % 2 == 0` | Impresso? |
|---:|---|---|
| 2 | `True` | sim |
| 5 | `False` | não |
| 8 | `True` | sim |

Para um loop `while`, rastreie o estado que controla a condição.

Rastrear por camadas é mais fácil do que executar mentalmente todas as linhas de uma vez.

## 31. Exemplo 1: iterar e classificar

Arquivo: [`examples/select_and_classify.py`](examples/select_and_classify.py)

```python
scores = [92, 67, 81, 45]

for score in scores:
    if score >= 90:
        label = "excellent"
    elif score >= 70:
        label = "ready"
    else:
        label = "review"

    print(f"{score}: {label}")
```

Saída:

```text
92: excellent
67: review
81: ready
45: review
```

Por que essas ferramentas?

- `for` porque cada nota deve ser processada;
- `if` / `elif` / `else` porque cada nota pertence a exatamente uma categoria booleana.

## 32. Exemplo 2: busca com posição e tratamento da conclusão

Arquivo: [`examples/search_with_position.py`](examples/search_with_position.py)

```python
items = ["pen", "book", "cable", "mug"]
target = "cable"

for position, item in enumerate(items, start=1):
    if item == target:
        print(f"Found {target} at position {position}")
        break
else:
    print(f"{target} not found")
```

Saída:

```text
Found cable at position 3
```

Por que essas ferramentas?

- `enumerate()` porque tanto o item quanto a posição amigável ao usuário importam;
- `for` porque o iterável guia a busca;
- `if` porque a igualdade decide se o alvo foi encontrado;
- `break` porque a primeira correspondência é suficiente;
- `else` do loop porque esgotar o iterável sem `break` significa "não encontrado".

## 33. Exemplo 3: fluxo guiado por estado

Arquivo: [`examples/state_driven_workflow.py`](examples/state_driven_workflow.py)

```python
state = "queued"
processed_steps = 0

while state != "done":
    match state:
        case "queued":
            print("Preparing")
            state = "running"
        case "running":
            print("Processing")
            processed_steps += 1

            if processed_steps >= 2:
                state = "done"
        case _:
            print("Unknown state")
            break

print(f"Final state: {state}")
```

Saída:

```text
Preparing
Processing
Processing
Final state: done
```

Por que essas ferramentas?

- `while` porque a conclusão depende de um estado de workflow que evolui;
- `match` porque um estado seleciona uma ação específica daquele estado;
- `if` porque o estado em execução tem uma regra adicional de limite;
- `break` porque um estado desconhecido invalidaria o fluxo normal.

## 34. Compare formatos válidos antes de escolher

Requisito:

> Imprima valores positivos.

Uma forma direta:

```python
values = [3, -1, 5]

for value in values:
    if value > 0:
        print(value)
```

Uma forma com pulo antecipado:

```python
values = [3, -1, 5]

for value in values:
    if value <= 0:
        continue

    print(value)
```

Uma forma com índice manual:

```python
values = [3, -1, 5]
index = 0

while index < len(values):
    value = values[index]
    index += 1

    if value > 0:
        print(value)
```

Todas podem produzir a saída desejada.

A primeira normalmente é a mais clara porque:

- a coleção guia a repetição;
- a condição é simples;
- nenhum pulo antecipado é necessário;
- nenhum estado manual de índice é necessário.

Correção é necessária, mas clareza também importa.

## 35. Uma receita de decisão para fluxo do programa

Ao enfrentar um problema novo, pergunte:

1. **Seleção ou repetição?**
2. Se for seleção, a regra é **booleana** ou **baseada em padrões**?
3. Se for repetição, o próximo ciclo vem de um **iterável** ou de uma **condição**?
4. O loop `for` precisa de `range()`, `enumerate()` ou `zip()`?
5. O caminho normal do loop realmente precisa de `break` ou `continue`?
6. Terminar sem `break` tem um resultado significativo que o `else` do loop pode expressar?

Não escolha todas as ferramentas de uma vez.

Construa a estrutura a partir do requisito.

## 36. Erros comuns

### Escolher a sintaxe antes de modelar o requisito

Fraco:

```text
I need to use match somewhere.
```

Melhor:

```text
I have one value with several meaningful patterns.
match may fit this model.
```

### Percorrer uma coleção normal com indexação manual em `while`

Se você só precisa de cada item, `for` normalmente expressa isso diretamente.

### Usar `range(len(...))` quando apenas os itens são necessários

Não fabrique índices automaticamente.

### Usar `match` para faixas numéricas ordenadas

Lógica de limites normalmente fica mais clara com `if` / `elif`.

### Esquecer a ordem das ramificações

O primeiro `elif` verdadeiro ou `case` correspondente altera quais ramificações posteriores continuam alcançáveis.

### Esconder o progresso do `while`

Verifique se todo caminho pode mover o estado em direção ao término.

### Adicionar `break` e `continue` demais

Se o leitor pergunta repetidamente para onde a execução vai em seguida, simplifique o loop.

### Confundir `else` do loop com `else` de `if`

A indentação mostra a qual instrução a cláusula pertence.

### Assumir que menos linhas sempre significam código mais claro

Compacidade e legibilidade não são o mesmo objetivo.

## 37. Exercício: projete um fluxo combinado

Dado:

```python
events = ["ready", "skip", "running", "done", "running"]
```

Escreva um programa que:

1. processe os eventos com `for`;
2. use `enumerate(..., start=1)` para posições amigáveis ao usuário;
3. use `continue` quando o evento for `"skip"`;
4. use `match` para distinguir `"ready"`, `"running"`, `"done"` e eventos desconhecidos;
5. imprima a posição e o evento para `"ready"` e `"running"`;
6. imprima `Done at position X` e use `break` para `"done"`;
7. use `else` do loop para imprimir `No done event` somente se o loop terminar sem `"done"`.

Saída esperada:

```text
1: ready
3: running
Done at position 4
```

Antes de programar, escreva uma frase explicando a responsabilidade de cada ferramenta escolhida.

## 38. Perguntas de revisão do exercício

Depois de concluir o exercício, responda:

- Por que `for` é mais natural do que `while` para a repetição externa?
- Por que `enumerate()` é mais direto do que `range(len(events))`?
- O que `continue` altera para o evento `"skip"`?
- Por que `break` impede o `else` do loop?
- Por que `match` é razoável para os estados dos eventos?
- Parte da lógica poderia ser expressa com `if`?
- Qual versão seria mais fácil de explicar para outro iniciante?

A última pergunta importa. Legibilidade faz parte da qualidade técnica.

## 39. Checklist de revisão

Antes de avançar, confirme que você consegue:

- [ ] explicar a diferença entre seleção e repetição;
- [ ] escolher `if` para regras booleanas;
- [ ] escolher `match` para padrões em torno de um único valor;
- [ ] distinguir ramificações mutuamente exclusivas de condições independentes;
- [ ] escolher `for` para repetição guiada por iterável;
- [ ] escolher `while` para repetição guiada por estado ou condição;
- [ ] escolher `range()`, `enumerate()` e `zip()` de acordo com a intenção;
- [ ] decidir quando `zip(strict=True)` expressa uma regra importante;
- [ ] usar `break` apenas para uma saída antecipada significativa;
- [ ] usar `continue` apenas para um encerramento antecipado significativo da iteração atual;
- [ ] explicar `else` do loop como conclusão sem `break`;
- [ ] combinar loops e decisões mantendo cada responsabilidade clara;
- [ ] rastrear fluxos combinados uma camada de cada vez;
- [ ] identificar o estado que controla um loop `while`;
- [ ] reconhecer indexação manual desnecessária;
- [ ] reconhecer aninhamento desnecessário;
- [ ] explicar uma estrutura de controle de fluxo em linguagem comum;
- [ ] reconhecer que fluxos maiores se beneficiarão de funções mais adiante.

## 40. Referência rápida

| Necessidade | Ferramenta a considerar | Ideia principal |
|---|---|---|
| Testar uma regra booleana | `if` | executar um bloco condicionalmente |
| Escolher uma ramificação booleana ordenada | `if` / `elif` / `else` | a primeira condição verdadeira vence |
| Comparar um valor com padrões | `match` / `case` | o primeiro `case` correspondente vence |
| Processar itens de um iterável | `for` | o iterável guia a repetição |
| Gerar progressão de inteiros | `range()` | produzir sequência aritmética de inteiros |
| Processar item mais posição | `enumerate()` | parear posições com itens |
| Processar iteráveis correspondentes | `zip()` | parear itens pela posição de iteração |
| Exigir entradas de mesmo tamanho em `zip` | `zip(..., strict=True)` | tornar o mesmo tamanho uma regra |
| Repetir enquanto o estado satisfaz uma regra | `while` | a condição guia a repetição |
| Parar o loop mais próximo agora | `break` | término antecipado |
| Pular o restante desta iteração | `continue` | encerramento antecipado da iteração |
| Tratar conclusão sem `break` | `else` do loop | não ocorreu saída antecipada por `break` |

## 41. O modelo mental completo da Fase 4

Fluxo do Programa agora forma uma progressão conectada:

```text
Build a trustworthy condition
        ↓
Choose a branch with if / elif / else
        ↓
Match structured alternatives with match / case
        ↓
Repeat for each iterable item with for
        ↓
Use range / enumerate / zip when iteration needs structure
        ↓
Repeat according to changing state with while
        ↓
Use break / continue / loop else when normal loop flow needs refinement
        ↓
Choose and combine only the tools that match the real requirement
```

O passo final não é outro recurso de sintaxe.

É julgamento.

## 42. Conclusão da Fase 4 e próximos passos

Ao concluir este capítulo, você terminou a fase Fluxo do Programa do Python Study Guide.

Agora você consegue raciocinar sobre:

- condições e lógica booleana;
- ramificações condicionais;
- correspondência de padrões estruturais;
- loops guiados por iteráveis;
- auxiliares de iteração numérica, com posição e paralela;
- loops guiados por estado;
- término antecipado e pulo de iterações;
- conclusão normal de loops;
- combinações dessas ferramentas.

Esta fase intencionalmente ainda não exige:

- funções definidas pelo usuário com `def`;
- parâmetros e valores de retorno;
- escopo de funções;
- tratamento de exceções;
- manipulação de arquivos;
- comprehensions;
- módulos e pacotes;
- bibliotecas externas.

À medida que o fluxo de controle cresce, funções se tornam a próxima ferramenta natural porque permitem **nomear e separar responsabilidades**.

A próxima fase de aprendizagem planejada é a **Fase 5: Funções**.

Volte para a [trilha completa de estudos](../../docs/learning-path.pt-BR.md) ou para o [roadmap](../../docs/roadmap.pt-BR.md) para continuar quando a Fase 5 for publicada.

## Referências

Referências primárias usadas neste capítulo:

- [Python 3.13 Tutorial: More Control Flow Tools](https://docs.python.org/3.13/tutorial/controlflow.html)
- [Python 3.13 Language Reference: Compound Statements](https://docs.python.org/3.13/reference/compound_stmts.html)
- [Python 3.13 Built-in Functions](https://docs.python.org/3.13/library/functions.html)
- [Python 3.13 Built-in Types: `range`](https://docs.python.org/3.13/library/stdtypes.html#ranges)
