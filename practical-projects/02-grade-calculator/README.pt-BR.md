<div align="center">

# Projeto 02 · Calculadora de Notas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Projetos Práticos](../README.pt-BR.md)

Este é o segundo projeto da **Fase 10: Projetos Práticos**. O foco está em regras configuráveis, agregação ponderada, validação, acompanhamento parcial e testes determinísticos, sem repetir as fronteiras de persistência do Projeto 01.

**Tempo estimado de estudo e implementação:** 150–210 minutos.

## Objetivos de aprendizagem

Ao concluir este projeto, você deverá conseguir:

- transformar regras de notas em contratos de dados explícitos;
- modelar avaliações e faixas de notas imutáveis com dataclasses;
- validar notas e pesos antes de alterar o estado da calculadora;
- calcular médias ponderadas sem depender de ponto flutuante binário;
- diferenciar uma média de progresso de um resultado final da disciplina;
- tornar configuráveis as regras de conceito e aprovação;
- retornar um relatório estruturado antes de formatá-lo para exibição;
- testar valores de fronteira, configurações inválidas e políticas personalizadas.

## 1. Resumo do projeto

Construa uma calculadora de notas que consiga:

1. registrar avaliações corrigidas;
2. atribuir um peso percentual a cada avaliação;
3. rejeitar pesos acumulados acima de 100%;
4. calcular a média ponderada atual com as avaliações já informadas;
5. mostrar o peso concluído e o peso restante;
6. classificar a média com uma política de notas configurável;
7. informar aprovação/reprovação somente quando a disciplina atingir exatamente 100% do peso;
8. aceitar faixas de conceitos e nota mínima de aprovação personalizadas;
9. gerar um relatório textual determinístico;
10. comprovar os comportamentos importantes com testes automatizados.

## 2. Requisitos funcionais

Cada avaliação contém:

```text
name   -> texto não vazio
score  -> percentual de 0.00 a 100.00
weight -> percentual maior que 0.00 e no máximo 100.00
```

A calculadora preserva a ordem de inserção e nunca permite que a soma dos pesos ultrapasse `100.00`.

## 3. Política padrão de notas

A política padrão é:

```text
A -> 90.00 a 100.00
B -> 80.00 a 89.99
C -> 70.00 a 79.99
D -> 60.00 a 69.99
F ->  0.00 a 59.99

nota mínima de aprovação -> 60.00
```

Esses limites são uma convenção do projeto, não um padrão acadêmico universal. Outra instituição pode fornecer uma `GradePolicy` diferente.

## 4. Por que os percentuais usam `Decimal`

Notas e pesos são normalizados para duas casas decimais com `ROUND_HALF_UP`.

```python
Assessment.create("Midterm", "91", "30")
```

O projeto não usa `float` para valores de nota. A conversão também usa um contexto decimal local explícito, impedindo que precisão, arredondamento ou traps definidos pelo código chamador alterem o contrato de validação.

## 5. Agregação ponderada exata

Depois que notas e pesos são validados com duas casas decimais, a calculadora os converte para centésimos inteiros.

```text
91.00 -> 9100
30.00 -> 3000
```

A agregação ponderada usa então inteiros do Python, evitando perda de precisão causada por um contexto aritmético externo de `Decimal`. A razão final é arredondada com half up para duas casas decimais.

## 6. O modelo `Assessment`

`Assessment` é imutável:

```python
@dataclass(frozen=True, slots=True)
class Assessment:
    name: str
    score: Decimal
    weight: Decimal
```

A validação ocorre mesmo quando o construtor da dataclass é usado diretamente.

## 7. Faixas e políticas de notas

Uma faixa contém um rótulo e uma nota mínima:

```python
GradeBand.create("A", "90")
```

Uma política contém faixas ordenadas e a nota mínima de aprovação. As faixas devem:

- usar rótulos únicos;
- usar notas mínimas únicas;
- estar ordenadas da maior para a menor;
- terminar em `0.00` para cobrir toda nota válida.

## 8. Adicionando avaliações

```python
calculator = GradeCalculator()
calculator.add("Homework", "82.50", "20")
calculator.add("Midterm", "91", "30")
```

Se uma nova avaliação fizer o peso total ultrapassar `100.00`, a operação gera `ValueError` e não adiciona a avaliação rejeitada.

## 9. Média de progresso

`average()` calcula a média ponderada normalizada apenas sobre as avaliações informadas até o momento.

Se somente 40% da disciplina foi avaliada, a média atual descreve esses 40%. Ela **não** trata os 60% restantes como nota zero.

## 10. Relatório parcial versus relatório final

`report()` pode ser usado antes da conclusão. Nesse estado:

```text
complete -> False
passed   -> None
```

`final_report()` exige peso total exatamente igual a `100.00`. Somente então aprovação/reprovação é considerada final.

Essa distinção evita apresentar uma disciplina incompleta como resultado concluído.

## 11. Relatório estruturado

A calculadora primeiro retorna uma dataclass `GradeReport` contendo:

```text
assessment_count
total_weight
remaining_weight
average
letter_grade
complete
passed
```

A formatação fica separada em `format_report(...)`. Assim, as regras podem ser testadas sem interpretar texto impresso.

## 12. Política personalizada

O chamador pode substituir as regras A–F:

```python
policy = GradePolicy(
    bands=(
        GradeBand.create("Excellent", "85"),
        GradeBand.create("Satisfactory", "70"),
        GradeBand.create("Needs Improvement", "0"),
    ),
    passing_score=Decimal("70"),
)
```

O código da calculadora não precisa mudar quando a política muda.

## 13. Estrutura do projeto

```text
02-grade-calculator/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── grade_calculator.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_grade_calculator.py
```

## 14. Executar a demonstração determinística

A partir da raiz do repositório:

```bash
python practical-projects/02-grade-calculator/demo.py
```

Saída esperada:

```text
assessments: 4
weight: 100.00
remaining: 0.00
average: 89.65
letter: B
status: complete
passed: yes
```

## 15. Executar os testes

```bash
python -m pytest -q practical-projects/02-grade-calculator/tests
```

A suíte inicial cobre validação, isolamento do contexto decimal, fronteiras das políticas, regras personalizadas, relatórios parciais, agregação ponderada exata, segurança contra mutação, regras de conclusão e formatação determinística.

## 16. Caminhos de falha para inspecionar manualmente

Experimente:

```python
calculator.add("Quiz", "101", "10")
calculator.add("Quiz", "90", "0")
calculator.add("Project", "90", "100.01")
calculator.final_report()
```

Leia cada exceção e confirme que avaliações rejeitadas não alteram a calculadora.

## 17. Nota de design: configuração é dado

Os limites de conceito são representados por valores `GradeBand`, em vez de uma cadeia de `if` fixa dentro de `GradeCalculator`.

Isso torna alterações de política explícitas, testáveis e independentes da lógica de agregação.

## 18. Nota de design: incompleto é um estado real

Uma disciplina parcial não é um erro. É um estado válido com média atual, peso restante e ainda sem resultado final de aprovação/reprovação.

Modelar esse estado diretamente é mais claro do que inventar notas para avaliações ainda não realizadas.

## 19. Nota de design: validar antes de alterar

`add()` cria e valida um `Assessment`, verifica o futuro peso acumulado e só depois adiciona o registro.

Uma operação rejeitada deixa a coleção existente inalterada.

## 20. Estratégia de testes

Os testes focam contratos públicos e fronteiras importantes:

- notas `0.00`, `60.00`, `90.00` e `100.00`;
- excesso de peso acima de `100.00`;
- conclusão exata em `100.00`;
- comportamento de disciplina parcial;
- erros de configuração de política;
- comportamento de política personalizada;
- isolamento do contexto decimal externo.

## 21. O que este projeto não inclui

Esta versão não inclui:

- contas de alunos;
- persistência ou banco de dados;
- regras de presença;
- descarte da menor nota;
- pontos extras;
- múltiplas disciplinas;
- interface gráfica;
- gráficos.

Esses recursos esconderiam a lição central: transformar regras configuráveis em contratos de dados e cálculos pequenos e confiáveis.

## 22. Desafio de extensão: descartar a menor nota

Adicione um grupo de avaliações em que a menor nota possa ser excluída antes da agregação. Defina o comportamento de empates e pesos antes de programar.

## 23. Desafio de extensão: calcular nota necessária

Com base no peso restante, calcule a nota necessária nas avaliações pendentes para alcançar uma média final desejada.

Defina o que deve acontecer quando a meta for matematicamente impossível.

## 24. Desafio de extensão: múltiplos alunos

Crie uma coleção separada que aplique uma mesma `GradePolicy` a calculadoras de vários alunos e gere um resumo da turma.

Mantenha a identidade do aluno separada das regras de cálculo.

## 25. Desafio de extensão: política de arredondamento

Torne o arredondamento configurável. Compare arredondar cada contribuição separadamente com arredondar apenas a média ponderada final e documente as consequências.

## 26. Discussão de portfólio

Ao apresentar este projeto, explique as decisões, não apenas que “ele calcula notas”:

- política de notas configurável;
- registros imutáveis e validados;
- normalização exata de percentuais;
- agregação ponderada baseada em inteiros;
- estado parcial versus final explícito;
- ausência de mutação após entrada rejeitada;
- relatório estruturado separado da apresentação;
- testes automatizados focados em fronteiras.

## 27. Checklist de revisão

Antes de considerar sua implementação concluída, verifique:

- Notas ou pesos inválidos conseguem entrar na coleção?
- O peso acumulado consegue ultrapassar 100%?
- O relatório parcial evita declarar aprovação/reprovação final?
- O relatório final exige exatamente 100% de peso?
- As fronteiras de conceitos funcionam nos valores exatos?
- Uma política diferente pode ser fornecida sem editar a lógica da calculadora?
- Os cálculos são independentes do contexto decimal externo?
- Os testes comprovam caminhos de sucesso e falha?

## 28. Próximo projeto

O Projeto 02 adiciona regras configuráveis e agregação ponderada ao padrão da Fase 10.

O próximo projeto planejado é **Cadastro de Usuários**, com foco em validação de dados semelhantes a identidade, prevenção de duplicidade, busca e fronteiras mais claras de serviço, sem introduzir autenticação real nem dados pessoais.
