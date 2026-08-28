<div align="center">

# Projetando Pipelines Lazy de Iteradores com `itertools`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Standard Library](../README.pt-BR.md) · [← Capítulo anterior: Collections](../06-collections/README.pt-BR.md)

Capítulos anteriores introduziram `for`, iteráveis, a diferença básica entre iterable e iterator e helpers como `range()`, `enumerate()` e `zip()`. Este capítulo avança: estuda `itertools` como uma caixa de ferramentas para compor **pipelines lazy de iteradores** com contratos explícitos de consumo, buffering, agrupamento e combinatória.

A pergunta central é:

```text
Can this transformation be expressed as a stream of values
without materializing every intermediate collection?
```

`itertools` é poderoso porque suas funções retornam iteradores. Isso pode reduzir o uso de memória intermediária e tornar o fluxo de dados mais preciso, mas também significa que a ordem de consumo importa.

**Tempo estimado de estudo:** 170–220 minutos.

**Requisito de Python:** Python 3.10 ou mais recente para o conteúdo central e os exemplos executáveis. Seções sensíveis à versão identificam `batched()` (3.12) e `batched(strict=...)` (3.13).

**Base documental:** comportamentos e notas de versão foram conferidos na documentação oficial do Python 3.14 para `itertools` e no Functional Programming HOWTO.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar por que `itertools` é uma caixa de ferramentas de álgebra de iteradores, e não um módulo de coleções;
- distinguir construção lazy de pipeline de materialização eager;
- raciocinar sobre consumo single-pass de iteradores;
- combinar streams com `chain()` e `chain.from_iterable()`;
- agrupar entradas finitas em lotes e entender os requisitos de versão de `batched(strict=...)`;
- recortar streams com `islice()` sem assumir semântica de sequência;
- comparar elementos vizinhos com `pairwise()`;
- selecionar elementos com `compress()`, `filterfalse()`, `dropwhile()` e `takewhile()`;
- construir estado acumulado com `accumulate()`;
- aplicar tuplas de argumentos pré-agrupadas com `starmap()`;
- limitar iteradores infinitos como `count()`, `cycle()` e `repeat()`;
- alinhar streams de comprimentos diferentes com `zip_longest()`;
- entender buffering e limitações de thread safety de `tee()`;
- usar `groupby()` para runs consecutivos, em vez de agrupamento global no estilo SQL;
- estimar o crescimento de `product()`, `permutations()` e combinations antes de consumi-los;
- testar pipelines de iteradores sem esconder acidentalmente bugs de consumo.

## 1. O que este capítulo acrescenta após os capítulos anteriores de iteração

Os capítulos anteriores já estabeleceram:

```text
for item in iterable
range() -> numeric progression
enumerate() -> position + item
zip() -> parallel items
```

Este capítulo acrescenta um modelo mais composicional:

```text
source
  -> transform lazily
  -> select lazily
  -> combine lazily
  -> consume at an intentional boundary
```

O objetivo não é substituir loops legíveis. É reconhecer quando um pipeline expressa o fluxo de dados de forma mais direta.

## 2. Funções de `itertools` constroem iteradores

A documentação oficial descreve o módulo como um conjunto de building blocks de iteradores rápidos e eficientes em memória.

```python
from itertools import islice

numbers = iter(range(100))
first_five = islice(numbers, 5)

print(type(first_five))
```

`islice()` não retorna uma lista. Ele retorna um iterador que produz valores quando é consumido.

## 3. Lazy não significa sem custo

Laziness normalmente significa que o trabalho é adiado até que a iteração peça um valor.

```python
from itertools import chain

stream = chain([1, 2], [3, 4])
print(next(stream))
```

Apenas o trabalho necessário para fornecer o valor solicitado é realizado.

Mesmo assim, pipelines lazy podem:

- consumir CPU;
- reter valores em buffer;
- manter referências a objetos;
- materializar dados posteriormente em um consumidor;
- tornar-se infinitos.

"Lazy" descreve o momento da avaliação, não custo zero.

## 4. Iteradores normalmente são single-pass

```python
values = iter([10, 20, 30])

print(list(values))
print(list(values))
```

Saída:

```text
[10, 20, 30]
[]
```

A primeira conversão esgota o iterador. A segunda não encontra valores restantes.

Esse modelo de consumo é central em `itertools`.

## 5. Escolha deliberadamente a fronteira de materialização

Um pipeline útil costuma permanecer lazy até que o programa precise de um resultado concreto:

```python
from itertools import islice

stream = (number * number for number in range(1_000_000))
preview = list(islice(stream, 3))
print(preview)
```

Aqui, apenas o preview é materializado.

Materialize porque a próxima operação precisa de uma coleção, não apenas porque `list(...)` é familiar.

## 6. Importe as ferramentas que comunicam o pipeline

```python
from itertools import (
    accumulate,
    chain,
    combinations,
    groupby,
    islice,
    pairwise,
    product,
    tee,
    zip_longest,
)
```

Imports específicos deixam visível o vocabulário do pipeline.

# Parte I: compondo e moldando streams

## 7. `chain()` concatena iteráveis de forma lazy

```python
from itertools import chain

combined = chain(["a", "b"], ("c", "d"), "ef")
print(list(combined))
```

Saída:

```text
['a', 'b', 'c', 'd', 'e', 'f']
```

`chain()` consome o primeiro iterável, depois o próximo e assim por diante.

## 8. `chain()` não é um algoritmo de merge

`chain()` não ordena, remove duplicados, alinha ou compara entradas.

```text
input A -> all values
input B -> all values
input C -> all values
```

Se o requisito real for merge ordenado ou reconciliação por chave, escolha uma ferramenta que modele esse contrato.

## 9. `chain.from_iterable()` achata um nível

```python
from itertools import chain

pages = [[1, 2], [3], [4, 5]]
flattened = chain.from_iterable(pages)
print(list(flattened))
```

Saída:

```text
[1, 2, 3, 4, 5]
```

Ele achata um nível de iterable-of-iterables. Não é uma função recursiva para flattening de profundidade arbitrária.

## 10. `chain.from_iterable()` mantém a fonte externa lazy

O iterável externo também pode ser lazy:

```python
from itertools import chain

rows = ([number, number * 10] for number in range(3))
print(list(chain.from_iterable(rows)))
```

O próximo iterável interno é solicitado à medida que a chain avança.

## 11. `batched()` cria tuplas não sobrepostas

O Python 3.12 adicionou `itertools.batched()`:

```python
from itertools import batched

print(list(batched("ABCDEFG", 3)))
```

No Python 3.12+, o resultado é:

```text
[('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
```

O lote final pode ser menor que `n`.

## 12. `batched(strict=True)` transforma lotes completos em contrato

O Python 3.13 adicionou o parâmetro `strict`:

```python
from itertools import batched

print(list(batched([1, 2, 3, 4], 2, strict=True)))
```

Se o lote final estiver incompleto, `strict=True` lança `ValueError`.

Use modo estrito quando dados incompletos devem ser tratados como inválidos, e não como um lote menor válido.

## 13. `batched()` consome apenas o necessário para o próximo lote

A implementação é lazy em relação à entrada. Ela solicita valores suficientes para preencher a próxima tupla, entrega o lote e continua.

Isso torna batching adequado para streams em que construir uma lista completa antes seria desnecessário.

## 14. `islice()` recorta iteráveis, não sequências

```python
from itertools import islice

stream = iter(range(20))
print(list(islice(stream, 2, 10, 3)))
```

Saída:

```text
[2, 5, 8]
```

`islice()` expressa start, stop e step sobre iteração.

## 15. `islice()` não suporta índices negativos

Slicing de sequências pode trabalhar a partir do final porque uma sequência pode conhecer seu tamanho e oferecer acesso indexado.

Um iterador arbitrário pode nem ter final conhecido.

Por isso, `start` negativo, `stop` negativo e `step` não positivo não são suportados por `islice()`.

## 16. Recortar um stream avança a fonte

```python
from itertools import islice

source = iter([0, 1, 2, 3, 4, 5])
print(list(islice(source, 3)))
print(list(source))
```

Saída:

```text
[0, 1, 2]
[3, 4, 5]
```

`islice()` não copia o iterador de entrada. Ele o consome.

## 17. Um `islice()` com step ainda consome valores pulados

Se a entrada for um iterador, consumir completamente um `islice()` avança a entrada de acordo com os limites do slice, mesmo quando nem todo valor atravessado é entregue.

Isso importa quando outra parte do programa continua usando o mesmo iterador subjacente depois.

## 18. `pairwise()` expõe relações adjacentes

O Python 3.10 adicionou `pairwise()`:

```python
from itertools import pairwise

readings = [10, 15, 13, 18]
for previous, current in pairwise(readings):
    print(previous, current)
```

Saída:

```text
10 15
15 13
13 18
```

É ideal para transições, deltas, arestas e comparações adjacentes.

## 19. `pairwise()` produz um resultado a menos

Uma entrada com `n` valores produz `n - 1` pares quando `n >= 1`.

Entradas com menos de dois elementos não produzem pares.

Esse comportamento de fronteira deve fazer parte dos testes quando a quantidade de pares importa.

# Parte II: selecionando e parando

## 20. `compress()` aplica um stream de seletores Booleanos

```python
from itertools import compress

names = ["Ana", "Bo", "Cy", "Di"]
selected = [True, False, True, False]
print(list(compress(names, selected)))
```

Saída:

```text
['Ana', 'Cy']
```

Os iteráveis de dados e seletores avançam juntos.

## 21. `compress()` para quando qualquer entrada termina

Um stream de seletores menor trunca o resultado mesmo que ainda existam dados.

Esse é um contrato de alinhamento semelhante ao de `zip()`. Valide comprimentos separadamente se tamanhos diferentes representam entrada malformada.

## 22. `filterfalse()` mantém falhas do predicado

```python
from itertools import filterfalse

numbers = [1, 2, 3, 4, 5]
print(list(filterfalse(lambda value: value % 2 == 0, numbers)))
```

Saída:

```text
[1, 3, 5]
```

Ele é o contraponto de seleção inversa de `filter()`.

## 23. `dropwhile()` muda de comportamento após a primeira falha

```python
from itertools import dropwhile

values = [1, 2, 5, 2, 1]
print(list(dropwhile(lambda value: value < 4, values)))
```

Saída:

```text
[5, 2, 1]
```

Depois que o predicado se torna falso pela primeira vez, todos os elementos restantes são entregues sem filtragem adicional.

## 24. `dropwhile()` não é `filterfalse()`

Para o mesmo predicado:

```text
dropwhile -> discard only the leading matching prefix
filterfalse -> test every element and keep every failure
```

Os nomes representam formatos de stream diferentes.

## 25. `takewhile()` para na primeira falha

```python
from itertools import takewhile

values = [1, 2, 5, 2, 1]
print(list(takewhile(lambda value: value < 4, values)))
```

Saída:

```text
[1, 2]
```

Diferente de `filter()`, os valores após a primeira falha nunca são considerados por `takewhile()`.

## 26. `takewhile()` consome o primeiro elemento que falha

Este é um contrato sutil e importante.

```python
from itertools import takewhile

source = iter([1, 2, 5, 6])
print(list(takewhile(lambda value: value < 4, source)))
print(list(source))
```

Saída:

```text
[1, 2]
[6]
```

O `5` que falhou foi consumido para descobrir que o prefixo deveria terminar.

# Parte III: estado acumulado e aplicação de argumentos

## 27. `accumulate()` entrega resultados acumulados

```python
from itertools import accumulate

print(list(accumulate([2, 3, 4])))
```

Saída:

```text
[2, 5, 9]
```

A operação padrão é soma.

## 28. `accumulate()` difere de `sum()` e `reduce()`

```text
accumulate -> every running result
sum        -> final additive total
reduce     -> final accumulated result
```

Escolha de acordo com a necessidade ou não de estados intermediários na saída.

## 29. `accumulate()` aceita outra função binária

```python
from itertools import accumulate

values = [3, 1, 5, 2]
print(list(accumulate(values, max)))
```

Saída:

```text
[3, 3, 5, 5]
```

Mínimos, máximos, produtos, saldos e transições de estado podem seguir o mesmo contrato.

## 30. `initial=` muda o estado e o tamanho da saída

```python
from itertools import accumulate

print(list(accumulate([1, 2, 3], initial=10)))
```

Saída:

```text
[10, 11, 13, 16]
```

Com `initial`, o valor inicial é entregue primeiro, então a saída possui um elemento a mais que a entrada.

## 31. A função de acumulação recebe estado e depois elemento

Conceitualmente:

```text
new_state = function(previous_state, next_element)
```

A ordem dos argumentos importa quando a função não é comutativa.

## 32. `starmap()` desempacota tuplas de argumentos

```python
from itertools import starmap

arguments = [(2, 5), (3, 2), (10, 3)]
print(list(starmap(pow, arguments)))
```

Saída:

```text
[32, 9, 1000]
```

É útil quando um iterável já contém tuplas de argumentos.

## 33. `map()` e `starmap()` modelam formatos diferentes de entrada

```text
map(function, a, b)       -> function(a_item, b_item)
starmap(function, tuples) -> function(*tuple_item)
```

Escolha conforme os argumentos são representados upstream.

# Parte IV: iteradores infinitos

## 34. Iteradores infinitos exigem um desenho de término

`count()`, `cycle()` e `repeat()` podem produzir valores indefinidamente.

Uma fonte infinita não é perigosa por si só. O problema é um **consumidor sem limite**.

Defina o limite antes de consumir o stream.

## 35. `count()` cria uma progressão aritmética

```python
from itertools import count, islice

numbers = count(10, 3)
print(list(islice(numbers, 5)))
```

Saída:

```text
[10, 13, 16, 19, 22]
```

`count()` é útil quando a progressão deve permanecer como iterador.

## 36. `count()` com float pode acumular erro

A documentação oficial observa que, em alguns casos, melhor precisão de ponto flutuante pode ser obtida derivando cada valor de um índice inteiro:

```python
from itertools import count, islice

values = (0.1 * index for index in count())
print(list(islice(values, 4)))
```

Para regras de negócio que exigem decimal exato, o próximo capítulo introduzirá `decimal`.

## 37. `repeat()` fornece um stream constante

```python
from itertools import repeat

print(list(repeat("x", 3)))
```

Saída:

```text
['x', 'x', 'x']
```

Sem o segundo argumento, a repetição é infinita.

## 38. `repeat()` compõe naturalmente com `map()`

```python
from itertools import repeat

print(list(map(pow, [2, 3, 4], repeat(2))))
```

Saída:

```text
[4, 9, 16]
```

A constante repetida fornece o mesmo expoente para cada chamada.

## 39. `cycle()` repete a sequência de entrada indefinidamente

```python
from itertools import cycle, islice

rotating = cycle(["A", "B", "C"])
print(list(islice(rotating, 7)))
```

Saída:

```text
['A', 'B', 'C', 'A', 'B', 'C', 'A']
```

## 40. `cycle()` armazena valores de entrada para repetições futuras

Para repetir um iterável arbitrário, `cycle()` salva os valores conforme os encontra.

Por isso, sua memória auxiliar pode crescer com o tamanho da entrada finita original.

Não interprete automaticamente "iterator" como "memória constante".

## 41. Limite streams infinitos perto da fonte

Um padrão legível é:

```python
from itertools import count, islice

limited = islice(count(1), 5)
print(list(limited))
```

Colocar o limite perto do produtor infinito torna o término mais fácil de auditar.

# Parte V: alinhamento e fan-out

## 42. `zip_longest()` alinha até a maior entrada terminar

```python
from itertools import zip_longest

left = [1, 2, 3]
right = ["a"]
print(list(zip_longest(left, right, fillvalue="-")))
```

Saída:

```text
[(1, 'a'), (2, '-'), (3, '-')]
```

Isso contrasta com `zip()` normal, que para no menor iterável.

## 43. `zip_longest()` e `zip(strict=True)` representam políticas diferentes

```text
zip()                -> shortest wins
zip(strict=True)     -> unequal lengths are invalid
zip_longest()        -> longest wins; missing values are filled
```

Escolha a política que corresponde ao contrato dos dados, em vez de reparar diferenças depois.

## 44. Uma entrada infinita pode tornar `zip_longest()` infinito

Se qualquer entrada continuar para sempre, `zip_longest()` também pode continuar para sempre.

Envolva o resultado com uma ferramenta limitadora como `islice()` quando o consumidor precisar ser finito.

## 45. `tee()` cria visões independentes do iterador

```python
from itertools import tee

source = iter([10, 20, 30])
left, right = tee(source, 2)

print(next(left))
print(list(right))
print(list(left))
```

Saída:

```text
10
[10, 20, 30]
[20, 30]
```

Cada iterador retornado possui sua própria posição lógica.

## 46. A independência de `tee()` exige buffering

Se uma branch avança mais rápido, `tee()` precisa reter valores até que branches mais lentas os consumam.

O custo de memória depende, portanto, de quanto os consumidores divergem.

## 47. Prefira materialização quando os consumidores ficam muito separados

A documentação oficial observa que, se uma branch consome quase todos ou todos os dados antes que outra comece, converter para uma lista pode ser mais rápido que `tee()`.

`tee()` é valioso para consumidores streaming coordenados, não automaticamente para todo requisito de "usar duas vezes".

## 48. Iteradores de `tee()` não são thread-safe

O uso simultâneo de iteradores retornados pela mesma chamada a `tee()` não é thread-safe e pode lançar `RuntimeError`.

Não trate `tee()` como primitiva de concorrência.

## 49. Evite misturar o iterador original com as branches de tee

Após criar as branches, continue consumindo por elas, em vez de seguir usando o iterador original em código separado.

Um único caminho de ownership torna buffering e consumo muito mais fáceis de raciocinar.

# Parte VI: agrupando runs consecutivos

## 50. `groupby()` agrupa chaves iguais consecutivas

```python
from itertools import groupby

values = ["A", "A", "B", "B", "A"]
for key, group in groupby(values):
    print(key, list(group))
```

Saída:

```text
A ['A', 'A']
B ['B', 'B']
A ['A']
```

O `A` final inicia um novo grupo porque não está adjacente ao primeiro run de `A`.

## 51. `groupby()` não é `GROUP BY` do SQL

Agrupamento no estilo SQL normalmente reúne todas as linhas que compartilham uma chave, independentemente da posição.

`itertools.groupby()` inicia um novo grupo sempre que a chave muda.

Pense em **runs**, não em buckets globais.

## 52. Ordene antes quando a intenção for agrupar globalmente por chave

```python
from itertools import groupby
from operator import itemgetter

records = [("b", 2), ("a", 1), ("b", 3)]
records.sort(key=itemgetter(0))

for key, group in groupby(records, key=itemgetter(0)):
    print(key, list(group))
```

Ordenar pela mesma função de chave aproxima chaves iguais antes do agrupamento.

## 53. Iteradores de grupo compartilham a fonte subjacente

O `group` retornado por `groupby()` é ele próprio um iterador sobre a entrada compartilhada.

Quando o `groupby()` externo avança, um grupo anterior pode deixar de estar disponível.

Materialize um grupo se ele precisar sobreviver além da iteração externa atual.

## 54. `groupby()` pode expressar run-length encoding

```python
from itertools import groupby

values = "AAABBCCCCA"
runs = [(key, len(list(group))) for key, group in groupby(values)]
print(runs)
```

Saída:

```text
[('A', 3), ('B', 2), ('C', 4), ('A', 1)]
```

Isso preserva fronteiras de runs, em vez de colapsar todos os valores iguais.

# Parte VII: iteradores combinatórios

## 55. `product()` modela um produto cartesiano

```python
from itertools import product

print(list(product(["A", "B"], [1, 2])))
```

Saída:

```text
[('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

Em significado, equivale a loops aninhados sobre cada pool de entrada.

## 56. `product()` consome pools de entrada antes de produzir combinações

Embora `product()` retorne um iterador, primeiro ele consome cada iterável de entrada em pools mantidos em memória.

Portanto exige entradas finitas, e seu comportamento de memória na entrada é diferente de ferramentas como `chain()`.

## 57. `repeat=` multiplica dimensões do produto

```python
from itertools import product

print(list(product([0, 1], repeat=2)))
```

Saída:

```text
[(0, 0), (0, 1), (1, 0), (1, 1)]
```

A quantidade de resultados cresce multiplicativamente a cada dimensão.

## 58. `permutations()` modela seleções ordenadas

```python
from itertools import permutations

print(list(permutations("ABC", 2)))
```

Saída:

```text
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

A ordem importa, e posições não são reutilizadas dentro da mesma permutação.

## 59. Unicidade combinatória é posicional

Se valores iguais aparecerem em posições diferentes da entrada, as ferramentas ainda tratam essas posições como escolhas distintas.

Não presuma que valores duplicados na entrada produzirão automaticamente tuplas de saída deduplicadas.

## 60. `combinations()` ignora a ordenação dentro do subconjunto escolhido

```python
from itertools import combinations

print(list(combinations("ABC", 2)))
```

Saída:

```text
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

`('B', 'A')` não é outra combinação, porque as mesmas duas posições já foram escolhidas.

## 61. `combinations_with_replacement()` permite reutilizar posições

```python
from itertools import combinations_with_replacement

print(list(combinations_with_replacement("AB", 2)))
```

Saída:

```text
[('A', 'A'), ('A', 'B'), ('B', 'B')]
```

É útil quando repetir uma escolha é permitido e a ordem não cria um novo resultado.

## 62. Estime cardinalidade antes de consumir

Entradas pequenas podem produzir saídas enormes rapidamente.

Fórmulas úteis incluem:

```text
product sizes       -> multiply pool sizes
permutations(n, r)  -> n! / (n-r)!
combinations(n, r)  -> n! / (r! * (n-r)!)
```

`math.perm()` e `math.comb()` podem estimar duas dessas quantidades sem gerar as tuplas.

## 63. Um iterador ainda pode representar uma computação enorme

Entregar valores de forma lazy evita criar automaticamente uma lista gigante de resultados, mas não reduz o número de combinações que precisam ser geradas se você consumir todas.

Laziness protege armazenamento intermediário, não elimina complexidade algorítmica.

# Parte VIII: desenho de pipelines

## 64. Componha da esquerda para a direita em torno de uma fonte clara

```python
from itertools import chain, islice

pages = [[1, 2], [3, 4], [5, 6]]
stream = chain.from_iterable(pages)
preview = islice(stream, 4)
print(list(preview))
```

Saída:

```text
[1, 2, 3, 4]
```

Cada estágio responde uma pergunta: achatar, limitar, consumir.

## 65. Generator expressions e `itertools` se complementam

```python
from itertools import islice

squares = (number * number for number in range(100))
print(list(islice(squares, 5)))
```

Use generator expressions para expressões customizadas simples e `itertools` para padrões reutilizáveis de iteração.

## 66. Não compacte todo loop em um pipeline

Um loop com múltiplas etapas pode ser mais claro quando contém:

- branching complexo;
- vários efeitos colaterais;
- tratamento de erro por item;
- estado mutável que merece nomes explícitos.

Estilo pipeline é uma opção de design, não uma exigência de code golf.

## 67. Dê nomes aos estágios importantes

Prefira:

```python
from itertools import chain, islice

rows = [[1, 2], [3], [4, 5]]
flattened = chain.from_iterable(rows)
preview = islice(flattened, 3)
print(list(preview))
```

a uma expressão profundamente aninhada quando nomes intermediários explicam o modelo.

## 68. Documente o ownership de iteradores compartilhados

Quando vários helpers consomem o mesmo iterador, deixe claro qual estágio possui o próximo valor.

Bugs envolvendo `takewhile()`, `islice()`, `groupby()` ou `tee()` frequentemente são bugs de consumo, e não de aritmética.

## 69. Teste consumo parcial, não apenas listas finais

Um teste útil de iterador pode inspecionar o que restou:

```python
from itertools import islice

source = iter([1, 2, 3, 4])
assert list(islice(source, 2)) == [1, 2]
assert list(source) == [3, 4]
```

Isso verifica diretamente o contrato de consumo.

## 70. Limite testes infinitos explicitamente

Nunca escreva um teste que tente materializar um iterador infinito.

Use `islice()`, um `repeat(..., times)` finito ou outra condição explícita de parada.

## 71. Quatro exemplos executáveis neste capítulo

O diretório `examples/` contém programas determinísticos:

```text
lazy_pipeline.py
pairwise_deltas.py
groupby_runs.py
combinatoric_options.py
```

Eles são pequenos o suficiente para CI não interativo e usam APIs de `itertools` compatíveis com Python 3.10.

## 72. Erros comuns

### Erro 1: materializar todos os estágios

```python
values = list(range(1_000_000))
```

quando o consumidor só precisa de um prefixo curto.

Melhor: preserve laziness até uma coleção concreta ser realmente necessária.

### Erro 2: reutilizar um iterador esgotado

Um iterador consumido não reinicia automaticamente.

### Erro 3: esperar que `groupby()` reúna chaves iguais não adjacentes

Ele agrupa runs consecutivos.

### Erro 4: esquecer que `takewhile()` consome o valor que falhou

Esse valor não fica disponível para um consumidor posterior da mesma fonte.

### Erro 5: assumir que `tee()` duplica dados de graça

Branches atrasadas causam buffering.

### Erro 6: usar um iterador infinito sem um limite visível

O pipeline pode nunca terminar.

### Erro 7: tratar combinatória lazy como combinatória barata

A quantidade de resultados ainda pode explodir.

### Erro 8: usar `islice()` como slicing comum de sequência

Índices negativos não são suportados e elementos percorridos são consumidos.

## 73. Exercício prático

Construa um pequeno pipeline de análise de eventos.

Requisitos:

1. Comece com várias páginas de medições inteiras, representadas como uma lista de listas.
2. Achate um nível com `chain.from_iterable()`.
3. Use `islice()` para inspecionar apenas as primeiras oito medições.
4. Use `pairwise()` para calcular diferenças adjacentes.
5. Classifique cada diferença como `"up"`, `"down"` ou `"same"`.
6. Use `groupby()` para resumir runs consecutivos das classificações.
7. Não materialize a fonte achatada inteira antes da fronteira de preview.

Bônus: explique quais estágios consomem sua entrada e onde ocorre materialização.

## 74. Referência rápida

```text
chain(a, b, c)                  concatenate iterables
chain.from_iterable(rows)       flatten one level
batched(iterable, n)            non-overlapping batches [Python 3.12+]
batched(..., strict=True)       require complete batches [Python 3.13+]
islice(iterable, ...)           lazy positive slicing
pairwise(iterable)              adjacent pairs
compress(data, selectors)       Boolean-mask selection
filterfalse(predicate, items)   keep predicate failures
dropwhile(predicate, items)     drop leading matching prefix
takewhile(predicate, items)     keep leading matching prefix
accumulate(items, func)         running state
starmap(func, argument_tuples)  call func(*args)
count(start, step)              infinite arithmetic progression
cycle(iterable)                 repeat saved input indefinitely
repeat(value, times=None)       repeat one object
zip_longest(..., fillvalue=x)   align until longest input ends
tee(iterable, n)                fork logical iterator positions
groupby(iterable, key)          group consecutive equal keys
product(...)                    Cartesian product
permutations(items, r)          ordered selections
combinations(items, r)          unordered selections
combinations_with_replacement   unordered selections with reuse
```

## 75. Checklist de design

Antes de adicionar um estágio de `itertools`, pergunte:

- A fonte é finita ou potencialmente infinita?
- Quem possui o consumo deste iterador?
- O estágio é lazy, usa buffer ou materializa internamente a entrada?
- Outro consumidor precisará dos valores depois?
- Um helper de fronteira consome um sentinel ou valor que falhou?
- Entradas de tamanhos diferentes devem truncar, falhar ou preencher?
- O agrupamento é consecutivo ou global?
- Divergência entre branches pode tornar `tee()` caro?
- Quantos resultados combinatórios esta solicitação pode gerar?
- Onde o pipeline deve se tornar uma coleção concreta?
- Um loop explícito seria mais fácil de entender?
- Estou dependendo de uma API sensível à versão?

## 76. Conexões com outros conceitos de Python

`itertools` conecta-se diretamente a tópicos já estudados:

- **loops `for` e iteração:** todo itertool participa do protocolo de iteradores do Python.
- **`range()`, `enumerate()` e `zip()`:** esses built-ins são vizinhos naturais de pipelines de iteradores.
- **funções:** predicados, funções de chave e funções binárias de acumulação são passados como comportamento.
- **coleções:** `chain()` percorre contêineres; `groupby()` expõe iteradores de grupo; ferramentas combinatórias normalmente criam pools de entradas finitas.
- **generators:** generator expressions e estágios de itertools compõem naturalmente sem listas intermediárias eager.
- **algoritmos:** laziness muda o comportamento de armazenamento, mas não apaga complexidade temporal ou crescimento combinatório.
- **testes:** ownership e comportamento de consumo parcial são contratos que merecem asserts diretos.
- **próximo `decimal`:** aritmética exata torna-se importante quando pipelines numéricos representam dinheiro ou outros valores sensíveis à precisão.

## Referências

Referências primárias usadas neste capítulo:

- [Documentação Python 3.14: `itertools` — funções que criam iteradores para laços eficientes](https://docs.python.org/3.14/library/itertools.html)
- [Python 3.14 Functional Programming HOWTO — iteradores, generators e `itertools`](https://docs.python.org/3.14/howto/functional.html)
- [Documentação Python 3.14 do built-in `zip()`, incluindo `strict=True`](https://docs.python.org/3.14/library/functions.html#zip)
- [Documentação Python 3.14 de `math.comb()` e `math.perm()`](https://docs.python.org/3.14/library/math.html#combinatorics)

## Próximo capítulo

Continue com o [Capítulo 08: `decimal`](../08-decimal/README.pt-BR.md).

O próximo capítulo muda de contratos de iteração lazy para **contratos de precisão numérica**: representação decimal, contexts, rounding, traps, quantização e aritmética exata para valores em que o comportamento binário de ponto flutuante não é o modelo desejado.
