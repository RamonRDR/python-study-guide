<div align="center">

# Contêineres Especializados e Contratos de Coleções

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Standard Library](../README.pt-BR.md) · [← Capítulo anterior: Logging](../05-logging/README.pt-BR.md)

A Fase 3 apresentou os quatro modelos de coleções de uso geral: `list`, `tuple`, `dict` e `set`. Este capítulo não substitui esses tipos embutidos. Ele estuda o módulo `collections` como um conjunto de contêineres especializados para situações em que as **operações necessárias** são mais específicas do que o modelo de uma coleção genérica.

A pergunta central é:

```text
Qual comportamento a estrutura de dados está prometendo,
e esse comportamento combina com as operações que meu programa executa com mais frequência?
```

Um contêiner especializado é útil quando sua semântica deixa a intenção mais clara, reduz controle manual ou oferece um contrato de desempenho melhor para um padrão específico de acesso.

**Tempo estimado de estudo:** 150–190 minutos.

**Requisito de Python:** Python 3.10 ou mais recente para o conteúdo principal e os exemplos executáveis. Notas sensíveis à versão identificam mudanças posteriores quando forem relevantes.

**Base de documentação:** os comportamentos e as notas de versão foram conferidos na documentação oficial do Python 3.14 para `collections`, `collections.abc` e `typing`.

## Objetivos de aprendizagem

Ao final deste capítulo, você deve conseguir:

- explicar por que `collections` complementa, em vez de substituir, os contêineres embutidos;
- usar `Counter` como abstração de contagem e multiconjunto;
- raciocinar sobre contagens zero, negativas e ausentes em um `Counter`;
- usar `defaultdict` sem criar chaves acidentalmente durante leituras;
- escolher `deque` para operações eficientes nas duas extremidades e janelas de histórico limitadas;
- explicar a diferença entre acesso nas extremidades de um deque e indexação no meio;
- usar `namedtuple()` quando compatibilidade com tupla e campos nomeados forem úteis ao mesmo tempo;
- distinguir os casos de uso de `namedtuple()`, `typing.NamedTuple` e `dataclass`;
- usar `ChainMap` para mapear camadas sem copiá-las antecipadamente;
- entender por que `ChainMap` lê ao longo de toda a cadeia, mas escreve apenas no primeiro mapeamento;
- explicar quando `OrderedDict` ainda oferece comportamentos que um `dict` comum não expressa tão diretamente;
- reconhecer `UserDict`, `UserList` e `UserString` como bases de extensão orientadas a wrappers;
- usar `collections.abc` para raciocinar sobre interfaces de coleção, e não apenas implementações concretas;
- escolher contêineres especializados pela semântica e pelo padrão de acesso, e não pela novidade.

## 1. O que este capítulo acrescenta depois da Fase 3

A Fase 3 ensinou as estruturas centrais:

```python
items = ["alpha", "beta"]
point = (10, 20)
settings = {"mode": "safe"}
tags = {"python", "study"}
```

Essas estruturas continuam sendo as escolhas padrão para a maioria dos programas.

O módulo `collections` se torna útil quando o programa precisa de um contrato mais específico:

```text
contar valores repetidos                    -> Counter
criar valores ausentes por meio de factory  -> defaultdict
adicionar/remover com eficiência nas pontas -> deque
sobrepor mapeamentos sem copiar             -> ChainMap
manter comportamento de tupla com campos    -> namedtuple
reordenar chaves de mapeamento de propósito -> OrderedDict
estender coleções por wrappers               -> UserDict/UserList/UserString
raciocinar sobre interfaces                  -> collections.abc
```

O objetivo não é decorar nomes incomuns. É reconhecer o padrão de operações que torna uma estrutura mais adequada do que outra.

## 2. Comece pelo contrato de operações

A escolha de uma estrutura de dados deve responder perguntas como:

- A consulta é feita por chave ou por posição?
- Um valor ausente significa erro, zero ou criação de um padrão?
- As escritas se concentram em uma extremidade, nas duas ou em posições aleatórias?
- A estrutura é uma cópia estática ou uma visão viva sobre outros mapeamentos?
- A ordem afeta igualdade ou apenas iteração?
- O objeto precisa continuar compatível com tuplas?

Se um tipo embutido já comunica o contrato pretendido com clareza, prefira o tipo embutido.

A especialização é útil quando reduz ambiguidade.

## 3. Importe apenas o que torna o design mais claro

Um estilo comum é importar os nomes específicos usados pelo módulo:

```python
from collections import ChainMap, Counter, defaultdict, deque, namedtuple
```

Para interfaces abstratas, importe do submódulo dedicado:

```python
from collections.abc import Iterable, Mapping, Sequence
```

`collections.abc` está relacionado a `collections`, mas serve a outro propósito: interfaces e protocolos, não armazenamento especializado concreto.

# Parte I: `Counter`

## 4. `Counter` modela contagens

`Counter` é uma subclasse de `dict` projetada em torno da contagem de objetos hasheáveis.

```python
from collections import Counter

counts = Counter(["ok", "ok", "retry", "ok", "failed"])
print(counts)
```

Uma representação típica é:

```text
Counter({'ok': 3, 'retry': 1, 'failed': 1})
```

As chaves são os elementos contados e os valores são suas contagens.

## 5. Construa um `Counter` a partir de elementos, mapeamentos ou argumentos nomeados

```python
from collections import Counter

from_elements = Counter("banana")
from_mapping = Counter({"red": 3, "blue": 1})
from_keywords = Counter(red=3, blue=1)
```

A primeira forma conta ocorrências. As formas com mapeamento e argumentos nomeados tratam os valores fornecidos como contagens.

## 6. Uma chave ausente tem contagem zero

Diferentemente de uma consulta em dicionário comum, uma chave ausente de `Counter` retorna `0`:

```python
from collections import Counter

counts = Counter({"ready": 4})
print(counts["missing"])
```

Saída:

```text
0
```

Isso facilita contagens incrementais porque o código não precisa inicializar cada chave possível antes.

## 7. Contagem zero não é o mesmo que entrada ausente

Atribuir zero não exclui a chave:

```python
from collections import Counter

counts = Counter(a=2)
counts["a"] = 0

print("a" in counts)
del counts["a"]
print("a" in counts)
```

Saída:

```text
True
False
```

Essa diferença importa ao inspecionar chaves ou serializar o contador.

## 8. `total()` soma todas as contagens

O Python 3.10 adicionou `Counter.total()`:

```python
from collections import Counter

counts = Counter(success=8, retry=2, failed=1)
print(counts.total())
```

Saída:

```text
11
```

O total considera as contagens numéricas como armazenadas, inclusive valores negativos quando existirem.

## 9. `most_common()` preserva a ordem de primeira aparição nos empates

```python
from collections import Counter

counts = Counter(["b", "a", "b", "a", "c"])
print(counts.most_common())
```

Elementos com a mesma contagem mantêm a ordem em que apareceram pela primeira vez.

Não trate empates silenciosamente como ordem alfabética, a menos que seu programa faça essa ordenação explicitamente depois.

## 10. `Counter.update()` soma contagens

`Counter.update()` não se comporta como `dict.update()`.

```python
from collections import Counter

counts = Counter(a=2)
counts.update(a=3, b=1)
print(counts)
```

O resultado contém `a=5`, e não `a=3`.

Essa é uma operação de contagem, não uma substituição de valor.

## 11. `subtract()` mantém resultados com sinal

```python
from collections import Counter

balance = Counter(apples=5, pears=1)
balance.subtract(apples=2, pears=3)
print(balance)
```

`Counter` permite contagens zero e negativas. Isso é útil para deltas, saldos e cálculos intermediários.

## 12. Aritmética de multiconjuntos filtra resultados não positivos

Os operadores aritméticos têm um contrato de saída diferente de `subtract()`:

```python
from collections import Counter

required = Counter(a=4, b=2)
actual = Counter(a=1, b=5)

print(required - actual)
print(required + actual)
print(required & actual)
print(required | actual)
```

Nessas operações de multiconjunto, o resultado exclui contagens iguais ou menores que zero.

Isso torna a subtração conveniente para perguntas como "o que ainda está faltando?".

## 13. `+` e `-` unários normalizam counters com sinal

```python
from collections import Counter

counts = Counter(a=3, b=0, c=-2)
print(+counts)
print(-counts)
```

O `+` unário mantém contagens positivas. O `-` unário mantém as magnitudes positivas das contagens negativas.

Isso pode ser mais claro do que filtrar manualmente um counter com sinais.

## 14. Comparações de Counter tratam contagens ausentes como zero

Desde o Python 3.10, comparações ricas suportam igualdade e relações de inclusão de multiconjuntos.

```python
from collections import Counter

left = Counter(a=1)
right = Counter(a=1, b=0)

print(left == right)
```

Saída:

```text
True
```

Um elemento ausente é tratado como se tivesse contagem zero nessas comparações.

## 15. Valores de Counter não estão limitados a inteiros positivos

A classe em si não exige apenas contagens inteiras positivas. Muitas operações aceitam outros valores numéricos.

Entretanto, cada método possui seu próprio contrato. Por exemplo, `elements()` exige contagens que possam ser interpretadas como repetições e ignora contagens abaixo de um.

Não suponha que todo método de `Counter` aceite tipos numéricos arbitrários da mesma forma.

## 16. Use `dict` comum quando você não estiver contando

Se o valor associado a uma chave for um estado, objeto, timestamp, configuração ou registro arbitrário em vez de uma contagem, um dicionário comum normalmente comunica melhor a intenção.

`Counter` deve responder uma pergunta de contagem ou multiconjunto.

# Parte II: `defaultdict`

## 17. `defaultdict` modela criação de valores ausentes

`defaultdict` é uma subclasse de `dict` com uma `default_factory`.

```python
from collections import defaultdict

groups = defaultdict(list)
groups["blue"].append("item-1")
print(groups)
```

Quando `groups["blue"]` não existe, `list()` é chamado, a nova lista é inserida e essa lista é retornada.

## 18. A factory é um callable, não um valor já criado

Correto:

```python
from collections import defaultdict

rows = defaultdict(list)
counts = defaultdict(int)
```

A factory é chamada quando necessária.

Passar `list()` em vez de `list` passaria uma lista já criada, e não o callable exigido como factory.

## 19. `__missing__()` é acionado por `__getitem__()`

O comportamento para valores ausentes está ligado à consulta por colchetes:

```python
from collections import defaultdict

values = defaultdict(list)
values["new"].append(1)
```

O caminho de `dict.__getitem__()` chama o método `__missing__()` da subclasse, que chama a factory quando apropriado.

## 20. `get()` não chama a default factory

Esse é um dos contratos mais importantes de `defaultdict`:

```python
from collections import defaultdict

values = defaultdict(list)

print(values.get("missing"))
print("missing" in values)
```

Saída:

```text
None
False
```

`get()` se comporta como `dict.get()` normal e não cria a chave.

## 21. Testes de pertencimento não criam chaves

```python
from collections import defaultdict

values = defaultdict(int)
print("x" in values)
print(values)
```

Um teste de pertencimento é apenas observacional. Ele não invoca a factory.

## 22. Leituras com colchetes podem alterar o mapeamento

Esta linha parece apenas uma leitura:

```python
value = values["missing"]
```

Com um `defaultdict`, ela também pode inserir `"missing"`.

Essa é uma diferença semântica em relação a um dicionário comum e uma fonte frequente de chaves acidentais.

Se você quiser apenas inspecionar sem criar, use testes de pertencimento ou `get()` conforme apropriado.

## 23. `defaultdict(list)` é uma ferramenta natural de agrupamento

```python
from collections import defaultdict

by_category = defaultdict(list)

for category, value in [("a", 1), ("b", 2), ("a", 3)]:
    by_category[category].append(value)

print(dict(by_category))
```

Isso evita repetir uma lógica de inicialização quando a chave ainda não existe.

## 24. `defaultdict(int)` é útil para contagens simples

```python
from collections import defaultdict

counts = defaultdict(int)

for word in ["red", "blue", "red"]:
    counts[word] += 1
```

Para frequência pura, `Counter` normalmente expressa o objetivo de forma mais direta. `defaultdict(int)` continua útil quando contar é apenas uma parte de um fluxo maior de mapeamento.

## 25. Factories podem representar padrões mais ricos

```python
from collections import defaultdict


def new_state() -> dict[str, int]:
    return {"attempts": 0, "successes": 0}


state = defaultdict(new_state)
state["worker-a"]["attempts"] += 1
```

Use uma factory nomeada quando a política de inicialização merecer um nome ou for mais complexa do que um construtor embutido.

## 26. Operadores de merge não significam "executar a factory"

`defaultdict` suporta os operadores de merge de mapeamentos introduzidos para dicionários.

O merge combina o conteúdo dos mapeamentos. A criação de chave ausente continua acontecendo somente pelo caminho normal de `default_factory` / `__missing__()`.

Não confunda comportamento de merge com comportamento de valor ausente.

# Parte III: `deque`

## 27. `deque` é uma fila de duas extremidades

Um `deque` suporta adições e remoções eficientes nas duas extremidades.

```python
from collections import deque

queue = deque(["a", "b"])
queue.append("c")
print(queue.popleft())
```

É a estrutura da biblioteca padrão indicada quando as duas extremidades participam ativamente do algoritmo.

## 28. Operações nas extremidades são aproximadamente O(1)

A documentação oficial descreve adições e remoções em ambos os lados como aproximadamente O(1).

Por contraste, remover o primeiro elemento de uma lista com `pop(0)` exige deslocar os elementos restantes e é O(n).

Para filas FIFO, prefira:

```python
from collections import deque

queue = deque()
queue.append("job-1")
job = queue.popleft()
```

em vez de usar repetidamente `list.pop(0)`.

## 29. `maxlen` cria uma janela de histórico limitada

```python
from collections import deque

recent = deque(maxlen=3)

for value in [10, 20, 30, 40, 50]:
    recent.append(value)

print(list(recent))
```

Saída:

```text
[30, 40, 50]
```

Depois que fica cheio, adicionar em uma extremidade descarta itens da extremidade oposta.

## 30. A expulsão de `append()` em deque limitado difere de `insert()`

Um deque limitado e cheio aceita adições nas extremidades descartando da extremidade oposta.

Um `insert()` que faria o deque limitado ultrapassar `maxlen` levanta `IndexError`.

As duas operações possuem contratos diferentes de propósito.

## 31. `extendleft()` inverte a ordem de entrada

```python
from collections import deque

values = deque([4])
values.extendleft([1, 2, 3])
print(list(values))
```

Saída:

```text
[3, 2, 1, 4]
```

Cada elemento é adicionado à esquerda em sequência, portanto o iterável aparece em ordem invertida.

## 32. `rotate()` desloca as extremidades lógicas

```python
from collections import deque

values = deque([1, 2, 3, 4])
values.rotate(1)
print(list(values))
values.rotate(-2)
print(list(values))
```

Valores positivos rotacionam para a direita; negativos, para a esquerda.

Isso é útil em escalonamento cíclico e algoritmos em que a frente atual muda repetidamente.

## 33. Indexação de deque não transforma a estrutura em substituta de list

O acesso indexado de deque é O(1) próximo às duas extremidades, mas fica O(n) em direção ao meio.

Se a operação dominante for acesso posicional aleatório, uma lista normalmente é mais adequada.

Use deque por causa do comportamento nas extremidades, e não apenas porque ele aceita `d[index]`.

## 34. Operações thread-safe nas extremidades não são um modelo completo de transação

A documentação oficial descreve as adições e remoções de deque como thread-safe.

Isso não significa que uma sequência de várias operações se torne automaticamente uma transação atômica de negócio.

Por exemplo, um fluxo de "verificar, depois remover, depois atualizar outra estrutura" ainda pode exigir sincronização explícita se várias threads precisarem observar toda a sequência de forma consistente.

Use a garantia restrita pelo que ela realmente promete, e não como substituta de um design de concorrência.

## 35. Remoções em deque vazio levantam `IndexError`

```python
from collections import deque

queue = deque()

try:
    queue.popleft()
except IndexError:
    print("queue is empty")
```

Defina em seu próprio contrato de aplicação se uma fila vazia é um ramo esperado ou uma condição excepcional.

# Parte IV: `namedtuple()`

## 36. `namedtuple()` dá nomes às posições de uma tupla

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
point = Point(10, 20)

print(point.x)
print(point[0])
```

O objeto continua semelhante a uma tupla: indexável, iterável, desempacotável e imutável no sentido de uma tupla.

Os campos nomeados melhoram a legibilidade quando as posições possuem significados estáveis.

## 37. A factory cria uma nova subclasse de tuple

`namedtuple()` não cria apenas um registro. Ela cria uma classe.

```python
from collections import namedtuple

Coordinate = namedtuple("Coordinate", "latitude longitude")
a = Coordinate(10.0, 20.0)
b = Coordinate(30.0, 40.0)
```

`Coordinate` é a subclasse de tupla gerada; `a` e `b` são instâncias.

## 38. Defaults são aplicados aos campos mais à direita

```python
from collections import namedtuple

Account = namedtuple("Account", ["name", "active"], defaults=[True])
print(Account("demo"))
```

Um campo com valor padrão não pode anteceder um campo obrigatório na assinatura gerada.

## 39. `rename=True` corrige nomes de campo inválidos ou duplicados

```python
from collections import namedtuple

Row = namedtuple("Row", ["name", "class", "name"], rename=True)
print(Row._fields)
```

Use isso quando os nomes de campo vierem de um esquema externo que você não controla totalmente.

Quando você controla o esquema, nomes válidos explícitos normalmente são mais claros do que depender de renomeação automática.

## 40. Named tuples são registros imutáveis

Você não pode atribuir diretamente a um campo:

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
point = Point(1, 2)

updated = point._replace(x=10)
print(updated)
```

`_replace()` retorna uma nova instância.

A partir do Python 3.13, argumentos nomeados inválidos passados a `_replace()` levantam `TypeError` em vez de `ValueError`.

## 41. `_asdict()` retorna um dicionário comum

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
point = Point(1, 2)
print(point._asdict())
```

Desde o Python 3.8, `_asdict()` retorna um `dict` normal, não um `OrderedDict`.

## 42. `_fields` e `_field_defaults` dão suporte à introspecção

```python
from collections import namedtuple

Record = namedtuple("Record", "key enabled", defaults=[False])
print(Record._fields)
print(Record._field_defaults)
```

Os underscores iniciais fazem parte da API de named tuples e existem para reduzir colisões com nomes de campos do usuário.

## 43. Vincule a classe gerada ao nome do tipo quando pickle for importante

A documentação oficial recomenda atribuir a classe gerada a uma variável com o mesmo nome de `typename` quando o suporte a pickle for relevante:

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
```

A geração dinâmica de classes pode interagir com serialização e importabilidade. Para tipos de registro reutilizáveis, prefira definições no nível do módulo.

## 44. `typing.NamedTuple` é a alternativa tipada

Quando anotações estáticas dos campos forem centrais ao design, `typing.NamedTuple` com sintaxe de classe normalmente é mais claro:

```python
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int
```

Ele preserva semântica de tupla enquanto expressa diretamente os tipos dos campos.

## 45. Uma dataclass não é apenas uma named tuple mais nova

Escolha pela semântica:

```text
precisa compatibilidade com tuple, indexação e unpacking -> namedtuple / NamedTuple
precisa classe orientada a registros com métodos gerados e semântica flexível -> dataclass
```

Não migre automaticamente apenas porque as duas ferramentas criam objetos compactos semelhantes a registros.

# Parte V: `ChainMap`

## 46. `ChainMap` cria uma visão viva sobre mapeamentos

```python
from collections import ChainMap

defaults = {"mode": "safe", "retries": 2}
overrides = {"mode": "fast"}

config = ChainMap(overrides, defaults)
print(config["mode"])
print(config["retries"])
```

As consultas percorrem os mapeamentos do primeiro ao último até encontrar a chave.

## 47. ChainMap mantém referências aos mapeamentos

```python
from collections import ChainMap

base = {"region": "global"}
config = ChainMap({}, base)

base["region"] = "test"
print(config["region"])
```

Saída:

```text
test
```

Um `ChainMap` não é uma cópia achatada criada antecipadamente. Alterações nos mapeamentos subjacentes continuam visíveis.

## 48. Escritas e exclusões atingem apenas o primeiro mapeamento

```python
from collections import ChainMap

local = {}
defaults = {"retries": 3}
config = ChainMap(local, defaults)

config["retries"] = 1
print(local)
print(defaults)
```

Saída:

```text
{'retries': 1}
{'retries': 3}
```

Precedência de leitura e destino de escrita são assimétricos de propósito.

## 49. `new_child()` cria uma nova camada frontal gravável

```python
from collections import ChainMap

base = ChainMap({"mode": "safe"})
child = base.new_child({"mode": "fast"})

print(child["mode"])
print(base["mode"])
```

Isso modela naturalmente escopos aninhados e camadas temporárias de override.

## 50. `parents` ignora o primeiro mapeamento

`chain.parents` retorna um novo `ChainMap` sobre todos os mapeamentos exceto o primeiro.

Isso é útil quando a primeira camada representa o escopo local atual e você precisa da visão envolvente.

## 51. Ordem de iteração não é ordem de consulta

As consultas procuram do primeiro ao último mapeamento.

A ordem de iteração é determinada examinando os mapeamentos do último para o primeiro com semântica de sobrescrita de mapeamento.

Isso pode surpreender código que pressupõe que "primeiro consultado" também significa "primeiro iterado".

Teste o contrato do qual seu programa realmente depende.

## 52. Achate explicitamente quando precisar de uma cópia estática

```python
from collections import ChainMap

config = ChainMap({"mode": "fast"}, {"mode": "safe", "retries": 2})
snapshot = dict(config)
```

O dicionário comum é independente como uma cópia dos valores resolvidos naquele momento.

Use `ChainMap` quando a sobreposição viva for a característica desejada. Use um dicionário combinado quando a característica desejada for uma cópia resolvida independente.

# Parte VI: `OrderedDict`

## 53. Dicionários comuns já preservam ordem de inserção

A ordem de inserção é garantida para dicionários comuns desde o Python 3.7.

Portanto, "preciso manter as chaves na ordem de inserção" normalmente **não** é motivo suficiente para escolher `OrderedDict` atualmente.

## 54. `OrderedDict` é especializado em reordenação

Ele ainda oferece comportamentos projetados para manipular a ordem de propósito:

```python
from collections import OrderedDict

items = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
items.move_to_end("a")
items.move_to_end("c", last=False)
print(list(items))
```

Reordenar frequentemente as extremidades é uma das razões que ainda justificam considerá-lo.

## 55. Igualdade de `OrderedDict` pode ser sensível à ordem

Dois objetos `OrderedDict` são iguais apenas quando seus pares chave-valor e sua ordem coincidem.

Igualdade entre dicionários comuns ignora a ordem de inserção.

Essa diferença semântica importa quando a ordem faz parte do contrato do valor, e não apenas da apresentação.

## 56. `popitem(last=False)` expressa remoção FIFO diretamente

`OrderedDict.popitem()` aceita `last=True` ou `last=False`.

O `popitem()` de um dict comum remove o item inserido mais recentemente. `OrderedDict` possui uma API direta para escolher qualquer extremidade.

Se você não precisa dessas semânticas especializadas de reordenação, prefira um dicionário comum.

# Parte VII: Wrappers de extensão e interfaces de coleção

## 57. `UserDict`, `UserList` e `UserString` envolvem tipos embutidos

Essas classes oferecem bases orientadas a wrappers cujo conteúdo subjacente fica disponível por `.data`.

```python
from collections import UserDict


class NormalizedKeys(UserDict):
    def __setitem__(self, key: str, value: object) -> None:
        super().__setitem__(key.strip().lower(), value)
```

Elas podem ser mais fáceis de estender de forma consistente do que herdar diretamente de um tipo embutido quando você quer interceptar muitas operações por meio de uma abstração controlada de wrapper.

## 58. Bases wrapper são uma escolha de design, não uma obrigação

O Python moderno permite herança direta de `dict`, `list` e `str` em muitas situações.

As classes `User*` continuam úteis quando o acesso ao contêiner `.data` e seu modelo de extensão tornam a customização mais simples.

Prefira composição ou uma classe específica quando seu objeto não for conceitualmente uma coleção de uso geral.

## 59. `collections.abc` modela interfaces

```python
from collections.abc import Mapping, Sequence

print(isinstance({"a": 1}, Mapping))
print(isinstance([1, 2, 3], Sequence))
```

ABCs permitem que o código pergunte "este objeto satisfaz uma interface semelhante a mapping/sequence?" em vez de "este objeto é exatamente um dict/list?".

Isso favorece APIs mais flexíveis.

## 60. Testes com `Iterable` possuem uma limitação importante

`isinstance(obj, Iterable)` reconhece iteráveis registrados e objetos com `__iter__()`.

Ele não detecta de forma confiável todo objeto legado que consegue iterar por meio de `__getitem__()`.

A documentação oficial afirma que a única forma confiável de determinar se um objeto é iterável é chamar `iter(obj)` e tratar a falha.

## 61. Mixins de ABC podem ter consequências de desempenho

Alguns métodos mixin de `Sequence` chamam `__getitem__()` repetidamente.

Se uma sequência customizada implementar `__getitem__()` em O(n), mixins herdados como iteração podem chegar a O(n²).

Uma interface pode fornecer comportamento correto e ainda ter o contrato de desempenho errado para uma implementação específica.

# Escolhendo e combinando as ferramentas

## 62. Tabela de decisão

| Necessidade | Prefira | Motivo principal |
|---|---|---|
| Contar valores hasheáveis | `Counter` | Semântica de contagem e multiconjunto |
| Agrupar/criar valores ausentes | `defaultdict` | Política de chave ausente baseada em factory |
| Fila FIFO ou operações nas duas pontas | `deque` | Operações eficientes nas extremidades |
| Manter apenas os N valores mais recentes | `deque(maxlen=N)` | Expulsão automática da extremidade oposta |
| Registro compatível com tuple e campos nomeados | `namedtuple` / `NamedTuple` | Campos nomeados mais semântica de tupla |
| Sobrepor mapeamentos com precedência viva | `ChainMap` | Visão em vez de merge antecipado |
| Reordenação frequente de mapeamento | `OrderedDict` | API orientada a reordenação |
| Estender coleção por comportamento wrapper | `UserDict` / `UserList` / `UserString` | `.data` subjacente controlado |
| Aceitar uma interface, não um tipo concreto | `collections.abc` | Design orientado a protocolos |

## 63. Combine estruturas especializadas apenas quando cada uma tiver um papel

Um programa pode legitimamente usar:

```text
Counter      -> resumir frequências
deque        -> manter eventos recentes
ChainMap     -> resolver configuração em camadas
```

Isso não significa que toda estrutura de dados do programa deve vir de `collections`.

A especialização deve simplificar o modelo, não decorá-lo com tipos pouco familiares.

## 64. Erros comuns

### Usar `Counter` como dicionário genérico

Se os valores não forem contagens, use um mapeamento adequado para valores arbitrários.

### Presumir que `Counter.update()` substitui valores

Ele soma contagens.

### Presumir que valor zero em `Counter` remove a chave

Use `del` se a chave precisar desaparecer.

### Ler `defaultdict[key]` apenas para verificar se uma chave existe

Isso pode criar a chave.

### Esperar que `defaultdict.get()` invoque a factory

Ele não invoca.

### Usar `list.pop(0)` para uma fila FIFO duradoura

Use `deque.popleft()` quando a fila cresce e diminui pela frente.

### Tratar indexação no meio de deque como O(1)

Use listas para acesso posicional aleatório rápido.

### Presumir que `extendleft()` preserva a ordem do iterável

Ele inverte a ordem visível.

### Esperar que escritas em `ChainMap` atualizem o mapeamento em que a chave foi encontrada

As escritas vão apenas para o primeiro mapeamento.

### Usar `OrderedDict` apenas porque dicionários precisam preservar ordem de inserção

Dicionários comuns já preservam.

## 65. Exemplo prático: reconciliação de capacidade com `Counter`

```python
from collections import Counter

required = Counter({"sensor": 4, "cable": 3, "case": 2})
packed = Counter({"sensor": 4, "cable": 1, "case": 3})

missing = required - packed
surplus = packed - required

print(f"required units: {required.total()}")
print(f"missing: {dict(missing)}")
print(f"surplus: {dict(surplus)}")
```

Saída esperada:

```text
required units: 9
missing: {'cable': 2}
surplus: {'case': 1}
```

O modelo de dados comunica que esses mapeamentos representam quantidades, e não estado arbitrário de chave-valor.

## 66. Exemplo prático: agrupamento com `defaultdict`

```python
from collections import defaultdict

records = [
    ("billing", "INV-101"),
    ("support", "REQ-203"),
    ("billing", "INV-102"),
]

by_team = defaultdict(list)

for team, reference in records:
    by_team[team].append(reference)
```

A factory remove boilerplate de inicialização enquanto mantém visível a intenção de agrupamento.

## 67. Exemplo prático: histórico recente com deque limitado

```python
from collections import deque

recent = deque(maxlen=3)

for event in ["boot", "load-config", "connect", "ready"]:
    recent.append(event)

print(list(recent))
```

Saída esperada:

```text
['load-config', 'connect', 'ready']
```

Nenhum ramo explícito do tipo "se estiver cheio, remova o mais antigo" é necessário.

## 68. Exemplo prático: precedência de configuração com `ChainMap`

```python
from collections import ChainMap

defaults = {"mode": "safe", "retries": 2}
environment = {"retries": 4}
command_line = {"mode": "fast"}

config = ChainMap(command_line, environment, defaults)

print(config["mode"])
print(config["retries"])
```

Saída esperada:

```text
fast
4
```

A cadeia preserva as camadas originais enquanto oferece uma única visão de consulta.

## 69. Exercício

Construa uma pequena simulação de processamento de tarefas com estes requisitos:

1. As categorias de tarefas recebidas devem ser contadas.
2. As tarefas aguardando execução devem suportar remoção FIFO pela esquerda.
3. Apenas os cinco IDs de tarefas concluídas mais recentes devem ser mantidos.
4. A configuração deve ser resolvida a partir dos mapeamentos `runtime`, depois `environment`, depois `defaults`, sem copiá-los para um único dicionário.
5. O programa deve imprimir:
   - total de tarefas recebidas;
   - contagem por categoria;
   - ordem em que as tarefas são processadas;
   - histórico de conclusões retido;
   - limite de tentativas resolvido.

Ferramentas sugeridas:

```text
Counter
deque
ChainMap
```

Não use um contêiner especializado apenas porque ele aparece na lista. Explique em comentários ou notas por que cada estrutura escolhida combina com as operações exigidas.

## 70. Referência rápida

```python
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple

Counter(iterable)
Counter(mapping)
counter.total()
counter.most_common(n)
counter.update(...)
counter.subtract(...)
+counter
-counter

defaultdict(list)
defaultdict(int)
mapping.default_factory

deque(iterable)
deque(iterable, maxlen=n)
d.append(value)
d.appendleft(value)
d.pop()
d.popleft()
d.extend(values)
d.extendleft(values)
d.rotate(n)

Record = namedtuple("Record", "field_a field_b")
record._asdict()
record._replace(field_a=value)
Record._fields
Record._field_defaults

ChainMap(front, fallback)
chain.maps
chain.new_child()
chain.parents

ordered.move_to_end(key, last=True)
ordered.popitem(last=False)
```

## 71. Checklist de design

Antes de escolher uma coleção especializada, pergunte:

- Qual operação domina este fluxo?
- O que um valor ausente deve significar?
- A estrutura pode sofrer mutação durante uma leitura?
- Desempenho nas extremidades é importante?
- A ordem faz parte da igualdade ou apenas da iteração?
- Preciso de uma visão viva ou de uma cópia estática?
- Compatibilidade com tuple importa?
- Um tipo embutido seria mais simples?
- Estou dependendo de comportamento específico de versão?
- Testei as semânticas importantes, e não apenas a saída do caminho feliz?

## 72. Conexões com outros conceitos de Python

`collections` se conecta diretamente aos tópicos já estudados:

- **Coleções da Fase 3:** contêineres especializados constroem sobre os modelos mentais de listas, tuplas, dicionários e conjuntos.
- **Loops:** `Counter`, agrupamentos, filas e históricos limitados normalmente processam iteráveis incrementalmente.
- **Funções:** factories passadas a `defaultdict` são políticas chamáveis.
- **Type hints:** `typing.NamedTuple` e interfaces genéricas de coleção tornam contratos de dados explícitos.
- **Programação orientada a objetos:** wrappers `User*` e ABCs mostram diferentes modelos de extensão.
- **Algoritmos:** a escolha entre operações na frente de uma list e nas extremidades de deque altera a complexidade.
- **Design de configuração:** `ChainMap` modela precedência sem achatar as camadas de origem.
- **Testes:** semânticas como criação de chave ausente, igualdade sensível à ordem e expulsão em estrutura limitada merecem testes comportamentais.

## Referências

Referências primárias usadas neste capítulo:

- [Documentação Python 3.14: `collections` — tipos de dados de contêineres](https://docs.python.org/3.14/library/collections.html)
- [Documentação Python 3.14: `collections.abc` — classes base abstratas para contêineres](https://docs.python.org/3.14/library/collections.abc.html)
- [Documentação Python 3.14: `typing.NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple)
- [Tutorial Python 3.14: estruturas de dados, incluindo orientação de deque para filas](https://docs.python.org/3.14/tutorial/datastructures.html#using-lists-as-queues)

## Próximo capítulo

Continue com o [Capítulo 07: `itertools`](../07-itertools/README.pt-BR.md).

O próximo capítulo muda de **contêineres** especializados para **pipelines de iteradores** especializados: compondo transformações lazy, repetição, recorte, agrupamento e iteração combinatória sem criar coleções intermediárias desnecessárias.
