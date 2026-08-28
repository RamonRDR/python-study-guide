<div align="center">

# Controlando Dialetos CSV e Contratos de Texto Tabular

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Biblioteca Padrão](../README.pt-BR.md) · [← Anterior: Controlando Contratos de Serialização e Decodificação JSON](../03-json/README.pt-BR.md)

A Fase 7 apresentou CSV como formato tabular e ensinou o uso prático de `csv.reader()`, `csv.writer()`, `csv.DictReader()` e `csv.DictWriter()`. Este capítulo avança uma camada.

O módulo `csv` não é apenas uma forma de separar linhas em colunas. Ele é uma ferramenta de fronteira para definir como delimitadores, quoting, escaping, finais de linha, cabeçalhos, campos ausentes, campos extras e conversão de tipos se comportam entre sistemas.

O objetivo é transformar "este é um arquivo CSV" em uma pergunta mais precisa:

```text
Qual contrato de texto tabular este programa aceita e produz?
```

**Tempo estimado de estudo:** 120–160 minutos.

**Requisito de Python:** Python 3.10 ou mais recente para as APIs centrais ensinadas aqui. `csv.QUOTE_NOTNULL` e `csv.QUOTE_STRINGS` foram adicionados no Python 3.12 e seu comportamento de escrita está disponível nessa versão. Por causa de um bug documentado do Python 3.12, o comportamento especial de leitura exige Python 3.13 ou mais recente.

**Base da documentação:** comportamentos e exemplos foram conferidos com a documentação oficial do `csv` do Python 3.14.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- tratar CSV como uma família de contratos de texto tabular, e não como um único layout universal;
- separar codificação de texto das regras do dialeto CSV;
- explicar por que objetos de arquivo CSV devem ser abertos com `newline=""`;
- distinguir registros CSV lógicos de linhas físicas de texto;
- configurar delimitadores, caracteres de aspas, escaping e terminadores de linha de forma deliberada;
- explicar o comportamento dos principais modos `QUOTE_*`;
- reconhecer o comportamento de conversão de tipos de `QUOTE_NONNUMERIC`;
- entender o comportamento de escrita de `QUOTE_NOTNULL` e `QUOTE_STRINGS` no Python 3.12+, além da semântica corrigida de leitura no Python 3.13+;
- explicar por que a conversão padrão de `None` pelo writer perde informação;
- validar cabeçalhos do `DictReader` e larguras irregulares de linhas;
- controlar chaves extras e ausentes com `DictWriter`;
- usar `strict=True` e `csv.Error` quando entrada malformada deve falhar visivelmente;
- usar `field_size_limit()` como um dos controles da fronteira de entrada;
- tratar `Sniffer` e `has_header()` como heurísticas, e não como autoridades;
- lidar com BOM UTF-8 apenas quando a interface ao redor exigir;
- distinguir segurança de parsing CSV da interpretação de fórmulas por planilhas;
- projetar contratos explícitos e testáveis de importação e exportação CSV.

## 1. O que muda em relação à introdução de CSV da Fase 7?

Você já conhece as APIs centrais orientadas a linhas:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

e as variantes orientadas a dicionários:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])
```

A Fase 7 concentrou-se em escolher o parser correto e manter parsing separado da validação.

Este capítulo se concentra na política ao redor do parser:

```text
bytes de texto
   ↓ decodificação de caracteres
texto Python
   ↓ dialeto CSV + política de parsing
linhas e campos
   ↓ schema + validação de tipos
valores confiáveis para a aplicação
```

As APIs são familiares. O contrato é mais profundo.

## 2. CSV não é um único dialeto universal

O nome CSV sugere valores separados por vírgula, mas interfaces reais de texto tabular diferem em vários pontos:

- delimitador;
- caractere de aspas;
- regra de escaping;
- terminador de linha;
- se espaços após delimitadores são significativos;
- se entrada malformada deve ser aceita ou rejeitada;
- se existe cabeçalho;
- o que os nomes das colunas significam;
- qual codificação de texto transporta o arquivo.

A RFC 4180 documenta um formato CSV comum e o media type `text/csv`, mas é informativa e não elimina os muitos dialetos usados na prática.

Portanto, um nome de arquivo terminado em `.csv` não é um contrato completo de parsing.

## 3. Codificação de texto e dialeto CSV são camadas separadas

Um parser CSV opera sobre texto. Se a origem está armazenada como bytes, a decodificação de caracteres acontece primeiro.

Mantenha as camadas separadas:

```text
bytes
   ↓ UTF-8, UTF-8 com BOM ou outra codificação declarada
texto
   ↓ regras de delimitador + quoting + escaping
campos
```

Para um contrato UTF-8:

```python
with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Trocar `delimiter=","` por `delimiter=";"` não muda a codificação de caracteres. Trocar `encoding="utf-8"` não escolhe o delimitador CSV.

## 4. Use `newline=""` para objetos de arquivo CSV

Quando um arquivo real é passado ao módulo `csv`, abra-o com `newline=""`:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)
```

O módulo `csv` realiza seu próprio tratamento de novas linhas. A documentação oficial observa que omitir `newline=""` pode quebrar novas linhas embutidas em campos entre aspas e pode introduzir um carriage return adicional ao escrever em plataformas que usam finais de linha `\r\n`.

Trate `newline=""` como parte do padrão de I/O de arquivos CSV, não como sintaxe decorativa.

## 5. Um registro CSV pode ocupar várias linhas físicas

Este é um único registro CSV lógico:

```text
name,note
Ada,"first line
second line"
```

A nova linha dentro do campo entre aspas pertence aos dados do campo. Ela não necessariamente encerra o registro CSV.

Por isso, código assim não é seguro para parsing CSV geral:

```python
for line in file:
    columns = line.split(",")
```

Um parser CSV entende quoting e fronteiras de registros. Um loop por linhas físicas, sozinho, não possui informação suficiente.

## 6. Um dialeto agrupa decisões de formatação

O Python agrupa opções relacionadas de formatação CSV em um **dialeto**.

Um dialeto pode definir configurações como:

- `delimiter`;
- `quotechar`;
- `doublequote`;
- `escapechar`;
- `lineterminator`;
- `quoting`;
- `skipinitialspace`;
- `strict`.

Você pode fornecer um dialeto nomeado:

```python
reader = csv.reader(file, dialect="excel")
```

ou fornecer parâmetros de formatação diretamente:

```python
reader = csv.reader(
    file,
    delimiter=";",
    quotechar='"',
    strict=True,
)
```

O ponto importante não é se a política é nomeada ou inline. O importante é que produtor e consumidor concordem com ela.

## 7. O Python inclui vários dialetos registrados

Nomes embutidos comuns incluem:

- `excel`;
- `excel-tab`;
- `unix`.

Você pode inspecionar os nomes registrados:

```python
import csv

print(csv.list_dialects())
```

Não presuma que um arquivo produzido por um programa de planilha corresponde automaticamente a cada detalhe do dialeto `excel` do Python. Configurações de exportação, locale, comportamento do aplicativo e transformações posteriores podem mudar o contrato de texto real.

Inspecione ou documente a interface que você realmente recebe.

## 8. Registre um dialeto nomeado quando o reuso melhora a clareza

Uma aplicação controlada pode registrar uma política de dialeto recorrente:

```python
import csv

csv.register_dialect(
    "study_semicolon",
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
```

Depois ela pode ser reutilizada:

```python
reader = csv.reader(file, dialect="study_semicolon")
```

Outras ferramentas relacionadas incluem:

- `csv.get_dialect()`;
- `csv.list_dialects()`;
- `csv.unregister_dialect()`.

Registre um nome compartilhado no processo somente quando esse nome tornar o contrato mais fácil de entender. Parâmetros explícitos podem ser mais claros para uma fronteira usada uma única vez.

## 9. Parâmetros de formatação podem sobrescrever um dialeto

`reader()` e `writer()` aceitam um dialeto e também parâmetros individuais de formatação. Esses parâmetros podem sobrescrever partes do dialeto selecionado.

Por exemplo:

```python
reader = csv.reader(
    file,
    dialect="excel",
    delimiter=";",
)
```

O resultado já não é simplesmente "o dialeto Excel". É o dialeto Excel com um override de delimitador.

Ao diagnosticar uma interface, inspecione a política efetiva completa em vez de raciocinar apenas a partir do nome do dialeto.

## 10. O delimitador é um separador de campos de um caractere

O dialeto `excel` padrão usa vírgula:

```python
reader = csv.reader(file, delimiter=",")
```

Um contrato com ponto e vírgula pode ser explícito:

```python
reader = csv.reader(file, delimiter=";")
```

A configuração `delimiter` é uma string de um caractere. Separadores com vários caracteres pertencem a outro desenho de parsing.

Não adivinhe o delimitador a partir de convenções regionais quando o produtor puder defini-lo explicitamente.

## 11. `quotechar` protege conteúdo especial

O caractere de aspas padrão é a aspa dupla:

```text
name,note
Ada,"commas, stay inside this field"
```

As aspas fazem parte da representação CSV e normalmente não fazem parte do valor retornado do campo.

Com a política normal `doublequote=True`, uma aspa dentro de um campo entre aspas é representada duplicando-a:

```text
name,note
Ada,"She said ""hello"""
```

O reader reconstrói o conteúdo do campo conforme o dialeto.

## 12. `doublequote` e `escapechar` definem como aspas são escapadas

Quando `doublequote=True`, um `quotechar` interno é duplicado.

Quando `doublequote=False`, o `escapechar` configurado é usado em seu lugar.

Por exemplo:

```python
writer = csv.writer(
    file,
    doublequote=False,
    escapechar="\\",
)
```

Se `doublequote=False` e não existir `escapechar`, escrever um campo que contenha o caractere de aspas pode levantar `csv.Error`.

Escaping é uma regra de representação. Ela deve corresponder às expectativas do consumidor.

## 13. Modos de quoting são política de parser e writer

O Python expõe várias constantes `QUOTE_*`:

| Modo | Ideia principal |
|---|---|
| `QUOTE_MINIMAL` | Colocar aspas apenas nos campos que exigem caracteres especiais |
| `QUOTE_ALL` | Colocar aspas em todos os campos |
| `QUOTE_NONNUMERIC` | Colocar aspas em campos de saída não numéricos e converter campos de entrada sem aspas para `float` |
| `QUOTE_NONE` | Nunca usar quoting; escaping passa a ser necessário para caracteres especiais |
| `QUOTE_NOTNULL` | Python 3.12+: distinguir campos vazios sem aspas como `None` |
| `QUOTE_STRINGS` | Python 3.12+: colocar aspas em strings e usar campos vazios sem aspas para `None` |

O modo não é apenas formatação visual. Alguns modos também mudam o comportamento de decodificação.

## 14. `QUOTE_MINIMAL` e `QUOTE_ALL` expressam políticas de saída diferentes

`QUOTE_MINIMAL` é o padrão mais comum:

```python
writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
```

Apenas campos que exigem aspas conforme o dialeto são citados.

`QUOTE_ALL` coloca aspas em todos os campos:

```python
writer = csv.writer(file, quoting=csv.QUOTE_ALL)
```

Colocar aspas em todos os campos pode tornar a representação mais uniforme, mas não resolve automaticamente validação de schema, diferenças de encoding ou questões de segurança específicas de planilhas.

## 15. `QUOTE_NONE` exige uma política deliberada de escaping

Com `QUOTE_NONE`, o writer nunca coloca campos entre aspas:

```python
writer = csv.writer(
    file,
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
)
```

Caracteres que precisam de escaping recebem o `escapechar` configurado como prefixo.

Se nenhum `escapechar` estiver configurado e um campo contiver um caractere que exija escaping, o writer levanta `csv.Error`.

Use `QUOTE_NONE` somente quando a interface receptora definir regras de escaping compatíveis.

## 16. `QUOTE_NONNUMERIC` muda os tipos de entrada

Por padrão, readers CSV retornam campos como strings.

`QUOTE_NONNUMERIC` é diferente. Na leitura, campos sem aspas são convertidos para `float`:

```python
import csv
from io import StringIO

source = StringIO('"name","score"\n"Ada",91\n')
reader = csv.reader(source, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    print(row)
```

O campo numérico `91` vira `91.0` porque não estava entre aspas.

Essa é uma regra de conversão orientada pela representação, não um sistema completo de tipos da aplicação. Alguns valores numéricos do Python, incluindo tipos cuja representação em string não pode ser convertida para `float`, não são adequados para round trip nesse modo.

Para muitos contratos de aplicação, conversão explícita após o parsing normal de strings é mais fácil de validar e explicar.

## 17. O Python 3.12 adicionou `QUOTE_NOTNULL`; o suporte do reader foi corrigido no 3.13

`csv.QUOTE_NOTNULL` foi adicionado no Python 3.12. Seu comportamento de escrita está disponível nessa versão, mas o Python 3.12 possui um bug documentado: essa constante não afeta objetos `reader`. Esse bug de leitura foi corrigido no Python 3.13.

Na escrita no Python 3.12+, ele coloca aspas em todo campo que não seja `None`. Um valor `None` é escrito como campo vazio sem aspas.

A partir do Python 3.13, na leitura, um campo vazio sem aspas vira `None`, enquanto os demais campos se comportam como em `QUOTE_ALL`.

Isso cria uma distinção no nível da representação entre:

```text

```

e:

```text
""
```

A partir do Python 3.13, o primeiro pode ser lido como `None` nesse modo, enquanto a string vazia entre aspas continua sendo uma string vazia.

Use apenas quando os dois lados da interface concordarem com esse significado e documente se o contrato precisa do suporte de escrita desde o Python 3.12 ou da semântica nullable do reader a partir do Python 3.13.

## 18. O Python 3.12 adicionou `QUOTE_STRINGS`; o suporte do reader foi corrigido no 3.13

`csv.QUOTE_STRINGS` também foi adicionado no Python 3.12. Seu comportamento de escrita está disponível nessa versão, mas seu comportamento especial de leitura é afetado pelo mesmo bug do Python 3.12 e exige Python 3.13+.

Na escrita no Python 3.12+, campos string sempre recebem aspas, enquanto `None` vira um campo vazio sem aspas.

A partir do Python 3.13, na leitura, campos vazios sem aspas viram `None`, e o comportamento restante segue `QUOTE_NONNUMERIC`, incluindo a conversão de campos não vazios e sem aspas para `float`.

Esse comportamento de conversão significa que o modo não é simplesmente "coloque aspas em todas as strings". Ele também carrega uma política de decodificação.

Constantes específicas de versão devem ser documentadas em interfaces que possam rodar em versões mais antigas do Python.

## 19. A conversão padrão de `None` pelo writer perde informação

O writer CSV comum escreve `None` como string vazia:

```python
import csv
from io import StringIO

output = StringIO(newline="")
writer = csv.writer(output, lineterminator="\n")
writer.writerow(["Ada", None, ""])

print(output.getvalue())
```

Assim, tanto `None` quanto a string vazia podem virar campos vazios na política padrão.

Essa transformação é intencionalmente não reversível.

Se sua aplicação precisa distinguir valores ausentes de strings vazias, defina uma representação explícita, como:

- um texto sentinela documentado;
- uma representação nullable definida pelo schema;
- `QUOTE_NOTNULL` ou `QUOTE_STRINGS` no Python 3.12+ quando sua semântica se encaixar na interface;
- outro formato de dados quando CSV não conseguir preservar claramente as distinções necessárias.

## 20. Campos CSV são strings por padrão, não valores inferidos da aplicação

Com o comportamento comum de `csv.reader()`:

```text
91
false
2026-08-28
```

todos chegam como campos de texto.

Seu programa decide se eles significam:

- um inteiro;
- um booleano;
- uma data;
- ou simplesmente uma string.

Mantenha as etapas visíveis:

```text
texto do campo CSV
   ↓ conversão da aplicação
valor candidato
   ↓ validação
valor confiável
```

Não dependa apenas da aparência de um campo para definir seu tipo.

## 21. Converta e valide depois do parsing

Um conversor estreito torna o contrato testável:

```python
def parse_score(text: str) -> int:
    score = int(text)
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score
```

O parser CSV responde onde um campo termina e o próximo começa. O conversor responde o que um campo significa para a aplicação.

São responsabilidades diferentes.

## 22. `DictReader` torna o cabeçalho parte da interface

Quando `fieldnames` é omitido, `DictReader` usa o primeiro registro como chaves do dicionário e não retorna esse registro como dado:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])
```

Se você fornecer `fieldnames` explicitamente, a primeira linha será tratada como dado.

Essa diferença importa quando uma interface não possui cabeçalho ou quando a aplicação fornece um schema fixo independentemente do arquivo.

## 23. `restkey` e `restval` revelam larguras irregulares de linhas

Um `DictReader` pode encontrar linhas com mais ou menos campos do que o cabeçalho.

Se uma linha possui campos extras, eles são armazenados em uma lista sob `restkey`. O `restkey` padrão é `None`.

Se uma linha não vazia possui campos a menos, valores ausentes são preenchidos com `restval`. O padrão é `None`.

Para validação, um objeto sentinela privado pode deixar campos ausentes visíveis sem colidir com texto CSV legítimo:

```python
missing = object()
reader = csv.DictReader(
    file,
    restkey="_extra_fields",
    restval=missing,
)
```

Como campos CSV comuns são strings, esse objeto privado não pode ser confundido com texto legítimo de um campo. Sua aplicação pode rejeitar campos extras com `row.get(restkey)` e campos ausentes com uma verificação de identidade como `value is missing`.

Não deixe a recuperação do parser virar aceitação da aplicação silenciosamente.

## 24. Nomes de cabeçalho duplicados precisam de uma política explícita

Um contrato tabular normalmente espera nomes de colunas únicos.

Antes de depender de acesso por dicionário, valide o cabeçalho quando unicidade importar:

```python
def require_unique_header(header: list[str]) -> None:
    if len(header) != len(set(header)):
        raise ValueError("CSV header contains duplicate names")
```

Uma abordagem clara é:

```text
ler cabeçalho como linha normal
   ↓ validar nomes, ordem e unicidade
criar ou continuar a política de leitura das linhas
```

Um dicionário não consegue preservar dois valores independentes sob o mesmo nome de chave. Se colunas duplicadas são significativas, uma interface orientada a dicionário provavelmente é a abstração errada.

## 25. `DictWriter` torna explícita a ordem das colunas de saída

`DictWriter` exige `fieldnames`:

```python
import csv

fieldnames = ["name", "score", "status"]

with open("records.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {"name": "Ada", "score": 91, "status": "complete"}
    )
```

A sequência de fieldnames define a ordem das colunas de saída.

Isso torna o schema mais fácil de revisar do que depender de construção arbitrária de dicionários em outro ponto do programa.

## 26. `extrasaction` controla chaves inesperadas do dicionário

Por padrão, `DictWriter` levanta `ValueError` quando um dicionário de entrada contém uma chave que não está em `fieldnames`.

Você pode escolher:

```python
writer = csv.DictWriter(
    file,
    fieldnames=fieldnames,
    extrasaction="ignore",
)
```

mas ignorar chaves inesperadas pode descartar dados silenciosamente.

Prefira o comportamento padrão `"raise"`, a menos que remover chaves extras seja uma política de exportação deliberada e documentada.

## 27. Chaves ausentes no `DictWriter` usam `restval`

Se um dicionário de entrada não possui um dos campos de saída configurados, `DictWriter` escreve seu `restval`. O padrão é uma string vazia.

Você pode tornar a política explícita:

```python
writer = csv.DictWriter(
    file,
    fieldnames=fieldnames,
    restval="N/A",
)
```

Um sentinela como `N/A` só é apropriado se o contrato receptor atribuir esse significado a ele.

Não invente texto placeholder apenas para tornar a linha retangular.

## 28. `strict=True` pode fazer CSV malformado falhar visivelmente

A opção `strict` de um dialeto é `False` por padrão.

Quando `strict=True`, entrada CSV malformada detectada pelo parser levanta `csv.Error`:

```python
reader = csv.reader(file, strict=True)
```

Capture `csv.Error` onde seja possível reportar ou recuperar de forma útil:

```python
try:
    rows = list(reader)
except csv.Error as error:
    print(f"Invalid CSV: {error}")
```

Parsing estrito ainda não valida seu cabeçalho, tipos, campos obrigatórios ou regras de negócio.

## 29. `reader.line_num` conta linhas lidas da origem, não registros lógicos

Objetos reader expõem `line_num`.

Como um registro CSV pode ocupar várias linhas físicas, `line_num` é o número de linhas lidas da origem, e não simplesmente a quantidade de registros retornados.

Isso é útil para diagnósticos, mas nomeie corretamente:

```text
contexto da linha da origem
```

nem sempre é igual a:

```text
número do registro
```

## 30. `field_size_limit()` pode limitar campos individuais processados

O módulo expõe o tamanho máximo atual de campo aceito pelo parser:

```python
import csv

current_limit = csv.field_size_limit()
print(current_limit)
```

Você pode definir um novo limite:

```python
csv.field_size_limit(1_000_000)
```

Um limite de tamanho de campo pode fazer parte da política de fronteira de entrada, mas não substitui limites para tamanho total do arquivo, quantidade de registros, tempo de processamento ou conteúdo específico da aplicação.

Se alterar o limite em um processo compartilhado, documente a escolha porque ela afeta parsing CSV posterior naquele interpretador.

## 31. `Sniffer.sniff()` é uma heurística

`csv.Sniffer` pode inspecionar uma amostra e inferir um dialeto:

```python
import csv

sample = "name;score\nAda;91\nLin;88\n"
dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")

print(dialect.delimiter)
```

Isso é útil quando o produtor não consegue declarar o delimitador, mas inferência não é certeza.

Restringir os delimitadores candidatos pode alinhar melhor a heurística aos formatos realmente suportados pela aplicação.

## 32. Reposicione o arquivo depois de ler a amostra

Ao usar Sniffer em um arquivo, ler a amostra avança a posição do arquivo:

```python
import csv

with open("records.csv", "r", encoding="utf-8", newline="") as file:
    sample = file.read(1024)
    dialect = csv.Sniffer().sniff(sample)
    file.seek(0)
    reader = csv.reader(file, dialect)
```

Sem `file.seek(0)`, o parsing começaria depois da amostra, não no início do arquivo.

Amostragem é uma operação de I/O, então a posição do cursor faz parte do fluxo.

## 33. `Sniffer.has_header()` também é uma heurística

`has_header()` examina uma amostra e tenta adivinhar se o primeiro registro se parece com nomes de colunas.

A documentação oficial descreve explicitamente esse método como uma heurística aproximada que pode produzir falsos positivos e falsos negativos.

Portanto:

```text
Sniffer diz que há cabeçalho
```

não deve significar automaticamente:

```text
contrato da interface garante cabeçalho
```

Se o produtor puder especificar a existência do cabeçalho, use esse contrato explícito em vez de adivinhar.

## 34. `skipinitialspace=True` não é limpeza geral de espaços

Com `skipinitialspace=True`, espaços imediatamente após o delimitador são ignorados:

```python
reader = csv.reader(file, skipinitialspace=True)
```

Essa é uma regra de dialeto, não uma instrução geral para remover espaços de todos os campos.

Por exemplo, espaços iniciais ou finais dentro de conteúdo entre aspas ainda podem ser dados significativos.

Evite aplicar `.strip()` cegamente, a menos que o contrato da aplicação defina explicitamente essa normalização.

## 35. `lineterminator` é principalmente uma política do writer

O writer usa `lineterminator` para encerrar registros de saída. O padrão é `"\r\n"`.

Você pode definir uma representação controlada:

```python
writer = csv.writer(file, lineterminator="\n")
```

O comportamento atual do reader é diferente: ele reconhece `\r` ou `\n` como final de linha e ignora a configuração `lineterminator` do dialeto.

Não presuma que um terminador personalizado do writer se torna uma regra simétrica do reader.

## 36. Tratamento de BOM UTF-8 pertence à fronteira de texto

Alguns produtores CSV, especialmente fluxos orientados a planilhas, podem gerar texto UTF-8 com byte-order mark no início.

Se a interface permitir explicitamente essa representação, o codec `utf-8-sig` do Python pode consumir o BOM durante a decodificação:

```python
with open("records.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)
```

Não use `utf-8-sig` como botão mágico de reparo CSV. Decida se entrada com BOM realmente faz parte do contrato de texto suportado.

Encoding continua separado das regras de delimitador e quoting.

## 37. Parsers CSV não avaliam fórmulas de planilha

O módulo `csv` processa campos de texto. Ele não executa fórmulas de planilha.

O risco pode aparecer depois quando dados CSV exportados contendo texto não confiável são abertos por software de planilha. Alguns programas podem interpretar valores de células iniciados por caracteres como `=`, `+`, `-` ou `@` como fórmulas.

Isso cria duas perguntas diferentes:

```text
Este campo está escapado corretamente como CSV?
```

e:

```text
A planilha de destino interpretará esta célula como conteúdo executável de fórmula?
```

Quoting CSV correto não responde universalmente à segunda pergunta.

Não existe uma única transformação de sanitização segura para todos os programas de planilha e todos os consumidores programáticos posteriores. Se uma exportação é destinada a visualização em planilhas e contém dados não confiáveis, defina e teste uma política de mitigação específica para o destino.

## 38. Valide o schema tabular depois do parsing

Uma fronteira de importação útil pode validar várias camadas de forma independente:

```text
codificação de texto
   ↓
sintaxe CSV e dialeto
   ↓
nomes e unicidade do cabeçalho
   ↓
largura da linha
   ↓
conversão de tipos dos campos
   ↓
regras de valor dos campos
```

Por exemplo, uma tabela de notas pode exigir:

```text
cabeçalho exato: name,score,status
name: texto não vazio
score: inteiro 0..100
status: um entre complete, review
sem campos extras
sem campos ausentes
```

A sintaxe CSV sozinha não consegue impor essas regras.

## 39. Erros comuns

### Erro 1: presumir que `.csv` significa vírgula mais configurações Excel padrão

A extensão não define cada regra de dialeto e encoding.

### Erro 2: omitir `newline=""` em objetos de arquivo CSV reais

Isso pode quebrar novas linhas embutidas e finais de linha na saída.

### Erro 3: separar linhas físicas manualmente

Campos CSV entre aspas podem conter delimitadores e novas linhas embutidas.

### Erro 4: tratar `QUOTE_NONNUMERIC` como conversor completo de schema

Ele aplica apenas uma regra específica de conversão para `float` orientada pela representação.

### Erro 5: esquecer que a saída padrão de `None` perde informação

`None` e uma string vazia podem ser serializados para o mesmo campo vazio.

### Erro 6: aceitar linhas irregulares de `DictReader` sem verificar `restkey` e `restval`

A recuperação do parser pode esconder formatos de tabela inválidos.

### Erro 7: usar `extrasaction="ignore"` apenas para silenciar erros de exportação

Campos inesperados podem desaparecer sem aviso.

### Erro 8: confiar em `Sniffer` como detector garantido de schema

Detecção de delimitador e cabeçalho é heurística.

### Erro 9: usar `.strip()` automaticamente em todos os campos

Espaços podem ser dados significativos.

### Erro 10: presumir que quoting CSV correto impede interpretação de fórmulas em planilhas

Segurança de sintaxe CSV e comportamento de execução de planilhas são preocupações separadas.

## 40. Exemplo prático: round trip com dialeto explícito

```python
import csv
from io import StringIO


rows = [
    ["name", "note"],
    ["Ada", "comma, semicolon; and newline\ninside"],
    ["Lin", 'She said "hello"'],
]

output = StringIO(newline="")
writer = csv.writer(
    output,
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerows(rows)

text = output.getvalue()
print(text)

source = StringIO(text, newline="")
reader = csv.reader(
    source,
    delimiter=";",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
)
print(list(reader))
```

Versão executável: [`examples/dialect_round_trip.py`](examples/dialect_round_trip.py).

## 41. Exemplo prático: validar linhas em dicionário

```python
import csv
from io import StringIO


text = "name,score,status\nAda,91,complete\nLin,88,review\n"
source = StringIO(text, newline="")
missing = object()
reader = csv.DictReader(
    source,
    restkey="_extra_fields",
    restval=missing,
)

expected_fields = ["name", "score", "status"]
if reader.fieldnames != expected_fields:
    raise ValueError("unexpected CSV header")

records = []
for row in reader:
    if row.get("_extra_fields") is not None:
        raise ValueError("row contains extra fields")
    if any(value is missing for value in row.values()):
        raise ValueError("row contains missing fields")

    score = int(row["score"])
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    records.append(
        {
            "name": row["name"],
            "score": score,
            "status": row["status"],
        }
    )

print(records)
```

Versão executável: [`examples/validate_dict_rows.py`](examples/validate_dict_rows.py).

## 42. Exemplo prático: detectar um delimitador permitido

```python
import csv
from io import StringIO


text = 'name;note\nAda;"uses, commas in text"\nLin;ready\n'
dialect = csv.Sniffer().sniff(text, delimiters=",;\t")

print(repr(dialect.delimiter))

source = StringIO(text, newline="")
reader = csv.reader(source, dialect)
print(list(reader))
```

Versão executável: [`examples/sniff_delimiter.py`](examples/sniff_delimiter.py).

## 43. Exemplo prático: escaping sem quoting

```python
import csv
from io import StringIO


row = ["alpha,beta", 'quoted "text"', "line\nbreak"]

output = StringIO(newline="")
writer = csv.writer(
    output,
    delimiter=",",
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
    lineterminator="\n",
)
writer.writerow(row)

text = output.getvalue()
print(repr(text))

source = StringIO(text, newline="")
reader = csv.reader(
    source,
    delimiter=",",
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
)
print(next(reader))
```

Versão executável: [`examples/quote_none_escape.py`](examples/quote_none_escape.py).

## 44. Exercício

Crie uma função chamada `decode_results(text)` para um contrato controlado de importação CSV.

Requisitos:

1. Faça o parsing de texto CSV com `StringIO` e `csv.DictReader`.
2. Exija o cabeçalho exato `name,score,status` nessa ordem.
3. Rejeite nomes duplicados no cabeçalho.
4. Rejeite linhas com campos extras.
5. Rejeite linhas com campos ausentes.
6. Exija que `name` seja não vazio após a política de normalização que você escolher explicitamente.
7. Converta `score` para `int` e exija valor de 0 a 100.
8. Exija que `status` seja `complete` ou `review`.
9. Retorne uma lista de dicionários validados cujos valores `score` sejam inteiros.

Depois crie `encode_results(records)` que:

1. escreva os mesmos três campos na mesma ordem;
2. escreva o cabeçalho explicitamente;
3. use `lineterminator="\n"` para saída determinística;
4. rejeite dicionários contendo chaves inesperadas em vez de descartá-las silenciosamente;
5. retorne o texto CSV gerado.

Teste pelo menos estes casos:

```text
linhas válidas
ordem errada do cabeçalho
cabeçalho duplicado
campo extra
campo ausente
score = texto
score = 101
status desconhecido
campo contendo vírgula
campo contendo nova linha embutida
```

A parte importante não é apenas processar linhas válidas. Torne cada suposição sobre a tabela visível o suficiente para que outro programador consiga explicar por que um arquivo inválido é rejeitado.

## 45. Referência rápida

| Necessidade | Ferramenta / política |
|---|---|
| Ler linhas CSV | `csv.reader()` |
| Escrever linhas CSV | `csv.writer()` |
| Ler linhas pelo nome da coluna | `csv.DictReader()` |
| Escrever dicionários em ordem fixa de colunas | `csv.DictWriter()` |
| Abrir arquivos CSV reais corretamente | `newline=""` |
| Escolher separador de campos | `delimiter=...` |
| Escolher caractere de aspas | `quotechar=...` |
| Escapar sem quoting comum | `escapechar=...`, frequentemente com `QUOTE_NONE` |
| Colocar aspas apenas quando necessário | `csv.QUOTE_MINIMAL` |
| Colocar aspas em todos os campos | `csv.QUOTE_ALL` |
| Converter campos de entrada sem aspas para `float` | `csv.QUOTE_NONNUMERIC` |
| Distinguir `None` de string vazia entre aspas na escrita (3.12+) e na leitura (3.13+) | `csv.QUOTE_NOTNULL` |
| Colocar aspas em strings / representar `None` na escrita (3.12+); usar semântica nullable do reader a partir do 3.13 | `csv.QUOTE_STRINGS` |
| Rejeitar entrada malformada do parser com mais rigor | `strict=True` |
| Detectar largura irregular no `DictReader` | `restkey=...`, `restval=...` |
| Rejeitar ou ignorar chaves extras no `DictWriter` | `extrasaction="raise"` / `"ignore"` |
| Controlar fim de registro do writer | `lineterminator=...` |
| Limitar tamanho de campo do parser | `csv.field_size_limit()` |
| Inferir dialeto a partir de amostra | `csv.Sniffer().sniff()` |
| Inferir se existe cabeçalho | `csv.Sniffer().has_header()` |
| Ler texto UTF-8 que pode começar com BOM | `encoding="utf-8-sig"` |
| Capturar erros do parser CSV | `csv.Error` |

## 46. Checklist de design

Antes de publicar ou consumir uma interface CSV, pergunte:

```text
Qual codificação de caracteres é usada?
BOM UTF-8 é permitido?
Qual delimitador é obrigatório?
Quais regras de aspas e escaping são obrigatórias?
Qual final de linha o produtor escreve?
Existe cabeçalho?
Os nomes do cabeçalho são únicos e case-sensitive?
A ordem das colunas é significativa?
Como campos ausentes e extras são tratados?
Como None é representado de forma diferente de string vazia?
Quais campos exigem conversão explícita de tipos?
Quais limites de arquivo, campo e número de linhas se aplicam?
Detecção de dialeto é permitida ou o formato deve ser explícito?
Campos não confiáveis serão depois abertos em software de planilha?
```

Se essas respostas forem explícitas, CSV se torna uma interface testável em vez de uma coleção de suposições escondidas atrás da extensão `.csv`.

## Referências

- [Documentação Python 3.14: `csv` — leitura e escrita de arquivos CSV](https://docs.python.org/3.14/library/csv.html)
- [Documentação Python 3.14: `codecs` — registro de codecs e classes base](https://docs.python.org/3.14/library/codecs.html)
- [RFC 4180: Common Format and MIME Type for Comma-Separated Values (CSV) Files](https://www.rfc-editor.org/rfc/rfc4180)
- [OWASP: CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection)

## Próximo capítulo

Continue com o [**Capítulo 05: Projetando Pipelines de Logging e Contratos de Contexto em Runtime**](../05-logging/README.pt-BR.md). Ele aprofunda níveis efetivos, roteamento por handlers, propagação, configuração, registros contextuais, entrega por filas, concorrência e segurança operacional de logging.
