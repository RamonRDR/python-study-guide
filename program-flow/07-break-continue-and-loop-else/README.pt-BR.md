<div align="center">

# `break`, `continue` e `else` de Loops

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Fluxo do Programa](../README.pt-BR.md) · [← Anterior: Loops `while` e Repetição Guiada por Estado](../06-while-loops-and-state-driven-repetition/README.pt-BR.md)

Loops normalmente seguem sua regra natural de repetição: um loop `for` consome seu iterável, e um loop `while` continua enquanto sua condição permanecer verdadeira. Às vezes, porém, um programa precisa **parar antes do fim, pular o restante de uma iteração ou distinguir o encerramento normal de uma saída antecipada**.

Este capítulo apresenta as três ferramentas que o Python oferece para essas situações: `break`, `continue` e a cláusula opcional `else` dos loops.

**Tempo estimado de estudo:** 110–135 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que significa encerramento normal em loops `for` e `while`;
- usar `break` para encerrar antecipadamente o loop envolvente mais próximo;
- reconhecer que o código posterior a `break` na mesma iteração não é executado;
- usar `continue` para pular as instruções restantes da iteração atual;
- explicar o próximo passo diferente após `continue` em `for` e `while`;
- atualizar o estado de um `while` com segurança quando `continue` for possível;
- usar `while True` de forma deliberada quando `break` expressar melhor a regra real de parada;
- explicar que o `else` de loop pertence ao loop, não a um `if` interno;
- prever quando o `else` de loop é executado e quando um `break` o impede;
- usar `for ... else` em buscas nas quais `break` significa que uma correspondência foi encontrada;
- usar `while ... else` quando o encerramento normal da condição tiver um caminho de conclusão significativo;
- reconhecer que um `for` vazio e uma condição inicialmente falsa em `while` ainda podem chegar ao `else` do loop;
- explicar que `break` afeta apenas o loop envolvente mais próximo em loops aninhados;
- escolher entre `break`, `continue`, `else` de loop e condições comuns de acordo com a intenção;
- evitar saltos desnecessários de controle que tornem o loop mais difícil de ler.

## 1. Comece pelo encerramento normal do loop

Antes de alterar um loop, defina o que aconteceria sem qualquer instrução especial de controle.

Um loop `for` normalmente termina quando seu iterador se esgota:

```python
for number in [1, 2, 3]:
    print(number)
```

Um loop `while` normalmente termina quando sua condição se torna falsa:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

`break`, `continue` e o `else` de loop só fazem sentido quando você entende primeiro esse caminho normal.

## 2. O que `break` faz

`break` encerra imediatamente o loop `for` ou `while` envolvente mais próximo.

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

Saída:

```text
1
2
```

Quando `number` se torna `3`, o loop termina antes que `print(number)` possa ser executado nessa iteração.

## 3. `break` sai do loop, não apenas do `if`

Considere:

```python
for item in ["pen", "book", "mug"]:
    if item == "book":
        break
    print(item)

print("Done")
```

Saída:

```text
pen
Done
```

O `if` decide se `break` será executado. O próprio `break` transfere o controle para fora do loop.

## 4. O código depois de `break` no mesmo corpo do loop é pulado

Este código nunca imprime `"After break"`:

```python
for number in [1, 2, 3]:
    if number == 2:
        break
        print("After break")
```

Assim que `break` é executado, o controle deixa o loop imediatamente.

Instruções inalcançáveis depois de um `break` incondicional não devem permanecer em código real.

## 5. `break` é útil quando a resposta já é conhecida

Suponha que você esteja buscando um único alvo:

```python
codes = ["PEN", "BOOK", "MUG", "CABLE"]
target = "MUG"

for code in codes:
    if code == target:
        print("Found")
        break
```

Depois que o alvo é encontrado, examinar os itens posteriores não mudaria a resposta.

## 6. Uma busca pode parar na primeira correspondência

Se duplicatas forem possíveis, mas apenas a primeira correspondência importar, `break` comunica essa política diretamente:

```python
values = [4, 7, 7, 9]

for value in values:
    if value == 7:
        print("First match found")
        break
```

O segundo `7` nunca é examinado pelo corpo do loop.

## 7. Não use `break` quando todos os itens precisam ser processados

Isto não combina bem com uma tarefa que precisa examinar todos os valores:

```python
scores = [82, 47, 91, 58]
```

Se você precisa classificar cada nota, encerrar o loop no primeiro valor reprovado perderia informação.

A instrução de controle deve corresponder ao requisito real, não apenas encurtar o código.

## 8. `break` também funciona em `while`

```python
count = 1

while count <= 10:
    print(count)
    if count == 3:
        break
    count += 1
```

Saída:

```text
1
2
3
```

A condição original do `while` ainda poderia ser verdadeira, mas `break` encerra o loop mesmo assim.

## 9. `while True` pode expressar um loop sem limite definido no cabeçalho

Um loop cuja regra natural de parada aparece dentro do corpo pode ser escrito assim:

```python
while True:
    command = input("Command: ")

    if command == "quit":
        break

    print(command)
```

`True` mantém o loop apto a repetir. A regra significativa de encerramento é o `break` acionado por `"quit"`.

Isso não é automaticamente melhor do que colocar uma condição no cabeçalho do `while`. Use quando a condição interna de parada for realmente mais clara.

## 10. `while True` precisa de um caminho de saída plausível

Este loop não apresenta nenhum caminho visível de encerramento:

```python
while True:
    print("Running")
```

Isso pode ser intencional em programas especializados, mas em código de aplicação para iniciantes deve provocar uma pergunta:

**Qual evento ou mudança de estado encerrará este loop?**

Se não houver resposta, você pode ter criado um loop infinito acidental.

## 11. O que `continue` faz

`continue` pula o restante da execução atual do corpo do loop e inicia o próximo ciclo do loop envolvente mais próximo.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Saída:

```text
1
2
4
5
```

O loop continua. Apenas o restante da iteração referente ao `3` é pulado.

## 12. `continue` não é `break`

Compare as intenções:

```text
break    -> stop this loop
continue -> skip the rest of this iteration and keep looping
```

Confundir os dois altera toda a forma do fluxo de controle.

## 13. `continue` é útil para filtrar dentro de um loop

```python
scores = [82, 47, 91, 58, 76]

for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

Saída:

```text
Passing score: 82
Passing score: 91
Passing score: 76
```

As notas reprovadas são puladas, enquanto os valores restantes ainda chegam à ação principal.

## 14. `continue` pode reduzir aninhamento

Sem `continue`:

```python
for score in scores:
    if score >= 60:
        print(f"Passing score: {score}")
```

Com `continue`:

```python
for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

As duas formas podem ser claras. A segunda costuma ser útil quando várias verificações iniciais rejeitam um item antes de um caminho principal mais longo.

Isso é uma escolha de legibilidade, não uma regra dizendo que `continue` é sempre superior.

## 15. Em um loop `for`, `continue` avança em direção ao próximo item

```python
for letter in "ABC":
    if letter == "B":
        continue
    print(letter)
```

Saída:

```text
A
C
```

Depois de pular o restante da iteração de `B`, o loop `for` solicita o próximo item ao seu iterador.

## 16. Em um loop `while`, `continue` testa a condição novamente

```python
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

Saída:

```text
1
2
4
5
```

Depois de `continue`, o Python volta para a condição do `while` antes de executar o corpo outra vez.

## 17. Atualize o estado do `while` antes de um possível `continue`

Este padrão é perigoso:

```python
number = 0

while number < 5:
    if number == 2:
        continue
    number += 1
```

Quando `number` chega a `2`, `continue` é executado antes da atualização. A condição permanece verdadeira e `number` continua valendo `2`, então o loop se repete para sempre.

Uma boa pergunta de revisão é:

**Todo caminho por este corpo de `while` ainda consegue avançar em direção ao encerramento?**

## 18. Condições às vezes são mais claras do que `continue`

Não adicione um salto apenas porque o Python oferece esse recurso.

```python
for number in range(1, 6):
    if number != 3:
        print(number)
```

pode ser perfeitamente legível em comparação com:

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Escolha a forma que comunica com mais clareza o caminho principal do loop.

## 19. O que é o `else` de loop

Tanto `for` quanto `while` podem ter uma cláusula opcional `else`.

Para um loop `for`:

```python
for item in iterable:
    statement
else:
    normal_completion_statement
```

Para um loop `while`:

```python
while condition:
    statement
else:
    normal_completion_statement
```

A regra principal não é “a condição ficou falsa”. A regra geral é:

**O `else` do loop é executado quando aquele loop termina sem executar um `break`.**

## 20. `for ... else` depois do esgotamento normal

```python
for number in [1, 2, 3]:
    print(number)
else:
    print("Finished normally")
```

Saída:

```text
1
2
3
Finished normally
```

O iterável se esgotou e nenhum `break` ocorreu, então o bloco `else` é executado.

## 21. `break` impede o `else` do loop

```python
for number in [1, 2, 3]:
    if number == 2:
        break
else:
    print("Finished normally")
```

Não há saída do `else`, porque `break` encerrou aquele loop.

## 22. `continue` não impede o `else` do loop

```python
for number in [1, 2, 3]:
    if number == 2:
        continue
    print(number)
else:
    print("Finished without break")
```

Saída:

```text
1
3
Finished without break
```

`continue` altera uma iteração, não a categoria final de encerramento do loop.

## 23. O `else` de loop pertence ao loop

Observe com atenção a indentação:

```python
for name in names:
    if name == target:
        print("Found")
        break
else:
    print("Not found")
```

O `else` está alinhado com `for`, não com `if`.

Essa relação visual é essencial para ler corretamente essa sintaxe.

## 24. Busca é o uso clássico de `for ... else`

```python
names = ["Ari", "Mina", "Leo"]
target = "Nora"

for name in names:
    if name == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} was not found")
```

Saída:

```text
Nora was not found
```

O significado é compacto:

```text
match found -> break -> skip else
no match     -> no break -> run else
```

## 25. O `else` de loop pode substituir uma flag manual

Uma busca com flag pode funcionar:

```python
found = False

for name in names:
    if name == target:
        found = True
        break

if not found:
    print("Not found")
```

A forma com `else` do loop representa diretamente o mesmo fato de controle:

```python
for name in names:
    if name == target:
        break
else:
    print("Not found")
```

Use a versão que seus leitores consigam compreender com segurança. O `else` de loop é um recurso real do Python, mas pode ser pouco familiar para algumas equipes.

## 26. Um `for` vazio ainda pode executar `else`

```python
for item in []:
    print(item)
else:
    print("No break occurred")
```

Saída:

```text
No break occurred
```

O corpo do loop foi executado zero vezes, mas o loop ainda terminou sem `break`.

## 27. `while ... else` é executado depois que a condição se torna falsa

```python
count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Condition became false")
```

Saída:

```text
1
2
3
Condition became false
```

Esse é o encerramento normal daquele loop `while`.

## 28. `break` também impede `while ... else`

```python
count = 1

while count <= 5:
    if count == 3:
        break
    count += 1
else:
    print("Condition became false")
```

O bloco `else` não é executado porque `break` encerrou o loop primeiro.

## 29. Um `while` inicialmente falso ainda pode executar `else`

```python
count = 5

while count < 3:
    print(count)
else:
    print("Loop completed without break")
```

Saída:

```text
Loop completed without break
```

O corpo foi executado zero vezes, mas nenhum `break` ocorreu.

## 30. Pense em “sem break”, não em “algo falhou”

Às vezes o `else` de loop é descrito informalmente como um bloco de “não encontrado”, porque buscas são um caso de uso comum.

Essa descrição é estreita demais.

O fato real de controle é:

```text
loop ended without break -> else runs
loop ended through break -> else is skipped
```

O significado de “sucesso”, “falha”, “encontrado” ou “não encontrado” vem do seu programa, não do próprio Python.

## 31. `break` afeta apenas o loop envolvente mais próximo

```python
rows = [[1, 2], [3, 4]]

for row in rows:
    for value in row:
        if value == 2:
            break
        print(value)
```

Saída:

```text
1
3
4
```

O `break` encerra apenas o loop interno. O loop externo continua com a próxima linha.

## 32. `continue` também aponta para o loop envolvente mais próximo

Em loops aninhados, `continue` avança o loop mais próximo que o contém sintaticamente.

Isso pode ficar difícil de ler quando vários níveis aninhados contêm saltos de controle.

Quando o aninhamento cresce, prefira tornar o fluxo explícito em vez de empilhar muitos `break` e `continue`.

## 33. O `else` pertence a um loop específico

Loops aninhados podem ter cada um seu próprio `else`, mas a indentação determina qual loop é dono de cada cláusula.

Para iniciantes, evite combinações densas até que a forma simples esteja completamente clara.

Um loop, um objetivo de busca e um `else` significativo costumam ser mais fáceis de estudar.

## 34. Erro comum: esperar que `break` saia de vários loops

Isto não encerra os dois loops:

```python
for row in rows:
    for value in row:
        if value == target:
            break
```

Apenas o loop interno termina.

Fases posteriores apresentam funções, que muitas vezes oferecem formas mais claras de organizar buscas maiores sem controle complicado de loops aninhados.

## 35. Erro comum: colocar atualizações importantes de estado depois de `continue`

```python
while condition:
    if skip_this_cycle:
        continue
    update_state()
```

Se `update_state()` for necessário para o encerramento, o caminho pulado pode nunca avançar.

Ao revisar um loop `while`, percorra mentalmente cada ramo que pode chegar a `continue`.

## 36. Erro comum: ler `else` de loop como `if ... else`

Esta indentação:

```python
for item in items:
    if condition:
        break
else:
    statement
```

significa que o `else` pertence a `for`.

Mover o `else` para baixo do `if` criaria outro programa, com comportamento diferente.

## 37. Erro comum: usar `else` de loop quando uma instrução normal basta

Se um código precisa sempre ser executado depois de um loop, independentemente de ter ocorrido `break`, coloque-o após o loop:

```python
for item in items:
    if should_stop:
        break

print("Cleanup message")
```

Não use `else` de loop para trabalho pós-loop incondicional, porque `break` faria esse bloco ser pulado.

## 38. Erro comum: exagerar em `break` e `continue`

Um loop com muitos saltos de controle pode virar um labirinto:

```text
condition -> continue
condition -> break
condition -> continue
condition -> nested break
```

Essas instruções são úteis porque são precisas, não porque mais delas torne o código melhor.

Prefira um número pequeno de saídas e pulos claramente motivados.

## 39. Exemplo completo: `break_search.py`

```python
codes = ["PEN", "BOOK", "MUG", "CABLE"]
target = "MUG"

for code in codes:
    print(f"Checking {code}")
    if code == target:
        print(f"Found {target}")
        break
```

Saída:

```text
Checking PEN
Checking BOOK
Checking MUG
Found MUG
```

Exemplo no repositório: [`examples/break_search.py`](examples/break_search.py)

## 40. Exemplo completo: `continue_filtering.py`

```python
scores = [82, 47, 91, 58, 76]

for score in scores:
    if score < 60:
        continue
    print(f"Passing score: {score}")
```

Saída:

```text
Passing score: 82
Passing score: 91
Passing score: 76
```

Exemplo no repositório: [`examples/continue_filtering.py`](examples/continue_filtering.py)

## 41. Exemplo completo: `loop_else_search.py`

```python
names = ["Ari", "Mina", "Leo"]
target = "Nora"

for name in names:
    if name == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} was not found")
```

Saída:

```text
Nora was not found
```

Exemplo no repositório: [`examples/loop_else_search.py`](examples/loop_else_search.py)

## 42. Exercício

Crie uma lista de códigos fictícios de tarefas:

```python
task_codes = ["A10", "B20", "SKIP", "C30", "STOP", "D40"]
```

Escreva um loop que:

1. use `continue` quando o valor for `"SKIP"`;
2. use `break` quando o valor for `"STOP"`;
3. imprima todos os outros códigos alcançados;
4. adicione um `else` de loop que imprima `"All tasks processed"` apenas se o loop terminar sem `break`.

Com a lista acima, a saída esperada é:

```text
A10
B20
C30
```

Depois remova `"STOP"` da lista e preveja o que muda antes de executar o programa.

## 43. Checklist de revisão

Antes de avançar, confirme que você consegue explicar cada afirmação sem executar o código:

- [ ] `break` encerra o loop `for` ou `while` envolvente mais próximo.
- [ ] instruções posteriores na mesma iteração são puladas após `break`.
- [ ] `continue` pula o restante da iteração atual sem encerrar o loop.
- [ ] em `for`, `continue` avança em direção ao próximo item.
- [ ] em `while`, `continue` volta ao teste da condição.
- [ ] um loop `while` ainda precisa atualizar estado relevante nos caminhos que podem chegar a `continue`.
- [ ] `while True` é apropriado quando um `break` interno expressa claramente a regra real de parada.
- [ ] o `else` de loop se alinha com o loop e pertence a ele.
- [ ] o `else` de loop é executado quando aquele loop termina sem `break`.
- [ ] `break` impede o `else` associado ao loop.
- [ ] `continue` por si só não impede o `else` do loop.
- [ ] um `for` vazio ainda pode executar seu `else`.
- [ ] um `while` inicialmente falso ainda pode executar seu `else`.
- [ ] em loops aninhados, `break` e `continue` afetam o loop envolvente mais próximo.
- [ ] instruções de controle de loop devem esclarecer a intenção, não criar saltos desnecessários.

## 44. Referência rápida

| Necessidade | Ferramenta típica |
|---|---|
| Parar o loop atual imediatamente | `break` |
| Pular o restante de uma iteração | `continue` |
| Repetir indefinidamente até uma regra interna de parada | `while True` + `break` |
| Executar um bloco somente quando nenhum `break` encerrou o loop | `else` de loop |
| Buscar até encontrar uma correspondência | `for` + condição + `break` |
| Tratar “não encontrado” depois de uma busca completa | `for ... else` |
| Pular itens rejeitados mantendo os itens posteriores | `continue` |
| Sempre executar código depois de um loop | instrução comum após o loop |

Lembre-se da progressão:

**repetição normal → saída antecipada → pular um ciclo → distinguir encerramento normal de `break`**

## Próximo passo

O próximo capítulo é **Escolhendo e Combinando o Fluxo do Programa**.

Agora você já conhece as principais ferramentas de seleção e repetição da Fase 4: condições, `if`, `match`, `for`, auxiliares de iteração, `while`, `break`, `continue` e `else` de loop. O capítulo final da fase se concentrará em escolher entre essas ferramentas e combiná-las sem transformar o fluxo de controle em um labirinto.

## Referências oficiais

- [Referência da linguagem Python 3.13: `break`](https://docs.python.org/3.13/reference/simple_stmts.html#the-break-statement)
- [Referência da linguagem Python 3.13: `continue`](https://docs.python.org/3.13/reference/simple_stmts.html#the-continue-statement)
- [Referência da linguagem Python 3.13: `while`](https://docs.python.org/3.13/reference/compound_stmts.html#the-while-statement)
- [Referência da linguagem Python 3.13: `for`](https://docs.python.org/3.13/reference/compound_stmts.html#the-for-statement)
- [Tutorial Python 3.13: `break`, `continue` e `else` de loops](https://docs.python.org/3.13/tutorial/controlflow.html#break-and-continue-statements)