<div align="center">

# Escopo

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Anterior: Valores de Retorno](../03-return-values/README.pt-BR.md)

O Capítulo 01 deu nome ao comportamento. O Capítulo 02 moveu dados para dentro de uma função. O Capítulo 03 enviou resultados de volta ao chamador. Este capítulo responde à próxima pergunta:

> Onde cada nome existe e onde o Python consegue encontrá-lo?

O modelo mental para iniciantes passa a ser:

```text
caller → arguments → function local scope → return value → caller
```

**Tempo estimado de estudo:** 80–105 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar a diferença inicial entre **escopo** e **namespace**;
- identificar nomes globais no nível do módulo e nomes locais de funções;
- explicar que parâmetros são nomes locais;
- explicar que cada chamada de função recebe seu próprio namespace local;
- ler um nome do nível do módulo de dentro de uma função;
- prever quando uma atribuição cria uma ligação local;
- reconhecer sombreamento quando a mesma grafia é ligada em escopos diferentes;
- explicar que instruções comuns `if`, `for` e `while` não criam um novo escopo local de função;
- reconhecer `NameError` e o caso comum de `UnboundLocalError` relacionado a escopo;
- explicar o que `global` altera e por que o fluxo com parâmetros e retorno costuma ser mais claro;
- rastrear o caminho inicial de busca de nomes do escopo local até nomes globais e embutidos.

## 1. Escopo responde onde um nome é visível

Um **escopo** é uma região do código em que um nome pode ser acessado diretamente.

```python
course = "Python"


def show_course():
    message = "Studying"
    print(course)
    print(message)


show_course()
print(course)
```

Saída:

```text
Python
Studying
Python
```

`course` é ligado no nível do módulo, então a função consegue lê-lo. `message` é criado dentro da função e é local àquela chamada.

A grafia de um nome é apenas parte da história. **O local onde o nome é ligado importa.**

## 2. Namespace e escopo são relacionados, mas diferentes

Um **namespace** associa nomes a objetos. Um **escopo** descreve onde esses nomes são diretamente visíveis.

```text
namespace → which names are bound to which objects
scope     → where those names are directly visible
```

Por exemplo:

```python
course = "Python"
chapter = 4

print(course)
print(chapter)
```

Saída:

```text
Python
4
```

O namespace do módulo contém ligações para `course` e `chapter`.

## 3. Nomes no nível do módulo são globais para esse módulo

Um nome ligado no nível superior de um arquivo Python pertence ao namespace global daquele módulo.

```python
course = "Python"
chapter = 4

print(course)
print(chapter)
```

Os dois são nomes globais neste módulo.

Para código iniciante, “global” aqui significa global ao módulo atual, não compartilhado magicamente com todo programa Python.

## 4. Uma chamada de função cria um namespace local

Quando uma função é chamada, o Python cria um namespace local para aquela chamada.

```python
def show_message():
    message = "Ready"
    print(message)


show_message()
```

Saída:

```text
Ready
```

`message` é um nome local criado durante essa chamada. Uma chamada posterior recebe outro namespace local.

## 5. Parâmetros são nomes locais

Os parâmetros de uma função participam do namespace local da função.

```python
def greet(name):
    message = f"Hello, {name}"
    print(message)


greet("Avery")
```

Saída:

```text
Hello, Avery
```

Durante a chamada:

```text
argument "Avery"
↓
local parameter name → "Avery"
↓
local message is created
```

O argumento fornece um objeto. O parâmetro é o nome local usado pela função.

## 6. Nomes locais não escapam automaticamente da função

```python
def create_message():
    message = "Ready"


create_message()
print(message)
```

A chamada funciona, mas a última linha gera `NameError`. Não existe uma ligação visível chamada `message` no nível do módulo.

```text
inside function  → message is local
outside function → that local name is not directly visible
```

Se o chamador precisar do valor, retorne-o.

## 7. Cada chamada recebe seu próprio namespace local

```python
def build_label(topic):
    label = f"Learning {topic}"
    print(label)


build_label("scope")
build_label("functions")
```

Saída:

```text
Learning scope
Learning functions
```

Pense nas chamadas como espaços de trabalho separados:

```text
call 1 → topic and label for "scope"
call 2 → topic and label for "functions"
```

Os nomes do código-fonte são reutilizados, mas cada chamada tem seu próprio namespace local.

## 8. Uma função pode ler um nome global

Uma função pode ler um nome no nível do módulo sem declará-lo como `global` quando apenas lê esse nome.

```python
course = "Python"


def show_course():
    print(course)


show_course()
```

Saída:

```text
Python
```

O Python não encontra uma ligação local chamada `course`, então a busca continua para fora e encontra a ligação no nível do módulo.

Ler um nome global e **religar** um nome global são operações diferentes.

## 9. Constantes de módulo podem ser entradas compartilhadas razoáveis

```python
TAX_RATE = 0.10


def calculate_tax(amount):
    return amount * TAX_RATE


print(calculate_tax(200))
```

Saída:

```text
20.0
```

Nomes em maiúsculas como `TAX_RATE` são uma convenção de estilo para constantes. O Python não impõe imutabilidade porque um nome está em maiúsculas.

Ler uma constante de módulo claramente nomeada pode ser compreensível. Estado global mutável oculto é outro problema de design e fica para depois.

## 10. Atribuição dentro de uma função normalmente cria uma ligação local

Sem `global` ou `nonlocal`, atribuir a um nome dentro de uma função normalmente liga esse nome localmente.

```python
status = "module"


def show_status():
    status = "function"
    print(status)


show_status()
print(status)
```

Saída:

```text
function
module
```

A atribuição dentro de `show_status()` não substitui a ligação no nível do módulo. Ela cria uma ligação local com a mesma grafia.

## 11. Sombreamento usa a mesma grafia para ligações diferentes

O exemplo anterior contém **sombreamento**:

```text
inside show_status → status = "function"
module level       → status = "module"
```

Sombreamento é permitido. Sombreamento desnecessário ainda pode deixar o programa mais difícil de rastrear, então prefira nomes diferentes quando os significados forem realmente diferentes.

## 12. Busca de nomes para iniciantes: LEGB

Considere:

```python
topic = "scope"


def show_topic():
    message = "ready"
    print(message)
    print(topic)
    print(len(topic))


show_topic()
```

Saída:

```text
ready
scope
5
```

O mnemônico tradicional de busca é:

```text
Local → Enclosing → Global → Built-in
```

- **Local:** nomes da chamada atual da função;
- **Enclosing:** nomes de funções externas quando funções estão aninhadas;
- **Global:** nomes do módulo atual;
- **Built-in:** nomes como `len`, `print` e `abs`.

Este capítulo usa Local, Global e Built-in diretamente. Funções aninhadas e `nonlocal` ficam para depois, então Enclosing aparece apenas como parte do mapa de busca.

## 13. Evite sombrear nomes embutidos

Evite religar nomes embutidos conhecidos:

```python
len = 10

print(len("scope"))
```

Agora `len` se refere ao inteiro `10` no escopo atual, então a função embutida foi sombreada e a chamada falha.

Nomes como `list`, `str`, `type`, `sum`, `min`, `max`, `input` e `print` merecem a mesma cautela.

## 14. `if` não cria um novo escopo local de função

```python
def classify_score(score):
    if score >= 60:
        result = "passing"
    else:
        result = "review"

    print(result)


classify_score(75)
```

Saída:

```text
passing
```

`result` pertence ao escopo local da função ao redor. Os dois ramos ligam o nome, então a leitura posterior é segura.

## 15. `for` não cria um novo escopo local de função

```python
def show_last_number():
    for number in [1, 2, 3]:
        print(number)

    print("Last:", number)


show_last_number()
```

Saída:

```text
1
2
3
Last: 3
```

O alvo do loop `number` pertence ao escopo da função ao redor. Instruções comuns `while` seguem a mesma ideia de escopo ao redor.

Não generalize isso para toda construção Python. Funções, classes, comprehensions e outras construções têm regras próprias.

## 16. Pergunte se o nome foi definitivamente ligado antes do uso

Escopo e fluxo do programa trabalham juntos.

Uma pergunta útil é:

> No caminho que realmente executou, esse nome foi ligado antes de o Python tentar lê-lo?

Isso importa em ramificações e loops porque alguns caminhos podem não executar uma atribuição.

## 17. Um nome visível ausente gera `NameError`

Retome:

```python
def create_message():
    message = "Ready"


create_message()
print(message)
```

A última linha não consegue resolver `message` no nível do módulo e gera `NameError`.

Um checklist útil de depuração é:

1. A grafia está correta?
2. O nome foi ligado antes deste uso?
3. Ele foi ligado em um escopo visível daqui?
4. Eu esperava que um valor local saísse da função sem retorná-lo?

## 18. Uma atribuição em qualquer ponto da função pode tornar o nome local

Esta regra é sutil e importante:

```python
count = 10


def show_count():
    print(count)
    count = 20


show_count()
```

Chamar `show_count()` gera `UnboundLocalError`.

Por quê? A atribuição `count = 20` torna `count` um nome local para o bloco da função. O `print(count)` anterior tenta ler esse nome local antes de a ligação local receber um valor.

```text
function contains local binding for count
↓
print(count) runs before local count receives a value
↓
UnboundLocalError
```

`UnboundLocalError` é uma subclasse de `NameError`. Tratamento de exceções vem depois; aqui o objetivo é entender por que a busca falha.

## 19. Prefira fluxo explícito de entrada e retorno quando possível

Em vez de religar silenciosamente estado global compartilhado, passe o valor para a função e retorne o novo valor.

```python
count = 10


def increase(value):
    return value + 1


count = increase(count)
print(count)
```

Saída:

```text
11
```

O movimento é explícito:

```text
module count
↓ argument
local parameter value
↓ return
new module count
```

Isso se apoia diretamente nos Capítulos 02 e 03.

## 20. Ler um nome global não exige `global`

```python
mode = "study"


def show_mode():
    print(mode)


show_mode()
```

Saída:

```text
study
```

Nenhuma instrução `global` é necessária. `global` trata de ligar um nome no nível do módulo, não de conceder permissão para lê-lo.

## 21. `global` permite religação explícita no nível do módulo

```python
mode = "study"


def enable_practice_mode():
    global mode
    mode = "practice"


enable_practice_mode()
print(mode)
```

Saída:

```text
practice
```

Dentro dessa função, `global mode` direciona usos e atribuições de `mode` para a ligação no nível do módulo.

A declaração `global` deve aparecer antes de usos ou atribuições desse nome no mesmo escopo.

## 22. Use `global` com cautela

Compare:

```text
global rebinding
function → hidden change to module state

parameter/return flow
caller → explicit input → function → explicit output → caller
```

O segundo modelo costuma ser mais fácil de testar, reutilizar e compreender.

Use `global` quando estado compartilhado no nível do módulo for realmente o design desejado e o custo estiver entendido. Prefira parâmetros e valores de retorno quando eles deixarem o fluxo de dados mais claro.

Isso é uma recomendação de design, não uma proibição do Python.

## 23. Escopo e valores de retorno trabalham juntos

```python
course = "Python"


def build_message(topic):
    label = f"{course}: {topic}"
    return label


message = build_message("scope")
print(message)
```

Saída:

```text
Python: scope
```

`topic` e `label` são locais. O chamador recebe o objeto útil por `return` e o liga ao nome `message`.

O escopo cria a fronteira. `return` oferece um caminho explícito através dela.

## 24. Rastreie o percurso completo

Para o exemplo anterior:

```text
module binds course → "Python"
↓
caller passes "scope"
↓
local parameter topic is bound
↓
local label is bound
↓
course is found in module global scope
↓
function returns "Python: scope"
↓
caller binds message to returned value
```

Isso combina os modelos mentais dos Capítulos 02, 03 e 04.

## 25. Exemplos executáveis

### Nomes locais e globais

Arquivo: [`examples/local_and_global_names.py`](examples/local_and_global_names.py)

```python
course = "Python"


def show_course():
    message = "Studying"
    print(course)
    print(message)


show_course()
print(course)
```

Saída esperada:

```text
Python
Studying
Python
```

### Namespaces locais separados por chamada

Arquivo: [`examples/separate_function_calls.py`](examples/separate_function_calls.py)

```python
def build_label(topic):
    label = f"Learning {topic}"
    print(label)


build_label("scope")
build_label("functions")
```

Saída esperada:

```text
Learning scope
Learning functions
```

### Sombreamento sem alterar a ligação global

Arquivo: [`examples/shadowing_names.py`](examples/shadowing_names.py)

```python
status = "module"


def show_status():
    status = "function"
    print(status)


show_status()
print(status)
```

Saída esperada:

```text
function
module
```

## 26. Exercício: rastreie nomes globais e locais

Estude este programa:

```python
language = "Python"


def describe_topic(topic):
    label = f"{language}: {topic}"
    return label


result = describe_topic("scope")
print(result)
```

Saída esperada:

```text
Python: scope
```

Antes de executar, responda:

1. Quais nomes estão no nível do módulo?
2. Quais nomes são locais a `describe_topic()`?
3. Por que a função consegue ler `language` sem `global`?
4. Por que o chamador consegue usar o valor retornado, mas não o nome local `label` diretamente?
5. O que muda se a função atribuir a `language` sem declará-lo como `global`?

Depois execute o programa e confirme sua explicação.

## 27. Checklist de revisão

Antes de continuar, confirme que você consegue:

- [ ] explicar escopo e namespace em nível iniciante;
- [ ] identificar nomes globais do módulo e nomes locais de funções;
- [ ] explicar que parâmetros são nomes locais;
- [ ] explicar que cada chamada recebe seu próprio namespace local;
- [ ] ler um nome global de uma função sem `global`;
- [ ] reconhecer sombreamento local e de nomes embutidos;
- [ ] explicar Local → Enclosing → Global → Built-in;
- [ ] explicar o comportamento de escopo de `if`, `for` e `while` comuns;
- [ ] reconhecer `NameError` causado por nome visível ausente;
- [ ] explicar o `UnboundLocalError` comum causado por leitura antes da ligação local;
- [ ] explicar o que `global` altera;
- [ ] preferir parâmetros e retorno quando eles tornarem o fluxo de dados mais claro.

## 28. Referência rápida

| Necessidade | Regra para iniciantes |
|---|---|
| nome no nível do módulo | nome global para esse módulo |
| parâmetro de função | nome local |
| atribuição em uma função | normalmente liga um nome local |
| ler global da função | não exige `global` |
| religar global da função | declarar com `global` |
| mesma grafia local e global | a ligação local sombreia a global |
| `if` / `for` / `while` comuns | não criam novo escopo local de função |
| nome não encontrado | `NameError` |
| nome local lido antes da ligação local | `UnboundLocalError` |
| enviar resultado local ao chamador | usar `return` |
| mudança de estado mais clara | frequentemente parâmetros + retorno |

## 29. Limite de escopo

Este capítulo adia intencionalmente:

- funções aninhadas como técnica de programação;
- `nonlocal`;
- closures;
- funções lambda;
- escopos de classes e detalhes de busca específicos de métodos;
- detalhes de escopo de comprehensions;
- mutação e aliasing de objetos globais compartilhados;
- importação de módulos como tema principal;
- tratamento de exceções;
- decorators e generators.

Esses temas aparecem depois na trilha ou precisam de contexto próprio.

## 30. O que vem depois

Agora você consegue rastrear:

```text
caller
↓
arguments
↓
local parameter names
↓
local function work
↓
name lookup across visible scopes
↓
return value
↓
caller
```

A próxima pergunta é:

> Como uma função pode comunicar os tipos de entradas e saídas que espera?

Isso leva ao **Capítulo 05: Type Hints**.

Volte para a [trilha de Funções](../README.pt-BR.md) ou para a [trilha completa de estudos](../../docs/learning-path.pt-BR.md).

## Referências

Documentação primária do Python:

- [Python 3.13 Language Reference: Execution model](https://docs.python.org/pt-br/3.13/reference/executionmodel.html)
- [Python 3.13 Tutorial: Python Scopes and Namespaces](https://docs.python.org/pt-br/3.13/tutorial/classes.html#python-scopes-and-namespaces)
- [Python 3.13 Language Reference: The `global` statement](https://docs.python.org/pt-br/3.13/reference/simple_stmts.html#the-global-statement)
