# Classes e objetos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../04-data-structures-and-algorithms-review/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../06-attributes-methods-and-object-behavior/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [functions/01-defining-and-calling-functions](../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.pt-BR.md)
- [comments-and-documentation/02-docstrings](../../comments-and-documentation/02-docstrings/README.pt-BR.md)

## O que é e por quê

Uma classe define um tipo e agrupa comportamentos relacionados; uma instância é um objeto desse tipo com estado próprio. Prefira uma classe quando estado e operações compartilham ciclo de vida ou invariante. Uma função pura pode ser mais simples para um cálculo sem estado.

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

first = Counter()
second = Counter()
first.increment()
print(first.value, second.value)  # 1 0
```

A chamada da classe normalmente cria e inicializa uma instância. `__init__` inicializa uma instância já criada; não é o mecanismo de criação do objeto (`__new__`). Não retorne valor diferente de None em `__init__`. `self` é o nome convencional do parâmetro da instância; uma chamada como `first.increment()` vincula essa instância automaticamente. Cada atribuição a `self.value` armazena estado na instância.

## Exemplo prático e erros

O exemplo compartilhado modela uma sessão de leitura. Seu método read valida a quantidade antes de atualizar o estado. Duas sessões mantêm totais independentes. Não use atributo mutável compartilhado da classe para estado por instância; não adicione classes apenas para envolver uma função independente.

## Prática

Implemente uma sessão que acompanhe tarefas concluídas em vez de páginas. Crie duas instâncias, teste estado independente e garanta que quantidades inválidas não alterem o total. Explique classe, instância, atributo e método com suas palavras.

**Referência rápida:** classe define tipo; instância guarda estado; método opera na instância; inicialize e valide deliberadamente.

[Exemplo executável compartilhado](examples/reading_session.py)

`python technical-interview-preparation/05-classes-and-objects/examples/reading_session.py`

## Referências oficiais (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../04-data-structures-and-algorithms-review/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../06-attributes-methods-and-object-behavior/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
