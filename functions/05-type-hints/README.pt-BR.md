<div align="center">

# Type Hints

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Anterior: Escopo](../04-scope/README.pt-BR.md)

O Capítulo 01 deu nome ao comportamento. O Capítulo 02 levou dados para dentro das funções. O Capítulo 03 devolveu resultados. O Capítulo 04 explicou onde os nomes existem. Este capítulo adiciona outra camada:

> Como uma função pode descrever os tipos de valores que espera receber e devolver?

```text
function interface
├── parameter names
├── parameter type hints
└── return type hint
        ↓
function body still runs as ordinary Python
```

**Tempo estimado de estudo:** 75–100 minutos.

**Versão do Python:** este capítulo requer **Python 3.10 ou mais recente**.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que uma type hint comunica;
- anotar parâmetros com `name: type`;
- anotar retornos com `-> type`;
- explicar que o Python não impõe type hints em runtime por conta própria;
- distinguir hints de validação em runtime e conversão;
- usar `str`, `int`, `float`, `bool` e `None` em assinaturas simples;
- anotar o conteúdo de listas, dicionários e tuplas;
- usar `str | None` para um resultado simples valor-ou-`None`;
- ler uma assinatura tipada como uma interface compacta;
- manter as hints alinhadas ao comportamento real da função.

## 1. Type hints descrevem tipos esperados

Uma **type hint** é uma informação anexada ao código que descreve o tipo que se espera que um valor tenha.

Uma função tipada básica se parece com isto:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


message = greet("Avery")
print(message)
```

Saída:

```text
Hello, Avery
```

Leia a assinatura assim:

```text
name: str → espera-se que o parâmetro receba uma string
-> str    → espera-se que a função retorne uma string
```

As hints tornam o fluxo de dados pretendido visível antes de você ler o corpo.

## 2. Anotações de parâmetros usam dois-pontos

Uma hint de parâmetro aparece depois do nome do parâmetro:

```text
parameter_name: type
```

Os dois-pontos anotam o parâmetro que já existe. Eles não criam um segundo parâmetro.

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


print(calculate_total(12.5, 4))
```

Saída:

```text
50.0
```

A assinatura comunica `price → float`, `quantity → int` e `return → float`.

## 3. Anotações de retorno usam uma seta

Uma hint de retorno aparece depois da lista de parâmetros:

```text
def function_name(...) -> return_type:
```

A seta descreve o resultado esperado. Ela não realiza uma conversão.

```python
def is_passing(score: int) -> bool:
    return score >= 60


print(is_passing(72))
print(is_passing(45))
```

Saída:

```text
True
False
```

## 4. Type hints não impõem tipos em runtime por conta própria

Esta é a regra mais importante do capítulo.

O Python não rejeita automaticamente uma chamada apenas porque um argumento não corresponde a uma type hint:

```python
def echo_text(value: str) -> str:
    return value


result = echo_text(42)

print(result)
print(type(result).__name__)
```

Saída:

```text
42
int
```

A função declara `value: str`, mas a execução normal do Python ainda aceita `42` porque o corpo simplesmente devolve o objeto.

Uma IDE ou um verificador estático pode alertar sobre a chamada. A anotação em si não é uma guarda de runtime.

## 5. Type hints não convertem valores

Uma hint descreve um tipo esperado. Ela não executa silenciosamente `int()`, `float()`, `str()` ou outro conversor.

```python
def add_tax(amount: float) -> float:
    return amount * 1.1


print(add_tax(100.0))
```

Mantenha os conceitos separados:

```text
type hint  → descreve
conversion → transforma explicitamente um valor compatível
validation → verifica um valor ou uma regra real
```

## 6. Type hints e validação em runtime resolvem problemas diferentes

Ferramentas de tipagem estática raciocinam sobre tipos declarados antes ou enquanto você escreve o código. Validação em runtime verifica valores reais durante a execução.

Este exemplo contém as duas ideias:

```python
def set_username(username: str) -> str:
    if not isinstance(username, str):
        raise TypeError("username must be a str")

    return username


print(set_username("Avery"))
```

`username: str` documenta o tipo pretendido. `isinstance(username, str)` participa da verificação em runtime.

Usar `str` aqui mantém o exemplo focado. Uma verificação como `isinstance(value, int)` possui um detalhe extra importante para iniciantes: `bool` é uma subclasse de `int` em Python.

Não adicione validação em todo lugar apenas porque uma função possui anotações. Valide onde fronteiras reais do programa ou regras exigirem isso.

## 7. Tipos embutidos geralmente são suficientes

Muitas assinaturas para iniciantes precisam apenas de tipos que você já conhece: `str`, `int`, `float` e `bool`.

Você não precisa importar nada de `typing` para essas anotações básicas.

```python
def build_label(topic: str, chapter: int) -> str:
    return f"Chapter {chapter}: {topic}"


label = build_label("Type Hints", 5)
print(label)
```

Saída:

```text
Chapter 5: Type Hints
```

## 8. `-> None` descreve ausência de retorno útil

Use `-> None` quando uma função não foi projetada para devolver um resultado útil ao chamador:

```python
def show_status(status: str) -> None:
    print(f"Status: {status}")


show_status("ready")
```

Isso se conecta diretamente ao Capítulo 03: chegar ao fim de uma função sem outro valor retornado produz `None`.

## 9. Coleções podem descrever tipos de elementos

Um `list` isolado diz apenas que se espera uma lista. Python moderno também pode descrever o tipo esperado dos elementos:

```python
def first_topic(topics: list[str]) -> str:
    return topics[0]


print(first_topic(["scope", "type hints", "defaults"]))
```

Leia `list[str]` como “uma lista cujos elementos esperados são strings”.

## 10. Dicionários descrevem tipos de chaves e valores

```python
def total_scores(scores: dict[str, int]) -> int:
    return sum(scores.values())


print(total_scores({"Avery": 8, "Jordan": 9}))
```

`dict[str, int]` comunica:

```text
keys   → expected str
values → expected int
```

A hint não faz o Python inspecionar automaticamente cada item em runtime.

## 11. Hints de tupla podem descrever múltiplos resultados

```python
def min_and_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


print(min_and_max([4, 8, 2, 9]))
```

`tuple[int, int]` descreve uma tupla com dois itens inteiros esperados. Isso se encaixa naturalmente nos retornos separados por vírgula do Capítulo 03.

## 12. `str | None` descreve um resultado valor-ou-`None`

```python
def find_topic(topics: list[str], target: str) -> str | None:
    for topic in topics:
        if topic == target:
            return topic

    return None


print(find_topic(["scope", "type hints"], "type hints"))
print(find_topic(["scope", "type hints"], "files"))
```

Saída:

```text
type hints
None
```

`str | None` significa que o resultado esperado pode ser uma string ou `None`. A barra vertical expressa uma união de tipos permitidos.

Código mais antigo pode expressar a mesma ideia como `typing.Optional[str]`. Como este guia usa Python moderno, `str | None` é a forma preferida aqui. Por enquanto, basta reconhecer a forma antiga quando ela aparecer.

## 13. Assinaturas tipadas rotulam o fluxo de dados que você já conhece

```python
def summarize_scores(scores: list[int]) -> tuple[int, int]:
    lowest = min(scores)
    highest = max(scores)
    return lowest, highest


result = summarize_scores([72, 88, 91])
print(result)
```

Rastreie a interface:

```text
caller
↓
list[int]
↓
parameter
↓
function-local work
↓
tuple[int, int]
↓
caller
```

Hints não substituem parâmetros, escopo ou `return`. Elas descrevem essas fronteiras.

## 14. Hints devem corresponder ao comportamento real

```python
def format_score(score: int) -> str:
    return f"Score: {score}"


print(format_score(95))
```

A função recebe um inteiro e formata uma string, então `score: int -> str` corresponde à implementação. Uma hint desatualizada pode ser pior do que nenhuma hint porque cria confiança falsa.

## 15. Anotações de variáveis também existem

```python
course: str = "Python"
chapter: int = 5

print(course)
print(chapter)
```

Interfaces de funções continuam sendo o foco principal aqui. Você não precisa anotar toda variável local. Adicione uma anotação local quando ela realmente melhorar a clareza ou o suporte de ferramentas.

## 16. Anotações são metadados da função

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


print(greet.__annotations__)
```

No Python 3.13, anotações de função ficam disponíveis pelo mapeamento `__annotations__` do objeto função.

A representação impressa exata importa menos do que a ideia de que ferramentas podem inspecionar os metadados. Código de iniciante normalmente lê as hints no código-fonte em vez de usar `__annotations__` diretamente.

## 17. Análise estática e runtime são separados

Um verificador de tipos pode sinalizar esta chamada antes da execução:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


greet(42)
```

O Python ainda pode executá-la se as operações do corpo aceitarem o objeto.

```text
static analysis → reasons about declared types
runtime         → executes Python objects and operations
```

## 18. Editores e ferramentas podem usar hints

Ferramentas com suporte a tipos podem usar hints para alertas, autocomplete, informações ao passar o mouse, navegação e apoio a refatorações.

Os recursos exatos dependem da ferramenta e da configuração. O recurso da linguagem continua o mesmo: anotações descrevem a interface pretendida.

## 19. Fronteiras de funções são um lugar de alto valor para hints

Compare:

```python
def summarize(scores):
    ...
```

com:

```python
def summarize(scores: list[int]) -> str:
    ...
```

A segunda assinatura responde imediatamente “o que devo passar?” e “o que devo esperar de volta?”.

## 20. Não anote tudo apenas porque é possível

Isto é válido:

```python
def double(number: int) -> int:
    result: int = number * 2
    return result
```

Mas a anotação local pode acrescentar pouco porque a expressão já torna `result` óbvio.

Prefira hints que esclareçam interfaces e valores não óbvios. Evite transformar uma função pequena em um labirinto de rótulos redundantes.

## 21. Uma type hint não é uma regra de domínio

`value: int` pode comunicar que se espera um inteiro. Sozinho, isso não comunica nem impõe um intervalo como:

```text
0 <= value <= 100
```

Restrições de tipo e regras de domínio são dimensões diferentes. Implemente verificações em runtime quando as regras em runtime importarem.

## 22. Erros comuns

### Erro 1: esperar enforcement automático em runtime

```python
def echo(value: str) -> str:
    return value


echo(10)
```

A anotação sozinha não é uma guarda de runtime.

### Erro 2: esperar conversão automática

```python
def parse_count(count: int) -> int:
    return count
```

Passar `"5"` não cria automaticamente o inteiro `5`.

### Erro 3: anotar o tipo de retorno errado

```python
def label(score: int) -> int:
    return f"Score: {score}"
```

A implementação retorna uma string, então `-> int` é enganoso.

### Erro 4: supor que type hints provam que o algoritmo está correto

Uma função perfeitamente anotada ainda pode conter lógica incorreta.

## 23. Um exemplo prático

```python
def progress_message(completed: int, total: int) -> str:
    percentage = completed / total * 100
    return f"{percentage:.0f}% complete"


print(progress_message(4, 5))
```

Saída:

```text
80% complete
```

A assinatura torna a fronteira clara: `completed → int`, `total → int`, `return → str`. O corpo continua responsável pelo cálculo.

## Exemplos executáveis

O capítulo inclui três exemplos aprovados para execução automática:

### `annotated_greeting.py`

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


message = greet("Avery")

print(message)
```

```text
Hello, Avery
```

### `collection_summary.py`

```python
def summarize_topics(topics: list[str]) -> str:
    return f"{len(topics)} topics: {', '.join(topics)}"


print(summarize_topics(["scope", "type hints", "defaults"]))
```

```text
3 topics: scope, type hints, defaults
```

### `runtime_does_not_enforce.py`

```python
def echo_text(value: str) -> str:
    return value


result = echo_text(42)

print(result)
print(type(result).__name__)
```

```text
42
int
```

O último exemplo passa deliberadamente um `int` para um parâmetro anotado como `str`. O Python executa a chamada porque as anotações não impõem o tipo por conta própria.

## 24. Exercício

Crie `build_summary`.

Requisitos:

1. Receba `topic` como string.
2. Receba `scores` como uma lista de inteiros.
3. Retorne uma string.
4. Adicione hints aos dois parâmetros e ao retorno.
5. Produza este resultado para a chamada de exemplo:

```python
print(build_summary("Python", [8, 9, 10]))
```

```text
Python: 3 scores
```

Antes de executar, explique o que `topic: str`, `scores: list[int]` e `-> str` comunicam. Também responda se o Python rejeitaria automaticamente todo argumento incompatível em runtime.

## 25. Uma possível solução

```python
def build_summary(topic: str, scores: list[int]) -> str:
    return f"{topic}: {len(scores)} scores"


print(build_summary("Python", [8, 9, 10]))
```

Saída:

```text
Python: 3 scores
```

## 26. Checklist de revisão

Antes de continuar, confirme que você consegue explicar:

- [ ] o que uma type hint comunica;
- [ ] a sintaxe de parâmetro com `:`;
- [ ] a sintaxe de retorno com `->`;
- [ ] por que hints não impõem tipos em runtime por conta própria;
- [ ] por que hints não convertem valores;
- [ ] hints versus validação em runtime;
- [ ] `-> None`;
- [ ] `list[str]`;
- [ ] `dict[str, int]`;
- [ ] `tuple[int, int]`;
- [ ] `str | None`;
- [ ] por que hints devem corresponder ao comportamento real;
- [ ] por que nem toda variável local precisa de anotação.

## 27. Consulta rápida

| Objetivo | Sintaxe | Significado |
|---|---|---|
| Anotar parâmetro | `name: str` | argumento string esperado |
| Anotar retorno | `-> int` | resultado inteiro esperado |
| Sem resultado útil | `-> None` | chamador não deve esperar resultado útil |
| Lista de strings | `list[str]` | elementos string esperados |
| Dicionário | `dict[str, int]` | chaves string, valores inteiros |
| Tupla de dois inteiros | `tuple[int, int]` | dois itens inteiros esperados |
| String ou `None` | `str | None` | qualquer um dos resultados é esperado |
| Validação em runtime | código explícito | verifica valores reais em execução |
| Conversão | `int(value)`, etc. | cria explicitamente um valor convertido |

## Limite de escopo

Este capítulo deixa intencionalmente para depois:

- `TypeVar` e parâmetros de tipo genéricos;
- `Protocol` e subtipagem estrutural;
- overloads;
- `Literal` e `TypedDict`;
- aliases de tipo avançados;
- tipagem de callables e funções de ordem superior;
- ferramentas de estreitamento de tipos como `TypeGuard` e `TypeIs`;
- configuração de verificadores estáticos específicos;
- bibliotecas de validação em runtime.

Esses temas são úteis, mas exigem mais contexto do que um primeiro capítulo sobre anotações de funções.

## 28. O que vem depois

Agora você tem este modelo de função:

```text
define behavior
↓
receive arguments through parameters
↓
work inside local scope
↓
return results
↓
describe the interface with type hints
```

O próximo capítulo adiciona **Valores Padrão**, permitindo que alguns parâmetros se tornem opcionais no momento da chamada enquanto a interface continua explícita.

[← Anterior: Escopo](../04-scope/README.pt-BR.md) · [Voltar para Funções](../README.pt-BR.md)

## Referências

Documentação primária do Python:

- [Python 3.13 `typing` — Support for type hints](https://docs.python.org/3.13/library/typing.html)
- [Python 3.13 Data model — anotações de função e `__annotations__`](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13 Tipos embutidos — relação entre `bool` e `int`](https://docs.python.org/3.13/library/stdtypes.html)
