<div align="center">

# Loops `while` e Repetição Guiada por Estado

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Fluxo do Programa](../README.pt-BR.md) · [← Anterior: `range()`, `enumerate()` e `zip()`](../05-range-enumerate-and-zip/README.pt-BR.md)

Um loop `for` repete um trabalho consumindo itens de um iterável. Um loop `while` responde a uma pergunta diferente:

**Este trabalho deve acontecer novamente com base no estado atual do programa?**

Este capítulo introduz a repetição controlada por uma condição que é testada novamente antes de cada iteração.

**Tempo estimado de estudo:** 105–130 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar o que é um loop `while` e por que ele existe;
- escrever a sintaxe básica `while condition:` com indentação correta;
- explicar que a condição é testada antes de cada iteração;
- reconhecer que o corpo de um `while` pode ser executado zero vezes;
- conectar condições de `while` ao teste de valor de verdade dos capítulos anteriores;
- descrever o ciclo de estado inicial, condição, corpo, atualização de estado e nova avaliação;
- atualizar o estado de forma deliberada para que um loop finito possa avançar em direção ao término;
- usar contadores, acumuladores e limites com `while`;
- explicar por que um loop não precisa chegar exatamente a um limite numérico para terminar;
- distinguir loops `for` guiados por iteráveis de loops `while` guiados por estado;
- reconhecer causas comuns de loops infinitos;
- verificar se uma atualização move o estado em direção ou para longe da condição de parada;
- entender que mais de uma variável pode participar da condição do loop;
- reconhecer que modificar uma coleção também pode alterar o estado testado por um loop;
- entender o que `while True` significa sem usá-lo ainda como exemplo executável seguro;
- manter `break`, `continue` e `else` de loop separados até o próximo capítulo;
- escolher `while` somente quando seu modelo guiado por estado comunicar a tarefa com mais clareza do que `for`.

## 1. Por que `while` existe

Os dois capítulos anteriores se concentraram em repetição guiada por iteráveis:

```python
for item in iterable:
    statement
```

Esse modelo é excelente quando o programa já possui algo para percorrer, como uma lista, string, dicionário, `range`, objeto `enumerate` ou objeto `zip`.

Mas algumas tarefas não são descritas naturalmente como “para cada item”.

Em vez disso, elas soam como:

```text
enquanto houver trabalho restante, continue
enquanto um valor estiver abaixo de um limite, continue atualizando-o
enquanto uma condição permanecer verdadeira, repita o bloco
```

Esse é o papel de `while`.

## 2. A sintaxe básica

A forma básica é:

```python
while condition:
    statement
```

Os dois-pontos encerram o cabeçalho do `while`, e o bloco indentado é o corpo do loop.

Por exemplo:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

Saída:

```text
3
2
1
```

O loop continua executando enquanto `remaining > 0` for verdadeiro.

## 3. Um loop `while` testa antes de executar o corpo

Um loop `while` é um **loop de pré-teste**: o Python avalia a condição antes de entrar no corpo em cada passagem.

O fluxo é:

```text
testar condição
    ↓
verdadeira -> executar corpo -> testar condição novamente
falsa      -> sair do loop
```

Esse detalhe explica vários comportamentos importantes no restante do capítulo.

## 4. O corpo pode ser executado zero vezes

Como a condição é testada primeiro, o corpo é ignorado quando ela já é falsa.

```python
remaining = 0

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Done")
```

Saída:

```text
Done
```

O próprio loop realizou zero iterações.

## 5. `while` usa teste de valor de verdade

A condição não precisa ser um valor escrito literalmente como `True` ou `False`.

O Python testa o valor de verdade da expressão, assim como faz em uma condição de `if`.

Isso significa que as ideias booleanas do Capítulo 01 continuam valendo:

```python
attempts = 2

while attempts:
    print(attempts)
    attempts = attempts - 1
```

Como inteiros diferentes de zero são verdadeiros e zero é falso, isso imprime:

```text
2
1
```

Em código para iniciantes, uma comparação explícita como `while attempts > 0:` muitas vezes é mais fácil de ler porque declara diretamente a regra pretendida.

## 6. O modelo mental central: o estado muda ao longo do tempo

Uma forma útil de raciocinar sobre um loop `while` finito é:

```text
1. estabelecer o estado inicial
2. testar a condição
3. executar o corpo se a condição for verdadeira
4. atualizar o estado relevante
5. voltar à condição
6. parar quando a condição se tornar falsa
```

A nova ideia importante é **estado**: informação cujo valor atual afeta se outra iteração deve acontecer.

## 7. Estado é aquilo de que a condição depende

Neste loop:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

`remaining` é estado do loop porque a condição depende dele.

O estado começa em `3`, depois se torna `2`, `1` e finalmente `0`.

Quando o Python testa `remaining > 0` com `remaining == 0`, a condição é falsa e o loop termina.

## 8. Um loop finito precisa de um caminho para terminar

Se um loop deve terminar normalmente, algo precisa eventualmente tornar sua condição falsa.

Para a contagem regressiva:

```text
estado inicial: 3
condição:       remaining > 0
atualização:    remaining = remaining - 1
```

A atualização move o estado em direção ao ponto em que a condição falha.

Uma pergunta prática ao ler um `while` é:

**O que muda, e como essa mudança pode eventualmente tornar a condição falsa?**

## 9. Contando para cima com `while`

O estado também pode crescer:

```python
number = 1

while number <= 3:
    print(number)
    number = number + 1
```

Saída:

```text
1
2
3
```

A condição se torna falsa depois que `number` muda de `3` para `4`.

## 10. Contando para baixo com `while`

Uma contagem regressiva usa a direção oposta:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

Saída:

```text
3
2
1
Start
```

O `print()` final está fora do loop porque deve executar somente depois que a repetição terminar.

## 11. A indentação decide o que se repete

Compare estas duas formas:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

e:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
    print("Still inside the loop")
```

Somente as instruções indentadas sob o cabeçalho `while` pertencem ao corpo do loop.

A indentação, portanto, faz parte tanto da sintaxe do Python quanto do significado do programa.

## 12. A inicialização vem antes do primeiro teste

A condição normalmente depende de um estado que já precisa existir:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1
```

A atribuição `remaining = 3` acontece antes de o Python chegar ao primeiro teste da condição.

Uma ordem útil de leitura é:

```text
inicializar -> testar -> trabalhar -> atualizar -> testar novamente
```

## 13. A atualização não precisa ser a última instrução

Não existe uma regra do Python dizendo que a atualização de estado deve ser a última linha do corpo.

Porém, posicionar a atualização importante onde ela seja fácil de enxergar costuma melhorar a legibilidade:

```python
progress = 0

while progress < 3:
    progress = progress + 1
    print(f"Progress: {progress}")
```

O requisito central é semântico: o estado do loop muda de uma forma compatível com a condição e com o comportamento pretendido.

## 14. Repetição controlada por limite

Um loop `while` é útil quando a repetição depende de alcançar ou ultrapassar um limite por meio de um estado que muda.

```python
studied_minutes = 0
session_minutes = 20
target_minutes = 60

while studied_minutes < target_minutes:
    studied_minutes = studied_minutes + session_minutes
    print(f"Study total: {studied_minutes} min")
```

Saída:

```text
Study total: 20 min
Study total: 40 min
Study total: 60 min
```

O número de iterações decorre do estado que muda e da condição.

## 15. Um acumulador também pode controlar o loop

Um acumulador armazena um resultado em andamento.

No exemplo anterior, `studied_minutes` é ao mesmo tempo:

- um acumulador que armazena o total corrente;
- estado usado pela condição do `while`.

Uma variável pode exercer mais de um papel quando esses papéis descrevem claramente o mesmo valor em evolução.

## 16. O estado não precisa chegar exatamente ao limite

Considere:

```python
value = 1
limit = 20

while value < limit:
    print(value)
    value = value * 2

print(value)
```

Saída:

```text
1
2
4
8
16
32
```

O loop para porque `32 < 20` é falso no teste seguinte.

Nada exige que o estado se torne exatamente `20`.

A regra de parada é o valor de verdade da condição, não o fato de um valor de limite ter sido visitado exatamente.

## 17. A condição é reavaliada com o estado atual

O Python não calcula a condição uma vez e reutiliza esse resultado para sempre.

Cada passagem volta ao cabeçalho e avalia a expressão novamente usando os valores atuais.

Para:

```python
value = 1

while value < 5:
    value = value * 2
```

O Python efetivamente observa:

```text
1 < 5 -> True
2 < 5 -> True
4 < 5 -> True
8 < 5 -> False
```

Essa reavaliação repetida é o motor de um loop `while`.

## 18. `for` e `while` resolvem formatos diferentes de repetição

Uma primeira distinção útil é:

```text
for   -> repetir para itens de um iterável
while -> repetir enquanto uma condição permanecer verdadeira
```

Por exemplo, quando a tarefa é apenas imprimir os números `1`, `2` e `3`, um loop `for` costuma ser mais claro:

```python
for number in range(1, 4):
    print(number)
```

Uma versão com `while` pode funcionar:

```python
number = 1

while number <= 3:
    print(number)
    number = number + 1
```

Mas ela introduz estado manual que `range()` poderia fornecer diretamente.

## 19. Prefira `for` quando o iterável já expressa a tarefa

Se você já possui uma coleção:

```python
topics = ["conditions", "loops", "functions"]
```

isto é direto:

```python
for topic in topics:
    print(topic)
```

Reconstruir o mesmo percurso manualmente com índices e `while` adicionaria gerenciamento de estado sem melhorar o significado.

Use `while` porque a condição de continuação é o modelo natural, não apenas porque ele consegue imitar `for`.

## 20. Prefira `while` quando a próxima repetição depende do estado atual

Uma tarefa guiada por estado pode não conhecer de antemão seu número útil de iterações.

Por exemplo:

```python
value = 1
limit = 100

while value < limit:
    value = value * 2
```

A ideia importante não é “repita exatamente sete vezes”.

A ideia importante é “continue dobrando enquanto o valor permanecer abaixo do limite”.

Essa intenção combina naturalmente com `while`.

## 21. Loop infinito: esquecer de atualizar o estado

Este loop nunca altera o valor usado pela condição:

```python
remaining = 3

while remaining > 0:
    print(remaining)
```

`remaining > 0` permanece verdadeiro para sempre.

Se executado, o loop continua imprimindo `3` a menos que algo fora do término normal do loop interrompa o programa.

Este exemplo aparece para explicar o erro. Ele intencionalmente não faz parte do manifesto de exemplos executáveis do repositório.

## 22. Loop infinito: atualizar na direção errada

Uma atualização pode existir e ainda assim afastar o estado do término:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining + 1
```

Os valores se tornam `3`, `4`, `5` e assim por diante, portanto `remaining > 0` não se torna falso.

Não pergunte apenas se o estado muda. Pergunte se ele muda **em direção a um estado capaz de encerrar o loop**.

## 23. Loop infinito: redefinir o estado dentro do corpo

Um erro menos óbvio é restaurar repetidamente o mesmo estado:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = 2
```

Depois da primeira passagem, `remaining` permanece em `2` para sempre.

Progresso exige mais do que uma atribuição. A sequência de estados precisa permitir o término.

## 24. Condições podem combinar várias partes do estado

Uma condição de `while` pode usar os operadores booleanos aprendidos anteriormente:

```python
remaining = 5
energy = 3

while remaining > 0 and energy > 0:
    print(remaining, energy)
    remaining = remaining - 1
    energy = energy - 1
```

Saída:

```text
5 3
4 2
3 1
```

O teste seguinte falha porque `energy > 0` se torna falso.

Quando várias variáveis participarem, verifique como cada uma muda e qual parte da condição pode encerrar o loop.

## 25. Coleções podem fazer parte do estado do loop

Estado não se limita a números.

Uma coleção mutável pode mudar de modo a afetar uma condição de `while`:

```python
tasks = ["review", "practice", "recap"]

while tasks:
    current = tasks.pop()
    print(current)
```

Saída:

```text
recap
practice
review
```

A lista fica menor após cada `pop()`. Quando fica vazia, ela é falsa e o loop termina.

Isso é válido, mas a iteração direta com `for` costuma ser mais clara quando o objetivo é apenas ler todos os itens sem consumir ou modificar a coleção.

## 26. A mutação pode ser a atualização de estado

No exemplo anterior não existe contador numérico.

A atualização relevante é:

```python
current = tasks.pop()
```

`pop()` modifica `tasks`, e essa mutação altera o valor de verdade testado por `while tasks:`.

A regra mais ampla é:

**Encontre o estado usado pela condição e depois encontre o que altera esse estado.**

## 27. Condições explícitas podem facilitar a auditoria da intenção

O Python permite usar valores verdadeiros e falsos diretamente:

```python
while tasks:
    ...
```

Às vezes, uma condição explícita comunica a regra com mais precisão:

```python
while remaining_attempts > 0:
    ...
```

Nenhum dos estilos é obrigatório em todos os casos. Escolha a forma que torne a regra de parada mais fácil de entender.

## 28. Prévia: o que `while True` significa

Esta sintaxe é Python válido:

```python
while True:
    statement
```

Como a condição literal `True` nunca se torna falsa por conta própria, a própria condição não fornece um ponto normal de parada.

Programas reais frequentemente combinam `while True` com outro mecanismo de controle de fluxo que sai do loop quando uma condição é atendida.

Esse mecanismo é deliberadamente adiado para o próximo capítulo, no qual `break`, `continue` e `else` de loop são ensinados em conjunto.

## 29. Por que este capítulo não usa `while True` nos exemplos seguros

Um loop `while True` isolado é intencionalmente ilimitado, a menos que outro mecanismo o encerre.

Os exemplos executáveis seguros do repositório precisam terminar de forma determinística, então este capítulo não registra um exemplo ilimitado com `while True`.

Por enquanto, lembre apenas do significado:

```text
while True -> continuar repetindo porque a própria condição do loop nunca se torna falsa
```

O próximo capítulo mostra como instruções explícitas de controle de loop interagem com esse padrão.

## 30. `break`, `continue` e `else` de loop vêm a seguir

A sintaxe completa de loops em Python inclui recursos de controle de fluxo que podem alterar ou interpretar o término normal.

Eles não são pré-requisitos para compreender loops `while` comuns guiados por condição.

Por isso, este capítulo mantém o modelo intencionalmente simples:

```text
condição verdadeira -> executar corpo
atualizar estado    -> testar novamente
condição falsa      -> loop termina
```

O Capítulo 07 adiciona os caminhos extras de controle.

## 31. Uma auditoria prática de término

Antes de executar um novo loop `while`, responda a quatro perguntas:

1. Qual é o estado inicial?
2. Qual condição exata controla a repetição?
3. O que altera o estado usado por essa condição?
4. Por que essa mudança pode eventualmente tornar a condição falsa?

Se a quarta resposta não estiver clara, inspecione o loop cuidadosamente antes de executá-lo.

Essa pequena auditoria detecta muitos loops infinitos acidentais.

## 32. Erros comuns

### Erro 1: esquecer os dois-pontos

Incorreto:

```python
while remaining > 0
    print(remaining)
```

O cabeçalho do `while` deve terminar com `:`.

### Erro 2: indentação incorreta

As instruções repetidas precisam estar indentadas sob o cabeçalho `while`.

### Erro 3: esquecer a atualização de estado

Se a condição permanecer verdadeira e nada relevante mudar, o loop pode nunca terminar.

### Erro 4: atualizar na direção errada

Uma atualização que afasta o estado da condição de parada também pode criar um loop infinito.

### Erro 5: assumir que o corpo sempre executa uma vez

A condição é testada primeiro, portanto zero iterações são possíveis.

### Erro 6: usar `while` para percorrer diretamente uma coleção

Quando a tarefa é simplesmente “para cada item”, a iteração direta com `for` costuma ser mais clara.

### Erro 7: assumir que um limite precisa ser atingido exatamente

Um loop termina quando sua condição se torna falsa. O estado pode atravessar um limite numérico sem nunca ser igual a ele.

## 33. Exemplo trabalhado: `countdown_state.py`

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining = remaining - 1

print("Start")
```

Saída:

```text
3
2
1
Start
```

Exemplo no repositório: [`examples/countdown_state.py`](examples/countdown_state.py)

## 34. Exemplo trabalhado: `study_target.py`

```python
studied_minutes = 0
session_minutes = 20
target_minutes = 60

while studied_minutes < target_minutes:
    studied_minutes = studied_minutes + session_minutes
    print(f"Study total: {studied_minutes} min")
```

Saída:

```text
Study total: 20 min
Study total: 40 min
Study total: 60 min
```

Exemplo no repositório: [`examples/study_target.py`](examples/study_target.py)

## 35. Exemplo trabalhado: `doubling_until_limit.py`

```python
value = 1
limit = 20

while value < limit:
    print(value)
    value = value * 2

print(f"Stopped at {value}")
```

Saída:

```text
1
2
4
8
16
Stopped at 32
```

Exemplo no repositório: [`examples/doubling_until_limit.py`](examples/doubling_until_limit.py)

## 36. Exercício

Crie um pequeno rastreador de progresso com este estado inicial:

```python
completed = 0
target = 4
```

Seu programa deve:

1. usar um loop `while` cuja condição compare `completed` com `target`;
2. imprimir a próxima etapa concluída em cada iteração;
3. atualizar `completed` para que o loop avance em direção ao término;
4. após o loop, imprimir `Target reached`.

Saída esperada:

```text
Completed: 1
Completed: 2
Completed: 3
Completed: 4
Target reached
```

Depois responda, sem executar o programa:

- Qual é o estado inicial?
- Qual expressão é reavaliada antes de cada iteração?
- Qual instrução altera o estado do loop?
- Qual valor torna a condição falsa?
- O corpo seria executado se `completed` começasse em `4`?

Não use `break`, `continue`, `else` de loop ou `while True` neste exercício.

## 37. Checklist de revisão

Antes de avançar, confirme que você consegue explicar cada afirmação sem executar o código:

- [ ] `while` repete um bloco enquanto sua condição for verdadeira.
- [ ] a condição é testada antes de cada iteração.
- [ ] o corpo pode ser executado zero vezes.
- [ ] estado do loop é informação que afeta se a repetição continua.
- [ ] um loop finito guiado por condição precisa de um caminho para tornar sua condição falsa.
- [ ] o estado pode aumentar, diminuir, multiplicar, acumular ou sofrer outras mudanças deliberadas.
- [ ] um estado numérico não precisa ser exatamente igual a um limite para o loop parar.
- [ ] esquecer uma atualização pode criar um loop infinito.
- [ ] atualizar na direção errada também pode impedir o término.
- [ ] `for` costuma ser mais claro para percorrer diretamente um iterável.
- [ ] `while` é útil quando a continuação depende naturalmente do estado atual.
- [ ] várias variáveis podem participar da condição.
- [ ] uma coleção mutável pode fazer parte do estado que muda.
- [ ] `while True` possui uma condição que nunca se torna falsa por conta própria.
- [ ] `break`, `continue` e `else` de loop são deliberadamente adiados para o Capítulo 07.

## 38. Referência rápida

| Necessidade | Forma típica |
|---|---|
| Repetir enquanto uma comparação for verdadeira | `while value < limit:` |
| Contar para cima até um limite | inicializar, testar, incrementar |
| Contar para baixo até um limite | inicializar, testar, decrementar |
| Acumular até uma meta | atualizar acumulador dentro de `while accumulator < target:` |
| Repetir enquanto uma coleção não estiver vazia | `while collection:` quando consumir/modificar é intencional |
| Percorrer cada item de um iterável | normalmente `for item in iterable` |
| Auditar término | identificar estado inicial, condição, atualização e caminho até falso |
| Prévia de condição ilimitada | `while True:`; controle de loop vem no próximo capítulo |

Lembre da progressão:

**estado inicial → condição → corpo → atualização de estado → condição novamente → término**

## Próximo passo

O próximo capítulo é **`break`, `continue` e `else` de Loops**.

Agora você conhece o ciclo de vida normal de um loop `while` guiado por condição. Em seguida, o guia adiciona instruções que podem sair de um loop antes do término normal, avançar diretamente para a próxima iteração e distinguir conclusão normal de término por `break`.

## Referências oficiais

- [Referência do Python 3.13: a instrução `while`](https://docs.python.org/3.13/reference/compound_stmts.html#the-while-statement)
- [Tipos embutidos do Python 3.13: teste de valor de verdade](https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing)
- [Tutorial do Python 3.13: primeiros passos em direção à programação](https://docs.python.org/3.13/tutorial/introduction.html#first-steps-towards-programming)
