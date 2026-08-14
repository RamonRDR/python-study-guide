<div align="center">

# Fluxo de Dados Entre Funções

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Anterior: Funções Trabalhando Juntas](../08-functions-working-together/README.pt-BR.md) · [Próxima fase: Comentários e Documentação →](../../comments-and-documentation/README.pt-BR.md)

Quando funções trabalham juntas, valores percorrem o programa. Um argumento entra em uma função, um parâmetro o recebe, nomes locais podem transformá-lo e um valor retornado pode levar um resultado de volta ao chamador ou adiante para outra função.

Este capítulo torna esse movimento explícito. Ele também introduz uma distinção importante: **reatribuir um nome de parâmetro não é a mesma coisa que mutar um objeto mutável compartilhado**.

**Tempo estimado de estudo:** 90–120 minutos.

**Requisito de Python:** Python 3.10 ou mais recente. Este capítulo usa sintaxe moderna de anotações, como `int | None`, e anotações de coleções embutidas, como `list[int]`.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- rastrear um valor do chamador até um parâmetro e de volta por meio de `return`;
- explicar que parâmetros são nomes locais criados para cada chamada de função;
- distinguir o nome de variável do chamador do nome de parâmetro da função;
- explicar por que reatribuir um parâmetro não reatribui a variável do chamador;
- reconhecer quando a mutação de uma lista ou dicionário compartilhado fica visível fora da função;
- escolher entre retornar um valor transformado e mutar deliberadamente um objeto;
- usar variáveis intermediárias como pontos de verificação em um pipeline de dados;
- acompanhar dados através de condições, loops e várias chamadas de função;
- usar retornos em tupla quando uma função produz naturalmente vários resultados relacionados;
- tratar `None` deliberadamente quando uma função pode não ter um resultado útil;
- usar type hints para descrever o fluxo de dados esperado sem tratá-los como enforcement em runtime;
- evitar fluxo de dados oculto por estado global desnecessário;
- distinguir um grafo de chamadas de um rastreamento de fluxo de dados;
- concluir a Fase 5 com um modelo mental completo de entradas, trabalho local e saídas de funções.

## 1. O ciclo básico do fluxo de dados

Uma chamada de função costuma seguir este padrão:

```text
valor do chamador
    ↓
expressão de argumento
    ↓
parâmetro
    ↓
trabalho local
    ↓
valor retornado
    ↓
chamador recebe o resultado
```

Por exemplo:

```python
def double(number: int) -> int:
    result = number * 2
    return result


original = 6
doubled = double(original)
print(original)
print(doubled)
```

Saída:

```text
6
12
```

`original` e `number` são nomes diferentes. Durante a chamada, `number` é um nome de parâmetro local vinculado ao valor fornecido pelo chamador.

## 2. Nomes de argumentos e parâmetros não precisam ser iguais

O chamador pode usar qualquer nome de variável adequado:

```python
def format_name(name: str) -> str:
    return name.strip().title()


raw_text = "  ava stone  "
clean_text = format_name(raw_text)
print(clean_text)
```

Saída:

```text
Ava Stone
```

A relação é criada pela chamada de função, não por nomes iguais:

```text
raw_text ──argument──> name
```

Dentro de `format_name()`, a função trabalha com seu parâmetro local `name`.

## 3. Cada chamada recebe seus próprios vínculos locais de parâmetros

Chamar a mesma função duas vezes não faz com que as duas chamadas compartilhem um único parâmetro local.

```python
def add_one(number: int) -> int:
    number = number + 1
    return number


first = add_one(4)
second = add_one(10)
print(first, second)
```

Saída:

```text
5 11
```

Cada chamada possui seu próprio vínculo local para `number`.

Isso se conecta diretamente ao capítulo anterior sobre escopo: nomes locais pertencem a uma chamada específica da função.

## 4. Reatribuir um parâmetro não reatribui a variável do chamador

Considere um inteiro:

```python
def add_five(number: int) -> int:
    number += 5
    return number


score = 70
updated_score = add_five(score)
print(score)
print(updated_score)
```

Saída:

```text
70
75
```

Dentro da função, `number += 5` faz o nome local `number` passar a se referir ao resultado `75`.

Isso **não** faz o nome `score` do chamador passar a se referir a `75`.

O chamador só muda se atribuir explicitamente o valor retornado:

```python
score = add_five(score)
```

## 5. Um valor retornado não substitui automaticamente o valor original

Esta chamada calcula e retorna um resultado:

```python
updated_score = add_five(score)
```

O resultado é armazenado em `updated_score` porque o chamador escolheu esse alvo de atribuição.

Esta chamada descarta o valor retornado:

```python
add_five(score)
```

Python ainda executa a função, mas nenhum nome do chamador mantém o inteiro retornado.

Um modelo mental útil é:

```text
return fornece um valor
assignment decide onde o chamador o armazena
```

## 6. Valores imutáveis deixam a reatribuição mais fácil de enxergar

Inteiros, strings e tuplas são imutáveis. Uma função não consegue alterar um objeto inteiro ou string existente no lugar.

Por exemplo:

```python
def add_prefix(text: str) -> str:
    text = "INFO: " + text
    return text


message = "Ready"
formatted = add_prefix(message)
print(message)
print(formatted)
```

Saída:

```text
Ready
INFO: Ready
```

O parâmetro local é reatribuído ao novo resultado string. O nome original do chamador continua apontando para a string original.

## 7. Objetos mutáveis adicionam uma segunda possibilidade importante

Listas e dicionários são mutáveis. Se o chamador e a função se referirem ao mesmo objeto mutável, a função pode mutar esse objeto.

```python
def add_topic(topics: list[str], topic: str) -> None:
    topics.append(topic)


topics = ["Functions"]
add_topic(topics, "Data flow")
print(topics)
```

Saída:

```text
['Functions', 'Data flow']
```

A função não reatribuiu a variável do chamador. Ela mutou o próprio objeto lista ao qual os dois nomes se referiam durante a chamada.

## 8. Reatribuir um parâmetro lista é diferente de mutar a lista

Compare estas funções:

```python
def replace_topics(topics: list[str]) -> None:
    topics = ["New topic"]


def append_topic(topics: list[str]) -> None:
    topics.append("New topic")


first = ["Functions"]
second = ["Functions"]

replace_topics(first)
append_topic(second)

print(first)
print(second)
```

Saída:

```text
['Functions']
['Functions', 'New topic']
```

`replace_topics()` apenas reatribui seu nome de parâmetro local.

`append_topic()` altera o próprio objeto lista compartilhado.

Essa distinção é central para raciocinar sobre fluxo de dados em Python.

## 9. Mutação não é automaticamente errada

Uma função que atualiza deliberadamente uma lista pode ter uma interface clara:

```python
def record_score(scores: list[int], score: int) -> None:
    scores.append(score)
```

A pergunta importante é se a mutação é esperada e compreensível.

A mutação se torna difícil quando quem chama assume que a função apenas lê os dados, mas ela altera o objeto silenciosamente.

Torne efeitos colaterais deliberados e fáceis de descobrir por meio de nomes, documentação e comportamento pequeno e focado.

## 10. Retornar um novo resultado pode deixar transformações mais fáceis de rastrear

Em vez de mutar uma coleção de entrada, uma função pode construir e retornar uma nova coleção.

```python
def clamp_scores(scores: list[int]) -> list[int]:
    result = []

    for score in scores:
        if score < 0:
            result.append(0)
        elif score > 100:
            result.append(100)
        else:
            result.append(score)

    return result


raw_scores = [105, 80, -4]
clean_scores = clamp_scores(raw_scores)
print(raw_scores)
print(clean_scores)
```

Saída:

```text
[105, 80, -4]
[100, 80, 0]
```

Esse design preserva a entrada original e deixa a transformação explícita pelo valor retornado.

## 11. Escolha mutação ou transformação retornada de acordo com a intenção

Não existe uma regra do Python dizendo que toda função deve evitar mutação.

Uma pergunta útil de decisão é:

```text
Esta função deve atualizar este objeto existente?
    sim → mutação deliberada pode fazer sentido
    não → retorne um novo resultado
```

Qualquer que seja o design escolhido, torne-o previsível para o chamador.

## 12. Variáveis intermediárias são pontos de verificação do fluxo de dados

O Capítulo 08 mostrou que várias funções podem formar um pipeline. Nomes intermediários deixam cada etapa visível.

```python
def clamp_score(score: int) -> int:
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score


def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


raw_score = 108
clean_score = clamp_score(raw_score)
status = classify_score(clean_score)

print(raw_score, clean_score, status)
```

Saída:

```text
108 100 excellent
```

Os nomes `raw_score`, `clean_score` e `status` funcionam como pontos de verificação rotulados.

## 13. Rastreie o pipeline uma transformação por vez

O exemplo anterior pode ser desenhado assim:

```text
108
 ↓ clamp_score()
100
 ↓ classify_score()
"excellent"
```

Isso é um **rastreamento de fluxo de dados**. Ele enfatiza os valores se movendo entre etapas.

Isso é diferente de um grafo de chamadas:

```text
main code
├── clamp_score()
└── classify_score()
```

Um grafo de chamadas enfatiza quem chama quem. Um rastreamento de fluxo de dados enfatiza quais dados se movem e mudam.

## 14. Uma função coordenadora pode tornar o fluxo explícito

O mesmo pipeline pode viver dentro de uma coordenadora:

```python
def clamp_score(score: int) -> int:
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score


def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def build_score_summary(score: int) -> str:
    clean_score = clamp_score(score)
    status = classify_score(clean_score)
    return f"{clean_score}: {status}"


print(build_score_summary(108))
```

Saída:

```text
100: excellent
```

A coordenadora é dona da sequência. As auxiliares são donas das transformações individuais.

## 15. Dados podem se ramificar por condições

Uma função não precisa retornar o mesmo valor interno em todas as etapas, mas seu comportamento público deve continuar compreensível.

```python
def find_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

A entrada `score` chega a um de dois `return`.

Um rastreamento simples é:

```text
score
  ↓ condition
  ├─ true  → "ready"
  └─ false → "review"
```

## 16. Retornos antecipados podem interromper o fluxo deliberadamente

Às vezes uma função detecta que não existe um resultado útil para continuar.

```python
def find_first_positive(values: list[int]) -> int | None:
    for value in values:
        if value > 0:
            return value
    return None


result = find_first_positive([-4, -2, 7, 9])
print(result)
```

Saída:

```text
7
```

A função retorna assim que encontra o primeiro valor adequado.

## 17. `None` pode representar ausência de um resultado útil

Quando `None` faz parte da interface, o chamador deve tratá-lo de forma intencional.

```python
def find_first_positive(values: list[int]) -> int | None:
    for value in values:
        if value > 0:
            return value
    return None


result = find_first_positive([-4, -2])

if result is None:
    print("No positive value")
else:
    print(result)
```

Saída:

```text
No positive value
```

O chamador verifica o resultado antes de enviá-lo para outro cálculo.

## 18. Não continue um pipeline com `None` sem perceber

Suponha que outra função espere um inteiro:

```python
def double(number: int) -> int:
    return number * 2
```

Passar um possível `None` sem verificar antes cria um fluxo inseguro.

O type hint `int | None` é útil porque informa leitores e ferramentas de análise estática que o caso de ausência existe.

Type hints descrevem a interface pretendida. Python não os aplica automaticamente em runtime.

## 19. Vários resultados relacionados podem viajar em uma tupla

Uma função pode produzir naturalmente mais de um resultado relacionado.

```python
def summarize(values: list[int]) -> tuple[int, int]:
    total = sum(values)
    count = len(values)
    return total, count


total, count = summarize([10, 20, 30])
print(total)
print(count)
```

Saída:

```text
60
3
```

Python cria uma tupla para os valores retornados, e o chamador desempacota essa tupla em dois nomes.

## 20. Retornos em tupla deixam dependências posteriores visíveis

Um cálculo posterior pode usar um ou ambos os valores retornados:

```python
def summarize(values: list[int]) -> tuple[int, int]:
    return sum(values), len(values)


def calculate_average(total: int, count: int) -> float:
    if count == 0:
        return 0.0
    return total / count


total, count = summarize([10, 20, 30])
average = calculate_average(total, count)
print(average)
```

Saída:

```text
20.0
```

A dependência está explícita: `calculate_average()` precisa de `total` e `count`.

## 21. Loops podem mover muitos valores pelo mesmo helper

Um loop pode enviar um item por vez para uma função:

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


names = [" ava ", "LEO", " mia"]
clean_names = []

for name in names:
    clean_names.append(normalize_name(name))

print(clean_names)
```

Saída:

```text
['Ava', 'Leo', 'Mia']
```

Cada iteração cria outra chamada e outro vínculo local de parâmetro.

## 22. Coleções podem passar por várias etapas

Uma coleção pode ser transformada, resumida e formatada por funções diferentes.

```python
def keep_positive(values: list[int]) -> list[int]:
    result = []

    for value in values:
        if value > 0:
            result.append(value)

    return result


def calculate_total(values: list[int]) -> int:
    return sum(values)


def format_total(total: int) -> str:
    return f"Total: {total}"


raw_values = [-3, 5, 8, -1]
positive_values = keep_positive(raw_values)
total = calculate_total(positive_values)
message = format_total(total)
print(message)
```

Saída:

```text
Total: 13
```

O tipo de dado muda ao longo do caminho:

```text
list[int] → list[int] → int → str
```

## 23. Type hints podem documentar a forma de cada etapa

O pipeline anterior expõe suas transições esperadas diretamente nas assinaturas:

```text
keep_positive(list[int]) -> list[int]
calculate_total(list[int]) -> int
format_total(int) -> str
```

Isso pode facilitar a inspeção de um design com várias funções.

Lembre-se: type hints comunicam intenção e apoiam ferramentas. Eles não validam nem convertem valores automaticamente em runtime.

## 24. Globais ocultas dificultam enxergar o fluxo de dados

Compare esta dependência escondida:

```python
tax_rate = 0.10


def add_tax(amount: float) -> float:
    return amount * (1 + tax_rate)
```

com uma dependência explícita:

```python
def add_tax(amount: float, tax_rate: float) -> float:
    return amount * (1 + tax_rate)
```

A segunda assinatura mostra exatamente quais dados a função precisa.

Uma constante no nível do módulo pode ser apropriada em alguns designs. O problema é usar estado global para esconder entradas variáveis comuns que deveriam estar visíveis na interface.

## 25. Evite fazer uma função ler variáveis locais de outra função

Um nome local dentro de uma função não fica diretamente disponível dentro de outra função não relacionada.

```python
def first() -> int:
    value = 10
    return value


def second() -> int:
    value = first()
    return value * 2
```

`second()` recebe os dados pelo valor retornado por `first()`. Ela não entra no namespace local de `first()`.

Essa passagem explícita é uma fronteira saudável.

## 26. Exemplo prático: construir um relatório de aprendizagem

Este exemplo combina várias ideias de toda a fase de Funções:

```python
def summarize_sessions(sessions: list[int]) -> tuple[int, float]:
    total = sum(sessions)
    if not sessions:
        return total, 0.0
    return total, total / len(sessions)


def classify_total(total: int) -> str:
    if total >= 120:
        return "deep"
    if total >= 60:
        return "steady"
    return "light"


def build_learning_report(subject: str, sessions: list[int]) -> str:
    total, average = summarize_sessions(sessions)
    workload = classify_total(total)
    return (
        f"{subject}: {total} minutes, "
        f"average {average:.1f}, workload {workload}"
    )


print(build_learning_report("Python", [30, 45, 60]))
```

Saída:

```text
Python: 135 minutes, average 45.0, workload deep
```

Rastreamento:

```text
subject = "Python"
sessions = [30, 45, 60]
        ↓ summarize_sessions()
total = 135, average = 45.0
        ↓ classify_total(total)
workload = "deep"
        ↓ formatting
final str returned to caller
```

## 27. O comportamento com entrada vazia faz parte do design do fluxo de dados

`summarize_sessions()` trata explicitamente uma lista vazia:

```python
if not sessions:
    return total, 0.0
```

Sem esse ramo, dividir por `len(sessions)` falharia quando a lista estivesse vazia.

Pensar em fluxo de dados inclui perguntar:

- Quais valores podem entrar nesta função?
- Quais valores podem sair dela?
- O que acontece nos casos de borda?
- A próxima função consegue consumir com segurança todos os resultados possíveis?

## 28. Erro comum: assumir que reatribuir um parâmetro altera o chamador

Expectativa incorreta:

```python
def reset_score(score: int) -> None:
    score = 0


score = 80
reset_score(score)
print(score)
```

Saída:

```text
80
```

Se o chamador deve receber `0`, retorne o valor e atribua o resultado:

```python
def reset_score(score: int) -> int:
    return 0


score = reset_score(score)
```

## 29. Erro comum: mutar a entrada sem intenção

Esta função altera a lista do chamador:

```python
def prepare_names(names: list[str]) -> None:
    names.sort()
```

Isso pode estar correto se a mutação for o contrato pretendido.

Se o chamador espera que a ordem original permaneça intacta, construa e retorne um resultado separado.

A lição importante não é “nunca mute”. É “não esconda mutação”.

## 30. Erro comum: confundir dados retornados com saída impressa

Uma função pode imprimir uma mensagem útil e ainda retornar `None`:

```python
def show_total(values: list[int]) -> None:
    print(sum(values))
```

Se a próxima função precisa do total numérico, imprimir não basta. Retorne o número.

Essa distinção apareceu em toda a Fase 5 porque é uma das fronteiras mais importantes no fluxo de dados entre funções.

## 31. Erro comum: passar a etapa errada para a próxima função

Considere este pipeline:

```text
raw score → clamp → classify
```

Se a regra de classificação deve usar o score limitado, isto está errado:

```python
clean_score = clamp_score(raw_score)
status = classify_score(raw_score)
```

O código executa, mas o caminho dos dados não é o pretendido.

Nomes de variáveis intermediárias tornam esse tipo de erro mais fácil de perceber.

## 32. Erro comum: esconder etapas demais em uma expressão profundamente aninhada

Isto pode ser tecnicamente válido:

```python
message = format_total(calculate_total(keep_positive(raw_values)))
```

Mas ao aprender, depurar ou inspecionar várias etapas, checkpoints explícitos costumam ser mais claros:

```python
positive_values = keep_positive(raw_values)
total = calculate_total(positive_values)
message = format_total(total)
```

Prefira legibilidade a competições de quantidade de linhas.

## 33. Exercício

Construa um pequeno pipeline para temperaturas.

Requisitos:

1. Crie `clamp_temperature(temperature: int) -> int` que limite valores abaixo de `-50` para `-50` e acima de `50` para `50`.
2. Crie `classify_temperature(temperature: int) -> str` que retorne `"hot"` para valores de pelo menos `30`, `"cold"` para valores abaixo de `10` e `"mild"` caso contrário.
3. Crie `build_temperature_report(city: str, temperature: int) -> str`.
4. Dentro da coordenadora, envie primeiro a temperatura original para a função de limite.
5. Passe o resultado limitado para a função de classificação.
6. Retorne uma string final contendo cidade, temperatura limitada e categoria.
7. Teste a coordenadora com pelo menos uma temperatura fora do intervalo aceito.

Antes de programar, desenhe o fluxo de dados com setas.

## 34. Checklist de revisão

Agora você deve conseguir responder:

- Qual é a diferença entre uma variável do chamador e um nome de parâmetro?
- Reatribuir um parâmetro reatribui automaticamente a variável do chamador?
- Por que a mutação de uma lista ainda pode ficar visível para o chamador?
- Quando retornar um novo valor é mais claro do que mutar uma entrada?
- O que `return` fornece ao chamador?
- Qual é o papel da atribuição depois que uma função retorna?
- Como `None` pode interromper um pipeline?
- Como type hints podem deixar o movimento entre etapas mais fácil de entender?
- Qual é a diferença entre grafo de chamadas e rastreamento de fluxo de dados?
- Por que dependências globais ocultas são mais difíceis de raciocinar?

## 35. Resumo para consulta rápida

| Situação | Modelo útil |
|---|---|
| Chamador envia um valor | expressão de argumento vincula a um parâmetro naquela chamada |
| Função reatribui um parâmetro | vínculo da variável do chamador não muda |
| Função muta lista/dict compartilhado | mutação pode ficar visível para o chamador |
| Função produz valor transformado | retorne e deixe o chamador atribuir |
| Função pode não produzir resultado útil | retorne e trate `None` deliberadamente |
| Função produz resultados relacionados | retorne uma tupla e desempacote |
| Várias etapas cooperam | use nomes intermediários para expor o pipeline |
| Dependências estão ocultas em globais | prefira parâmetros/retornos explícitos quando apropriado |
| Precisa de visão estrutural | desenhe um grafo de chamadas |
| Precisa de visão do movimento de valores | desenhe um rastreamento de fluxo de dados |

## 36. Fase 5 concluída

Agora você consegue conectar toda a sequência de Funções:

```text
define and call
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
*args and **kwargs
    ↓
functions working together
    ↓
data flow between functions
```

A fase começou com um único `def` e termina com um modelo para compor funções acompanhando exatamente como os dados entram, mudam e saem de cada chamada.

Próximo passo na sequência recomendada: [Comentários, Documentação e Código Limpo](../../comments-and-documentation/README.pt-BR.md).

## Referências oficiais

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Tutorial: More on Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Python 3.13 Language Reference: `return` statement](https://docs.python.org/3.13/reference/simple_stmts.html#the-return-statement)
- [Python 3.13 Data Model](https://docs.python.org/3.13/reference/datamodel.html)
