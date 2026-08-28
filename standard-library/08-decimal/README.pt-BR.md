<div align="center">

# Projetando Contratos de Precisão e Arredondamento Decimal

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Biblioteca Padrão](../README.pt-BR.md) · [← Anterior: `itertools`](../07-itertools/README.pt-BR.md)

O `float` embutido do Python é a ferramenta certa para uma grande quantidade de trabalho numérico, mas ele modela números com ponto flutuante binário. O Capítulo 03 de Strings e Números já mostrou por que um valor como `0.1` pode não ter uma representação binária exata.

O módulo `decimal` resolve um problema diferente. Ele fornece aritmética decimal de ponto flutuante com controle explícito sobre representação, precisão, arredondamento, condições excepcionais e validação.

Este capítulo não trata de substituir todo `float` por `Decimal`. Ele trata de escolher deliberadamente um contrato numérico quando os próprios dígitos decimais fazem parte do significado dos dados.

**Tempo estimado de estudo:** 180–240 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que `Decimal` resolve e o que ele não resolve;
- construir valores decimais sem importar acidentalmente aproximação de ponto flutuante binário;
- distinguir representação decimal exata de aritmética com precisão ilimitada;
- explicar sinal, dígitos do coeficiente, expoente e preservação de zeros à direita;
- inspecionar representação com `as_tuple()` e distinguir igualdade de valor de ordenação por representação;
- explicar por que a precisão do contexto conta dígitos significativos e não casas decimais;
- inspecionar e sobrescrever temporariamente o contexto aritmético ativo;
- escolher regras de arredondamento explicitamente em vez de depender de um padrão acidental;
- usar `quantize()` para impor um expoente-alvo ou escala decimal fixa;
- distinguir os sinais `Rounded` e `Inexact`;
- usar flags para monitoramento e traps para imposição de regras;
- validar uma escala decimal capturando `Inexact` como trap;
- tratar `Infinity`, `NaN`, NaN sinalizante e zero com sinal de forma deliberada;
- reconhecer quando aritmética entre `Decimal` e `float` é rejeitada intencionalmente;
- usar `FloatOperation` para detectar caminhos de conversão implícita de float;
- explicar a finalidade de `BasicContext`, `ExtendedContext` e objetos `Context` explícitos;
- usar `fma()` quando uma única etapa de arredondamento importa mais do que arredondar um produto intermediário;
- escolher fronteiras seguras para JSON, texto, bancos de dados, APIs e entrada do usuário;
- reconhecer trade-offs de desempenho, interoperabilidade e manutenção;
- testar políticas decimais como comportamento, não apenas como saída formatada.

## 1. O problema não é que `float` esteja quebrado

Ponto flutuante binário é um modelo de representação deliberado. Ele é rápido, amplamente suportado por hardware e apropriado para cargas científicas, gráficas, estatísticas e muitos usos numéricos gerais.

A incompatibilidade aparece quando a **representação decimal em si faz parte do contrato**.

```python
print(0.1 + 0.1 + 0.1 == 0.3)
```

```text
False
```

Esse resultado vem de erro de representação binária, não de o Python ter esquecido aritmética.

## 2. `Decimal` usa representação decimal

```python
from decimal import Decimal


result = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")
print(result)
print(result == Decimal("0.3"))
```

```text
0.3
True
```

As strings decimais podem ser representadas exatamente como números decimais.

## 3. Representação exata não significa que todo resultado será exato para sempre

Uma distinção essencial:

```text
exact decimal input
        ↓
Decimal representation
        ↓
arithmetic under a finite context precision
        ↓
possibly rounded result
```

Por exemplo, `1 / 7` possui expansão decimal infinita.

```python
from decimal import Decimal, localcontext


with localcontext(prec=8):
    print(Decimal(1) / Decimal(7))
```

```text
0.14285714
```

`Decimal` remove erro de representação binária para entradas decimais. Ele não elimina a existência de precisão finita.

## 4. Importe os nomes que seu código realmente usa

Para exemplos didáticos, imports explícitos deixam dependências visíveis:

```python
from decimal import Decimal, ROUND_HALF_EVEN
```

O módulo expõe vários contextos, sinais e constantes de arredondamento. Evite `from decimal import *` em código de aplicação normal quando nomes explícitos tornam a política numérica mais fácil de auditar.

## 5. Prefira strings quando o valor de origem é texto decimal

```python
from decimal import Decimal


price = Decimal("19.90")
rate = Decimal("0.075")

print(price)
print(rate)
```

Um construtor a partir de string expressa diretamente os dígitos decimais.

## 6. Inteiros são convertidos exatamente

```python
from decimal import Decimal


quantity = Decimal(7)
print(quantity)
```

```text
7
```

A conversão de inteiro para Decimal é exata.

## 7. Passar um `float` preserva exatamente o valor binário do float

Essa é uma das fronteiras mais importantes do módulo:

```python
from decimal import Decimal


print(Decimal(0.1))
```

O resultado contém muitos dígitos porque o Python converte o `float` binário já existente **exatamente** para seu equivalente decimal.

Isso é diferente de:

```python
from decimal import Decimal


print(Decimal("0.1"))
```

A segunda forma representa diretamente o valor decimal um décimo.

## 8. `Decimal.from_float()` deixa essa fronteira explícita

```python
from decimal import Decimal


converted = Decimal.from_float(0.1)
print(converted)
```

Use quando preservar exatamente o valor de um `float` existente for a intenção real.

Isso não é um atalho para recuperar texto decimal que existia antes de o float ser criado.

## 9. `Decimal.from_number()` é uma adição do Python 3.14

O Python 3.14 adiciona um construtor alternativo que aceita `int`, `float` ou `Decimal`, mas não strings ou tuplas:

```python
from decimal import Decimal


value = Decimal.from_number(314)
print(value)
```

Quando compatibilidade com versões anteriores ao Python 3.14 importa, use os construtores mais antigos apropriados ao tipo da origem.

## 10. Decida onde o contrato decimal começa

Uma fronteira robusta costuma se parecer com:

```text
text / database decimal / validated API text
                    ↓
              Decimal(...)
                    ↓
          Decimal-only calculation
                    ↓
      explicit rounding / quantization
                    ↓
         output or persistence boundary
```

Converter para `Decimal` somente depois de vários cálculos em float binário não apaga aproximações já introduzidas antes.

## 11. `Decimal` e `float` normalmente não se misturam em aritmética

```python
from decimal import Decimal


amount = Decimal("1.25")
# amount + 0.5  # TypeError
```

Essa rejeição é útil. Ela evita que um pipeline misture silenciosamente dois modelos numéricos diferentes.

Comparações possuem regras próprias, mas aritmética comum normalmente deve permanecer dentro de uma representação numérica deliberada.

## 12. Um Decimal possui sinal, dígitos do coeficiente e expoente

Conceitualmente:

```text
Decimal("12.340")

sign        = positive
coefficient = 1, 2, 3, 4, 0
exponent    = -3
```

O expoente descreve a escala decimal em relação ao coeficiente.

## 13. Zeros à direita podem preservar significância

```python
from decimal import Decimal


print(Decimal("1.20"))
print(Decimal("1.2000"))
```

```text
1.20
1.2000
```

Os valores são numericamente iguais, mas suas representações armazenadas preservam informações diferentes de zeros à direita.

## 14. Inspecione a representação com `as_tuple()`

```python
from decimal import Decimal


value = Decimal("12.340")
print(value.as_tuple())
```

O resultado expõe sinal, dígitos do coeficiente e expoente como uma named tuple.

## 15. Igualdade numérica ignora diferenças de representação

```python
from decimal import Decimal


print(Decimal("12.0") == Decimal("12.00"))
```

```text
True
```

Os números possuem o mesmo valor numérico.

## 16. `compare_total()` consegue distinguir representações

Quando a própria representação importa, `compare_total()` fornece uma ordenação total baseada na representação abstrata do Decimal:

```python
from decimal import Decimal


left = Decimal("12.0")
right = Decimal("12")
print(left.compare_total(right))
```

Não use comparação sensível à representação quando igualdade numérica comum é o requisito real.

## 17. Objetos Decimal são imutáveis

A aritmética cria novos valores em vez de alterar objetos Decimal existentes.

```python
from decimal import Decimal


amount = Decimal("10.00")
updated = amount + Decimal("2.50")

print(amount)
print(updated)
```

```text
10.00
12.50
```

Esse comportamento combina naturalmente com funções, chaves de dicionário, sets e cálculos repetíveis.

## 18. A aritmética acontece sob um contexto

O contexto aritmético controla propriedades como:

- precisão;
- modo de arredondamento;
- limites de expoente;
- flags de sinais;
- habilitadores de traps.

Pense no contexto como a **política de execução numérica** ao redor das operações Decimal.

## 19. Inspecione o contexto ativo com `getcontext()`

```python
from decimal import getcontext


context = getcontext()
print(context.prec)
print(context.rounding)
```

A precisão padrão é 28 dígitos e o modo de arredondamento padrão é `ROUND_HALF_EVEN`, a menos que o contexto ativo tenha sido alterado.

## 20. Precisão significa dígitos significativos, não casas decimais

Essa distinção é essencial.

```python
from decimal import Decimal, localcontext


with localcontext(prec=4):
    print(Decimal("12345") + Decimal("1"))
    print(Decimal("1.2345") + Decimal("0"))
```

A precisão do contexto limita dígitos significativos nos resultados aritméticos. Ela não significa "sempre mantenha quatro dígitos depois do ponto decimal".

Use `quantize()` quando um expoente ou escala fixa for exigido.

## 21. Construção a partir de string não arredonda para a precisão do contexto

```python
from decimal import Decimal, localcontext


with localcontext(prec=4):
    value = Decimal("3.1415926535")
    print(value)
```

O construtor preserva os dígitos fornecidos pela string. A precisão do contexto se torna relevante quando aritmética é executada.

## 22. A aritmética aplica o contexto

```python
from decimal import Decimal, localcontext


with localcontext(prec=6):
    result = Decimal("3.1415926535") + Decimal("2.7182818285")
    print(result)
```

```text
5.85987
```

Os operandos exatos possuem mais dígitos do que a precisão do resultado permite, então ocorre arredondamento.

## 23. Evite alterar a política aritmética global casualmente

Isto funciona:

```python
from decimal import getcontext


getcontext().prec = 50
```

Mas alterar o contexto ativo dentro de código de biblioteca reutilizável pode surpreender chamadores cujos cálculos compartilham esse contexto.

Prefira um escopo local quando a precisão ou regra de arredondamento pertencer somente a uma operação.

## 24. `localcontext()` delimita uma política temporária

```python
from decimal import Decimal, getcontext, localcontext


original_precision = getcontext().prec

with localcontext(prec=8):
    result = Decimal(1) / Decimal(7)

print(result)
print(getcontext().prec == original_precision)
```

O contexto anterior é restaurado após o bloco `with`.

Argumentos nomeados para definir atributos diretamente em `localcontext()` estão disponíveis a partir do Python 3.11.

## 25. Objetos `Context` explícitos tornam a política transportável

```python
from decimal import Context, Decimal, ROUND_HALF_UP


policy = Context(prec=12, rounding=ROUND_HALF_UP)
result = policy.divide(Decimal(1), Decimal(7))
print(result)
```

Um contexto explícito pode ser passado ou reutilizado como objeto de política em vez de depender de estado ambiente.

## 26. `Context.create_decimal()` aplica o contexto durante a conversão

O construtor comum `Decimal` não reduz os dígitos de entrada segundo a precisão do contexto.

`Context.create_decimal()` é diferente: ele aplica precisão, arredondamento, flags e traps do contexto durante a conversão.

```python
from decimal import Context, ROUND_DOWN


policy = Context(prec=5, rounding=ROUND_DOWN)
value = policy.create_decimal("3.1415926")
print(value)
```

```text
3.1415
```

Use quando normalizar a entrada fizer intencionalmente parte da política do contexto.

## 27. Arredondamento é uma regra de domínio ou numérica, não decoração

Formatação controla apresentação. Arredondamento altera o valor numérico.

São decisões separadas:

```text
calculation precision
        ≠
quantization policy
        ≠
display formatting
```

Torne cada uma explícita quando a correção depender dela.

## 28. `ROUND_HALF_EVEN` é o modo padrão do contexto

Half-even arredonda para o resultado mais próximo e resolve um empate exato em direção ao candidato cujo último dígito mantido é par.

```python
from decimal import Decimal, ROUND_HALF_EVEN


whole = Decimal("1")
print(Decimal("2.5").quantize(whole, rounding=ROUND_HALF_EVEN))
print(Decimal("3.5").quantize(whole, rounding=ROUND_HALF_EVEN))
```

```text
2
4
```

Não descreva isso como "arredondar para baixo em .5". O desempate depende de qual resultado vizinho é par.

## 29. `ROUND_HALF_UP` resolve empates afastando-se de zero

```python
from decimal import Decimal, ROUND_HALF_UP


whole = Decimal("1")
print(Decimal("2.5").quantize(whole, rounding=ROUND_HALF_UP))
print(Decimal("-2.5").quantize(whole, rounding=ROUND_HALF_UP))
```

```text
3
-3
```

Escolha um modo de arredondamento porque o domínio exige, não porque o nome parece familiar.

## 30. Modos de arredondamento direcionais têm contratos diferentes

O módulo também inclui:

```text
ROUND_CEILING  -> toward +Infinity
ROUND_FLOOR    -> toward -Infinity
ROUND_DOWN     -> toward zero
ROUND_UP       -> away from zero
ROUND_HALF_DOWN
ROUND_05UP
```

O comportamento para números negativos é o motivo pelo qual "up" e "ceiling" não devem ser tratados como sinônimos.

## 31. `quantize()` impõe o expoente de outro Decimal

```python
from decimal import Decimal


value = Decimal("1.41421356")
rounded = value.quantize(Decimal("1.000"))
print(rounded)
```

```text
1.414
```

O operando da direita funciona como um template de expoente.

## 32. Use um quantum nomeado para trabalho repetido com escala fixa

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")
amount = Decimal("12.345")

print(amount.quantize(CENT, rounding=ROUND_HALF_UP))
```

```text
12.35
```

Um quantum nomeado deixa o contrato de escala visível e reutilizável.

## 33. Faça quantize após operações que podem alterar a escala

Multiplicação e divisão podem produzir mais casas decimais do que um domínio de escala fixa permite.

```python
from decimal import Decimal, ROUND_HALF_EVEN


CENT = Decimal("0.01")
amount = Decimal("10.00")
rate = Decimal("0.0375")
raw_result = amount * rate
final_result = raw_result.quantize(CENT, rounding=ROUND_HALF_EVEN)

print(raw_result)
print(final_result)
```

O local correto para quantizar depende da regra do domínio. Não insira arredondamento automaticamente após toda operação.

## 34. Quantização também pode validar escala

Um validador de escala deve definir tanto a escala permitida quanto a magnitude suportada. `quantize()` pode sinalizar `InvalidOperation` quando o coeficiente do resultado quantizado excederia a precisão do contexto. O validador abaixo trata ambas as condições como traps e limita explicitamente os dígitos de coeficiente aceitos:

```python
from decimal import Context, Decimal, Inexact, InvalidOperation


TWO_PLACES = Decimal("0.01")
MAX_COEFFICIENT_DIGITS = 28
validator = Context(
    prec=MAX_COEFFICIENT_DIGITS,
    traps=[Inexact, InvalidOperation],
)

value = Decimal("3.21")

if not value.is_finite() or len(value.as_tuple().digits) > MAX_COEFFICIENT_DIGITS:
    raise ValueError("unsupported decimal value")

print(value.quantize(TWO_PLACES, context=validator))
```

Um valor como `Decimal("3.214")` gera `Inexact`. Valores grandes demais ou não finitos são rejeitados antes que possam passar como um `NaN` aceito, enquanto `InvalidOperation` também é tratado como proteção defensiva.

## 35. `quantize()` possui uma regra especial de Underflow

Diferentemente de outras operações, `quantize()` nunca sinaliza `Underflow`, mesmo quando o resultado é subnormal e inexato.

Esse é um contrato avançado, mas importa quando monitoramento de sinais faz parte de um design de validação ou controle numérico.

## 36. `round()` e o contexto Decimal interagem de formas diferentes conforme os argumentos

```python
from decimal import Decimal


value = Decimal("2.675")
print(round(value, 2))
```

Com um `ndigits` inteiro, o arredondamento de Decimal respeita o modo de arredondamento do contexto e equivale a quantizar para a potência de dez correspondente.

Por outro lado, `round(decimal_value)` sem `ndigits` retorna um `int`, resolve empates para o par e ignora o modo de arredondamento do contexto Decimal.

## 37. `to_integral_value()` arredonda sem sinalizar `Inexact` ou `Rounded`

```python
from decimal import Decimal, ROUND_HALF_UP


value = Decimal("7.8")
print(value.to_integral_value(rounding=ROUND_HALF_UP))
```

Use quando precisar de um resultado Decimal integral sem esses sinais de arredondamento.

## 38. `to_integral_exact()` relata condições de arredondamento

```python
from decimal import Decimal, Inexact, Rounded, localcontext


with localcontext() as context:
    context.clear_flags()
    result = Decimal("7.8").to_integral_exact()
    print(result)
    print(context.flags[Rounded])
    print(context.flags[Inexact])
```

A variante `exact` é útil quando você precisa monitorar se informação foi descartada.

## 39. Sinais fazem parte do contrato Decimal

Sinais descrevem condições encontradas durante aritmética decimal.

Exemplos importantes incluem:

- `Clamped`;
- `DivisionByZero`;
- `InvalidOperation`;
- `Inexact`;
- `Rounded`;
- `Subnormal`;
- `Overflow`;
- `Underflow`;
- `FloatOperation`.

Um sinal pode definir uma flag, gerar exceção por trap ou fazer ambos nessa sequência.

## 40. Flags são sticky

Depois que uma flag de sinal se torna verdadeira, ela permanece marcada até ser limpa.

```python
from decimal import Decimal, Inexact, localcontext


with localcontext(prec=5) as context:
    context.clear_flags()
    Decimal(1) / Decimal(7)
    print(context.flags[Inexact])
```

```text
True
```

Sempre limpe flags antes de um cálculo que você pretende monitorar de forma independente.

## 41. `Rounded` e `Inexact` não são a mesma condição

`Rounded` significa que dígitos foram descartados.

`Inexact` significa que os dígitos descartados continham informação não-zero, portanto o resultado difere do resultado matemático exato.

Por exemplo, reduzir `5.00` para `5.0` pode sinalizar `Rounded` mesmo sem perda de informação não-zero.

## 42. Traps transformam sinais selecionados em exceções

```python
from decimal import Decimal, DivisionByZero, localcontext


with localcontext() as context:
    context.traps[DivisionByZero] = True
    # Decimal(1) / Decimal(0)  # raises DivisionByZero
```

Um trap é uma regra de imposição. Uma flag é um registro de observação.

## 43. Escolha traps de acordo com o contrato

Políticas possíveis incluem:

```text
monitor and continue -> inspect flags
reject inexact input -> trap Inexact
reject divide by zero -> trap DivisionByZero
reject accidental float conversion -> trap FloatOperation
```

Não habilite todos os traps apenas porque exceções parecem mais seguras. A semântica desejada depende da aplicação.

## 44. `FloatOperation` pode expor fronteiras implícitas com float

```python
from decimal import Decimal, FloatOperation, localcontext


with localcontext() as context:
    context.traps[FloatOperation] = True
    # Decimal(3.14)  # raises FloatOperation
```

Conversão explícita por `Decimal.from_float()` não sinaliza `FloatOperation`, porque a intenção da conversão já está visível.

## 45. Comparação de igualdade com float possui uma exceção especial

Aritmética entre Decimal e float é geralmente rejeitada, mas as regras de comparação são mais sutis.

Quando `FloatOperation` está como trap, comparações de ordenação como `<` podem gerar exceção, enquanto comparações de igualdade continuam permitidas.

Não construa um pipeline numérico em torno de peculiaridades de comparação entre tipos. Normalize as fronteiras numéricas deliberadamente.

## 46. `BasicContext` é útil para depuração

`BasicContext` possui precisão 9, usa `ROUND_HALF_UP` e habilita muitos traps.

Isso torna condições inesperadas rapidamente visíveis durante depuração.

```python
from decimal import BasicContext


print(BasicContext.prec)
print(BasicContext.rounding)
```

## 47. `ExtendedContext` prefere valores-resultados a exceções

`ExtendedContext` possui precisão 9, usa `ROUND_HALF_EVEN` e não possui traps habilitados.

Uma operação como divisão por zero pode, portanto, produzir `Infinity` enquanto registra o sinal em vez de levantar uma exceção imediatamente.

Use esse comportamento somente quando valores numéricos especiais fizerem parte intencional do algoritmo.

## 48. O contexto padrão não é a mesma coisa que `BasicContext`

O contexto padrão comum usa precisão 28 e `ROUND_HALF_EVEN`, com traps habilitados para `Overflow`, `InvalidOperation` e `DivisionByZero`.

Não deduza o comportamento padrão a partir das configurações dos contextos padrão nomeados.

## 49. `IEEEContext()` é novo no Python 3.14

O Python 3.14 adiciona `decimal.IEEEContext(bits)` para criar um contexto configurado para um dos formatos de intercâmbio IEEE suportados.

```python
from decimal import IEEEContext


context = IEEEContext(128)
print(context.prec)
```

Código que precisa rodar em versões anteriores não deve depender dessa API sem uma estratégia de compatibilidade.

## 50. Decimal suporta valores especiais

```python
from decimal import Decimal


values = [
    Decimal("Infinity"),
    Decimal("-Infinity"),
    Decimal("NaN"),
    Decimal("sNaN"),
    Decimal("-0"),
]

for value in values:
    print(value)
```

Esses são valores aritméticos com semântica Decimal definida, não strings comuns de erro.

## 51. Classifique valores especiais antes do processamento comum quando necessário

```python
from decimal import Decimal


value = Decimal("Infinity")
print(value.is_finite())
print(value.is_infinite())
print(value.is_nan())
```

Fronteiras de validação muitas vezes precisam rejeitar valores não finitos antes de persistência ou cálculos posteriores.

## 52. NaN não se comporta como um número comum

Um NaN representa um resultado numérico indefinido ou não representável.

Não dependa de lógica de ordenação comum para valores NaN. Detecte-os explicitamente com `is_nan()` quando o domínio não os permite.

NaNs sinalizantes (`sNaN`) são projetados para sinalizar `InvalidOperation` quando usados na maioria das operações.

## 53. Zero com sinal pode preservar informação direcional

Decimal diferencia representações de zero positivo e negativo:

```python
from decimal import Decimal


positive_zero = Decimal("0")
negative_zero = Decimal("-0")

print(positive_zero == negative_zero)
print(negative_zero.is_signed())
```

Os valores são numericamente iguais mesmo que a informação de sinal permaneça na representação.

## 54. Precisão finita ainda pode causar perda de significância

A aritmética Decimal pode arredondar sempre que um resultado excede a precisão do contexto.

```python
from decimal import Decimal, localcontext


with localcontext(prec=5):
    large = Decimal("10000")
    small = Decimal("0.12345")
    result = large + small
    print(result)
```

O modelo decimal evita erro de representação binária, mas baixa precisão ainda pode descartar dígitos decimais significativos.

## 55. Aumentar a precisão pode fazer parte de uma estratégia numérica

Para cálculos intermediários, pode ser apropriado usar mais precisão do que a saída final precisa e arredondar somente na fronteira exigida.

```python
from decimal import Decimal, localcontext


with localcontext(prec=30):
    ratio = Decimal(1) / Decimal(7)

print(ratio)
```

A precisão de trabalho necessária é uma propriedade do algoritmo e do domínio, não um número mágico universal.

## 56. `fma()` evita arredondamento do produto intermediário

Fused multiply-add calcula:

```text
self * other + third
```

sem arredondar o resultado intermediário da multiplicação.

```python
from decimal import Decimal


value = Decimal("2").fma(Decimal("3"), Decimal("5"))
print(value)
```

```text
11
```

Isso pode importar em fórmulas sensíveis à precisão nas quais um arredondamento intermediário alteraria o resultado final.

## 57. `normalize()` simplifica a representação preservando o valor

```python
from decimal import Decimal


print(Decimal("32.1000").normalize())
```

```text
32.1
```

Use normalização quando a significância codificada por zeros à direita não for necessária. Não normalize automaticamente se a representação carregar significado de domínio.

## 58. Formatação não substitui quantização

```python
from decimal import Decimal


value = Decimal("2.675")
print(f"{value:.2f}")
print(value)
```

Formatação produz texto para apresentação. O objeto Decimal original continua inalterado.

Se cálculos posteriores exigem um valor com escala fixa, crie esse valor numérico explicitamente com a política de arredondamento necessária.

## 59. Faça parsing deliberado de números decimais em JSON

O capítulo anterior de JSON apresentou esta fronteira:

```python
import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
```

`parse_float=Decimal` permite que o decoder construa um Decimal a partir da forma textual do número JSON em vez de primeiro convertê-lo para `float` do Python.

## 60. Codificação JSON precisa de uma política explícita própria

O encoder padrão de `json` não serializa objetos `Decimal` arbitrários como números JSON automaticamente.

Possíveis designs de aplicação incluem:

- converter para string quando o schema externo define uma string;
- usar representação em unidades mínimas inteiras quando esse schema for adequado;
- implementar uma fronteira de encoding personalizada e deliberada;
- usar outra tecnologia de serialização com tipo decimal nativo.

Não converta silenciosamente um Decimal para float apenas para facilitar serialização quando a semântica decimal exata importa.

## 61. Preserve texto decimal nas fronteiras de entrada

Suponha que um formulário forneça:

```text
19.90
```

Prefira:

```python
from decimal import Decimal


raw_value = "19.90"
amount = Decimal(raw_value)
```

em vez de converter o texto para float primeiro e depois para Decimal.

## 62. Fronteiras de banco de dados devem respeitar o tipo numérico do banco

Quando um driver de banco de dados expõe uma coluna numeric ou decimal exata como `Decimal`, manter esse valor como Decimal evita uma ida desnecessária por float.

O comportamento varia entre drivers, então inspecione o contrato real do adaptador em vez de presumir que toda coluna numérica chega com o mesmo tipo Python.

## 63. Contratos de API devem declarar a representação

"Número" frequentemente é vago demais para dados sensíveis a precisão.

Perguntas úteis de contrato incluem:

- O valor é texto de número JSON ou texto dentro de string JSON?
- Quantas casas decimais são permitidas?
- Qual modo de arredondamento se aplica?
- Zeros à direita têm significado?
- Valores não finitos são permitidos?
- Quem executa a quantização final?

Correção numérica começa na fronteira, não na expressão aritmética final.

## 64. Mantenha a política de arredondamento perto da regra de domínio

Um helper pode tornar a política explícita:

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")


def to_cents(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)
```

O nome do helper e seus testes devem explicar por que aquele modo de arredondamento é correto para o domínio que o utiliza.

## 65. Evite mutação oculta do contexto dentro de helpers

Um helper arriscado altera estado ambiente:

```python
from decimal import getcontext


def calculate_something():
    getcontext().prec = 6
    # calculation continues
```

Um design mais seguro:

- usa `localcontext()`;
- aceita um `Context` explícito;
- documenta que mutação do contexto faz parte da API pública.

Política local é mais fácil de raciocinar do que efeitos colaterais globais invisíveis.

## 66. Contextos Decimal e concorrência merecem design deliberado

O contexto decimal ativo é gerenciado de forma independente para contextos de execução conforme o build do Python e o suporte de gerenciamento de contexto.

A regra prática é mais simples: não use mutação descontrolada de contexto ambiente como mecanismo de comunicação entre tarefas concorrentes.

Passe a política explicitamente ou delimite mudanças com `localcontext()` quando isolamento importa.

## 67. Decimal normalmente é mais lento que ponto flutuante binário

A aritmética Decimal fornece semântica decimal mais rica, contexto controlado por software e tratamento de sinais. Esses recursos têm custo.

Não escolha Decimal para toda carga numérica apenas porque ele parece "mais preciso".

Escolha quando representação decimal, controle de arredondamento, auditabilidade ou fronteiras decimais exatas justificarem o trade-off.

## 68. Decimal não é a mesma coisa que aritmética racional

`Decimal("0.1")` pode ser representado exatamente, mas um valor periódico como um terço ainda exige precisão finita durante divisão.

Para algoritmos cujo contrato são razões exatas como `1/3`, o tipo `fractions.Fraction` da biblioteca padrão modela uma forma diferente de exatidão.

A seleção do tipo numérico deve seguir o modelo matemático de que o programa precisa.

## 69. Um cálculo prático com escala fixa

```python
from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")

unit_price = Decimal("19.95")
quantity = 3
discount = Decimal("2.50")

subtotal = unit_price * quantity
final_amount = (subtotal - discount).quantize(
    CENT,
    rounding=ROUND_HALF_UP,
)

print(f"subtotal: {subtotal}")
print(f"final: {final_amount}")
```

```text
subtotal: 59.85
final: 57.35
```

O ponto importante não é este exemplo usar dinheiro. O importante é que representação de entrada, aritmética, escala final e política de arredondamento estejam visíveis.

## 70. Um cálculo prático com precisão local

```python
from decimal import Decimal, getcontext, localcontext


default_precision = getcontext().prec

with localcontext(prec=8):
    result = Decimal(1) / Decimal(7)

print(f"default precision: {default_precision}")
print(f"local result: {result}")
print(f"restored precision: {getcontext().prec}")
```

Com o contexto padrão comum, a saída visível é:

```text
default precision: 28
local result: 0.14285714
restored precision: 28
```

## 71. Um validador prático de escala

```python
from decimal import Context, Decimal, Inexact, InvalidOperation


TWO_PLACES = Decimal("0.01")
MAX_COEFFICIENT_DIGITS = 28
validator = Context(
    prec=MAX_COEFFICIENT_DIGITS,
    traps=[Inexact, InvalidOperation],
)


def normalize_two_places(raw_value: str) -> Decimal:
    value = Decimal(raw_value)

    if (
        not value.is_finite()
        or len(value.as_tuple().digits) > MAX_COEFFICIENT_DIGITS
    ):
        raise ValueError("unsupported decimal value")

    normalized = value.quantize(TWO_PLACES, context=validator)

    if not normalized.is_finite():
        raise ValueError("quantization produced a non-finite result")

    return normalized


for raw_value in [
    "12.50",
    "7.00",
    "3.141",
    "12345678901234567890123456789.00",
    "NaN",
]:
    try:
        normalized = normalize_two_places(raw_value)
    except (Inexact, InvalidOperation, ValueError):
        print(f"rejected: {raw_value}")
    else:
        print(f"accepted: {normalized}")
```

```text
accepted: 12.50
accepted: 7.00
rejected: 3.141
rejected: 12345678901234567890123456789.00
rejected: NaN
```

Esse validador possui duas políticas explícitas: no máximo 28 dígitos de coeficiente e um resultado com duas casas que não descarte dígitos não-zero. Ele também rejeita valores não finitos e trata `InvalidOperation` como trap, portanto uma quantização inválida não pode ser aceita como `NaN`.

## 72. Um monitor prático de sinais

```python
from decimal import Decimal, Inexact, Rounded, localcontext


with localcontext(prec=5) as context:
    context.clear_flags()
    result = Decimal(1) / Decimal(7)

    print(f"result: {result}")
    print(f"rounded: {context.flags[Rounded]}")
    print(f"inexact: {context.flags[Inexact]}")
```

```text
result: 0.14286
rounded: True
inexact: True
```

## 73. Erros comuns

### Erro: construir a partir de float quando a origem original é texto decimal

```python
from decimal import Decimal


bad_boundary = Decimal(0.1)
good_boundary = Decimal("0.1")
```

Os dois construtores preservam valores de origem diferentes.

### Erro: tratar precisão como casas decimais

```python
from decimal import localcontext


with localcontext(prec=2):
    pass
```

`prec=2` significa dois dígitos significativos para aritmética, não duas casas depois do ponto decimal.

### Erro: formatar em vez de definir uma política numérica de arredondamento

```python
from decimal import Decimal


value = Decimal("12.345")
print(f"{value:.2f}")
```

Isso é apresentação. Não transforma `value` em um Decimal com duas casas.

### Erro: ler flags antigas

Se uma operação anterior marcou `Inexact`, uma verificação posterior pode enganar se as flags não forem limpas antes do cálculo monitorado.

### Erro: usar um contexto ambiente como estado compartilhado oculto

Uma função que altera silenciosamente a precisão pode mudar cálculos não relacionados mais tarde no mesmo contexto de execução.

### Erro: converter para float na fronteira final de integração sem verificar o contrato

Uma conversão para float pode ser aceitável para uma API de visualização ou inaceitável para um valor persistido exato. O contrato de destino decide.

## 74. Tabela de decisão

| Requisito | Prefira |
|---|---|
| aritmética binária geral e rápida | `float` |
| representação exata de entrada decimal | `Decimal` a partir de texto ou origem decimal exata |
| escala decimal fixa explícita | `Decimal.quantize()` |
| precisão temporária de trabalho | `localcontext()` |
| política numérica explícita reutilizável | `Context` |
| observar arredondamento sem levantar exceção | flags de sinais |
| rejeitar uma condição aritmética específica | traps |
| preservar exatamente um float existente | `Decimal.from_float()` |
| detectar conversão acidental de float | `FloatOperation` |
| razões racionais exatas | considere `fractions.Fraction` |
| formatação decimal apenas para exibição | especificação de formato / f-string |

## 75. Referência rápida

```text
Decimal("1.25")
Decimal(7)
Decimal.from_float(0.1)
Decimal.from_number(value)        # Python 3.14+

getcontext()
setcontext(context)
localcontext()
localcontext(prec=40)             # keyword attributes: Python 3.11+
Context(prec=28, rounding=...)
Context.create_decimal(value)

value.quantize(Decimal("0.01"))
value.to_integral_value()
value.to_integral_exact()
value.normalize()
value.as_tuple()
value.compare_total(other)
value.fma(other, third)

context.clear_flags()
context.flags[Inexact]
context.flags[Rounded]
context.traps[Inexact] = True
context.traps[FloatOperation] = True

BasicContext
ExtendedContext
DefaultContext
IEEEContext(bits)                 # Python 3.14+
```

## 76. Checklist de design

Antes de escolher ou configurar Decimal, pergunte:

- De onde o valor se origina?
- A origem já existe como float binário?
- Representação decimal exata é necessária?
- Quantos dígitos significativos o cálculo precisa?
- O domínio exige um número fixo de casas decimais?
- Qual regra de arredondamento se aplica e em qual etapa?
- Arredondamento é uma transformação aceita ou uma falha de validação?
- Preciso monitorar `Rounded` ou `Inexact`?
- Algum sinal deve virar exceção por meio de trap?
- `NaN` e infinitos são valores válidos para o domínio?
- Zeros à direita carregam significado?
- Outra biblioteca ou API converterá o valor para float?
- Mutação do contexto ambiente é segura aqui?
- Um `Context` explícito deixaria a política mais clara?
- Testei valores de empate, negativos, zero e limites de escala?
- Estou dependendo de uma API específica de versão?

## 77. Exercício

Construa uma calculadora fictícia de precificação por medição com estes requisitos:

1. Leia preço unitário, quantidade e taxa de ajuste a partir de strings.
2. Converta texto decimal diretamente para `Decimal`.
3. Execute aritmética intermediária com pelo menos 20 dígitos significativos de precisão local.
4. Quantize o valor final para duas casas decimais usando uma regra de arredondamento escolhida explicitamente.
5. Rejeite um preço unitário de entrada que contenha mais de duas casas decimais não-zero tratando `Inexact` como trap durante a validação.
6. Limpe e inspecione flags ao redor do cálculo principal.
7. Mostre se o cálculo principal produziu sinal `Inexact` ou `Rounded` antes da quantização final.
8. Mantenha o contexto ativo original inalterado depois que a função retornar.

Desafios adicionais:

- rejeitar valores não finitos;
- adicionar um teste para caso de arredondamento exatamente no meio;
- aceitar um `Context` explícito como argumento da função;
- serializar o valor final sob um contrato externo de representação documentado.

## 78. Conexões com outros conceitos de Python

`decimal` se conecta diretamente a tópicos já estudados:

- **`float`:** o modelo anterior de representação binária explica por que Decimal existe.
- **Strings:** texto decimal frequentemente é a fronteira de entrada exata mais segura.
- **Funções:** helpers de arredondamento e contextos explícitos transformam política numérica em interfaces reutilizáveis.
- **Exceções:** sinais tratados como traps viram exceções e participam de fluxos normais de validação.
- **Context managers:** `localcontext()` delimita política numérica com `with`.
- **JSON:** `parse_float=Decimal` preserva texto de número JSON como Decimal sem um float Python intermediário.
- **Logging:** flags e falhas de validação podem ser registradas como evidência de runtime sem expor dados sensíveis.
- **Testes:** arredondamento de empate, limites de precisão, flags de sinal e restauração de contexto merecem assertions comportamentais.
- **`itertools`:** pipelines de iteradores que agregam valores Decimal devem preservar o modelo numérico escolhido da origem ao destino.
- **Próximos utilitários de sistema:** valores decimais frequentemente cruzam fronteiras de arquivo, ambiente ou processo externo onde contratos de conversão para texto importam.

## Referências

Referências primárias usadas neste capítulo:

- [Documentação Python 3.14: `decimal` — aritmética decimal de ponto fixo e ponto flutuante](https://docs.python.org/3.14/library/decimal.html)
- [Tutorial Python 3.14: Aritmética de Ponto Flutuante — Problemas e Limitações](https://docs.python.org/3.14/tutorial/floatingpoint.html)
- [Tutorial Python 3.14: aritmética decimal de ponto flutuante](https://docs.python.org/3.14/tutorial/stdlib2.html#decimal-floating-point-arithmetic)
- [Documentação Python 3.14: módulos numéricos e matemáticos](https://docs.python.org/3.14/library/numeric.html)

## Próximo capítulo

Continue com o [Capítulo 09: `os` e `shutil`](../09-os-shutil/README.pt-BR.md).

O próximo capítulo passa de contratos numéricos para contratos de operações do sistema operacional e filesystem: estado do ambiente, interfaces path-like, travessia, metadados, cópia, movimentação, remoção recursiva, segurança de archives e a fronteira entre `pathlib`, `os` e `shutil`.
