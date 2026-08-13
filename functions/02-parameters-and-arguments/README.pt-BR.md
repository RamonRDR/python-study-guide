<div align="center">

# Parâmetros e Argumentos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Anterior: Definindo e Chamando Funções](../01-defining-and-calling-functions/README.pt-BR.md)

O Capítulo 01 deu um nome ao comportamento. O Capítulo 02 faz esse comportamento **trabalhar com valores de entrada diferentes**.

A distinção central é:

```text
parameter = name in the function definition
argument  = value supplied by a function call
```

Este capítulo foca parâmetros obrigatórios e chamadas comuns. Valores de retorno, valores padrão, type hints, `*args`, `**kwargs` e regras detalhadas de escopo vêm depois.

**Tempo estimado de estudo:** 90–120 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- distinguir parâmetro de argumento;
- definir uma função com um ou mais parâmetros obrigatórios;
- chamar a mesma função com argumentos diferentes;
- passar literais, variáveis, expressões e coleções como argumentos;
- explicar como argumentos posicionais se associam pela posição;
- usar argumentos nomeados básicos;
- misturar argumentos posicionais e nomeados em uma ordem válida;
- escolher nomes significativos para parâmetros;
- usar parâmetros com lógica já conhecida de `if`, `for` e `range()`;
- reconhecer argumentos ausentes, extras, duplicados e inesperados como erros de chamada;
- rastrear os dados de entrada do chamador até o corpo da função.

## 1. De comportamento fixo para comportamento configurável

Uma função sem parâmetros repete um comportamento fixo:

```python
def greet():
    print("Hello, Maya!")


greet()
greet()
```

Toda chamada imprime o mesmo nome.

Um parâmetro cria um lugar para o chamador fornecer dados:

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Maya")
greet("Leo")
```

Agora o comportamento permanece o mesmo enquanto a entrada muda.

## 2. Parâmetro versus argumento

Na definição:

```python
def greet(name):
    print(f"Hello, {name}!")
```

`name` é um **parâmetro**.

Na chamada:

```python
greet("Maya")
```

`"Maya"` é um **argumento**.

Mantenha este modelo mental:

```text
definition → parameter
call       → argument
```

## 3. Um parâmetro obrigatório precisa de um argumento

```python
def show_city(city):
    print(f"City: {city}")


show_city("Recife")
```

A chamada fornece um argumento para um parâmetro obrigatório.

Chamar `show_city()` sem argumento gera `TypeError` porque a entrada obrigatória não foi fornecida.

## 4. A lista de parâmetros fica dentro dos parênteses

O Capítulo 01 usou uma lista de parâmetros vazia:

```python
def show_status():
    print("Ready")
```

O Capítulo 02 coloca nomes dentro dela:

```python
def show_status(status):
    print(status)
```

Pense:

```text
()             → no parameters
(status)       → one parameter
(title, year)  → two parameters
```

## 5. Uma definição pode receber muitos valores

```python
def show_language(language):
    print(f"Studying: {language}")


show_language("Python")
show_language("JavaScript")
show_language("SQL")
```

Saída:

```text
Studying: Python
Studying: JavaScript
Studying: SQL
```

A função é definida uma vez. Cada chamada fornece um novo argumento.

## 6. Argumentos podem ser literais

```python
def show_quantity(quantity):
    print(f"Quantity: {quantity}")


show_quantity(3)
```

Aqui `3` é o argumento fornecido a `quantity`.

## 7. Argumentos podem vir de variáveis

```python
def show_quantity(quantity):
    print(f"Quantity: {quantity}")


items_in_cart = 4
show_quantity(items_in_cart)
```

A variável do chamador e o parâmetro não precisam ter o mesmo nome.

```text
items_in_cart → name in caller code
quantity      → parameter name in function
```

## 8. Argumentos podem ser expressões

Python avalia uma expressão usada como argumento antes que o corpo use o valor resultante.

```python
def show_total(total):
    print(f"Total: {total}")


price = 12
quantity = 3
show_total(price * quantity)
```

Saída:

```text
Total: 36
```

A função recebe o resultado de `price * quantity`.

## 9. Vários parâmetros criam várias entradas

Separe os parâmetros com vírgulas:

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book("Python Basics", 2026)
```

A definição tem dois parâmetros, e a chamada fornece dois argumentos.

## 10. Argumentos posicionais se associam pela posição

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")


show_route("Home", "Library")
```

Associação:

```text
origin      ← "Home"
destination ← "Library"
```

O primeiro argumento posicional vai para o primeiro parâmetro compatível, o segundo vai para o segundo e assim por diante.

## 11. A ordem posicional pode mudar o significado

```python
show_route("Library", "Home")
```

Essa chamada é válida, mas agora a rota aponta na direção oposta.

Python segue a posição. Ele não tenta adivinhar sua intenção.

## 12. Argumentos nomeados básicos indicam o parâmetro de destino

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book(title="Python Basics", year=2026)
```

Argumentos nomeados tornam explícito qual parâmetro recebe cada valor.

Para parâmetros comuns, a ordem também pode mudar quando todos os argumentos são nomeados:

```python
show_book(year=2026, title="Python Basics")
```

## 13. Chamadas posicionais e nomeadas podem representar a mesma entrada

Estas chamadas associam os mesmos valores:

```python
show_book("Python Basics", 2026)
show_book(title="Python Basics", year=2026)
show_book("Python Basics", year=2026)
```

A terceira forma mistura estilos: primeiro posicional, depois nomeado.

Use a forma que deixar a chamada mais fácil de ler.

## 14. Argumentos posicionais vêm antes dos argumentos nomeados

Válido:

```python
show_book("Python Basics", year=2026)
```

Sintaxe inválida:

```python
show_book(title="Python Basics", 2026)
```

Depois que um argumento nomeado aparece, um argumento posicional comum não pode vir depois dele naquela chamada.

## 15. Não forneça o mesmo parâmetro duas vezes

```python
show_book("Python Basics", title="Another Title")
```

O argumento posicional já associa `title`, e o argumento nomeado tenta associá-lo novamente.

Python gera `TypeError`.

## 16. Nomes de parâmetros fazem parte da interface

Compare:

```python
def show_route(a, b):
    print(f"{a} -> {b}")
```

com:

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")
```

A segunda definição comunica o papel de cada entrada com mais clareza.

Bons nomes de parâmetros descrevem significado, não apenas tipo de dado.

## 17. Um parâmetro pode ser usado mais de uma vez

```python
def show_name_box(name):
    print("---")
    print(name)
    print(name)
    print("---")


show_name_box("Maya")
```

Isso usa um parâmetro duas vezes. Não cria dois parâmetros.

## 18. Parâmetros funcionam com `if`

```python
def show_score_status(name, score):
    if score >= 70:
        print(f"{name}: ready")
    else:
        print(f"{name}: review")


show_score_status("Ana", 82)
show_score_status("Luis", 61)
```

Saída:

```text
Ana: ready
Luis: review
```

`if` mantém seu significado normal. A condição apenas usa valores fornecidos pelo chamador.

## 19. Parâmetros funcionam com loops

```python
def repeat_message(message, times):
    for repetition in range(times):
        print(message)


repeat_message("Practice", 3)
```

Saída:

```text
Practice
Practice
Practice
```

O loop continua responsável pela repetição. Os parâmetros tornam o comportamento configurável.

## 20. Coleções podem ser argumentos

```python
def show_topics(topics):
    for topic in topics:
        print(topic)


study_topics = ["functions", "parameters", "arguments"]
show_topics(study_topics)
```

Saída:

```text
functions
parameters
arguments
```

Este capítulo apenas lê a coleção. Mutação e comportamento mais profundo de compartilhamento de objetos são intencionalmente adiados.

## 21. Rastreie o fluxo de entrada

```python
def greet(name):
    print(f"Hello, {name}!")


person = "Maya"
greet(person)
```

Rastreio:

```text
"Maya"
  ↓
person
  ↓
argument in greet(person)
  ↓
parameter name
  ↓
function body
```

Os nomes podem ser diferentes. Rastreie o valor.

## 22. A chamada deve satisfazer os parâmetros obrigatórios

Esta função exige duas entradas:

```python
def show_book(title, year):
    print(f"{title} ({year})")
```

Poucos argumentos:

```python
show_book("Python Basics")
```

Argumentos demais:

```python
show_book("Python Basics", 2026, "Beginner")
```

As duas chamadas geram `TypeError`.

Capítulos posteriores introduzirão entradas opcionais e flexíveis.

## 23. Nomes de argumentos nomeados devem corresponder aos parâmetros

Válido:

```python
show_book(title="Python Basics", year=2026)
```

Argumento nomeado inesperado:

```python
show_book(name="Python Basics", year=2026)
```

A função não tem um parâmetro chamado `name`, então Python gera `TypeError`.

## 24. Parâmetros e variáveis externas têm papéis diferentes

```python
def show_city(city):
    print(city)


home_city = "Curitiba"
show_city(home_city)
```

`home_city` pertence ao código chamador. `city` é o parâmetro da função.

As regras detalhadas de nomes locais versus globais pertencem ao Capítulo 04: Escopo.

## 25. Erros comuns

### Faltar um argumento obrigatório

```python
def greet(name):
    print(f"Hello, {name}!")


greet()
```

### Fornecer argumentos demais

```python
greet("Maya", "Leo")
```

### Trocar o significado posicional

```python
show_route("Library", "Home")
```

### Associar o mesmo parâmetro duas vezes

```python
show_book("Python Basics", title="Another Title")
```

### Colocar argumento posicional depois de argumento nomeado

```python
show_book(title="Python Basics", 2026)
```

### Usar nomes vagos para parâmetros

Prefira:

```python
def show_route(origin, destination):
    print(f"{origin} -> {destination}")
```

## 26. Exemplo executável: um parâmetro, várias chamadas

Arquivo: [`examples/greet_people.py`](examples/greet_people.py)

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Maya")
greet("Leo")
greet("Nina")
```

Saída esperada:

```text
Hello, Maya!
Hello, Leo!
Hello, Nina!
```

## 27. Exemplo executável: argumentos posicionais e nomeados

Arquivo: [`examples/book_details.py`](examples/book_details.py)

```python
def show_book(title, year):
    print(f"{title} ({year})")


show_book("Python Basics", 2026)
show_book(year=2025, title="Study Notes")
```

Saída esperada:

```text
Python Basics (2026)
Study Notes (2025)
```

## 28. Exemplo executável: parâmetros e fluxo do programa

Arquivo: [`examples/score_status.py`](examples/score_status.py)

```python
def show_score_status(name, score):
    if score >= 70:
        print(f"{name}: ready")
    else:
        print(f"{name}: review")


show_score_status("Ana", 82)
show_score_status("Luis", 61)
```

Saída esperada:

```text
Ana: ready
Luis: review
```

## 29. Exercício: cartão de estudo configurável

Crie `show_study_card` com dois parâmetros obrigatórios: `topic` e `minutes`.

Requisitos:

1. defina com `def`;
2. use os dois parâmetros no corpo;
3. imprima `Topic: ...` e `Minutes: ...`;
4. chame uma vez com argumentos posicionais para `"Python"` e `45`;
5. chame novamente com argumentos nomeados para `"SQL"` e `30`;
6. não use valores padrão;
7. ainda não use `return`.

Saída esperada:

```text
Topic: Python
Minutes: 45
Topic: SQL
Minutes: 30
```

## 30. Perguntas de revisão

- Qual nome é o parâmetro em `def greet(name):`?
- Qual valor é o argumento em `greet("Maya")`?
- Um parâmetro pode receber argumentos diferentes em chamadas diferentes?
- O que determina a associação posicional?
- Por que argumentos nomeados podem melhorar a legibilidade?
- Um argumento posicional comum pode vir depois de um argumento nomeado?
- O que acontece quando falta um argumento obrigatório?
- O que acontece quando um parâmetro recebe duas tentativas de valor?
- O nome da variável do chamador e o nome do parâmetro precisam ser iguais?
- Uma lista pode ser passada como argumento?

## 31. Checklist de revisão

Antes de continuar, confirme que você consegue:

- [ ] explicar parâmetro versus argumento;
- [ ] definir parâmetros obrigatórios;
- [ ] chamar a mesma função com valores diferentes;
- [ ] passar literais, variáveis, expressões e coleções;
- [ ] associar argumentos posicionais pela ordem;
- [ ] escrever argumentos nomeados básicos;
- [ ] misturar corretamente argumentos posicionais e depois nomeados;
- [ ] evitar associação duplicada de parâmetros;
- [ ] escolher nomes significativos para parâmetros;
- [ ] usar parâmetros com `if` e loops;
- [ ] reconhecer argumentos ausentes, extras, duplicados e inesperados;
- [ ] rastrear a entrada do chamador ao parâmetro e ao corpo.

## 32. Referência rápida

| Necessidade | Forma | Significado |
|---|---|---|
| uma entrada obrigatória | `def greet(name):` | `name` é um parâmetro |
| fornecer entrada | `greet("Maya")` | `"Maya"` é um argumento |
| várias entradas | `def show_book(title, year):` | dois parâmetros |
| chamada posicional | `show_book("Python", 2026)` | associa pela posição |
| chamada nomeada | `show_book(title="Python", year=2026)` | associa pelo nome do parâmetro |
| chamada mista válida | `show_book("Python", year=2026)` | posicional primeiro, depois nomeado |
| entrada obrigatória ausente | poucos argumentos | `TypeError` |
| entrada extra | argumentos demais | `TypeError` |
| nome inesperado | sem parâmetro correspondente | `TypeError` |
| associação duplicada | mesmo parâmetro duas vezes | `TypeError` |

## 33. Limite de escopo

Este capítulo intencionalmente não ensina em profundidade:

- `return` e design de valores de retorno;
- regras de escopo local e global;
- type hints e anotações;
- valores padrão de parâmetros;
- armadilhas de padrões mutáveis;
- `*args` e `**kwargs`;
- parâmetros somente posicionais com `/`;
- parâmetros somente nomeados com `*`;
- desempacotamento de argumentos com `*` ou `**`;
- semântica de mutação e compartilhamento de objetos;
- funções aninhadas, lambdas, decorators, generators ou recursão.

O objetivo aqui é um modelo confiável de **entradas obrigatórias e chamadas comuns**.

## 34. O que vem a seguir

Agora você consegue fornecer valores de entrada obrigatórios a uma função e associar argumentos de chamadas comuns aos parâmetros.

A próxima pergunta é:

> Como uma função pode enviar um resultado útil de volta ao chamador?

Isso leva ao **Capítulo 03: Valores de Retorno**.

Volte para a [trilha de Funções](../README.pt-BR.md) ou para a [trilha completa](../../docs/learning-path.pt-BR.md).

## Referências

Documentação primária do Python:

- [Tutorial do Python 3.13: Definindo funções](https://docs.python.org/pt-br/3.13/tutorial/controlflow.html#defining-functions)
- [Tutorial do Python 3.13: Mais sobre definição de funções](https://docs.python.org/pt-br/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Tutorial do Python 3.13: Argumentos nomeados](https://docs.python.org/pt-br/3.13/tutorial/controlflow.html#keyword-arguments)
- [Referência da Linguagem Python 3.13: Definições de função](https://docs.python.org/pt-br/3.13/reference/compound_stmts.html#function-definitions)
- [Referência da Linguagem Python 3.13: Chamadas](https://docs.python.org/pt-br/3.13/reference/expressions.html#calls)
