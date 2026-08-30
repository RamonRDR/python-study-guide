<div align="center">

# Projeto 01 · Controle de Despesas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Projetos Práticos](../README.pt-BR.md)

Este é o primeiro projeto da **Fase 10: Projetos Práticos**. O objetivo é parar de estudar conceitos isoladamente e combinar modelagem de dados, funções, coleções, exceções, arquivos, JSON, CSV, `pathlib`, `Decimal` e `pytest` em um fluxo pequeno, mas completo.

**Tempo estimado de estudo e implementação:** 180–240 minutos.

## Objetivos de aprendizagem

Ao final deste projeto, você deverá ser capaz de:

- transformar uma descrição curta do problema em requisitos explícitos de software;
- modelar uma despesa como dado estruturado validado;
- usar `Decimal` para valores monetários exatos com duas casas decimais;
- separar responsabilidades de validação, armazenamento, filtro e relatório;
- persistir registros em JSON sem converter dinheiro silenciosamente para ponto flutuante binário;
- exportar os mesmos registros para CSV;
- escrever testes automatizados repetíveis para caminhos de sucesso e falha;
- explicar o projeto como peça de portfólio, e não apenas mostrar código.

## 1. Descrição do projeto

Construa um pequeno controle de despesas capaz de:

1. cadastrar despesas;
2. listar despesas armazenadas;
3. filtrar despesas por categoria;
4. calcular o total completo;
5. calcular o total de uma categoria;
6. resumir totais por categoria;
7. salvar registros em JSON;
8. restaurar registros do JSON;
9. exportar registros para CSV;
10. comprovar os comportamentos importantes com testes automatizados.

O projeto começa deliberadamente como módulo Python, e não como aplicação gráfica. A Fase 10 começa integrando lógica e contratos de dados antes de adicionar outra camada de interface.

## 2. Requisitos funcionais

Cada despesa deve conter:

```text
spent_on    -> date in YYYY-MM-DD format
description -> non-blank text
category    -> non-blank text
amount      -> positive monetary value with two decimal places
```

O tracker deve preservar a ordem de inserção e expor os registros sem entregar ao código chamador acesso direto para alterar sua lista interna.

## 3. Requisitos de validação

Entrada inválida deve falhar explicitamente.

Exemplos:

- texto de data inválido gera `ValueError`;
- descrição vazia gera `ValueError`;
- categoria vazia gera `ValueError`;
- valor zero ou negativo gera `ValueError`;
- `NaN` e infinito são rejeitados;
- JSON com estrutura raiz incorreta é rejeitado;
- registros JSON sem campos obrigatórios são rejeitados.

Uma validação que falha não pode adicionar uma despesa parcial ao tracker.

## 4. Por que dinheiro usa `Decimal`

O projeto armazena valores com `decimal.Decimal`, e não com `float`.

```python
from decimal import Decimal

amount = Decimal("25.90")
```

O parser de valor arredonda para duas casas com `ROUND_HALF_UP` depois de verificar que o número é finito e maior que zero.

Isso não pretende ser um motor contábil universal. É uma regra explícita deste projeto de controle de despesas com duas casas decimais.

## 5. O modelo de dados `Expense`

`Expense` é uma dataclass imutável:

```python
@dataclass(frozen=True, slots=True)
class Expense:
    spent_on: date
    description: str
    category: str
    amount: Decimal
```

Os registros normalmente são criados por `Expense.create(...)`, que aplica toda a normalização antes de o objeto existir.

## 6. O serviço do tracker

`ExpenseTracker` é responsável pela coleção de despesas e pelas operações que utilizam essa coleção.

```python
tracker = ExpenseTracker()
tracker.add("2026-08-29", "Lunch", "Food", "25.40")
tracker.add("2026-08-29", "Bus", "Transport", "12.00")
```

A propriedade pública `expenses` devolve uma tupla, permitindo inspecionar os registros atuais sem receber a lista interna mutável.

## 7. Filtro por categoria

A comparação de categoria ignora diferenças entre maiúsculas e minúsculas:

```python
food_expenses = tracker.filter_by_category("food")
```

`Food`, `food` e `FOOD` são tratados como a mesma categoria para filtros e resumos, enquanto a primeira grafia armazenada permanece como forma de exibição.

## 8. Totais

O total completo é obtido com:

```python
total = tracker.total()
```

O total de uma categoria é:

```python
food_total = tracker.total("Food")
```

Como todo valor armazenado já é um `Decimal`, a soma nunca cruza para aritmética binária de ponto flutuante.

## 9. Totais por categoria

O tracker pode produzir um dicionário como:

```text
Food      -> 53.90
Transport -> 120.00
```

Essa operação combina acumulação em dicionário, normalização sem diferenciar maiúsculas/minúsculas, iteração e aritmética decimal exata.

## 10. Persistência em JSON

`save_json()` grava uma lista de registros.

O valor monetário é serializado como texto:

```json
{
  "spent_on": "2026-08-29",
  "description": "Coffee",
  "category": "Food",
  "amount": "8.50"
}
```

Gravar o valor como string torna a representação decimal explícita, em vez de passá-la por um número de ponto flutuante do JSON.

## 11. Restauração do JSON

`ExpenseTracker.load_json(...)` interpreta o arquivo e reconstrói cada item usando o mesmo caminho validado `Expense.create(...)` usado por dados novos.

Isso significa que dados persistidos não ignoram validação só porque vieram de um arquivo.

## 12. Exportação CSV

`export_csv()` cria este schema:

```text
spent_on,description,category,amount
```

O arquivo é aberto com `newline=""`, seguindo o contrato de fronteira CSV estudado anteriormente no currículo.

## 13. Estrutura do projeto

```text
01-expense-tracker/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── expense_tracker.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_expense_tracker.py
```

O projeto é pequeno o suficiente para ser entendido em uma sessão, mas ainda contém fronteiras parecidas com aplicações reais: modelo, comportamento do serviço, persistência, exportação, demo e testes.

## 14. Execute a demo determinística

A partir da raiz do repositório:

```bash
python practical-projects/01-expense-tracker/demo.py
```

Saída esperada:

```text
expenses: 3
total: 173.90
food: 53.90
transport: 120.00
json round-trip: True
csv rows: 3
```

A demo usa um diretório temporário, portanto não deixa arquivos JSON ou CSV no repositório.

## 15. Execute os testes do projeto

```bash
python -m pytest -q practical-projects/01-expense-tracker/tests
```

A suíte inicial cobre:

- normalização de campos;
- arredondamento half-up de valores;
- rejeição de valores monetários inválidos;
- total completo;
- total por categoria e filtro sem diferenciar maiúsculas/minúsculas;
- round-trip JSON;
- rejeição de estrutura raiz JSON inválida;
- header e linhas exatas do CSV.

## 16. Nota de design: um único caminho de validação

Dados novos e registros restaurados do JSON chegam a `Expense.create(...)`.

Isso evita dois sistemas concorrentes de validação:

```text
new input ----\
              -> Expense.create -> validated Expense
JSON record --/
```

Uma única fronteira de validação é mais fácil de raciocinar e testar.

## 17. Nota de design: registros imutáveis, coleção mutável

Uma `Expense` individual é congelada, mas o tracker pode adicionar novas despesas válidas.

Essa divisão representa duas responsabilidades diferentes:

- um registro de despesa representa um fato que não deve mudar acidentalmente;
- o tracker representa uma coleção que cresce conforme novas despesas são cadastradas.

## 18. Nota de design: persistência explícita

Adicionar uma despesa altera a memória. Salvar JSON altera um arquivo.

O tracker não grava silenciosamente no disco toda vez que `add()` é executado. Manter essas operações explícitas torna os efeitos colaterais mais visíveis, testáveis e fáceis de substituir futuramente.

## 19. Caminhos de falha para inspecionar manualmente

Teste estas chamadas e leia as exceções:

```python
tracker.add("not-a-date", "Lunch", "Food", "10.00")
tracker.add("2026-08-29", "", "Food", "10.00")
tracker.add("2026-08-29", "Lunch", "Food", "0")
tracker.add("2026-08-29", "Lunch", "Food", "NaN")
```

O objetivo não é apenas observar falhas. Confirme que o tracker continua inalterado depois de cada entrada rejeitada.

## 20. Estratégia de testes

Os testes focam contratos observáveis, e não detalhes privados de implementação.

Por exemplo, o teste de CSV verifica o arquivo resultante em vez de afirmar quantas vezes `csv.DictWriter.writerow()` foi chamado.

Assim, refatorações futuras continuam possíveis enquanto o comportamento público for preservado.

## 21. O que esta primeira versão não inclui

A primeira versão não inclui:

- interface gráfica;
- banco de dados;
- autenticação;
- sincronização em nuvem;
- múltiplas moedas;
- despesas recorrentes;
- orçamentos;
- edição ou exclusão de registros;
- gráficos.

Um projeto pequeno com fronteiras claras ensina mais do que um projeto grande com várias funcionalidades pela metade.

## 22. Desafio de extensão: filtro por data

Adicione métodos para:

- uma data exata;
- intervalo inicial/final;
- um mês.

Escreva testes de fronteira antes de adicionar código de apresentação.

## 23. Desafio de extensão: edição e exclusão

Introduza um identificador estável de despesa e implemente atualização/exclusão deliberadas.

Pense no comportamento quando um ID não existe e se arquivos persistidos devem preservar os IDs depois de recarregar.

## 24. Desafio de extensão: orçamentos mensais

Adicione orçamento por categoria e calcule:

```text
budget
spent
remaining
percentage used
```

Mantenha `Decimal` em todo o pipeline monetário.

## 25. Desafio de extensão: relatório com pandas

Carregue o CSV exportado com pandas e produza um resumo por mês/categoria.

O objetivo não é substituir o núcleo do tracker por pandas. É usar pandas na fronteira analítica onde transformação tabular passa a ser útil.

## 26. Desafio de extensão: relatório Excel

Use openpyxl para gerar um workbook com:

- despesas brutas;
- resumo por categoria;
- resumo mensal;
- formatos numéricos;
- uma tabela.

Isso conecta diretamente o Projeto 01 à Fase 9.

## 27. Discussão de portfólio

Ao apresentar o projeto, não diga apenas “é um controle de despesas”. Explique as decisões de engenharia:

- dinheiro exato com `Decimal`;
- registros imutáveis e validados;
- um único caminho de validação para dados novos e persistidos;
- preservação no round-trip JSON;
- interoperabilidade por CSV;
- comportamento de categoria sem diferenciar maiúsculas/minúsculas;
- testes automatizados determinísticos;
- arquivos temporários em demos/testes para evitar poluir o repositório.

Essas decisões demonstram mais habilidade do que a quantidade de linhas do programa.

## 28. Checklist de revisão

Antes de considerar sua própria implementação concluída, verifique:

- Todo registro inválido falha antes de ocorrer mutação?
- Os cálculos monetários são exatos dentro da regra declarada de duas casas?
- Dados JSON podem ser salvos e restaurados sem mudar os registros?
- O CSV pode ser lido por outra ferramenta?
- As regras de categoria são explícitas?
- Os efeitos no filesystem são intencionais?
- Os testes cobrem caminhos de sucesso e falha?
- Outro desenvolvedor consegue entender a estrutura sem perguntar onde está o código importante?

## 29. Próximo projeto

O Projeto 01 estabelece o padrão da Fase 10: **requisitos → design → implementação → testes → explicação → extensões → discussão de portfólio**.

O próximo projeto planejado é a **Calculadora de Notas**, com foco em regras configuráveis, agregação, validação e relatórios sem repetir o design de persistência deste projeto.
