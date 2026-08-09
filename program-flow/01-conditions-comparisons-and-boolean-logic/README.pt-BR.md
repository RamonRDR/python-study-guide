<div align="center">

# Condições, Comparações e Lógica Booleana

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Fluxo do Programa](../README.pt-BR.md) · [← Fase anterior: Escolhendo a Coleção Certa](../../collections/06-choosing-the-right-collection/README.pt-BR.md)

Condições são as perguntas que um programa consegue avaliar antes de decidir o que deve acontecer em seguida.

Você já encontrou partes dessa ideia nas fases anteriores. Comparações como `score >= 70` produzem valores booleanos, testes de pertencimento como `"lists" in topics` respondem se um valor está presente e `bool()` mostra como o Python interpreta muitos valores como verdadeiros ou falsos.

Este capítulo conecta essas peças antes de introduzir `if`. O objetivo é entender as expressões que, mais adiante, controlarão decisões e loops.

**Tempo estimado de estudo:** 100–125 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deve conseguir:

- usar comparações de valor como `==`, `!=`, `<`, `<=`, `>` e `>=`;
- diferenciar atribuição com `=` de comparação com `==`;
- ler e escrever comparações encadeadas;
- usar `in` e `not in` com strings e coleções;
- explicar por que o pertencimento em dicionários testa chaves por padrão;
- diferenciar igualdade de valor de identidade de objeto;
- usar `is None` e `is not None` adequadamente;
- reconhecer valores falsos comuns e usar `bool()` para inspecionar valores de verdade;
- combinar condições com `and`, `or` e `not`;
- explicar avaliação de curto-circuito;
- lembrar que `and` e `or` podem retornar operandos em vez de `True` ou `False`;
- usar parênteses quando eles deixarem expressões booleanas mais fáceis de ler;
- preparar condições claras para o próximo capítulo sobre `if`, `elif` e `else`.

## 1. Uma condição é uma expressão interpretada quanto ao valor de verdade

Uma **condição** é uma expressão cujo resultado o Python consegue interpretar como verdadeiro ou falso.

Uma comparação é uma fonte comum de condição:

```python
score = 82

print(score >= 70)
```

```text
True
```

A expressão `score >= 70` faz uma pergunta sobre dois valores. O resultado é um valor booleano.

No próximo capítulo, condições controlarão qual bloco de código é executado. Por enquanto, mantenha a condição separada da própria estrutura de decisão.

## 2. Comparações produzem valores de verdade

O Python fornece seis operadores familiares de comparação de valores:

| Operador | Significado |
|---|---|
| `==` | igual |
| `!=` | diferente |
| `<` | menor que |
| `<=` | menor que ou igual |
| `>` | maior que |
| `>=` | maior que ou igual |

Exemplo:

```python
score = 82

print(score == 82)
print(score != 90)
print(score < 100)
print(score >= 70)
```

```text
True
True
True
True
```

Comparações normalmente produzem `True` ou `False`.

## 3. `=` atribui; `==` compara

Esses símbolos parecem semelhantes, mas realizam trabalhos diferentes.

A atribuição armazena ou associa novamente um valor:

```python
score = 82
```

A comparação pergunta se dois valores são iguais:

```python
print(score == 82)
```

```text
True
```

Um hábito útil de leitura é:

- `=` → **armazenar ou associar**
- `==` → **perguntar se os valores são iguais**

Essa diferença se torna especialmente importante quando condições aparecem dentro de estruturas de fluxo do programa.

## 4. Igualdade e ordenação são perguntas diferentes

Igualdade pergunta se os valores são considerados iguais.

Ordenação pergunta se um valor vem antes, depois, abaixo ou acima de outro conforme as regras suportadas por esses tipos.

Para números:

```python
print(10 == 10.0)
print(10 < 12.5)
```

```text
True
True
```

Os tipos numéricos do Python frequentemente podem ser comparados entre tipos numéricos compatíveis.

Isso **não** significa que qualquer par de tipos suporte ordenação.

Por exemplo:

```python
print(10 < "12")
```

gera `TypeError` porque o Python não define essa ordenação entre `int` e `str`.

```text
TypeError
```

O traceback exato contém informações de arquivo e linha. O ponto importante aqui é que comparações de ordenação exigem tipos cujas regras de comparação suportem aquela operação.

## 5. Comparações encadeadas expressam intervalos com clareza

O Python permite encadear comparações:

```python
age = 28

print(18 <= age < 65)
```

```text
True
```

Para este exemplo, a ideia equivale a fazer as duas perguntas:

```python
age = 28

print(age >= 18 and age < 65)
```

```text
True
```

A forma encadeada costuma ser mais fácil de ler para intervalos.

O Python avalia cada expressão em uma cadeia de comparações no máximo uma vez. Esse detalhe se torna mais relevante quando as expressões ficam complexas; para iniciantes, o principal é entender que comparações encadeadas são um recurso real do Python, não um atalho produzido por reescrever o texto do código.

## 6. Cadeias de comparação não implicam todas as comparações possíveis

Considere:

```python
value = 5

print(1 < value < 10)
```

```text
True
```

Isso significa:

- `1 < value`
- e `value < 10`

Não cria nenhuma comparação adicional entre `1` e `10`.

Mantenha a cadeia focada na relação que você realmente deseja expressar.

## 7. Testes de pertencimento perguntam se um valor está presente

Você já usou `in` ao estudar coleções.

```python
topics = ["strings", "numbers", "collections"]

print("collections" in topics)
print("loops" in topics)
```

```text
True
False
```

`in` pergunta se há pertencimento.

`not in` pergunta o contrário:

```python
topics = ["strings", "numbers", "collections"]

print("loops" not in topics)
```

```text
True
```

As duas formas produzem resultados booleanos.

## 8. Pertencimento também funciona com strings

Para strings, o teste de pertencimento verifica se uma string ocorre dentro de outra:

```python
message = "study python"

print("python" in message)
print("java" not in message)
```

```text
True
True
```

Embora strings e listas sejam tipos diferentes, ambos oferecem testes de pertencimento com significado claro.

## 9. Pertencimento em dicionários verifica chaves por padrão

Um dicionário representa relações entre chave e valor.

```python
profile = {"name": "Ava", "level": "beginner"}

print("name" in profile)
print("Ava" in profile)
```

```text
True
False
```

`"name" in profile` verifica se `"name"` é uma chave.

Ele não procura nos valores do dicionário por padrão.

Se a sua pergunta for especificamente sobre os valores, deixe essa intenção visível:

```python
profile = {"name": "Ava", "level": "beginner"}

print("Ava" in profile.values())
```

```text
True
```

## 10. Igualdade e identidade não são o mesmo conceito

`==` compara valores conforme as regras de igualdade do tipo.

`is` pergunta se duas referências apontam para o **mesmo objeto**.

Essas perguntas podem produzir respostas diferentes:

```python
first = [1, 2]
second = [1, 2]

print(first == second)
print(first is second)
```

```text
True
False
```

As listas contêm valores iguais, mas são objetos de lista separados.

Para comparação comum de valores, use `==` e `!=`.

Não substitua igualdade de valor por `is` apenas porque um exemplo pequeno parece funcionar.

## 11. Use comparação de identidade para `None`

`None` é um valor singleton usado para representar a ausência de um valor normal em muitas APIs e programas Python.

A PEP 8 recomenda comparação de identidade para singletons como `None`:

```python
result = None

print(result is None)
print(result is not None)
```

```text
True
False
```

Use:

```python
result is None
```

em vez de:

```python
result == None
```

A segunda expressão pode produzir um resultado booleano, mas `is None` comunica a verificação de identidade pretendida e segue a orientação de estilo padrão.

## 12. Teste de valor de verdade vai além de `True` e `False` literais

O Python consegue interpretar muitos objetos como verdadeiros ou falsos em um contexto booleano.

Entre os principais valores embutidos considerados falsos estão:

- `False`;
- `None`;
- zero numérico, como `0` e `0.0`;
- strings vazias;
- listas e tuplas vazias;
- dicionários vazios;
- conjuntos vazios.

Exemplo:

```python
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(None))
```

```text
False
False
False
False
False
False
```

Esse comportamento é chamado de **teste de valor de verdade**.

## 13. Coleções não vazias normalmente são truthy

Compare valores vazios e não vazios:

```python
print(bool("Python"))
print(bool(["lists"]))
print(bool({"topic": "python"}))
print(bool({"python"}))
```

```text
True
True
True
True
```

Para as coleções embutidas apresentadas até aqui, o estado vazio ou não vazio é uma distinção booleana útil.

Não confunda truthiness com uma afirmação sobre o significado do conteúdo. Uma lista não vazia é truthy mesmo que seu único item seja `False`:

```python
print(bool([False]))
```

```text
True
```

A própria lista não está vazia.

## 14. `bool()` torna explícita a interpretação de verdade

`bool()` converte um valor em `True` ou `False` conforme suas regras de valor de verdade.

```python
value = []

print(bool(value))
print(type(bool(value)))
```

```text
False
<class 'bool'>
```

Isso é útil durante o aprendizado e a depuração.

Mais adiante, condições normalmente poderão usar o valor diretamente sem envolver toda expressão em `bool()`.

## 15. `and` exige que o lado esquerdo seja truthy antes de avaliar o lado direito

Com operandos booleanos:

```python
has_ticket = True
venue_open = True

print(has_ticket and venue_open)
```

```text
True
```

Se qualquer requisito for falso, o resultado lógico combinado será falso:

```python
has_ticket = True
venue_open = False

print(has_ticket and venue_open)
```

```text
False
```

Leia `and` como a exigência de que ambas as condições sejam satisfeitas quando os operandos são condições booleanas.

## 16. `or` aceita a primeira alternativa truthy

Com operandos booleanos:

```python
has_permission = False
is_admin = True

print(has_permission or is_admin)
```

```text
True
```

Se pelo menos uma condição booleana for verdadeira, a expressão será verdadeira.

Isso torna `or` útil para alternativas.

## 17. `not` inverte a interpretação de verdade e retorna um booleano

`not` produz um resultado booleano real:

```python
is_blocked = False

print(not is_blocked)
print(not "")
print(not "Python")
```

```text
True
True
False
```

`not` pergunta pelo valor de verdade oposto.

Ele sempre produz `True` ou `False`.

## 18. `and` e `or` nem sempre retornam `bool`

Este é um dos detalhes mais importantes deste capítulo.

`and` e `or` usam teste de valor de verdade, mas retornam um de seus operandos.

Exemplo com `or`:

```python
display_name = "" or "Guest"

print(display_name)
print(type(display_name))
```

```text
Guest
<class 'str'>
```

A string vazia é falsy, então `or` avalia e retorna `"Guest"`.

Exemplo com `and`:

```python
result = "Python" and 3

print(result)
print(type(result))
```

```text
3
<class 'int'>
```

O primeiro operando é truthy, então `and` avalia e retorna o segundo operando.

Quando os dois operandos são condições booleanas reais, o resultado frequentemente se parece com um `True` ou `False` comum. Não transforme essa aparência em uma regra de que `and` e `or` sempre retornam `bool`.

## 19. Operadores booleanos usam curto-circuito

O Python nem sempre avalia todos os operandos.

Para `and`:

- se o operando esquerdo for falsy, esse valor é retornado e o operando direito não é avaliado;
- caso contrário, o operando direito é avaliado e retornado.

Para `or`:

- se o operando esquerdo for truthy, esse valor é retornado e o operando direito não é avaliado;
- caso contrário, o operando direito é avaliado e retornado.

Isso é chamado de **avaliação de curto-circuito**.

Um pequeno exemplo mostra por que isso importa:

```python
denominator = 0

safe_check = denominator != 0 and 10 / denominator > 2

print(safe_check)
```

```text
False
```

`denominator != 0` é `False`, então o Python não avalia `10 / denominator > 2`. A expressão de divisão por zero nunca é alcançada.

O curto-circuito pode tornar condições mais seguras e claras, mas não esconda efeitos colaterais importantes dentro de expressões booleanas apenas para explorar a ordem de avaliação.

## 20. Combine comparações em expressões booleanas com significado

Operadores booleanos se tornam especialmente úteis quando seus operandos são comparações.

```python
score = 82
is_active = True

eligible = score >= 70 and is_active

print(eligible)
```

```text
True
```

Outro exemplo:

```python
temperature = 28

needs_attention = temperature < 5 or temperature > 35

print(needs_attention)
```

```text
False
```

Procure nomear variáveis de acordo com a pergunta respondida pela expressão.

## 21. Precedência afeta como expressões booleanas são agrupadas

Entre os operadores deste capítulo:

1. comparações como `>=`, `==`, `in` e `is` se ligam mais fortemente do que operadores booleanos;
2. `not` se liga mais fortemente do que `and`;
3. `and` se liga mais fortemente do que `or`.

Portanto:

```python
print(True or False and False)
```

```text
True
```

O Python agrupa a parte com `and` antes da parte com `or`.

Mesmo conhecendo as regras de precedência, parênteses podem deixar a intenção mais visível:

```python
print(True or (False and False))
```

```text
True
```

Prefira legibilidade a demonstrar que você memorizou a tabela de precedência.

## 22. Parênteses podem documentar os grupos pretendidos

Considere:

```python
score = 82
has_project = False
has_certificate = True

eligible = score >= 70 and (has_project or has_certificate)

print(eligible)
```

```text
True
```

Os parênteses deixam as alternativas visualmente explícitas.

Eles não são decorativos quando ajudam uma pessoa a entender os grupos lógicos.

## 23. Não substitua lógica booleana por operadores bit a bit

O Python também possui operadores como `&`, `|` e `^`.

Eles são principalmente **operadores bit a bit** para operações em bits de inteiros e podem ter significados especializados para outros tipos.

Para condições lógicas comuns, use:

- `and`;
- `or`;
- `not`.

Não aprenda `&` e `|` como grafias alternativas para `and` e `or`.

## 24. Exemplo prático: resultados de comparações

O arquivo [`examples/comparison_results.py`](examples/comparison_results.py) contém:

```python
age = 28
minimum_age = 18
maximum_age = 65
topics = ["strings", "numbers", "collections"]
profile = {"name": "Ava", "level": "beginner"}

print("At least 18:", age >= minimum_age)
print("Under 65:", age < maximum_age)
print("Inside interval:", minimum_age <= age < maximum_age)
print("Collections available:", "collections" in topics)
print("Name key exists:", "name" in profile)
print("Email key missing:", "email" not in profile)
```

Saída esperada:

```text
At least 18: True
Under 65: True
Inside interval: True
Collections available: True
Name key exists: True
Email key missing: True
```

Este exemplo combina comparação de valores, intervalo encadeado, pertencimento em coleção e pertencimento por chave em dicionário sem introduzir estruturas de controle ainda.

## 25. Exemplo prático: lógica booleana e curto-circuito

O arquivo [`examples/boolean_logic.py`](examples/boolean_logic.py) contém:

```python
has_ticket = True
venue_open = True
is_blocked = False
denominator = 0

can_enter = has_ticket and venue_open and not is_blocked
needs_attention = not has_ticket or is_blocked
safe_ratio_check = denominator != 0 and 10 / denominator > 2
display_name = "" or "Guest"

print("Can enter:", can_enter)
print("Needs attention:", needs_attention)
print("Safe ratio check:", safe_ratio_check)
print("Display name:", display_name)
```

Saída esperada:

```text
Can enter: True
Needs attention: False
Safe ratio check: False
Display name: Guest
```

Observe que o mesmo exemplo contém tanto condições booleanas quanto o comportamento de `or` de retornar um operando.

## 26. Exemplo prático: inspecionando valores de verdade

O arquivo [`examples/truth_values.py`](examples/truth_values.py) contém:

```python
print("Empty string:", bool(""))
print("Text:", bool("Python"))
print("Zero:", bool(0))
print("Nonzero:", bool(-3))
print("None:", bool(None))
print("Empty list:", bool([]))
print("Filled list:", bool(["python"]))
print("Empty dictionary:", bool({}))
print("Filled dictionary:", bool({"topic": "python"}))
print("Empty set:", bool(set()))
print("Filled set:", bool({"python"}))
```

Saída esperada:

```text
Empty string: False
Text: True
Zero: False
Nonzero: True
None: False
Empty list: False
Filled list: True
Empty dictionary: False
Filled dictionary: True
Empty set: False
Filled set: True
```

Os valores foram escolhidos intencionalmente entre conceitos já apresentados nas fases anteriores.

## 27. Erros comuns

### Erro 1: confundir atribuição e igualdade

```python
score = 82
print(score == 82)
```

`=` realiza atribuição. `==` realiza comparação de igualdade.

### Erro 2: usar `is` para igualdade comum de valores

Evite tratar isto como substituto de comparação de valor:

```python
first = [1, 2]
second = [1, 2]

print(first is second)
```

```text
False
```

Use `==` quando a pergunta for se os valores são considerados iguais.

### Erro 3: esperar que `and` e `or` sempre retornem valores booleanos

```python
print("" or "fallback")
print("Python" and 5)
```

```text
fallback
5
```

Eles retornam operandos conforme o teste de valor de verdade.

### Erro 4: presumir que o texto `"False"` é falsy

```python
print(bool("False"))
```

```text
True
```

A string não está vazia.

### Erro 5: esquecer que pertencimento em dicionários verifica chaves

```python
profile = {"name": "Ava"}

print("name" in profile)
print("Ava" in profile)
```

```text
True
False
```

### Erro 6: fazer a precedência exigir trabalho mental desnecessário

Isto é válido:

```python
ready = True or False and False
```

Mas, quando condições reais ficarem maiores, use parênteses se eles facilitarem reconhecer os grupos pretendidos.

### Erro 7: comparar valores incompatíveis com operadores de ordenação

```python
print(10 < "12")
```

Isso gera `TypeError`.

Converta ou modele os dados adequadamente em vez de esperar que qualquer par de tipos possua uma relação de ordenação.

## 28. Exercício: monte um conjunto de condições de prontidão para estudo

Crie um arquivo chamado `study_readiness.py`.

Comece com:

```python
completed_topics = ["strings", "numbers", "collections"]
score = 82
is_active = True
optional_note = ""
```

Sem usar `if`, `elif`, `else`, `for` ou `while`, crie e imprima expressões que respondam a estas perguntas:

1. `score` é pelo menos `70`?
2. `score` está dentro do intervalo de `70` até `100`, inclusive?
3. `"collections"` está presente em `completed_topics`?
4. `"loops"` está ausente de `completed_topics`?
5. Tanto o requisito de pontuação mínima quanto `is_active` são verdadeiros?
6. `optional_note` é truthy?
7. Qual valor `optional_note or "No note"` produz?

Uma implementação possível é:

```python
completed_topics = ["strings", "numbers", "collections"]
score = 82
is_active = True
optional_note = ""

minimum_reached = score >= 70
inside_expected_range = 70 <= score <= 100
has_collections = "collections" in completed_topics
loops_not_started = "loops" not in completed_topics
ready = minimum_reached and is_active
has_note = bool(optional_note)
display_note = optional_note or "No note"

print("Minimum reached:", minimum_reached)
print("Inside expected range:", inside_expected_range)
print("Has collections:", has_collections)
print("Loops not started:", loops_not_started)
print("Ready:", ready)
print("Has note:", has_note)
print("Display note:", display_note)
```

Saída esperada:

```text
Minimum reached: True
Inside expected range: True
Has collections: True
Loops not started: True
Ready: True
Has note: False
Display note: No note
```

O exercício para intencionalmente antes de `if`. O objetivo é primeiro tornar a própria condição confiável.

## 29. Checklist de revisão

Antes de avançar, certifique-se de conseguir explicar:

- [ ] a diferença entre `=` e `==`;
- [ ] o que cada um dos seis operadores de comparação de valor pergunta;
- [ ] por que `18 <= age < 65` é útil;
- [ ] o que `in` e `not in` testam;
- [ ] o que o pertencimento em dicionários verifica por padrão;
- [ ] a diferença entre `==` e `is`;
- [ ] por que `is None` é preferido;
- [ ] quais valores embutidos comuns são falsy;
- [ ] o que `bool()` faz;
- [ ] como `and`, `or` e `not` se comportam;
- [ ] por que `and` e `or` podem retornar operandos não booleanos;
- [ ] o que significa avaliação de curto-circuito;
- [ ] por que parênteses podem melhorar a legibilidade de condições.

## 30. Consulta rápida

| Necessidade | Forma típica |
|---|---|
| Valores iguais | `a == b` |
| Valores diferentes | `a != b` |
| Ordenação | `a < b`, `a <= b`, `a > b`, `a >= b` |
| Intervalo | `lower <= value <= upper` |
| Pertencimento | `item in collection` |
| Ausência | `item not in collection` |
| Identidade com `None` | `value is None` |
| Identidade negada com `None` | `value is not None` |
| Exigir as duas condições | `condition_a and condition_b` |
| Aceitar uma das condições | `condition_a or condition_b` |
| Inverter valor de verdade | `not value` |
| Inspecionar valor de verdade explicitamente | `bool(value)` |

Lembre:

```text
comparison -> truth value -> Boolean combination -> future decision
```

Este capítulo construiu o lado esquerdo dessa ponte. O próximo capítulo adiciona a estrutura de decisão.

## Próximo passo

O próximo capítulo é **`if`, `elif` e `else`**.

Nele, essas condições deixam de ser valores que você apenas imprime e começam a controlar qual código o Python executa.

## Referências oficiais

- [Tipos embutidos do Python 3.13: teste de valor de verdade e operações booleanas](https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing)
- [Referência da linguagem Python 3.13: comparações](https://docs.python.org/3.13/reference/expressions.html#comparisons)
- [PEP 8: recomendações de programação](https://peps.python.org/pep-0008/#programming-recommendations)
