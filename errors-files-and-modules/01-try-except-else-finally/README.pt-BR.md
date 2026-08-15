<div align="center">

# Tratando Exceções com `try`, `except`, `else` e `finally`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Erros, Arquivos e Módulos](../README.pt-BR.md) · [← Fase anterior: Comentários e Documentação](../../comments-and-documentation/README.pt-BR.md)

Programas nem sempre seguem o caminho feliz. Uma conversão pode receber texto inválido, uma divisão pode usar zero, uma busca em dicionário pode não encontrar uma chave ou uma operação futura com arquivos pode falhar.

Python representa muitas dessas falhas de runtime com **exceções**. Uma instrução `try` permite que o programa defina o que deve acontecer quando uma exceção específica interrompe a execução normal.

Este capítulo se concentra em **tratar exceções que já acontecem**. O Capítulo 02 abordará como criar exceções deliberadamente com `raise` e como definir classes simples de exceções personalizadas.

**Tempo estimado de estudo:** 90–120 minutos.

**Requisito de Python:** Python 3.10 ou mais recente. Os exemplos reutilizam sintaxe moderna de type hints, como `int | None`, apresentada na fase de Funções.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar a diferença entre um erro de sintaxe e uma exceção de runtime;
- descrever como uma exceção interrompe o fluxo normal de controle;
- usar `try` e uma cláusula `except` específica;
- tratar diferentes tipos de exceção com handlers separados;
- acessar uma exceção capturada com `as` quando seus detalhes forem úteis;
- explicar por que a ordem dos handlers importa;
- usar `else` para código que deve executar somente quando o bloco `try` termina normalmente;
- usar `finally` para trabalho de limpeza que deve acontecer em todos os caminhos de saída;
- explicar o que acontece quando nenhuma cláusula `except` corresponde à exceção;
- manter blocos `try` estreitos o suficiente para mostrar qual operação pode falhar;
- evitar esconder falhas não relacionadas com handlers amplos demais;
- distinguir tratar uma exceção de prevenir todo estado inválido possível;
- rastrear o caminho de execução por `try`, `except`, `else` e `finally`.

## 1. Fluxo normal e fluxo excepcional

A maior parte do código segue uma sequência normal:

```text
instrução 1
    ↓
instrução 2
    ↓
instrução 3
```

Uma exceção muda esse caminho:

```text
instrução 1
    ↓
operação com falha
    ↓ exceção levantada
procurar um handler correspondente
```

Se existir um handler correspondente, a execução pode continuar a partir da estrutura de tratamento. Se não existir, a exceção continua para fora através do código ao redor e das chamadas de função.

Esse é um mecanismo de fluxo de controle diferente de `if`, loops e valores retornados normalmente.

## 2. Erros de sintaxe e exceções não são a mesma coisa

Um **erro de sintaxe** significa que Python não consegue analisar o código-fonte de acordo com a gramática da linguagem.

Por exemplo, este código-fonte é inválido:

```python
if score > 70
    print("Ready")
```

A ausência dos dois-pontos impede que o arquivo seja analisado normalmente.

Uma **exceção de runtime** acontece depois que Python já possui código válido para executar, mas uma operação não consegue terminar normalmente.

```python
number = int("seven")
```

A sintaxe é válida. A conversão falha em runtime e levanta `ValueError`.

Este capítulo trata principalmente de exceções de runtime.

## 3. Como pensar em uma exceção não tratada

Considere:

```python
number = int("seven")
print(number)
```

`int("seven")` não consegue produzir o inteiro solicitado. Python levanta `ValueError` antes que `print(number)` possa executar.

Quando uma exceção permanece sem tratamento em um script normal, a execução é interrompida e Python exibe um traceback mostrando por onde a falha se propagou.

O modelo inicial importante é:

```text
a operação não consegue terminar
        ↓
o objeto exceção é levantado
        ↓
o caminho normal é interrompido
        ↓
Python procura um handler correspondente
```

## 4. O menor `try` e `except` útil

```python
try:
    number = int("seven")
except ValueError:
    print("Invalid integer")
```

Saída:

```text
Invalid integer
```

O bloco `try` contém código que pode levantar uma exceção.

O bloco `except ValueError` descreve o que fazer se um `ValueError` alcançar essa instrução `try`.

## 5. Leia a estrutura como dois caminhos possíveis

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

Um rastreamento útil é:

```text
try int(text)
    ├─ sucesso → continuar após a instrução try
    └─ ValueError → executar except ValueError
```

O bloco `except` não executa quando a operação protegida tem sucesso.

## 6. Capture a exceção que você espera

Prefira nomear a falha que o código sabe tratar:

```python
try:
    score = int("ninety")
except ValueError:
    print("Score must be an integer")
```

Isso informa ao leitor que texto numérico inválido é um caso de falha esperado aqui.

Handlers específicos também permitem que erros de programação não relacionados continuem aparecendo, em vez de serem silenciosamente convertidos para a mesma resposta alternativa.

## 7. Um `try` bem-sucedido ignora seus handlers `except`

```python
try:
    score = int("90")
except ValueError:
    print("Invalid score")

print(score)
```

Saída:

```text
90
```

Nenhum `ValueError` ocorreu, então o handler foi ignorado.

## 8. O restante de um bloco `try` é ignorado depois de uma exceção

```python
try:
    number = int("seven")
    print("Conversion succeeded")
except ValueError:
    print("Conversion failed")
```

Saída:

```text
Conversion failed
```

Quando `int("seven")` levanta `ValueError`, Python não continua para a próxima instrução dentro desse mesmo bloco `try`.

O controle passa para o handler correspondente.

## 9. Acesse o objeto exceção com `as`

Um handler pode vincular a exceção capturada a um nome local:

```python
try:
    number = int("seven")
except ValueError as error:
    print(type(error).__name__)
```

Saída:

```text
ValueError
```

O nome depois de `as` se refere ao objeto exceção enquanto o handler está executando.

Use-o quando o tipo ou os detalhes da exceção realmente ajudarem em logging, diagnóstico ou uma explicação para o usuário.

## 10. Não construa lógica baseada na mensagem exata da exceção

O texto de uma exceção é útil para pessoas, mas a redação exata pode mudar entre versões do Python ou detalhes de implementação.

Prefira ramificar pelo **tipo** da exceção:

```python
try:
    number = int("seven")
except ValueError:
    print("Invalid integer")
```

em vez de verificar se a mensagem da exceção contém uma frase específica.

## 11. Falhas diferentes podem precisar de handlers diferentes

Um cálculo pode falhar durante a conversão do texto ou durante a divisão:

```python
try:
    numerator = float("12")
    denominator = float("0")
    result = numerator / denominator
except ValueError:
    print("Invalid numeric text")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Saída:

```text
Cannot divide by zero
```

Python procura os handlers na ordem e executa o primeiro que corresponde à exceção levantada.

## 12. A ordem dos handlers importa

Classes de exceção formam uma hierarquia. Um handler para uma classe base mais geral também pode corresponder às subclasses.

Quando um handler específico e um mais amplo estiverem presentes, coloque o específico primeiro:

```python
try:
    value = int(text)
except ValueError:
    print("Invalid integer")
except Exception:
    print("Unexpected application error")
```

Colocar `except Exception` primeiro tornaria o `except ValueError` posterior inalcançável para um `ValueError`, porque o handler mais amplo já corresponderia a ele.

## 13. Um handler pode corresponder a uma tupla de tipos de exceção

Se várias falhas realmente precisarem da mesma resposta, uma cláusula `except` pode nomear uma tupla:

```python
try:
    result = int(text) / divisor
except (ValueError, ZeroDivisionError):
    print("Could not calculate the result")
```

Isso é útil somente quando o mesmo comportamento de recuperação faz sentido para todas as exceções listadas.

Handlers separados são mais claros quando falhas diferentes exigem explicações ou caminhos de recuperação diferentes.

## 14. `else` descreve o caminho exclusivo de sucesso

Uma instrução `try` pode incluir `else`:

```python
try:
    score = int("90")
except ValueError:
    print("Invalid score")
else:
    print(f"Parsed score: {score}")
```

Saída:

```text
Parsed score: 90
```

O bloco `else` executa quando o bloco `try` termina normalmente sem exceção e sem uma saída antecipada de fluxo como `return`, `break` ou `continue`.

## 15. Por que não colocar todo o código de sucesso dentro de `try`?

Isto funciona:

```python
try:
    score = int(text)
    print(f"Parsed score: {score}")
except ValueError:
    print("Invalid score")
```

Mas a chamada `print()` não é a operação que esperamos que levante `ValueError`.

Usar `else` pode manter a região protegida menor:

```python
try:
    score = int(text)
except ValueError:
    print("Invalid score")
else:
    print(f"Parsed score: {score}")
```

Agora a estrutura comunica com mais precisão qual operação pertence à fronteira de falha esperada.

## 16. Mantenha o bloco `try` estreito

Um bloco `try` grande pode tornar difícil saber qual instrução produziu a exceção.

Prefira:

```python
try:
    quantity = int(text)
except ValueError:
    print("Invalid quantity")
else:
    total = quantity * unit_price
    print(total)
```

quando somente a conversão deve falhar com `ValueError`.

Blocos `try` estreitos tornam as fronteiras de exceção mais fáceis de inspecionar e reduzem a chance de tratar acidentalmente uma falha não relacionada.

## 17. `finally` descreve a limpeza que precisa acontecer

Um bloco `finally` executa enquanto a instrução `try` está sendo encerrada, tanto se o trabalho protegido teve sucesso quanto se um handler correspondente executou ou uma exceção não tratada continua se propagando.

```python
try:
    number = int("12")
except ValueError:
    print("Invalid integer")
finally:
    print("Finished conversion attempt")
```

Saída:

```text
Finished conversion attempt
```

O bloco `finally` trata de limpeza e finalização garantida, não de decidir se a operação original teve sucesso.

## 18. `finally` também executa depois de uma exceção tratada

```python
try:
    number = int("twelve")
except ValueError:
    print("Invalid integer")
finally:
    print("Finished conversion attempt")
```

Saída:

```text
Invalid integer
Finished conversion attempt
```

O handler responde ao `ValueError`. O bloco `finally` ainda executa depois.

## 19. `finally` também executa quando uma exceção permanece sem tratamento

Conceitualmente:

```python
try:
    result = 10 / 0
finally:
    print("Cleanup runs")
```

`ZeroDivisionError` não é tratado aqui, então continua se propagando depois que `finally` termina.

A limpeza executa, mas a exceção não é magicamente convertida em sucesso.

## 20. Combine `try`, `except`, `else` e `finally`

```python
try:
    score = int("90")
except ValueError:
    print("except: invalid score")
else:
    print(f"else: parsed {score}")
finally:
    print("finally: attempt finished")
```

Saída:

```text
else: parsed 90
finally: attempt finished
```

A estrutura separa quatro responsabilidades:

| Cláusula | Responsabilidade |
|---|---|
| `try` | executar trabalho que pode levantar uma exceção esperada |
| `except` | tratar uma falha correspondente |
| `else` | continuar o caminho exclusivo de sucesso |
| `finally` | executar limpeza em todos os caminhos de saída |

## 21. Rastreie uma falha tratada por todas as cláusulas

```python
try:
    score = int("ninety")
except ValueError:
    print("except: invalid score")
else:
    print(f"else: parsed {score}")
finally:
    print("finally: attempt finished")
```

Saída:

```text
except: invalid score
finally: attempt finished
```

Rastreamento:

```text
entrar em try
    ↓
int("ninety") levanta ValueError
    ↓
o except correspondente executa
    ↓
else é ignorado
    ↓
finally executa
    ↓
continuar após a instrução try
```

## 22. Se nenhum handler corresponder, a exceção se propaga

```python
try:
    result = "12" + 3
except ValueError:
    print("Invalid value")
```

A operação levanta `TypeError`, não `ValueError`.

Como o handler não corresponde, o `TypeError` continua para fora em busca de handlers ao redor ou, se nenhum existir, chega ao interpretador.

Esse comportamento é útil. Um handler não deve fingir que se recuperou de uma falha que não entende.

## 23. Exceções podem atravessar fronteiras de funções

```python
def parse_score(text: str) -> int:
    return int(text)


try:
    score = parse_score("ninety")
except ValueError:
    print("Invalid score")
```

Saída:

```text
Invalid score
```

`parse_score()` não trata a exceção. O `ValueError` se propaga de volta ao chamador, onde o chamador decide tratá-lo.

Isso conecta o fluxo de exceções diretamente à pilha de chamadas estudada na Fase 5.

## 24. Decida onde uma exceção pode ser tratada de forma significativa

Nem toda função deve capturar toda exceção que pode encontrar.

Uma pergunta de design útil é:

```text
Esta camada sabe qual recuperação ou explicação faz sentido?
    sim → o tratamento pode ficar aqui
    não → deixe a exceção se propagar
```

Um helper de parsing de baixo nível pode simplesmente deixar `ValueError` se propagar. Uma função coordenadora voltada ao usuário pode saber como transformar essa falha em uma mensagem útil.

Isso é uma diretriz de design, não uma regra de sintaxe do Python.

## 25. Evite `except:` sem tipo no tratamento comum de aplicações

Um handler sem tipo é assim:

```python
try:
    value = int(text)
except:
    print("Something failed")
```

Ele captura exceções derivadas de `BaseException`, direta ou indiretamente, incluindo exceções de controle como `KeyboardInterrupt` e `SystemExit`, que aplicações normalmente não deveriam engolir acidentalmente.

Para falhas comuns de aplicação, capture os tipos específicos de exceção que você espera.

## 26. `except Exception` também é amplo

Isto é mais estreito que `except:` sem tipo:

```python
try:
    value = int(text)
except Exception:
    print("Operation failed")
```

`Exception` é a classe base comum da maioria das exceções built-in de nível de aplicação, então ainda pode esconder muitos bugs não relacionados quando usado sem cuidado.

Um handler amplo pode ser apropriado em uma fronteira deliberada, como uma camada superior de logging, mas código iniciante normalmente deve começar por exceções específicas e esperadas.

## 27. Exceções built-in comuns que você encontrará

| Exceção | Situação típica para iniciantes |
|---|---|
| `ValueError` | um valor tem o tipo geral correto, mas um valor inválido, como `int("seven")` |
| `TypeError` | uma operação recebe um tipo inadequado, como somar uma string e um inteiro |
| `ZeroDivisionError` | divisão ou módulo usa zero como divisor |
| `KeyError` | uma busca em dicionário pede uma chave ausente com `mapping[key]` |
| `IndexError` | um índice de sequência está fora do intervalo disponível |
| `FileNotFoundError` | o caminho solicitado não existe ao abrir um arquivo |

O objetivo não é memorizar toda exceção built-in agora. Aprenda a ler o tipo da exceção e entender qual operação a produziu.

## 28. Exceções e validação são ferramentas diferentes

Às vezes uma condição simples pode impedir uma operação inválida:

```python
if denominator == 0:
    print("Cannot divide by zero")
else:
    print(numerator / denominator)
```

Em outros casos, uma API naturalmente sinaliza falha levantando uma exceção:

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

Não transforme isso em uma regra rígida de que exceções são sempre melhores ou sempre piores que validação.

Escolha a fronteira mais clara para a operação e para a API que você está usando.

## 29. Um handler deve definir um caminho real de recuperação

Este código captura um erro, mas não entrega informação útil ao chamador:

```python
try:
    number = int(text)
except ValueError:
    pass
```

A exceção desaparece silenciosamente.

Tratamento silencioso é perigoso quando o programa continua com estado incompleto ou incorreto.

Prefira um handler que retorne deliberadamente um fallback, peça nova entrada em um programa interativo, registre a falha ou comunique o que aconteceu.

## 30. Retornar um fallback pode ser um contrato explícito

```python
def parse_integer(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None
```

Aqui `None` significa explicitamente que o parsing não produziu um inteiro.

O chamador precisa então tratar os dois resultados possíveis:

```python
result = parse_integer("seven")

if result is None:
    print("Invalid integer")
else:
    print(result)
```

Isso combina tratamento de exceções com o modelo de fluxo de dados com `None` da Fase 5.

## 31. Exemplo prático: divisão segura a partir de texto

```python
def safe_divide(numerator_text: str, denominator_text: str) -> str:
    try:
        numerator = float(numerator_text)
        denominator = float(denominator_text)
        result = numerator / denominator
    except ValueError:
        return "invalid number"
    except ZeroDivisionError:
        return "division by zero"
    else:
        return f"result: {result:.2f}"
```

Chamadas de exemplo:

```python
print(safe_divide("12", "4"))
print(safe_divide("twelve", "4"))
print(safe_divide("12", "0"))
```

Saída:

```text
result: 3.00
invalid number
division by zero
```

A função distingue falha de conversão de falha aritmética e retorna um resultado determinístico para cada caminho esperado.

## 32. Loops podem tratar um item ruim sem descartar todos os bons

```python
values = ["10", "twenty", "30"]
parsed_values = []

for text in values:
    try:
        parsed_values.append(int(text))
    except ValueError:
        print(f"Skipped invalid value: {text}")

print(parsed_values)
```

Saída:

```text
Skipped invalid value: twenty
[10, 30]
```

O handler fica dentro do loop porque cada item é uma tentativa de conversão independente.

Isso é diferente de envolver o loop inteiro em um grande bloco `try`, onde o primeiro item inválido poderia interromper as iterações restantes.

## 33. Mantenha efeitos colaterais depois do trabalho arriscado ter sucesso quando possível

Suponha que uma operação possa falhar durante o parsing. Muitas vezes é mais claro fazer o parsing primeiro e só atualizar estado compartilhado depois do sucesso:

```python
try:
    quantity = int(text)
except ValueError:
    print("Invalid quantity")
else:
    quantities.append(quantity)
```

Isso reduz a chance de deixar estado parcialmente atualizado depois de uma falha.

## 34. `finally` não é um bom lugar para `return`

Um `return` dentro de `finally` pode substituir um valor de retorno anterior e até suprimir uma exceção que estava se propagando.

Evite este padrão:

```python
def calculate() -> int:
    try:
        return 10 // 0
    finally:
        return 0
```

O `return` de `finally` esconde o `ZeroDivisionError`.

Use `finally` para limpeza. Mantenha decisões normais de valor retornado nos caminhos normal, tratado ou de sucesso.

## 35. O trabalho futuro com arquivos normalmente preferirá `with`

`finally` é uma ferramenta geral de limpeza. No capítulo de arquivos, você aprenderá que a instrução `with` empacota padrões comuns de gerenciamento de recursos em uma interface mais clara.

Por exemplo, arquivos normalmente são gerenciados com um context manager em vez de reproduzir manualmente todos os caminhos de limpeza.

Esse capítulo posterior se apoia diretamente na ideia de limpeza introduzida aqui.

## 36. Erro comum: capturar o tipo de exceção errado

```python
try:
    result = 10 / 0
except ValueError:
    print("Invalid value")
```

Isso não trata a falha porque divisão por zero levanta `ZeroDivisionError`.

Leia o traceback e faça o handler corresponder à falha real da qual você pretende se recuperar.

## 37. Erro comum: deixar o bloco `try` enorme

```python
try:
    quantity = int(text)
    total = quantity * unit_price
    report = build_report(total)
    save_result(report)
except ValueError:
    print("Invalid quantity")
```

Se uma operação posterior também puder levantar `ValueError`, o handler pode tratar acidentalmente outro bug como se fosse entrada inválida do usuário.

Proteja a menor região prática cujas falhas esperadas você entende.

## 38. Erro comum: engolir toda exceção

```python
try:
    process_data()
except Exception:
    pass
```

Isso pode esconder erros de programação, suposições inválidas e informação importante de diagnóstico.

O tratamento só é útil quando o programa possui uma resposta deliberada para a falha.

## 39. Erro comum: usar exceções como ramificação invisível

Tratamento de exceções deve deixar fronteiras de falha mais claras, não transformar decisões comuns em um labirinto.

Se uma condição já é conhecida e simples de testar, um `if` normal pode comunicar melhor a decisão.

Se uma operação naturalmente informa falha por meio de uma exceção, tratar essa exceção pode ser o design mais claro.

## 40. Erro comum: assumir que `finally` significa sucesso

`finally` significa que o caminho de limpeza executa. Ele não diz nada sobre sucesso.

```text
sucesso              → finally executa
exceção tratada       → finally executa
exceção não tratada   → finally executa, depois a exceção continua
```

Mantenha trabalho exclusivo de sucesso em `else` ou depois de uma operação concluída com sucesso.

## 41. Exercício

Construa um pequeno parser de scores que trate texto inválido com segurança.

Requisitos:

1. Crie `parse_score(text: str) -> int | None`.
2. Dentro da função, tente converter `text` com `int()`.
3. Capture `ValueError` e retorne `None`.
4. Use uma cláusula `else` para retornar o inteiro convertido com sucesso.
5. Crie uma lista contendo pelo menos três strings, incluindo um inteiro inválido.
6. Percorra a lista e chame `parse_score()` para cada item.
7. Imprima uma mensagem clara para valores inválidos e imprima o inteiro para valores válidos.
8. Adicione um bloco `finally` dentro de `parse_score()` que imprima uma mensagem curta e determinística de limpeza para cada tentativa.
9. Antes de executar o código, desenhe os caminhos possíveis por `try`, `except`, `else` e `finally`.

Desafio extra: decida se imprimir a partir de `finally` pertence ao design final ou se deve ser removido depois de terminar o rastreamento do exercício.

## 42. Checklist de revisão

Agora você deve conseguir responder:

- Qual é a diferença entre sintaxe Python inválida e uma exceção de runtime?
- O que acontece com as instruções restantes de um bloco `try` depois que uma exceção é levantada?
- Por que `except ValueError` normalmente deve ser preferido a `except:` sem tipo quando `ValueError` é a falha esperada?
- Quando uma cláusula `else` executa?
- Quando uma cláusula `finally` executa?
- O que acontece quando nenhuma cláusula `except` corresponde?
- Por que um bloco `try` grande pode esconder a fonte real de uma falha?
- Por que a ordem dos handlers importa?
- O que `except Exception` captura de forma ampla e por que deve ser usado deliberadamente?
- Por que o código deve evitar depender da redação exata de mensagens de exceção?
- Como uma função pode deixar uma exceção se propagar para um chamador que sabe tratá-la?
- Como o fluxo de exceções se conecta à pilha de chamadas de função?

## 43. Resumo para consulta rápida

| Situação | Abordagem útil |
|---|---|
| Operação pode levantar uma exceção esperada | `try` estreito + `except` específico |
| Falhas diferentes precisam de respostas diferentes | cláusulas `except` separadas |
| Vários tipos de exceção compartilham uma resposta | tupla em uma cláusula `except` |
| Precisa do objeto exceção capturado | `except SomeError as error` |
| Trabalho deve executar somente depois de `try` bem-sucedido | `else` |
| Limpeza deve acontecer em todo caminho de saída | `finally` |
| Nenhum handler entende a falha | deixe a exceção se propagar |
| Handler captura coisas demais | estreite o tipo da exceção ou o bloco `try` |
| Precisa ramificar pela mensagem exata do erro | evite; ramifique pelo tipo da exceção |
| Precisa criar uma exceção deliberadamente | Capítulo 02: `raise` e exceções personalizadas |

## 44. Limite de escopo deste capítulo

Este capítulo deliberadamente **não** ensina em profundidade ainda:

- `raise` e criação explícita de exceções;
- classes de exceção personalizadas;
- encadeamento de exceções com `raise ... from ...`;
- grupos de exceção e `except*`;
- abertura de arquivos e context managers;
- logging de tracebacks de exceção;
- estratégias avançadas de retry.

Essas ideias ficam mais fáceis depois que o modelo básico de handlers está estável.

## 45. Para onde a Fase 7 segue

A sequência começa assim:

```text
operação em runtime
        ↓
uma exceção pode ocorrer
        ↓
try / except / else / finally
        ↓
próximo: levantar exceções deliberadamente com raise
        ↓
arquivos e dados estruturados
        ↓
módulos e pacotes
```

Próximo capítulo planejado: **Levantando Exceções e Exceções Personalizadas**.

## Referências oficiais

- [Python 3.13 Tutorial: Errors and Exceptions](https://docs.python.org/3.13/tutorial/errors.html)
- [Python 3.13 Language Reference: The `try` statement](https://docs.python.org/3.13/reference/compound_stmts.html#the-try-statement)
- [Python 3.13 Execution Model: Exceptions](https://docs.python.org/3.13/reference/executionmodel.html#exceptions)
- [Python 3.13 Built-in Exceptions](https://docs.python.org/3.13/library/exceptions.html)