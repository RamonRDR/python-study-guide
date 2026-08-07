<div align="center">

# Saída com `print()` e Entrada com `input()`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Como o Python executa um programa](../01-how-python-runs-a-program/README.pt-BR.md)

Um programa se torna mais fácil de compreender quando consegue mostrar o que está fazendo e receber informações da pessoa que o utiliza. O Python fornece duas funções embutidas para essas primeiras conversas: `print()` exibe saídas, e `input()` lê uma linha de texto no terminal.

Este capítulo constrói um pequeno programa interativo enquanto mantém clara a diferença entre saída do programa, entrada digitada e código-fonte.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante absoluto |
| Pré-requisitos | Criar, salvar e executar um arquivo `.py` pelo terminal |
| Tempo estimado de estudo | 45 a 65 minutos |
| Conceitos principais | Saída, entrada, chamada de função, argumento, prompt, `sep`, `end`, texto retornado |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- usar `print()` para exibir textos e outros valores;
- passar mais de um valor para `print()`;
- controlar o separador e o final da linha com `sep` e `end`;
- usar `input()` com um prompt claro;
- explicar por que `input()` pausa o programa;
- armazenar sob um nome o texto retornado por `input()`;
- distinguir a saída do programa do texto digitado pela pessoa usuária;
- reconhecer quando uma entrada interativa é inadequada para programas sem supervisão.

## 1. Saída e entrada seguem direções diferentes

**Saída** é a informação que o programa envia para fora. Ela pode aparecer em um terminal, interface gráfica, arquivo, log ou outro destino.

**Entrada** é a informação que entra no programa. Ela pode vir de um teclado, arquivo, requisição de rede, sensor ou outro sistema.

Neste capítulo:

- `print()` envia texto para o terminal;
- `input()` recebe uma linha digitada no terminal.

```text
pessoa ──entrada──▶ programa ──saída──▶ terminal
```

## 2. `print()` e `input()` são funções embutidas

Uma função é uma operação reutilizável. Chamar uma função significa escrever seu nome seguido de parênteses.

```python
print("Hello, World!")
```

Nesta chamada:

- `print` é o nome da função;
- os parênteses chamam a função;
- `"Hello, World!"` é um argumento fornecido à função.

Tanto `print()` quanto `input()` são embutidas no Python, portanto estes primeiros exemplos não precisam de uma instrução `import`.

## 3. Exiba um valor com `print()`

A forma mais simples exibe um valor:

```python
print("Python is running.")
```

Saída esperada:

```text
Python is running.
```

As aspas pertencem ao código-fonte. Elas indicam um valor de texto e não são exibidas como parte da saída.

## 4. Exiba vários valores

Separe vários argumentos com vírgulas:

```python
print("Python", "Study", "Guide")
```

Saída esperada:

```text
Python Study Guide
```

Por padrão, `print()` insere um espaço entre os argumentos exibidos.

Uma vírgula entre argumentos faz parte da sintaxe do Python. Uma vírgula escrita dentro das aspas é um texto comum:

```python
print("Hello,", "student!")
```

Saída esperada:

```text
Hello, student!
```

## 5. Altere o separador com `sep`

O argumento `sep` controla o que aparece entre vários valores exibidos:

```python
print("2026", "08", "06", sep="-")
```

Saída esperada:

```text
2026-08-06
```

Outro exemplo:

```python
print("Python", "Study", "Guide", sep=" | ")
```

Saída esperada:

```text
Python | Study | Guide
```

`sep` só faz diferença quando `print()` recebe mais de um valor.

## 6. Altere o final da linha com `end`

Por padrão, `print()` termina com uma quebra de linha, fazendo a próxima saída começar na linha seguinte.

O argumento `end` substitui essa quebra final:

```python
print("Loading", end="...")
print("done!")
```

Saída esperada:

```text
Loading...done!
```

Use `end` de forma deliberada. Remover quebras de linha em todos os lugares pode tornar a saída do terminal difícil de ler.

## 7. Imprima uma linha em branco

Chamar `print()` sem argumentos escreve somente sua quebra de linha padrão:

```python
print("First section")
print()
print("Second section")
```

Saída esperada:

```text
First section

Second section
```

Isso é útil para separar pequenos grupos de saída no terminal.

## 8. Leia uma linha com `input()`

`input()` pode exibir um prompt e aguardar a pessoa digitar uma resposta:

```python
name = input("What is your name? ")
```

O programa pausa nesta linha. Depois que a pessoa digita uma resposta e pressiona Enter, `input()` retorna essa resposta como texto.

O espaço antes das aspas finais mantém o cursor visualmente separado do prompt:

```text
What is your name? Ada
```

Sem esse espaço, a resposta digitada pode parecer grudada na pergunta.

## 9. Armazene o texto retornado

Esta linha realiza duas operações conectadas:

```python
name = input("What is your name? ")
```

1. `input()` lê e retorna um texto.
2. `name =` armazena esse texto retornado sob o nome `name`.

O próximo capítulo explica variáveis e nomes em detalhes. Por enquanto, trate `name` como um rótulo que permite ao programa usar a resposta depois.

## 10. Exiba a resposta

Após armazenar o resultado, passe-o para `print()`:

```python
name = input("What is your name? ")
print("Hello,", name)
```

Uma possível sessão no terminal é:

```text
What is your name? Ada
Hello, Ada
```

A primeira linha contém o prompt do programa e a resposta digitada pela pessoa. Normalmente, o terminal mostra os caracteres conforme são digitados. A segunda linha é produzida por `print()`.

## 11. Faça mais de uma pergunta

As instruções continuam sendo executadas em ordem:

```python
name = input("What is your name? ")
city = input("Which city do you live in? ")

print("Name:", name)
print("City:", city)
```

O Python aguarda a primeira resposta antes de exibir o segundo prompt.

Uma possível sessão é:

```text
What is your name? Ada
Which city do you live in? London
Name: Ada
City: London
```

## 12. `input()` retorna texto

Mesmo quando uma pessoa digita algarismos, `input()` retorna um valor de texto. A resposta a seguir é um texto contendo os caracteres `2` e `5`, ainda não um número:

```python
age = input("How old are you? ")
print("You entered:", age)
```

O capítulo posterior sobre conversão de tipos explicará como transformar textos compatíveis em valores numéricos. Até lá, use o resultado como texto.

## 13. Pressionar Enter pode retornar texto vazio

Uma pessoa pode pressionar Enter sem digitar nenhum caractere visível:

```python
answer = input("Press Enter without typing: ")
print("You entered:", answer)
```

Nesse caso, `answer` contém um valor de texto vazio. O programa não decide automaticamente que uma entrada vazia é inválida. A validação será apresentada depois das condições e do fluxo do programa.

## 14. `input()` remove a quebra final do Enter

Pressionar Enter encerra a resposta. O caractere de final de linha usado para enviar a resposta não é incluído no texto retornado.

Por isso, a saída a seguir permanece em uma única linha:

```python
word = input("Type one word: ")
print("Received:", word)
```

A palavra digitada é retornada, mas a quebra usada para enviá-la é removida.

## 15. Quando usar `input()`

`input()` é útil para:

- exercícios para iniciantes;
- pequenas conversas no terminal;
- utilitários manuais usados por uma pessoa por vez;
- experimentos rápidos nos quais aguardar uma resposta é esperado.

Evite depender de `input()` quando um programa precisa executar sem uma pessoa, como em:

- tarefas agendadas;
- testes automatizados;
- serviços em segundo plano;
- integração contínua;
- pipelines de processamento de dados.

Um programa sem supervisão pode permanecer pausado indefinidamente ou falhar quando não existe uma fonte de entrada. Esses programas normalmente recebem configurações por argumentos, arquivos, variáveis de ambiente, APIs ou outras interfaces explícitas.

## 16. Exemplos do repositório

| Arquivo | Finalidade | Execução automática |
|---|---|---|
| [`output_basics.py`](examples/output_basics.py) | Demonstra vários valores, `sep`, `end` e linhas em branco | Sim |
| [`interactive_greeting.py`](examples/interactive_greeting.py) | Lê um nome e exibe uma saudação | Não; aguarda entrada no terminal |

O exemplo interativo não é incluído deliberadamente no manifesto de exemplos executados sem supervisão.

## 17. Exemplo prático: um cartão de estudante

Crie `student_card.py`:

```python
name = input("Name: ")
city = input("City: ")
learning_goal = input("Learning goal: ")

print()
print("STUDENT CARD")
print("Name:", name)
print("City:", city)
print("Goal:", learning_goal)
```

Uma possível sessão é:

```text
Name: Ada
City: London
Learning goal: Build useful programs

STUDENT CARD
Name: Ada
City: London
Goal: Build useful programs
```

Esse programa já possui um fluxo de dados simples: as perguntas produzem textos, os nomes mantêm esses textos e `print()` os exibe em uma nova organização.

## 18. Exercício

Crie um arquivo chamado `learning_check_in.py` que:

1. pergunte o nome da pessoa estudante;
2. pergunte qual tema de Python ela deseja estudar;
3. pergunte quantos minutos ela pretende praticar, mantendo a resposta como texto;
4. imprima uma linha em branco;
5. imprima o título `LEARNING CHECK-IN`;
6. exiba as três respostas em linhas separadas e identificadas;
7. imprima `Study`, `Understand` e `Practice` separados por ` -> `;
8. termine com `Ready!` na mesma linha que `Starting...`.

Use exatamente estas três chamadas finais:

```python
print("Study", "Understand", "Practice", sep=" -> ")
print("Starting", end="...")
print("Ready!")
```

Execute o programa pelo menos duas vezes com respostas diferentes.

## 19. Erros comuns

### Esquecer os parênteses

```text
print "Hello"
```

O Python 3 exige uma chamada de função com parênteses:

```python
print("Hello")
```

### Esquecer as aspas em um texto literal

```text
print(Hello)
```

Sem aspas, o Python trata `Hello` como um nome, e não como texto literal.

### Usar a sintaxe errada para o separador

Escreva `sep` dentro da chamada de `print()`:

```python
print("A", "B", sep="-")
```

### Esperar que `input()` continue imediatamente

`input()` aguarda até que uma linha seja enviada. Um programa que parece travado pode estar apenas esperando uma resposta.

### Esquecer de armazenar a resposta

Chamar `input()` sozinho lê um texto, mas a resposta é descartada se o programa não armazenar nem usar o valor retornado.

### Tratar algarismos digitados como número

`input()` retorna texto. A conversão numérica pertence a um capítulo posterior.

### Confundir o eco do terminal com `print()`

O terminal pode mostrar o que a pessoa digita. Essa resposta visível não é uma chamada adicional de `print()`.

## 20. Autoverificação

Você está pronto para o próximo capítulo quando conseguir responder:

- Em qual direção a saída se desloca?
- O que `print()` coloca entre vários argumentos por padrão?
- O que `end` substitui?
- Por que `input()` pausa o programa?
- Qual tipo de valor `input()` retorna?
- O que acontece quando a pessoa pressiona Enter sem digitar?
- Por que um script sem supervisão normalmente deve evitar entrada interativa?
- Qual texto visível no terminal foi produzido pelo programa e qual foi digitado pela pessoa?

## 21. Resumo para consulta rápida

| Objetivo | Exemplo |
|---|---|
| Exibir texto | `print("Hello")` |
| Exibir vários valores | `print("Name:", name)` |
| Alterar o separador | `print("A", "B", sep="-")` |
| Permanecer na mesma linha | `print("Loading", end="...")` |
| Imprimir uma linha em branco | `print()` |
| Fazer uma pergunta | `input("Question: ")` |
| Armazenar uma resposta | `answer = input("Question: ")` |
| Tipo importante da entrada | `input()` retorna texto |
| Resposta vazia | Pressionar Enter pode retornar texto vazio |
| Execução sem supervisão | Evite aguardar `input()` |

## 22. Execute os exemplos do repositório

Na raiz do repositório, execute o exemplo automático:

```bash
python fundamentals/02-print-and-input/examples/output_basics.py
```

Execute o exemplo interativo e responda ao prompt:

```bash
python fundamentals/02-print-and-input/examples/interactive_greeting.py
```

## 23. Execute as verificações do repositório

Na raiz do repositório:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

O executor de exemplos aprovados executa `output_basics.py`, mas não executa `interactive_greeting.py`, pois verificações sem supervisão não devem aguardar entrada pelo teclado.

## Referências oficiais

- [Documentação do Python — Funções embutidas: `print()` e `input()`](https://docs.python.org/3/library/functions.html)
- [Tutorial do Python — Entrada e saída](https://docs.python.org/3/tutorial/inputoutput.html)

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Como o Python executa um programa](../01-how-python-runs-a-program/README.pt-BR.md)
