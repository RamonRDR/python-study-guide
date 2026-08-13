<div align="center">

# Definindo e Chamando Funções

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Fase anterior: Fluxo do Programa](../../program-flow/README.pt-BR.md)

Funções dão um nome significativo a comportamentos que um programa pode precisar executar mais de uma vez.

Este capítulo inicia a Fase 5 com uma distinção:

```text
definition = describe and name behavior
call       = execute that behavior now
```

Parâmetros, argumentos, projeto de valores de retorno e escopo vêm depois.

**Tempo estimado de estudo:** 75–100 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar por que funções existem;
- definir uma função simples com `def`;
- identificar nome da função, lista de parâmetros vazia, dois-pontos e corpo indentado;
- chamar uma função depois que sua definição foi executada;
- explicar que definir uma função não executa seu corpo;
- rastrear a execução para dentro e para fora de uma chamada;
- chamar a mesma função mais de uma vez;
- diferenciar `name` de `name()`;
- usar nomes significativos em `snake_case`;
- usar `pass` para um corpo intencionalmente vazio;
- colocar estruturas de fluxo já conhecidas dentro de uma função;
- reconhecer que uma função sem `return` explícito produz `None`.

## 1. Por que funções existem

Um programa já consegue armazenar valores, escolher caminhos e repetir trabalho.

Conforme cresce, grupos de instruções começam a representar tarefas reconhecíveis:

```text
show a heading
show a menu
print a separator
display a status
```

Uma função permite dar um nome a uma dessas tarefas.

O primeiro modelo mental é:

> **Funções dão nome a comportamentos.**

Uma boa função também pode reduzir duplicação e tornar o fluxo de um programa mais fácil de ler.

## 2. Defina primeiro, chame depois

```python
def show_welcome():
    print("Welcome to Python functions.")


show_welcome()
```

A definição é:

```python
def show_welcome():
    print("Welcome to Python functions.")
```

A chamada é:

```python
show_welcome()
```

São operações diferentes.

## 3. Anatomia do `def`

```python
def show_welcome():
    print("Welcome to Python functions.")
```

| Parte | Significado |
|---|---|
| `def` | inicia uma definição de função |
| `show_welcome` | nome da função |
| `()` | lista de parâmetros, vazia neste capítulo |
| `:` | inicia o bloco da função |
| instrução indentada | corpo da função |

Este capítulo mantém `()` vazio de propósito. O Capítulo 02 adicionará parâmetros e argumentos.

## 4. Uma definição não executa o corpo

Quando o Python executa uma instrução `def`, ele cria a função e a associa ao nome da função.

O corpo fica preparado para execução posterior.

Então isto não imprime nada:

```python
def show_welcome():
    print("Welcome")
```

O corpo executa somente depois de uma chamada:

```python
show_welcome()
```

Pense:

```text
def       → prepare behavior
name()    → execute behavior
```

## 5. Uma chamada redireciona a execução temporariamente

```python
def show_step():
    print("Inside function")


print("Before call")
show_step()
print("After call")
```

Saída:

```text
Before call
Inside function
After call
```

Rastreamento:

1. O Python define `show_step`.
2. A execução no nível principal imprime `Before call`.
3. `show_step()` chama a função.
4. A execução entra no corpo.
5. O corpo imprime `Inside function`.
6. O corpo termina.
7. A execução continua depois da chamada.
8. O Python imprime `After call`.

O chamador não desaparece. A execução volta ao ponto logo depois da chamada.

## 6. Uma definição, várias chamadas

```python
def show_separator():
    print("---")


print("Start")
show_separator()
print("Study")
show_separator()
print("Finish")
```

Saída:

```text
Start
---
Study
---
Finish
```

A função é definida uma vez e chamada duas vezes.

Esse é o reuso básico:

```text
define once
call when needed
```

## 7. Reuso é mais do que copiar e colar

Código repetido pode funcionar, mas uma função adiciona significado.

Compare a ideia:

```text
print("---")
```

com:

```text
show_separator()
```

A segunda forma explica *por que* aquela linha existe.

Quando o comportamento muda, uma única definição pode atualizar todos os pontos que chamam a função.

## 8. Nomes de função devem descrever ações

Prefira nomes como:

```text
show_status
print_summary
validate_choice
calculate_total
```

Nomes normais de função em Python usam `snake_case`.

Evite nomes como:

```text
x
thing
func1
do_it
```

a menos que o contexto realmente os torne claros.

Uma chamada deve parecer uma ação significativa.

## 9. `name` e `name()` são diferentes

```python
def show_message():
    print("Hello")


print(show_message)
show_message()
```

`show_message` referencia o objeto função.

`show_message()` chama a função.

Você ainda não precisa dominar objetos função. Guarde esta regra:

```text
name   → reference
name() → call
```

## 10. A indentação define o corpo

Válido:

```python
def show_message():
    print("Hello")
```

Inválido:

```python
def show_message():
print("Hello")
```

Uma definição de função introduz um bloco indentado, assim como outras instruções compostas que você já conhece.

O cabeçalho também exige dois-pontos:

```python
def show_message():
```

## 11. Fluxo do programa pode ficar dentro de uma função

```python
def show_even_numbers():
    for number in range(1, 6):
        if number % 2 == 0:
            print(number)


show_even_numbers()
```

Saída:

```text
2
4
```

`for` e `if` mantêm seu significado normal.

A função apenas dá um nome reutilizável a esse comportamento combinado.

Isso conecta as fases:

```text
program flow → controls what happens
functions    → name a unit of behavior
```

## 12. Um corpo pode conter várias instruções

```python
def show_study_plan():
    print("Read")
    print("Practice")
    print("Review")


show_study_plan()
```

Saída:

```text
Read
Practice
Review
```

Toda instrução corretamente indentada pertence ao corpo.

## 13. A ordem da definição importa

No nível principal, esta ordem falha:

```python
show_welcome()


def show_welcome():
    print("Welcome")
```

O Python chega à chamada antes de executar a definição que associa `show_welcome`.

Use:

```python
def show_welcome():
    print("Welcome")


show_welcome()
```

A regra precisa é:

> A definição deve ter sido executada antes da chamada acontecer.

Depois que os nomes existem, a ordem das chamadas ainda pode ser diferente da ordem das definições.

## 14. `pass` pode marcar um corpo intencionalmente vazio

```python
def planned_step():
    pass


planned_step()
```

`pass` é uma instrução válida que não faz nada.

Ela é útil quando o corpo precisa existir estruturalmente, mas o comportamento real ainda não foi escrito.

Não adicione `pass` a um corpo que já tenha instruções reais.

## 15. Uma função sem `return` explícito produz `None`

```python
def show_ready():
    print("Ready")


result = show_ready()
print(result)
```

Saída:

```text
Ready
None
```

Este capítulo ainda não ensina projeto de valores de retorno.

Por enquanto, observe apenas que chegar ao fim de uma função sem `return` explícito conclui a chamada e o resultado da chamada é `None`.

O Capítulo 03 tratará valores de retorno como assunto completo.

## 16. Imprimir não é retornar

Esta função:

```python
def show_ready():
    print("Ready")
```

exibe uma saída.

Ela não envia explicitamente um valor útil de volta ao chamador.

Mantenha os conceitos separados:

```text
print(...) → display something
return ... → send a result to the caller
```

A segunda ideia vem depois.

## 17. Funções devem representar tarefas significativas

Uma função normalmente deve responder:

```text
What job does this function perform?
```

Por exemplo:

```python
def show_menu():
    print("1. Study")
    print("2. Practice")
```

A responsabilidade é clara.

Não crie funções apenas porque funções são o assunto atual. Wrappers pequenos sem propósito significativo podem piorar a leitura.

## 18. Chamadas e loops podem trabalhar juntos

Um loop pode controlar a repetição:

```python
def show_tick():
    print("Tick")


for repetition in range(3):
    show_tick()
```

Ou a função pode controlar a repetição:

```python
def show_three_ticks():
    for repetition in range(3):
        print("Tick")


show_three_ticks()
```

Os dois imprimem três ticks, mas distribuem responsabilidade de formas diferentes.

O alvo descritivo do loop mantém o modelo de iteração familiar. O valor dele não é necessário nesses corpos específicos; o loop só precisa repetir três vezes.

Capítulos posteriores darão mais controle ao chamador por meio de parâmetros.

## 19. Rastreie antes de depurar

Quando uma função surpreender, escreva o caminho de execução:

```text
define function
run top-level code
call function
enter body
run body
leave body
continue after call
```

Esse rastreamento simples encontra muitos erros de iniciante.

## 20. Erros comuns

### Definir e nunca chamar

```python
def show_message():
    print("Hello")
```

Sem chamada, o corpo não executa.

### Esquecer os parênteses

```python
show_message
```

referencia a função. Use `show_message()` para chamá-la.

### Chamar antes da definição executar

```python
show_message()


def show_message():
    print("Hello")
```

No nível principal, coloque a definição antes da chamada.

### Quebrar a indentação

```python
def show_message():
print("Hello")
```

O corpo precisa ser indentado.

### Adicionar conceitos posteriores cedo demais

Talvez você já tenha visto:

```python
def greet(name):
    print(f"Hello, {name}")
```

Isso é útil, mas agora a função recebe dados.

Primeiro deixe este modelo confiável:

```text
define
call
trace
reuse
```

Depois, parâmetros ficam muito mais fáceis.

## 21. Exemplo executável: definir e chamar

Arquivo: [`examples/define_and_call.py`](examples/define_and_call.py)

```python
def show_welcome():
    print("Welcome to Python functions.")


show_welcome()
```

Saída esperada:

```text
Welcome to Python functions.
```

## 22. Exemplo executável: chamadas repetidas

Arquivo: [`examples/repeated_calls.py`](examples/repeated_calls.py)

```python
def show_separator():
    print("---")


print("Start")
show_separator()
print("Study")
show_separator()
print("Finish")
```

Saída esperada:

```text
Start
---
Study
---
Finish
```

## 23. Exemplo executável: ordem de execução

Arquivo: [`examples/execution_order.py`](examples/execution_order.py)

```python
def show_step():
    print("Inside function")


print("Before call")
show_step()
print("After call")
```

Saída esperada:

```text
Before call
Inside function
After call
```

## 24. Exercício: banner de estudo reutilizável

Crie uma função chamada `show_study_banner`.

Requisitos:

1. defina com `def`;
2. mantenha a lista de parâmetros vazia;
3. imprima exatamente:

```text
==========
STUDY TIME
==========
```

4. imprima `Before`;
5. chame a função;
6. imprima `After`;
7. chame a mesma função novamente.

Saída esperada:

```text
Before
==========
STUDY TIME
==========
After
==========
STUDY TIME
==========
```

Ainda não use parâmetros nem `return`.

## 25. Perguntas de revisão

- Quais linhas definem comportamento?
- Quais linhas chamam comportamento?
- Quantas vezes a função é definida?
- Quantas vezes ela é chamada?
- Por que o corpo executa duas vezes?
- O que acontece se as duas chamadas forem removidas?
- O que muda se você escrever o nome da função sem parênteses?
- Quais instruções estão no nível principal?
- Quais instruções pertencem ao corpo?

## 26. Checklist de revisão

Antes de continuar, confirme que você consegue:

- [ ] explicar por que funções existem;
- [ ] escrever `def name():`;
- [ ] indentar o corpo;
- [ ] diferenciar definição de chamada;
- [ ] chamar uma função com `name()`;
- [ ] diferenciar `name` de `name()`;
- [ ] rastrear a execução para dentro e para fora de uma chamada;
- [ ] chamar a mesma função mais de uma vez;
- [ ] explicar por que a ordem de execução da definição importa;
- [ ] escolher um nome significativo em `snake_case`;
- [ ] usar `pass` para um corpo intencionalmente vazio;
- [ ] colocar ferramentas de fluxo conhecidas dentro de uma função;
- [ ] reconhecer `None` implícito quando não há `return` explícito.

## 27. Referência rápida

| Necessidade | Forma | Significado |
|---|---|---|
| definir uma função | `def name():` | criar e associar uma função a um nome |
| escrever comportamento | corpo indentado | instruções executadas por uma chamada |
| chamar | `name()` | executar o corpo |
| referenciar | `name` | acessar o objeto função |
| manter corpo vazio temporariamente | `pass` | instrução válida sem operação |
| estilo normal de nome | `snake_case` | convenção legível para funções |
| sem `return` explícito | fim do corpo | resultado da chamada é `None` |

## 28. Limite de escopo

Este capítulo intencionalmente não ensina em profundidade:

- parâmetros e argumentos;
- projeto de valores de retorno;
- escopo local e global;
- type hints;
- valores padrão;
- `*args` e `**kwargs`;
- funções aninhadas;
- lambdas;
- decorators;
- generators;
- recursão.

Essas ideias merecem modelos mentais separados.

## 29. O que vem depois

Agora você consegue definir comportamento, chamá-lo, reutilizá-lo e rastrear sua execução.

A próxima pergunta é:

> Como uma função pode trabalhar com diferentes valores de entrada?

Isso leva ao **Capítulo 02: Parâmetros e Argumentos**.

Volte para a [trilha de Funções](../README.pt-BR.md) ou para a [trilha completa](../../docs/learning-path.pt-BR.md).

## Referências

Documentação primária do Python:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Language Reference: Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13 Language Reference: Calls](https://docs.python.org/3.13/reference/expressions.html#calls)
