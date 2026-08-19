<div align="center">

# Levantando Exceções e Criando Exceções Personalizadas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Erros, Arquivos e Módulos](../README.pt-BR.md) · [← Capítulo anterior: Tratando Exceções](../01-try-except-else-finally/README.pt-BR.md)

O Capítulo 01 se concentrou em **tratar exceções que já acontecem**. Este capítulo acrescenta o outro lado do contrato: decidir quando o seu próprio código deve informar deliberadamente que uma operação não pode continuar normalmente.

Python usa a instrução `raise` para esse propósito. Uma função pode validar suas entradas ou seu estado, levantar uma exceção apropriada quando não consegue cumprir seu contrato e deixar que um chamador decida onde a recuperação ou a explicação deve acontecer.

O capítulo também introduz **classes de exceção personalizadas**. Esta é uma introdução restrita à herança de classes especificamente para exceções, não um capítulo completo de programação orientada a objetos.

**Tempo estimado de estudo:** 90–120 minutos.

**Requisito de Python:** Python 3.10 ou mais recente. Os exemplos reutilizam anotações modernas como `list[str]` e os conceitos de tratamento de exceções do Capítulo 01.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar a diferença entre tratar uma exceção e levantar uma exceção;
- usar `raise` para sinalizar deliberadamente um valor ou estado inválido;
- escolher uma exceção built-in adequada para falhas comuns de validação;
- escrever mensagens de exceção úteis sem tratar o texto da mensagem como uma API programática;
- explicar por que levantar uma exceção interrompe o caminho normal atual;
- deixar exceções se propagarem até uma camada capaz de tratá-las de forma significativa;
- relançar a exceção atualmente tratada com um `raise` sem expressão;
- traduzir uma exceção em outra com `raise ... from ...`;
- explicar o propósito do encadeamento explícito de exceções;
- definir uma classe de exceção personalizada simples;
- escolher quando uma exceção personalizada acrescenta significado útil ao domínio;
- capturar uma exceção personalizada sem esconder falhas não relacionadas;
- distinguir `raise` de `assert`;
- evitar designs de exceção amplos, vagos ou desnecessários.

## 1. Tratar e levantar são responsabilidades diferentes

O Capítulo 01 usou `except` para responder a uma falha:

```python
try:
    number = int(text)
except ValueError:
    print("Invalid integer")
```

Este capítulo se concentra no código que **cria deliberadamente o sinal de falha**:

```python
if score < 0:
    raise ValueError("score cannot be negative")
```

As duas responsabilidades se conectam assim:

```text
a função chamada detecta uma condição que não pode aceitar
        ↓
a função chamada levanta uma exceção
        ↓
a execução normal daquela chamada é interrompida
        ↓
a exceção se propaga para fora
        ↓
um chamador adequado pode tratá-la
```

Uma função não precisa saber como todo chamador irá se recuperar. Ela precisa informar a falha com precisão suficiente para que os chamadores possam tomar essa decisão.

## 2. A sintaxe básica de `raise`

A forma mais comum para iniciantes é:

```python
raise ValueError("score must be between 0 and 100")
```

`ValueError` é a classe da exceção. O texto passado a ela se torna informação de diagnóstico útil carregada pela instância da exceção.

A sintaxe geral também permite relançar e encadear exceções, assuntos que aparecem mais adiante neste capítulo.

## 3. Levantar uma exceção interrompe o caminho normal atual

Considere:

```python
def validate_score(score: int) -> int:
    if score > 100:
        raise ValueError("score cannot exceed 100")
    print("Validation finished")
    return score
```

Se `score` for `120`, a execução alcança `raise`. O `print()` e o `return` posteriores não executam nessa chamada, a menos que a exceção seja tratada dentro de alguma estrutura ao redor antes que o controle a deixe.

Conceitualmente:

```text
score = 120
    ↓
a condição é verdadeira
    ↓
raise ValueError(...)
    ↓
o caminho normal termina aqui
    ↓
procurar para fora um handler correspondente
```

Esse é o mesmo modelo de propagação estudado no Capítulo 01, mas agora o seu próprio código inicia deliberadamente o caminho excepcional.

## 4. Levante uma exceção quando uma função não puder cumprir seu contrato

Uma forma útil de pensar em validação é por meio do contrato da função.

Suponha que esta função prometa aceitar somente percentuais de 0 a 100:

```python
def normalize_percentage(value: int) -> int:
    if not 0 <= value <= 100:
        raise ValueError("value must be between 0 and 100")
    return value
```

Para `75`, a função consegue cumprir seu contrato e retorna normalmente.

Para `130`, retornar o valor como se tudo estivesse válido violaria o contrato. Levantar `ValueError` torna o estado inválido explícito.

## 5. Guard clauses mantêm os caminhos inválidos perto do início

A validação frequentemente fica clara quando os casos inválidos são rejeitados primeiro:

```python
def calculate_average(total: float, count: int) -> float:
    if count <= 0:
        raise ValueError("count must be greater than zero")
    return total / count
```

O primeiro `if` é uma **guard clause**. Ele protege o caminho válido contra uma pré-condição inválida conhecida.

Esse padrão costuma tornar a operação principal mais fácil de ler:

```text
pré-condição inválida? → levantar exceção
caso contrário         → continuar o trabalho normal
```

Guard clause é um padrão de design, não uma sintaxe especial do Python.

## 6. `ValueError` é apropriado para muitos valores inválidos

`ValueError` é útil quando um argumento possui um tipo geral aceitável, mas seu valor específico é inválido para a operação.

Exemplos:

```python
def set_progress(progress: int) -> int:
    if not 0 <= progress <= 100:
        raise ValueError("progress must be between 0 and 100")
    return progress
```

e:

```python
def choose_level(level: str) -> str:
    if level not in {"beginner", "intermediate", "advanced"}:
        raise ValueError("unsupported level")
    return level
```

A pergunta importante não é apenas "Python consegue armazenar esse valor?". A pergunta é "esse valor é válido para o contrato desta função?".

## 7. `TypeError` pode descrever um tipo não suportado

Uma API pública às vezes pode rejeitar deliberadamente um argumento porque seu tipo em runtime não é suportado:

```python
def repeat_label(label: str, times: int) -> str:
    if not isinstance(label, str):
        raise TypeError("label must be a string")
    if not isinstance(times, int):
        raise TypeError("times must be an integer")
    return label * times
```

No entanto, não adicione verificações de tipo em runtime em todo lugar apenas porque existem type hints.

Type hints comunicam tipos esperados a leitores e ferramentas, mas não impõem esses tipos automaticamente em runtime. Adicione verificações explícitas somente quando a API realmente precisar de validação em runtime.

## 8. Escolha a exceção que melhor descreve o contrato que falhou

Algumas escolhas úteis para iniciantes:

| Situação | Exceção comum |
|---|---|
| valor fora de um intervalo aceito | `ValueError` |
| tipo de argumento em runtime não suportado | `TypeError` |
| chave obrigatória ausente em uma API que naturalmente expõe essa busca | `KeyError` |
| posição solicitada fora do intervalo disponível de uma sequência | `IndexError` |
| arquivo solicitado não existe | `FileNotFoundError` |
| operação não está implementada para o caso solicitado | `NotImplementedError` |

Essa tabela é orientação, não uma regra dizendo que toda função deve levantar manualmente cada uma dessas exceções.

Muitas vezes uma operação built-in já levanta naturalmente a exceção mais apropriada. Não duplique verificações apenas para recriar o mesmo sinal, a menos que sua função precise de um contrato ou mensagem mais claro.

## 9. Não use `Exception` quando uma built-in mais específica servir

Isto é válido:

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise Exception("invalid age")
    return age
```

Mas isso dá ao chamador pouca informação sobre qual categoria de falha ocorreu.

Prefira:

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

Tipos de exceção específicos tornam possível o tratamento seletivo.

## 10. Mensagens de exceção devem explicar a expectativa violada

Compare:

```python
raise ValueError("invalid")
```

com:

```python
raise ValueError("score must be between 0 and 100")
```

A segunda mensagem é mais útil para uma pessoa lendo um traceback ou log.

Uma mensagem prática frequentemente informa:

- o que estava inválido;
- qual era a condição aceita;
- contexto suficiente para diagnosticar o problema sem expor segredos ou dados sensíveis.

Evite colocar senhas, tokens de acesso, caminhos privados ou payloads confidenciais em mensagens de exceção.

## 11. Não faça a lógica do programa depender do texto exato da mensagem

Mensagens são principalmente texto de diagnóstico para pessoas.

Evite lógica como:

```python
try:
    validate_score(score)
except ValueError as error:
    if str(error) == "score must be between 0 and 100":
        print("Range problem")
```

Se os chamadores precisarem distinguir categorias de falha de forma programática, use **tipos** de exceção diferentes, valores de retorno estruturados ou outro contrato explícito de API.

## 12. `raise` pode receber uma instância ou uma classe de exceção

Python permite:

```python
raise ValueError("invalid score")
```

e também:

```python
raise ValueError
```

Quando recebe uma classe de exceção, Python cria a instância quando necessário, sem argumentos.

Para ensino e código de aplicação, levantar uma instância com mensagem útil normalmente é mais claro:

```python
raise ValueError("score must be between 0 and 100")
```

## 13. Exceções podem se propagar por várias chamadas de função

Um helper pode levantar uma exceção sem tratá-la:

```python
def validate_quantity(quantity: int) -> int:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return quantity


def build_order(quantity: int) -> str:
    valid_quantity = validate_quantity(quantity)
    return f"Order quantity: {valid_quantity}"
```

Se `validate_quantity()` levantar `ValueError`, `build_order()` também interrompe seu caminho normal, a menos que trate essa exceção.

A exceção continua se propagando para fora pela pilha de chamadas.

## 14. Trate a exceção em uma camada capaz de responder de forma significativa

Um helper de validação de baixo nível pode saber **o que está errado**, mas não **o que o programa deve fazer depois**.

Por exemplo:

```python
def validate_quantity(quantity: int) -> int:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return quantity


try:
    quantity = validate_quantity(0)
except ValueError as error:
    print(f"Could not continue: {error}")
```

O validador informa a violação de contrato. O chamador escolhe a resposta voltada ao usuário.

Uma pergunta de design útil é:

```text
Esta camada sabe como se recuperar ou explicar a falha?
    sim → o tratamento pode ficar aqui
    não → deixe a exceção se propagar
```

## 15. Não levante e capture imediatamente sem um motivo

Isto frequentemente acrescenta cerimônia sem melhorar o design:

```python
def validate_score(score: int) -> int:
    try:
        if not 0 <= score <= 100:
            raise ValueError("invalid score")
    except ValueError:
        return 0
    return score
```

A função transforma uma violação clara de contrato em um valor fallback não relacionado.

Se `0` for realmente o fallback documentado, retorná-lo diretamente pode ser mais claro. Se a entrada inválida deve ser informada, deixe `ValueError` se propagar.

Levante e trate na mesma camada somente quando essa camada realmente possuir uma ação significativa de recuperação.

## 16. Um `raise` sem expressão relança a exceção ativa

Dentro de um bloco `except`, um `raise` sem expressão envia novamente para fora a exceção que está sendo tratada:

```python
def parse_quantity(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        print("Could not parse quantity")
        raise
```

O handler executa algum trabalho local e depois preserva a falha em vez de fingir que a operação teve sucesso.

Conceitualmente:

```text
ocorre ValueError
    ↓
except ValueError executa
    ↓
logging ou limpeza local
    ↓
raise sem expressão
    ↓
a mesma exceção ativa continua para fora
```

## 17. Prefira `raise` sem expressão quando o objetivo for apenas relançar

Dentro de um handler ativo, esta é a forma direta de relançar:

```python
except ValueError:
    raise
```

Escrever `raise error` levanta novamente aquele objeto de exceção como uma operação explícita de `raise` e pode alterar a apresentação do traceback ao acrescentar o local atual do novo `raise`.

Quando sua intenção é "continuar propagando a exceção que estou tratando agora", um `raise` sem expressão comunica essa intenção com mais precisão.

## 18. Traduzir exceções pode melhorar uma fronteira de abstração

Às vezes uma exceção de baixo nível expõe um detalhe de implementação que os chamadores não deveriam precisar conhecer.

Suponha que um texto de configuração precise conter um inteiro:

```python
class ConfigurationError(Exception):
    pass


def parse_attempt_limit(text: str) -> int:
    try:
        return int(text)
    except ValueError as error:
        raise ConfigurationError("attempt limit must be an integer") from error
```

Agora o chamador pode tratar `ConfigurationError` como parte da API de configuração, sem depender diretamente do detalhe interno de conversão.

## 19. `raise ... from ...` cria um encadeamento explícito de exceções

Em:

```python
raise ConfigurationError("attempt limit must be an integer") from error
```

`ConfigurationError` é a nova exceção e `error` é registrado como sua causa explícita.

Se a nova exceção permanecer sem tratamento, a exibição do traceback do Python mostra a relação entre a falha original e a falha traduzida.

Isso preserva o histórico de diagnóstico e permite que a API de nível superior exponha um tipo de exceção mais significativo.

## 20. O encadeamento explícito é especialmente útil ao mudar de nível de abstração

Um formato comum é:

```text
uma operação de baixo nível falha
        ↓
a exceção de baixo nível é capturada
        ↓
uma exceção de nível superior é levantada a partir da original
        ↓
o chamador enxerga o contrato de nível superior
        ↓
o diagnóstico ainda preserva a causa original
```

Exemplos incluem traduzir erros de parsing em erros de configuração ou erros de uma biblioteca de armazenamento em um erro de persistência específico da aplicação.

Não traduza toda exceção automaticamente. Traduza quando isso tornar a fronteira pública mais clara.

## 21. `from None` suprime o contexto exibido e deve ser deliberado

Python também permite:

```python
raise ValueError("invalid identifier") from None
```

Isso suprime a exibição automática do contexto da exceção anterior no traceback resultante.

Pode ser útil quando a falha de baixo nível é irrelevante ou confusa para usuários, mas também remove contexto de diagnóstico do traceback exibido. Use com moderação e deliberadamente.

## 22. Exceções personalizadas são classes de exceção que você define

Uma exceção personalizada permite que uma aplicação atribua a uma falha um tipo específico do domínio.

A menor forma útil é:

```python
class EmptyStudyPlanError(Exception):
    pass
```

Isso cria uma nova classe de exceção chamada `EmptyStudyPlanError`, que herda o comportamento normal de exceções de aplicação de `Exception`.

A instrução `pass` significa que a classe ainda não adiciona comportamento extra.

## 23. Esta é uma introdução restrita à herança de classes

A sintaxe:

```python
class EmptyStudyPlanError(Exception):
    pass
```

significa, conceitualmente:

```text
Exception
    ↓
EmptyStudyPlanError
```

`EmptyStudyPlanError` é um tipo mais específico de `Exception`.

Essa relação importa porque:

```python
except EmptyStudyPlanError:
```

pode capturar somente essa categoria personalizada, enquanto:

```python
except Exception:
```

também pode capturá-la, porque a classe personalizada herda de `Exception`.

Você não precisa de um modelo completo de programação orientada a objetos para usar esse padrão simples com segurança.

## 24. Exceções personalizadas de aplicação normalmente herdam de `Exception`

Para falhas comuns de aplicação, defina exceções personalizadas abaixo de `Exception`, diretamente ou por meio de outra exceção de aplicação apropriada.

Prefira:

```python
class StudyPlanError(Exception):
    pass
```

a derivar diretamente de `BaseException`.

`BaseException` também fica acima de exceções de controle como `KeyboardInterrupt` e `SystemExit`, que handlers comuns de aplicação normalmente não deveriam agrupar acidentalmente com falhas de domínio.

## 25. Nomes de exceções personalizadas convencionalmente terminam com `Error`

Exemplos:

```python
class EmptyStudyPlanError(Exception):
    pass
```

```python
class ConfigurationError(Exception):
    pass
```

O sufixo `Error` é uma forte convenção do Python para nomes de classes de exceção e torna seu propósito imediatamente visível.

## 26. Levante uma exceção personalizada como uma built-in

```python
class EmptyStudyPlanError(Exception):
    pass


def summarize_plan(topics: list[str]) -> str:
    if not topics:
        raise EmptyStudyPlanError("study plan must contain at least one topic")
    return ", ".join(topics)
```

O tipo personalizado carrega significado do domínio. A mensagem carrega o detalhe legível por pessoas.

## 27. Capture o tipo personalizado quando souber como responder

```python
try:
    summary = summarize_plan([])
except EmptyStudyPlanError as error:
    print(f"Plan error: {error}")
```

Esse handler não captura acidentalmente exceções não relacionadas, como um `TypeError` de programação em outro ponto da mesma operação.

Tipos personalizados específicos podem, portanto, tornar uma API mais fácil de tratar corretamente.

## 28. Não crie uma exceção personalizada para toda pequena regra de validação

Isso pode ficar ruidoso:

```text
NegativeScoreError
ScoreTooLargeError
EmptyScoreTextError
UnsupportedScoreFormatError
...
```

Se todas essas situações significarem a mesma coisa para os chamadores, uma built-in `ValueError` pode ser suficiente.

Crie uma exceção personalizada quando a **categoria em si** for significativa para chamadores, logging, testes ou uma fronteira de abstração.

## 29. Uma exceção personalizada pode herdar de uma categoria built-in significativa

Se um erro específico do domínio também for claramente um tipo de erro built-in, a herança pode preservar os dois significados:

```python
class ScoreRangeError(ValueError):
    pass
```

Agora os chamadores podem escolher:

```python
except ScoreRangeError:
```

para o caso específico do domínio, ou:

```python
except ValueError:
```

para uma política mais ampla de erros de valor.

Use isso somente quando a classe built-in pai realmente descrever a falha personalizada.

## 30. Exceções personalizadas podem carregar atributos estruturados

Uma classe personalizada simples frequentemente precisa apenas de `pass`, mas uma exceção também pode armazenar detalhes estruturados:

```python
class ScoreRangeError(ValueError):
    def __init__(self, score: int) -> None:
        self.score = score
        super().__init__(f"score must be between 0 and 100: {score}")
```

Um chamador pode então inspecionar `error.score` sem precisar interpretar o texto da mensagem.

Esse é um padrão de classe um pouco mais avançado. Prefira a forma simples com `pass` até que dados estruturados na exceção tragam um benefício real.

## 31. Exemplo prático: validar scores explicitamente

```python
def validate_score(score: int) -> int:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score


scores = [85, 120]

for score in scores:
    try:
        valid_score = validate_score(score)
    except ValueError as error:
        print(f"Rejected {score}: {error}")
    else:
        print(f"Accepted {valid_score}")
```

Saída:

```text
Accepted 85
Rejected 120: score must be between 0 and 100
```

Cada item é validado de forma independente. O validador levanta a exceção; o loop decide como continuar depois de um item inválido.

Versão executável: [`examples/validate_score.py`](examples/validate_score.py).

## 32. Exemplo prático: uma exceção personalizada de domínio

```python
class EmptyStudyPlanError(Exception):
    pass


def summarize_plan(topics: list[str]) -> str:
    if not topics:
        raise EmptyStudyPlanError("study plan must contain at least one topic")
    return ", ".join(topics)


plans = [["Functions", "Exceptions"], []]

for topics in plans:
    try:
        print(summarize_plan(topics))
    except EmptyStudyPlanError as error:
        print(f"Plan error: {error}")
```

Saída:

```text
Functions, Exceptions
Plan error: study plan must contain at least one topic
```

Versão executável: [`examples/custom_exception.py`](examples/custom_exception.py).

## 33. Exemplo prático: traduzir e encadear uma exceção

```python
class ConfigurationError(Exception):
    pass


def parse_attempt_limit(text: str) -> int:
    try:
        limit = int(text)
    except ValueError as error:
        raise ConfigurationError("attempt limit must be an integer") from error

    if limit <= 0:
        raise ConfigurationError("attempt limit must be greater than zero")

    return limit


try:
    parse_attempt_limit("three")
except ConfigurationError as error:
    cause_name = type(error.__cause__).__name__ if error.__cause__ else "None"
    print(f"{type(error).__name__}: {error}")
    print(f"Cause: {cause_name}")
```

Saída:

```text
ConfigurationError: attempt limit must be an integer
Cause: ValueError
```

A causa explícita continua disponível por `__cause__`, mesmo que o código de nível superior trate `ConfigurationError`.

Versão executável: [`examples/exception_chaining.py`](examples/exception_chaining.py).

## 34. `raise` e `assert` não são intercambiáveis

Uma assertion expressa uma condição que o programador espera que seja verdadeira durante depuração ou verificação de uma invariante interna:

```python
assert total >= 0
```

Assertions podem ser desabilitadas quando Python executa com otimização ativada.

Por isso, não use `assert` para validação que precisa acontecer sempre, como verificar entrada do usuário, conteúdo de arquivos, dados de API ou o contrato de uma função pública.

Use uma exceção explícita:

```python
if total < 0:
    raise ValueError("total cannot be negative")
```

## 35. Levante antes de alterar estado compartilhado quando possível

Suponha que dados inválidos não devam entrar em uma lista:

```python
def add_score(scores: list[int], score: int) -> None:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    scores.append(score)
```

A validação acontece antes da mutação.

Essa ordem reduz a chance de deixar estado parcialmente atualizado depois de uma falha.

Um fluxo útil é:

```text
validar pré-condições
        ↓
levantar exceção se forem inválidas
        ↓
alterar estado somente depois que a validação tiver sucesso
```

## 36. Erro comum: levantar a categoria errada

Isto é enganoso:

```python
def validate_name(name: str) -> str:
    if not name:
        raise TypeError("name is empty")
    return name
```

Uma string vazia ainda possui o tipo esperado `str`; o problema está em seu valor.

`ValueError` comunica a falha com mais precisão:

```python
def validate_name(name: str) -> str:
    if not name:
        raise ValueError("name cannot be empty")
    return name
```

## 37. Erro comum: capturar sua base personalizada de forma ampla demais

Imagine:

```python
class ApplicationError(Exception):
    pass
```

Pode ser tentador envolver grandes trechos com:

```python
except ApplicationError:
    print("Something failed")
```

Mas uma classe base ampla da aplicação ainda pode juntar várias categorias de falha diferentes em uma resposta vaga.

Capture o tipo mais específico que a camada atual realmente sabe tratar de forma significativa.

## 38. Erro comum: converter toda exceção em uma exceção personalizada

Isto não é automaticamente melhor:

```python
try:
    value = int(text)
except ValueError as error:
    raise ApplicationError("operation failed") from error
```

Se os chamadores já entendem `ValueError` e a conversão faz parte do contrato público, a tradução pode não acrescentar nenhuma abstração útil.

Exceções personalizadas devem esclarecer fronteiras, não apenas renomear falhas built-in.

## 39. Erro comum: esconder histórico de diagnóstico sem necessidade

Usar:

```python
raise ConfigurationError("invalid configuration") from None
```

pode produzir um traceback mais limpo para o usuário, mas suprime a exibição do contexto da exceção anterior.

Se a causa de baixo nível ajudar desenvolvedores a diagnosticar a falha, o encadeamento explícito com `from error` costuma ser mais informativo.

## 40. Exercício

Construa um pequeno validador de sessões de estudo que informe deliberadamente entradas inválidas.

Requisitos:

1. Crie uma exceção personalizada chamada `StudySessionError` que herde de `Exception`.
2. Crie `validate_session(minutes: int, topic: str) -> tuple[int, str]`.
3. Levante `ValueError` quando `minutes` for menor ou igual a zero.
4. Levante `StudySessionError` quando `topic` estiver vazio depois de `strip()`.
5. Retorne a tupla validada `(minutes, topic)` quando os dois valores forem válidos.
6. Crie pelo menos três casos de teste contendo uma sessão válida e as duas categorias de falha.
7. Trate `ValueError` e `StudySessionError` separadamente no chamador.
8. Imprima mensagens determinísticas para cada caso.
9. Adicione um helper que receba uma versão textual dos minutos, converta com `int()` e levante `StudySessionError("minutes must be an integer") from error` quando a conversão falhar.
10. Antes de executar o código, desenhe os caminhos normal e excepcional de cada entrada.

Desafio extra: decida se o helper de conversão deve expor `ValueError` diretamente ou traduzi-lo para `StudySessionError` e explique qual fronteira de API sua escolha cria.

## 41. Checklist de revisão

Agora você deve conseguir responder:

- O que `raise` faz com o caminho normal de execução atual?
- Quando `ValueError` é mais adequado que `TypeError`?
- Por que mensagens de exceção não devem virar uma API baseada em comparação de strings?
- O que acontece quando uma exceção levantada não possui handler local?
- Quando um helper de baixo nível deve deixar uma exceção se propagar?
- O que um `raise` sem expressão faz dentro de um bloco `except`?
- Por que `raise` sem expressão normalmente é preferível ao apenas relançar a exceção ativa?
- Qual relação `raise NewError(...) from error` registra?
- Por que o encadeamento de exceções pode melhorar uma fronteira de abstração?
- Por que `from None` deve ser usado deliberadamente?
- O que `class CustomError(Exception): pass` significa em um nível inicial?
- Por que exceções personalizadas de aplicação normalmente herdam de `Exception` em vez de diretamente de `BaseException`?
- Quando uma exceção personalizada é mais útil que uma built-in?
- Por que `assert` não deve validar entrada externa obrigatória?
- Por que validar antes de alterar estado compartilhado costuma ser mais seguro?

## 42. Consulta rápida

| Necessidade | Abordagem útil |
|---|---|
| rejeitar um valor inválido | `raise ValueError("...")` |
| rejeitar um tipo em runtime não suportado | `raise TypeError("...")` quando a verificação em runtime realmente fizer parte da API |
| preservar a exceção atualmente tratada | `raise` sem expressão |
| traduzir uma exceção preservando sua causa | `raise NewError("...") from error` |
| suprimir deliberadamente o contexto anterior exibido | `raise NewError("...") from None` |
| introduzir uma categoria de falha específica do domínio | `class DomainError(Exception): pass` |
| preservar significado de domínio e de erro de valor built-in | herdar de uma built-in apropriada, como `ValueError` |
| distinguir falhas programaticamente | use tipos de exceção ou dados estruturados, não parsing do texto da mensagem |
| validar dados externos/do usuário de forma confiável | verificações explícitas + `raise`, não `assert` |
| reduzir alterações parciais de estado | valide antes da mutação quando for prático |

## 43. Limite de escopo

Este capítulo deliberadamente **não** ensina em profundidade ainda:

- programação orientada a objetos completa e design geral de classes;
- herança múltipla para classes de exceção;
- `ExceptionGroup` e `except*`;
- manipulação avançada de tracebacks;
- políticas de retry;
- frameworks de logging;
- context managers e limpeza de arquivos;
- testes de contratos de exceção com `pytest`.

Esses tópicos ficam mais fáceis depois que o modelo básico de levantar/propagar/tratar estiver estável.

## 44. Para onde a Fase 7 segue

A progressão agora é:

```text
tratar exceções que já acontecem
        ↓
levantar exceções deliberadamente
        ↓
escolher tipos built-in ou personalizados
        ↓
propagar, relançar ou encadear deliberadamente
        ↓
próximo: abrir e gerenciar arquivos com segurança
        ↓
dados textuais estruturados
        ↓
módulos e pacotes
```

Próximo capítulo planejado: **`open()` e `with`**.

## Referências oficiais

- [Python 3.14 Language Reference: The `raise` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-raise-statement)
- [Python 3.14 Tutorial: Raising Exceptions](https://docs.python.org/3.14/tutorial/errors.html#raising-exceptions)
- [Python 3.14 Tutorial: User-defined Exceptions](https://docs.python.org/3.14/tutorial/errors.html#user-defined-exceptions)
- [Python 3.14 Built-in Exceptions](https://docs.python.org/3.14/library/exceptions.html)
- [Python 3.14 Language Reference: The `assert` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-assert-statement)
