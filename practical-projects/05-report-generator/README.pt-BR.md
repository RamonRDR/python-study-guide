<div align="center">

# Projeto 05 · Gerador de Relatórios

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Projetos Práticos](../README.pt-BR.md)

Este é o quinto projeto da **Fase 10: Projetos Práticos**. O foco é transformar registros de domínio já validados em um pipeline confiável de relatórios: janelas explícitas de período, agregação determinística, resumos independentes da apresentação, múltiplos renderizadores e saída segura em arquivos de texto.

**Tempo estimado de estudo e implementação:** 180–240 minutos.

## Objetivos de aprendizagem

Ao final deste projeto, você deverá ser capaz de:

- modelar dados de origem com registros imutáveis e validados;
- definir explicitamente uma janela inclusiva de relatório;
- rejeitar identificadores duplicados antes da agregação;
- separar registros de origem dos registros incluídos no período;
- calcular métricas de status, duração, percentual e agrupamento por equipe de forma determinística;
- representar agregados com objetos de resumo imutáveis e validados;
- separar construção do relatório de sua renderização;
- renderizar o mesmo relatório em texto puro ou Markdown;
- escapar delimitadores de tabela Markdown em valores exibidos;
- gravar arquivos UTF-8 com um contrato explícito entre formato e extensão;
- testar períodos vazios, datas-limite, ordenação, arredondamento, renderização e escrita em arquivo.

## 1. Proposta do projeto

Construa um gerador de relatórios para um conjunto fictício de atividades operacionais.

O gerador deve:

1. validar registros imutáveis de atividade;
2. definir uma janela inclusiva de datas para cada relatório;
3. rejeitar IDs de atividade duplicados no conjunto de origem;
4. incluir somente registros cuja data esteja dentro do período solicitado;
5. ordenar os registros incluídos de forma determinística;
6. calcular métricas de resumo sem depender da apresentação;
7. agrupar equipes ignorando diferenças de maiúsculas/minúsculas, preservando a primeira grafia aceita para exibição;
8. renderizar o mesmo relatório como texto puro estilo TXT ou Markdown;
9. exigir que a extensão do arquivo corresponda ao formato escolhido;
10. gravar arquivos UTF-8 sem criar silenciosamente diretórios inexistentes;
11. provar o contrato do relatório com testes automatizados.

Todos os dados de exemplo são fictícios.

## 2. Pipeline do relatório

O modelo central de aprendizagem é:

```text
registros validados
    -> validação da origem
    -> filtro inclusivo por data
    -> ordenação determinística
    -> resumo validado
    -> relatório imutável
    -> renderizador
    -> gravação opcional em arquivo
```

A ideia importante é que agregação, apresentação e persistência são responsabilidades diferentes.

## 3. Contrato do registro de atividade

Um item válido de origem é representado por `ActivityRecord`:

```python
ActivityRecord(
    activity_id=101,
    team="Accounting",
    status=WorkStatus.COMPLETED,
    duration_minutes=30,
    occurred_on=date(2026, 8, 1),
)
```

O registro exige:

```text
activity_id      -> inteiro positivo, excluindo bool
team             -> texto legível não vazio, com espaços normalizados
status           -> valor do enum WorkStatus
duration_minutes -> inteiro não negativo, excluindo bool
occurred_on      -> valor simples datetime.date
```

A dataclass é congelada e usa slots para que o código de relatório receba um objeto de valor estável.

## 4. Normalização de texto legível

Títulos e nomes de equipe eliminam espaços externos e colapsam espaços repetidos.

Por exemplo:

```python
team="  Shared   Services  "
```

se torna:

```text
Shared Services
```

Valores vazios e valores acima dos pequenos limites definidos pelo projeto são rejeitados.

A intenção não é corrigir texto agressivamente. É manter um contrato de normalização estreito e visível.

## 5. Estados explícitos do fluxo

O projeto usa:

```python
class WorkStatus(str, Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
```

Uma string crua como `"completed"` não é aceita pelo construtor do registro.

Depois que o dado foi validado, o restante do domínio trabalha com valores explícitos do enum.

## 6. Janela do relatório

`ReportWindow` contém:

```text
title
start_date
end_date
```

As duas datas são inclusivas.

Em uma janela de `2026-08-01` até `2026-08-31`, registros nas duas datas-limite são incluídos.

Uma data inicial posterior à data final é rejeitada.

## 7. Datas simples em vez de datetimes

Este projeto exige valores exatos de `datetime.date` no limite do domínio em vez de aceitar silenciosamente subclasses `datetime.datetime`.

O relatório agrupa atividades por data de calendário, então valores com horário ampliariam o contrato sem necessidade.

## 8. Validação da identidade da origem

`activity_id` deve ser único em toda a coleção fornecida para uma operação de relatório.

IDs duplicados são rejeitados antes do filtro de datas.

Isso significa que uma duplicidade fora do período também torna o conjunto de origem inválido.

A validade da identidade é tratada como propriedade da origem, não como efeito colateral do período escolhido.

## 9. Filtro inclusivo por período

`build_report(...)` valida a origem e depois mantém os registros em que:

```python
start_date <= record.occurred_on <= end_date
```

O relatório resultante preserva:

```text
source_record_count
registros incluídos
```

A partir desses valores, ele também expõe quantos registros foram excluídos sem perder a visibilidade do tamanho original da coleção.

## 10. Ordenação determinística

Os registros incluídos são ordenados por:

```text
occurred_on
activity_id
```

Coleções equivalentes produzem a mesma ordem no relatório mesmo quando o chamador fornece os dados em outra sequência.

Isso torna testes, diffs e artefatos gerados mais previsíveis.

## 11. Métricas de resumo

`summarize_activities(...)` calcula:

- total de registros;
- concluídos;
- em andamento;
- bloqueados;
- duração total;
- duração média;
- maior duração;
- percentual de conclusão;
- contagem por equipe.

O resumo é representado por `ReportSummary`, e não por um dicionário sem estrutura.

## 12. Arredondamento exato com duas casas

A duração média e o percentual de conclusão usam valores `Decimal` com duas casas decimais.

O projeto calcula unidades inteiras escaladas e aplica arredondamento half-up de forma explícita.

Por exemplo:

```text
31 minutos / 3 registros -> 10.33
2 concluídos / 3 total   -> 66.67%
3 minutos / 8 registros  -> 0.38
```

O cálculo não depende do contexto decimal global do chamador.

## 13. Por que não usar float nessas métricas

Ponto flutuante binário é excelente para muitos cálculos científicos e gerais, mas métricas apresentadas com casas decimais costumam precisar de uma política de arredondamento visível.

Este projeto torna essa política explícita para que o relatório não dependa de contexto numérico oculto.

## 14. Agrupamento por equipe

A comparação entre nomes de equipe ignora diferenças entre maiúsculas e minúsculas.

Estes registros:

```text
Accounting
accounting
```

pertencem ao mesmo grupo lógico.

A primeira grafia aceita vira o nome de exibição e os grupos finais são ordenados sem considerar caixa.

## 15. Períodos sem registros

Um relatório sem registros incluídos continua sendo válido.

Seu resumo contém:

```text
total de registros: 0
todos os status: 0
duração total: 0
duração média: 0.00
maior duração: 0
conclusão: 0.00%
contagem por equipe: vazia
```

Os dois renderizadores exibem um estado vazio explícito em vez de falhar com divisão por zero ou produzir uma seção ambígua.

## 16. Invariantes do resumo

`ReportSummary` valida seu construtor público.

Entre as verificações:

- as contagens de status devem somar o total;
- campos de duração não podem ser negativos;
- a média deve corresponder à duração total e ao total de registros;
- o percentual de conclusão deve corresponder aos concluídos e ao total;
- a maior duração deve ser matematicamente possível;
- nomes de equipe devem estar normalizados;
- nomes de equipe devem ser únicos ignorando caixa;
- as equipes devem estar ordenadas deterministicamente;
- as contagens por equipe devem somar o total.

O resumo, portanto, é mais do que um saco de números.

## 17. Limite imutável do relatório

`OperationalReport` combina:

```text
ReportWindow
source_record_count
tupla de ActivityRecord incluídos
ReportSummary
```

Ele valida que os registros incluídos estão ordenados, possuem IDs únicos e pertencem à janela solicitada.

A fronteira pública usa tuplas para não expor listas mutáveis internas.

## 18. Construção versus apresentação

`build_report(...)` não decide se o documento final será TXT ou Markdown.

Essa separação permite renderizar o mesmo relatório de mais de uma forma:

```python
report = build_report(...)

text = render_report(report, ReportFormat.TEXT)
markdown = render_report(report, ReportFormat.MARKDOWN)
```

O resultado de negócio não precisa ser recalculado para cada formato visual.

## 19. Renderizador de texto puro

`render_text_report(...)` produz um documento amigável para CLI contendo:

```text
título
período
contagens de origem/incluídos/excluídos
resumo
contagens por equipe
detalhes ordenados dos registros
```

A saída termina com exatamente uma quebra de linha para manter comparações de arquivo estáveis.

## 20. Renderizador Markdown

`render_markdown_report(...)` produz:

- título nível um;
- linha de período;
- tabela de resumo;
- contagens por equipe;
- tabela de registros.

O mesmo conteúdo do relatório é expresso por uma camada de apresentação diferente, sem duplicar a lógica de agregação.

## 21. Escape de delimitadores Markdown

Nomes de equipe podem conter barra vertical (`|`) ou barra invertida.

Como `|` possui significado estrutural dentro de tabelas Markdown, a renderização escapa primeiro barras invertidas e depois os delimitadores de tabela.

É um exemplo pequeno, mas importante, de adaptação de texto válido do domínio para a sintaxe de um formato de saída.

## 22. Seleção explícita de formato

O renderizador genérico aceita somente:

```python
ReportFormat.TEXT
ReportFormat.MARKDOWN
```

Uma string simples como `"text"` é rejeitada.

Após a validação, o programa trabalha com valores explícitos em vez de reinterpretar configuração crua repetidamente.

## 23. Contrato da extensão do arquivo

`write_report(...)` exige que a extensão corresponda ao formato:

```text
ReportFormat.TEXT     -> .txt
ReportFormat.MARKDOWN -> .md
```

A comparação da extensão ignora caixa, então `REPORT.TXT` é válido para texto.

Extensão ausente ou incompatível é rejeitada antes da escrita.

## 24. Saída UTF-8

Os relatórios são gravados com:

```python
encoding="utf-8"
newline="\n"
```

Isso torna o contrato de arquivo visível e mantém o texto gerado consistente entre ambientes suportados.

## 25. Diretórios ausentes não são criados

Este projeto grava um arquivo solicitado, mas deliberadamente **não** cria diretórios-pai ausentes.

Se o diretório não existir, o `FileNotFoundError` normal é propagado.

Descoberta, criação, movimentação e organização de diretórios pertencem ao próximo projeto: **File Organizer**.

## 26. Estrutura do projeto

```text
05-report-generator/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── report_generator.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_report_generator.py
```

## 27. Execute a demonstração determinística

A partir da raiz do repositório:

```bash
python practical-projects/05-report-generator/demo.py
```

Início esperado da saída:

```text
August Operations
=================
period: 2026-08-01 to 2026-08-31
source records: 4
included records: 3
excluded records: 1

SUMMARY
completed: 1
in progress: 1
blocked: 1
completion: 33.33%
```

O quarto registro fictício está fora de agosto, deixando visível a diferença entre origem e registros incluídos.

## 28. Execute os testes do projeto

```bash
python -m pytest -q practical-projects/05-report-generator/tests
```

A suíte inicial contém **70 cenários pytest**, cobrindo validação do modelo imutável, normalização de texto, limites de enums, regras da janela de datas, IDs duplicados, agregação, arredondamento com duas casas, agrupamento sem considerar caixa, relatórios vazios, ordenação determinística, invariantes do resumo, renderização TXT, renderização e escape Markdown, seleção de renderizador, validação de extensão, escrita UTF-8 e falhas de filesystem.

## 29. Caminhos de falha para inspecionar manualmente

Experimente incluir:

```text
activity_id = 0
activity_id duplicado
equipe vazia
status = "completed" em vez de WorkStatus.COMPLETED
duração negativa
datetime em vez de date
start_date posterior a end_date
formato = "text" em vez de ReportFormat.TEXT
Markdown gravado em report.txt
diretório de destino inexistente
```

Observe se o problema pertence ao registro, à janela, à coleção de origem, ao renderizador ou à fronteira do filesystem.

## 30. Nota de design: um resumo, vários renderizadores

Um erro comum em relatórios é misturar cálculos diretamente com o código de apresentação.

Isso faz cada novo formato repetir a lógica de negócio.

Aqui, um único modelo de relatório validado é construído e cada renderizador apenas traduz esse modelo para sua sintaxe.

## 31. Nota de design: validar antes de filtrar

IDs duplicados são verificados antes da aplicação do período.

Isso é intencional.

Se a correção da origem dependesse do filtro de datas, o mesmo conjunto poderia ser válido em um relatório e inválido em outro apenas porque uma duplicidade ficou fora do período.

## 32. Nota de design: relatório é uma fronteira

Um relatório não é apenas uma string.

Ele conecta:

```text
dados de domínio
regras de agregação
regras de ordenação
sintaxe de apresentação
saída no filesystem
```

Manter essas etapas explícitas facilita testes e evolução.

## 33. O que este projeto não inclui de propósito

Esta versão não inclui:

- parsing de CSV;
- planilhas Excel;
- pandas;
- gráficos ou dashboards;
- geração de PDF;
- templates HTML;
- envio por e-mail;
- criação automática de diretórios;
- tratamento de colisões de nomes de arquivo;
- organização recursiva de arquivos;
- persistência em banco de dados;
- formatação de datas/números por locale;
- interface gráfica.

Esses recursos são úteis, mas diluiriam a lição de relatórios ou antecipariam projetos posteriores.

## 34. Desafio de extensão: renderizador JSON

Adicione `ReportFormat.JSON` e produza uma versão estruturada em JSON.

Defina se datas e enums devem virar strings na fronteira de renderização e teste ordenação determinística das chaves quando relevante.

## 35. Desafio de extensão: métricas por equipe

Amplie o resumo de cada equipe para incluir:

```text
quantidade de registros
duração total
duração média
percentual de conclusão
```

Avalie se um modelo imutável dedicado `TeamSummary` fica mais claro do que tuplas aninhadas.

## 36. Desafio de extensão: seção de detalhes opcional

Permita gerar um relatório somente com resumo.

Mantenha os cálculos inalterados e decida se a escolha de exibir detalhes pertence ao modelo do relatório ou apenas à configuração do renderizador.

## 37. Discussão de portfólio

Ao apresentar este projeto, explique mais do que “ele grava um relatório”.

Pontos úteis de engenharia incluem:

- registros de origem imutáveis e validados;
- janelas explícitas e inclusivas;
- validação de identidade no conjunto de dados;
- filtro e ordenação determinísticos;
- arredondamento decimal explícito;
- agrupamento sem considerar caixa com nomes de exibição estáveis;
- invariantes do resumo;
- separação entre construção e renderização;
- vários formatos a partir do mesmo resultado de domínio;
- escape específico do formato;
- contratos explícitos de UTF-8 e extensão de arquivo;
- limites de escopo deliberados antes do File Organizer.

## 38. Checklist de revisão

Antes de considerar sua implementação completa, verifique:

- Os registros de origem são validados antes do relatório?
- Valores Booleanos são impedidos de se passar por inteiros?
- IDs duplicados são rejeitados antes do filtro de datas?
- As duas datas-limite são inclusivas?
- Os registros incluídos são ordenados deterministicamente?
- As contagens de status somam o total?
- O arredondamento da duração média é explícito e estável?
- O percentual de conclusão é determinístico?
- As equipes são agrupadas ignorando caixa e ordenadas de forma estável?
- O relatório usa coleções públicas imutáveis?
- O mesmo relatório pode ser renderizado sem recalcular métricas?
- Delimitadores de tabela Markdown são escapados?
- Cada formato exige a extensão correspondente?
- UTF-8 e quebras de linha são explícitos?
- Diretórios ausentes ficam sob responsabilidade do chamador ou do próximo projeto?
- Todos os exemplos são fictícios e seguros para publicação?

## 39. Próximo projeto

O Projeto 05 transforma registros validados em artefatos de relatório determinísticos mantendo agregação, renderização e persistência separadas.

A seguir, **Projeto 06: File Organizer** desloca o foco do conteúdo de um único arquivo para fluxos controlados de filesystem: descobrir arquivos, classificá-los, planejar movimentos, tratar colisões e manter as operações seguras e testáveis.
