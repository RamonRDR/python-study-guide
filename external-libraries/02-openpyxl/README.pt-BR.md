<div align="center">

# Automatizando Workbooks do Excel com `openpyxl`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Bibliotecas Externas](../README.pt-BR.md) · [← Anterior: `pandas`](../01-pandas/README.pt-BR.md)

O `pandas` trata dados semelhantes aos de planilhas principalmente como tabelas. O `openpyxl` atua em outra camada: o próprio workbook do Excel. Ele permite que Python crie, inspecione, edite, formate e salve workbooks Office Open XML preservando conceitos como planilhas, células, fórmulas, estilos, tabelas, validações, gráficos e configurações de impressão.

Este capítulo tem como alvo **openpyxl 3.1.x** e foi pesquisado com base na documentação atual da série 3.1 e no pacote estável **openpyxl 3.1.5** publicado no PyPI. O PyPI declara Python 3.8 ou superior; este repositório valida os exemplos em Python 3.13.

**Tempo estimado de estudo:** 240–330 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar quando `openpyxl` é mais adequado do que `pandas` ou o módulo padrão `csv`;
- criar, carregar, inspecionar e salvar workbooks `.xlsx`;
- trabalhar com segurança com planilhas, células, intervalos e iteração por linhas;
- distinguir fórmulas de valores calculados;
- entender o que `data_only`, `read_only`, `write_only` e `keep_vba` realmente significam;
- aplicar estilos reutilizáveis, formatos numéricos, dimensões e congelamento de painéis;
- criar tabelas, regras de validação, filtros, comentários, hyperlinks e gráficos;
- compreender os limites de células mescladas, movimentação de linhas/colunas, tradução de fórmulas, preservação de VBA e fidelidade de round-trip;
- escolher modos otimizados para workbooks grandes;
- tratar arquivos de planilha como entrada externa com limites explícitos de segurança e validação;
- combinar `pandas` e `openpyxl` sem confundir suas responsabilidades;
- construir automações determinísticas de workbook que possam ser revisadas e testadas sem Microsoft Excel instalado.

## 1. Por que `openpyxl` existe

Workbooks do Excel contêm mais do que dados retangulares. Eles podem conter várias planilhas, fórmulas, formatação, tabelas, regras de validação, regiões mescladas, gráficos, comentários, hyperlinks, configurações de impressão e metadados do workbook.

`openpyxl` é uma biblioteca Python de terceiros para leitura e escrita de arquivos de planilha Office Open XML, como `.xlsx` e `.xlsm`.

Use-a quando a **estrutura do workbook em si importa**.

## 2. `pandas` e `openpyxl` resolvem problemas diferentes

Uma distinção útil é:

```text
pandas   -> manipulate tabular data
openpyxl -> manipulate Excel workbook structure
```

Se você precisa agrupar dez milhões de linhas, `pandas` normalmente oferece uma abstração melhor. Se precisa definir `B2` como fórmula, congelar a primeira linha, aplicar um formato numérico, criar uma tabela do Excel ou preservar o layout do workbook, `openpyxl` é a camada mais natural.

Muitos fluxos reais usam os dois.

## 3. Bibliotecas externas exigem um contrato de dependências

O repositório declara as dependências executáveis da Fase 9 em `requirements-external.txt`.

Para este capítulo, o contrato é:

```text
openpyxl >= 3.1 and < 3.2
```

Fixar uma série minor suportada evita ensinar silenciosamente sobre uma API futura desconhecida, ao mesmo tempo em que permite releases de patch compatíveis.

## 4. Instale a dependência em um ambiente isolado

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative-o conforme seu sistema operacional e instale o contrato do repositório:

```bash
python -m pip install -r requirements-external.txt
```

Um `pip install openpyxl` direto é válido para experimentação, mas um arquivo de dependências torna o ambiente do projeto reproduzível.

## 5. Conheça os formatos de workbook no escopo

`openpyxl` foi projetado em torno de formatos Office Open XML como:

```text
.xlsx
.xlsm
.xltx
.xltm
```

Ele não é um leitor genérico para todo arquivo que o Excel consegue abrir. Em particular, arquivos binários legados `.xls` e workbooks `.xlsb` são formatos diferentes e exigem outras ferramentas.

Trate a extensão como parte do contrato de entrada.

## 6. Crie um workbook

A classe central é `Workbook`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
print(worksheet.title)
```

```text
Sheet
```

Um novo workbook normal começa com uma planilha ativa.

## 7. Dê nomes significativos às planilhas

Renomeie a planilha ativa ou crie planilhas adicionais explicitamente:

```python
from openpyxl import Workbook


workbook = Workbook()
summary = workbook.active
summary.title = "Summary"
details = workbook.create_sheet("Details")
print(workbook.sheetnames)
```

```text
['Summary', 'Details']
```

Nomes de planilhas fazem parte da navegação do workbook e também podem aparecer em fórmulas e nomes definidos.

## 8. Selecione uma planilha pelo nome

Use acesso semelhante a um mapeamento:

```python
from openpyxl import Workbook


workbook = Workbook()
workbook.active.title = "Summary"
worksheet = workbook["Summary"]
print(worksheet.title)
```

Evite depender da posição física de uma planilha quando o nome é o contrato real.

## 9. Células usam coordenadas no estilo Excel

Células podem ser acessadas com coordenadas como `A1`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = "status"
worksheet["B1"] = "ready"
print(worksheet["B1"].value)
```

```text
ready
```

Coordenadas são convenientes quando o layout do workbook é fixo e significativo.

## 10. `cell()` usa índices de linha e coluna iniciando em um

Geração programática costuma combinar melhor com `Worksheet.cell()`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.cell(row=2, column=3, value=42)
print(worksheet["C2"].value)
```

```text
42
```

Linhas e colunas do Excel são indexadas a partir de um nessa API.

## 11. Acessar células pode criá-las em memória

Uma planilha normal cria objetos de célula quando eles são acessados pela primeira vez. Isso significa que um loop sobre um intervalo de coordenadas enorme e desnecessário pode alocar muitas células mesmo sem atribuir dados úteis.

Não percorra um retângulo de um milhão por um milhão apenas para descobrir quais células existem.

Use intervalos conhecidos, dimensões da planilha ou modo de leitura otimizado quando apropriado.

## 12. Adicione linhas completas com `append()`

Para saída orientada a linhas, `append()` costuma ser mais claro do que atribuir cada coordenada:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["item", "quantity"])
worksheet.append(["Cable", 3])
worksheet.append(["Adapter", 2])
print(worksheet.max_row)
```

```text
3
```

Isso funciona bem para exports montados registro por registro.

## 13. Itere linhas em vez de codificar cada célula

`iter_rows()` expõe uma região retangular:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["name", "score"])
worksheet.append(["A", 8])
worksheet.append(["B", 9])

for row in worksheet.iter_rows(min_row=2, values_only=True):
    print(row)
```

```text
('A', 8)
('B', 9)
```

`values_only=True` retorna valores Python em vez de objetos `Cell` quando os metadados da célula não são necessários.

## 14. Itere colunas apenas quando o padrão de acesso exigir

Planilhas normais também suportam `iter_cols()`. A iteração por linhas costuma ser mais natural para dados semelhantes a registros, enquanto a iteração por colunas é útil quando a regra do workbook é orientada a coluna.

O modo otimizado read-only possui uma API mais restrita, então não projete todo fluxo em torno de métodos indisponíveis nele.

## 15. Dimensões da planilha são uma pista, não uma regra de negócio

Propriedades como `max_row`, `max_column` e `calculate_dimension()` descrevem a região aparentemente usada da planilha.

Elas não provam que cada célula dentro dessa região contém dados significativos.

Células vazias porém formatadas, metadados antigos ou geradores de terceiros podem tornar as dimensões maiores ou menores do que o esperado.

## 16. Salve deliberadamente em um novo caminho

Um workbook é persistido com `save()`:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from openpyxl import Workbook


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "report.xlsx"
    workbook = Workbook()
    workbook.active["A1"] = "ready"
    workbook.save(path)
    print(path.exists())
```

```text
True
```

Em automações de produção, prefira um caminho de saída deliberado a sobrescrever casualmente o workbook de origem.

## 17. Carregue um workbook existente

Use `load_workbook()`:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from openpyxl import Workbook, load_workbook


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "input.xlsx"
    workbook = Workbook()
    workbook.active["A1"] = "loaded"
    workbook.save(path)

    reloaded = load_workbook(path)
    print(reloaded.active["A1"].value)
    reloaded.close()
```

```text
loaded
```

Fechar explicitamente é especialmente importante em workbooks read-only e é um bom hábito para recursos associados a arquivos.

## 18. Um round-trip pode perder recursos não suportados

Abrir um workbook complexo e salvá-lo novamente não garante a preservação de todo artefato criado pelo Excel ou por outro aplicativo.

O tutorial oficial alerta explicitamente que openpyxl não lê todos os itens possíveis de um workbook e que algumas shapes podem ser perdidas durante um round-trip de load/save.

Portanto:

```text
load -> edit one cell -> save
```

não é automaticamente uma transformação sem perdas para qualquer workbook.

## 19. `read_only=True` é um modo de operação diferente

Workbooks grandes podem consumir muita memória. O modo read-only carrega o conteúdo da planilha de forma lazy:

```python
from openpyxl import load_workbook


workbook = load_workbook("large.xlsx", read_only=True, data_only=True)
worksheet = workbook["Data"]
for row in worksheet.iter_rows(values_only=True):
    process = row
workbook.close()
```

O exemplo é intencionalmente ilustrativo, e não executável no repositório, porque depende de um arquivo externo.

Planilhas read-only não são planilhas normais editáveis.

## 20. O modo read-only deve ser fechado explicitamente

A documentação oficial dos modos otimizados destaca `close()` para workbooks read-only.

Use uma fronteira `try/finally` quando o processamento posterior puder falhar:

```python
from openpyxl import load_workbook


workbook = load_workbook("large.xlsx", read_only=True)
try:
    worksheet = workbook.active
    for row in worksheet.iter_rows(values_only=True):
        process = row
finally:
    workbook.close()
```

A liberação do recurso deve sobreviver a exceções.

## 21. Dimensões em read-only podem estar incorretas

A leitura lazy depende dos metadados de dimensões armazenados no workbook. Alguns aplicativos produtores gravam essas dimensões incorretamente.

A documentação recomenda verificar `calculate_dimension()` e, quando você sabe que o metadado está errado, usar `reset_dimensions()` em uma planilha read-only.

Faça isso somente quando houver um motivo externo para saber que as dimensões gravadas estão incorretas.

## 22. `write_only=True` é otimizado para saída em streaming

Workbooks write-only são criados de forma diferente:

```python
from openpyxl import Workbook


workbook = Workbook(write_only=True)
worksheet = workbook.create_sheet("Data")
worksheet.append(["id", "value"])
worksheet.append([1, 10])
worksheet.append([2, 20])
```

Diferente de `Workbook()` normal, um workbook write-only começa sem planilha. Você precisa criar uma explicitamente.

## 23. O modo write-only é orientado a `append()`

Uma planilha write-only foi desenhada para saída sequencial. Linhas são adicionadas com `append()` em vez de leitura e escrita arbitrária de células.

Isso combina bem com exports grandes em que registros chegam em ordem e linhas anteriores não precisam ser editadas novamente.

## 24. Um workbook write-only só pode ser salvo uma vez

A documentação dos modos otimizados informa que um workbook write-only pode ser salvo apenas uma vez.

Portanto, o fluxo deve ser:

```text
configure workbook -> append rows -> save once
```

e não:

```text
save -> append more -> save again
```

Crie configurações de workbook que precisam existir antes dos dados antes de iniciar o streaming de linhas.

## 25. Escolha conscientemente entre normal, read-only e write-only

| Necessidade | Prefira |
|---|---|
| editar células arbitrárias | workbook normal |
| inspecionar estilos, gráficos, imagens e estrutura completa | workbook normal |
| fazer streaming de planilha existente muito grande | `read_only=True` |
| fazer streaming de novo export muito grande | `Workbook(write_only=True)` |
| salvar repetidamente durante edição | workbook normal |

Modos otimizados trocam recursos por menor uso de memória.

## 26. Valores Python são convertidos para valores de célula

Células podem armazenar valores Python comuns como strings, números, booleanos, datas, datetimes e fórmulas representadas por strings iniciadas com `=`.

Mantenha sua validação de domínio separada. O fato de um valor poder ser gravado em uma célula não significa que ele seja válido para sua aplicação.

## 27. Datas são valores mais formatos numéricos

Excel armazena valores de data/hora com semântica de data de planilha e os exibe por meio de formatos numéricos.

Ao atribuir um `datetime` Python, openpyxl aplica automaticamente um formato compatível com data/hora:

```python
from datetime import datetime

from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = datetime(2026, 8, 29, 14, 30)
print(worksheet["A1"].is_date)
```

```text
True
```

Não trate o texto exibido no Excel como a única representação relevante.

## 28. Excel possui dois sistemas de data

Datas de planilhas podem usar o sistema 1900 ou 1904, dependendo das configurações e do histórico do workbook.

Deixe o workbook e openpyxl gerenciarem a conversão em vez de adicionar manualmente um número fixo de dias a valores seriais.

Aritmética manual de serial é uma forma fácil de criar erros de época e deslocamento.

## 29. Fórmulas são armazenadas como fórmulas

Atribua uma string de fórmula iniciada por `=`:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = 10
worksheet["A2"] = 20
worksheet["A3"] = "=SUM(A1:A2)"
print(worksheet["A3"].value)
```

```text
=SUM(A1:A2)
```

A célula contém uma expressão de fórmula, não um cálculo Python.

## 30. `openpyxl` não calcula fórmulas

Esta é uma das fronteiras mais importantes da biblioteca.

`openpyxl` consegue ler e gravar expressões de fórmula, mas não é um motor de cálculo do Excel. Gravar `=SUM(A1:A2)` não faz openpyxl calcular `30`.

Se seu fluxo Python precisa do resultado naquele momento, calcule o valor em Python ou use um motor de cálculo separado com contrato documentado.

## 31. `data_only=True` lê resultados em cache

Ao carregar um workbook, `data_only` controla se células com fórmula expõem a fórmula ou o valor em cache deixado pela última aplicação de planilha que calculou o arquivo.

```text
load_workbook(path, data_only=False) -> formula text
load_workbook(path, data_only=True)  -> cached result, if available
```

Um workbook recém-criado pode não possuir nenhum valor calculado em cache.

Não confunda `data_only=True` com “calcular fórmulas agora”.

## 32. Nomes de fórmulas são gravados em inglês

A documentação de fórmulas do openpyxl informa que os nomes das funções devem estar em inglês e os argumentos usam vírgulas.

Por exemplo:

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = "=SUM(1,2,3)"
print(worksheet["A1"].value)
```

```text
=SUM(1,2,3)
```

Não gere sintaxe de fórmula específica de idioma com base em como o Excel mostra fórmulas em uma máquina.

## 33. Estilos são objetos do workbook, não strings de aparência

Componentes comuns de estilo incluem:

```text
Font
PatternFill / GradientFill
Border
Alignment
Protection
number_format
```

O modelo é explícito porque a aparência de uma célula do Excel é composta por várias propriedades independentes.

## 34. Aplique fonte, preenchimento e alinhamento

```python
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill


workbook = Workbook()
worksheet = workbook.active
cell = worksheet["A1"]
cell.value = "Header"
cell.font = Font(bold=True)
cell.fill = PatternFill(fill_type="solid", fgColor="D9EAF7")
cell.alignment = Alignment(horizontal="center")
print(cell.font.bold)
```

```text
True
```

Formatação deve comunicar estrutura, não compensar dados pouco claros.

## 35. Estilos de célula são efetivamente imutáveis após atribuição

A documentação oficial de estilos explica que componentes atribuídos são compartilhados e não podem ser alterados in-place.

Isto é intencionalmente inválido:

```text
a1.font.italic = True
```

Atribua um novo objeto `Font`:

```python
from openpyxl import Workbook
from openpyxl.styles import Font


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"].font = Font(color="FF0000")
worksheet["A1"].font = Font(color="FF0000", italic=True)
print(worksheet["A1"].font.italic)
```

```text
True
```

## 36. Reutilize objetos de estilo em vez de criar milhares de variações

Se muitas células compartilham o mesmo papel visual, reutilize a mesma definição de estilo ou um `NamedStyle`.

Criar objetos levemente diferentes para cada célula pode inflar a tabela de estilos e o tamanho do arquivo.

Trate estilos como um vocabulário controlado: cabeçalho, moeda, data, alerta, entrada, saída.

## 37. Formatos numéricos mudam a exibição, não o valor armazenado

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet["A1"] = 0.125
worksheet["A1"].number_format = "0.00%"
print(worksheet["A1"].value)
```

```text
0.125
```

O Excel pode mostrar `12.50%`, mas o valor numérico armazenado continua sendo `0.125`.

Essa diferença importa quando outro programa lê o workbook.

## 38. Named styles tornam formatação repetida explícita

```python
from openpyxl import Workbook
from openpyxl.styles import Font, NamedStyle


workbook = Workbook()
worksheet = workbook.active
header = NamedStyle(name="header")
header.font = Font(bold=True)
workbook.add_named_style(header)
worksheet["A1"].style = "header"
print(worksheet["A1"].style)
```

```text
header
```

Depois que um named style é atribuído a uma célula, alterações posteriores no `NamedStyle` não reestilizam retroativamente essa célula.

## 39. Largura de coluna e altura de linha são metadados de layout

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.column_dimensions["A"].width = 24
worksheet.row_dimensions[1].height = 30
print(worksheet.column_dimensions["A"].width)
```

```text
24.0
```

Não presuma que openpyxl reproduzirá o AutoFit interativo do Excel apenas com base no conteúdo.

## 40. Freeze panes preserva contexto durante a rolagem

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.freeze_panes = "A2"
print(worksheet.freeze_panes)
```

```text
A2
```

`A2` congela as linhas acima da linha 2, mantendo a primeira linha visível.

## 41. Células mescladas possuem uma única célula real de valor

Quando um intervalo é mesclado, apenas a célula superior esquerda é a célula normal que carrega valor. As outras posições se tornam placeholders de merged cell.

```python
from openpyxl import Workbook


workbook = Workbook()
worksheet = workbook.active
worksheet.merge_cells("A1:C1")
worksheet["A1"] = "Quarterly report"
print(worksheet["A1"].value)
```

```text
Quarterly report
```

Células mescladas são estrutura de apresentação, não substituto para dados tabulares normalizados.

## 42. Inserções e exclusões não gerenciam todas as dependências

`insert_rows()`, `delete_rows()`, `insert_cols()` e `delete_cols()` podem deslocar células.

A documentação oficial observa que openpyxl não gerencia toda dependência que possa referenciar as células afetadas, como fórmulas, tabelas ou gráficos.

Uma edição estrutural pode, portanto, exigir lógica específica da aplicação para reparar referências.

## 43. `move_range()` pode traduzir algumas fórmulas, não toda referência

`move_range(..., translate=True)` pode traduzir fórmulas dentro das células movidas.

Porém, referências a essas células vindas de outras células ou de nomes definidos não são atualizadas automaticamente por essa operação.

Não confunda “células movidas” com “semântica do workbook reparada”.

## 44. Tabelas de planilha adicionam semântica de tabela do Excel

Uma worksheet table é mais do que um intervalo colorido. Ela possui nome e referência de células definida:

```python
from openpyxl import Workbook
from openpyxl.worksheet.table import Table


workbook = Workbook()
worksheet = workbook.active
worksheet.append(["item", "amount"])
worksheet.append(["A", 10])
worksheet.append(["B", 20])
table = Table(displayName="SalesTable", ref="A1:B3")
worksheet.add_table(table)
print(list(worksheet.tables.keys()))
```

```text
['SalesTable']
```

Tabelas são úteis quando usuários posteriores do Excel esperam referências estruturadas e formatação consciente de tabela.

## 45. Nomes e cabeçalhos de tabela são contratos

Display names de tabela precisam ser válidos e únicos no namespace relevante do workbook. A documentação também exige que os cabeçalhos das colunas sejam strings.

Valide cabeçalhos antes de construir a tabela em vez de depender do Excel para reparar uma saída malformada depois.

## 46. Filtros descrevem comportamento do workbook; não filtram dados Python

Auto filters podem ser configurados para que aplicações de planilha saibam quais linhas exibir sob certos critérios.

Isso é diferente de filtrar registros em Python antes de gravá-los.

Se um relatório deve conter fisicamente apenas linhas aprovadas, filtre os dados Python primeiro. Se usuários precisam de filtragem interativa no Excel, configure uma tabela ou auto filter como comportamento de apresentação.

## 47. Regras de validação são gravadas, não executadas por openpyxl

A documentação oficial de validação é explícita: validadores não são aplicados nem avaliados por openpyxl.

```python
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation


workbook = Workbook()
worksheet = workbook.active
validation = DataValidation(type="list", formula1='"open,closed"')
worksheet.add_data_validation(validation)
validation.add("A2:A20")
print(len(worksheet.data_validations.dataValidation))
```

```text
1
```

A regra se torna metadado do workbook que o Excel ou outra aplicação compatível pode aplicar interativamente.

## 48. Formatação condicional também é comportamento do workbook

Regras de conditional formatting dizem a uma aplicação de planilha como formatar células quando condições são atendidas.

Não use formatação condicional como substituto oculto para validação de dados. Uma célula vermelha pode comunicar um erro a uma pessoa, mas o programa Python ainda deve validar entradas críticas explicitamente.

## 49. Gráficos referenciam dados da planilha

`openpyxl.chart` pode construir gráficos a partir de intervalos. Um fluxo típico cria um chart, define objetos `Reference` para dados e categorias e ancora o gráfico em uma planilha.

Gráficos são objetos de apresentação sobre dados da planilha. Teste os números subjacentes separadamente do layout do gráfico.

## 50. Imagens introduzem uma dependência opcional de Pillow

A API de imagens pode inserir imagens raster em planilhas, mas o tratamento de imagens depende de Pillow.

Como o contrato executável deste capítulo não exige imagens, Pillow não é adicionada apenas por causa de um exemplo decorativo.

Adicione dependências opcionais somente quando o projeto realmente precisa da funcionalidade.

## 51. Comentários e hyperlinks são metadados de célula

Células podem conter comentários e hyperlinks além de valores e estilos.

Use esses recursos quando oferecerem contexto útil para humanos, mas mantenha informações essenciais legíveis por máquina em células normais ou dados estruturados em vez de escondê-las em comentários.

## 52. Nomes definidos podem representar referências no nível do workbook

Defined names do Excel podem apontar para células, intervalos, constantes ou fórmulas e podem ter escopo do workbook ou da planilha.

Eles são úteis para contratos de workbook, mas também criam outra camada de dependência quando células são movidas ou planilhas renomeadas.

Inspecione nomes definidos antes de realizar edições estruturais em templates complexos.

## 53. Proteção de planilha não é criptografia

Proteção de célula e worksheet controla comportamento de edição na planilha. Não substitui criptografia de arquivos sensíveis nem autorização no servidor.

Trate proteção do workbook como uma restrição de interface, não como limite de segurança.

## 54. Configurações de impressão fazem parte do produto workbook

Orientação de página, margens, áreas de impressão, títulos repetidos e escala podem importar quando um `.xlsx` deve virar PDF ou relatório impresso.

Para um workbook de troca de dados, isso pode ser irrelevante. Para um relatório voltado a pessoas, pode fazer parte dos critérios de aceite.

## 55. Entenda as flags importantes de `load_workbook()`

Flags comuns incluem:

```text
read_only=True  -> lazy, lower-memory reading
data_only=True  -> cached formula results instead of formula text
keep_vba=True   -> preserve VBA content when possible
keep_links=True -> preserve cached external-link data
rich_text=True  -> preserve rich text formatting in cells
```

Cada flag muda o contrato. Não as ative apenas porque parecem mais seguras ou completas.

## 56. `keep_vba=True` preserva VBA; não permite editá-lo

O tutorial oficial informa que elementos VBA podem ser preservados, mas continuam não editáveis pelo openpyxl.

Se um `.xlsm` com macros precisa fazer round-trip preservando VBA, use a extensão correspondente e `keep_vba=True`, e teste o artefato real.

Preservação não significa execução, inspeção ou modificação.

## 57. Incompatibilidades entre template e extensão podem quebrar expectativas

Tipo do workbook, extensão do arquivo e configurações de VBA/template devem estar alinhados.

Salvar um workbook com macros usando a extensão errada ou ignorar seu contrato de VBA pode produzir um arquivo rejeitado pelo Excel ou que perde funcionalidade silenciosamente.

Trate explicitamente os tipos de origem e destino.

## 58. Workbooks não confiáveis são uma fronteira de segurança

Um `.xlsx` é um pacote ZIP contendo XML e recursos relacionados. A página do projeto openpyxl no PyPI alerta que openpyxl não protege por padrão contra ataques XML de quadratic blowup ou billion laughs e recomenda `defusedxml` como proteção.

Para exemplos confiáveis gerados pelo próprio repositório, isso não é necessário. Para serviços que aceitam workbooks arbitrários enviados por usuários, modelagem de ameaça e parsing XML endurecido fazem parte do design.

## 59. Arquivos inválidos devem falhar de forma visível

`load_workbook()` pode rejeitar arquivos OOXML malformados ou incompatíveis.

Capture exceções apenas quando puder acrescentar contexto útil e preserve a falha:

```python
from pathlib import Path
from zipfile import BadZipFile

from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException


def read_sheet_names(path: Path) -> list[str]:
    try:
        workbook = load_workbook(path, read_only=True)
    except (BadZipFile, InvalidFileException, OSError) as exc:
        raise RuntimeError(f"Could not open workbook: {path.name}") from exc

    try:
        return workbook.sheetnames
    finally:
        workbook.close()
```

Não transforme todo erro de workbook em um relatório vazio.

## 60. Prefira validar a saída em vez de aceitar apenas “save funcionou”

Um `save()` bem-sucedido prova que bytes foram gravados. Não prova que o workbook atende ao contrato de negócio ou apresentação.

Verificações úteis após salvar incluem:

```text
file exists
expected sheet names exist
required cells contain expected values or formulas
expected table names exist
expected validations exist
critical number formats/styles are present
workbook reopens successfully
```

Para templates importantes, abra o artefato gerado na aplicação de planilha de destino durante testes de aceite também.

## 61. Exemplo: crie um workbook e preserve uma fórmula

[`examples/workbook_basics.py`](examples/workbook_basics.py) cria um workbook temporário, adiciona linhas tabulares e fórmulas, salva, recarrega com fórmulas visíveis e verifica a estrutura.

Saída esperada:

```text
sheet: Summary
rows: 3
formula: =B2*C2
```

O exemplo testa aquilo que openpyxl realmente controla: texto da fórmula e estrutura do workbook, não o cálculo da fórmula.

## 62. Exemplo: faça streaming de linhas de um workbook

[`examples/load_and_iterate.py`](examples/load_and_iterate.py) grava um workbook pequeno, reabre com `read_only=True`, itera valores e calcula um total em Python.

Saída esperada:

```text
orders: 3
total: 100.00
```

Isso separa deliberadamente a leitura do workbook do cálculo de negócio.

## 63. Exemplo: crie um relatório formatado

[`examples/styled_report.py`](examples/styled_report.py) aplica tratamento reutilizável de cabeçalho, formato numérico, freeze pane e larguras de coluna, depois recarrega o workbook para verificar os metadados persistidos.

Saída esperada:

```text
header bold: True
number format: #,##0.00
freeze panes: A2
```

Um teste determinístico de workbook pode inspecionar metadados sem iniciar o Excel.

## 64. Exemplo: tabelas e regras de validação

[`examples/table_and_validation.py`](examples/table_and_validation.py) cria uma tabela do Excel e uma regra de validação por lista, salva, recarrega e verifica se ambas as estruturas existem.

Saída esperada:

```text
tables: ['CatalogTable']
validations: 1
```

Lembre que a regra de validação é armazenada, não executada, por openpyxl.

## 65. Exemplo: export write-only

[`examples/write_only_export.py`](examples/write_only_export.py) faz streaming de linhas para um workbook write-only, salva uma única vez e depois reabre o resultado em modo read-only para verificação.

Saída esperada:

```text
rows: 3
sum: 60
```

Isso modela o ciclo de vida de um export sequencial grande sem depender de um fixture enorme.

## 66. Erros comuns, guia de decisão, exercício e referências

Evite estes erros:

- usar `openpyxl` para análise tabular pesada que pertence ao `pandas`;
- esperar suporte a `.xls` ou `.xlsb` de uma biblioteca de `.xlsx`;
- supor que `data_only=True` recalcula fórmulas;
- sobrescrever um workbook de origem complexo antes de verificar a fidelidade do round-trip;
- tratar dimensões da planilha como prova de dados válidos;
- usar modo normal para cargas enormes sem considerar memória;
- esquecer de fechar workbooks read-only;
- salvar um workbook write-only mais de uma vez;
- tentar alterar estilos atribuídos in-place;
- criar milhares de variantes quase idênticas de estilo;
- confundir formatos numéricos do Excel com valores armazenados;
- supor que inserção de linhas/colunas repara fórmulas, tabelas, gráficos e nomes definidos automaticamente;
- esperar que data validation seja executada por openpyxl;
- tratar proteção de planilha como segurança;
- preservar VBA sem testar o artefato `.xlsm`;
- aceitar workbooks não confiáveis sem estratégia de segurança XML;
- considerar `save()` sozinho como verificação suficiente.

### Tabela de decisão

| Necessidade | Prefira |
|---|---|
| filtrar/agrupar/juntar dados | `pandas` |
| troca simples via CSV | `csv` ou `pandas` |
| criar/editar estrutura `.xlsx` | `openpyxl` |
| editar células arbitrárias | workbook normal |
| leitura sequencial grande | `read_only=True` |
| escrita sequencial grande | `Workbook(write_only=True)` |
| texto da fórmula | carga normal / `data_only=False` |
| valor de fórmula em cache | `data_only=True` |
| preservar container VBA | `keep_vba=True` + contrato `.xlsm` |
| formatação repetida | objetos de estilo reutilizados / `NamedStyle` |
| validação interativa no Excel | `DataValidation` |
| validação de máquina | validação Python antes da escrita |

### Referência rápida

```text
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws = wb["SheetName"]
wb.create_sheet("Details")

ws["A1"] = "value"
ws.cell(row=1, column=1, value="value")
ws.append([...])
ws.iter_rows(values_only=True)

wb.save(path)
wb = load_workbook(path)
wb = load_workbook(path, read_only=True, data_only=True)
wb.close()

ws.freeze_panes = "A2"
ws.column_dimensions["A"].width = 20
ws["B2"].number_format = "#,##0.00"

ws.merge_cells("A1:C1")
ws.unmerge_cells("A1:C1")

ws.add_table(...)
ws.add_data_validation(...)
```

### Checklist de design

Antes de aceitar uma automação de workbook, pergunte:

- Quais formatos de workbook são permitidos?
- O arquivo é confiável ou enviado por usuário?
- Recursos não suportados precisam sobreviver ao round-trip?
- A origem pode ser sobrescrita?
- Quais planilhas, células, tabelas e nomes formam o contrato?
- Fórmulas precisam do texto ou do valor calculado?
- Quem é responsável pelo cálculo?
- Valores de fórmula em cache são recentes o suficiente?
- Modo normal, read-only ou write-only é apropriado?
- Recursos do workbook são fechados?
- Estilos são reutilizados de forma intencional?
- Formatos numéricos estão separados dos valores armazenados?
- Edições estruturais podem quebrar referências?
- Regras de validação são apenas UI ou validação real de negócio?
- VBA precisa ser preservado?
- A saída reabre com sucesso?
- Estruturas críticas são verificadas após salvar?

### Exercício

Construa um workbook fictício de operações mensais:

1. Crie um `.xlsx` com planilhas `Summary` e `Transactions`.
2. Adicione uma linha de cabeçalho e pelo menos dez transações fictícias.
3. Use valores Python `date` ou `datetime` explícitos para datas.
4. Adicione uma fórmula do Excel à planilha de resumo.
5. Explique por que seu teste deve verificar o texto da fórmula em vez de esperar que openpyxl a calcule.
6. Formate células monetárias com number format.
7. Reutilize um estilo de cabeçalho em vez de criar formatação desconectada por célula.
8. Congele a linha de cabeçalho das transações.
9. Crie uma tabela do Excel sobre os dados.
10. Adicione uma validação por lista à coluna de status.
11. Salve em um novo caminho.
12. Reabra e verifique nomes de planilhas, texto da fórmula, nome da tabela, quantidade de validações e um estilo crítico.
13. Adicione uma função read-only que calcule um total Python das linhas salvas.
14. Faça falhas aparecerem com contexto útil.

Desafios extras:

- crie um gráfico a partir dos valores do resumo;
- adicione um nome definido e inspecione-o após recarregar;
- compare designs de export normal e write-only;
- processe um `DataFrame` do pandas e use openpyxl somente para a camada de apresentação;
- projete um teste seguro de round-trip `.xlsm` com `keep_vba=True` sem tentar editar o projeto VBA.

### Conexões com conceitos anteriores

`openpyxl` se apoia diretamente no conteúdo anterior:

- **funções e módulos:** isole etapas de geração e validação;
- **exceções:** reporte entradas malformadas ou incompatíveis;
- **`pathlib`:** modele caminhos de origem e destino;
- **datas:** armazene valores temporais Python com formatos de planilha;
- **`decimal`:** decida explicitamente como valores monetários exatos atravessam a fronteira para células numéricas do Excel;
- **`logging`:** registre caminhos, nomes de planilha, contagens e falhas sem esconder exceções;
- **`os` e `shutil`:** descubra, prepare, copie e arquive workbooks com segurança;
- **`pandas`:** transforme dados tabulares antes de openpyxl montar a apresentação final do Excel.

### Referências primárias

- [documentação do openpyxl](https://openpyxl.readthedocs.io/)
- [tutorial do openpyxl](https://openpyxl.readthedocs.io/en/stable/tutorial.html)
- [Optimised Modes](https://openpyxl.readthedocs.io/en/stable/optimized.html)
- [Working with styles](https://openpyxl.readthedocs.io/en/stable/styles.html)
- [Worksheet tables](https://openpyxl.readthedocs.io/en/stable/worksheet_tables.html)
- [Data validation](https://openpyxl.readthedocs.io/en/stable/validation.html)
- [Worksheet editing](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html)
- [openpyxl no PyPI](https://pypi.org/project/openpyxl/)

No momento em que este capítulo foi preparado, o PyPI listava openpyxl 3.1.5 como release estável mais recente. O currículo mira a série 3.1.x em vez de depender de uma versão futura sem limite.

## 67. Próximo capítulo

A Fase 9 agora possui duas camadas práticas de dados/workbook:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
```

Continue com **[`requests`: Consumindo APIs HTTP](../03-requests/README.pt-BR.md)**, quando a fronteira deixa arquivos locais e passa para serviços HTTP e APIs.

Antes de avançar, pratique gerando workbooks que possam ser inspecionados manualmente e validados automaticamente. Automação de planilhas fica confiável quando tanto o contrato de dados quanto o contrato do workbook são explícitos.
