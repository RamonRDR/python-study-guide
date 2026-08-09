<div align="center">

# `int`, `float` e `bool`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Métodos comuns de strings](../02-common-string-methods/README.pt-BR.md) · [Próximo capítulo: Funções numéricas embutidas →](../04-numeric-builtins/README.pt-BR.md)

O Python já apresentou esses tipos na fase de Fundamentos. Este capítulo avança um nível ao focar em como eles se comportam em expressões, como seus resultados diferem e quais detalhes importam ao escolher entre eles.

O objetivo não é memorizar regras isoladas. O objetivo é construir um modelo mental confiável para números inteiros, valores decimais aproximados e valores de verdade.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- escolher `int`, `float` ou `bool` de acordo com o significado de um valor;
- explicar por que inteiros em Python não estão limitados a um intervalo fixo de 32 ou 64 bits;
- prever o tipo de resultado de expressões numéricas mistas comuns;
- distinguir `/` de `//` e `%`;
- entender por que divisão inteira com números negativos pode surpreender iniciantes;
- reconhecer os limites de aproximação de valores de ponto flutuante binários;
- explicar por que `0.1 + 0.2 == 0.3` é `False`;
- usar `bool()` e valores de verdade sem confundir conteúdo textual com significado booleano;
- explicar a relação especial entre `bool` e `int`;
- evitar usar valores booleanos como quantidades numéricas quando isso esconder a intenção.

## 1. Três tipos, três funções principais

Um primeiro modelo útil é:

| Tipo | Função principal | Exemplo |
|---|---|---|
| `int` | valores inteiros | `12`, `0`, `-4` |
| `float` | valores fracionários ou reais aproximados | `7.5`, `-0.25` |
| `bool` | valores de verdade | `True`, `False` |

```python
item_count = 12
unit_price = 7.5
is_available = True

print(type(item_count))
print(type(unit_price))
print(type(is_available))
```

```text
<class 'int'>
<class 'float'>
<class 'bool'>
```

Esses tipos podem interagir, mas ainda comunicam significados diferentes.

## 2. `int` representa inteiros

Use `int` para valores que conceitualmente não possuem parte fracionária.

```python
students = 30
temperature_change = -4
balance_adjustment = 0

print(students)
print(temperature_change)
print(balance_adjustment)
```

```text
30
-4
0
```

Um inteiro pode ser positivo, negativo ou zero.

## 3. Inteiros em Python têm precisão arbitrária

Em muitas linguagens de programação, um tipo inteiro está ligado a uma quantidade fixa de bits. O `int` embutido do Python é diferente: inteiros têm precisão arbitrária, limitada principalmente pela memória disponível e por restrições de implementação, e não por um intervalo normal fixo de 32 ou 64 bits.

```python
large_number = 10 ** 100

print(type(large_number))
print(len(str(large_number)))
```

```text
<class 'int'>
101
```

Isso não significa que inteiros extremamente grandes sejam gratuitos. Valores maiores exigem mais memória e processamento. O ponto importante para iniciantes é apenas que valores `int` comuns em Python não estouram em um limite pequeno fixo como 2.147.483.647.

## 4. Separadores numéricos melhoram a legibilidade

Python permite underscores dentro de literais numéricos para melhorar a leitura.

```python
annual_revenue = 1_250_000
binary_mask = 0b1010

print(annual_revenue)
print(binary_mask)
```

```text
1250000
10
```

Os underscores fazem parte da notação do código-fonte, não do valor numérico armazenado.

O literal binário aparece apenas para mostrar que a notação de inteiros pode variar. Bases numéricas não são o foco deste capítulo.

## 5. `float` representa valores de ponto flutuante

Use `float` quando um valor precisa de uma parte fracionária ou quando uma operação produz naturalmente um resultado de ponto flutuante.

```python
unit_price = 19.90
exchange_rate = 5.42
temperature = -3.5

print(type(unit_price))
print(type(exchange_rate))
print(type(temperature))
```

```text
<class 'float'>
<class 'float'>
<class 'float'>
```

Um literal numérico real que contém um ponto decimal, como `19.90`, produz um `float`.

## 6. `int` e `float` podem participar da mesma expressão

Python oferece aritmética mista entre esses tipos numéricos.

```python
whole_number = 4
decimal_number = 2.5

print(whole_number + decimal_number)
print(type(whole_number + decimal_number))
```

```text
6.5
<class 'float'>
```

Quando um inteiro e um valor de ponto flutuante participam de uma operação aritmética comum, Python normalmente produz um resultado de ponto flutuante para preservar a capacidade fracionária.

Esse é um exemplo de conversão numérica implícita. Ele não substitui os conceitos de conversão explícita estudados em Fundamentos.

## 7. `/` é divisão verdadeira

O operador `/` realiza divisão verdadeira.

```python
print(7 / 2)
print(type(7 / 2))
```

```text
3.5
<class 'float'>
```

Mesmo quando os dois operandos são inteiros, `/` produz um resultado de ponto flutuante quando o resultado matemático pode ser representado como `float`. Se esse resultado for grande demais para ser convertido em um `float` finito, a divisão verdadeira gera `OverflowError`.

```python
print(8 / 4)
print(type(8 / 4))
```

```text
2.0
<class 'float'>
```

Quando o quociente pode ser representado como `float`, um quociente matematicamente inteiro ainda tem tipo `float` quando `/` é utilizado.

## 8. `//` é divisão pelo piso

O operador `//` realiza divisão pelo piso.

```python
print(7 // 2)
print(7.0 // 2)
```

```text
3
3.0
```

Com dois inteiros, o resultado é inteiro. Se um operando de ponto flutuante participar, o resultado é um valor de ponto flutuante que representa o quociente arredondado para baixo.

A palavra **piso** é importante. `//` não significa simplesmente "remover a parte decimal".

## 9. `%` fornece o resto associado à divisão pelo piso

O operador `%` fornece o resto.

```python
print(7 % 2)
print(14 % 5)
```

```text
1
4
```

Para inteiros, `//` e `%` se relacionam por esta igualdade:

```text
dividend == divisor * (dividend // divisor) + (dividend % divisor)
```

Exemplo:

```python
value = 17
divisor = 5

quotient = value // divisor
remainder = value % divisor

print(quotient)
print(remainder)
print(divisor * quotient + remainder)
```

```text
3
2
17
```

Essa relação se torna especialmente útil ao dividir valores em grupos e sobras.

## 10. Divisão pelo piso com números negativos pode surpreender

Um erro comum é esperar que a divisão pelo piso simplesmente trunque em direção a zero.

```python
print(-7 // 3)
print(-7 % 3)
```

```text
-3
2
```

Por que `-3` em vez de `-2`?

Porque a divisão pelo piso arredonda o quociente para baixo, em direção ao infinito negativo. O quociente exato é aproximadamente `-2.333...`, e seu piso é `-3`.

O resto então preserva a identidade da divisão:

```text
-7 == 3 * (-3) + 2
```

Você não precisa memorizar cada caso negativo. Lembre da regra: `//` significa divisão pelo piso, não truncamento.

## 11. `**` realiza exponenciação

O operador de exponenciação é `**`.

```python
print(2 ** 5)
print(9 ** 0.5)
```

```text
32
3.0
```

O tipo do resultado depende dos valores e da operação. Elevar `9` a `0.5` usa um expoente de ponto flutuante e produz um `float`.

## 12. Divisão por zero é um erro

Tipos numéricos não tornam válida a divisão por zero.

```python
print(10 / 0)
```

A operação gera:

```text
ZeroDivisionError: division by zero
```

O traceback completo contém linhas adicionais e informações do arquivo. O ponto importante aqui é o tipo da exceção.

Tratamento de exceções será estudado mais adiante no roadmap. Por enquanto, reconheça que uma operação aritmética inválida pode interromper a execução do programa.

## 13. Valores de ponto flutuante geralmente são aproximações

Na maioria dos sistemas modernos, números de ponto flutuante do Python usam aritmética binária de ponto flutuante fornecida pelo hardware.

Muitas frações decimais simples não podem ser representadas exatamente como frações binárias finitas. Isso significa que um valor como `0.1` é armazenado como a aproximação binária representável mais próxima.

Isso não é um bug específico do Python. É uma propriedade da aritmética binária de ponto flutuante usada por muitas linguagens e processadores.

## 14. O exemplo clássico de `0.1 + 0.2`

```python
result = 0.1 + 0.2

print(result)
print(result == 0.3)
```

```text
0.30000000000000004
False
```

O resultado exibido revela uma pequena diferença de representação.

A lição importante não é que floats sejam pouco confiáveis. A lição é que eles representam muitos valores decimais de forma aproximada, então igualdade decimal exata pode ser inadequada em algumas situações.

## 15. O texto decimal exibido não conta toda a história interna

Python normalmente exibe uma representação decimal curta que volta ao mesmo valor de ponto flutuante armazenado.

Você pode inspecionar uma razão inteira exata para um float finito:

```python
value = 0.1

print(value)
print(value.as_integer_ratio())
```

```text
0.1
(3602879701896397, 36028797018963968)
```

Em plataformas modernas de Python que usam IEEE 754 binary64 para `float`, a razão mostra o valor exato armazenado que esse `float` representa. A linguagem não exige que toda implementação de Python use esse formato de hardware.

Para um iniciante, o modelo mental simples é suficiente: o texto `0.1` é uma notação conveniente para um valor de ponto flutuante representável próximo dele.

## 16. Não use igualdade de floats sem pensar no contexto

Isto pode ser frágil:

```python
print(0.1 + 0.2 == 0.3)
```

```text
False
```

Se igualdade exata é adequada depende do domínio.

Para comparações numéricas aproximadas, a biblioteca padrão do Python fornece ferramentas como `math.isclose()`. Para aritmética decimal exata em base 10, o módulo `decimal` muitas vezes é mais adequado.

Essas ferramentas estão fora do escopo deste capítulo. A ideia importante aqui é reconhecer quando a igualdade direta entre valores `float` pode não expressar a comparação pretendida.

## 17. Valores monetários merecem atenção especial

Um padrão tentador para iniciantes é:

```python
account_balance = 0.1 + 0.2
```

Um `float` pode ser perfeitamente adequado para muitas medições, cálculos gráficos, simulações e tarefas numéricas comuns. Mas domínios que exigem comportamento decimal exato, como muitos cálculos contábeis, frequentemente precisam de uma representação decimal criada para esse requisito.

Não transforme isso na regra simplista "float é ruim para dinheiro". A pergunta correta é quais garantias de precisão, arredondamento, armazenamento e domínio a aplicação exige.

## 18. `float.is_integer()` pergunta se um float tem valor integral

Um `float` pode representar um valor sem parte fracionária.

```python
print((5.0).is_integer())
print((5.25).is_integer())
```

```text
True
False
```

`5.0` continua sendo um `float`. `is_integer()` pergunta sobre seu valor numérico, e não sobre seu tipo em tempo de execução.

```python
value = 5.0

print(type(value))
print(value.is_integer())
```

```text
<class 'float'>
True
```

## 19. `bool` representa valores de verdade

O tipo booleano tem dois valores:

```python
is_ready = True
has_error = False

print(type(is_ready))
print(type(has_error))
```

```text
<class 'bool'>
<class 'bool'>
```

Use `bool` quando o significado for sim/não, verdadeiro/falso, habilitado/desabilitado, disponível/indisponível ou outra condição de dois estados.

## 20. Comparações produzem resultados booleanos

Comparações respondem perguntas sobre valores e normalmente produzem `True` ou `False`.

```python
temperature = 18

print(temperature > 20)
print(temperature == 18)
```

```text
False
True
```

O uso detalhado de comparações dentro de `if`, `while` e outras estruturas de fluxo vem depois. Aqui, foque no tipo do resultado.

## 21. Todo objeto pode participar de teste de valor verdade

Python pode interpretar muitos valores como verdadeiros ou falsos em um contexto booleano.

```python
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(None))
print(bool(1))
print(bool(-3))
print(bool("Python"))
```

```text
False
False
False
False
True
True
True
```

Para os tipos já apresentados neste guia:

- zero numérico é falso;
- uma string vazia é falsa;
- `None` é falso;
- números diferentes de zero são verdadeiros;
- strings não vazias são verdadeiras.

Coleções acrescentarão mais regras de valor verdade depois.

## 22. Conteúdo textual não é interpretado como uma palavra booleana

Esta é uma armadilha clássica para iniciantes:

```python
print(bool("False"))
print(bool("0"))
```

```text
True
True
```

As duas strings não estão vazias, portanto ambas são truthy.

`bool()` não lê palavras em inglês e decide o significado delas. Ele aplica as regras de valor verdade do Python ao objeto.

## 23. `bool` é uma subclasse de `int`

Python possui uma relação histórica e técnica entre valores booleanos e inteiros.

```python
print(isinstance(True, bool))
print(isinstance(True, int))
print(int(True))
print(int(False))
```

```text
True
True
1
0
```

É por isso que o Capítulo 05 de Fundamentos mostrou que `isinstance(True, int)` é `True`, embora `type(True) is bool`.

A relação é real, mas não deve apagar o significado semântico.

## 24. Aritmética booleana funciona, mas frequentemente comunica a ideia errada

Como `bool` é uma subclasse de `int`, isto é Python válido:

```python
print(True + True)
print(False + 10)
```

```text
2
10
```

Isso não significa que aritmética booleana deva ser seu design padrão.

Se uma variável significa disponibilidade, validação, permissão ou outra condição, preserve esse significado em vez de tratar o valor como um `0` ou `1` acidental.

## 25. Escolha um tipo de acordo com o significado, não com a aparência

Considere este pequeno modelo:

```python
items_in_cart = 3
average_price = 14.75
is_checkout_open = True

print(type(items_in_cart))
print(type(average_price))
print(type(is_checkout_open))
```

```text
<class 'int'>
<class 'float'>
<class 'bool'>
```

Os três valores poderiam participar de comportamento numérico em algumas circunstâncias, mas seus significados de domínio são diferentes.

Boas escolhas de tipo tornam o código posterior mais fácil de entender.

## 26. Evite flags inteiras quando um booleano expressa a intenção

Menos claro:

```python
is_active = 1
```

Mais claro:

```python
is_active = True
```

Uma flag inteira pode ser válida ao se comunicar com um formato de arquivo, banco de dados, protocolo ou API legada que exija `0` e `1`. Dentro da lógica Python comum, um `bool` geralmente comunica a intenção booleana com mais clareza.

## 27. Evite adicionar `.0` apenas para fazer um valor parecer decimal

Isto não é automaticamente melhor:

```python
employee_count = 42.0
```

Se o valor representa uma contagem que não pode ser fracionária, `42` pode expressar melhor o domínio.

Da mesma forma, um valor como `5.0` pode legitimamente precisar permanecer `float` quando pertence a uma cadeia de cálculos baseada em medições ou operações de ponto flutuante.

O significado vem primeiro.

## 28. Tipos de resultado numérico podem carregar informação

Compare:

```python
print(5 + 2)
print(5 + 2.0)
print(5 / 2)
print(5 // 2)
```

```text
7
7.0
2.5
2
```

Os operadores e os tipos dos operandos influenciam tanto o valor quanto o tipo do resultado.

Ao depurar código numérico, inspecione ambos.

## 29. Exemplo prático: comportamento numérico

O arquivo [`examples/numeric_behavior.py`](examples/numeric_behavior.py) contém:

```python
whole_number = 7
decimal_number = 2.5

print("Mixed addition:", whole_number + decimal_number)
print("True division:", 7 / 2)
print("Floor division:", 7 // 2)
print("Remainder:", 7 % 2)
print("Negative floor division:", -7 // 3)
print("Matching remainder:", -7 % 3)
```

Saída esperada:

```text
Mixed addition: 9.5
True division: 3.5
Floor division: 3
Remainder: 1
Negative floor division: -3
Matching remainder: 2
```

Este exemplo mantém várias regras numéricas relacionadas no mesmo lugar.

## 30. Exemplo prático: verdade e precisão

O arquivo [`examples/truth_and_precision.py`](examples/truth_and_precision.py) contém:

```python
print("0.1 + 0.2:", 0.1 + 0.2)
print("Exactly 0.3:", 0.1 + 0.2 == 0.3)
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print('bool(""):', bool(""))
print('bool("False"):', bool("False"))
print("bool is int-compatible:", isinstance(True, int))
```

Saída esperada:

```text
0.1 + 0.2: 0.30000000000000004
Exactly 0.3: False
bool(0): False
bool(1): True
bool(""): False
bool("False"): True
bool is int-compatible: True
```

O exemplo coloca deliberadamente duas surpresas comuns lado a lado: aproximação de ponto flutuante e regras de valor verdade booleano.

## 31. Erros comuns

### Erro 1: esperar que `/` preserve `int`

```python
print(type(8 / 4))
```

```text
<class 'float'>
```

### Erro 2: interpretar `//` como truncamento em direção a zero

```python
print(-7 // 3)
```

```text
-3
```

### Erro 3: esperar que aritmética decimal com floats seja exata

```python
print(0.1 + 0.2 == 0.3)
```

```text
False
```

### Erro 4: supor que o texto `"False"` seja falso

```python
print(bool("False"))
```

```text
True
```

### Erro 5: esquecer que `bool` é compatível com `int`

```python
print(isinstance(True, int))
```

```text
True
```

Compatibilidade não significa que os dois tipos expressem a mesma intenção.

## 32. Exercício: monte um perfil numérico

Crie um arquivo chamado `numeric_profile.py`.

Use estes valores iniciais:

```python
item_count = 12
unit_price = 7.5
is_available = True
```

Seu programa deve:

1. calcular `subtotal` multiplicando `item_count` por `unit_price`;
2. imprimir cada valor original;
3. imprimir o tipo de cada valor original;
4. imprimir `subtotal`;
5. imprimir o tipo de `subtotal`;
6. explicar, com suas próprias palavras, por que `subtotal` é um `float`.

Uma implementação possível é:

```python
item_count = 12
unit_price = 7.5
is_available = True

subtotal = item_count * unit_price

print("Item count:", item_count)
print("Item count type:", type(item_count))
print("Unit price:", unit_price)
print("Unit price type:", type(unit_price))
print("Available:", is_available)
print("Available type:", type(is_available))
print("Subtotal:", subtotal)
print("Subtotal type:", type(subtotal))
```

Saída esperada:

```text
Item count: 12
Item count type: <class 'int'>
Unit price: 7.5
Unit price type: <class 'float'>
Available: True
Available type: <class 'bool'>
Subtotal: 90.0
Subtotal type: <class 'float'>
```

Tente o exercício sozinho antes de comparar com o exemplo.

## 33. Autoavaliação

Agora você deve conseguir responder estas perguntas antes de executar Python:

1. Qual é a principal diferença conceitual entre `int`, `float` e `bool`?
2. Por que Python pode armazenar um inteiro muito maior que um inteiro normal de 64 bits?
3. Que tipo `7 / 2` produz?
4. Qual é a diferença entre `/` e `//`?
5. Por que `-7 // 3` é igual a `-3`?
6. O que `%` retorna?
7. Por que `0.1 + 0.2 == 0.3` pode ser `False`?
8. `5.0` é um `int` porque sua parte fracionária é zero?
9. Por que `bool("False")` é igual a `True`?
10. Por que `isinstance(True, int)` retorna `True`?

## 34. Consulta rápida

| Objetivo | Exemplo | Detalhe importante |
|---|---|---|
| Número inteiro | `count = 12` | `int` tem precisão arbitrária |
| Valor numérico fracionário | `rate = 5.42` | `float` normalmente é ponto flutuante binário aproximado |
| Valor de verdade | `is_ready = True` | `bool` possui `True` e `False` |
| Divisão verdadeira | `7 / 2` | retorna `3.5` |
| Divisão pelo piso | `7 // 2` | retorna o quociente pelo piso |
| Resto | `7 % 2` | trabalha em conjunto com divisão pelo piso |
| Exponenciação | `2 ** 5` | retorna `32` |
| Testar valor integral de float | `(5.0).is_integer()` | o valor pode ser integral enquanto o tipo continua `float` |
| Converter para valor verdade | `bool(value)` | segue regras de valor verdade |
| Tipo exato em tempo de execução | `type(value)` | `type(True) is bool` |
| Tipo compatível | `isinstance(value, int)` | `True` é compatível com `int` |

## 35. Execute os exemplos

A partir da raiz do repositório:

```bash
python strings-and-numbers/03-int-float-and-bool/examples/numeric_behavior.py
python strings-and-numbers/03-int-float-and-bool/examples/truth_and_precision.py
```

Depois execute as validações do repositório:

```bash
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 36. O que vem a seguir

Agora você possui um modelo mais forte para números inteiros, valores de ponto flutuante e valores booleanos.

O próximo capítulo conclui a Fase 2 apresentando funções numéricas comuns: **`round()`, `abs()`, `min()`, `max()` e `sum()`**.

Esse capítulo vai se apoiar diretamente no comportamento numérico estabelecido aqui, em vez de tratar essas funções como uma lista isolada.

## Referências oficiais

- [Tipos embutidos do Python: Tipos numéricos](https://docs.python.org/pt-br/3.14/library/stdtypes.html#numeric-types-int-float-complex)
- [Tipos embutidos do Python: Teste do valor verdade](https://docs.python.org/pt-br/3.14/library/stdtypes.html#truth-value-testing)
- [Tipos embutidos do Python: Tipo booleano](https://docs.python.org/pt-br/3.14/library/stdtypes.html#boolean-type-bool)
- [Tutorial do Python: Aritmética de ponto flutuante, problemas e limitações](https://docs.python.org/pt-br/3.14/tutorial/floatingpoint.html)

[← Voltar ao índice da seção](../README.pt-BR.md)
