<div align="center">

# Controlando Dialetos CSV, Quoting e Contratos Tabulares

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

> **Fase 8 · Biblioteca Padrão · Capítulo 04**

CSV parece simples porque um arquivo pequeno pode se parecer com linhas separadas por vírgulas. Interfaces CSV reais são mais exigentes: produtores divergem em delimitadores, quoting, finais de linha, valores nulos, cabeçalhos, encodings e linhas malformadas. O módulo `csv` do Python existe para modelar essas regras explicitamente em vez de reconstruir um parser com `split(",")`.

Este capítulo revisita CSV em um nível mais profundo de biblioteca. A Fase 7 introduziu CSV como formato de arquivo. Aqui o foco é o **contrato** ao redor de `csv.reader`, `csv.writer`, `DictReader`, `DictWriter`, dialetos, modos de quoting, entrada malformada, limites de recursos e interoperabilidade.

## 1. Qual problema o `csv` resolve?

O módulo lê e escreve **texto tabular delimitado** de acordo com um dialeto.

```python
import csv
from io import StringIO

text = "name,score\nAna,88\nBob,91\n"
reader = csv.reader(StringIO(text, newline=""))

for row in reader:
    print(row)
```

Por padrão, os campos retornam como strings. CSV por si só não fornece um schema completo da aplicação, então fazer o parsing das linhas e validar o significado de negócio são responsabilidades separadas.

## 2. CSV é uma família de dialetos, não um layout universal

"CSV" não garante que todo produtor use o mesmo delimitador ou as mesmas regras de quoting.

Variações comuns incluem:

```text
delimitador vírgula
delimitador ponto e vírgula
delimitador tab
campos com aspas
campos escapados
diferentes finais de linha
diferentes encodings de caracteres
```

O Python agrupa escolhas de parsing e formatação em um `Dialect`. Dialetos embutidos incluem `excel`, `excel-tab` e `unix`.

Um dialeto descreve sintaxe. Ele não prova que os dados possuem as colunas ou regras de valores exigidas pela aplicação.

## 3. Readers fazem parsing de texto; writers formatam texto

Um writer recebe valores Python e escreve texto delimitado por meio de um objeto file-like com `write()`.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(stream, lineterminator="\n")
writer.writerow(["name", "score"])
writer.writerow(["Ana", 88])

print(stream.getvalue())
```

Um reader consome um iterável de strings. Em arquivos reais, a decodificação de caracteres pertence a `open()`, enquanto o parsing da sintaxe CSV pertence a `csv`.

Essa separação é parecida com a fronteira de JSON do capítulo anterior:

```text
bytes em armazenamento/rede
   ↓ decodificação de texto
Python str
   ↓ parsing CSV
linhas e campos
   ↓ validação da aplicação
valores de domínio confiáveis
```

## 4. Use `newline=""` em objetos de arquivo CSV

Quando um arquivo real é passado a `csv.reader()` ou `csv.writer()`, a documentação do Python recomenda abri-lo com `newline=""`.

```python
import csv

with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Isso permite que o módulo `csv` faça seu próprio tratamento de novas linhas. É especialmente importante para campos entre aspas que contêm quebras de linha e para evitar comportamento indesejado de carriage return em plataformas que usam `\r\n`.

`newline=""` é uma política de abertura do arquivo. Não é configuração de delimitador nem de schema de registro.

## 5. `delimiter` e `quotechar` fazem parte da interface

Se um produtor usa ponto e vírgula, configure isso explicitamente:

```python
import csv
from io import StringIO

text = 'name;note\nAna;"uses;semicolon"\n'
reader = csv.reader(
    StringIO(text, newline=""),
    delimiter=";",
    quotechar='"',
)

print(list(reader))
```

Delimitador e caractere de aspas são escolhas de sintaxe de um único caractere. Sempre que possível, devem vir de um contrato conhecido da interface.

Não adivinhe um delimitador apenas porque uma amostra contém determinado sinal de pontuação.

## 6. `QUOTE_MINIMAL` coloca aspas somente quando a sintaxe CSV exige

`csv.QUOTE_MINIMAL` é o padrão usual quando existe um caractere de aspas.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerow(["Ana", "uses;semicolon"])

print(stream.getvalue())
```

Aqui o segundo campo contém o delimitador, então o writer o coloca entre aspas.

Outras políticas importantes são:

- `QUOTE_ALL`: coloca todos os campos entre aspas;
- `QUOTE_MINIMAL`: coloca entre aspas apenas campos exigidos pelo dialeto;
- `QUOTE_NONNUMERIC`: o writer coloca campos não numéricos entre aspas e o reader converte campos sem aspas para `float`;
- `QUOTE_NONE`: nunca trata caracteres de aspas de maneira especial;
- `QUOTE_NOTNULL`: coloca todos os campos diferentes de `None` entre aspas e preserva um campo vazio sem aspas como `None` na leitura;
- `QUOTE_STRINGS`: coloca strings entre aspas, aplica conversão no estilo de `QUOTE_NONNUMERIC` a valores numéricos sem aspas e usa campos vazios sem aspas como `None`.

`QUOTE_NOTNULL` e `QUOTE_STRINGS` foram adicionados no Python 3.12 e estão disponíveis no Python 3.14.

## 7. `QUOTE_NONNUMERIC` altera tipos durante a leitura

A maior parte da leitura CSV retorna strings. `QUOTE_NONNUMERIC` é uma exceção importante.

```python
import csv
from io import StringIO

text = '3,19.90,"ready"\n'
reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NONNUMERIC,
)

row = next(reader)
print(row)
print([type(value).__name__ for value in row])
```

Campos sem aspas são convertidos para `float`; campos entre aspas permanecem strings.

Esse modo não é um sistema geral de schema. Alguns valores produzidos a partir de tipos Python com aparência numérica, como `bool`, `Fraction` ou `IntEnum`, podem ter representações em texto que não podem ser convertidas de volta para `float`.

Use validação explícita da aplicação quando tipos exatos importarem.

## 8. `QUOTE_NOTNULL` pode distinguir `None` de string vazia

O writer comum serializa `None` como string vazia, o que sozinho não é reversível.

Python 3.12+ fornece `QUOTE_NOTNULL`:

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NOTNULL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", None])
writer.writerow(["Bob", ""])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NOTNULL,
)
print(list(reader))
```

Com essa política:

- `None` vira um campo vazio **sem aspas**;
- uma string vazia continua sendo um valor diferente de `None` e recebe aspas;
- o reader correspondente interpreta um campo vazio sem aspas como `None`.

Isso é útil somente quando as duas pontas concordam com essa política de dialeto.

## 9. `QUOTE_STRINGS` só é útil quando seu contrato de conversão serve

`QUOTE_STRINGS` coloca campos string entre aspas, escreve `None` como campo vazio sem aspas e faz o reader interpretar campos não vazios sem aspas de forma semelhante a `QUOTE_NONNUMERIC`.

Isso significa que valores sem aspas são candidatos à conversão para `float`. Não equivale a "preservar tipos Python arbitrários."

Se a interface possui colunas como IDs, booleanos, decimais, datas ou enums, um schema coluna por coluna normalmente é mais claro que depender do modo de quoting para inferir tipos.

## 10. `QUOTE_NONE` normalmente exige uma estratégia de escape

Se quoting estiver desativado, delimitadores e outros caracteres especiais ainda precisam de representação.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NONE,
    escapechar="\\",
    lineterminator="\n",
)
writer.writerow(["Ana", "A,B"])

print(stream.getvalue())
```

Sem um `escapechar` utilizável, o writer pode lançar `csv.Error` ao encontrar caracteres que precisam ser escapados.

`doublequote`, `quotechar`, `escapechar` e `quoting` trabalham juntos. Alterar uma configuração pode mudar o que as demais precisam fazer.

## 11. O `lineterminator` do writer é explícito

Um dialeto também controla o final de linha do writer. O dialeto `excel` usa `\r\n` por padrão.

Para texto gerado de forma determinística, você pode definir:

```python
writer = csv.writer(file, lineterminator="\n")
```

Atualmente o reader reconhece `\r` ou `\n` de forma fixa como final de linha e não usa o `lineterminator` do dialeto como regra de correspondência. Não ensine `lineterminator` como um contrato simétrico entre reader e writer.

## 12. `DictReader` mapeia um cabeçalho para dicionários

Quando a primeira linha é um cabeçalho, `DictReader` permite acesso por nome:

```python
import csv
from io import StringIO

text = "name,score\nAna,88\nBob,91\n"
reader = csv.DictReader(StringIO(text, newline=""))

for row in reader:
    print(row["name"], row["score"])
```

Se `fieldnames` for omitido, a primeira linha vira a sequência de nomes dos campos e não é retornada como dado.

O mapeamento resultante preserva a ordem dos nomes, mas os valores ainda são campos decodificados de CSV, geralmente strings.

## 13. Campos extras e ausentes precisam de uma política explícita

Uma linha pode possuir mais ou menos campos que o cabeçalho.

```python
import csv
from io import StringIO

text = "name,score\nAna,88,extra\nBob\n"
reader = csv.DictReader(
    StringIO(text, newline=""),
    restkey="_extra",
    restval="_missing",
)

for row in reader:
    print(row)
```

No `DictReader`:

- campos extras são armazenados sob `restkey` como lista;
- campos ausentes recebem `restval`;
- ambos usam `None` por padrão se você não escolher outra coisa.

Usar os padrões pode deixar larguras de linha malformadas menos evidentes. Em contratos estritos, verifique deliberadamente valores extras e ausentes.

## 14. `DictWriter` possui sua própria fronteira de schema

`DictWriter` exige uma sequência `fieldnames` explícita.

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.DictWriter(
    stream,
    fieldnames=["name", "score"],
    extrasaction="raise",
    lineterminator="\n",
)
writer.writeheader()
writer.writerow({"name": "Ana", "score": 88})

print(stream.getvalue())
```

Se um dicionário de entrada contiver uma chave desconhecida:

- `extrasaction="raise"` lança `ValueError` e é o padrão;
- `extrasaction="ignore"` exclui silenciosamente a chave extra.

Chaves esperadas ausentes são escritas usando `restval`, cujo padrão é string vazia.

Escolha essas políticas intencionalmente. Omissão silenciosa pode ser conveniente, mas também pode esconder um erro do produtor.

## 15. Um cabeçalho CSV não é o mesmo que schema validado

Verificar o cabeçalho exato costuma ser uma boa primeira fronteira:

```python
import csv
from io import StringIO

EXPECTED = ["name", "score"]

text = "name,score\nAna,88\n"
reader = csv.DictReader(StringIO(text, newline=""))

if reader.fieldnames != EXPECTED:
    raise ValueError("unexpected CSV header")

rows = list(reader)
print(rows)
```

A aplicação também pode precisar validar:

```text
quantidade exata de colunas
colunas obrigatórias
ordem das colunas
identificadores não vazios
faixas de inteiros
formatos de data
regras decimais
status permitidos
identificadores duplicados
relações entre linhas
```

O módulo `csv` cuida da sintaxe. A aplicação é responsável pela validação semântica.

## 16. Tratamento de espaços não é limpeza automática

`skipinitialspace=True` ignora espaços imediatamente depois dos delimitadores.

Isso não significa "aplicar strip em todos os campos". Espaços finais, por exemplo, continuam fazendo parte dos dados até que a aplicação os remova.

Além disso, combinar `delimiter=" "` com `skipinitialspace=True` não permite campos vazios sem aspas. Trate regras de whitespace como parte do dialeto, não como limpeza genérica.

## 17. `strict=True` pede ao parser que rejeite entrada CSV ruim

O dialeto padrão é relativamente permissivo. Em interfaces que devem rejeitar sintaxe CSV malformada, use `strict=True`.

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'

try:
    list(csv.reader(StringIO(text, newline=""), strict=True))
except csv.Error:
    print("Malformed CSV rejected")
```

`strict=True` trata sintaxe CSV. Uma linha sintaticamente válida ainda pode violar o schema da aplicação.

## 18. `csv.Error` é a exceção de parsing/formatação do módulo

Quando o processamento CSV detecta um erro, pode lançar `csv.Error`.

Um reader também expõe `line_num`:

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'
reader = csv.reader(StringIO(text, newline=""), strict=True)

try:
    for row in reader:
        print(row)
except csv.Error:
    print(f"CSV error near physical line {reader.line_num}")
```

`line_num` conta linhas físicas lidas da origem. Não é necessariamente igual à quantidade de registros retornados porque um registro entre aspas pode ocupar várias linhas físicas.

## 19. `Sniffer` é heurística, não validação

`csv.Sniffer().sniff()` pode estimar um dialeto a partir de uma amostra de texto.

```python
import csv

sample = "name;score\nAna;88\nBob;91\n"
dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")

print(dialect.delimiter)
```

`Sniffer.has_header()` também pode estimar se a primeira linha parece ser um cabeçalho.

Ambos são heurísticos. `has_header()` pode produzir falsos positivos ou negativos, e `sniff()` pode escolher entre delimitadores plausíveis usando suas preferências.

Use sniffing para descoberta quando você realmente não controla o formato e depois valide o resultado contra políticas permitidas pela interface antes de confiar nele.

## 20. Dialetos registrados podem centralizar sintaxe repetida

Se vários arquivos compartilham a mesma sintaxe, registre um dialeto nomeado:

```python
import csv
from io import StringIO

csv.register_dialect(
    "study_semicolon",
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
)

reader = csv.reader(
    StringIO("name;score\nAna;88\n", newline=""),
    dialect="study_semicolon",
)
print(list(reader))

csv.unregister_dialect("study_semicolon")
```

`get_dialect()` retorna um objeto de dialeto imutável e `list_dialects()` mostra os nomes registrados.

O registro global de dialetos afeta o registry do processo inteiro. Em bibliotecas, parâmetros locais explícitos ou nomes de dialeto cuidadosamente namespaced podem ser mais fáceis de entender.

## 21. Limite o tamanho de campos em entrada não confiável ou restrita

`csv.field_size_limit()` retorna o tamanho máximo de campo atual do parser. Passar um argumento altera esse limite para o processo.

```python
import csv
from io import StringIO

previous_limit = csv.field_size_limit()

try:
    csv.field_size_limit(8)
    try:
        list(csv.reader(StringIO("value\n123456789\n", newline="")))
    except csv.Error:
        print("Field limit enforced")
finally:
    csv.field_size_limit(previous_limit)
```

Um limite de campo é uma fronteira de recursos, não uma solução de segurança completa. O documento ainda pode conter muitas linhas, e a validação posterior ainda pode consumir tempo ou memória.

Como o limite é global ao processo, restaure-o ao fazer uma alteração temporária em código reutilizável.

## 22. Encoding pertence à fronteira do arquivo de texto

O módulo `csv` trabalha com strings. `open()` decide como bytes viram texto.

Para CSV UTF-8 comum:

```python
with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Alguns arquivos UTF-8 produzidos por planilhas começam com BOM. Quando isso fizer parte do contrato externo, `encoding="utf-8-sig"` pode consumi-lo:

```python
import csv

with open(
    "records.csv",
    encoding="utf-8-sig",
    newline="",
) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Não escolha `utf-8-sig` automaticamente para todo CSV. Encoding é uma decisão de interface.

## 23. A conversão padrão de `None` do writer perde informação

No `csv.writer` comum, `None` é escrito como string vazia. Isso facilita exports de bancos de dados, mas a transformação não é reversível por padrão.

Se `None` e `""` possuem significados diferentes na aplicação, escolha uma política de representação como:

```text
um sentinela acordado
uma coluna separada de presença
QUOTE_NOTNULL no Python 3.12+
outro formato com semântica explícita de null
```

A escolha correta depende dos requisitos de interoperabilidade.

## 24. Quoting CSV não define a política de execução da planilha

Quoting protege a sintaxe CSV. Ele não torna automaticamente um valor inofensivo quando outro programa interpreta a célula depois de abrir o arquivo.

Se dados controlados por usuários forem abertos em software de planilha, fórmulas e outras interpretações específicas do consumidor precisam de uma política de segurança de saída separada.

Trate como outra fronteira:

```text
sintaxe CSV válida
        ≠
comportamento seguro em todo consumidor CSV
```

## 25. Faça streaming de arquivos grandes em vez de criar listas desnecessárias

Readers são iteradores. É possível processar registros um por vez:

```python
import csv

with open("records.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        process_name = row["name"].strip()
        print(process_name)
```

Isso pode manter o uso de memória muito menor que `list(reader)` em arquivos grandes.

Streaming não remove a necessidade de limites. Ainda podem ser necessárias políticas para tamanho do arquivo, quantidade de linhas, comprimento dos campos e tempo de processamento.

## 26. `writerows()` aceita um iterável de linhas

Um writer pode consumir um generator:

```python
import csv
from io import StringIO

rows = (
    [name, score]
    for name, score in [("Ana", 88), ("Bob", 91)]
)

stream = StringIO(newline="")
writer = csv.writer(stream, lineterminator="\n")
writer.writerows(rows)

print(stream.getvalue())
```

Isso é útil para pipelines que transformam registros de forma lazy.

Lembre que o writer ainda converte valores de campos não string segundo as regras do módulo. Streaming muda comportamento de memória, não o significado do schema.

## 27. Um round trip CSV não preserva tipos Python arbitrários

Com o par reader/writer comum:

```text
Python int 88
   ↓ writer
campo CSV 88
   ↓ reader
Python str "88"
```

`QUOTE_NONNUMERIC`, `QUOTE_NOTNULL` e `QUOTE_STRINGS` alteram partes específicas desse comportamento, mas nenhum transforma CSV em um formato geral de serialização de objetos Python.

Se reconstrução exata de tipos for importante, defina-a coluna por coluna.

## 28. Quando CSV é uma boa escolha

CSV é útil quando:

- os dados são naturalmente tabulares;
- as linhas compartilham um contrato estável de colunas;
- pessoas ou ferramentas de planilha precisam inspecionar os dados;
- interoperabilidade com sistemas que já trocam texto delimitado importa;
- processamento em streaming linha por linha é valioso.

## 29. Quando CSV é uma escolha ruim

Considere outro formato quando:

- os dados são profundamente aninhados;
- null versus string vazia precisa ser inequívoco sem dialeto personalizado;
- tipos ricos precisam fazer round trip diretamente;
- schemas por registro variam bastante;
- dados binários são um campo de primeira classe;
- é necessário um envelope ou modelo de metadados fortemente padronizado.

## 30. Erros comuns

### Erro 1: usar `split(",")`

```python
line = 'Ana,"A,B"'
print(line.split(","))
```

Isso ignora regras de quoting. Use `csv.reader()`.

### Erro 2: omitir `newline=""` em arquivos CSV reais

Deixe o módulo `csv` tratar novas linhas CSV.

### Erro 3: presumir que todo arquivo `.csv` usa vírgulas

Confirme ou configure o dialeto.

### Erro 4: tratar cabeçalho como validação de schema

Valide largura das linhas e semântica dos valores separadamente.

### Erro 5: esperar round trip automático de tipos numéricos

O reader padrão retorna strings.

### Erro 6: confiar em `Sniffer` como prova

Ele é heurístico.

### Erro 7: ignorar silenciosamente chaves extras de dicionário

Use `extrasaction="raise"` a menos que a omissão seja intencional.

### Erro 8: presumir que saída entre aspas é segura em qualquer planilha

Sintaxe CSV e comportamento de execução da planilha são fronteiras diferentes.

## 31. Exemplo prático: round trip com dialeto de ponto e vírgula

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    delimiter=";",
    quoting=csv.QUOTE_MINIMAL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", "uses;semicolon"])
writer.writerow(["Bob", 'says "hello"'])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    delimiter=";",
)
print(list(reader))
```

Versão executável: [`examples/semicolon_dialect.py`](examples/semicolon_dialect.py).

## 32. Exemplo prático: validar contrato de linhas em dicionário

```python
import csv
from io import StringIO

EXPECTED_FIELDS = ["name", "score"]

text = "name,score\nAna,88\nBob,91\n"
reader = csv.DictReader(StringIO(text, newline=""))

if reader.fieldnames != EXPECTED_FIELDS:
    raise ValueError("unexpected header")

for row in reader:
    if None in row:
        raise ValueError("row has extra fields")
    if any(value is None for value in row.values()):
        raise ValueError("row has missing fields")
    print(row)
```

Versão executável: [`examples/dict_contract.py`](examples/dict_contract.py).

## 33. Exemplo prático: preservar `None` versus string vazia

```python
import csv
from io import StringIO

stream = StringIO(newline="")
writer = csv.writer(
    stream,
    quoting=csv.QUOTE_NOTNULL,
    lineterminator="\n",
)
writer.writerow(["name", "note"])
writer.writerow(["Ana", None])
writer.writerow(["Bob", ""])

text = stream.getvalue()
print(text, end="")

reader = csv.reader(
    StringIO(text, newline=""),
    quoting=csv.QUOTE_NOTNULL,
)
print(list(reader))
```

Versão executável: [`examples/quote_notnull.py`](examples/quote_notnull.py).

## 34. Exemplo prático: rejeitar sintaxe CSV malformada

```python
import csv
from io import StringIO

text = 'name,score\n"Ana,88\n'

try:
    list(csv.reader(StringIO(text, newline=""), strict=True))
except csv.Error:
    print("Malformed CSV rejected")
```

Versão executável: [`examples/strict_csv.py`](examples/strict_csv.py).

## 35. Exercício

Crie `decode_inventory_csv(text)` para este contrato:

```text
cabeçalho: item,quantity,active
delimitador: vírgula
quoting: quoting CSV normal
conceito de nível superior: uma linha por item de estoque
```

Requisitos:

1. faça parsing com `csv.DictReader`;
2. exija a ordem exata de cabeçalho `item`, `quantity`, `active`;
3. rejeite linhas com campos extras ou ausentes;
4. exija que `item` seja string não vazia depois de remover whitespace das bordas;
5. converta `quantity` com `int()` e exija valor zero ou maior;
6. aceite apenas `true` ou `false` em `active`, sem diferenciar maiúsculas e minúsculas;
7. retorne dicionários validados em que `quantity` seja `int` e `active` seja `bool`;
8. rejeite sintaxe CSV malformada com erro claro no nível da aplicação.

Depois crie `encode_inventory_csv(rows)` que escreva a mesma ordem de campos com:

```text
escrita CSV consciente de newline
lineterminator explícito
extrasaction="raise"
```

Teste dados válidos e também:

```text
cabeçalho incorreto
campo extra
campo ausente
inteiro inválido
quantidade negativa
booleano inválido
vírgula entre aspas dentro de item
```

O objetivo é tornar a fronteira explicável, não apenas fazer o happy path funcionar.

## 36. Referência rápida

| Necessidade | Ferramenta / política |
|---|---|
| Ler linhas | `csv.reader(...)` |
| Escrever linhas | `csv.writer(...)` |
| Ler linhas mapeadas por cabeçalho | `csv.DictReader(...)` |
| Escrever dicionários | `csv.DictWriter(...)` |
| Abrir arquivos CSV reais | `newline=""` |
| Escolher delimitador | `delimiter=";"` ou outro valor de um caractere |
| Escolher caractere de aspas | `quotechar='"'` |
| Quoting mínimo | `csv.QUOTE_MINIMAL` |
| Colocar todos os campos entre aspas | `csv.QUOTE_ALL` |
| Converter campos sem aspas para `float` na leitura | `csv.QUOTE_NONNUMERIC` |
| Preservar campo vazio sem aspas como `None` | `csv.QUOTE_NOTNULL` |
| Colocar strings entre aspas com conversão numérica de valores sem aspas | `csv.QUOTE_STRINGS` |
| Desativar processamento de aspas | `csv.QUOTE_NONE` |
| Escapar caracteres especiais | `escapechar=...` |
| Final de linha explícito do writer | `lineterminator="\n"` |
| Rejeitar sintaxe CSV malformada | `strict=True` |
| Erro do parser/formatter CSV | `csv.Error` |
| Inspecionar progresso de linha física | `reader.line_num` |
| Estimar dialeto | `csv.Sniffer().sniff(...)` |
| Estimar presença de cabeçalho | `csv.Sniffer().has_header(...)` |
| Registrar dialeto reutilizável | `csv.register_dialect(...)` |
| Limitar tamanho de campo do parser | `csv.field_size_limit(...)` |
| Rejeitar chaves desconhecidas no DictWriter | `extrasaction="raise"` |

## 37. Checklist de design

Antes de publicar ou consumir uma interface CSV, pergunte:

```text
Qual delimitador é exigido?
Quais regras de aspas e escape são exigidas?
Qual final de linha os writers produzirão?
Qual encoding de caracteres transporta o texto?
Existe cabeçalho e sua ordem é significativa?
Como campos extras ou ausentes são tratados?
Como null e string vazia são diferenciados?
Quais colunas exigem conversão de tipos?
Como linhas malformadas são reportadas?
Quais limites de tamanho se aplicam?
Sniffing de dialeto é permitido ou o formato deve ser explícito?
Software de planilha interpretará o conteúdo das células exportadas?
```

Quando essas respostas são explícitas, CSV deixa de ser "apenas texto separado por vírgulas" e vira um contrato de interface testável.

## Referências

- [Documentação Python 3.14: `csv` — CSV File Reading and Writing](https://docs.python.org/3.14/library/csv.html)
- [PEP 305: CSV File API](https://peps.python.org/pep-0305/)
- [RFC 4180: Common Format and MIME Type for CSV Files](https://www.rfc-editor.org/rfc/rfc4180)

## Próximo capítulo

Continue com o **Capítulo 05: `logging`** quando estiver disponível. Ele aprofundará hierarquias de loggers, handlers, formatters, níveis, configuração e logging de aplicação versus biblioteca.

[← Anterior: Capítulo 03 · `json`](../03-json/README.pt-BR.md)
