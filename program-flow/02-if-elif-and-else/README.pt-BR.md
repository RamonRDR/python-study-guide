<div align="center">

# `if`, `elif` e `else`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Fluxo do Programa](../README.pt-BR.md) · [← Anterior: Condições, Comparações e Lógica Booleana](../01-conditions-comparisons-and-boolean-logic/README.pt-BR.md)

Condições respondem perguntas. Uma instrução `if` permite que o programa **faça algo por causa da resposta**.

O capítulo anterior construiu expressões como `score >= 70`, `topic in topics` e `has_access and is_active`. Este capítulo usa essas expressões para escolher quais instruções Python executa.

**Tempo estimado de estudo:** 100–125 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que significa execução condicional;
- escrever uma instrução `if` básica;
- usar dois pontos e indentação corretamente;
- diferenciar a sintaxe de indentação do Python da recomendação da PEP 8 de quatro espaços por nível;
- explicar o que acontece quando uma condição de `if` é truthy ou falsy;
- usar `else` para uma decisão com dois caminhos;
- usar uma ou mais cláusulas `elif` para alternativas adicionais;
- explicar por que somente o primeiro ramo truthy de uma cadeia `if`/`elif` é executado;
- ordenar condições sobrepostas de forma deliberada;
- diferenciar instruções `if` independentes de uma única cadeia mutuamente exclusiva;
- combinar `if` com `and`, `or`, `not`, testes de pertencimento, coleções truthy e `is None`;
- usar aninhamento moderado quando uma segunda decisão só fizer sentido dentro de uma primeira;
- evitar deixar variáveis indefinidas porque um ramo não foi executado;
- reconhecer erros comuns de iniciantes envolvendo indentação, `=`, `==` e ordem dos ramos;
- preparar-se para repetição com loops `for` no próximo capítulo.

## 1. O que significa execução condicional

Até aqui, a maioria dos exemplos foi executada de cima para baixo, com todas as instruções sendo alcançadas.

A execução condicional muda esse padrão. Python avalia uma condição e usa seu valor de verdade para decidir se um bloco de instruções deve ser executado.

A ideia central é:

1. avaliar uma condição;
2. se a condição for truthy, executar seu bloco indentado;
3. caso contrário, pular esse bloco;
4. continuar com o código depois da decisão completa.

Esse é o primeiro grande ponto em que seus programas podem seguir caminhos diferentes.

## 2. A sintaxe básica de `if`

Uma instrução `if` básica possui uma condição, dois pontos e um bloco indentado:

```python
if condition:
    statement
```

A palavra `if` inicia a decisão.

A expressão depois de `if` é avaliada quanto ao seu valor de verdade. Os dois pontos `:` encerram o cabeçalho da cláusula. As instruções indentadas pertencem ao bloco controlado por essa cláusula.

Um exemplo real:

```python
temperature = 24

if temperature >= 20:
    print("Comfortable temperature")
```

Saída:

```text
Comfortable temperature
```

Como `temperature >= 20` é `True`, o `print()` indentado é executado.

## 3. A condição não precisa ser literalmente `True` ou `False`

Python usa teste de valor de verdade para a expressão depois de `if`.

Isso significa que ambas as formas podem controlar uma decisão:

```python
score = 82

if score >= 70:
    print("Passed")
```

e:

```python
topics = ["lists", "tuples"]

if topics:
    print("Topics available")
```

A primeira condição é avaliada como o valor Booleano `True`.

A segunda condição usa o valor de verdade de uma lista não vazia. Você aprendeu esse comportamento no capítulo anterior; agora `if` dá a ele uma finalidade prática.

## 4. Os dois pontos fazem parte da sintaxe

Cada cabeçalho de cláusula `if`, `elif` e `else` termina com dois pontos.

Correto:

```python
age = 20

if age >= 18:
    print("Adult")
```

Esquecer os dois pontos é um erro de sintaxe:

```python
age = 20

if age >= 18
    print("Adult")
```

Os dois pontos separam visualmente e sintaticamente o cabeçalho da cláusula do bloco que ela controla.

## 5. A indentação define o bloco

Python usa indentação no início das linhas para agrupar instruções em blocos.

```python
age = 20

if age >= 18:
    print("Adult")
    print("Access rule checked")

print("Done")
```

Saída:

```text
Adult
Access rule checked
Done
```

As duas chamadas de `print()` indentadas pertencem ao bloco do `if`.

O `print("Done")` final não está mais indentado, então fica fora do bloco e é executado depois da decisão.

## 6. Indentação é sintaxe; quatro espaços são uma recomendação de estilo

Estes são dois fatos relacionados, mas diferentes:

- Python usa níveis de indentação para determinar como as instruções são agrupadas;
- a PEP 8 recomenda **quatro espaços por nível de indentação** para código Python normal.

Este guia segue a recomendação da PEP 8:

```python
if age >= 18:
    print("Adult")
```

Não remova a indentação:

```python
if age >= 18:
print("Adult")
```

E não misture tabs e espaços de forma casual. Python pode rejeitar uma indentação inconsistente entre tabs e espaços com `TabError`.

Para quem está começando, a regra prática é simples: configure o editor para inserir quatro espaços por nível de indentação e mantenha consistência.

## 7. Quando a condição é truthy, o bloco é executado

```python
score = 85

if score >= 70:
    print("Passed")

print("Result checked")
```

Saída:

```text
Passed
Result checked
```

A condição é truthy, então Python entra no bloco. Depois que o bloco termina, a execução continua na próxima instrução sem indentação.

## 8. Quando a condição é falsy, o bloco é ignorado

```python
score = 50

if score >= 70:
    print("Passed")

print("Result checked")
```

Saída:

```text
Result checked
```

A instrução `print("Passed")` é ignorada porque `score >= 70` é falsa.

O programa não para. Ele apenas continua depois do bloco do `if`.

## 9. Use `if` quando uma ação for opcional

Um `if` isolado é útil quando algo deve acontecer apenas se uma condição for satisfeita, mas nenhuma ação especial é necessária caso contrário.

```python
has_notification = True

if has_notification:
    print("New notification")

print("Application ready")
```

Saída:

```text
New notification
Application ready
```

Não existe obrigação de adicionar `else` a toda instrução `if`.

## 10. `else` cria uma decisão com dois caminhos

Use `else` quando você precisa de um bloco para o caso truthy e de outro bloco para todos os casos restantes.

```python
is_member = False

if is_member:
    print("Member price")
else:
    print("Standard price")
```

Saída:

```text
Standard price
```

Exatamente um desses dois blocos é executado.

## 11. `else` não possui condição

A cláusula `else` significa: **nenhuma das condições anteriores desta cadeia selecionou um ramo**.

Por isso, sua sintaxe é:

```python
if condition:
    statement_a
else:
    statement_b
```

E não:

```python
if condition:
    statement_a
else other_condition:
    statement_b
```

Se você precisa de outra condição, use `elif`.

## 12. `elif` adiciona outra condição à mesma decisão

`elif` é a forma do Python de criar outro ramo condicional dentro da mesma cadeia.

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Saída:

```text
Result: Passed
```

Python verifica as condições de cima para baixo.

`score >= 90` é falsa, então ele segue para o `elif`. `score >= 70` é verdadeira, portanto esse bloco é executado e o restante da cadeia é ignorado.

## 13. Uma cadeia pode ter zero ou mais cláusulas `elif`

A gramática da linguagem permite:

- uma cláusula `if` obrigatória;
- zero ou mais cláusulas `elif`;
- uma cláusula `else` opcional.

Uma decisão com dois caminhos não precisa de `elif`:

```python
if is_ready:
    print("Start")
else:
    print("Wait")
```

Uma decisão com vários caminhos pode usar vários:

```python
level = 3

if level == 1:
    print("Beginner")
elif level == 2:
    print("Intermediate")
elif level == 3:
    print("Advanced")
else:
    print("Unknown level")
```

Saída:

```text
Advanced
```

## 14. Uma cadeia `if`/`elif` seleciona no máximo um ramo

Esta é uma das regras mais importantes do capítulo.

Python avalia as condições em ordem. Assim que uma delas é truthy, Python executa aquele ramo e ignora o restante da mesma cadeia.

```python
score = 95

if score >= 70:
    print("Passed")
elif score >= 90:
    print("Excellent")
```

Saída:

```text
Passed
```

As duas comparações são matematicamente verdadeiras para `95`, mas a segunda nunca é alcançada porque o primeiro ramo já venceu.

## 15. A ordem das condições pode mudar o resultado

Quando as condições se sobrepõem, ordene-as de forma deliberada.

Um limite mais específico frequentemente precisa aparecer antes de um limite mais amplo:

```python
score = 95

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Passed")
else:
    print("Keep practicing")
```

Saída:

```text
Excellent
```

Isso não é uma regra do Python dizendo que "números maiores devem vir primeiro". É uma consequência de projeto da regra do primeiro ramo truthy.

Pergunte quais condições se sobrepõem e então ordene-as de acordo com o comportamento desejado.

## 16. Condições posteriores da mesma cadeia não são avaliadas após uma correspondência

A referência da linguagem vai além de dizer que os ramos posteriores não são executados: depois que um ramo é selecionado, as condições posteriores daquela instrução `if` também não são avaliadas.

```python
value = 10

if value > 0:
    print("Positive")
elif 10 / 0 > 1:
    print("Never reached")
```

Saída:

```text
Positive
```

A expressão de divisão falharia se Python a avaliasse. Ela nunca é alcançada porque `value > 0` já selecionou o primeiro ramo.

Este exemplo demonstra a ordem de avaliação, não uma recomendação para esconder expressões inseguras em ramos posteriores.

## 17. Instruções `if` independentes são diferentes

Duas instruções `if` separadas representam duas decisões separadas.

```python
minutes = 50

if minutes >= 30:
    print("At least 30 minutes")

if minutes >= 45:
    print("At least 45 minutes")
```

Saída:

```text
At least 30 minutes
At least 45 minutes
```

Os dois blocos podem ser executados porque estas são duas instruções independentes.

## 18. Cadeia versus decisões independentes

Compare a intenção:

| Estrutura | Significado |
|---|---|
| instruções `if` separadas | cada condição é uma pergunta independente; vários blocos podem ser executados |
| uma cadeia `if`/`elif`/`else` | escolhe no máximo um ramo entre um conjunto de alternativas |

Use instruções `if` independentes quando vários fatos puderem exigir ações próprias.

Use uma cadeia `if`/`elif` quando os ramos forem alternativas dentro de uma única decisão.

Escolher a estrutura errada pode produzir código sintaticamente válido, mas logicamente incorreto.

## 19. Combine condições com `and`

A lógica Booleana do Capítulo 01 se encaixa diretamente dentro de `if`.

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
```

Saída:

```text
Entry allowed
```

O bloco é executado somente quando os dois requisitos são truthy.

## 20. Combine alternativas com `or`

```python
is_admin = False
is_editor = True

if is_admin or is_editor:
    print("Edit access")
```

Saída:

```text
Edit access
```

Apenas um dos lados precisa ser truthy para a condição combinada ser truthy.

Lembre que `and` e `or` retornam os próprios operandos, mas uma instrução `if` interpreta o valor resultante quanto ao seu valor de verdade.

## 21. Use `not` quando a condição negativa for mais clara

```python
is_blocked = False

if not is_blocked:
    print("Account available")
```

Saída:

```text
Account available
```

Prefira uma condição que seja lida naturalmente. Muitas camadas de negação podem dificultar a compreensão da decisão.

## 22. Testes de pertencimento criam condições úteis

```python
topics = ["lists", "dictionaries", "sets"]

if "dictionaries" in topics:
    print("Dictionary topic found")
```

Saída:

```text
Dictionary topic found
```

O mesmo padrão funciona com `not in` quando a ausência é a condição que importa.

## 23. Pertencimento em dicionários continua verificando chaves por padrão

As regras da fase de Coleções continuam valendo dentro de uma instrução `if`.

```python
profile = {"name": "Ana", "level": "beginner"}

if "name" in profile:
    print("Name field exists")
```

Saída:

```text
Name field exists
```

Isso verifica se `"name"` é uma chave. Não pesquisa os valores do dicionário.

## 24. Coleções truthy podem simplificar testes de presença

Uma coleção embutida vazia é falsy; uma não vazia é truthy.

```python
tasks = ["review"]

if tasks:
    print("Tasks available")
```

Saída:

```text
Tasks available
```

Para um simples teste de presença, essa forma costuma ser mais clara do que escrever `if len(tasks) > 0:`.

A forma explícita com `len()` não é inválida. A forma truthy é um idioma comum do Python quando o tamanho exato não é necessário.

## 25. `not` funciona naturalmente com coleções vazias

```python
tasks = []

if not tasks:
    print("No tasks")
```

Saída:

```text
No tasks
```

Como uma lista vazia é falsy, `not tasks` se torna verdadeiro.

## 26. Use verificações de identidade para `None`

A PEP 8 recomenda comparar valores singleton como `None` com `is` ou `is not`.

```python
next_topic = None

if next_topic is None:
    print("No next topic selected")
```

Saída:

```text
No next topic selected
```

Isso é mais claro e preciso do que usar `== None`.

## 27. Não escreva `== True` quando a intenção real for testar verdade

Suponha que um nome já represente se algo está ativo:

```python
is_active = True

if is_active:
    print("Active")
```

Saída:

```text
Active
```

Escrever `if is_active == True:` costuma ser desnecessário quando você simplesmente quer que Python teste o valor quanto à verdade.

Existem situações especializadas em que comparar valor ou tipo exato importa, mas esse não é o caso normal de iniciante para uma condição de `if`.

## 28. Instruções `if` aninhadas criam decisões dentro de decisões

Um bloco controlado por um `if` pode conter outra instrução `if`.

```python
has_account = True
email_verified = True

if has_account:
    print("Account found")

    if email_verified:
        print("Email verified")
```

Saída:

```text
Account found
Email verified
```

A segunda decisão só é alcançada depois que a primeira condição é truthy.

## 29. Aninhe quando a segunda pergunta depender de entrar no primeiro bloco

O aninhamento pode comunicar uma dependência:

- primeiro determinar se uma conta existe;
- somente então avaliar algo que faça sentido sobre essa conta.

Mas, se duas condições simplesmente formarem um único requisito conjunto, `and` pode ser mais claro:

```python
has_account = True
email_verified = True

if has_account and email_verified:
    print("Account ready")
```

Saída:

```text
Account ready
```

Nenhum dos estilos é universalmente correto. Escolha a estrutura que representa a relação entre as decisões.

## 30. Evite aninhamento profundo quando uma decisão mais plana for mais clara

Vários níveis de instruções `if` aninhadas podem ficar difíceis de percorrer visualmente.

Neste estágio, prefira:

- expressões Booleanas claras;
- uma cadeia `if`/`elif` sensata;
- aninhamento moderado somente quando ele comunicar uma dependência real.

Fases posteriores adicionarão funções e outras técnicas que podem ajudar a organizar lógicas de decisão maiores.

## 31. Atribuir nomes dentro de ramos exige cuidado

Um ramo pode não ser executado.

Este código é inseguro:

```python
score = 50

if score >= 70:
    result = "Passed"

print(result)
```

Como a condição é falsa, `result` nunca é atribuído. O `print(result)` posterior gera `NameError`.

Uma solução é garantir que todos os caminhos relevantes atribuam o nome:

```python
score = 50

if score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print(result)
```

Saída:

```text
Keep practicing
```

## 32. Uma cadeia exaustiva pode produzir um valor com segurança

Quando o `else` final cobre todos os casos restantes, um nome de resultado pode ser atribuído em todos os ramos.

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Saída:

```text
Result: Passed
```

Esse padrão é útil quando uma decisão escolhe um valor que o código posterior precisa usar.

## 33. Condições longas podem usar parênteses para legibilidade

Parênteses permitem que uma expressão continue por várias linhas físicas sem usar barra invertida.

```python
age = 22
has_ticket = True
is_blocked = False

if (
    age >= 18
    and has_ticket
    and not is_blocked
):
    print("Entry allowed")
```

Saída:

```text
Entry allowed
```

A indentação do corpo continua visualmente distinta das linhas que dão continuidade à condição.

Não adicione parênteses apenas para fazer toda condição parecer maior. Use-os quando realmente melhorarem a leitura.

## 34. Prefira blocos normais com várias linhas neste guia

A gramática do Python permite alguns blocos simples na mesma linha física do cabeçalho, mas a PEP 8 geralmente desencoraja instruções compostas em uma única linha.

Este guia prefere:

```python
if is_ready:
    print("Start")
```

em vez de comprimir o corpo na linha do cabeçalho.

A forma em várias linhas torna a estrutura do bloco mais visível e permite que a decisão cresça sem ficar espremida.

## 35. Quando usar cada forma

Use um `if` isolado quando:

- uma ação for opcional;
- não houver uma ação alternativa especial.

Use `if`/`else` quando:

- exatamente um de dois caminhos deve ser executado.

Use `if`/`elif`/`else` quando:

- você estiver escolhendo entre várias alternativas;
- a ordem dessas alternativas for deliberada.

Use instruções `if` independentes quando:

- mais de uma condição puder precisar disparar sua própria ação.

Use aninhamento moderado quando:

- uma decisão posterior só fizer sentido depois que um ramo anterior tiver sido acessado.

## 36. Quando evitar adicionar mais ramos

Uma instrução `if` não é automaticamente a melhor resposta para toda variação nos dados.

Tenha cuidado quando:

- uma cadeia longa estiver apenas mapeando chaves exatas para valores exatos;
- várias condições repetirem o mesmo trabalho;
- o aninhamento ficar difícil de acompanhar;
- as condições descreverem relações de dados que um dicionário ou conjunto poderia representar de forma mais direta.

Você não precisa refatorar toda decisão pequena. O objetivo é perceber quando a lógica de ramos está descrevendo comportamento e quando ela está apenas recriando uma estrutura de dados.

## 37. Exemplo prático: classificar uma sessão de estudo

O exemplo a seguir combina `not`, `elif`, ordem de limites e um `else` final:

```python
completed = True
minutes = 50

if not completed:
    status = "In progress"
elif minutes >= 60:
    status = "Completed: extended"
elif minutes >= 30:
    status = "Completed: focused"
else:
    status = "Completed: short"

print("Status:", status)
```

Saída:

```text
Status: Completed: focused
```

O primeiro ramo trata sessões não concluídas. Depois que a conclusão é conhecida, os ramos restantes classificam a duração do limite maior mais específico para o limite menor mais amplo.

## 38. Exemplo aprovado: `basic_if.py`

```python
temperature = 24

if temperature >= 20:
    print("Comfortable temperature")

print("Check complete")
```

Saída:

```text
Comfortable temperature
Check complete
```

Este exemplo demonstra a forma básica de `if` e mostra que o código sem indentação continua depois da decisão.

## 39. Exemplo aprovado: `if_elif_else.py`

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Passed"
else:
    result = "Keep practicing"

print("Result:", result)
```

Saída:

```text
Result: Passed
```

Este exemplo demonstra uma cadeia mutuamente exclusiva e uma ordem deliberada de limites.

## 40. Exemplo aprovado: `independent_conditions.py`

```python
minutes = 50
completed = True

if completed:
    print("Session completed")

if minutes >= 30:
    print("At least 30 minutes")

if minutes >= 60:
    session_type = "Extended"
elif minutes >= 30:
    session_type = "Focused"
else:
    session_type = "Short"

print("Session type:", session_type)
```

Saída:

```text
Session completed
At least 30 minutes
Session type: Focused
```

As duas primeiras instruções `if` são independentes, então ambas podem ser executadas. A cadeia final escolhe exatamente um tipo de sessão.

## 41. Erros comuns

### Erro 1: esquecer os dois pontos

Errado:

```python
if score >= 70
    print("Passed")
```

Correto:

```python
if score >= 70:
    print("Passed")
```

### Erro 2: remover a indentação do bloco

Errado:

```python
if score >= 70:
print("Passed")
```

Correto:

```python
if score >= 70:
    print("Passed")
```

### Erro 3: usar `=` em vez de `==`

Errado:

```python
if level = 2:
    print("Intermediate")
```

Correto:

```python
if level == 2:
    print("Intermediate")
```

Atribuição e comparação de igualdade são operações diferentes.

### Erro 4: esperar que todo `elif` truthy seja executado

Uma única cadeia `if`/`elif` para depois do primeiro ramo truthy.

Use instruções `if` separadas quando várias ações independentes puderem ser necessárias.

### Erro 5: colocar primeiro uma condição ampla que se sobrepõe às demais

```python
if score >= 70:
    print("Passed")
elif score >= 90:
    print("Excellent")
```

Uma pontuação de `95` nunca alcança a segunda condição.

### Erro 6: adicionar uma condição depois de `else`

`else` não possui condição. Use `elif` quando outro teste for necessário.

### Erro 7: assumir que um nome foi atribuído em um ramo ignorado

Se o código posterior precisa de um nome, garanta que os caminhos relevantes façam essa atribuição.

### Erro 8: comparar todo nome de aparência Booleana com `True`

Prefira:

```python
if is_ready:
    print("Ready")
```

quando um teste de verdade comum for a intenção.

## 42. Exercício

Crie um arquivo chamado `study_decision.py`.

Comece com:

```python
minutes = 42
completed = True
has_notes = False
```

Seu programa deve:

1. imprimir `"Session completed"` somente quando `completed` for truthy;
2. independentemente, imprimir `"Notes available"` somente quando `has_notes` for truthy;
3. criar um nome `duration` usando uma única cadeia `if`/`elif`/`else`:
   - `"Long"` para 60 minutos ou mais;
   - `"Medium"` para 30 minutos ou mais;
   - `"Short"` nos demais casos;
4. imprimir a duração final;
5. manter os identificadores do código e o texto de saída em inglês.

Saída esperada para os valores iniciais:

```text
Session completed
Duration: Medium
```

Depois, altere os três valores iniciais e preveja a saída antes de executar o programa novamente.

## 43. Autoavaliação

Sem executar este código primeiro, preveja sua saída:

```python
score = 92
has_bonus = True

if score >= 90 and has_bonus:
    print("Top result")
elif score >= 90:
    print("High score")
else:
    print("Standard result")

if has_bonus:
    print("Bonus recorded")
```

Resposta:

```text
Top result
Bonus recorded
```

Por quê?

A primeira cadeia seleciona seu primeiro ramo e ignora os demais ramos daquela cadeia. O `if` final é uma decisão separada, portanto é avaliado independentemente.

## 44. Checklist de revisão

Antes de seguir em frente, verifique se você consegue explicar:

- [ ] o que significa execução condicional;
- [ ] o papel da condição, dos dois pontos e do bloco indentado em uma instrução `if`;
- [ ] por que indentação é sintaxe enquanto quatro espaços são uma recomendação de estilo da PEP 8;
- [ ] o que acontece quando uma condição de `if` é falsy;
- [ ] quando um `if` isolado é suficiente;
- [ ] como `else` cria o caminho restante;
- [ ] como `elif` adiciona outra alternativa testada;
- [ ] por que uma cadeia `if`/`elif` seleciona no máximo um ramo;
- [ ] por que a ordem das condições importa quando os testes se sobrepõem;
- [ ] por que condições posteriores de uma cadeia que já encontrou correspondência não são avaliadas;
- [ ] a diferença entre instruções `if` independentes e uma única cadeia;
- [ ] como `and`, `or`, `not`, pertencimento, truthiness de coleções e `is None` entram nas condições;
- [ ] quando um aninhamento moderado comunica uma dependência real;
- [ ] por que um nome atribuído apenas dentro de um ramo ignorado pode continuar indefinido;
- [ ] por que a formatação de blocos em várias linhas é preferida neste guia.

## 45. Consulta rápida

| Necessidade | Forma típica |
|---|---|
| Ação opcional | `if condition:` |
| Duas alternativas | `if condition:` ... `else:` |
| Várias alternativas | `if` ... `elif` ... `else` |
| Exigir ambas | `if condition_a and condition_b:` |
| Aceitar uma ou outra | `if condition_a or condition_b:` |
| Negar uma condição | `if not condition:` |
| Testar pertencimento | `if item in collection:` |
| Testar ausência | `if item not in collection:` |
| Testar `None` | `if value is None:` |
| Verificar coleção não vazia | `if collection:` |
| Verificar coleção vazia | `if not collection:` |
| Várias decisões independentes | instruções `if` separadas |
| Uma decisão exclusiva | uma cadeia `if`/`elif`/`else` |

Lembre da progressão:

**condição → escolher um ramo → executar seu bloco → continuar depois da decisão**

## Próximo passo

O próximo capítulo é **Loops `for` e Iteração**.

Agora você sabe como uma condição pode escolher se um bloco será executado. Em seguida, Python aprenderá a executar um bloco repetidamente para itens de strings, listas, tuplas, dicionários, conjuntos e outros iteráveis.

## Referências oficiais

- [Referência da linguagem Python 3.13: instruções compostas e a instrução `if`](https://docs.python.org/3.13/reference/compound_stmts.html#if)
- [Tutorial do Python: instruções `if`](https://docs.python.org/3.13/tutorial/controlflow.html#if-statements)
- [Referência da linguagem Python 3.13: indentação](https://docs.python.org/3.13/reference/lexical_analysis.html#indentation)
- [PEP 8: indentação e instruções compostas](https://peps.python.org/pep-0008/#indentation)
