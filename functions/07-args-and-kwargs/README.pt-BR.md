<div align="center">

# `*args` e `**kwargs`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Anterior: Valores Padrão](../06-default-values/README.pt-BR.md)

Os capítulos anteriores deram às funções parâmetros obrigatórios, valores de retorno, escopo, type hints e valores padrão seguros. Este capítulo adiciona uma nova opção de design: uma função pode coletar uma **quantidade variável de argumentos** quando a contagem exata é intencionalmente flexível.

```text
extra positional arguments → *args   → tuple
extra keyword arguments    → **kwargs → dictionary
```

**Tempo estimado de estudo:** 75–100 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que `*args` coleta;
- explicar o que `**kwargs` coleta;
- identificar a tupla armazenada por `*args`;
- identificar o dicionário armazenado por `**kwargs`;
- usar zero, um ou vários argumentos coletados;
- combinar parâmetros obrigatórios com `*args` ou `**kwargs`;
- usar `*args` e `**kwargs` juntos em uma assinatura simples;
- adicionar type hints aos valores coletados;
- diferenciar coleta na definição da função de desempacotamento no ponto de chamada;
- reconhecer quando uma lista explícita de parâmetros é mais clara do que uma coleta flexível.

## 1. Por que argumentos de tamanho variável existem

Às vezes uma função aceita naturalmente uma quantidade de valores que não é fixa com antecedência.

Uma função que soma pontuações pode receber dois valores em uma chamada e cinco em outra:

```python
def total_scores(*scores):
    return sum(scores)


print(total_scores(10, 20))
print(total_scores(10, 20, 30, 40, 50))
```

Saída:

```text
30
150
```

Sem um parâmetro de tamanho variável, seria necessário decidir uma quantidade fixa de parâmetros de pontuação ou exigir que o chamador montasse uma coleção antes.

Use coleta flexível quando a flexibilidade fizer parte do design da função, e não apenas para evitar decidir o que ela deve aceitar.

## 2. `*args` coleta argumentos posicionais extras

A sintaxe usa um `*` antes do nome do parâmetro:

```python
def show_values(*values):
    print(values)


show_values(4, 7, 9)
```

Saída:

```text
(4, 7, 9)
```

Dentro da função, `values` é uma tupla contendo os argumentos posicionais coletados por esse parâmetro.

```text
call:       show_values(4, 7, 9)
                         ↓  ↓  ↓
*values collects:      (4, 7, 9)
```

## 3. `args` é uma convenção, não um nome especial

Você verá com frequência:

```python
def show_values(*args):
    print(args)
```

Mas a parte especial é o `*`, e não a palavra `args`.

Isto é igualmente válido e muitas vezes mais descritivo:

```python
def show_scores(*scores):
    print(scores)
```

Prefira um nome significativo quando os valores coletados tiverem uma função clara.

## 4. `*args` pode coletar zero argumentos

Um parâmetro posicional de tamanho variável não exige pelo menos um valor:

```python
def show_items(*items):
    print(items)


show_items()
show_items("pen")
show_items("pen", "book")
```

Saída:

```text
()
('pen',)
('pen', 'book')
```

A chamada vazia produz uma tupla vazia.

## 5. Itere sobre a tupla coletada

Como o valor coletado é uma tupla, a iteração normal com `for` funciona naturalmente:

```python
def print_names(*names):
    for name in names:
        print(name)


print_names("Ava", "Leo", "Mia")
```

Saída:

```text
Ava
Leo
Mia
```

Tudo o que foi aprendido antes sobre iteração em tuplas continua valendo.

## 6. Parâmetros obrigatórios podem vir antes de `*args`

Uma função pode exigir um valor antes de coletar argumentos posicionais adicionais. O parâmetro comum antes de `*args` continua sendo posicional-ou-nomeado, a menos que a assinatura use uma sintaxe separada de somente posicional:

```python
def announce(prefix, *messages):
    for message in messages:
        print(prefix, message)


announce("INFO:", "Ready", "Running")
```

Saída:

```text
INFO: Ready
INFO: Running
```

Na chamada acima, `"INFO:"` é associado a `prefix` por posição. Os argumentos posicionais restantes são associados a `messages`:

```text
"INFO:"             → prefix
"Ready", "Running" → messages → ("Ready", "Running")
```

`prefix` é obrigatório porque não possui valor padrão, mas **obrigatório** não significa **somente posicional**. Se nenhuma mensagem extra for necessária, o mesmo parâmetro pode ser associado por nome:

```python
announce(prefix="INFO:")
```

Aqui, `messages` se torna uma tupla vazia. Com essa assinatura, as mensagens extras são posicionais, então, quando você quiser fornecê-las, a forma mais simples é a chamada posicional mostrada acima.

## 7. `**kwargs` coleta argumentos nomeados extras

A sintaxe usa dois caracteres `*` antes do nome do parâmetro:

```python
def show_details(**details):
    print(details)


show_details(color="blue", size="medium")
```

Saída:

```text
{'color': 'blue', 'size': 'medium'}
```

Dentro da função, `details` é um dicionário.

```text
color="blue"   → key "color", value "blue"
size="medium"  → key "size", value "medium"
```

## 8. `kwargs` também é apenas uma convenção

Isto é comum:

```python
def show_details(**kwargs):
    print(kwargs)
```

Mas isto é igualmente válido:

```python
def show_settings(**settings):
    print(settings)
```

Novamente, quem controla a coleta é `**`. O nome do parâmetro é uma escolha sua.

## 9. `**kwargs` pode coletar zero argumentos nomeados

```python
def show_options(**options):
    print(options)


show_options()
show_options(theme="dark")
```

Saída:

```text
{}
{'theme': 'dark'}
```

Nenhum argumento nomeado coletado significa um dicionário vazio.

## 10. Itere sobre nomes e valores nomeados

Iterar diretamente sobre um dicionário produz as chaves. Use `.items()` quando precisar de chaves e valores:

```python
def print_settings(**settings):
    for name, value in settings.items():
        print(name, value)


print_settings(language="Python", level="beginner")
```

Saída:

```text
language Python
level beginner
```

Isso é comportamento normal de dicionários, e não uma regra especial de `**kwargs`.

## 11. Parâmetros obrigatórios podem vir antes de `**kwargs`

Uma função pode exigir um dado nomeado e coletar informações adicionais por palavra-chave:

```python
def build_profile(name, **details):
    print("Name:", name)

    for key, value in details.items():
        print(key, value)


build_profile("Ava", role="student", active=True)
```

Saída:

```text
Name: Ava
role student
active True
```

O argumento obrigatório é associado a `name`. Os demais argumentos nomeados são coletados em `details`.

## 12. Use `*args` e `**kwargs` juntos

Uma assinatura simples pode coletar as duas formas:

```python
def describe_group(name, *members, **details):
    print("Group:", name)
    print("Members:", members)
    print("Details:", details)


describe_group("Study", "Ava", "Leo", topic="Python", active=True)
```

Saída:

```text
Group: Study
Members: ('Ava', 'Leo')
Details: {'topic': 'Python', 'active': True}
```

O modelo mental é:

```text
required positional-or-keyword input → ordinary parameter
extra positional input               → *members → tuple
extra keyword input                  → **details → dictionary
```

Um parâmetro comum como `name` é obrigatório aqui, mas pode receber seu valor tanto por posição quanto por nome. As duas chamadas abaixo são válidas, e nenhuma delas adiciona um valor a `*members`:

```python
describe_group("Study", topic="Python")
describe_group(name="Study", topic="Python")
```

Na segunda chamada, `name="Study"` é associado diretamente ao parâmetro comum `name`. Apenas `topic="Python"` permanece disponível para ser coletado por `**details`.

## 13. A ordem importa na assinatura da função

Para o padrão iniciante deste capítulo, pense em:

```python
def function(required, *args, **kwargs):
    pass
```

O parâmetro obrigatório é associado primeiro, `*args` coleta os argumentos posicionais restantes e `**kwargs` coleta os argumentos nomeados restantes.

Python também oferece outros recursos de ordenação de parâmetros, incluindo parâmetros somente nomeados e somente posicionais. Eles merecem tratamento próprio e ficam fora do foco principal deste capítulo.

## 14. Type hints descrevem cada valor coletado

Quando você anota `*args`, a anotação descreve cada valor posicional coletado:

```python
def total_scores(*scores: int) -> int:
    return sum(scores)
```

Conceitualmente, dentro da função:

```text
scores → tuple of int values
```

Para `**kwargs`, a anotação descreve cada valor coletado no dicionário:

```python
def show_labels(**labels: str) -> None:
    for name, value in labels.items():
        print(name, value)
```

Conceitualmente:

```text
labels → dictionary with string keys and str values
```

Como visto no Capítulo 05, type hints descrevem interfaces pretendidas, mas não impõem tipos automaticamente em runtime.

## 15. `*args` é uma tupla, não uma lista

Um erro comum é esperar métodos de lista:

```python
def collect(*items):
    print(type(items))


collect("a", "b")
```

Saída:

```text
<class 'tuple'>
```

Se a função realmente precisar de uma lista mutável, crie uma de forma explícita:

```python
def collect(*items):
    result = list(items)
    result.append("done")
    return result
```

Não trate mentalmente a tupla como lista apenas porque ambas são coleções ordenadas.

## 16. `**kwargs` é um dicionário normal dentro da função

Você pode usar operações já conhecidas de dicionários:

```python
def get_mode(**options):
    return options.get("mode", "standard")


print(get_mode())
print(get_mode(mode="compact"))
```

Saída:

```text
standard
compact
```

O dicionário existe para a chamada atual da função, assim como outros objetos locais criados durante essa chamada.

## 17. Não use flexibilidade quando parâmetros explícitos forem mais claros

Esta assinatura esconde a interface esperada:

```python
def create_user(**data):
    pass
```

Se a função realmente exige exatamente um nome e um email, isto é mais claro:

```python
def create_user(name, email):
    pass
```

Parâmetros explícitos melhoram legibilidade, suporte de editores, documentação e mensagens de erro quando as entradas aceitas são conhecidas.

Use `*args` e `**kwargs` porque a quantidade ou os nomes dos argumentos são intencionalmente variáveis, e não apenas porque deixam a assinatura menor.

## 18. Coleta na definição não é desempacotamento na chamada

Este capítulo usa estrelas nas definições de funções:

```python
def show_values(*values):
    print(values)


def show_details(**details):
    print(details)
```

Aqui, as estrelas **coletam** argumentos.

Python também pode usar `*` e `**` em chamadas para desempacotar um iterável ou mapping existente. Esse é o sentido oposto do fluxo de dados e fica intencionalmente para depois, para não misturar as duas ideias.

```text
definition side → collect
call side       → unpack (later topic)
```

## 19. Erro comum: esperar argumentos nomeados em `*args`

```python
def inspect(*values):
    print(values)


inspect(10, 20, 30)
```

Saída:

```text
(10, 20, 30)
```

`*values` coleta argumentos posicionais. Se você precisa de argumentos nomeados flexíveis, use um parâmetro com `**`.

## 20. Erro comum: iterar sobre `**kwargs` como se ele produzisse pares

```python
def show(**details):
    for item in details:
        print(item)


show(color="blue", size="medium")
```

Saída:

```text
color
size
```

A iteração direta em dicionários produz chaves. Use `details.items()` para pares chave-valor.

## 21. Erro comum: aceitar tudo sem um motivo

Uma assinatura como:

```python
def process(*args, **kwargs):
    pass
```

é extremamente flexível, mas pouco informativa.

Antes de usá-la, pergunte:

1. Os valores posicionais realmente têm quantidade variável?
2. Os nomes dos argumentos realmente são abertos?
3. Uma assinatura mais explícita comunicaria melhor o contrato?
4. A função vai validar ou usar claramente os dados coletados?

Flexibilidade é útil quando representa o problema. Flexibilidade desnecessária deixa APIs mais difíceis de entender.

## 22. Exemplos executáveis

### Calcular uma média com `*args`

Arquivo: [`examples/calculate_average.py`](examples/calculate_average.py)

```python
def calculate_average(first_score: float, *scores: float) -> float:
    return (first_score + sum(scores)) / (1 + len(scores))


print(calculate_average(8.0, 9.0, 10.0))
```

Saída esperada:

```text
9.0
```

Uma média exige pelo menos um valor, então `first_score` é obrigatório enquanto `*scores` coleta quaisquer pontuações adicionais.

### Exibir configurações com `**kwargs`

Arquivo: [`examples/display_settings.py`](examples/display_settings.py)

```python
def display_settings(**settings: str) -> None:
    for name, value in settings.items():
        print(f"{name}: {value}")


display_settings(theme="dark", language="English")
```

Saída esperada:

```text
theme: dark
language: English
```

### Combinar entrada obrigatória, posicional e nomeada

Arquivo: [`examples/describe_session.py`](examples/describe_session.py)

```python
def describe_session(title: str, *topics: str, **details: str) -> None:
    print(f"Title: {title}")
    print(f"Topics: {', '.join(topics)}")

    for name, value in details.items():
        print(f"{name}: {value}")


describe_session(
    "Python Study",
    "functions",
    "arguments",
    level="beginner",
    format="guided",
)
```

Saída esperada:

```text
Title: Python Study
Topics: functions, arguments
level: beginner
format: guided
```

## 23. Exercício: resumo flexível de pedido

Crie `summarize_order(order_id, *items, **details)`.

Requisitos:

1. imprima o ID do pedido;
2. imprima cada item em uma linha;
3. imprima cada detalhe como `name: value`;
4. chame a função com o ID `A-104`;
5. passe `"notebook"` e `"pen"` como itens posicionais;
6. passe `priority="normal"` e `channel="online"` como detalhes nomeados.

Saída esperada:

```text
Order: A-104
notebook
pen
priority: normal
channel: online
```

Mantenha o exercício focado na coleta. Não desempacote uma lista ou dicionário existente no ponto de chamada.

## 24. Checklist de revisão

Antes de continuar, confirme que você consegue:

- [ ] explicar que um `*` coleta argumentos posicionais extras;
- [ ] explicar que dois caracteres `*` coletam argumentos nomeados extras;
- [ ] identificar a tupla criada por um parâmetro no estilo `*args`;
- [ ] identificar o dicionário criado por um parâmetro no estilo `**kwargs`;
- [ ] lidar com zero argumentos coletados;
- [ ] iterar sobre valores posicionais coletados;
- [ ] iterar sobre pares chave-valor com `.items()`;
- [ ] combinar um parâmetro obrigatório com `*args` ou `**kwargs`;
- [ ] usar as duas formas em uma assinatura simples;
- [ ] adicionar type hints básicos aos valores coletados;
- [ ] explicar por que `args` e `kwargs` são convenções, e não nomes mágicos;
- [ ] diferenciar coleta na definição de desempacotamento na chamada;
- [ ] escolher parâmetros explícitos quando a interface for fixa.

## 25. Referência rápida

| Necessidade | Forma | Dentro da função |
|---|---|---|
| coletar argumentos posicionais extras | `def f(*values):` | `values` é uma tupla |
| coletar argumentos nomeados extras | `def f(**options):` | `options` é um dicionário |
| exigir um valor e coletar mais posicionais | `def f(first, *rest):` | `first` é normal; `rest` é uma tupla |
| exigir um valor e coletar detalhes nomeados | `def f(name, **details):` | `name` é normal; `details` é um dicionário |
| coletar as duas formas | `def f(name, *items, **details):` | tupla mais dicionário |
| anotar valores posicionais | `def f(*values: int):` | cada valor coletado é pretendido como `int` |
| anotar valores nomeados | `def f(**values: str):` | cada valor coletado é pretendido como `str` |

## 26. Limite de escopo

Este capítulo adia intencionalmente:

- desempacotar iteráveis com `*` no ponto de chamada;
- desempacotar mappings com `**` no ponto de chamada;
- sintaxe somente posicional com `/`;
- design detalhado de parâmetros somente nomeados;
- encaminhamento de argumentos arbitrários em funções wrapper;
- decorators;
- tipagem avançada para assinaturas flexíveis;
- introspecção de assinaturas de funções.

O objetivo aqui é construir um modelo mental estável de **coleta** antes de adicionar a operação inversa de desempacotamento.

## 27. O que vem depois

Agora você consegue projetar funções com entradas fixas, valores padrão opcionais e quantidades intencionalmente variáveis de argumentos.

A próxima pergunta é mais ampla:

> Como várias funções devem dividir trabalho e chamar umas às outras sem virar um emaranhado?

Isso leva ao **Capítulo 08: Funções Trabalhando Juntas**.

Volte para a [trilha de Funções](../README.pt-BR.md) ou para a [trilha completa](../../docs/learning-path.pt-BR.md).

## Referências

Documentação primária do Python:

- [Python 3.13 Tutorial: Arbitrary Argument Lists](https://docs.python.org/3.13/tutorial/controlflow.html#arbitrary-argument-lists)
- [Python 3.13 Tutorial: Keyword Arguments](https://docs.python.org/3.13/tutorial/controlflow.html#keyword-arguments)
- [Python 3.13 Language Reference: Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
