<div align="center">

# Tipos de Dados Embutidos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Variáveis e nomes](../03-variables-and-naming/README.pt-BR.md)

As variáveis fornecem nomes úteis aos valores. A próxima pergunta é qual tipo de valor cada nome referencia. Os valores do Python possuem tipos, e um tipo ajuda a determinar como um valor é representado, quais operações fazem sentido e como o programa pode utilizá-lo.

Este capítulo apresenta um primeiro grupo direcionado de tipos embutidos: `str`, `int`, `float`, `bool` e `NoneType`. Ele não tenta catalogar todos os tipos do Python e deixa a inspeção formal com `type()` e `isinstance()` para o próximo capítulo.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir os Capítulos 01 a 03 |
| Tempo estimado de estudo | 55 a 75 minutos |
| Conceitos principais | Valor, tipo, tipo embutido, literal, `str`, `int`, `float`, `bool`, `None` |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar que todo valor do Python possui um tipo;
- reconhecer formas comuns no código-fonte que criam textos, inteiros, números de ponto flutuante, valores booleanos e `None`;
- diferenciar `"42"`, `42` e `42.0`;
- explicar por que as aspas alteram o tipo de valor criado;
- escrever `True`, `False` e `None` com a capitalização obrigatória;
- usar `None` para representar um valor intencionalmente ausente;
- prever comportamentos simples que mudam conforme o tipo do valor;
- lembrar que `input()` retorna texto;
- reconhecer que este capítulo aborda apenas um primeiro subconjunto dos tipos embutidos do Python.

## 1. Valores possuem tipos

Um **valor** é um dado utilizado por um programa. Um **tipo** classifica esse valor e define partes importantes de seu comportamento.

```text
notação do código-fonte ──cria──▶ valor ──possui──▶ tipo
```

Considere estas atribuições:

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

Os nomes são diferentes, mas a distinção decisiva também está nos valores:

- `"Python Study Guide"` é texto;
- `4` é um número inteiro;
- `60.0` é um número de ponto flutuante;
- `True` é um valor booleano;
- `None` indica a ausência de um valor.

## 2. O que significa “embutido”

Um tipo embutido está disponível como parte do próprio Python. Você não precisa instalar um pacote nem escrever uma instrução `import` para criar strings, inteiros, floats, valores booleanos ou `None` comuns.

“Embutido” não significa “os únicos tipos aceitos pelo Python”. Os programas também podem utilizar tipos de coleções, tipos fornecidos por bibliotecas e tipos criados por programadores.

## 3. A notação do código-fonte cria valores

Um programa utiliza formas reconhecíveis no código-fonte para criar valores diretamente. Aspas, pontos decimais e palavras reservadas são partes significativas dessa notação.

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None
```

Uma pequena alteração de caractere pode criar outro tipo de valor:

- `"4"` cria texto;
- `4` cria um inteiro;
- `4.0` cria um número de ponto flutuante.

O próximo capítulo mostrará como inspecionar esses tipos diretamente. Aqui, o objetivo é reconhecê-los a partir do código-fonte.

## 4. Textos usam `str`

O Python representa dados textuais com o tipo embutido `str`, pronunciado como “string”.

```python
course_name = "Python Study Guide"
learner_name = 'Ada'

print(course_name)
print(learner_name)
```

Saída esperada:

```text
Python Study Guide
Ada
```

Aspas simples ou duplas correspondentes podem criar literais de string comuns. Este projeto normalmente usa aspas duplas em exemplos pequenos por consistência, mas as duas formas são válidas.

## 5. Aspas não são decoração

As aspas informam ao Python que os caracteres delimitados formam texto:

```python
chapter_label = "4"
```

Sem aspas, a mesma sequência de algarismos cria um número:

```python
chapter_number = 4
```

As aspas pertencem ao código-fonte. `print()` exibe o conteúdo da string sem normalmente mostrar as aspas que a delimitam.

## 6. Números inteiros usam `int`

O Python representa números inteiros com o tipo embutido `int`.

```python
chapter_number = 4
practice_minutes = 45

print(chapter_number)
print(practice_minutes)
```

Os inteiros não contêm ponto decimal em sua notação decimal comum. Eles podem ser positivos, negativos ou zero:

```python
positive_value = 12
negative_value = -3
zero_value = 0
```

A aritmética detalhada pertence à fase de textos e números. Por enquanto, reconheça que `45` é um dado numérico, enquanto `"45"` é texto.

## 7. Números de ponto flutuante usam `float`

Um número escrito com ponto decimal normalmente cria um `float`:

```python
estimated_hours = 1.5
completion_rate = 0.75

print(estimated_hours)
print(completion_rate)
```

Valores de ponto flutuante são úteis para medidas, taxas, médias e muitos cálculos que não ficam restritos a números inteiros.

O ponto flutuante binário não consegue representar exatamente toda fração decimal. Esse tema de precisão importa em programas reais, mas pertence a um capítulo numérico posterior.

## 8. Valores lógicos usam `bool`

O tipo `bool` possui dois valores:

- `True`;
- `False`.

```python
is_available = True
needs_review = False

print(is_available)
print(needs_review)
```

Saída esperada:

```text
True
False
```

Valores booleanos normalmente representam estados de sim ou não, como disponibilidade, conclusão, permissão ou se uma condição foi atendida.

## 9. `True` e `False` exigem capitalização

A primeira letra deve ser maiúscula:

```python
is_available = True
needs_review = False

print(is_available)
print(needs_review)
```

Estas formas em minúsculas não são literais booleanos:

```text
is_available = true
needs_review = false
```

O Python trata `true` e `false` em minúsculas como nomes comuns. Se esses nomes não foram atribuídos anteriormente, sua leitura gera `NameError`.

## 10. `None` representa um valor ausente

`None` é uma constante embutida especial utilizada com frequência para representar a ausência de um valor.

```python
next_chapter = None
print(next_chapter)
```

Saída esperada:

```text
None
```

`None` é a única instância do tipo `NoneType`. Pessoas iniciantes normalmente escrevem `None` diretamente, em vez de tentar construir um valor `NoneType`.

## 11. `None` é uma informação intencional

`None` não significa necessariamente que algo deu errado. Ele pode comunicar deliberadamente:

- nenhum resultado está disponível ainda;
- um valor opcional não foi fornecido;
- um campo não possui valor aplicável;
- uma etapa posterior deverá fornecer o valor.

Escolha `None` quando “nenhum valor” for significativamente diferente de um texto válido ou de um número válido.

## 12. Saídas semelhantes podem esconder tipos diferentes

Estes valores parecem relacionados quando são impressos:

```python
text_number = "42"
whole_number = 42
decimal_number = 42.0

print(text_number)
print(whole_number)
print(decimal_number)
```

Saída esperada:

```text
42
42
42.0
```

As duas primeiras linhas exibem `42`, mas o primeiro valor é texto e o segundo é um inteiro. A saída simples nem sempre revela claramente o tipo.

## 13. O tipo afeta as operações

O mesmo operador pode se comportar de formas diferentes com tipos distintos:

```python
text_number = "42"
whole_number = 42
decimal_number = 42.0

print("Text repeated:", text_number + text_number)
print("Integer added:", whole_number + whole_number)
print("Float added:", decimal_number + decimal_number)
```

Saída esperada:

```text
Text repeated: 4242
Integer added: 84
Float added: 84.0
```

Para strings, `+` junta textos. Para números, `+` realiza adição. O Python utiliza os tipos dos operandos para decidir qual comportamento se aplica.

## 14. Um booleano entre aspas é apenas texto

Compare:

```python
real_flag = True
text_flag = "True"

print(real_flag)
print(text_flag)
```

As duas linhas exibem uma palavra semelhante, mas `real_flag` armazena um booleano e `text_flag` armazena texto.

Use valores booleanos verdadeiros para estados lógicos. Use strings somente quando o programa realmente precisar da palavra escrita.

## 15. A palavra `"None"` não é `None`

Compare:

```python
missing_value = None
written_word = "None"

print(missing_value)
print(written_word)
```

`missing_value` armazena o marcador especial de ausência. `written_word` armazena quatro caracteres comuns de texto.

Eles podem ser impressos de forma semelhante, mas comunicam informações diferentes ao programa.

## 16. `input()` continua retornando `str`

O Capítulo 02 estabeleceu uma regra importante:

```python
practice_minutes = input("Practice minutes: ")
print("Stored response:", practice_minutes)
```

Mesmo quando a pessoa digita `45`, o valor retornado é texto. O Python não converte automaticamente a entrada do terminal em inteiro ou float.

A conversão de tipos recebe um capítulo próprio depois que a pessoa estudante conseguir inspecionar tipos de forma confiável.

## 17. Um nome pode depois referenciar outro tipo

Os nomes no Python não são declarados permanentemente como um único tipo:

```python
current_value = "42"
print(current_value)

current_value = 42
print(current_value)

current_value = 42.0
print(current_value)
```

O nome `current_value` primeiro referencia uma string, depois um inteiro e, por fim, um float.

Essa flexibilidade é útil, mas alterar o significado e o tipo da mesma variável sem uma razão clara pode dificultar a compreensão do código.

## 18. Os nomes devem apoiar, não substituir, a compreensão dos tipos

Nomes claros podem sugerir o que um valor representa:

```python
age_text = "30"
age_number = 30
is_active = True
missing_note = None
```

Os sufixos e prefixos melhoram a legibilidade, mas o Python não os impõe. Uma pessoa ainda poderia atribuir o tipo errado de valor.

Use nomes significativos junto com a compreensão do valor real e de seu tipo.

## 19. Este capítulo não é um catálogo completo

O Python inclui muitos outros tipos embutidos. Uma breve prévia:

```python
topics = ["variables", "types"]
coordinates = (10, 20)
learner = {"name": "Ada"}
tags = {"python", "beginner"}
```

Esses exemplos apresentam listas, tuplas, dicionários e conjuntos apenas como um mapa do que existe. Suas estruturas e operações pertencem à fase de coleções.

O Python também possui outros tipos numéricos e de dados binários. A trilha de aprendizagem os apresenta quando se tornam úteis.

## 20. Exemplos do repositório

| Arquivo | Finalidade | Execução automática |
|---|---|---|
| [`value_catalog.py`](examples/value_catalog.py) | Armazena e exibe um exemplo de cada categoria de valor abordada | Sim |
| [`same_looking_values.py`](examples/same_looking_values.py) | Demonstra que valores de aparência semelhante podem se comportar de forma diferente | Sim |

Os dois exemplos são determinísticos, não interativos e estão incluídos no manifesto de exemplos executados sem supervisão.

## 21. Exemplo prático: catálogo de valores

Crie `value_catalog.py`:

```python
course_name = "Python Study Guide"
chapter_number = 4
estimated_minutes = 60.0
is_available = True
next_chapter = None

print("Course:", course_name)
print("Chapter:", chapter_number)
print("Estimated minutes:", estimated_minutes)
print("Available:", is_available)
print("Next chapter:", next_chapter)
```

Saída esperada:

```text
Course: Python Study Guide
Chapter: 4
Estimated minutes: 60.0
Available: True
Next chapter: None
```

Os rótulos deixam visível a função de cada valor. A notação do código-fonte revela a categoria do tipo antes mesmo de o próximo capítulo apresentar a inspeção direta.

## 22. Exercício

Crie `chapter_status.py` utilizando exatamente estes nomes:

```python
guide_name
chapter_number
estimated_minutes
is_published
review_note
```

Armazene:

1. o texto `"Python Study Guide"` em `guide_name`;
2. o inteiro `4` em `chapter_number`;
3. o float `60.0` em `estimated_minutes`;
4. o booleano `True` em `is_published`;
5. `None` em `review_note`.

Imprima cada valor em uma linha identificada. Depois crie uma versão textual do número do capítulo chamada `chapter_number_text` e atribua `"4"` a ela.

Adicione estas duas linhas finais:

```python
print("Number result:", chapter_number + chapter_number)
print("Text result:", chapter_number_text + chapter_number_text)
```

Antes de executar o programa, preveja os dois resultados. Explique por que eles são diferentes.

## 23. Erros comuns

### Colocar aspas em todos os valores

```python
chapter_number = "4"
```

Isso armazena texto, não um inteiro. Use `4` quando o valor precisar se comportar como um número inteiro.

### Esquecer o ponto decimal quando um float é desejado

```python
estimated_hours = 2
```

Isso cria um inteiro. Escreva `2.0` quando o exemplo precisar especificamente de um valor float.

### Escrever estados lógicos como strings

```text
is_ready = "False"
```

A string `"False"` é texto. Use o valor booleano `False` para um estado lógico.

### Escrever dados ausentes como texto

```text
next_chapter = "None"
```

A string `"None"` não é o marcador de ausência. Use `None`.

### Usar a capitalização errada

```text
is_ready = TRUE
next_chapter = none
```

Escreva `True`, `False` e `None` exatamente como o Python os define.

### Confiar somente na aparência impressa

`print()` foi projetado para produzir uma saída legível. Tipos diferentes podem gerar textos visíveis semelhantes, portanto a saída sozinha nem sempre é suficiente para identificar o tipo de um valor.

O próximo capítulo apresenta a inspeção direta com `type()` e as verificações de relação com `isinstance()`.

## 24. Autoverificação

Você está pronto para o próximo capítulo quando conseguir responder:

- Qual é a relação entre um valor e um tipo?
- O que significa “embutido”?
- Qual tipo representa texto?
- Qual é a diferença entre `"42"`, `42` e `42.0`?
- Quais dois valores pertencem a `bool`?
- Por que `true` e `false` estão incorretos no Python?
- O que `None` normalmente representa?
- `"None"` é o mesmo valor que `None`?
- Qual tipo `input()` retorna?
- Por que o mesmo símbolo `+` pode se comportar de forma diferente para strings e números?
- Este capítulo lista todos os tipos embutidos do Python?

## 25. Resumo para consulta rápida

| Categoria do valor | Exemplo no código-fonte | Tipo embutido |
|---|---|---|
| Texto | `"Python"` | `str` |
| Número inteiro | `42` | `int` |
| Número com ponto decimal | `42.0` | `float` |
| Valor lógico | `True` ou `False` | `bool` |
| Marcador de ausência | `None` | `NoneType` |

Lembretes adicionais:

- aspas criam texto;
- um ponto decimal normalmente indica um literal float;
- `True`, `False` e `None` diferenciam maiúsculas de minúsculas;
- a aparência impressa pode não revelar o tipo;
- `input()` retorna `str`;
- a conversão de tipos é deliberada e pertence a um capítulo posterior.

## 26. Execute os exemplos do repositório

Na raiz do repositório:

```bash
python fundamentals/04-built-in-data-types/examples/value_catalog.py
python fundamentals/04-built-in-data-types/examples/same_looking_values.py
```

Os dois exemplos estão aprovados para execução sem supervisão.

## 27. Execute as verificações do repositório

Na raiz do repositório:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## Referências oficiais

- [Modelo de dados do Python — Objetos, valores e tipos](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [Biblioteca padrão do Python — Tipos embutidos](https://docs.python.org/3/library/stdtypes.html)
- [Referência da linguagem Python — Literais](https://docs.python.org/3/reference/lexical_analysis.html#literals)
- [Biblioteca padrão do Python — Constantes embutidas](https://docs.python.org/3/library/constants.html)

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Variáveis e nomes](../03-variables-and-naming/README.pt-BR.md)
