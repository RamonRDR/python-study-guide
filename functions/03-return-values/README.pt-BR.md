<div align="center">

# Valores de Retorno

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Anterior: Parâmetros e Argumentos](../02-parameters-and-arguments/README.pt-BR.md)

O Capítulo 01 deu nome ao comportamento. O Capítulo 02 permitiu que o chamador enviasse valores para esse comportamento. Este capítulo completa a primeira viagem de ida e volta dos dados:

```text
caller → arguments → function → return value → caller
```

**Tempo estimado de estudo:** 75–100 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- escrever `return expression`;
- explicar que `return` encerra a chamada atual da função;
- armazenar e reutilizar valores retornados;
- diferenciar `print()` de `return`;
- usar valores retornados em expressões e condições;
- retornar valores normais do Python, tuplas e `None`;
- usar diferentes `return` em diferentes ramificações;
- diferenciar `return` de `break`;
- rastrear entrada, transformação, retorno e uso pelo chamador.

## 1. Envie um valor de volta com `return`

```python
def double(number):
    return number * 2


result = double(6)
print(result)
```

Saída:

```text
12
```

Rastreamento:

```text
6 binds to number
→ number * 2 becomes 12
→ return sends 12 back
→ double(6) becomes 12
→ result receives 12
```

Uma função não atribui diretamente a uma variável do chamador. Ela retorna um valor, e o chamador decide o que acontece em seguida.

## 2. Uma chamada que retorna valor é uma expressão

```python
def square(number):
    return number * number


answer = square(5)
print(answer)
```

Saída:

```text
25
```

Pense:

```text
square(5) → 25
```

Como a chamada produz um valor, ela pode participar de outra expressão:

```python
def double(number):
    return number * 2


final_score = double(7) + 3
print(final_score)
```

Saída:

```text
17
```

## 3. `print()` e `return` são diferentes

```python
def show_total(price, quantity):
    print(price * quantity)


def calculate_total(price, quantity):
    return price * quantity
```

A primeira função exibe um valor. A segunda envia um valor ao chamador.

```text
print(...) → display something
return ... → send a value to the caller
```

Um cálculo costuma ser mais reutilizável quando a função retorna o resultado e o chamador escolhe se vai imprimir, comparar, armazenar ou combinar esse valor.

## 4. Armazene ou use um valor retornado diretamente

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(8, 3)
print(total)
print(calculate_total(5, 4))
```

Saída:

```text
24
20
```

Uma variável intermediária com um bom nome costuma ser mais fácil de rastrear durante o aprendizado ou a depuração.

## 5. Funções podem retornar valores normais do Python

```python
def get_status():
    return "ready"


def is_passing(score):
    return score >= 60


def get_topics():
    return ["strings", "loops", "functions"]
```

Um valor de retorno pode ser uma string, número, booleano, coleção, tupla, `None` ou outro valor normal do Python.

## 6. Booleanos retornados funcionam com condições

```python
def is_passing(score):
    return score >= 60


if is_passing(75):
    print("Passed")
```

Saída:

```text
Passed
```

`is_passing(75)` é avaliada como `True`, então as regras de booleanos e `if` aprendidas anteriormente continuam valendo.

## 7. `return` encerra a chamada atual da função

```python
def get_message():
    return "Ready"
    print("This line never runs")
```

Quando `return` é executado:

```text
evaluate expression
→ obtain value
→ leave function
→ continue at caller
```

Um trabalho necessário não deve aparecer depois de um `return` incondicional no mesmo caminho.

## 8. Ramificações diferentes podem retornar valores diferentes

```python
def classify_score(score):
    if score >= 90:
        return "excellent"

    if score >= 60:
        return "passing"

    return "needs review"
```

Chamadas:

```python
print(classify_score(95))
print(classify_score(72))
print(classify_score(40))
```

Saída:

```text
excellent
passing
needs review
```

Apenas um `return` é executado em cada chamada. Quando um deles roda, aquela chamada termina.

## 9. Retornos antecipados podem simplificar um caso especial

```python
def describe_quantity(quantity):
    if quantity <= 0:
        return "invalid quantity"

    return "quantity accepted"
```

O caso especial sai primeiro, deixando o caminho normal fácil de ler. Use retornos antecipados quando eles melhorarem a clareza.

## 10. `return` dentro de um loop encerra a função inteira

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None
```

```python
print(find_first_even([3, 7, 8, 10]))
```

Saída:

```text
8
```

`return number` encerra a função, e não apenas o loop.

## 11. `return` e `break` abandonam limites diferentes

```text
break  → leave the current loop
return → leave the current function call
```

`break` pode continuar com instruções posteriores na mesma função. `return` devolve o controle ao chamador.

## 12. Chegar ao fim retorna `None`

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

Se a execução chega ao fim sem um `return` explícito, o resultado da chamada é `None`.

## 13. `return` sem expressão e `return None`

```python
def show_if_nonnegative(number):
    if number < 0:
        return

    print(number)
```

`return` sem expressão encerra imediatamente e produz `None`.

Todas estas formas podem produzir `None`:

```text
reach end of function → None
bare return           → None
return None           → None
```

Um `return None` explícito pode comunicar intenção:

```python
def find_positive(numbers):
    for number in numbers:
        if number > 0:
            return number

    return None
```

Aqui `None` significa que nenhum valor positivo foi encontrado.

## 14. `None` e `False` são valores diferentes

```python
def is_empty(items):
    return len(items) == 0
```

Essa função retorna um booleano. Uma função de busca pode retornar `None` para significar “não encontrado”.

Os dois valores são falsy em contextos booleanos, mas não significam a mesma coisa. Quando a distinção importar, teste deliberadamente.

## 15. A expressão de retorno é avaliada primeiro

```python
def calculate_area(width, height):
    return width * height
```

Para `calculate_area(4, 6)`:

```text
evaluate width * height
→ obtain 24
→ return 24
→ leave function
```

O valor resultante se torna o valor da expressão de chamada.

## 16. Retornando uma coleção

```python
def get_even_numbers(numbers):
    evens = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)

    return evens
```

```python
result = get_even_numbers([1, 2, 3, 4, 5, 6])
print(result)
```

Saída:

```text
[2, 4, 6]
```

Detalhes sobre propriedade de objetos e mutação ficam para depois.

## 17. Expressões separadas por vírgula em `return` produzem uma tupla

```python
def get_dimensions():
    return 1920, 1080


dimensions = get_dimensions()
print(dimensions)
```

Saída:

```text
(1920, 1080)
```

A função retorna uma única tupla. Como desempacotamento de tuplas já é conhecido:

```python
width, height = get_dimensions()

print(width)
print(height)
```

Saída:

```text
1920
1080
```

É uma única tupla retornada, e não dois valores de retorno independentes.

## 18. Erro comum: imprimir em vez de retornar

```python
def calculate_total(price, quantity):
    print(price * quantity)


total = calculate_total(8, 3)
print(total)
```

Saída:

```text
24
None
```

A função exibiu `24`, mas o resultado da chamada é `None`.

Correção:

```python
def calculate_total(price, quantity):
    return price * quantity
```

## 19. Erro comum: retornar cedo demais em um loop

Incorreto para contar todos os números pares:

```python
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

        return count
```

A função termina na primeira iteração.

Correto:

```python
def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count
```

A indentação muda o momento em que a função termina.

## 20. Erro comum: um `None` implícito acidental

```python
def get_level(score):
    if score >= 90:
        return "high"

    if score >= 60:
        return "medium"
```

Pontuações abaixo de `60` retornam `None` implicitamente.

Se toda pontuação deve ter uma categoria:

```python
def get_level(score):
    if score >= 90:
        return "high"

    if score >= 60:
        return "medium"

    return "low"
```

Projete deliberadamente os resultados possíveis.

## 21. Rastreie a viagem completa de ida e volta

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(12, 4)
```

```text
caller has 12 and 4
↓
arguments bind to price and quantity
↓
function evaluates price * quantity
↓
result is 48
↓
return sends 48 back
↓
call expression becomes 48
↓
total receives 48
```

Esse é o principal modelo mental do capítulo.

## 22. Exemplos executáveis

### Calcular um total

Arquivo: [`examples/calculate_total.py`](examples/calculate_total.py)

```python
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(12, 4)

print(total)
print(total + 5)
```

Saída esperada:

```text
48
53
```

### Retornar por ramificação

Arquivo: [`examples/classify_score.py`](examples/classify_score.py)

```python
def classify_score(score):
    if score >= 90:
        return "excellent"

    if score >= 60:
        return "passing"

    return "needs review"


print(classify_score(95))
print(classify_score(72))
print(classify_score(40))
```

Saída esperada:

```text
excellent
passing
needs review
```

### Busca com `None`

Arquivo: [`examples/find_first_even.py`](examples/find_first_even.py)

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


print(find_first_even([3, 7, 8, 10]))
print(find_first_even([1, 3, 5]))
```

Saída esperada:

```text
8
None
```

## 23. Exercício: categoria de temperatura

Crie `classify_temperature(temperature)`.

Requisitos:

1. retorne `"hot"` para valores de pelo menos `30`;
2. retorne `"mild"` para valores de pelo menos `18`, mas abaixo de `30`;
3. retorne `"cold"` nos demais casos;
4. chame com `34`, `22` e `10`;
5. armazene cada resultado antes de imprimi-lo.

Saída esperada:

```text
hot
mild
cold
```

Não use type hints, valores padrão, `*args` ou `**kwargs`.

## 24. Checklist de revisão

Antes de continuar, confirme que você consegue:

- [ ] escrever `return expression`;
- [ ] explicar que a expressão é avaliada antes de a função terminar;
- [ ] armazenar e reutilizar valores retornados;
- [ ] usar um booleano retornado em `if`;
- [ ] diferenciar `print()` de `return`;
- [ ] usar diferentes retornos em diferentes ramificações;
- [ ] diferenciar `return` de `break`;
- [ ] explicar `None` implícito, `return` sem expressão e `return None`;
- [ ] explicar que `return a, b` retorna uma única tupla;
- [ ] reconhecer um `return` colocado cedo demais em um loop;
- [ ] rastrear valores dos argumentos de volta ao chamador.

## 25. Referência rápida

| Necessidade | Forma | Significado |
|---|---|---|
| retornar valor | `return expression` | avaliar, sair da função e enviar valor ao chamador |
| armazenar resultado | `result = function()` | associar valor retornado no chamador |
| usar resultado | `print(function())` | usar valor retornado em outra chamada |
| retornar booleano | `return condition` | chamador recebe `True` ou `False` |
| retornar `None` | `return` / `return None` | sair da função com `None` |
| `None` implícito | chegar ao fim | resultado da chamada é `None` |
| retornar tupla | `return a, b` | retornar uma única tupla |
| parar loop | `break` | sair do loop atual |
| parar função | `return value` | encerrar a chamada atual da função |

## 26. Limite de escopo

Este capítulo adia intencionalmente:

- regras de escopo local/global;
- type hints e anotações de retorno;
- valores padrão;
- `*args` e `**kwargs`;
- sintaxe positional-only e keyword-only;
- desempacotamento de argumentos;
- funções aninhadas e lambdas;
- decorators, generators, `yield` e recursão;
- tratamento de exceções;
- design avançado de propriedade e mutação.

## 27. O que vem depois

Agora você consegue rastrear:

```text
caller → arguments → parameters → function body → return value → caller
```

A próxima pergunta é:

> Onde existem os nomes dentro e fora de uma função, e quando eles ficam visíveis?

Isso leva ao **Capítulo 04: Escopo**.

Volte para a [trilha de Funções](../README.pt-BR.md) ou para a [trilha completa de estudos](../../docs/learning-path.pt-BR.md).

## Referências

Documentação primária do Python:

- [Tutorial do Python 3.13: Definindo Funções](https://docs.python.org/pt-br/3.13/tutorial/controlflow.html#defining-functions)
- [Referência da Linguagem Python 3.13: A instrução `return`](https://docs.python.org/pt-br/3.13/reference/simple_stmts.html#the-return-statement)
