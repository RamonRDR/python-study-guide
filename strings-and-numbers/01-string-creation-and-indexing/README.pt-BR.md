<div align="center">

# Criação e Indexação de Strings

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md)

A Fase 1 ensinou que valores de texto comuns usam o tipo `str`. Este primeiro capítulo da Fase 2 aprofunda esse conceito: ele mostra como criar strings e como ler posições individuais e intervalos dentro delas.

Uma string em Python é uma sequência imutável de pontos de código Unicode. Para quem está começando, um modelo mental útil é mais simples: uma string é um valor de texto ordenado cujas posições podem ser lidas, mas não substituídas no próprio valor.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir a Fase 1: Fundamentos |
| Tempo estimado de estudo | 70 a 90 minutos |
| Conceitos principais | `str`, literais de string, `len()`, indexação, índices negativos, fatiamento, imutabilidade, `IndexError` |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- criar strings com aspas simples, duplas e triplas;
- explicar o que as aspas do código-fonte fazem e o que não se torna parte do valor;
- usar sequências de escape comuns quando necessário;
- medir uma string com `len()`;
- ler posições usando índices positivos e negativos;
- explicar por que o primeiro índice é `0`;
- ler intervalos usando slices;
- explicar por que um slice exclui seu limite final;
- distinguir um índice direto inválido de um slice amplo e válido;
- explicar a imutabilidade das strings;
- reconhecer que indexar uma string retorna outro `str`.

## 1. Strings são valores de texto ordenados

Você já usou strings ao longo do guia:

```python
course_name = "Python Study Guide"
current_topic = "Strings"
```

A ordem importa. `"Python"` e `"nohtyP"` contêm as mesmas letras, mas são strings diferentes porque seus itens aparecem em sequências diferentes.

Essa estrutura ordenada torna a indexação possível.

```text
Text:   P y t h o n
Index:  0 1 2 3 4 5
```

Cada posição possui um índice inteiro. A primeira posição é `0`.

## 2. Criando literais de string

Um literal de string é uma notação no código-fonte que cria um valor de string.

Aspas simples e aspas duplas criam strings comuns:

```python
single_quoted = 'Python'
double_quoted = "Python"

print(single_quoted == double_quoted)
```

```text
True
```

Para strings comuns, a escolha das aspas não altera o texto resultante. Escolha a forma que mantenha o código-fonte mais legível.

```python
message = "Python's syntax can be readable."
quotation = 'She said "practice".'
```

As aspas que delimitam o literal fazem parte da sintaxe. Normalmente, elas não fazem parte do valor resultante.

## 3. Escapes dentro de um literal

Uma barra invertida pode iniciar uma sequência de escape quando o texto precisa de um caractere que seria inconveniente escrever diretamente.

```python
message = "She said \"practice\"."
two_lines = "first line\nsecond line"

print(message)
print(two_lines)
```

```text
She said "practice".
first line
second line
```

Algumas sequências de escape úteis no início são:

- `\n` para uma nova linha;
- `\t` para uma tabulação;
- `\\` para uma barra invertida literal;
- `\"` para uma aspa dupla;
- `\'` para uma aspa simples.

Não tente memorizar todas de uma vez. Use-as quando um valor real precisar delas.

## 4. Strings com aspas triplas

Grupos correspondentes de três aspas simples ou três aspas duplas podem ocupar várias linhas físicas.

```python
message = """Study
understand
practice"""

print(message)
```

```text
Study
understand
practice
```

As quebras de linha fazem parte do valor da string.

Strings com aspas triplas também aparecem em docstrings, mas uma string com aspas triplas não é automaticamente uma docstring. Seu papel depende de onde ela aparece no programa.

## 5. A string vazia

Uma string pode não conter nenhum ponto de código.

```python
empty_text = ""

print(len(empty_text))
```

```text
0
```

A string vazia continua sendo um `str` válido. Ela não é a mesma coisa que `None`.

## 6. Medindo uma string com `len()`

`len()` retorna a quantidade de itens de uma sequência. Para strings, retorna a quantidade de pontos de código Unicode.

```python
language = "Python"
topic = "Python strings"

print(len(language))
print(len(topic))
```

```text
6
14
```

Os espaços também contam porque fazem parte da string.

Para exemplos cotidianos de nível iniciante, `len(text)` é uma boa forma de raciocinar sobre quantas posições indexadas a string disponibiliza.

### Nota de precisão sobre Unicode

Strings em Python são texto Unicode. `len()` conta pontos de código Unicode, não bytes. Alguns símbolos visíveis podem ser representados por vários pontos de código, então a quantidade de símbolos visuais e o resultado de `len()` não são garantidos como iguais em todos os sistemas de escrita ou sequências de emoji.

Você não precisa estudar algoritmos de segmentação Unicode neste capítulo. A ideia principal é que o texto do Python não é modelado como bytes brutos.

## 7. A indexação positiva começa em zero

Colchetes leem uma posição de uma string.

```python
language = "Python"

print(language[0])
print(language[1])
print(language[5])
```

```text
P
y
n
```

Para uma string não vazia de comprimento `n`, os índices positivos válidos vão de `0` até `n - 1`.

```text
len("Python") == 6
valid indexes: 0 1 2 3 4 5
```

O índice `6` já está fora da string.

## 8. Por que o primeiro índice é zero

Ajuda pensar em um índice como um deslocamento a partir do início.

```text
P y t h o n
^
0 positions away from the beginning
```

O item no índice `0` está a zero posições do início. O item no índice `1` está a uma posição do início.

O Python usa essa convenção de indexação iniciada em zero para vários tipos de sequência, não apenas strings.

## 9. Índices negativos contam a partir do final

Índices negativos permitem ler posições em relação ao final.

```python
language = "Python"

print(language[-1])
print(language[-2])
print(language[-6])
```

```text
n
o
P
```

```text
Text:       P  y  t  h  o  n
Positive:   0  1  2  3  4  5
Negative:  -6 -5 -4 -3 -2 -1
```

`-1` representa o último item, `-2` representa o anterior e assim por diante.

## 10. A indexação retorna outra string

O Python não possui um tipo embutido separado para caracteres.

```python
language = "Python"
first_item = language[0]

print(first_item)
print(type(first_item))
print(len(first_item))
```

```text
P
<class 'str'>
1
```

Um item textual indexado é simplesmente um `str` de comprimento `1`.

## 11. Índices diretos inválidos geram `IndexError`

Um índice direto pede uma posição exata. Se essa posição não existir, o Python gera `IndexError`.

```python
language = "Python"

print(language[6])
```

```text
IndexError: string index out of range
```

O traceback completo também contém informações de arquivo e linha. Aqui, a parte importante é o tipo da exceção e sua mensagem.

Uma string vazia não possui nenhum índice direto válido.

## 12. Fatiamento lê um intervalo

A indexação lê um item. O fatiamento lê um intervalo e retorna um resultado do tipo string sem modificar a string original.

Sintaxe básica:

```text
text[start:stop]
```

O limite `start` é incluído. O limite `stop` é excluído.

```python
language = "Python"

print(language[0:3])
```

```text
Pyt
```

Os índices `0`, `1` e `2` são incluídos. O índice `3` marca onde o slice termina.

## 13. Por que o limite final é excluído

Limites finais exclusivos fazem intervalos adjacentes se encaixarem de forma limpa.

```python
language = "Python"

prefix = language[0:3]
suffix = language[3:6]

print(prefix)
print(suffix)
print(prefix + suffix)
```

```text
Pyt
hon
Python
```

O limite `3` encerra o primeiro slice e inicia o segundo.

Com o passo unitário padrão, quando `0 <= start <= stop <= len(text)`, o tamanho do slice é `stop - start`.

## 14. Omitindo limites do slice

Omita `start` para começar no início da string:

```python
language = "Python"

print(language[:3])
print(language[3:])
print(language[:])
```

```text
Pyt
hon
Python
```

Omitir `stop` continua até o final. Omitir ambos retorna o texto completo como um slice.

Como strings são imutáveis, um slice completo normalmente é desnecessário apenas para "proteger" o valor original.

## 15. Índices negativos em slices

Os limites de um slice também podem ser negativos.

```python
filename = "notes.txt"

print(filename[:-4])
print(filename[-3:])
```

```text
notes
txt
```

Isso pode ser útil quando um limite é naturalmente descrito a partir do final.

Mantenha a legibilidade em mente. Uma expressão menor não é automaticamente uma expressão mais clara.

## 16. Slices toleram limites amplos

Um índice direto fora da string gera `IndexError`, mas um slice pode ultrapassar o intervalo disponível.

```python
language = "Python"

print(language[:100])
print(language[100:])
```

```text
Python

```

O primeiro slice retorna todo o texto disponível. O segundo retorna a string vazia.

```text
language[100]   -> one exact missing position -> IndexError
language[:100] -> available range             -> valid string
```

## 17. Primeiro contato com o passo de um slice

Slices podem possuir um terceiro componente:

```text
text[start:stop:step]
```

O passo controla como as posições são percorridas.

```python
language = "Python"

print(language[::2])
```

```text
Pto
```

Isso percorre os índices `0`, `2` e `4`.

Você não precisa de quebra-cabeças avançados de slicing nesta etapa. Slices com início e fim são mais importantes para código iniciante legível.

## 18. Strings são imutáveis

Uma string imutável não permite que uma de suas posições seja substituída no próprio valor após sua criação.

```python
language = "Python"
language[0] = "J"
```

```text
TypeError: 'str' object does not support item assignment
```

Para produzir um texto diferente, crie outro valor de string.

```python
language = "Python"
updated_language = "J" + language[1:]

print(language)
print(updated_language)
```

```text
Python
Jython
```

O próximo capítulo apresenta métodos de string que frequentemente expressam transformações de texto de forma mais clara.

## 19. Reatribuição não é mutação

Um nome de variável pode ser associado novamente a outra string.

```python
topic = "indexing"
topic = "slicing"

print(topic)
```

```text
slicing
```

O nome agora se refere a um valor de string diferente. A string original não foi editada no próprio objeto.

Isso se conecta diretamente à distinção entre nomes e valores estudada na Fase 1.

## 20. Exemplo prático: texto com posições fixas

Quando um formato realmente possui posições fixas, indexação e slicing podem separar suas partes.

```python
record_code = "PY-2048"

category = record_code[:2]
separator = record_code[2]
number_text = record_code[3:]

print("Category:", category)
print("Separator:", separator)
print("Number text:", number_text)
```

```text
Category: PY
Separator: -
Number text: 2048
```

Isso é apropriado somente quando as regras de posição são estáveis e conhecidas. Índices fixos se tornam frágeis quando o formato da entrada pode variar.

## 21. Exemplo prático: inspecionar um texto curto

```python
label = "practice"

print("Length:", len(label))
print("First:", label[0])
print("Last:", label[-1])
print("First four:", label[:4])
print("Remaining:", label[4:])
```

```text
Length: 8
First: p
Last: e
First four: prac
Remaining: tice
```

Esse exemplo combina as principais ferramentas do capítulo sem introduzir métodos de string ainda.

## 22. Erros comuns

### Tratar o índice `1` como a primeira posição

```python
language = "Python"
print(language[1])
```

Isso imprime `y`, não `P`. O primeiro índice é `0`.

### Usar `len(text)` como um índice válido

```python
language = "Python"
print(language[len(language)])
```

`len(language)` é `6`, mas o último índice positivo válido é `5`. Para o último item, `language[-1]` é mais claro.

### Esperar que o limite final do slice seja incluído

`language[0:3]` produz `"Pyt"`, não `"Pyth"`.

### Confundir reatribuição com mutação

Associar um nome novamente é válido. Atribuir a `text[0]` tenta modificar uma string e gera `TypeError`.

### Indexar um texto que pode estar vazio

Um índice direto exige que a posição solicitada exista. Capítulos posteriores sobre condicionais mostrarão como proteger essas suposições dinamicamente.

### Usar posições fixas em formatos variáveis

Use índices fixos somente quando o formato dos dados realmente garantir essas posições.

## 23. Conexões com conceitos anteriores

Este capítulo se apoia diretamente na Fase 1:

- variáveis dão nomes a valores de string;
- `type()` pode confirmar que resultados indexados são valores `str`;
- `len()` retorna um inteiro;
- índices são inteiros;
- slices retornam resultados do tipo string sem modificar a original;
- `print()` continua útil para inspecionar resultados.

Ele também prepara tópicos posteriores:

- métodos de string transformam e pesquisam texto;
- listas e tuplas também suportam indexação e slicing;
- loops podem percorrer itens de uma sequência repetidamente;
- condicionais podem proteger suposições sobre texto vazio;
- arquivos e dados externos frequentemente chegam como strings que precisam ser interpretadas.

## 24. Exercício: construa um inspetor de texto

Crie `text_inspector.py` com este valor inicial:

```python
text = "Python practice"
```

Exiba:

1. o texto completo;
2. seu comprimento;
3. seu primeiro item;
4. seu último item;
5. os seis primeiros itens;
6. a segunda palavra usando um slice;
7. um item a cada duas posições usando o passo de um slice;
8. o tipo do primeiro item indexado.

Um formato possível de saída é:

```text
Text: Python practice
Length: 15
First: P
Last: e
First six: Python
Second word: practice
Every second: Pto rcie
Indexed type: <class 'str'>
```

Tente escrever as expressões sozinho antes de comparar com os exemplos do repositório.

### Desafio extra

Crie um código fictício de formato fixo, como `"AB-2048"`, e separe o prefixo de duas letras, o hífen e o texto numérico usando índices e slices.

Ainda não converta o texto numérico. O objetivo é praticar posições em texto.

## 25. Autoavaliação

Certifique-se de conseguir responder:

1. Qual tipo representa texto comum em Python?
2. Qual é o primeiro índice válido de uma string não vazia?
3. O que `-1` representa?
4. Por que `text[len(text)]` está fora do intervalo válido?
5. Qual é a diferença entre indexação e slicing?
6. O limite final é incluído em um slice?
7. O que acontece quando um índice direto está fora da string?
8. Por que um slice amplo pode funcionar quando um índice direto amplo falha?
9. O que a imutabilidade das strings impede?
10. A indexação produz um tipo separado para caracteres?

## 26. Referência rápida

| Objetivo | Sintaxe | Exemplo |
|---|---|---|
| Criar texto | aspas | `name = "Python"` |
| String vazia | aspas vazias | `text = ""` |
| Medir texto | `len(text)` | `len("Python")` → `6` |
| Primeiro item | `text[0]` | `"Python"[0]` → `"P"` |
| Último item | `text[-1]` | `"Python"[-1]` → `"n"` |
| Ler um intervalo | `text[start:stop]` | `"Python"[0:3]` → `"Pyt"` |
| Desde o início | `text[:stop]` | `"Python"[:3]` → `"Pyt"` |
| Até o final | `text[start:]` | `"Python"[3:]` → `"hon"` |
| Usar um passo | `text[start:stop:step]` | `"Python"[::2]` → `"Pto"` |
| Índice direto inválido | posição exata inexistente | gera `IndexError` |
| Substituir um item | não suportado | gera `TypeError` |

## 27. Exemplos do repositório

Execute os exemplos determinísticos:

```bash
python strings-and-numbers/01-string-creation-and-indexing/examples/string_basics.py
python strings-and-numbers/01-string-creation-and-indexing/examples/fixed_position_text.py
```

Depois execute as verificações do repositório:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 28. O que vem depois

Agora você consegue criar strings, medi-las, ler posições exatas, ler intervalos e explicar por que uma string não pode ser editada item por item.

O próximo capítulo passa de posições para comportamento: **métodos comuns de strings** para tarefas como alterar capitalização, remover espaços extras, pesquisar, substituir, dividir e unir texto.

## Referências oficiais

- [Python Language Reference — String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)
- [Python Built-in Types — Text Sequence Type `str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python Built-in Types — Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [Python Built-in Functions — `len()`](https://docs.python.org/3/library/functions.html#len)

[← Voltar ao índice da seção](../README.pt-BR.md)
