<div align="center">

# Valores Padrão

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Anterior: Type Hints](../05-type-hints/README.pt-BR.md)

Os capítulos anteriores mostraram como funções recebem argumentos, devolvem valores, resolvem nomes e descrevem tipos esperados. Este capítulo adiciona mais uma decisão de interface:

> Quais entradas todo chamador precisa fornecer e quais podem ter um valor alternativo sensato?

```text
required input
    +
defaulted input
        ↓
caller supplies only what needs to differ
```

**Tempo estimado de estudo:** 75–100 minutos.

**Versão do Python:** os exemplos usam **Python 3.10 ou mais recente**, acompanhando o capítulo de Type Hints.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- definir um valor padrão com `name=value`;
- combinar type hints e padrões com `name: type = value`;
- diferenciar parâmetros obrigatórios de parâmetros com padrão;
- substituir padrões com argumentos posicionais ou nomeados;
- explicar a regra de ordem para parâmetros obrigatórios e com padrão comuns;
- explicar quando expressões padrão são avaliadas;
- reconhecer a armadilha de argumentos padrão mutáveis;
- usar `None` antes de criar um objeto mutável novo;
- escolher padrões que esclareçam a interface em vez de esconder entradas obrigatórias.

## 1. Um padrão permite omitir um argumento

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


print(greet("Avery"))
print(greet("Avery", "Welcome"))
```

Saída:

```text
Hello, Avery
Welcome, Avery
```

`name` não tem padrão, então o chamador precisa fornecê-lo.

`greeting` tem o padrão `"Hello"`, então seu argumento pode ser omitido.

```text
greet("Avery")
       ↓
name = "Avery"
greeting = "Hello"  ← default fills the missing slot
```

## 2. A sintaxe da definição e da chamada tem funções diferentes

A forma básica da definição é:

```text
def function_name(required, optional=default_value):
    ...
```

Exemplo:

```python
def build_label(topic, prefix="Topic"):
    return f"{prefix}: {topic}"


print(build_label("Functions"))
print(build_label("Functions", prefix="Chapter"))
```

Saída:

```text
Topic: Functions
Chapter: Functions
```

Mantenha os dois usos de `=` separados:

```text
definition → prefix="Topic"     establishes a default
call       → prefix="Chapter"   supplies a keyword argument
```

## 3. Parâmetros obrigatórios e com padrão representam decisões de design

```python
def create_message(name, language="English"):
    return f"{name}: {language}"
```

`name` é obrigatório porque a função não deveria inventá-lo.

`language` possui padrão porque `"English"` foi escolhido como alternativa deliberada.

Pergunte:

> Se o chamador não informar nada sobre esta opção, qual comportamento é razoável e pouco surpreendente?

Não adicione padrões apenas para tornar todos os argumentos opcionais.

## 4. Um argumento fornecido substitui o padrão naquela chamada

```python
def format_score(score, suffix=" points"):
    return f"{score}{suffix}"


print(format_score(80))
print(format_score(80, " pts"))
```

Saída:

```text
80 points
80 pts
```

Python usa o padrão apenas quando o parâmetro correspondente ainda não recebeu valor.

Fornecer outro valor em uma chamada não altera o padrão armazenado.

## 5. Vários padrões funcionam bem com substituições por nome

```python
def create_badge(name, color="blue", size="medium"):
    return f"{name}: {color}, {size}"


print(create_badge("Python"))
print(create_badge("Python", size="large"))
print(create_badge("Python", color="green"))
```

Saída:

```text
Python: blue, medium
Python: blue, large
Python: green, medium
```

Argumentos nomeados permitem alterar uma opção sem repetir as demais.

## 6. Parâmetros obrigatórios normalmente vêm primeiro

Isto é válido:

```python
def register(name, active=True):
    return f"{name}: {active}"
```

Isto não é:

```python
# SyntaxError: non-default argument follows default argument
def register(active=True, name):
    return f"{name}: {active}"
```

Para parâmetros comuns, use esta regra inicial:

```text
required parameters first
defaulted parameters after them
```

Categorias especiais de parâmetros refinam essa regra mais adiante.

## 7. Type hints e padrões podem aparecer juntos

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(greet("Avery"))
```

Leia a assinatura assim:

```text
name: str
├── expected type: str
└── no default → argument required

greeting: str = "Hello"
├── expected type: str
└── default: "Hello" → argument may be omitted

-> str
└── expected return type
```

Type hints descrevem tipos esperados. Padrões descrevem o comportamento quando um argumento é omitido.

Nenhum dos dois substitui validação em runtime.

## 8. Mantenha quatro conceitos separados

```text
default    → fallback when an argument is omitted
type hint  → expected type information
validation → checks actual values or rules
conversion → explicitly transforms compatible data
```

Por exemplo:

```python
def repeat_text(text: str, times: int = 2) -> str:
    return text * times
```

`times=2` é um valor alternativo. Ele não valida todo valor futuro.

## 9. Um padrão faz parte do comportamento público

```python
def create_heading(title: str, level: int = 2) -> str:
    return f"h{level}: {title}"
```

A interface comunica:

> Se o chamador não escolher um nível, use 2.

Alterar o padrão depois modifica todas as chamadas que omitem `level`.

Padrões são pequenas decisões de interface, não apenas sintaxe mais curta.

## 10. Não esconda entradas realmente obrigatórias

Este design pode esconder dados ausentes:

```python
def create_student(name="", course=""):
    ...
```

Se as duas informações forem necessárias, exija ambas:

```python
def create_student(name: str, course: str, active: bool = True):
    ...
```

Agora apenas `active` possui um valor alternativo deliberado.

Uma chamada menor não é automaticamente uma interface mais clara.

## 11. Expressões padrão são avaliadas quando a função é definida

```python
level = "beginner"


def describe(topic, course_level=level):
    return f"{topic}: {course_level}"


level = "advanced"

print(describe("Functions"))
print(describe("Functions", level))
```

Saída:

```text
Functions: beginner
Functions: advanced
```

Quando a instrução `def` foi executada, `level` valia `"beginner"`.

Esse valor virou o padrão armazenado de `course_level`.

Alterar a variável externa depois não recalcula o padrão.

## 12. Padrões são avaliados uma vez, não uma vez por chamada

Use este modelo mental:

```text
execute def statement
    ↓
evaluate default expressions
    ↓
store their resulting values
    ↓
future calls reuse stored defaults when needed
```

Esse detalhe importa principalmente quando o objeto armazenado pode mudar.

## 13. Padrões imutáveis costumam ser simples

Strings, números, booleanos e `None` são padrões comuns:

```python
def describe_course(
    name: str,
    level: str = "beginner",
    lessons: int = 10,
    published: bool = False,
) -> str:
    return f"{name} | {level} | {lessons} | {published}"
```

Esses valores são imutáveis, então não criam o problema de mutação compartilhada mostrado a seguir.

Ainda assim, pergunte se cada valor alternativo faz sentido.

## 14. Padrões mutáveis podem conservar alterações entre chamadas

```python
def add_topic(topic, topics=[]):
    topics.append(topic)
    return topics


print(add_topic("functions"))
print(add_topic("defaults"))
```

Saída:

```text
['functions']
['functions', 'defaults']
```

A mesma lista é reutilizada porque foi criada quando a definição da função foi executada.

Essa é a **armadilha do argumento padrão mutável**.

## 15. O problema é reutilizar o objeto padrão

Listas são normais dentro do corpo de funções:

```python
def create_topics():
    topics = []
    topics.append("functions")
    return topics
```

Uma nova lista é criada sempre que o corpo executa.

A forma arriscada é especificamente:

```python
def add_topic(topic, topics=[]):
    ...
```

porque essa lista pertence aos padrões armazenados e pode sobreviver entre chamadas.

## 16. Use `None` quando a omissão deve criar um objeto novo

```python
def add_topic(topic: str, topics: list[str] | None = None) -> list[str]:
    if topics is None:
        topics = []

    topics.append(topic)
    return topics


print(add_topic("functions"))
print(add_topic("defaults"))
```

Saída:

```text
['functions']
['defaults']
```

Cada omissão de `topics` produz `None` primeiro; depois o corpo cria uma nova lista.

## 17. `None` atua como sentinela neste padrão

Aqui, `None` significa:

> Nenhuma lista foi fornecida, então crie uma agora.

```text
topics supplied?
├── yes → use that object
└── no  → default gives None
            ↓
        create a fresh list
```

Isso funciona quando `None` não é um dado significativo por si só para o parâmetro.

Sentinelas personalizadas são um tema avançado de design de interface e ficam fora deste capítulo.

## 18. Um objeto mutável fornecido ainda pode ser alterado

```python
def add_topic(topic: str, topics: list[str] | None = None) -> list[str]:
    if topics is None:
        topics = []

    topics.append(topic)
    return topics


planned = ["scope"]
result = add_topic("defaults", planned)

print(planned)
print(result)
```

Saída:

```text
['scope', 'defaults']
['scope', 'defaults']
```

O padrão seguro não copia um objeto fornecido explicitamente pelo chamador.

Estado padrão compartilhado e mutação deliberada de dados do chamador são perguntas diferentes.

## 19. Argumentos posicionais e nomeados podem substituir padrões

```python
def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(5, 3))
print(power(5, exponent=3))
```

Saída:

```text
25
125
125
```

Para configurações opcionais, um argumento nomeado costuma deixar a intenção mais clara.

## 20. Argumentos nomeados permitem pular padrões anteriores

```python
def export_summary(name, format="text", include_title=True):
    return f"{name}: {format}, title={include_title}"


print(export_summary("study", include_title=False))
```

Saída:

```text
study: text, title=False
```

Não existe um espaço posicional vazio para “mantenha este padrão, mas altere o próximo”.

Argumentos nomeados permitem substituições seletivas.

## 21. `None` não é automaticamente o melhor padrão

Um padrão pode ser qualquer valor adequado:

```python
def format_name(name, separator=", "):
    ...
```

Use `None` quando ele representar corretamente o caso de argumento omitido, principalmente para criar um objeto mutável novo.

Não substitua todo padrão por `None` mecanicamente.

## 22. Erros comuns

### Objeto mutável como padrão

Evite:

```python
def collect_item(item, items=[]):
    items.append(item)
    return items
```

Prefira:

```python
def collect_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items
```

### Parâmetro obrigatório depois de um padrão

Evite:

```python
# SyntaxError
def connect(timeout=30, host):
    return host, timeout
```

Prefira:

```python
def connect(host, timeout=30):
    return host, timeout
```

### Valor alternativo enganoso

Se `topic` é realmente obrigatório, não esconda essa decisão:

```python
def study(topic):
    return topic
```

## 23. Rastreando uma chamada completa

```python
def create_title(topic: str, prefix: str = "Chapter", number: int = 1) -> str:
    return f"{prefix} {number}: {topic}"


title = create_title("Defaults", number=6)
print(title)
```

Rastreamento:

```text
1. call create_title("Defaults", number=6)
2. topic = "Defaults"
3. number = 6
4. prefix is unfilled
5. prefix receives stored default "Chapter"
6. body returns "Chapter 6: Defaults"
7. title receives that returned string
```

Todo parâmetro possui um valor antes de o corpo executar, vindo de um argumento fornecido ou de um padrão.

## 24. Exemplo executável: opções de saudação

```python
def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"


print(greet("Avery"))
print(greet("Avery", greeting="Welcome"))
print(greet("Avery", punctuation="."))
```

Saída:

```text
Hello, Avery!
Welcome, Avery!
Hello, Avery.
```

## 25. Exemplo executável: cotação de frete

```python
def calculate_shipping(weight: float, rate: float = 2.5, handling: float = 3.0) -> float:
    return weight * rate + handling


print(calculate_shipping(4.0))
print(calculate_shipping(4.0, rate=3.0))
print(calculate_shipping(4.0, handling=0.0))
```

Saída:

```text
13.0
15.0
10.0
```

## 26. Exemplo executável: padrão seguro para lista

```python
def add_task(task: str, tasks: list[str] | None = None) -> list[str]:
    if tasks is None:
        tasks = []

    tasks.append(task)
    return tasks


print(add_task("study"))
print(add_task("practice"))
print(add_task("review", ["plan"]))
```

Saída:

```text
['study']
['practice']
['plan', 'review']
```

As duas primeiras chamadas criam listas independentes. A terceira altera deliberadamente a lista fornecida.

## 27. Conexão com capítulos anteriores

```text
definition and call
        ↓
parameters and arguments
        ↓
return values
        ↓
scope
        ↓
type hints
        ↓
default values
        ↓
required vs optional caller input
```

Padrões não substituem argumentos. Eles definem como um parâmetro recebe valor quando seu argumento é omitido.

## 28. Checklist de design

Antes de adicionar um padrão, pergunte:

- Esta entrada é realmente opcional?
- O valor alternativo é pouco surpreendente?
- Alterá-lo depois modifica comportamento importante?
- O padrão é mutável?
- Se for mutável, `None` deveria disparar um objeto novo?
- `None` é um dado significativo por si só?
- Um argumento nomeado deixaria a chamada mais clara?
- O type hint inclui `None` quando `None` é suportado?

## 29. Limite de escopo

Este capítulo trata de padrões comuns para parâmetros normais de função.

Ele não exige:

- parâmetros somente posicionais com `/`;
- design somente nomeado com `*`;
- `*args` e `**kwargs`;
- objetos sentinela personalizados;
- decorators;
- recursos avançados de tipagem;
- dataclasses ou construtores de classes.

O próximo capítulo apresenta `*args` e `**kwargs`.

## 30. Exercício

Crie `build_reminder`.

Requisitos:

- `task` é obrigatório;
- `priority` tem `"normal"` como padrão;
- `done` tem `False` como padrão;
- use type hints;
- retorne uma string formatada;
- faça uma chamada usando os dois padrões;
- faça outra substituindo apenas `priority` por nome.

```python
print(build_reminder("Study Python"))
print(build_reminder("Review functions", priority="high"))
```

### Desafio extra

Crie outra função com uma lista opcional:

- não use `[]` diretamente como padrão;
- use `None`;
- crie uma lista nova dentro do corpo;
- demonstre que duas chamadas sem lista não compartilham estado.

## 31. Perguntas de revisão

1. O que `language="English"` significa em uma definição?
2. Quando Python usa um padrão?
3. O que acontece quando o chamador fornece esse argumento?
4. Por que parâmetros obrigatórios comuns normalmente aparecem primeiro?
5. Quando expressões padrão são avaliadas?
6. Por que `items=[]` pode compartilhar estado entre chamadas?
7. Como o padrão com `None` evita esse problema?
8. Um padrão valida um argumento?
9. Qual a diferença entre type hints e padrões?
10. Por que um padrão deve representar comportamento realmente opcional?

## Referência rápida

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
```

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"
```

```python
greet("Avery", greeting="Welcome")
```

```python
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items
```

```text
default
→ used when the corresponding argument is omitted

default expression
→ evaluated when the function definition executes

mutable default object
→ can be shared between calls

None sentinel pattern
→ create a fresh mutable object inside the body
```

## Exemplos executáveis

```bash
python functions/06-default-values/examples/greet_with_style.py
python functions/06-default-values/examples/shipping_quote.py
python functions/06-default-values/examples/safe_list_default.py
```

## Referências

- [Python 3.13 Tutorial — Default Argument Values](https://docs.python.org/3.13/tutorial/controlflow.html#default-argument-values)
- [Python 3.13 Language Reference — Function definitions](https://docs.python.org/3.13/reference/compound_stmts.html#function-definitions)
- [Python 3.13 Language Reference — Calls](https://docs.python.org/3.13/reference/expressions.html#calls)

---

Próximo: **07. `*args` e `**kwargs`**.
