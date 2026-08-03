<div align="center">

# Comentários em Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Comentários ajudam quem lê a compreender decisões, restrições e contextos que não são evidentes apenas pelo código. Eles são valiosos quando preservam um raciocínio. Tornam-se ruído quando apenas repetem o que o código já diz.

> **Princípio orientador:** O código deve explicar o que acontece. Os comentários devem explicar por que acontece quando o motivo não é evidente.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Uma familiaridade básica com variáveis e condicionais ajuda, mas não é obrigatória |
| Tempo estimado de estudo | 35 a 50 minutos |
| Conceitos principais | `#`, comentários de bloco, comentários na mesma linha, contexto útil, comentários desatualizados, `TODO`, `FIXME`, `NOTE` |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- reconhecer a sintaxe de comentários em Python;
- diferenciar comentários, strings e docstrings;
- explicar quando um comentário acrescenta informação útil;
- identificar comentários que apenas narram um código evidente;
- escrever comentários sobre decisões, restrições, limites e regras de negócio fictícias;
- utilizar `TODO`, `FIXME` e `NOTE` como convenções claras de projeto;
- escolher entre um comentário, um nome melhor, uma docstring, uma documentação ou logging;
- revisar comentários considerando exatidão, clareza, privacidade e relevância ao longo do tempo.

## 1. O que é um comentário

Um comentário em Python começa com o caractere cerquilha (`#`) que não esteja dentro de uma string e continua até o fim da linha física.

```python
# This entire line is a comment.
message = "Hello"  # This is an inline comment.
```

Comentários normalmente são ignorados pela sintaxe do Python e não alteram o resultado do programa. Comentários com formatos especiais ainda podem ser lidos pelo decodificador do código-fonte ou por ferramentas externas, como explicado adiante.

```python
score = 80
# score = 100
print(score)
```

Saída:

```text
80
```

A atribuição comentada não é executada.

### Uma cerquilha dentro de uma string não é um comentário

```python
label = "Ticket #42"
print(label)
```

O caractere `#` faz parte da string porque aparece entre aspas.

### Comentários com finalidade especial

Alguns comentários seguem convenções que fornecem informações ao decodificador do código-fonte do Python, ao sistema operacional ou a ferramentas de desenvolvimento. Alguns exemplos:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
value = load_value()  # type: ignore[assignment]
```

- Um *shebang* na primeira linha pode ajudar sistemas operacionais semelhantes ao Unix a escolher um interpretador quando o arquivo é executado diretamente.
- Uma declaração de codificação válida na primeira ou segunda linha informa ao Python como decodificar o arquivo-fonte. O Python 3 utiliza UTF-8 por padrão quando nenhuma declaração é informada.
- Diretivas como `# type: ignore`, `# noqa` ou marcadores de formatação podem ser consumidas por verificadores de tipos, linters ou formatadores. O comportamento exato pertence à ferramenta correspondente, não à execução comum de comentários.

Utilize diretivas de ferramentas apenas quando forem necessárias, específicas e compreensíveis. Explique ou indique a razão quando uma supressão puder esconder um problema real.

## 2. Por que comentários existem

O código consegue expressar operações com precisão, mas nem sempre consegue preservar o motivo por trás de uma decisão.

Considere esta condição:

```python
if days_before_event >= 14:
    apply_discount()
```

O código mostra a regra, mas não responde perguntas como:

- Por que o limite é de 14 dias?
- O décimo quarto dia está incluído de propósito?
- Isso é uma limitação técnica ou uma regra fictícia?
- O operador poderia ser alterado de `>=` para `>` com segurança?

Um comentário útil pode preservar esse contexto ausente:

```python
# The fictional policy includes the fourteenth day in the discount window.
if days_before_event >= 14:
    apply_discount()
```

O comentário protege o motivo por trás da comparação. Ele ajuda a evitar uma alteração futura que pareça inofensiva, mas mude a regra pretendida.

## 3. Sintaxe e formas

### Comentários de uma linha

Um comentário pode ocupar uma linha inteira:

```python
# Convert the temperature only after validating the selected scale.
temperature_celsius = convert_temperature(user_value)
```

A PEP 8 recomenda um espaço após `#` em comentários comuns escritos como texto.

```python
# Clear and conventional.
```

Evite:

```python
#Harder to read.
```

### Comentários na mesma linha

Um comentário na mesma linha aparece ao lado de uma instrução:

```python
remaining_attempts -= 1  # The first attempt was already recorded.
```

A PEP 8 recomenda utilizar esse formato com moderação, separar o comentário da instrução com pelo menos dois espaços e escrever `# ` antes do texto.

Comentários na mesma linha são mais úteis quando uma justificativa curta pertence diretamente a uma instrução. Quando a explicação for longa, utilize um comentário de bloco acima do código correspondente.

### Comentários de bloco

Um comentário de bloco é formado por linhas consecutivas de comentários e normalmente explica o código que vem em seguida.

```python
# The data source returns an empty value for days with no measurements.
# Treat that value as missing data instead of converting it to zero, because
# zero is a valid measurement in this fictional example.
measurement = read_measurement()
```

Mantenha o comentário no mesmo nível de indentação do código que ele descreve:

```python
if measurement is None:
    # Missing measurements are reported separately from valid zero values.
    record_missing_measurement()
```

### Python não possui uma sintaxe específica para comentários de várias linhas

Python não possui um delimitador separado como `/* ... */` para comentários de várias linhas. Utilize várias linhas iniciadas com `#`:

```python
# This is a block comment.
# Each physical line begins with a hash.
```

Strings com aspas triplas são literais de string, não comentários de várias linhas:

```python
"""This is a string literal, not comment syntax."""
```

Quando um literal de string é a primeira instrução de um módulo, função, classe ou método, ele se torna uma docstring e fica disponível por meio de `__doc__`. Docstrings serão abordadas separadamente nesta seção do guia.

## 4. Quando utilizar comentários

### Explique um motivo que não seja evidente

```python
# Retry once because the fictional simulator may need one cycle to become ready.
max_retries = 1
```

A atribuição é simples. O motivo do limite não é.

### Preserve uma regra de negócio fictícia

```python
# The fictional policy includes the registration date in the seven-day window.
if elapsed_days <= 7:
    allow_change = True
```

O comentário explica a interpretação pretendida do limite. Ele não afirma que a regra pertence a uma organização real.

### Documente uma restrição técnica

```python
# Keep the file name in ASCII because the external teaching tool used in this
# example rejects non-ASCII paths.
output_name = "summary.txt"
```

O comentário registra uma restrição que pode não ser percebida apenas pela atribuição.

### Explique uma solução temporária ou contorno

```python
# Iterate over a copy because approved items are removed from the original.
for item in pending_items.copy():
    if is_approved(item):
        pending_items.remove(item)
```

Um comentário sobre contorno deve explicar o risco que está sendo evitado. Sempre que possível, inclua um link para uma issue pública ou página de documentação que permita verificar no futuro se a solução ainda é necessária.

### Esclareça unidades ou interpretações quando o nome não for suficiente

```python
poll_interval = 30  # Seconds required by the fictional simulator.
```

Um nome melhor pode eliminar a necessidade do comentário:

```python
poll_interval_seconds = 30
```

Prefira o nome mais claro, a menos que o motivo do valor ainda precise ser explicado.

## 5. Quando evitar comentários

### Não narre um código evidente

```python
# Add one to the counter.
counter += 1
```

O comentário repete a operação sem acrescentar contexto.

Uma versão útil explicaria um motivo que o código não revela:

```python
# Count the restored session as an attempt so retry limits remain consistent.
counter += 1
```

### Não utilize comentários para consertar nomes pouco claros

Evite:

```python
x = 14  # Number of days required for the early-registration discount.
```

Prefira:

```python
early_registration_days = 14
```

Utilize um comentário apenas quando o nome ainda não conseguir explicar o motivo ou o limite:

```python
early_registration_days = 14

# The fictional policy includes the fourteenth day in the discount window.
if days_before_event >= early_registration_days:
    apply_discount()
```

### Não mantenha código desativado sem uma razão

Evite deixar grandes blocos de código comentado:

```python
# old_total = subtotal * 1.15
# print(old_total)
```

O controle de versão já preserva implementações anteriores. Exclua código obsoleto, exceto quando houver um motivo específico, temporário e documentado para mantê-lo.

### Não escreva comentários que possam se tornar falsos silenciosamente

```python
# Retry three times.
max_retries = 5
```

A contradição é mais perigosa do que a ausência de comentário. Atualize ou remova comentários sempre que o código relacionado mudar.

### Nunca coloque segredos ou informações privadas em comentários

Comentários são armazenados nos arquivos-fonte e podem ser versionados, copiados, indexados ou publicados.

Nunca inclua:

- senhas, tokens, chaves de API ou URLs privadas;
- dados pessoais ou de clientes;
- regras ou fluxos confidenciais;
- detalhes de empregadores, clientes, projetos pessoais ou familiares privados;
- código proprietário copiado ou explicações internas.

Crie exemplos fictícios e originais desde o início.

## 6. Comentários e código autoexplicativo

Comentários não são a primeira solução para todo problema de legibilidade.

Compare:

```python
# Check whether the user can access the event.
if a and not b and c:
    grant_access()
```

Com nomes mais claros:

```python
has_ticket = True
is_blocked = False
event_is_open = True

if has_ticket and not is_blocked and event_is_open:
    grant_access()
```

A segunda versão reduz a necessidade de explicação porque os nomes revelam as condições.

Uma ordem útil de decisões é:

1. O código pode ser simplificado?
2. Um nome pode expressar o significado?
3. Uma pequena função pode expressar a intenção?
4. Ainda existe um raciocínio importante que não está visível?
5. Adicione um comentário para esse raciocínio restante.

Um comentário deve complementar um código claro, não servir como desculpa para um código confuso.

## 7. Comentários, docstrings, documentação e logging

Essas ferramentas resolvem problemas diferentes.

| Recurso | Objetivo principal | Público mais comum | Disponível durante a execução? |
|---|---|---|---|
| Comentário | Explicar decisões ou contextos não evidentes no código-fonte | Pessoas que mantêm ou estudam o código-fonte | Não por meio da documentação normal dos objetos |
| Docstring | Descrever a finalidade e o uso público de um módulo, função, classe ou método | Pessoas que utilizam o código e responsáveis pela manutenção | Sim, por meio de `__doc__` e ferramentas como `help()` |
| README ou guia | Explicar instalação, conceitos, fluxos e formas amplas de uso | Estudantes, colaboradores e usuários | Não faz parte do comportamento do programa |
| Logging | Registrar eventos, avisos, falhas e contexto de diagnóstico durante a execução | Operação, desenvolvimento e suporte | Sim |
| Type hint | Expressar tipos esperados e auxiliar leitores e ferramentas de análise | Desenvolvedores, estudantes, editores e verificadores de tipos | Em muitos casos fica armazenado nas anotações, mas não é aplicado automaticamente pelo Python |

### Comentário versus docstring

Utilize um comentário para explicar uma decisão de implementação:

```python
# Preserve input order because the teaching report compares rows visually.
ordered_names = list(names)
```

Utilize uma docstring para explicar o que uma função reutilizável oferece:

```python
def calculate_average(values):
    """Return the arithmetic mean of the provided values."""
```

### Comentário versus logging

Um comentário não consegue registrar o que aconteceu em uma execução específica:

```python
# The file failed to open.
```

Essa frase não observa o comportamento em tempo de execução. O logging pode registrar o evento quando ele ocorrer:

```python
logger.error("Could not open the configuration file")
```

Não substitua diagnósticos de execução por comentários.

## 8. Exemplo básico

Comentário desnecessário:

```python
# Multiply the price by the quantity.
total = price * quantity
```

Melhor sem o comentário:

```python
total = price * quantity
```

Comentário útil:

```python
# The fictional exercise stores prices in cents to keep all calculations in
# integers and avoid introducing decimal arithmetic in this beginner chapter.
total_cents = price_cents * quantity
```

O último comentário explica uma decisão didática e de projeto, não a multiplicação em si.

## 9. Exemplo prático

```python
from datetime import date

EARLY_REGISTRATION_DAYS = 14
EARLY_DISCOUNT_PERCENT = 10


def calculate_registration_fee(
    base_fee_cents,
    event_date,
    registration_date,
):
    days_before_event = (event_date - registration_date).days

    # The fictional policy includes the fourteenth day in the discount window,
    # so this comparison must remain inclusive.
    if days_before_event >= EARLY_REGISTRATION_DAYS:
        discount_cents = base_fee_cents * EARLY_DISCOUNT_PERCENT // 100
        return base_fee_cents - discount_cents

    return base_fee_cents
```

O comentário é útil porque:

- o código já mostra que `>=` está sendo utilizado;
- o comentário explica por que o caso de igualdade importa;
- a palavra *fictícia* impede que o exemplo seja confundido com uma política real;
- uma pessoa que mantenha o código no futuro saberá que trocar `>=` por `>` mudaria a regra pretendida.

Consulte o exemplo executável completo em [`examples/business_rule_comments.py`](examples/business_rule_comments.py).

## 10. `TODO`, `FIXME` e `NOTE`

Python não atribui um comportamento nativo a esses rótulos. Eles são convenções humanas e de ferramentas utilizadas por muitos projetos.

### `TODO`

Utilize `TODO` para uma melhoria específica que ainda precisa ser concluída.

Fraco:

```python
# TODO: Improve this.
```

Melhor:

```python
# TODO: Replace the linear search after the catalog exceeds 10,000 items.
```

Um bom `TODO` explica o que precisa mudar e, quando útil, a condição que torna a alteração necessária. Projetos também podem incluir o número de uma issue ou o responsável, de acordo com sua própria política.

### `FIXME`

Utilize `FIXME` para um comportamento conhecido que esteja incorreto, inseguro ou incompleto e precise de correção.

```python
# FIXME: Preserve leading zeros when postal codes are loaded from CSV.
```

Um `FIXME` não substitui o registro de um defeito sério. Siga o processo de issues e segurança do projeto quando o impacto exigir.

### `NOTE`

Utilize `NOTE` para um contexto importante que possa passar despercebido por quem mantém o código.

```python
# NOTE: The sample data is intentionally unsorted for the ordering exercise.
```

Não transforme toda observação em `NOTE`. Reserve o marcador para informações que realmente afetem a compreensão ou a manutenção.

## 11. Erros comuns

### Explicar o que acontece em vez de explicar por quê

```python
# Check whether the value is greater than zero.
if value > 0:
    process(value)
```

A condição já explica a operação.

### Escrever um texto enorme ao lado de um código simples

Um comentário longo pode esconder um problema de projeto. Quando a explicação ficar grande, considere extrair uma função, simplificar o código ou mover a documentação mais ampla para um guia.

### Referenciar o código por uma posição frágil

Evite:

```python
# The loop below changes the list used on line 42.
```

Números de linha e posições mudam. Faça referência a nomes e conceitos estáveis.

### Utilizar um comentário como lista de tarefas sem contexto

```python
# TODO: Later.
```

Isso não informa o que falta, por que importa ou como reconhecer que a tarefa foi concluída.

### Comentar todas as linhas

Comentários em excesso obrigam quem lê a processar duas versões da mesma lógica. Comente apenas quando a segunda voz contribuir com algo que a primeira não consegue dizer claramente.

### Confiar mais no comentário do que no código

O programa executa o código, não a explicação. Quando ambos discordarem, investigue o comportamento pretendido, os testes e os requisitos antes de alterar qualquer um deles.

## 12. Exemplos neste repositório

| Arquivo | Objetivo |
|---|---|
| [`useful_comments.py`](examples/useful_comments.py) | Mostra um comentário que explica uma decisão de agendamento não evidente |
| [`unnecessary_comments.py`](examples/unnecessary_comments.py) | Compara a narração linha por linha com um código mais claro |
| [`business_rule_comments.py`](examples/business_rule_comments.py) | Preserva o limite de uma regra fictícia e original |

Execute um exemplo a partir da raiz do repositório:

```bash
python comments-and-documentation/01-comments/examples/useful_comments.py
```

Em sistemas onde o comando se chama `python3`:

```bash
python3 comments-and-documentation/01-comments/examples/useful_comments.py
```

## 13. Exercício

Revise este código:

```python
# Set the maximum number of attempts.
max_attempts = 3

# Set attempts to zero.
attempts = 0

# Loop while attempts is less than max attempts.
while attempts < max_attempts:
    # Print the attempt number.
    print(attempts + 1)

    # Add one to attempts.
    attempts += 1
```

Realize as seguintes tarefas:

1. Remova comentários que apenas repetem o código.
2. Renomeie variáveis somente quando um nome mais claro for realmente necessário.
3. Adicione um motivo fictício e útil para o limite de três tentativas.
4. Confirme que o código revisado produz a mesma saída.
5. Explique com suas palavras por que o comentário restante acrescenta informação.

Uma possível revisão:

```python
max_attempts = 3
attempts = 0

# The fictional practice terminal allows three tries before showing a hint.
while attempts < max_attempts:
    print(attempts + 1)
    attempts += 1
```

Essa não é a única resposta válida. A pergunta mais importante é se o comentário preserva um contexto que o código não consegue expressar sozinho.

## 14. Checklist de revisão de comentários

Antes de manter ou adicionar um comentário, pergunte:

- A informação é verdadeira?
- O código já diz a mesma coisa com clareza?
- Um nome melhor ou uma função menor poderia eliminar a necessidade do comentário?
- O comentário explica um motivo, restrição, limite, risco ou decisão?
- Uma alteração futura pode tornar esse comentário fácil de esquecer ou contradizer?
- A linguagem está clara para o público pretendido?
- Existe alguma informação privada, proprietária, pessoal ou identificável?
- Quando necessário, a explicação pode ser verificada em uma fonte ou issue pública?

## 15. Resumo para consulta rápida

| Situação | Abordagem preferida |
|---|---|
| O código está confuso porque os nomes são vagos | Melhore os nomes primeiro |
| Uma decisão não é evidente pelo código | Adicione um comentário curto explicando o motivo |
| Uma regra fictícia possui um limite importante | Comente a interpretação pretendida |
| Um contorno depende de uma limitação externa | Explique a limitação e, quando possível, inclua uma fonte pública |
| Um comentário repete a instrução | Remova o comentário |
| Um código antigo está comentado | Exclua-o e utilize o controle de versão |
| Uma função pública precisa de documentação de uso | Escreva uma docstring |
| Um comportamento de execução precisa ser registrado | Utilize logging |
| Um trabalho futuro é específico e executável | Utilize um `TODO` claro de acordo com a política do projeto |
| Um comportamento conhecido está incorreto | Utilize `FIXME` e siga o processo de defeitos do projeto |
| Um contexto pode passar despercebido | Utilize `NOTE` com moderação |

## Referências oficiais

- [Análise léxica do Python: comentários](https://docs.python.org/pt-br/3/reference/lexical_analysis.html#comments)
- [PEP 8: comentários](https://peps.python.org/pep-0008/#comments)
- [PEP 257: convenções de docstrings](https://peps.python.org/pep-0257/)

## Princípio final

Um comentário útil deixa o código mais fácil de compreender depois que a pessoa processa os dois. Se apagar o comentário não mudar nada na compreensão, provavelmente ele não era necessário.
