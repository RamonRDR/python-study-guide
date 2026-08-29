<div align="center">

# Trabalhando com Dados Tabulares Usando `pandas`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Bibliotecas Externas](../README.pt-BR.md) · [← Fase anterior: `os` + `shutil`](../../standard-library/09-os-shutil/README.pt-BR.md)

A Fase 9 começa onde a biblioteca padrão termina: adicionando pacotes de terceiros com seus próprios ciclos de release, contratos de dependência e abstrações específicas de domínio.

`pandas` é a primeira biblioteca externa porque se conecta diretamente a conceitos já estudados: listas, dicionários, CSV, JSON, datas, arquivos, funções, exceções, caminhos e validação de dados. O novo desafio não é apenas aprender métodos. É aprender a preservar a **semântica da tabela** enquanto as transformações se tornam mais expressivas.

Este capítulo tem como alvo **pandas 3.0.x** e foi pesquisado com base na documentação oficial do pandas **3.0.5**. pandas 3.0 suporta Python 3.11 ou superior.

**Tempo estimado de estudo:** 240–330 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar quando pandas é mais adequado do que coleções embutidas;
- criar e inspecionar objetos `Series` e `DataFrame`;
- raciocinar sobre índices, labels, alinhamento, colunas e dtypes;
- selecionar linhas e colunas com colchetes, `.loc` e `.iloc`;
- construir máscaras booleanas e atualizar linhas com segurança;
- entender Copy-on-Write no pandas 3.0 e por que chained assignment não é válido;
- tratar valores ausentes com uma política explícita;
- converter colunas numéricas, textuais e de data/hora de forma deliberada;
- agregar com `groupby()`, `agg()` e `transform()`;
- combinar tabelas com `merge()` validado e `concat()`;
- remodelar dados com `pivot_table()` e `melt()`;
- carregar e salvar CSV com decisões explícitas de schema;
- preferir operações vetorizadas quando elas expressam o problema;
- reconhecer quando `apply()` e iteração por linhas não são bons padrões iniciais;
- construir pipelines de dados tabulares determinísticos e revisáveis.

## 1. Por que `pandas` existe

`pandas` é uma biblioteca de terceiros para dados rotulados e tabulares. Ela é especialmente útil quando os dados possuem linhas, colunas, rótulos, valores ausentes, tipos diferentes por coluna ou precisam de filtros, agrupamentos, joins, reshape e entrada/saída por arquivos.

Ela não substitui as coleções do Python. Uma lista ou um dicionário frequentemente é melhor para pequenos estados de uma aplicação. `pandas` ganha força quando o problema é principalmente uma tabela de dados e as operações se aplicam a colunas ou grupos de linhas.

## 2. Bibliotecas externas introduzem contratos de dependência

Ao contrário da biblioteca padrão, pandas precisa ser instalado no ambiente Python que executará o código. O repositório declara as dependências executáveis da Fase 9 em `requirements-external.txt`.

Um contrato de dependência responde perguntas como:

```text
Qual pacote é necessário?
Quais versões são suportadas pelo capítulo?
Quais versões do Python são suportadas pelo pacote?
Como o CI reproduz o mesmo ambiente?
Quais comportamentos mudaram entre versões principais?
```

Este capítulo mira deliberadamente pandas 3.0.x em vez de fingir que todas as versões históricas se comportam da mesma forma.

## 3. Instale pandas em um ambiente isolado

Um ambiente virtual mantém as dependências do projeto separadas de outras instalações Python.

```bash
python -m venv .venv
```

Ative-o conforme seu sistema operacional e instale o contrato de dependências do repositório:

```bash
python -m pip install -r requirements-external.txt
```

A documentação oficial também mostra instalação direta com `pip install pandas` e via conda-forge. Aqui, um arquivo de dependências é preferível porque torna o contrato executável do guia reproduzível.

## 4. Importe pandas com o alias convencional

A documentação e a comunidade pandas usam `pd`:

```python
import pandas as pd
```

Seguir essa convenção facilita comparar os exemplos com a documentação oficial e outros projetos.

## 5. `Series` modela uma dimensão rotulada

Uma `Series` é uma estrutura unidimensional rotulada. Ela combina valores com um índice. Uma coluna de um DataFrame normalmente é exposta como uma `Series`.

```python
import pandas as pd


scores = pd.Series([8.5, 9.0, 7.5], index=["A", "B", "C"])
print(scores.loc["B"])
```

```text
9.0
```

Uma `Series` não é apenas uma lista com mais métodos. Os rótulos participam de seleção e alinhamento.

## 6. `DataFrame` modela uma tabela rotulada

Um `DataFrame` é uma tabela bidimensional com linhas e colunas rotuladas. Colunas diferentes podem ter dtypes diferentes, o que o torna adequado para muitos conjuntos semelhantes a planilhas, SQL e CSV.

```python
import pandas as pd


people = pd.DataFrame(
    {
        "name": ["Ana", "Bruno"],
        "age": [28, 34],
        "active": [True, False],
    }
)
print(people.shape)
```

```text
(2, 3)
```

Um dicionário de sequências com o mesmo tamanho é um dos construtores mais claros para exemplos pequenos. As chaves se tornam nomes de colunas.

## 7. O índice faz parte do modelo de dados

O índice rotula as linhas. O `RangeIndex` padrão é perfeitamente adequado em muitos casos. Use um índice personalizado significativo apenas quando os rótulos das linhas realmente participarem da seleção, alinhamento ou identidade.

```python
import pandas as pd


temperatures = pd.Series([21.5, 19.0], index=["morning", "evening"])
print(temperatures.index.tolist())
```

```text
['morning', 'evening']
```

Não transforme automaticamente todo identificador de negócio em índice. Uma coluna normal costuma ser mais fácil de validar, combinar, exportar e explicar.

## 8. O alinhamento por rótulos é poderoso e pode surpreender

Quando pandas combina objetos rotulados, ele normalmente alinha valores pelos rótulos do índice em vez de usar cegamente a posição física.

```python
import pandas as pd


left = pd.Series([10, 20], index=["a", "b"])
right = pd.Series([1, 2], index=["b", "c"])
print((left + right).to_dict())
```

O rótulo compartilhado `b` recebe valores dos dois objetos. Rótulos presentes em apenas um dos lados se tornam ausentes no resultado.

Trate o índice como dado, não decoração. Rótulos inesperados podem alterar aritmética, joins, atribuições e comparações.

## 9. Inspecione colunas e dtypes cedo

Um fluxo confiável inspeciona o que foi carregado antes de transformar. `columns` revela os rótulos e `dtypes` mostra o dtype escolhido para cada coluna.

```python
import pandas as pd


table = pd.DataFrame({"label": ["x", "y"], "count": [1, 2]})
print(table.columns.tolist())
print(table.dtypes.astype(str).to_dict())
```

pandas 3.0 mudou um padrão importante: colunas contendo somente strings são inferidas com o dtype dedicado `str`, em vez do antigo dtype genérico `object`.

Esse é um dos motivos para este capítulo declarar explicitamente sua versão de pandas.

## 10. `shape`, `size` e `ndim` respondem perguntas diferentes

```python
import pandas as pd


table = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(table.shape, table.size, table.ndim)
```

```text
(3, 2) 6 2
```

- `shape` retorna `(linhas, colunas)`;
- `size` retorna a quantidade de células;
- `ndim` retorna o número de dimensões.

São fatos estruturais, não validações por si só.

## 11. Visualizar dados ajuda, mas não valida

`head()` e `tail()` são ferramentas rápidas de inspeção. `sample()` pode mostrar padrões fora das primeiras linhas, mas use `random_state` quando a reprodução do resultado for importante.

```python
import pandas as pd


table = pd.DataFrame({"value": [10, 20, 30, 40]})
print(table.sample(2, random_state=7)["value"].tolist())
```

Uma visualização não prova que colunas obrigatórias existem, dtypes estão corretos, identificadores são únicos ou valores estão dentro de intervalos permitidos.

## 12. `info()` e `describe()` respondem perguntas de inspeção diferentes

`DataFrame.info()` resume quantidade de linhas, nomes de colunas, contagem de não nulos, dtypes e uso aproximado de memória. É útil para inspeção humana.

`describe()` resume estatísticas como contagem, média, dispersão e extremos para colunas apropriadas.

```python
import pandas as pd


values = pd.DataFrame({"amount": [10.0, 20.0, 30.0]})
print(values["amount"].describe()[["count", "mean", "max"]].to_dict())
```

Nenhuma dessas funções entende o significado de negócio. Um valor negativo pode ser matematicamente válido e inválido para um conjunto específico. Um identificador pode parecer numérico e ainda não fazer sentido calcular sua média.

## 13. Selecione uma coluna com colchetes

`df["column"]` retorna uma `Series`.

```python
import pandas as pd


table = pd.DataFrame({"unit price": [10.0, 12.5]})
prices = table["unit price"]
print(type(prices).__name__)
```

```text
Series
```

Prefira colchetes a acesso por atributo como `df.column`. Nomes podem conter espaços, conflitar com atributos do DataFrame ou ser escolhidos dinamicamente.

## 14. Selecione múltiplas colunas com uma lista

Passar uma lista de nomes de colunas retorna um DataFrame e preserva a ordem solicitada.

```python
import pandas as pd


table = pd.DataFrame({"a": [1], "b": [2], "c": [3]})
subset = table[["c", "a"]]
print(subset.columns.tolist())
```

```text
['c', 'a']
```

A distinção importa: uma string seleciona uma coluna como `Series`; uma lista de strings seleciona uma tabela como `DataFrame`.

## 15. Use `.loc` para seleção baseada em rótulos

`.loc` seleciona por labels e condições booleanas.

```python
import pandas as pd


table = pd.DataFrame({"status": ["new", "done"], "value": [5, 8]}, index=["a", "b"])
print(table.loc["b", "value"])
```

```text
8
```

`.loc` também é a ferramenta preferida para atribuição condicional porque linhas-alvo e coluna de destino podem ser expressas numa única operação.

## 16. Use `.iloc` para seleção posicional

`.iloc` seleciona por posição inteira, independentemente dos labels do índice.

```python
import pandas as pd


table = pd.DataFrame({"name": ["first", "second", "third"]}, index=[10, 20, 30])
print(table.iloc[1, 0])
```

```text
second
```

Use `.iloc` quando a posição for parte do significado. Não use apenas porque a seleção por labels parece menos familiar.

## 17. Slices por label e por posição têm limites diferentes

Com `.loc`, um slice por label inclui o label final quando ele existe. Com `.iloc`, o fatiamento segue o Python posicional normal e exclui a posição final.

```python
import pandas as pd


table = pd.DataFrame({"value": [10, 20, 30]}, index=["a", "b", "c"])
print(table.loc["a":"b", "value"].tolist())
print(table.iloc[0:2, 0].tolist())
```

```text
[10, 20]
[10, 20]
```

Os exemplos retornam os mesmos valores por motivos diferentes. Mantenha os dois modelos mentais separados.

## 18. Máscaras booleanas filtram linhas

Uma comparação contra uma `Series` produz uma `Series` booleana. Usar essa máscara com `.loc` mantém as linhas em que a condição é verdadeira.

```python
import pandas as pd


orders = pd.DataFrame({"amount": [50, 120, 80]})
mask = orders["amount"] >= 80
print(orders.loc[mask, "amount"].tolist())
```

```text
[120, 80]
```

Máscaras são uma das pontes mais importantes entre lógica booleana do Python e operações orientadas a tabelas.

## 19. Combine máscaras com `&`, `|` e `~`

Use operadores booleanos elemento a elemento para condições de `Series` e coloque cada comparação entre parênteses.

```python
import pandas as pd


orders = pd.DataFrame(
    {"status": ["paid", "paid", "pending"], "amount": [50, 150, 200]}
)
mask = (orders["status"] == "paid") & (orders["amount"] >= 100)
print(orders.loc[mask, "amount"].tolist())
```

```text
[150]
```

Os operadores escalares `and` e `or` do Python não expressam lógica linha a linha para uma `Series` pandas.

## 20. Faça atribuição no objeto que pretende alterar

Ao atualizar um DataFrame, expresse o seletor de linhas e a coluna de destino em uma única operação `.loc`.

```python
import pandas as pd


orders = pd.DataFrame({"amount": [50, 150], "priority": ["normal", "normal"]})
orders.loc[orders["amount"] >= 100, "priority"] = "high"
print(orders["priority"].tolist())
```

```text
['normal', 'high']
```

Esse padrão é explícito e compatível com a semântica Copy-on-Write do pandas 3.0.

## 21. Copy-on-Write é a regra no pandas 3.0

No pandas 3.0, objetos derivados por indexação ou métodos se comportam como cópias do ponto de vista do usuário. Alterar um objeto derivado não altera o objeto original.

```python
import pandas as pd


original = pd.DataFrame({"value": [1, 2, 3]})
subset = original["value"]
subset.iloc[0] = 99

print(original["value"].tolist())
print(subset.tolist())
```

```text
[1, 2, 3]
[99, 2, 3]
```

Internamente, pandas pode compartilhar memória até que uma escrita exija uma cópia. Para o código de aplicação, o contrato importante é o comportamento observável.

## 22. Chained assignment não é uma estratégia válida de atualização

Código como este usa múltiplas etapas de indexação:

```text
df["value"][mask] = 10
```

No pandas 3.0, chained assignment não atualiza o DataFrame original. A antiga ambiguidade que gerava `SettingWithCopyWarning` foi substituída por uma regra mais simples: modifique o próprio objeto em uma operação.

```python
import pandas as pd


table = pd.DataFrame({"value": [1, 2, 3]})
table.loc[table["value"] >= 2, "value"] = 10
print(table["value"].tolist())
```

```text
[1, 10, 10]
```

Esse é um ponto importante ao encontrar materiais antigos de pandas 1.x ou 2.x na internet.

## 23. Crie colunas derivadas com expressões vetorizadas

Expressões de coluna operam sobre objetos `Series` inteiros e normalmente são mais claras do que escrever um loop Python para cada linha.

```python
import pandas as pd


sales = pd.DataFrame({"units": [2, 3], "unit_price": [10.0, 12.5]})
sales["total"] = sales["units"] * sales["unit_price"]
print(sales["total"].tolist())
```

```text
[20.0, 37.5]
```

Esse é um hábito central do pandas: expresse a transformação em termos de colunas quando a própria regra é orientada a colunas.

## 24. `assign()` é útil em method chains

`assign()` retorna um DataFrame com colunas adicionadas ou substituídas.

```python
import pandas as pd


sales = pd.DataFrame({"units": [2, 3], "price": [5.0, 8.0]})
result = sales.assign(total=lambda frame: frame["units"] * frame["price"])
print(result["total"].tolist())
```

```text
[10.0, 24.0]
```

Use quando um pipeline fica mais legível mantendo as transformações encadeadas. A atribuição direta continua válida quando é mais clara.

## 25. Renomeie, remova e ordene com intenção

`rename()` pode normalizar nomes externos ruins. `drop()` remove linhas ou colunas. `sort_values()` e `sort_index()` tornam a ordem explícita.

```python
import pandas as pd


table = pd.DataFrame({"Order Amount": [20, 10], "temporary_note": ["b", "a"]})
clean = (
    table.rename(columns={"Order Amount": "amount"})
    .drop(columns=["temporary_note"])
    .sort_values("amount")
)
print(clean["amount"].tolist())
```

```text
[10, 20]
```

Um campo removido pode ser impossível de reconstruir depois. Uma ordenação pode ser necessária para relatórios determinísticos. Essas operações codificam política, não apenas aparência.

## 26. Dados ausentes precisam de uma política explícita

Valores ausentes podem significar desconhecido, não aplicável, não coletado, inválido, atrasado ou intencionalmente vazio. Esses significados não são equivalentes.

Antes de chamar `dropna()` ou `fillna()`, decida o significado da ausência para cada coluna relevante.

```python
import pandas as pd


table = pd.DataFrame({"value": [1.0, None, 3.0], "label": ["a", "b", None]})
print(table.isna().sum().to_dict())
```

```text
{'value': 1, 'label': 1}
```

Contar ausências é observação. Removê-las ou preenchê-las é uma transformação que exige regra.

## 27. `dropna()` descarta observações

`dropna()` só é correto quando as observações afetadas são realmente descartáveis segundo o contrato de dados.

```python
import pandas as pd


table = pd.DataFrame({"id": [1, 2, 3], "amount": [10.0, None, 30.0]})
complete = table.dropna(subset=["amount"])
print(complete["id"].tolist())
```

```text
[1, 3]
```

Usar `dropna()` sem `subset` pode remover linhas por causa de campos irrelevantes para a operação atual.

## 28. `fillna()` insere um significado escolhido

Substituir um valor desconhecido por zero afirma que zero é a interpretação correta.

```python
import pandas as pd


table = pd.DataFrame({"discount": [0.1, None, 0.2]})
filled = table["discount"].fillna(0.0)
print(filled.tolist())
```

```text
[0.1, 0.0, 0.2]
```

Documente regras de preenchimento porque elas alteram o conjunto de dados, não apenas sua aparência.

## 29. Dtypes fazem parte do schema

Uma coluna que parece numérica pode ter sido carregada como texto. Uma data pode continuar sendo string. Um identificador pode precisar permanecer textual mesmo quando todos os valores possuem apenas dígitos.

Use `astype()` quando os valores já forem válidos para o dtype de destino:

```python
import pandas as pd


table = pd.DataFrame({"units": ["1", "2", "3"]})
table["units"] = table["units"].astype("int64")
print(table["units"].sum())
```

```text
6
```

Escolha tipos de acordo com significado e operações, não apenas aparência.

## 30. `to_numeric()` torna a política de parsing explícita

`pd.to_numeric()` é útil quando a conversão numérica pode falhar.

```python
import pandas as pd


raw = pd.Series(["10", "invalid", "30"])
parsed = pd.to_numeric(raw, errors="coerce")
print(parsed.isna().sum())
```

```text
1
```

`errors="coerce"` transforma entradas inválidas em valores ausentes. Isso só é seguro quando o fluxo depois audita e trata essas novas ausências.

## 31. Operações de string são vetorizadas sob `.str`

O accessor `.str` aplica operações de string a uma `Series`.

```python
import pandas as pd


names = pd.Series(["  Alpha ", "BETA  "])
normalized = names.str.strip().str.lower()
print(normalized.tolist())
```

```text
['alpha', 'beta']
```

Normalize texto apenas quando a normalização corresponder ao contrato do domínio. Colocar identificadores em minúsculas ou remover espaços pode mudar significado.

## 32. Converta datetimes antes de usar semântica de data/hora

Use `pd.to_datetime()` quando texto deve se tornar realmente data/hora.

```python
import pandas as pd


dates = pd.to_datetime(pd.Series(["2026-08-01", "2026-08-03"]), format="%Y-%m-%d")
print((dates.iloc[1] - dates.iloc[0]).days)
```

```text
2
```

O accessor `.dt` então expõe componentes vetorizados:

```python
import pandas as pd


dates = pd.to_datetime(pd.Series(["2026-01-15", "2026-02-20"]))
print(dates.dt.month.tolist())
```

```text
[1, 2]
```

Formatos ambíguos de data devem ser controlados explicitamente em vez de adivinhados.

## 33. Duplicatas precisam de uma definição

Duas linhas são duplicadas apenas em relação às colunas escolhidas. `duplicated()` e `drop_duplicates()` aceitam `subset` para expressar a chave real de unicidade.

```python
import pandas as pd


table = pd.DataFrame(
    {"id": [1, 1, 2], "note": ["first", "repeated", "other"]}
)
print(table.duplicated(subset=["id"]).tolist())
```

```text
[False, True, False]
```

Não deduplique linhas inteiras quando a regra verdadeira é unicidade por identificador.

## 34. Métodos de frequência e resumo são diagnósticos compactos

`value_counts()` mostra frequência de categorias. `nunique()` conta valores distintos não ausentes por padrão. Reduções como `sum()`, `mean()`, `min()`, `max()` e `count()` resumem colunas.

```python
import pandas as pd


statuses = pd.Series(["paid", "pending", "paid", "paid"])
print(statuses.value_counts().sort_index().to_dict())
```

```text
{'paid': 3, 'pending': 1}
```

Uma frequência é evidência sobre os dados observados, não prova de que toda categoria observada é permitida.

## 35. `groupby()` implementa split-apply-combine

`groupby()` separa linhas por uma ou mais chaves, aplica agregação ou transformação e combina os resultados.

```python
import pandas as pd


sales = pd.DataFrame(
    {"category": ["A", "B", "A"], "amount": [10, 20, 30]}
)
summary = sales.groupby("category")["amount"].sum()
print(summary.to_dict())
```

```text
{'A': 40, 'B': 20}
```

Agrupamento é central no pandas porque muitas perguntas analíticas são "calcule algo por categoria, cliente, data, região ou outra chave".

## 36. Agregação nomeada torna o schema de saída explícito

Named aggregation permite declarar tanto a coluna de origem quanto a operação.

```python
import pandas as pd


sales = pd.DataFrame(
    {"category": ["A", "A", "B"], "amount": [10.0, 30.0, 20.0]}
)
summary = sales.groupby("category", as_index=False).agg(
    total=("amount", "sum"),
    average=("amount", "mean"),
)
print(summary.to_dict(orient="records"))
```

```text
[{'category': 'A', 'total': 40.0, 'average': 20.0}, {'category': 'B', 'total': 20.0, 'average': 20.0}]
```

Um schema de saída estável facilita validação, exportação e testes posteriores.

## 37. `transform()` mantém resultados alinhados às linhas originais

Ao contrário de uma agregação normal, `transform()` retorna resultado alinhado ao índice original.

```python
import pandas as pd


sales = pd.DataFrame({"team": ["A", "A", "B"], "score": [10, 20, 30]})
sales["team_total"] = sales.groupby("team")["score"].transform("sum")
print(sales["team_total"].tolist())
```

```text
[30, 30, 30]
```

É útil quando uma estatística de grupo precisa permanecer ao lado de cada observação.

## 38. `merge()` combina tabelas por chaves

`merge()` é a operação de join estilo banco de dados do pandas.

```python
import pandas as pd


orders = pd.DataFrame({"customer_id": [1, 2], "amount": [10, 20]})
customers = pd.DataFrame({"customer_id": [1, 2], "name": ["A", "B"]})
result = orders.merge(customers, on="customer_id", how="left")
print(result["name"].tolist())
```

```text
['A', 'B']
```

Um merge que executa sem erro ainda pode estar logicamente errado se as chaves tiverem duplicatas inesperadas.

## 39. Valide a cardinalidade do merge

O argumento `validate` pode afirmar relações como `one_to_one`, `one_to_many`, `many_to_one` ou `many_to_many`.

```python
import pandas as pd


orders = pd.DataFrame({"customer_id": [1, 1], "amount": [10, 20]})
customers = pd.DataFrame({"customer_id": [1], "name": ["A"]})
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one",
)
print(len(result))
```

```text
2
```

Quando a cardinalidade faz parte do contrato, validá-la transforma duplicação acidental de chaves em falha visível, em vez de multiplicação silenciosa de linhas.

## 40. `concat()` empilha objetos compatíveis

`pd.concat()` combina objetos pandas ao longo de um eixo. Concatenar linhas é comum quando vários arquivos têm o mesmo schema.

```python
import pandas as pd


first = pd.DataFrame({"id": [1, 2]})
second = pd.DataFrame({"id": [3]})
combined = pd.concat([first, second], ignore_index=True)
print(combined["id"].tolist())
```

```text
[1, 2, 3]
```

Depois da concatenação, decida se os labels de índice originais devem ser preservados ou redefinidos.

## 41. `pivot_table()` resume em uma matriz

Uma pivot table agrupa dados por dimensões de linha e coluna e agrega valores.

```python
import pandas as pd


sales = pd.DataFrame(
    {
        "region": ["north", "north", "south"],
        "product": ["A", "B", "A"],
        "amount": [10, 20, 30],
    }
)
pivot = sales.pivot_table(
    index="region",
    columns="product",
    values="amount",
    aggfunc="sum",
    fill_value=0,
)
print(pivot.loc["north", "B"])
```

```text
20
```

Use pivot table quando a saída desejada for ela própria uma matriz de resumo.

## 42. `melt()` converte dados wide para long

Dados em formato long frequentemente facilitam agrupamento e visualização.

```python
import pandas as pd


wide = pd.DataFrame({"item": ["A"], "jan": [10], "feb": [20]})
long = wide.melt(id_vars="item", var_name="month", value_name="amount")
print(long.to_dict(orient="records"))
```

```text
[{'item': 'A', 'month': 'jan', 'amount': 10}, {'item': 'A', 'month': 'feb', 'amount': 20}]
```

`melt()` é especialmente útil quando colunas repetidas representam, na verdade, valores de uma mesma variável conceitual.

## 43. `read_csv()` transforma texto delimitado em DataFrame

`pd.read_csv()` é uma das funções de I/O mais importantes do pandas.

```python
from io import StringIO

import pandas as pd


source = StringIO("id,amount\n1,10.5\n2,20.0\n")
table = pd.read_csv(source)
print(table.shape)
```

```text
(2, 2)
```

pandas infere um schema a menos que você forneça instruções mais fortes. Inferência é conveniência, não contrato de negócio.

## 44. Controle o parsing de CSV quando o schema é conhecido

Argumentos úteis de `read_csv()` incluem `usecols`, `dtype`, `parse_dates`, `na_values`, `encoding` e configurações de delimitador.

```python
from io import StringIO

import pandas as pd


source = StringIO("code,date,amount\n001,2026-08-01,10.5\n")
table = pd.read_csv(
    source,
    dtype={"code": "str"},
    parse_dates=["date"],
)
print(table.loc[0, "code"])
print(table.loc[0, "date"].year)
```

```text
001
2026
```

Fornecer informações conhecidas de schema reduz inferências acidentais e documenta expectativas perto da fronteira de entrada.

## 45. Identificadores frequentemente pertencem ao dtype string

Um código como `00123` pode parecer numérico, mas não ter significado aritmético. Convertê-lo para inteiro destrói zeros à esquerda.

```python
import pandas as pd


codes = pd.Series(["001", "010"], dtype="str")
print(codes.tolist())
```

```text
['001', '010']
```

Modele identificadores segundo sua semântica, não pelos caracteres que contêm.

## 46. `to_csv()` deve tornar a política do índice explícita

Para tabelas comuns cujo índice é apenas um label interno de linha, `index=False` evita que uma coluna extra apareça ao reimportar.

```python
from io import StringIO

import pandas as pd


table = pd.DataFrame({"id": [1], "value": [10]})
buffer = StringIO()
table.to_csv(buffer, index=False)
print(buffer.getvalue().strip())
```

```text
id,value
1,10
```

Se o índice carrega informação real, exporte-o intencionalmente em vez de sempre desativá-lo.

## 47. Method chains tornam a ordem das transformações visível

Uma cadeia curta pode ser lida como pipeline: filtrar, derivar, ordenar, agrupar, exportar.

```python
import pandas as pd


orders = pd.DataFrame(
    {"status": ["paid", "pending", "paid"], "amount": [30, 50, 20]}
)
result = (
    orders.loc[orders["status"] == "paid"]
    .assign(taxed=lambda frame: frame["amount"] * 1.1)
    .sort_values("amount")
)
print(result["amount"].tolist())
```

```text
[20, 30]
```

Cadeias longas podem ficar difíceis de depurar. Divida em etapas nomeadas quando a intenção deixar de ser óbvia.

## 48. Prefira operações vetorizadas a loops Python por linha

Quando um cálculo puder ser expresso com aritmética de `Series`, comparações, `.str`, `.dt` ou reduções nativas, prefira essa forma.

```python
import pandas as pd


table = pd.DataFrame({"quantity": [2, 3], "price": [4.0, 5.0]})
table["total"] = table["quantity"] * table["price"]
print(table["total"].tolist())
```

```text
[8.0, 15.0]
```

Vetorização comunica a intenção tabular e normalmente permite que pandas/NumPy executem o trabalho com mais eficiência do que chamadas Python repetidas.

## 49. `apply()` não é automaticamente vetorização

`Series.apply()` e `DataFrame.apply()` por linha podem ser úteis para lógica Python customizada, mas podem executar uma função Python repetidamente.

Antes de usar `apply()`, verifique se pandas já fornece uma operação nativa para a transformação.

Use `apply()` porque a lógica customizada é realmente necessária, não apenas porque parece menor que um loop.

## 50. Evite `iterrows()` para transformações comuns

Iteração por linha às vezes é necessária em fronteiras com efeitos externos, mas filtros, cálculos, agregações e atribuições normalmente têm formas melhores orientadas a colunas.

Uma linha retornada por `iterrows()` é uma representação `Series`. Não a trate como um handle mutável para atualizar o DataFrame original.

## 51. `.copy()` ainda tem papel deliberado

Copy-on-Write significa que cópias defensivas não são mais necessárias apenas para silenciar o antigo `SettingWithCopyWarning`.

Use `.copy()` quando uma cópia independente e imediata fizer parte do design ou contrato de ciclo de vida.

```python
import pandas as pd


original = pd.DataFrame({"value": [1, 2]})
independent = original.copy()
independent.loc[0, "value"] = 99
print(original["value"].tolist())
```

```text
[1, 2]
```

## 52. Erros do DataFrame devem permanecer visíveis

Falhas comuns incluem:

```text
KeyError
ValueError
pandas.errors.ParserError
pandas.errors.MergeError
```

Não capture exceções amplas apenas para manter um pipeline em movimento. Uma tabela parcialmente transformada pode ser mais perigosa do que uma falha visível.

Falhas de validação devem interromper o fluxo quando continuar tornaria a saída não confiável.

## 53. Exemplo prático: construir uma pequena tabela de vendas

```python
import pandas as pd


data = {
    "product": ["Notebook", "Keyboard", "Mouse"],
    "units": [2, 5, 8],
    "unit_price": [3500.0, 180.0, 95.0],
}

sales = pd.DataFrame(data)
sales["total"] = sales["units"] * sales["unit_price"]

print(f"shape: {sales.shape}")
print(f"columns: {sales.columns.tolist()}")
print(f"grand total: {sales['total'].sum():.2f}")
```

```text
shape: (3, 4)
columns: ['product', 'units', 'unit_price', 'total']
grand total: 8660.00
```

Este exemplo espelha `examples/dataframe_basics.py` e demonstra construção, inspeção, coluna derivada e agregação.

## 54. Exemplo prático: filtrar e atribuir com segurança

```python
import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [101, 102, 103, 104],
        "status": ["paid", "pending", "paid", "paid"],
        "amount": [120.0, 80.0, 250.0, 90.0],
    }
)

orders["priority"] = "normal"
orders.loc[
    (orders["status"] == "paid") & (orders["amount"] >= 200),
    "priority",
] = "high"

selected = orders.loc[
    orders["status"] == "paid",
    ["order_id", "priority"],
]
print(selected.to_dict(orient="records"))
```

```text
[{'order_id': 101, 'priority': 'normal'}, {'order_id': 103, 'priority': 'high'}, {'order_id': 104, 'priority': 'normal'}]
```

A atualização acontece diretamente em `orders` por `.loc`, o padrão seguro para pandas 3.0.

## 55. Exemplo prático: resumo agrupado

```python
import pandas as pd


transactions = pd.DataFrame(
    {
        "category": ["books", "games", "books", "games", "office"],
        "amount": [40.0, 120.0, 35.0, 80.0, 25.0],
    }
)

summary = (
    transactions.groupby("category", as_index=False)
    .agg(
        total_amount=("amount", "sum"),
        transaction_count=("amount", "size"),
    )
    .sort_values("category")
)

print(summary.to_dict(orient="records"))
```

As colunas nomeadas de saída formam um schema estável. O sort final torna o exemplo determinístico.

## 56. Exemplo prático: merge validado

```python
import pandas as pd


orders = pd.DataFrame(
    {
        "order_id": [1, 2, 3],
        "customer_id": [10, 20, 10],
        "amount": [50.0, 80.0, 30.0],
    }
)
customers = pd.DataFrame(
    {
        "customer_id": [10, 20],
        "customer": ["Aster", "Boreal"],
    }
)

report = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one",
)
report = report[["order_id", "customer", "amount"]].sort_values("order_id")

print(report.to_dict(orient="records"))
```

`validate="many_to_one"` documenta que muitos pedidos podem apontar para um cliente, enquanto a tabela de clientes deve manter chaves únicas.

## 57. Exemplo prático: pipeline CSV determinístico

```python
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source = workspace / "orders.csv"
    destination = workspace / "paid_orders.csv"

    source.write_text(
        "order_id,date,status,amount\n"
        "1,2026-08-01,paid,120.50\n"
        "2,2026-08-02,pending,80.00\n"
        "3,2026-08-03,paid,250.00\n",
        encoding="utf-8",
    )

    orders = pd.read_csv(source, parse_dates=["date"])
    paid_orders = orders.loc[orders["status"] == "paid"].sort_values("order_id")
    paid_orders.to_csv(destination, index=False)

    print(f"rows: {len(paid_orders)}")
    print(f"total: {paid_orders['amount'].sum():.2f}")
    print(f"saved: {destination.name}")
```

```text
rows: 2
total: 370.50
saved: paid_orders.csv
```

O diretório temporário mantém o exemplo seguro, `parse_dates` estabelece semântica de datetime na entrada, o sort estabiliza o resultado e `index=False` mantém o schema do CSV deliberado.

## 58. Erros comuns

Evite estes padrões:

- tratar pandas como substituto para toda lista ou dicionário;
- confiar em dtypes inferidos sem inspeção;
- converter identificadores para números só porque contêm dígitos;
- usar chained assignment em vez de uma atualização `.loc` única;
- chamar `dropna()` ou `fillna()` sem definir o significado de ausência;
- juntar tabelas sem verificar unicidade ou cardinalidade das chaves;
- depender de ordem incidental das linhas;
- usar `iterrows()` para cálculos que possuem formas vetorizadas;
- usar `apply()` antes de verificar operações nativas do pandas;
- exportar um índice interno sem querer;
- esconder erros de parsing ou merge e continuar com dados parciais;
- copiar conselhos de pandas 1.x/2.x sem verificar o comportamento do pandas 3.0.

## 59. Tabela de decisão

| Necessidade | Prefira |
|---|---|
| uma coluna rotulada | `Series` |
| tabela rotulada | `DataFrame` |
| seleção por label | `.loc` |
| seleção por posição | `.iloc` |
| filtro condicional de linhas | máscara booleana + `.loc` |
| atualização condicional | uma atribuição `.loc[...] = ...` |
| converter texto numérico | `pd.to_numeric()` |
| converter texto de data/hora | `pd.to_datetime()` / `parse_dates` |
| inspecionar ausências | `isna()` |
| remover linhas sob regra definida de ausência | `dropna()` |
| preencher ausências sob regra definida | `fillna()` |
| agregar por grupo | `groupby()` + `agg()` |
| estatística de grupo ao lado de cada linha | `groupby()` + `transform()` |
| join por chave estilo banco | `merge()` + `validate=` quando conhecido |
| empilhar tabelas compatíveis | `concat()` |
| matriz de resumo | `pivot_table()` |
| reshape wide-to-long | `melt()` |
| carregar CSV | `read_csv()` |
| salvar CSV | `to_csv(index=...)` |

## 60. Referência rápida

```text
import pandas as pd

pd.Series(...)
pd.DataFrame(...)

df.shape
df.columns
df.dtypes
df.head()
df.info()
df.describe()

df["column"]
df[["column_a", "column_b"]]
df.loc[...]
df.iloc[...]

df.assign(...)
df.rename(...)
df.drop(...)
df.sort_values(...)
df.sort_index(...)

df.isna()
df.dropna(...)
df.fillna(...)
df.astype(...)
pd.to_numeric(...)
pd.to_datetime(...)

series.str...
series.dt...
series.value_counts()
series.nunique()

df.groupby(...)
df.agg(...)
df.transform(...)

df.merge(...)
pd.concat(...)
df.pivot_table(...)
df.melt(...)

pd.read_csv(...)
df.to_csv(...)
```

## 61. Checklist de design

Antes de aceitar uma transformação pandas, pergunte:

- Qual é o schema esperado de entrada?
- Quais colunas são identificadores, números, texto, datas ou categorias?
- O índice é significativo ou apenas posicional?
- O alinhamento por labels pode alterar o resultado?
- Valores ausentes são permitidos e o que significam?
- Inferência de dtype é aceitável nessa fronteira?
- Atualizações condicionais são feitas diretamente com `.loc`?
- A cardinalidade do merge é conhecida e validada?
- A ordem das linhas pode variar, e a saída precisa ser ordenada?
- Existe operação vetorizada disponível?
- `apply()` ou iteração por linhas realmente exigem lógica Python?
- Uma exportação incluirá o índice sem querer?
- Falhas permanecem visíveis em vez de serem silenciosamente convertidas?
- O contrato de versão do pandas está documentado?
- O código depende de suposições antigas de copy/view anteriores ao pandas 3.0?

## 62. Exercício

Construa um pipeline fictício de análise de pedidos:

1. Crie ou carregue um CSV com `order_id`, `customer_id`, `date`, `status`, `category` e `amount`.
2. Preserve identificadores como strings se zeros à esquerda forem permitidos.
3. Converta `date` para datetime.
4. Valide as colunas obrigatórias antes das transformações.
5. Converta `amount` numericamente e detecte entradas inválidas.
6. Relate valores ausentes por coluna.
7. Mantenha apenas linhas `paid` sem loop Python por linha.
8. Crie uma coluna derivada `month` a partir dos datetimes.
9. Gere resumo por `category` com total, média e quantidade de transações.
10. Faça join com uma tabela fictícia de clientes e valide a cardinalidade esperada.
11. Ordene explicitamente a saída do relatório.
12. Salve o resumo final sem exportar um índice acidental.
13. Torne falhas esperadas de qualidade visíveis em vez de escondê-las.

Desafios de extensão:

- compare uma solução vetorizada com uma baseada em `apply()`;
- construa uma pivot table wide;
- converta-a novamente para long com `melt()`;
- adicione testes para contagem de linhas, totais, unicidade de chaves, dtypes e cardinalidade de merge;
- documente quais transformações alteram a quantidade de linhas e por quê.

## 63. Conexões com conceitos anteriores de Python

`pandas` constrói sobre conceitos já estudados:

- **listas e dicionários:** construtores e conversões de resultados;
- **funções:** etapas reutilizáveis de transformação;
- **lógica booleana:** máscaras de linhas;
- **exceções:** falhas visíveis de I/O, conversão e joins;
- **arquivos e context managers:** fronteiras CSV e outros dados;
- **`pathlib`:** objetos de caminho funcionam naturalmente com I/O do pandas;
- **`datetime`:** pandas amplia o trabalho com datas para colunas;
- **CSV e JSON:** pandas adiciona uma camada orientada a tabelas sobre formatos de dados;
- **`decimal`:** escolhas de representação continuam importantes; colunas de ponto flutuante não substituem requisitos de decimal exato;
- **`logging`:** pipelines operacionais devem relatar contexto útil sem esconder exceções;
- **`os` e `shutil`:** descoberta e movimentação de arquivos frequentemente cercam pipelines pandas.

## 64. Referências

Principais referências usadas neste capítulo:

- [Documentação pandas 3.0.5](https://pandas.pydata.org/docs/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Visão geral do pacote pandas](https://pandas.pydata.org/docs/getting_started/overview.html)
- [Tutoriais Getting Started](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)
- [Release notes do pandas 3.0.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html)

A documentação oficial identifica pandas 3.0.5 como a documentação estável usada para este capítulo, e pandas 3.0 requer Python 3.11 ou superior.

## 65. Próximo capítulo

Este capítulo abre a **Fase 9: Bibliotecas Externas**.

A próxima biblioteca planejada é **`openpyxl`**, com foco em operações programáticas sobre workbooks do Excel.

Antes de avançar, pratique pandas com conjuntos de dados pequenos o suficiente para serem inspecionados manualmente. Uma biblioteca de tabelas só se torna útil quando você ainda consegue raciocinar sobre o que cada transformação deveria fazer.
