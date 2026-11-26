# Identidade de objetos, referências e cópias

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../08-encapsulation-abstraction-and-solid/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../10-python-memory-management/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.pt-BR.md)
- [collections/02-modifying-lists-and-methods](../../collections/02-modifying-lists-and-methods/README.pt-BR.md)
- [program-flow/01-conditions-comparisons-and-boolean-logic](../../program-flow/01-conditions-comparisons-and-boolean-logic/README.pt-BR.md)

## Identidade, igualdade e vinculação

Todo objeto tem identidade, tipo e valor. `is` compara identidade; `==` usa a semântica de igualdade, que uma classe pode personalizar. Use `is None` para o singleton, não `is` para comparar strings ou inteiros. `id(obj)` identifica um objeto vivo, mas IDs podem ser reutilizados após sua vida; especificamente no CPython, é o endereço de memória.

Atribuição vincula um nome, não cria cópia. Parâmetros de função também se vinculam a objetos: reatribuir o parâmetro não reatribui o nome do chamador, enquanto mutar um objeto mutável compartilhado pode ser visível pelos dois nomes.

```python
from copy import copy, deepcopy

original = {"steps": ["draft"]}
alias = original
shallow = copy(original)
deep = deepcopy(original)
shallow["steps"].append("review")
print(original == shallow, original is shallow)
print(alias is original, deep["steps"])
```

A saída é `True False`, depois `True ['draft']`. Cópia rasa cria outro dicionário externo, mas compartilha a lista interna. Cópia profunda copia recursivamente componentes suportados; seu memo rastreia objetos já copiados, incluindo ciclos e referências repetidas. Não garante novo objeto para cada componente (imutáveis podem ser compartilhados), nem clona recursos externos. Classes personalizadas podem controlar a cópia.

## Igualdade e hashing

Objetos hashable devem ter hash estável e objetos iguais devem ter hashes iguais. Objetos diferentes podem colidir. Listas e dicionários não são hashable; uma tupla é hashable somente se seus elementos forem hashable. Se implementar igualdade por valor numa classe mutável, usá-la como chave pode quebrar a busca se seu hash mudar. Python normalmente torna a classe não hashable quando define `__eq__` sem `__hash__`.

## Prática

Execute o exemplo compartilhado. Faça duas chaves referenciarem a mesma lista e confira que a cópia profunda preserva essa relação interna, separando-a do original. Experimente cópia rasa primeiro. Prefira não copiar para compartilhamento intencional, cópia rasa para estrutura externa independente e cópia profunda apenas quando o contrato de ownership aninhado exigir; copiar grafos grandes custa tempo e memória.

**Referência rápida:** alias compartilha; rasa copia contêiner; profunda copia grafo suportado; igualdade não é identidade.

## Exemplo executável compartilhado

[copy_plan.py](examples/copy_plan.py)

`python technical-interview-preparation/09-object-identity-references-and-copying/examples/copy_plan.py`

## Referências oficiais (Python 3.13)

- [Python 3.13: reference/datamodel.html](https://docs.python.org/3.13/reference/datamodel.html)
- [Python 3.13: library/copy.html](https://docs.python.org/3.13/library/copy.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../08-encapsulation-abstraction-and-solid/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../10-python-memory-management/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
