<div align="center">

# Funções Trabalhando Juntas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Funções](../README.pt-BR.md) · [← Anterior: `*args` e `**kwargs`](../07-args-and-kwargs/README.pt-BR.md)

Um programa útil raramente depende de uma única função gigante. Com mais frequência, várias funções pequenas **dividem o trabalho, chamam umas às outras e conectam seus resultados**.

Este capítulo transforma os recursos de funções vistos anteriormente em um modelo de composição. O objetivo não é criar o maior número possível de funções. O objetivo é dar a cada parte significativa do trabalho um papel claro e depois conectar esses papéis de forma deliberada.

**Tempo estimado de estudo:** 90–120 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- chamar uma função definida pelo usuário a partir de outra;
- usar um valor retornado como entrada da função seguinte;
- explicar o que acontece com a função chamadora enquanto outra função comum está executando;
- distinguir uma função auxiliar focada de uma função coordenadora;
- separar cálculo de apresentação quando isso melhora a reutilização;
- manter dependências visíveis por meio de parâmetros e valores de retorno;
- reconhecer quando uma variável global está sendo usada para esconder o fluxo de dados;
- usar variáveis intermediárias para tornar uma cadeia de chamadas mais fácil de rastrear;
- ler um grafo simples de chamadas;
- combinar funções com condições e loops;
- reconhecer lógica duplicada que deveria virar uma função auxiliar reutilizável;
- evitar dividir uma operação simples em funções minúsculas desnecessárias;
- identificar efeitos colaterais escondidos que dificultam o raciocínio sobre a colaboração;
- se preparar para o tratamento mais profundo do fluxo de dados entre chamadas no próximo capítulo.

## 1. Por que funções precisam colaborar

Os capítulos anteriores isolaram habilidades individuais de funções:

```text
define behavior
receive inputs
return outputs
control scope
describe types
provide defaults
collect flexible arguments
```

Programas reais conectam essas habilidades.

Uma tarefa maior, como preparar um resumo de estudo, pode conter naturalmente tarefas menores:

```text
session durations
      ↓
calculate total minutes
      ↓
classify workload
      ↓
build readable summary
```

Cada etapa pode virar uma função quando separá-la torna o programa mais fácil de entender, testar, reutilizar ou alterar.

## 2. Uma função pode chamar outra

Uma chamada de função pode aparecer dentro de outra função assim como outras expressões e instruções.

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


def build_greeting(name: str) -> str:
    clean_name = normalize_name(name)
    return f"Welcome, {clean_name}!"


print(build_greeting("  ava stone  "))
```

Saída:

```text
Welcome, Ava Stone!
```

A relação importante é:

```text
build_greeting()
      ↓ calls
normalize_name()
      ↓ returns
clean_name
```

`build_greeting()` não precisa repetir a lógica de normalização. Ele delega essa parte para `normalize_name()`.

## 3. A função chamadora espera a função chamada terminar

Para uma chamada de função comum neste capítulo, a execução entra na função chamada. Quando essa chamada termina, a execução continua na função chamadora.

Rastreie este exemplo:

```python
def double(number: int) -> int:
    return number * 2


def add_one_after_doubling(number: int) -> int:
    doubled = double(number)
    return doubled + 1


print(add_one_after_doubling(5))
```

A ordem é:

```text
1. call add_one_after_doubling(5)
2. enter add_one_after_doubling()
3. call double(5)
4. enter double()
5. return 10
6. continue inside add_one_after_doubling()
7. return 11
8. print 11
```

A função externa não continua além de `double(number)` até essa chamada produzir seu resultado.

## 4. Valores de retorno são pontos naturais de conexão

Um valor de retorno permite que uma função conclua sua responsabilidade e entregue um resultado para outra parte do programa.

```python
def calculate_area(width: int, height: int) -> int:
    return width * height


def format_area(area: int) -> str:
    return f"Area: {area}"


area = calculate_area(6, 4)
message = format_area(area)
print(message)
```

Saída:

```text
Area: 24
```

As duas funções têm trabalhos diferentes:

```text
calculate_area() → produce a number
format_area()    → turn a number into text
```

Essa separação torna cada resultado mais fácil de reutilizar.

## 5. Use nomes intermediários quando eles melhorarem a história

Python permite chamadas aninhadas:

```python
def calculate_area(width: int, height: int) -> int:
    return width * height


def format_area(area: int) -> str:
    return f"Area: {area}"


print(format_area(calculate_area(6, 4)))
```

Isso é válido. Antes de `format_area()` poder executar, Python avalia `calculate_area(6, 4)` para obter o valor do argumento.

Para iniciantes, esta versão pode ser mais fácil de rastrear:

```python
area = calculate_area(6, 4)
message = format_area(area)
print(message)
```

Prefira a versão que torna o movimento dos dados mais fácil de entender. Menos linhas não significam automaticamente código mais claro.

## 6. Pense em responsabilidades

Imagine uma função que recebe uma pontuação, decide sua categoria, formata uma frase e a imprime.

Isso pode ser aceitável para um script pequeno de uso único. Mas, se a lógica de categoria ou a formatação forem reutilizadas, separar responsabilidades pode ajudar.

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"
```

Agora cada função responde a uma pergunta clara:

```text
classify_score()      → What category does this score belong to?
format_score_report() → How should these already-known values be displayed?
```

## 7. Uma função coordenadora pode conectar auxiliares

Uma função maior pode coordenar funções menores sem duplicar o trabalho delas.

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"


def build_score_report(student: str, score: int) -> str:
    status = classify_score(score)
    return format_score_report(student, score, status)


print(build_score_report("Ava", 84))
```

Saída:

```text
Ava: 84 points - ready
```

Neste guia, podemos chamar `classify_score()` e `format_score_report()` de **funções auxiliares**, enquanto `build_score_report()` atua como **coordenadora** ou **orquestradora**.

Essas palavras descrevem papéis de design. Elas não são sintaxe especial do Python.

## 8. Uma responsabilidade é uma diretriz de design, não uma regra do Python

Python não exige que toda função execute exatamente uma ação minúscula.

Esta função não é inválida:

```python
def build_label(name: str, quantity: int) -> str:
    clean_name = name.strip().title()
    return f"{clean_name} x{quantity}"
```

A pergunta útil não é:

> Esta função tem mais de uma linha?

Pergunte:

> Esta função representa uma responsabilidade compreensível no nível que este programa precisa?

Dividir código deve melhorar clareza, reutilização, testes ou manutenção. Dividir apenas para criar mais nomes de funções pode tornar o programa mais difícil de acompanhar.

## 9. Separe cálculo de apresentação quando a reutilização importar

Imprimir é útil, mas um valor que é apenas impresso não pode ser reutilizado diretamente pela função chamadora.

Menos reutilizável:

```python
def show_total(values: list[int]) -> None:
    total = sum(values)
    print(f"Total: {total}")
```

Mais reutilizável quando quem chama precisa do número:

```python
def calculate_total(values: list[int]) -> int:
    return sum(values)


def format_total(total: int) -> str:
    return f"Total: {total}"
```

Agora uma parte do programa pode imprimir o resultado formatado enquanto outra pode usar o total numérico em outro cálculo.

Essa é uma recomendação de design, não uma regra dizendo que imprimir dentro de funções é sempre errado.

## 10. Torne dependências visíveis com parâmetros

Se uma função precisa de dados de outra parte do programa, parâmetros tornam essa dependência visível.

```python
def calculate_bonus(points: int) -> int:
    return points // 10


def build_result(name: str, points: int) -> str:
    bonus = calculate_bonus(points)
    return f"{name}: {points} points + {bonus} bonus"
```

Quem lê `build_result(name, points)` consegue ver imediatamente quais valores ela exige.

Entradas visíveis tornam funções mais fáceis de entender isoladamente.

## 11. Evite usar variáveis globais como coordenação escondida

Isto funciona, mas a dependência fica escondida:

```python
points = 80


def calculate_bonus() -> int:
    return points // 10
```

Uma interface mais clara é:

```python
def calculate_bonus(points: int) -> int:
    return points // 10
```

A segunda versão declara diretamente do que precisa.

Variáveis globais podem ser apropriadas para algumas constantes de nível do programa e outros designs deliberados. O alerta aqui é especificamente sobre usar estado global compartilhado como substituto invisível para parâmetros e valores de retorno comuns.

## 12. Reutilize auxiliares em vez de copiar lógica

Imagine que vários relatórios precisem da mesma classificação de pontuação.

Duplicar as condições cria vários lugares que podem ficar diferentes com o tempo.

Prefira uma função auxiliar reutilizável:

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"
```

Então funções coordenadoras diferentes podem chamar a mesma auxiliar.

```text
student report ─┐
                ├─→ classify_score()
team summary ───┘
```

A reutilização é mais valiosa quando a função extraída representa um conceito realmente compartilhado, e não apenas uma linha trivial de sintaxe repetida.

## 13. A ordem das chamadas importa quando resultados dependem de trabalho anterior

Se uma função precisa do resultado de outra, o resultado necessário deve existir primeiro.

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


sessions = [30, 45, 60]
total_minutes = calculate_total_minutes(sessions)
workload = classify_workload(total_minutes)
print(total_minutes, workload)
```

Saída:

```text
135 deep
```

A classificação depende do total, então o total é calculado primeiro.

## 14. Construa pipelines simples uma etapa por vez

Um pipeline é um modelo mental útil quando um resultado vira a entrada da etapa seguinte.

```text
raw value
   ↓
normalize
   ↓
classify
   ↓
format
   ↓
final result
```

Por exemplo:

```python
def normalize_code(code: str) -> str:
    return code.strip().upper()


def classify_code(code: str) -> str:
    if code.startswith("A"):
        return "priority"
    return "standard"


def build_code_summary(code: str) -> str:
    clean_code = normalize_code(code)
    category = classify_code(clean_code)
    return f"{clean_code}: {category}"


print(build_code_summary(" a-17 "))
```

Saída:

```text
A-17: priority
```

A função coordenadora torna a sequência visível sem conter os detalhes de cada etapa.

## 15. Condições podem viver dentro de auxiliares focadas

Composição não substitui fluxo do programa. Ela dá à lógica de fluxo um lugar com significado.

```python
def is_passing(score: int) -> bool:
    return score >= 70


def build_result(score: int) -> str:
    if is_passing(score):
        return "Pass"
    return "Review"


print(build_result(78))
```

Saída:

```text
Pass
```

`is_passing()` responde a uma pergunta booleana. `build_result()` decide qual resultado produzir usando essa resposta.

## 16. Loops podem chamar auxiliares para cada item

Um loop pode delegar o trabalho específico de cada item para uma função.

```python
def format_name(name: str) -> str:
    return name.strip().title()


names = [" ava ", "LEO", " mia"]

for name in names:
    print(format_name(name))
```

Saída:

```text
Ava
Leo
Mia
```

Isso costuma manter o loop focado na repetição enquanto a auxiliar fica focada em transformar um item.

## 17. Funções coordenadoras devem descrever a história maior

Uma boa função coordenadora costuma ser lida como um pequeno resumo da tarefa.

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


def build_study_summary(subject: str, sessions: list[int]) -> str:
    total_minutes = calculate_total_minutes(sessions)
    workload = classify_workload(total_minutes)
    return f"{subject}: {total_minutes} minutes ({workload})"
```

Sem ler os detalhes internos das auxiliares, já é possível descrever `build_study_summary()`:

```text
calculate total → classify workload → build summary
```

Isso é um bom sinal de que a colaboração está comunicando bem a intenção.

## 18. Um grafo simples de chamadas mostra quem chama quem

Um **grafo de chamadas** é um diagrama das relações de chamada.

Para o exemplo anterior:

```text
build_study_summary()
├── calculate_total_minutes()
└── classify_workload()
```

Um grafo de chamadas não mostra todas as variáveis nem todos os detalhes de runtime. Ele responde a uma pergunta estrutural mais simples:

> Qual função chama qual outra função?

O próximo capítulo vai aprofundar exatamente como os dados se movem por essas chamadas.

## 19. Aninhamento profundo pode esconder a sequência

Isto é válido:

```python
result = format_total(calculate_total(values))
```

Mas uma cadeia maior pode ficar difícil de inspecionar:

```python
result = finalize(format_total(calculate_total(normalize_values(values))))
```

Nomes intermediários podem expor as etapas:

```python
clean_values = normalize_values(values)
total = calculate_total(clean_values)
message = format_total(total)
result = finalize(message)
```

A segunda forma é mais longa, mas costuma ser mais fácil de depurar, explicar e alterar.

## 20. Erro comum: imprimir quando outra função precisa do valor

Considere:

```python
def calculate_total(values: list[int]) -> None:
    print(sum(values))
```

Isso imprime um número, mas retorna `None`.

Portanto, isto não encaminha o número impresso:

```python
total = calculate_total([10, 20, 30])
print(total)
```

Saída:

```text
60
None
```

Quando outra função precisa do resultado, retorne o valor:

```python
def calculate_total(values: list[int]) -> int:
    return sum(values)
```

Imprimir e retornar resolvem problemas diferentes.

## 21. Erro comum: duplicar a mesma regra em várias funções

Regras repetidas de negócio ou classificação podem se afastar umas das outras.

Em vez de copiar:

```python
def student_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"


def course_status(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

Extraia o conceito compartilhado quando a regra for realmente a mesma:

```python
def classify_readiness(score: int) -> str:
    if score >= 70:
        return "ready"
    return "review"
```

Não extraia apenas porque dois trechos sem relação por acaso parecem iguais hoje. Funções compartilhadas devem representar significado compartilhado.

## 22. Erro comum: criar funções pequenas demais para esclarecer algo

Isto é tecnicamente válido:

```python
def add_one(number: int) -> int:
    return number + 1


def add_two(number: int) -> int:
    return add_one(add_one(number))
```

Mas nem toda expressão precisa de uma função separada.

Uma auxiliar merece existir quando seu nome ou reutilização torna o programa mais fácil de entender ou manter.

Pergunte:

1. O nome desta função explica um conceito significativo?
2. O comportamento é reutilizado?
3. A extração remove detalhes que distraem de uma função maior?
4. A função pode ser entendida e testada isoladamente?

Se a resposta for não para todas as quatro, a divisão pode ser desnecessária.

## 23. Erro comum: esconder efeitos colaterais dentro de auxiliares

Um **efeito colateral** é uma ação observável além de simplesmente retornar um valor, como imprimir ou alterar um objeto que existe fora da função.

Esta auxiliar transforma e também imprime:

```python
def normalize_name(name: str) -> str:
    clean_name = name.strip().title()
    print("Normalized")
    return clean_name
```

Isso pode ser intencional, mas quem reutilizar a auxiliar também receberá essa saída extra.

Para uma transformação reutilizável, uma auxiliar mais silenciosa pode ser mais fácil de combinar:

```python
def normalize_name(name: str) -> str:
    return name.strip().title()
```

Efeitos colaterais não são proibidos. O importante é que sejam deliberados e não surpreendam quem usa a função.

## 24. Exemplos executáveis

### Preparar uma saudação por meio de uma auxiliar

Arquivo: [`examples/prepare_greeting.py`](examples/prepare_greeting.py)

```python
def normalize_name(name: str) -> str:
    return name.strip().title()


def build_greeting(name: str) -> str:
    clean_name = normalize_name(name)
    return f"Welcome, {clean_name}!"


print(build_greeting("  ava stone  "))
```

Saída esperada:

```text
Welcome, Ava Stone!
```

`build_greeting()` delega a normalização e usa o texto retornado.

### Construir um relatório de pontuação com duas auxiliares

Arquivo: [`examples/build_score_report.py`](examples/build_score_report.py)

```python
def classify_score(score: int) -> str:
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "ready"
    return "review"


def format_score_report(student: str, score: int, status: str) -> str:
    return f"{student}: {score} points - {status}"


def build_score_report(student: str, score: int) -> str:
    status = classify_score(score)
    return format_score_report(student, score, status)


print(build_score_report("Ava", 84))
```

Saída esperada:

```text
Ava: 84 points - ready
```

A função coordenadora conecta classificação e formatação sem duplicar nenhuma das responsabilidades.

### Construir um resumo de estudo como um pequeno pipeline

Arquivo: [`examples/build_study_summary.py`](examples/build_study_summary.py)

```python
def calculate_total_minutes(sessions: list[int]) -> int:
    return sum(sessions)


def classify_workload(total_minutes: int) -> str:
    if total_minutes >= 120:
        return "deep"
    if total_minutes >= 60:
        return "steady"
    return "light"


def build_study_summary(subject: str, sessions: list[int]) -> str:
    total_minutes = calculate_total_minutes(sessions)
    workload = classify_workload(total_minutes)
    return f"{subject}: {total_minutes} minutes ({workload})"


print(build_study_summary("Python", [30, 45, 60]))
```

Saída esperada:

```text
Python: 135 minutes (deep)
```

A função maior é lida como um pequeno roteiro: calcular, classificar, resumir.

## 25. Exercício: componha um resumo de leitura

Crie estas funções:

```python
def calculate_total_pages(chapters: list[int]) -> int:
    pass


def classify_reading(total_pages: int) -> str:
    pass


def build_reading_summary(book: str, chapters: list[int]) -> str:
    pass
```

Requisitos:

1. `calculate_total_pages()` retorna a soma das quantidades de páginas dos capítulos;
2. `classify_reading()` retorna `"long"` para 100 páginas ou mais e `"short"` caso contrário;
3. `build_reading_summary()` chama as duas auxiliares;
4. a string final usa a forma `Book: 120 pages (long)`;
5. teste com `"Python Notes"` e `[35, 40, 45]`;
6. mantenha a impressão fora das auxiliares de cálculo.

Saída esperada:

```text
Python Notes: 120 pages (long)
```

Tente rastrear as chamadas no papel antes de executar o programa.

## 26. Checklist de revisão

Antes de continuar, confirme que você consegue:

- [ ] chamar uma função definida pelo usuário a partir de outra;
- [ ] explicar para onde a execução volta depois que uma auxiliar termina;
- [ ] armazenar o valor retornado por uma função e passá-lo para a etapa seguinte;
- [ ] explicar por que variáveis intermediárias podem melhorar a rastreabilidade;
- [ ] distinguir papéis auxiliares e coordenadores sem tratá-los como palavras-chave do Python;
- [ ] separar cálculo de formatação quando a reutilização se beneficia disso;
- [ ] expor dependências por meio de parâmetros em vez de globais escondidas;
- [ ] reutilizar uma auxiliar a partir de mais de uma função chamadora;
- [ ] explicar por que chamadas dependentes precisam ocorrer na ordem necessária;
- [ ] combinar auxiliares com `if` e loops;
- [ ] desenhar um grafo simples de chamadas;
- [ ] reconhecer quando imprimir impede a reutilização de um valor;
- [ ] reconhecer lógica duplicada que representa um conceito compartilhado;
- [ ] evitar fragmentação desnecessária em funções minúsculas;
- [ ] identificar um efeito colateral surpreendente dentro de uma auxiliar.

## 27. Referência rápida

| Necessidade | Padrão útil |
|---|---|
| reutilizar uma parte do comportamento | chamar uma função auxiliar |
| encaminhar um resultado | `result = helper(...)` |
| tornar uma sequência de várias etapas visível | usar variáveis intermediárias |
| coordenar várias auxiliares | usar uma função coordenadora maior |
| reutilizar um cálculo separadamente da saída | retornar o cálculo e formatar ou imprimir depois |
| mostrar dados exigidos claramente | usar parâmetros |
| evitar coordenação escondida | preferir parâmetros e retornos explícitos a estado global temporário |
| mostrar relações de chamada | desenhar um grafo simples de chamadas |
| manter regras repetidas consistentes | extrair uma auxiliar realmente compartilhada |
| evitar fragmentação excessiva | dividir apenas quando a função acrescentar significado, reutilização ou clareza |

## 28. Limite de escopo

Este capítulo não entra profundamente em:

- aliasing e identidade de objetos entre várias chamadas de função;
- propriedade de mutações entre funções chamadoras e auxiliares;
- cópias defensivas nas fronteiras entre funções;
- propagação de exceções por cadeias de chamadas;
- recursão;
- funções passadas como argumentos;
- closures;
- decorators;
- módulos e imports como estratégia de organização;
- funções assíncronas e concorrência;
- inspeção avançada da pilha de chamadas.

Esses assuntos exigem tratamento separado. O próximo capítulo se concentra especificamente em rastrear **o fluxo de dados entre funções**, incluindo de onde os valores vêm, para onde vão e qual função é responsável por alterá-los.

## 29. O que vem depois

Agora você consegue dividir uma tarefa maior em funções que cooperam e ler as relações básicas de chamada entre elas.

A próxima pergunta é mais precisa:

> Quando várias funções trocam valores, como podemos rastrear exatamente de onde os dados vieram, o que os alterou e quem é responsável por cada mudança?

Isso leva ao **Capítulo 09: Fluxo de Dados Entre Funções**.

Volte para a [trilha de Funções](../README.pt-BR.md) ou para a [trilha completa](../../docs/learning-path.pt-BR.md).

## Referências

Documentação primária do Python:

- [Python 3.13 Tutorial: Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions)
- [Python 3.13 Tutorial: More on Defining Functions](https://docs.python.org/3.13/tutorial/controlflow.html#more-on-defining-functions)
- [Python 3.13 Language Reference: The `return` statement](https://docs.python.org/3.13/reference/simple_stmts.html#the-return-statement)
