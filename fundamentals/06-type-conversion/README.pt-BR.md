<div align="center">

# Conversão de Tipos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: `type()` e `isinstance()`](../05-type-and-isinstance/README.pt-BR.md)

O Capítulo 05 ensinou como inspecionar o tipo que um valor já possui. Este último capítulo de Fundamentos ensina o próximo passo: criar deliberadamente um valor de outro tipo compatível.

Este capítulo foca em conversão explícita. Chamar `int()`, `float()`, `str()` ou `bool()` produz um resultado conforme as regras de conversão daquele tipo. O valor original não muda silenciosamente dentro do objeto que já existia.

O Python também pode realizar algumas conversões implícitas em contextos específicos, como operações numéricas mistas. Esses casos estão fora do escopo deste capítulo; aqui, toda conversão é escrita deliberadamente com uma dessas chamadas embutidas.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Concluir os Capítulos 01 a 05 |
| Tempo estimado de estudo | 60 a 80 minutos |
| Conceitos principais | `int()`, `float()`, `str()`, `bool()`, conversão, `ValueError`, valor-verdade |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- converter texto compatível para `int` e `float`;
- converter valores para `str`;
- explicar que uma conversão cria um valor resultante em vez de alterar o valor original;
- explicar por que `int()` trunca um valor de ponto flutuante em direção a zero em vez de arredondá-lo;
- reconhecer conversões textuais inválidas que geram `ValueError`;
- usar `bool()` de acordo com as regras de valor-verdade do Python;
- explicar por que `bool("False")` é `True`;
- converter o texto retornado por `input()` antes de cálculos numéricos;
- evitar conversões que escondam a intenção ou descartem informação acidentalmente.

## 1. Por que a conversão existe

Programas frequentemente recebem um valor em uma forma e precisam dele em outra. Um terminal fornece os resultados de `input()` como texto, enquanto operações aritméticas normalmente precisam de valores numéricos.

A conversão cria uma ponte explícita entre essas representações.

## 2. As chamadas básicas de conversão

Os nomes dos tipos embutidos podem ser chamados:

```python
integer_value = int(value)
decimal_value = float(value)
text_value = str(value)
boolean_value = bool(value)
```

Leia `int(value)` como "crie um inteiro a partir deste valor compatível". A mesma ideia vale para as outras chamadas.

## 3. Converta texto inteiro com `int()`

Uma string que contém uma representação inteira válida pode ser convertida para `int`:

```python
age_text = "28"
age = int(age_text)

print(age)
print(type(age))
```

Saída esperada:

```text
28
<class 'int'>
```

Os caracteres `"28"` são texto. O resultado `28` é um valor inteiro.

## 4. Converta texto decimal com `float()`

Uma string que contém uma representação de ponto flutuante compatível pode ser convertida para `float`:

```python
temperature_text = "21.5"
temperature = float(temperature_text)

print(temperature)
print(type(temperature))
```

Saída esperada:

```text
21.5
<class 'float'>
```

## 5. Converta valores para texto com `str()`

`str()` cria uma representação em string de um valor:

```python
attempts = 3
message = "Attempts: " + str(attempts)

print(message)
print(type(message))
```

Saída esperada:

```text
Attempts: 3
<class 'str'>
```

Sem a conversão, concatenar uma string e um inteiro com `+` misturaria tipos de operandos incompatíveis.

## 6. A conversão cria um novo resultado

O valor original não se transforma silenciosamente em outro tipo:

```python
price_text = "19.90"
price = float(price_text)

print(type(price_text))
print(type(price))
```

Saída esperada:

```text
<class 'str'>
<class 'float'>
```

`price_text` continua referenciando uma string. `price` referencia o novo resultado de ponto flutuante.

## 7. Uma conversão numérica pode mudar a representação

Um inteiro pode ser convertido para um valor de ponto flutuante:

```python
whole_number = float(8)

print(whole_number)
print(type(whole_number))
```

Saída esperada:

```text
8.0
<class 'float'>
```

A grandeza numérica é a mesma neste caso, mas o tipo resultante é diferente.

## 8. `int()` não arredonda valores de ponto flutuante

Ao converter um número de ponto flutuante finito, `int()` descarta a parte fracionária em direção a zero:

```python
print(int(8.9))
print(int(-8.9))
```

Saída esperada:

```text
8
-8
```

Isso é truncamento, não arredondamento.

## 9. Algumas conversões textuais são inválidas

O texto a seguir é válido para `float()`, mas não para `int()`:

```python
int("8.9")
```

Essa chamada gera `ValueError`.

Quando uma conversão em duas etapas de texto decimal para inteiro for realmente a intenção, deixe as etapas visíveis em vez de presumir que `int()` interpreta texto decimal diretamente.

## 10. Texto numérico inválido pode gerar `ValueError`

Esta chamada também falha:

```python
float("hello")
```

O Python gera `ValueError` porque a string não pode ser interpretada como uma representação de ponto flutuante aceita.

O tratamento detalhado de exceções pertence a uma fase posterior. Por enquanto, reconheça o erro e entenda por que a conversão falhou.

## 11. `bool()` segue o teste de valor-verdade

`bool()` não interpreta palavras humanas. Ele aplica as regras de valor-verdade do Python:

```python
print(bool(""))
print(bool("False"))
print(bool(0))
print(bool(7))
print(bool(None))
```

Saída esperada:

```text
False
True
False
True
False
```

Strings vazias, zero numérico e `None` são falsos. Muitos valores não vazios ou diferentes de zero são verdadeiros.

## 12. `bool("False")` continua sendo `True`

Um erro comum é esperar que o texto seja interpretado como uma palavra booleana:

```python
print(bool("False"))
print(bool("0"))
```

Saída esperada:

```text
True
True
```

As duas strings contêm caracteres, portanto ambas são verdadeiras em contexto booleano.

Transformar palavras textuais como `"true"` e `"false"` em booleanos da aplicação exige uma lógica explícita de interpretação, e não apenas `bool(text)`.

## 13. Booleanos podem ser convertidos para inteiros

Como `bool` é subclasse de `int`, a conversão explícita mapeia os dois valores booleanos para inteiros:

```python
print(int(True))
print(int(False))
```

Saída esperada:

```text
1
0
```

Use isso apenas quando a representação numérica tiver significado real. Uma intenção booleana clara costuma ser melhor do que tratar booleanos casualmente como números.

## 14. `None` pode virar texto ou booleano

Tipos de destino diferentes aplicam regras diferentes:

```python
print(str(None))
print(bool(None))
```

Saída esperada:

```text
None
False
```

`str(None)` cria o texto `"None"`. Ele não cria um marcador especial de valor ausente dentro da string.

## 15. Converta `input()` antes da aritmética numérica

`input()` sempre retorna texto. Converta esse texto antes da aritmética quando o programa espera um número:

```python
age_text = input("Age: ")
age = int(age_text)

print("Next year:", age + 1)
```

Exemplo de interação no terminal:

```text
Age: 28
Next year: 29
```

As teclas digitadas chegam primeiro como texto. A chamada a `int()` cria o inteiro usado no cálculo.

## 16. Converta em uma fronteira clara

Um padrão útil para iniciantes é:

1. receber texto externo;
2. armazená-lo com um nome que deixe sua forma atual clara;
3. convertê-lo uma vez quando o tipo pretendido for conhecido;
4. continuar usando o valor convertido.

Isso evita que o restante do programa carregue texto ambíguo por mais tempo do que o necessário.

## 17. Mantenha conversões em várias etapas legíveis

Conversões podem ser aninhadas, mas nomes intermediários costumam deixar a transformação mais fácil de entender:

```python
number_text = "8.9"
number = float(number_text)
whole_number = int(number)

print(whole_number)
```

Saída esperada:

```text
8
```

O código deixa visíveis as duas transformações: texto para `float` e depois `float` para `int`.

## 18. Uma conversão pode descartar informação

Converter `8.9` para `8` perde a parte fracionária.

Antes de converter, pergunte se o tipo de destino consegue representar tudo o que você ainda precisa. Uma conversão bem-sucedida pode continuar sendo uma decisão ruim se descartar informação significativa.

## 19. Conversão e validação são trabalhos diferentes

Uma conversão bem-sucedida significa que o Python conseguiu criar o valor solicitado. Isso não prova que o valor faça sentido para sua aplicação.

Por exemplo:

```python
quantity = int("-4")
```

A conversão em si é válida. Um programa futuro ainda pode rejeitar quantidades negativas conforme suas próprias regras.

Conversão responde "esta representação pode virar este tipo?". Validação da aplicação responde outra pergunta.

## 20. Não converta apenas para fazer um erro desaparecer

Uma conversão deve representar a intenção do programa.

Transformar tudo em texto ou forçar tudo para número pode esconder um erro de modelagem em vez de resolvê-lo. Prefira conversões nos pontos em que um valor realmente atravessa de uma representação para outra.

## 21. Exemplo prático: converta antes do cálculo

Aqui um preço chega como texto:

```python
price_text = "19.90"
price = float(price_text)
shipping = 2.50
total = price + shipping

print(total)
```

Saída esperada:

```text
22.4
```

A conversão acontece antes da aritmética, então os dois operandos da soma são numéricos.

## 22. Erros comuns

Observe estes padrões:

- supor que `int(8.9)` arredonda para `9`;
- esperar que `int("8.9")` funcione apenas porque o texto representa um número;
- esperar que `bool("False")` retorne `False`;
- converter um valor sem considerar perda de informação;
- converter repetidamente o mesmo valor de um tipo para outro sem um motivo claro;
- esquecer que `input()` retorna texto.

## 23. Referência rápida

| Expressão | Resultado | Significado |
|---|---|---|
| `int("28")` | `28` | Converter texto inteiro válido |
| `float("21.5")` | `21.5` | Converter texto decimal compatível |
| `float(8)` | `8.0` | Criar ponto flutuante a partir de inteiro |
| `int(8.9)` | `8` | Truncar um float finito em direção a zero |
| `str(28)` | `"28"` | Criar texto |
| `bool(0)` | `False` | Aplicar teste de valor-verdade |
| `bool("False")` | `True` | Strings não vazias são verdadeiras |

## 24. Exercício

Escreva um pequeno programa interativo que:

1. peça uma quantidade inteira;
2. peça um preço decimal;
3. converta os dois resultados de `input()`;
4. calcule `quantity * price`;
5. exiba o resultado.

Teste uma vez com texto numérico válido. Depois, digite deliberadamente um texto incompatível e observe o erro sem tentar tratá-lo ainda.

## 25. Autoavaliação

Antes de sair de Fundamentos, confirme que você consegue responder a estas perguntas:

- Qual tipo `input()` retorna?
- Por que `int("8.9")` falha enquanto `float("8.9")` funciona?
- `int(8.9)` arredonda?
- Por que `bool("False")` é verdadeiro?
- Converter `price_text` para `float` altera o valor armazenado em `price_text`?
- Quando uma conversão pode perder informação?

## 26. Exemplo: conversões básicas

O primeiro exemplo do repositório mantém os valores textuais originais separados dos valores convertidos:

```python
age_text = "28"
temperature_text = "21.5"

age = int(age_text)
temperature = float(temperature_text)
summary = str(age) + " years"

print(age, type(age))
print(temperature, type(temperature))
print(summary, type(summary))
```

Saída esperada:

```text
28 <class 'int'>
21.5 <class 'float'>
28 years <class 'str'>
```

## 27. Exemplo: surpresas da conversão

O segundo exemplo registra comportamentos importantes:

```python
print(int(8.9))
print(int(-8.9))
print(bool(""))
print(bool("False"))
print(bool(0))
print(bool(1))
```

Saída esperada:

```text
8
-8
False
True
False
True
```

## 28. Execute os exemplos

A partir da raiz do repositório:

```bash
python fundamentals/06-type-conversion/examples/conversion_basics.py
python fundamentals/06-type-conversion/examples/conversion_surprises.py
```

Os dois exemplos são determinísticos, não interativos, não usam rede nem dependências externas e são adequados para execução automática.

## 29. Execute as verificações do repositório

Depois de editar o capítulo ou os exemplos:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

## 30. Fase 1 concluída

Com este capítulo, a trilha de Fundamentos está concluída.

Agora você consegue executar um arquivo Python, exibir e receber informações, armazenar valores, reconhecer e inspecionar tipos comuns e converter deliberadamente valores compatíveis. O roadmap continua com a **Fase 2: Textos e números**.

## Referências oficiais

- [Funções embutidas do Python — `int()`](https://docs.python.org/3/library/functions.html#int)
- [Funções embutidas do Python — `float()`](https://docs.python.org/3/library/functions.html#float)
- [Funções embutidas do Python — `str()`](https://docs.python.org/3/library/functions.html#str)
- [Funções embutidas do Python — `bool()`](https://docs.python.org/3/library/functions.html#bool)
- [Tipos embutidos do Python — teste de valor-verdade](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
- [Exceções embutidas do Python — `ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: `type()` e `isinstance()`](../05-type-and-isinstance/README.pt-BR.md)
