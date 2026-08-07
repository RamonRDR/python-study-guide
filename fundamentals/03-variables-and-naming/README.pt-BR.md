<div align="center">

# Variáveis e Nomes

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: `print()` e `input()`](../02-print-and-input/README.pt-BR.md)

Os programas se tornam mais úteis quando conseguem manter informações sob nomes compreensíveis e reutilizá-las depois. A atribuição em Python conecta um nome a um valor, permitindo que instruções posteriores leiam esse valor sem repeti-lo.

Este capítulo apresenta variáveis, atribuição, reatribuição, identificadores válidos e convenções práticas de nomenclatura. Os tipos de dados em detalhes, as comparações e o escopo ficam deliberadamente para capítulos posteriores.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir os Capítulos 01 e 02 |
| Tempo estimado de estudo | 50 a 70 minutos |
| Conceitos principais | Variável, nome, atribuição, identificador, reatribuição, palavra-chave, `snake_case` |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- atribuir um valor a um nome com `=`;
- ler um valor armazenado usando seu nome;
- explicar que o lado direito é avaliado antes da atribuição;
- reatribuir um novo valor a um nome;
- reconhecer identificadores válidos e inválidos;
- explicar por que palavras-chave do Python não podem ser nomes de variáveis;
- escolher nomes claros em `snake_case`;
- evitar ocultar funções embutidas como `print` e `input`;
- diferenciar regras de sintaxe do Python de convenções de nomenclatura do projeto.

## 1. Por que os programas armazenam valores

Sem nomes, um programa precisa repetir o mesmo valor sempre que ele for necessário:

```python
print("Python Study Guide")
print("Current course:", "Python Study Guide")
```

Um nome permite armazenar o valor uma vez e reutilizá-lo:

```python
course_name = "Python Study Guide"

print(course_name)
print("Current course:", course_name)
```

Isso reduz repetições e facilita alterações posteriores.

## 2. A atribuição usa `=`

Uma instrução básica de atribuição possui um alvo à esquerda e uma expressão que produz valor à direita:

```python
learner_name = "Ada"
```

Leia assim:

> Atribua o texto `"Ada"` ao nome `learner_name`.

Para uma pessoa iniciante, é adequado chamar `learner_name` de variável. De forma mais precisa, o Python vincula o nome `learner_name` ao valor resultante.

O símbolo `=` realiza uma atribuição. Ele não pergunta se dois valores são iguais. As comparações com `==` pertencem a um capítulo posterior.

## 3. Use o nome para ler o valor

Após a atribuição, usar o nome recupera o valor atualmente associado a ele:

```python
learner_name = "Ada"

print(learner_name)
print("Learner:", learner_name)
```

Saída esperada:

```text
Ada
Learner: Ada
```

As aspas criam um texto literal. Um nome sem aspas pede ao Python o valor armazenado.

## 4. O lado direito é avaliado primeiro

O Python avalia a expressão à direita antes de atribuir o resultado ao nome à esquerda:

```python
topic = input("Topic: ")
```

A ordem é:

1. `input("Topic: ")` exibe o prompt e retorna um texto;
2. o texto retornado é atribuído a `topic`.

O mesmo padrão funciona com outras expressões:

```python
full_title = "Python" + " Study Guide"
print(full_title)
```

A expressão cria o texto final antes que `full_title` o receba.

## 5. A reatribuição atualiza o que um nome referencia

Um nome pode receber um novo valor depois:

```python
current_topic = "Output and input"
print("Before:", current_topic)

current_topic = "Variables and naming"
print("After:", current_topic)
```

Saída esperada:

```text
Before: Output and input
After: Variables and naming
```

A segunda atribuição substitui o valor recuperado por meio de `current_topic` daquele ponto em diante.

O Python não exige uma declaração especial antes da primeira atribuição.

## 6. Os nomes diferenciam maiúsculas de minúsculas

O Python trata letras maiúsculas e minúsculas como diferentes:

```python
topic = "Variables"
Topic = "Naming"

print(topic)
print(Topic)
```

`topic` e `Topic` são dois nomes diferentes. Evite nomes que diferem apenas pelas maiúsculas, pois são fáceis de confundir.

## 7. Uma regra segura para identificadores iniciantes

O nome de uma variável é um **identificador**. Para código iniciante portátil com identificadores em inglês, siga esta regra segura:

- comece com uma letra inglesa ou sublinhado;
- continue com letras inglesas, algarismos ou sublinhados;
- não use espaços nem hífens;
- não comece com um algarismo.

Exemplos válidos:

```python
name = "Ada"
learner_name = "Ada"
topic_2 = "Variables"
_private_note = "Draft"
```

Exemplos inválidos:

```text
2topic = "Variables"
learner-name = "Ada"
learner name = "Ada"
```

O Python aceita uma variedade maior de letras Unicode em identificadores. Mesmo assim, este projeto usa identificadores descritivos em inglês como convenção do repositório.

## 8. Palavras-chave não podem ser nomes de variáveis

Palavras-chave possuem significados gramaticais reservados no Python. Elas não podem ser reutilizadas como identificadores comuns:

```text
class = "beginner"
for = "practice"
```

As duas linhas são inválidas porque `class` e `for` são palavras-chave.

Você não precisa memorizar todas imediatamente. Os editores normalmente as destacam, e o módulo `keyword` da biblioteca padrão pode verificá-las posteriormente.

## 9. Prefira `snake_case`

A PEP 8 recomenda palavras minúsculas separadas por sublinhados para nomes de variáveis e funções:

```python
learner_name = "Ada"
study_topic = "Variables and naming"
practice_minutes = "30"
```

Esse estilo é chamado de `snake_case`.

Compare:

```text
learnername
LearnerName
learner-name
learner_name
```

Para variáveis comuns neste projeto, `learner_name` é a forma preferida.

## 10. Escolha nomes que revelem significado

Um nome deve ajudar a pessoa leitora a compreender a função do valor:

```python
x = "45"
```

O nome `x` quase não fornece contexto.

```python
practice_minutes = "45"
```

O nome mais claro revela tanto a finalidade quanto a unidade.

Perguntas úteis ao nomear uma variável:

- Qual informação este valor representa?
- Por que o programa usará esse valor?
- Uma unidade como minutos, quilogramas ou reais é importante?
- O nome ainda fará sentido várias linhas depois?

## 11. Evite abreviações sem explicação

Nomes curtos economizam teclas, mas podem custar compreensão:

```python
nm = "Ada"
tp = "Variables"
mins = "30"
```

Prefira nomes completos e legíveis:

```python
learner_name = "Ada"
study_topic = "Variables"
practice_minutes = "30"
```

Abreviações amplamente compreendidas podem ser adequadas, mas inventar abreviações locais normalmente cria um quebra-cabeça de decodificação.

## 12. Evite ocultar funções embutidas

O Python permite reatribuir alguns nomes de funções embutidas, mas isso oculta a função original sob aquele nome:

```python
print = "not a function anymore"
```

Após essa atribuição, esta chamada falha porque `print` agora referencia um texto:

```text
print("Hello")
```

Evite nomes de variáveis como:

- `print`;
- `input`;
- `str`;
- `int`;
- `list`;
- `sum`.

Nem todos são palavras-chave, mas preservar os nomes embutidos evita falhas confusas.

## 13. Identificadores em inglês são uma convenção do projeto

O Python aceita identificadores de diversos sistemas de escrita. O Python Study Guide usa identificadores em inglês no código compartilhado:

```python
learner_name = "Ada"
study_goal = "Build useful programs"
```

Essa é uma convenção do repositório, não uma exigência universal do Python. As explicações permanecem multilíngues, enquanto o código compartilhado fica idêntico entre as traduções.

## 14. Constantes usam uma convenção em maiúsculas

Um valor que se pretende manter inalterado durante o programa costuma ser escrito com palavras maiúsculas:

```python
COURSE_NAME = "Python Study Guide"
DEFAULT_TOPIC = "Fundamentals"
```

Esse estilo comunica intenção às pessoas leitoras. O Python não impede a reatribuição, portanto a escrita em maiúsculas é uma convenção, não uma garantia.

## 15. Armazene e reutilize entradas

O Capítulo 02 usou a atribuição como uma ponte. Agora você pode descrever as partes com mais precisão:

```python
learner_name = input("Name: ")
study_topic = input("Topic: ")

print("Learner:", learner_name)
print("Topic:", study_topic)
```

Cada prompt retorna um texto. Cada atribuição oferece um nome significativo a esse texto, e cada `print()` posterior lê o valor armazenado.

## 16. Um nome não é igual a um texto com a mesma grafia

Compare estas chamadas:

```python
learner_name = "Ada"

print(learner_name)
print("learner_name")
```

Saída esperada:

```text
Ada
learner_name
```

A primeira chamada lê a variável. A segunda imprime um texto literal porque os caracteres estão dentro das aspas.

## 17. Usar um nome antes da atribuição causa erro

O Python precisa encontrar uma atribuição antes que o nome seja lido no fluxo atual do programa:

```text
print(current_topic)
current_topic = "Variables"
```

Executar esse exemplo no nível principal gera `NameError`, pois `current_topic` ainda não foi atribuído quando a primeira linha é executada.

Mova a atribuição para antes da leitura:

```python
current_topic = "Variables"
print(current_topic)
```

## 18. Exemplos do repositório

| Arquivo | Finalidade | Execução automática |
|---|---|---|
| [`variable_basics.py`](examples/variable_basics.py) | Demonstra atribuição, reutilização, nomes claros e reatribuição | Sim |
| [`learning_profile.py`](examples/learning_profile.py) | Coleta e exibe um pequeno perfil de aprendizagem | Não; aguarda entrada no terminal |

O exemplo interativo é excluído deliberadamente do manifesto de exemplos executados sem supervisão.

## 19. Exemplo prático: perfil de aprendizagem

Crie `learning_profile.py`:

```python
learner_name = input("Name: ")
current_topic = input("Current topic: ")
study_goal = input("Study goal: ")

print()
print("LEARNING PROFILE")
print("Name:", learner_name)
print("Topic:", current_topic)
print("Goal:", study_goal)
```

Uma possível sessão é:

```text
Name: Ada
Current topic: Variables
Study goal: Build useful programs

LEARNING PROFILE
Name: Ada
Topic: Variables
Goal: Build useful programs
```

Os nomes explicam o que cada resposta representa e facilitam a montagem da saída final.

## 20. Exercício

Crie `study_session.py` que:

1. armazene o nome do guia em `GUIDE_NAME`;
2. pergunte o nome da pessoa estudante;
3. pergunte o tema;
4. pergunte o tempo de prática planejado como texto;
5. imprima uma linha em branco;
6. imprima um resumo identificado da sessão;
7. reatribua o tema para `"Review completed"`;
8. imprima o tema atualizado.

Use exatamente estes nomes:

```python
GUIDE_NAME
learner_name
study_topic
practice_minutes
```

Execute o programa duas vezes com respostas diferentes. Depois, substitua um nome claro por um nome vago como `x`, leia o programa e restaure o nome mais claro.

## 21. Erros comuns

### Ler antes da atribuição

```text
print(city)
city = "London"
```

Atribua primeiro e leia depois.

### Colocar o nome da variável entre aspas

```python
city = "London"
print("city")
```

Isso imprime `city`, e não `London`.

### Começar um nome com algarismo

```text
1st_topic = "Variables"
```

Use um identificador válido como `first_topic`.

### Usar espaços ou hífens

```text
learner name = "Ada"
learner-name = "Ada"
```

Use `learner_name`.

### Usar uma palavra-chave

```text
class = "beginner"
```

Escolha uma alternativa descritiva como `course_level`.

### Reutilizar um nome embutido

```text
input = "stored text"
```

Escolha um nome que descreva o valor, como `user_response`.

### Usar capitalização incompatível

```text
study_topic = "Variables"
print(Study_Topic)
```

Os nomes diferenciam maiúsculas de minúsculas.

## 22. Autoverificação

Você está pronto para o próximo capítulo quando conseguir responder:

- O que `=` faz?
- Qual lado de uma atribuição é avaliado primeiro?
- O que acontece durante uma reatribuição?
- Por que `topic` e `Topic` são diferentes?
- Quais caracteres são seguros em um identificador inglês?
- Por que `class` não pode ser nome de variável?
- Como é a aparência de `snake_case`?
- Por que uma variável não deve se chamar `print`?
- A escrita de constantes em maiúsculas é imposta pelo Python?
- Qual é a diferença entre `print(name)` e `print("name")`?

## 23. Resumo para consulta rápida

| Objetivo | Exemplo |
|---|---|
| Atribuir um valor | `topic = "Variables"` |
| Ler um valor | `print(topic)` |
| Reatribuir um nome | `topic = "Naming"` |
| Estilo claro de variável | `practice_minutes` |
| Convenção de constante | `COURSE_NAME` |
| Armazenar entrada | `name = input("Name: ")` |
| Texto literal | `print("name")` |
| Valor armazenado | `print(name)` |
| Evitar ocultar nomes embutidos | Não atribua a `print` nem `input` |
| Sensibilidade a maiúsculas | `name` e `Name` são diferentes |

## 24. Execute os exemplos do repositório

Na raiz do repositório, execute o exemplo automático:

```bash
python fundamentals/03-variables-and-naming/examples/variable_basics.py
```

Execute o exemplo interativo e responda aos prompts:

```bash
python fundamentals/03-variables-and-naming/examples/learning_profile.py
```

## 25. Execute as verificações do repositório

Na raiz do repositório:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

O executor de exemplos aprovados executa `variable_basics.py`, mas não executa `learning_profile.py`, pois verificações sem supervisão não devem aguardar entrada pelo teclado.

## Referências oficiais

- [Referência da linguagem Python — Instruções de atribuição](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)
- [Referência da linguagem Python — Identificadores e palavras-chave](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
- [Biblioteca padrão do Python — Verificação de palavras-chave](https://docs.python.org/3/library/keyword.html)
- [PEP 8 — Convenções de nomenclatura](https://peps.python.org/pep-0008/#naming-conventions)

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: `print()` e `input()`](../02-print-and-input/README.pt-BR.md)
