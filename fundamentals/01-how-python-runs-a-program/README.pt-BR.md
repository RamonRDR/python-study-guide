<div align="center">

# Como o Python Executa um Programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md)

Um programa Python começa como um texto escrito por uma pessoa. Salvar esse texto em um arquivo `.py` não o executa. O programa só é executado quando o interpretador Python recebe a instrução de ler e executar o arquivo.

Este capítulo leva você de um arquivo vazio até um programa funcionando e, depois, mostra como modificá-lo, executá-lo novamente e corrigir um erro básico de sintaxe.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante absoluto |
| Pré-requisitos | Python instalado; acesso a um editor de texto e a um terminal |
| Tempo estimado de estudo | 40 a 60 minutos |
| Conceitos principais | Programa, código-fonte, arquivo `.py`, editor, terminal, interpretador, ordem de execução, erro de sintaxe |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar o que são um programa e o código-fonte;
- identificar a finalidade de um arquivo `.py`;
- diferenciar editor, terminal e interpretador Python;
- descrever a diferença entre escrever, salvar e executar código;
- criar e executar um arquivo Python pelo terminal;
- explicar como instruções comuns no nível superior são executadas de cima para baixo;
- localizar as partes úteis de uma mensagem básica de `SyntaxError`;
- modificar, salvar e executar novamente um programa.

## 1. O que é um programa?

Um programa é um conjunto de instruções que um computador pode executar.

Uma receita culinária também contém instruções ordenadas, mas um computador precisa de instruções escritas em uma linguagem que consiga processar. Neste guia, essa linguagem é Python.

Um programa pode conter uma instrução ou milhões de instruções. Seu primeiro programa contém apenas uma:

```python
print("Hello, World!")
```

Essa instrução pede ao Python que exiba um texto.

## 2. O que é código-fonte?

**Código-fonte** é o texto legível por pessoas usado para descrever um programa.

O texto a seguir é código-fonte Python:

```python
print("Hello, World!")
```

Código-fonte não é uma captura de tela, um documento formatado ou o resultado exibido pelo programa. É o texto que você escreve e salva para que uma implementação da linguagem possa processá-lo.

## 3. O que é um arquivo `.py`?

Um arquivo terminado em `.py` é normalmente usado para armazenar código-fonte Python.

Por exemplo:

```text
hello_world.py
```

O nome possui duas partes:

- `hello_world` é o nome do arquivo;
- `.py` é a extensão associada a arquivos de código-fonte Python.

A extensão ajuda pessoas e ferramentas a reconhecer o tipo do arquivo. Ela não executa o arquivo sozinha.

## 4. Editor, terminal e interpretador possuem funções diferentes

Essas três ferramentas costumam aparecer na mesma tela, mas não são a mesma coisa.

| Ferramenta | Função principal |
|---|---|
| Editor | Escrever e alterar o código-fonte |
| Terminal | Digitar comandos e visualizar a saída dos comandos |
| Interpretador Python | Ler código Python e executá-lo |

Um editor pode incluir um terminal integrado. Um terminal pode iniciar o interpretador Python. As ferramentas podem trabalhar juntas sem se tornarem a mesma ferramenta.

## 5. Escrever, salvar e executar são ações separadas

Uma pessoa iniciante costuma realizar essas ações rapidamente e imaginar que são uma única etapa. Na verdade, são três:

1. **Escrever:** inserir ou modificar o código-fonte no editor.
2. **Salvar:** armazenar o texto atual em um arquivo.
3. **Executar:** pedir ao interpretador Python que execute o arquivo salvo.

Se você alterar o conteúdo no editor, mas não salvar, o interpretador normalmente executará a versão salva anteriormente. O texto não salvo ainda existe apenas no editor.

## 6. Crie `hello_world.py`

Abra um editor de texto simples ou um editor de código e crie um novo arquivo chamado:

```text
hello_world.py
```

Digite exatamente este código:

```python
print("Hello, World!")
```

Use aspas retas comuns (`"`), não aspas decorativas como `“` e `”`.

Salve o arquivo em uma pasta que você consiga encontrar novamente.

## 7. Abra o terminal na pasta do arquivo

O terminal trabalha com um **diretório atual**, que é a pasta onde os comandos estão sendo executados.

Antes de executar o programa, confirme que o terminal está na pasta que contém `hello_world.py`.

Muitos editores oferecem um comando como **Abrir no Terminal Integrado**. Você também pode abrir o terminal do sistema e navegar até a pasta.

Para visualizar os arquivos da pasta atual, um comando comum é:

```text
dir
```

no Windows, ou:

```text
ls
```

no macOS e Linux.

Você deverá ver `hello_world.py` no resultado.

## 8. Execute o arquivo

Execute:

```bash
python hello_world.py
```

Dependendo de como o Python foi instalado, o comando pode ser:

```bash
python3 hello_world.py
```

ou, em algumas instalações do Windows:

```bash
py hello_world.py
```

A saída esperada é:

```text
Hello, World!
```

A saída não faz parte do arquivo de código-fonte. Ela é produzida quando o programa é executado.

## 9. O que acontece depois do comando?

Para este comando:

```bash
python hello_world.py
```

um fluxo de execução simplificado é:

1. o terminal recebe o comando;
2. o sistema operacional inicia o interpretador Python;
3. o interpretador abre `hello_world.py`;
4. o Python verifica se o código-fonte segue a gramática da linguagem;
5. o Python executa as instruções de nível superior do programa em ordem;
6. `print()` envia texto para a saída padrão do programa;
7. o interpretador termina porque não restam instruções.

As implementações do Python realizam trabalhos internos que esta descrição para iniciantes não apresenta. Você não precisa entender bytecode ou máquinas virtuais para criar e executar seus primeiros scripts.

## 10. Instruções de nível superior normalmente são executadas de cima para baixo

Considere este arquivo:

```python
print("First")
print("Second")
print("Third")
```

Sua saída é:

```text
First
Second
Third
```

Os efeitos visíveis acontecem na mesma ordem das instruções de nível superior.

Capítulos posteriores apresentarão condições, laços, funções, exceções e importações. Esses recursos podem repetir, ignorar, adiar ou redirecionar a execução. Para um arquivo simples com chamadas consecutivas de `print()`, o modelo correto é de cima para baixo.

## 11. Um arquivo é diferente do modo interativo

Executar um arquivo:

```bash
python hello_world.py
```

pede ao Python que execute o script salvo.

Executar o Python sem informar um arquivo:

```bash
python
```

normalmente abre o interpretador interativo e exibe um prompt como:

```text
>>>
```

O modo interativo é útil para pequenos experimentos. Um arquivo `.py` é melhor quando você deseja salvar, revisar, executar novamente, compartilhar ou versionar o programa.

Para sair do modo interativo, use `exit()` ou o atalho de saída informado pelo terminal.

## 12. Modifique e execute o programa novamente

Altere o arquivo para:

```python
print("Hello, World!")
print("I changed my first program.")
```

Depois:

1. salve o arquivo;
2. volte ao terminal;
3. execute novamente o mesmo comando.

```bash
python hello_world.py
```

Saída esperada:

```text
Hello, World!
I changed my first program.
```

O Python não usa automaticamente o conteúdo não salvo do editor. Salve antes de executar novamente.

## 13. O que é um erro de sintaxe?

O código-fonte Python precisa seguir a gramática da linguagem. Um **erro de sintaxe** significa que o Python não conseguiu entender a estrutura do programa o suficiente para executá-lo.

Por exemplo, esta linha não possui a aspa de fechamento:

```python
print("Hello, World!)
```

Quando o Python lê o arquivo, ele para antes de executar o programa e informa um `SyntaxError`.

Uma mensagem de erro simplificada pode ser semelhante a esta:

```text
  File "hello_world.py", line 1
    print("Hello, World!)
          ^
SyntaxError: unterminated string literal
```

O texto exato, o caminho e a posição do acento circunflexo podem variar conforme a versão do Python e o ambiente.

## 14. Leia uma mensagem básica de erro de baixo para cima

Para um erro básico de sintaxe, examine estas partes:

1. **Tipo e mensagem do erro:** a última linha informa `SyntaxError` e descreve o problema.
2. **Arquivo e linha:** o Python identifica o arquivo e uma linha aproximada onde a análise falhou.
3. **Trecho do código-fonte:** o Python exibe a linha relevante.
4. **Acento circunflexo (`^`):** ele aponta para perto do local onde o Python detectou que algo estava errado.

A posição da detecção nem sempre é a causa original. Um símbolo ausente antes, na mesma linha ou em uma linha anterior, pode fazer o Python reclamar depois.

Corrija o primeiro erro de sintaxe informado, salve o arquivo e execute-o novamente.

## 15. Corrija o programa

Restaure a aspa ausente:

```python
print("Hello, World!")
```

Salve o arquivo e execute:

```bash
python hello_world.py
```

O programa deverá exibir:

```text
Hello, World!
```

Erros fazem parte da programação. O hábito útil não é evitar todos os erros, mas ler as evidências, alterar uma causa e testar novamente.

## 16. Problemas comuns no primeiro programa

### O comando não encontra o Python

Tente o comando usado pela sua instalação: `python`, `python3` ou `py`. Se nenhum funcionar, o Python pode não estar instalado ou pode não estar disponível no caminho de busca de comandos do terminal.

### O Python não consegue abrir o arquivo

O terminal pode estar no diretório errado ou o nome do arquivo pode ser diferente. Confira a pasta atual e a escrita do nome.

### A saída não mudou

Salve o arquivo antes de executá-lo novamente. Confirme também que você está editando e executando o mesmo arquivo.

### O arquivo é, na verdade, `hello_world.py.txt`

Alguns sistemas ocultam extensões conhecidas. Confira o nome completo no editor ou nas propriedades do arquivo.

### As aspas parecem curvas

Substitua aspas decorativas por aspas retas ASCII.

### O editor mostra um botão de execução

Esse botão pode ser conveniente, mas aprenda também o comando no terminal. Isso facilita a diferenciação entre editor, terminal, interpretador, arquivo e diretório atual.

## 17. Exercício prático

Crie um novo arquivo chamado:

```text
first_steps.py
```

Adicione estas instruções:

```python
print("Python is running.")
print("I wrote this program.")
print("I saved the file.")
print("I ran it from the terminal.")
```

Complete a sequência:

1. salve o arquivo;
2. execute-o pelo terminal;
3. confirme que as quatro linhas aparecem em ordem;
4. altere a terceira instrução para:

```python
print("I changed the program.")
```

5. salve e execute o arquivo novamente;
6. remova deliberadamente a aspa final da última instrução;
7. salve e execute o arquivo;
8. identifique o nome do arquivo, o número da linha, o tipo e a mensagem do erro;
9. restaure a aspa;
10. salve e execute o programa corrigido.

Seu programa final deverá ser executado sem erro de sintaxe e exibir quatro linhas.

## 18. Verificação de aprendizagem

Você está pronto para o próximo capítulo quando conseguir responder:

- Qual é a diferença entre código-fonte e saída do programa?
- Por que alterar o texto no editor não necessariamente altera a próxima execução?
- Qual ferramenta recebe `python hello_world.py`?
- Qual ferramenta entende o código-fonte Python?
- Em qual ordem instruções simples de `print()` no nível superior são executadas?
- Qual parte de uma mensagem básica de erro identifica o tipo do erro?
- O que você deve fazer depois de corrigir o código-fonte?

## 19. Resumo de consulta rápida

| Situação | Ação |
|---|---|
| Escrever código | Use um editor de texto simples ou de código |
| Armazenar as alterações atuais | Salve o arquivo `.py` |
| Executar um script | `python file_name.py` |
| Comandos alternativos | `python3 file_name.py` ou `py file_name.py` |
| Experimentar interativamente | Execute `python` sem informar um arquivo |
| A saída não foi atualizada | Salve e confirme o arquivo executado |
| O arquivo não foi encontrado | Confira o diretório e o nome do arquivo |
| Erro de sintaxe | Leia a última linha, o arquivo, a linha, o trecho e o `^` |
| Depois de uma correção | Salve e execute novamente |
| Ordem de execução simples | Instruções de nível superior são executadas em ordem, normalmente de cima para baixo |

## 20. Execute o exemplo do repositório

A partir da raiz do repositório:

```bash
python fundamentals/01-how-python-runs-a-program/examples/hello_world.py
```

Saída esperada:

```text
Hello, World!
```

## 21. Execute as verificações do repositório

A partir da raiz do repositório:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## Referências oficiais

- [Tutorial do Python — Utilizando o interpretador Python](https://docs.python.org/pt-br/3/tutorial/interpreter.html)
- [Tutorial do Python — Erros de sintaxe](https://docs.python.org/pt-br/3/tutorial/errors.html#erros-de-sintaxe)
- [Documentação do Python — Linha de comando e ambiente](https://docs.python.org/pt-br/3/using/cmdline.html)

[← Voltar ao índice da seção](../README.pt-BR.md)
