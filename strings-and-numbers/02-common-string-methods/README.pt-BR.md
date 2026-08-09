# Métodos Comuns de Strings

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Criação e indexação de strings](../01-string-creation-and-indexing/README.pt-BR.md) · [Próximo capítulo: `int`, `float` e `bool` →](../03-int-float-and-bool/README.pt-BR.md)

O capítulo anterior ensinou como criar strings e ler suas posições e intervalos. Este capítulo acrescenta uma nova ideia: strings também oferecem **métodos**, operações reutilizáveis que podem inspecionar texto ou produzir um resultado do tipo string sem modificar o valor original.

Você aprenderá um conjunto focado de métodos que aparece constantemente em programas reais. O objetivo não é memorizar toda a API de `str`. É entender o padrão de chamada de métodos, reconhecer tarefas comuns com texto e escolher uma operação cujo comportamento corresponda à sua intenção.

## Informações do capítulo

| Item | Valor |
|---|---|
| Fase | 2 — Textos e números |
| Capítulo | 02 |
| Nível | Iniciante |
| Pré-requisito | Capítulo 01 — Criação e indexação de strings |
| Tipo principal | `str` |
| Ideia principal | Chamar métodos comuns de strings de forma deliberada, respeitando a imutabilidade |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que é um método de string;
- chamar métodos usando a notação com ponto;
- distinguir a string original do resultado de um método;
- normalizar maiúsculas e minúsculas com `lower()` e `upper()`;
- remover espaços em branco ao redor com `strip()`;
- remover prefixos e sufixos exatos com `removeprefix()` e `removesuffix()`;
- substituir texto com `replace()`;
- testar inícios e finais com `startswith()` e `endswith()`;
- localizar e contar substrings com `find()` e `count()`;
- dividir texto em partes com `split()`;
- unir strings com `join()`;
- combinar alguns métodos sem esconder a intenção do programa.

## 1. O que é um método?

Um **método** é uma operação semelhante a uma função associada a um objeto.

Um valor de string sabe realizar operações específicas de strings. Você solicita uma delas usando a **notação com ponto**:

```python
language = "Python"

print(language.upper())
```

```text
PYTHON
```

O ponto conecta o valor à esquerda a um método fornecido por seu tipo.

```text
value.method(arguments)
```

Alguns métodos não recebem argumentos. Outros precisam de informações entre os parênteses.

## 2. Métodos pertencem aos valores, não aos nomes das variáveis

Não é o nome da variável que possui o método. É o valor de string.

Estas duas chamadas são válidas:

```python
language = "Python"

print(language.lower())
print("Practice".lower())
```

```text
python
practice
```

Um nome é apenas uma forma de se referir a um valor. Isso se conecta diretamente à distinção entre nomes e valores estudada na Fase 1.

## 3. Métodos de string não editam a string original no lugar

Strings são imutáveis. Um método como `lower()` produz um resultado, mas não reescreve o valor de string que já existia.

```python
language = "Python"

lowercase_language = language.lower()

print(language)
print(lowercase_language)
```

```text
Python
python
```

Quando você precisa manter o resultado, atribua-o a um nome.

```python
language = "Python"
language = language.lower()

print(language)
```

```text
python
```

Isso é reatribuição. A string original não foi modificada.

## 4. `lower()` e `upper()` alteram a capitalização no resultado

Use `lower()` quando precisar de um resultado em minúsculas:

```python
message = "Python Practice"

print(message.lower())
```

```text
python practice
```

Use `upper()` quando precisar de um resultado em maiúsculas:

```python
message = "Python Practice"

print(message.upper())
```

```text
PYTHON PRACTICE
```

A conversão de maiúsculas e minúsculas é útil para exibição e para algumas tarefas de normalização.

Não presuma que mudar a capitalização valida o significado. `"YES".lower()` vira `"yes"`, mas seu programa ainda precisa de regras para decidir o que `"yes"` significa.

## 5. Normalize antes de comparar quando a capitalização não deve importar

Imagine que dois textos devam ser tratados da mesma forma independentemente de maiúsculas e minúsculas.

```python
expected = "python"
received = "PyThOn"

print(received.lower() == expected)
```

```text
True
```

Esse é um padrão comum para iniciantes.

Para comparações sem distinção de caixa mais avançadas e internacionalizadas, Python também oferece `casefold()`. Essa diferença é adiada de propósito para manter este capítulo focado nas operações mais comuns para iniciantes.

## 6. `strip()` remove espaços em branco ao redor por padrão

Entrada de usuário e textos externos frequentemente contêm espaços ou quebras de linha ao redor do conteúdo importante.

```python
raw_name = "   Python   "

clean_name = raw_name.strip()

print("[" + raw_name + "]")
print("[" + clean_name + "]")
```

```text
[   Python   ]
[Python]
```

Sem argumento, `strip()` remove espaços em branco no início e no final.

Ele **não** remove espaços do meio:

```python
text = "  Python Study Guide  "

print(text.strip())
```

```text
Python Study Guide
```

## 7. `strip(chars)` trata `chars` como um conjunto de caracteres removíveis

Esse detalhe é importante.

```python
text = "...Python..."

print(text.strip("."))
```

```text
Python
```

Quando um argumento é fornecido, `strip()` remove combinações desses caracteres das duas extremidades. Ele não é um removedor de "prefixo exato" ou "sufixo exato".

Por isso, este estilo pode enganar:

```python
filename = "report.txt"

print(filename.strip(".txt"))
```

O argumento é tratado como caracteres removíveis, e não como o sufixo exato `".txt"`.

Quando a intenção for remover um prefixo ou sufixo exato, use os métodos criados para essa tarefa.

## 8. `removeprefix()` e `removesuffix()` removem texto exato

**Nota de compatibilidade:** `str.removeprefix()` e `str.removesuffix()` foram adicionados no Python 3.9. Portanto, os exemplos desta seção exigem Python 3.9 ou mais recente. No Python 3.8 ou anterior, esses métodos não estão disponíveis e chamá-los gera `AttributeError`.

Use `removeprefix()` para um prefixo conhecido:

```python
resource = "draft-report"

print(resource.removeprefix("draft-"))
```

```text
report
```

Use `removesuffix()` para um sufixo conhecido:

```python
filename = "report.txt"

print(filename.removesuffix(".txt"))
```

```text
report
```

Quando o prefixo ou sufixo exato não existe, o valor textual é preservado.

Esses métodos expressam a intenção com mais precisão do que tentar imitar a remoção de prefixos ou sufixos usando `strip()`.

## 9. `replace()` substitui ocorrências

`replace(old, new)` produz um resultado no qual ocorrências de `old` são substituídas por `new`.

```python
sentence = "Python is clear. Python is practical."

print(sentence.replace("Python", "Code"))
```

```text
Code is clear. Code is practical.
```

Você pode limitar a quantidade de substituições com um terceiro argumento:

```python
sentence = "one one one"

print(sentence.replace("one", "two", 1))
```

```text
two one one
```

`replace()` realiza substituição textual. Ele não entende palavras, gramática, formatos de arquivo ou significado de negócio, a menos que seu programa acrescente essas regras.

## 10. Use `in` quando você só precisa saber se um texto existe

O operador de pertinência costuma ser a forma mais clara de perguntar se uma substring está presente.

```python
message = "Learn Python step by step"

print("Python" in message)
print("Java" in message)
```

```text
True
False
```

Ele não é um método, mas pertence a este conjunto de ferramentas de busca porque normalmente é a melhor opção para uma simples verificação de presença.

## 11. `startswith()` e `endswith()` expressam verificações nas extremidades

Use `startswith()` quando o início importa:

```python
filename = "report-2026.csv"

print(filename.startswith("report-"))
```

```text
True
```

Use `endswith()` quando o final importa:

```python
filename = "report-2026.csv"

print(filename.endswith(".csv"))
```

```text
True
```

Esses métodos retornam valores booleanos, conectando o trabalho com strings ao tipo `bool` estudado na Fase 1.

## 12. `find()` retorna a primeira posição correspondente ou `-1`

Use `find()` quando precisar da posição de uma substring.

```python
message = "Learn Python"

print(message.find("Python"))
print(message.find("Java"))
```

```text
6
-1
```

Uma substring encontrada retorna seu menor índice correspondente. Uma substring ausente retorna `-1`.

Se você só precisa saber se a substring existe, prefira `in`, pois o resultado comunica diretamente a pergunta feita.

## 13. `find()` e `index()` são parecidos, mas falham de formas diferentes

Strings também oferecem `index()`.

```python
message = "Learn Python"

print(message.index("Python"))
```

```text
6
```

A diferença importante aparece quando a substring não existe:

- `find()` retorna `-1`;
- `index()` gera `ValueError`.

Em código para iniciantes, escolha de acordo com o comportamento que seu programa realmente precisa. Não use `index()` apenas porque o nome parece mais familiar.

## 14. `count()` conta ocorrências que não se sobrepõem

Use `count()` quando precisar da quantidade de ocorrências.

```python
text = "banana"

print(text.count("a"))
print(text.count("na"))
```

```text
3
2
```

A contagem considera correspondências que não se sobrepõem.

Uma contagem igual a zero significa que a substring não foi encontrada.

## 15. `split()` separa texto em uma lista de strings

Sem um separador explícito, `split()` separa o texto em sequências de espaços em branco.

```python
text = "Python   makes   text readable"

words = text.split()

print(words)
```

```text
['Python', 'makes', 'text', 'readable']
```

O resultado é uma **lista** de strings.

Listas terão uma seção completa mais adiante no guia. Por enquanto, você só precisa reconhecer que `split()` pode transformar uma string em uma coleção ordenada de partes do tipo string.

## 16. `split(separator)` usa um delimitador explícito

Quando você fornece um separador, Python divide o texto usando exatamente essa string separadora.

```python
record = "python|beginner|active"

parts = record.split("|")

print(parts)
```

```text
['python', 'beginner', 'active']
```

Isso é diferente do comportamento de espaços em branco de `split()` sem argumento.

Separadores explícitos também podem produzir itens vazios:

```python
record = "a||b"

print(record.split("|"))
```

```text
['a', '', 'b']
```

Esse item vazio é informação: não havia nada entre dois separadores.

## 17. Texto vazio se comporta de forma diferente com divisão padrão e explícita

Compare estas duas chamadas:

```python
text = ""

print(text.split())
print(text.split(","))
```

```text
[]
['']
```

Sem separador, uma string vazia ou contendo somente espaços em branco produz uma lista vazia.

Com separador explícito, uma string vazia produz uma lista contendo uma string vazia, porque havia um campo e nenhuma ocorrência do separador.

Essa pequena diferença se torna importante ao processar dados delimitados.

## 18. `join()` combina strings usando um separador

`join()` costuma parecer invertido à primeira vista.

```python
words = ["Python", "Study", "Guide"]

print(" ".join(words))
print("-".join(words))
```

```text
Python Study Guide
Python-Study-Guide
```

A string **antes do ponto** é o separador.

Uma forma útil de ler isso é:

```text
separator.join(strings)
```

O separador pede para ser colocado entre os itens de string.

## 19. `join()` exige itens do tipo string

Isto funciona:

```python
parts = ["chapter", "02", "methods"]

print("/".join(parts))
```

```text
chapter/02/methods
```

Mas `join()` não converte automaticamente valores arbitrários em texto. Se a coleção contiver itens que não sejam strings, Python gera `TypeError`.

Esse desenho evita que conversões silenciosas escondam erros. Converta valores deliberadamente quando texto for realmente a representação desejada.

## 20. Dividir e unir são ideias complementares

Você pode dividir um texto em partes e depois unir essas partes de string usando outro separador.

```python
path_text = "docs/guides/python"

parts = path_text.split("/")
rebuilt = " > ".join(parts)

print(parts)
print(rebuilt)
```

```text
['docs', 'guides', 'python']
docs > guides > python
```

A lista é uma representação temporária das partes. `join()` cria o resultado textual final.

## 21. Métodos podem ser encadeados

Como muitos métodos de string retornam resultados do tipo string, às vezes outro método de string pode ser chamado imediatamente sobre esse resultado.

```python
raw_title = "  Python Guide  "

normalized_title = raw_title.strip().lower().replace(" ", "-")

print(normalized_title)
```

```text
python-guide
```

As chamadas são avaliadas da esquerda para a direita:

```text
raw_title
    -> strip()
    -> lower()
    -> replace(" ", "-")
```

O encadeamento é conveniente quando cada etapa continua óbvia.

## 22. Não transforme cadeias de métodos em quebra-cabeças

Uma expressão mais curta não é automaticamente mais clara.

Isto é legível:

```python
raw_title = "  Python Guide  "
clean_title = raw_title.strip()
lowercase_title = clean_title.lower()
normalized_title = lowercase_title.replace(" ", "-")

print(normalized_title)
```

```text
python-guide
```

Valores intermediários nomeados são úteis quando:

- uma transformação precisa de explicação;
- você quer inspecionar uma etapa;
- a cadeia está ficando longa;
- etapas diferentes representam intenções diferentes.

Clareza vale mais do que espremer toda transformação em uma linha.

## 23. Exemplo prático: normalize um rótulo

```python
raw_title = "  Python Study Guide  "

clean_title = raw_title.strip()
normalized_title = clean_title.lower().replace(" ", "-")

print("Raw:", "[" + raw_title + "]")
print("Clean:", clean_title)
print("Normalized:", normalized_title)
print("Starts with python:", clean_title.lower().startswith("python"))
print("Word count:", len(clean_title.split()))
```

```text
Raw: [  Python Study Guide  ]
Clean: Python Study Guide
Normalized: python-study-guide
Starts with python: True
Word count: 3
```

Esse exemplo combina limpeza, normalização de capitalização, substituição, verificação de início e divisão de texto sem alterar a entrada original no lugar.

## 24. Exemplo prático: divida e reconstrua um texto parecido com caminho

```python
path_text = "docs/guides/python"

parts = path_text.split("/")

print("Parts:", parts)
print("Joined:", " > ".join(parts))
print("First separator:", path_text.find("/"))
print("Slash count:", path_text.count("/"))
print("Ends with python:", path_text.endswith("python"))
```

```text
Parts: ['docs', 'guides', 'python']
Joined: docs > guides > python
First separator: 4
Slash count: 2
Ends with python: True
```

Isto é texto simples de propósito, não lógica de sistema de arquivos. Um capítulo posterior da biblioteca padrão apresentará `pathlib` para caminhos reais do sistema de arquivos.

## 25. Erros comuns

### Esquecer os parênteses

Uma chamada de método precisa de parênteses:

```python
language = "Python"

print(language.lower())
```

Sem `()`, você está se referindo ao próprio método, em vez de chamá-lo.

### Esperar que um método modifique a string

```python
language = "Python"
language.lower()

print(language)
```

```text
Python
```

Armazene ou reatribua o resultado quando precisar dele.

### Usar `strip()` como removedor de prefixo ou sufixo exato

`strip(chars)` remove caracteres das duas extremidades de acordo com um conjunto de caracteres. Use `removeprefix()` ou `removesuffix()` para texto exato nas extremidades.

### Usar `find()` diretamente como booleano

Uma substring encontrada pode estar no índice `0`, e `0` é tratado como falso em um contexto booleano. Uma substring ausente produz `-1`, e `-1` é tratado como verdadeiro.

Por isso, este é um teste de presença ruim:

```python
text = "Python"

print(bool(text.find("Python")))
print(bool(text.find("Java")))
```

```text
False
True
```

Use `"Python" in text` quando a pergunta for simplesmente se a substring existe.

### Esquecer que separadores explícitos de `split()` preservam campos vazios

`"a||b".split("|")` contém uma string vazia entre os dois separadores. Não descarte esse fato a menos que as regras dos seus dados indiquem que é seguro.

### Chamar `join()` na coleção em vez do separador

O padrão é:

```text
separator.join(strings)
```

e não `strings.join(separator)`.

## 26. Conexões com conceitos anteriores

Este capítulo combina várias ideias já estudadas:

- valores de string são instâncias de `str`;
- strings são imutáveis;
- resultados de métodos podem ser atribuídos a variáveis;
- resultados `bool` aparecem em `startswith()` e `endswith()`;
- índices aparecem em `find()`;
- `len()` pode medir a lista retornada por `split()`;
- a conversão de tipos continua explícita quando valores que não são strings precisam virar texto.

Ele também antecipa assuntos posteriores:

- listas explicarão em profundidade o objeto retornado por `split()`;
- condicionais agirão sobre resultados booleanos de busca;
- loops processarão muitas partes de strings;
- arquivos e dados CSV exigirão divisão cuidadosa ou parsers estruturados;
- `pathlib` substituirá truques manuais com strings para caminhos reais do sistema de arquivos.

## 27. Exercício: limpe e inspecione um valor textual

Crie `text_methods_practice.py` com:

```python
raw_text = "  Python,practice,python  "
```

Produza e exiba:

1. o texto original cercado por colchetes;
2. o texto após `strip()`;
3. uma versão em minúsculas;
4. a quantidade de ocorrências de `"python"` em minúsculas após a normalização;
5. uma versão em que as vírgulas são substituídas por `" | "`;
6. se o texto limpo começa com `"Python"`;
7. se termina com `"python"`;
8. a lista produzida pela divisão por vírgulas;
9. as mesmas partes unidas com `" -> "`.

Um formato possível de saída é:

```text
Original: [  Python,practice,python  ]
Clean: Python,practice,python
Lowercase: python,practice,python
Python count: 2
Replaced: Python | practice | python
Starts with Python: True
Ends with python: True
Parts: ['Python', 'practice', 'python']
Joined: Python -> practice -> python
```

Tente resolver cada transformação separadamente antes de comprimir etapas em uma cadeia de métodos.

## 28. Autoavaliação

Confirme se você consegue responder:

1. O que o ponto significa em `text.lower()`?
2. Por que `text.lower()` não modifica `text` no lugar?
3. O que `strip()` remove quando chamado sem argumentos?
4. Por que `strip(".txt")` não representa a mesma ideia que `removesuffix(".txt")`?
5. Quando `in` é mais claro do que `find()`?
6. O que `find()` retorna quando nenhuma correspondência existe?
7. O que `count()` mede?
8. Qual tipo `split()` retorna?
9. Por que `split("|")` pode produzir itens de string vazios?
10. Qual objeto fornece o separador em `" - ".join(parts)`?
11. Por que uma cadeia de métodos longa pode reduzir a legibilidade?
12. O que você deve fazer quando `join()` recebe valores que não são strings?

## 29. Referência rápida

| Objetivo | Operação | Resultado de exemplo |
|---|---|---|
| Minúsculas | `text.lower()` | `"Py".lower()` → `"py"` |
| Maiúsculas | `text.upper()` | `"Py".upper()` → `"PY"` |
| Remover espaços ao redor | `text.strip()` | `"  Py  ".strip()` → `"Py"` |
| Remover prefixo exato | `text.removeprefix(prefix)` | `"pre-item".removeprefix("pre-")` → `"item"` |
| Remover sufixo exato | `text.removesuffix(suffix)` | `"file.txt".removesuffix(".txt")` → `"file"` |
| Substituir texto | `text.replace(old, new)` | `"a-b".replace("-", "/")` → `"a/b"` |
| Verificar presença | `sub in text` | `"Py" in "Python"` → `True` |
| Verificar início | `text.startswith(prefix)` | `"Python".startswith("Py")` → `True` |
| Verificar final | `text.endswith(suffix)` | `"a.py".endswith(".py")` → `True` |
| Encontrar primeira posição | `text.find(sub)` | `"Python".find("th")` → `2` |
| Contar ocorrências | `text.count(sub)` | `"banana".count("a")` → `3` |
| Dividir por espaços | `text.split()` | `"a  b".split()` → `['a', 'b']` |
| Dividir por delimitador | `text.split(sep)` | `"a|b".split("|")` → `['a', 'b']` |
| Unir strings | `sep.join(strings)` | `"-".join(["a", "b"])` → `"a-b"` |

## 30. Exemplos do repositório

Execute os exemplos determinísticos:

```bash
python strings-and-numbers/02-common-string-methods/examples/normalize_text.py
python strings-and-numbers/02-common-string-methods/examples/split_and_join.py
```

Depois execute as validações do repositório:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 31. O que vem a seguir

Agora você consegue transformar, inspecionar, dividir e unir texto mantendo a imutabilidade das strings em mente.

O próximo capítulo muda o foco do texto para valores numéricos e lógicos: **`int`, `float` e `bool` com mais profundidade**.

## Referências oficiais

- [Tipos embutidos do Python — Tipo sequência de texto `str`](https://docs.python.org/pt-br/3.14/library/stdtypes.html#text-sequence-type-str)
- [Tipos embutidos do Python — Métodos de string](https://docs.python.org/pt-br/3.14/library/stdtypes.html#string-methods)
- [Tipos embutidos do Python — Resumo dos métodos de sequência de texto e binária](https://docs.python.org/pt-br/3.14/library/stdtypes.html#text-and-binary-sequence-type-methods-summary)
- [O que há de novo no Python 3.9 — Novos métodos de strings para remover prefixos e sufixos](https://docs.python.org/pt-br/3/whatsnew/3.9.html#new-string-methods-to-remove-prefixes-and-suffixes)

[← Voltar ao índice da seção](../README.pt-BR.md)
