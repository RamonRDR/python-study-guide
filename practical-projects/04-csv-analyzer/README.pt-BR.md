<div align="center">

# Projeto 04 · Analisador CSV

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Projetos Práticos](../README.pt-BR.md)

Este é o quarto projeto da **Fase 10: Projetos Práticos**. O foco está em fronteiras de CSV, schemas explícitos, conversão tipada de linhas, validação por linha, falhas estruturais, agregação determinística e análise testável sem depender de pandas.

**Tempo estimado de estudo e implementação:** 180–240 minutos.

## Objetivos de aprendizagem

Ao concluir este projeto, você deverá ser capaz de:

- definir um schema CSV exato em vez de assumir que qualquer tabela é aceitável;
- diferenciar estrutura CSV malformada de dados inválidos em uma linha;
- converter campos de texto em valores `int`, `bool`, `date` e `Enum`;
- preservar linhas válidas mesmo quando outras falham na validação;
- relatar vários problemas de campo em uma única linha rejeitada;
- detectar identificadores duplicados entre as linhas aceitas;
- manter resultados públicos do parser imutáveis;
- agregar registros de forma determinística sem arredondamento oculto de `float`;
- filtrar registros validados sem modificá-los;
- testar cabeçalhos, entrada malformada, regras de conversão, rejeições e resumos.

## 1. Resumo do projeto

Construa um analisador CSV para um conjunto fictício de incidentes.

O analisador deve:

1. exigir um schema exato de cabeçalhos;
2. ler arquivos CSV UTF-8 com BOM UTF-8 opcional;
3. converter linhas de incidentes em registros tipados e imutáveis;
4. coletar problemas de validação por linha sem descartar todos os dados corretos;
5. rejeitar valores `event_id` duplicados entre registros aceitos;
6. diferenciar erros de schema/formato do documento de erros de dados por linha;
7. resumir registros válidos;
8. filtrar registros válidos por severidade, estado de resolução ou serviço;
9. formatar um relatório de texto determinístico;
10. comprovar caminhos de sucesso e falha com testes automatizados.

## 2. Contrato do conjunto de dados

O cabeçalho obrigatório exato é:

```text
event_id,service,severity,duration_minutes,resolved,occurred_on
```

Cada coluna possui um contrato diferente:

```text
event_id         -> inteiro ASCII positivo
service          -> texto legível não vazio, com espaços normalizados
severity         -> low | medium | high | critical
duration_minutes -> inteiro ASCII não negativo
resolved         -> true | false
occurred_on      -> data de calendário exata em YYYY-MM-DD
```

Todos os registros de exemplo são fictícios.

## 3. Por que o cabeçalho é rígido

CSV é apenas um formato contêiner. Um arquivo ser um CSV válido não significa que contém a tabela esperada pelo programa.

Estes são schemas diferentes:

```text
event_id,service,severity,duration_minutes,resolved,occurred_on
```

e:

```text
service,event_id,severity,duration_minutes,resolved,occurred_on
```

Este projeto exige deliberadamente os nomes e a ordem exatos definidos em `EXPECTED_HEADERS`.

Isso torna alterações inesperadas de schema visíveis em vez de mapear dados incorretamente em silêncio.

## 4. Erros estruturais versus erros de linha

O analisador separa dois níveis de falha.

### Falhas no nível do documento

Exemplos:

- ausência de linha de cabeçalho;
- nomes de cabeçalho duplicados;
- nomes ou ordem de cabeçalho incorretos;
- aspas malformadas rejeitadas pelo parser CSV do Python.

Esses casos levantam `CsvSchemaError` ou `CsvFormatError`, pois o documento não pode ser confiado como a tabela esperada.

### Falhas no nível da linha

Exemplos:

- `event_id` igual a zero;
- severidade igual a `urgent`;
- duração negativa;
- resolved igual a `yes`;
- data igual a `2026-02-30`;
- linha com valores extras ou ausentes.

Esses casos geram um `RejectedRow`. As demais linhas válidas permanecem disponíveis para análise.

## 5. Conversão tipada

`csv.DictReader` retorna valores em texto. O projeto não mantém tudo como strings.

Uma linha válida se transforma em:

```python
IncidentRecord(
    event_id=101,
    service="Payments",
    severity=Severity.HIGH,
    duration_minutes=45,
    resolved=True,
    occurred_on=date(2026, 8, 1),
)
```

Assim, erros de conversão ficam concentrados na fronteira de entrada e o restante do programa trabalha com tipos mais fortes.

## 6. Contratos de inteiros

Dois helpers deixam a intenção numérica explícita:

```python
parse_positive_integer(...)
parse_non_negative_integer(...)
```

`event_id` deve ser maior que zero.

`duration_minutes` pode ser zero.

Os parsers aceitam somente dígitos decimais ASCII. Valores como `-1`, `1.5` e dígitos Unicode de largura total são rejeitados pelo contrato deste projeto.

## 7. Normalização de serviço

Nomes de serviço são dados voltados à exibição.

O analisador reduz espaços externos e repetidos:

```python
normalize_service("  Data   Sync ")
# "Data Sync"
```

A capitalização é preservada e existe um pequeno limite de tamanho definido pelo projeto.

Para agrupamento e filtro, a comparação de serviços ignora maiúsculas e minúsculas, enquanto o primeiro formato de exibição aceito é preservado no resumo.

## 8. Severidade como enum

A severidade usa:

```python
class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
```

A entrada não diferencia maiúsculas e minúsculas, então `HIGH`, `high` e ` High ` se tornam `Severity.HIGH`.

Valores desconhecidos são rejeitados em vez de entrarem no modelo como texto arbitrário.

## 9. Parsing Boolean estrito

A coluna `resolved` aceita apenas:

```text
true
false
```

ignorando espaços externos e capitalização.

Valores como `yes`, `1` ou `truthy` são rejeitados.

Isso evita inventar regras surpreendentes de truthiness para dados externos.

## 10. Parsing estrito de datas

As datas devem usar exatamente:

```text
YYYY-MM-DD
```

O parser verifica tanto o formato quanto a validade do calendário.

Assim:

```text
2024-02-29 -> válido
2026-2-01  -> formato inválido
20260201   -> formato inválido
2026-02-30 -> data de calendário inválida
```

O resultado é um objeto real `datetime.date`, não uma string com aparência de data.

## 11. Registros válidos imutáveis

`IncidentRecord` é uma dataclass congelada com slots.

A validação também roda quando o construtor é chamado diretamente, então não é possível ignorar as regras simplesmente pulando o parser CSV.

O parser retorna tuplas de registros em vez de expor listas internas mutáveis.

## 12. Problemas no nível de campo

Uma única linha ruim pode conter vários problemas independentes.

Por exemplo:

```text
0, ,urgent,-2,yes,2026-02-30
```

gera problemas para:

```text
event_id
service
severity
duration_minutes
resolved
occurred_on
```

O projeto coleta todos esses problemas da linha lógica em vez de parar no primeiro erro.

## 13. Numeração de linhas lógicas

`RejectedRow.row_number` identifica a linha lógica do CSV, considerando o cabeçalho como linha 1 e o primeiro registro de dados como linha 2.

Linhas físicas completamente vazias são ignoradas pelo leitor CSV do Python.

Este projeto usa numeração de registros lógicos e não promete números físicos exatos para qualquer combinação possível de campos CSV multilinha entre aspas.

## 14. Valores extras e ausentes

Uma linha com mais valores do que o schema permite é rejeitada com um problema `_row`.

Uma linha com campo final ausente fornece `None` ao parser daquele campo e é rejeitada pelo contrato correspondente.

Isso impede que dados truncados ou deslocados pareçam válidos.

## 15. Identificadores duplicados

`event_id` deve ser único entre **linhas válidas aceitas**.

Se um `event_id=101` válido já foi aceito, uma linha válida posterior com `event_id=101` será rejeitada.

Uma linha anterior inválida não reserva o ID. Portanto, uma linha válida posterior pode usar o mesmo ID.

Essa regra faz do conjunto aceito a fonte da unicidade.

## 16. Leitura de arquivo e BOM UTF-8

`load_incident_csv(...)` abre arquivos com:

```python
encoding="utf-8-sig"
newline=""
```

`utf-8-sig` aceita um arquivo UTF-8 normal e remove um BOM UTF-8 opcional no início.

`newline=""` segue a orientação do módulo CSV do Python para que o próprio parser controle quebras de linha.

Arquivos inexistentes propagam `FileNotFoundError` intencionalmente.

## 17. Pontos de entrada por texto, stream e arquivo

O projeto expõe três fronteiras de entrada:

```python
parse_incident_csv(stream)
parse_incident_csv_text(text)
load_incident_csv(path)
```

O comportamento central de parsing permanece em `parse_incident_csv(...)`.

Isso separa I/O de arquivo da conversão de linhas e facilita testes com `StringIO` ou strings literais.

## 18. Resultado do parsing

O parsing bem-sucedido retorna:

```python
CsvLoadResult(
    records=(...),
    rejected_rows=(...),
)
```

Propriedades auxiliares fornecem:

```text
valid_count
rejected_count
data_row_count
```

`data_row_count` conta linhas lógicas aceitas mais rejeitadas, sem incluir o cabeçalho.

## 19. Agregação determinística

`summarize_incidents(...)` calcula:

- total de registros válidos;
- quantidades resolvida e não resolvida;
- duração total;
- duração média com duas casas decimais;
- maior duração;
- contagem para cada severidade;
- contagem por serviço.

As contagens de serviço são ordenadas sem diferenciar maiúsculas e minúsculas para produzir saída estável.

As severidades sempre seguem a ordem do enum:

```text
low
medium
high
critical
```

## 20. Arredondamento exato da média

A média é retornada como `Decimal` com duas casas decimais.

A implementação não depende do contexto global de `decimal` do chamador. Ela calcula centésimos inteiros diretamente e aplica arredondamento half-up.

Por exemplo, uma média exata de `0.375` se torna:

```text
0.38
```

Isso mantém o relatório determinístico.

## 21. Análise vazia

Um conjunto válido vazio ainda pode ser analisado.

O resumo retorna:

```text
total de registros: 0
duração média: 0.00
maior duração: 0
contagens por serviço: vazio
todas as severidades: 0
```

Não é necessário gerar uma exceção de divisão por zero.

## 22. Invariantes do resumo

`IncidentSummary` valida o próprio construtor público.

Entre outras verificações:

- resolvidos + não resolvidos deve ser igual ao total;
- contagens de severidade devem conter cada valor do enum exatamente uma vez;
- total das severidades deve ser igual ao total de registros;
- chaves de serviço devem ser únicas sem diferenciar capitalização;
- contagens de serviço devem estar ordenadas deterministicamente;
- total das contagens de serviço deve ser igual ao total de registros.

Um resumo que se contradiz é rejeitado.

## 23. Filtros

`filter_incidents(...)` pode combinar critérios opcionais:

```python
filter_incidents(
    records,
    severity=Severity.HIGH,
    resolved=True,
    service="Payments",
)
```

A função retorna uma tupla e não modifica a coleção original.

A comparação de serviço ignora maiúsculas e minúsculas depois da mesma normalização de espaços usada pelo modelo.

## 24. Relatório de texto determinístico

`format_analysis(...)` produz um relatório estável em estilo CLI:

```text
data rows: 6
valid: 4
rejected: 2
resolved: 3
unresolved: 1
total duration: 165
average duration: 41.25
longest duration: 90
```

A função também verifica se o resumo informado corresponde à mesma quantidade de linhas válidas do resultado de parsing.

## 25. Estrutura do projeto

```text
04-csv-analyzer/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── csv_analyzer.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_csv_analyzer.py
```

## 26. Executando a demonstração determinística

A partir da raiz do repositório:

```bash
python practical-projects/04-csv-analyzer/demo.py
```

Saída esperada:

```text
data rows: 6
valid: 4
rejected: 2
resolved: 3
unresolved: 1
total duration: 165
average duration: 41.25
longest duration: 90
critical: 1
```

A demonstração contém intencionalmente duas linhas inválidas para tornar o comportamento de rejeição visível.

## 27. Executando os testes do projeto

```bash
python -m pytest -q practical-projects/04-csv-analyzer/tests
```

A suíte inicial contém **73 cenários pytest** cobrindo helpers de parsing, validação direta dos modelos, falhas de schema, CSV malformado, problemas de campo por linha, IDs duplicados, BOM UTF-8, leitura de arquivo, invariantes de agregação, filtros e relatório determinístico.

## 28. Caminhos de falha para inspecionar manualmente

Experimente alterar os dados da demo para incluir:

```text
ordem de cabeçalho incorreta
occurred_on ausente
sétimo valor extra
severity = urgent
resolved = yes
occurred_on = 2026-02-30
event_id válido duplicado
```

Observe quais problemas interrompem o documento e quais rejeitam apenas uma linha.

## 29. Nota de design: parsear na fronteira

O restante do analisador não deve perguntar repetidamente se `"45"` é um número ou se `"true"` significa um Boolean.

Essas conversões acontecem uma vez na fronteira CSV.

Depois que uma linha vira `IncidentRecord`, as funções seguintes podem confiar em seus tipos e invariantes.

## 30. Nota de design: sucesso parcial útil

Muitos fluxos de importação precisam decidir se uma única linha inválida deve destruir todas as linhas válidas.

Este projeto escolhe:

```text
estrutura de documento inválida -> interromper
dados de linha inválidos        -> rejeitar linha e manter válidas
```

Essa não é a única política possível, mas é explícita, testável e útil para estudar design de ingestão de dados.

## 31. Nota de design: biblioteca padrão antes de pandas

A Fase 9 já apresentou pandas. Este projeto usa deliberadamente o módulo `csv` do Python.

O objetivo é expor mecanismos que pandas costuma esconder:

- expectativas de schema;
- conversão de strings brutas;
- campos extras e ausentes;
- política de rejeição por linha;
- duplicidade de identificadores;
- registros de domínio imutáveis.

Entender essas fronteiras facilita raciocinar sobre dataframes depois.

## 32. O que este projeto não inclui intencionalmente

Esta versão não inclui:

- detecção automática de delimitador;
- schemas arbitrários definidos pelo usuário;
- pandas;
- entrada Excel;
- persistência em banco de dados;
- datasets maiores que a memória com streaming;
- processamento paralelo;
- correção fuzzy de valores inválidos;
- gráficos ou dashboards;
- interface gráfica.

Esses itens são extensões possíveis, mas diluiriam a principal lição de ingestão e validação.

## 33. Desafio de extensão: schema configurável

Extraia as regras de campo para especificações reutilizáveis de colunas.

Uma versão futura poderia definir:

```text
nome da coluna
obrigatória/opcional
parser
normalizador
valor padrão
regra de unicidade
```

Mantenha o projeto atual simples antes de generalizá-lo.

## 34. Desafio de extensão: exportar rejeições

Grave as linhas lógicas rejeitadas e suas mensagens de problema em um segundo arquivo CSV.

Pense cuidadosamente em:

- colunas estáveis;
- quoting;
- vários problemas por linha;
- preservação ou não dos valores brutos;
- riscos de formula injection em CSV caso o arquivo seja aberto em software de planilhas.

## 35. Desafio de extensão: filtros de data

Adicione datas inicial e final opcionais a `filter_incidents(...)`.

Defina se os limites são inclusivos e teste intervalos inválidos, como data inicial posterior à data final.

## 36. Discussão de portfólio

Ao apresentar este projeto, explique mais do que “ele lê arquivos CSV”.

Pontos de engenharia úteis incluem:

- contratos exatos de schema;
- falhas estruturais versus falhas de linha;
- conversão tipada na fronteira dos dados;
- registros aceitos imutáveis;
- diagnóstico com vários campos por linha rejeitada;
- detecção de duplicidade entre linhas válidas;
- agregação e arredondamento determinísticos;
- invariantes públicas do resumo;
- pontos de entrada testáveis por arquivo, stream e texto;
- uso deliberado da biblioteca padrão em vez de esconder a ingestão atrás de pandas.

## 37. Checklist de revisão

Antes de considerar sua própria implementação concluída, verifique:

- Os nomes e a ordem dos cabeçalhos são verificados antes de confiar nas linhas?
- Cabeçalhos duplicados são rejeitados?
- CSV malformado levanta um erro no nível do documento?
- Uma linha ruim pode coexistir com linhas válidas no resultado?
- Todos os problemas de campo da linha rejeitada ficam visíveis?
- Valores extras e ausentes são detectados?
- Os `event_id` aceitos são únicos?
- Uma linha inválida deixa de reservar seu ID?
- Datas se tornam objetos reais `date` após o parsing?
- O parsing Boolean é explícito em vez de baseado em truthiness?
- As contagens do resumo são internamente consistentes?
- O arredondamento da média é determinístico?
- Os filtros não modificam os dados originais?
- Os exemplos são fictícios e seguros para publicação?

## 38. Próximo projeto

O Projeto 04 adiciona ingestão CSV consciente de schema, validação por linha, conversão tipada, política de sucesso parcial, filtros determinísticos e agregação à progressão da Fase 10.

O próximo projeto planejado é o **Gerador de Relatórios**, que mudará o foco da ingestão de dados estruturados para a composição de saídas estruturadas e relatórios prontos para apresentação.
