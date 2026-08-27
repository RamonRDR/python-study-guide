<div align="center">

# Trabalhando com TXT, CSV e JSON

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Erros, Arquivos e Módulos](../README.pt-BR.md) · [← Anterior: Abrindo Arquivos com Segurança com `open()` e `with`](../03-open-and-with/README.pt-BR.md)

Abrir um arquivo com segurança é apenas metade do trabalho. Um programa também precisa entender **como os dados dentro desse arquivo estão organizados**.

Um arquivo `.txt` pode conter um registro por linha, um CSV pode representar linhas e colunas e um documento JSON pode representar objetos e arrays aninhados. A extensão é uma pista útil, mas o contrato real é o formato dos dados e as regras usadas para interpretá-los.

Este capítulo apresenta registros de texto simples, o módulo `csv` do Python e o módulo `json` do Python. O objetivo não é memorizar todas as opções. O objetivo é escolher um formato deliberadamente, usar o parser responsável por esse formato e manter parsing separado de validação e lógica da aplicação.

**Tempo estimado de estudo:** 120–160 minutos.

**Requisito de Python:** Python 3.10 ou mais recente. O comportamento de `csv` e `json` ensinado aqui foi verificado na documentação oficial do Python 3.14.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar a diferença entre uma extensão de arquivo e um formato de dados;
- usar texto simples quando um contrato orientado por linhas for suficiente;
- explicar por que CSV não deve ser interpretado com um `split(",")` ingênuo;
- ler e escrever linhas CSV com o módulo `csv` da biblioteca padrão;
- usar `DictReader` e `DictWriter` quando colunas nomeadas melhorarem a clareza;
- explicar por que valores CSV normalmente chegam como strings e convertê-los deliberadamente;
- abrir arquivos CSV com `newline=""` e uma codificação de texto conhecida;
- distinguir objetos, arrays, strings, números, booleanos e `null` em JSON;
- usar `json.load()`, `json.loads()`, `json.dump()` e `json.dumps()` corretamente;
- tratar JSON inválido com `json.JSONDecodeError` quando houver recuperação significativa;
- distinguir parsing de validação;
- escolher TXT, CSV ou JSON de acordo com a forma e o contrato dos dados;
- evitar parsers feitos à mão quando já existe um parser específico para o formato.

## 1. Um arquivo é um contêiner; um formato é um contrato

O Capítulo 03 se concentrou em abrir, ler, escrever e fechar arquivos. Este capítulo acrescenta outra pergunta:

```text
bytes no armazenamento
      ↓ decodificação
texto no Python
      ↓ parsing
valores Python estruturados
      ↓ validação
valores nos quais o programa confia
```

Abrir um arquivo responde **de onde os dados vêm**. Fazer parsing responde **o que o texto significa**.

São responsabilidades relacionadas, mas não são a mesma responsabilidade.

## 2. A extensão não interpreta magicamente o conteúdo

Um nome como `topics.txt`, `scores.csv` ou `profile.json` comunica intenção a pessoas e ferramentas. Python não inspeciona automaticamente a extensão e transforma o conteúdo na estrutura correspondente.

Você escolhe a operação apropriada:

```python
with open("topics.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

ou um parser específico do formato, como `csv.reader()` ou `json.load()`.

## 3. TXT significa texto, não um único esquema universal

`.txt` normalmente significa texto simples, mas não existe um formato universal de registros TXT.

Todos estes podem ser contratos válidos de arquivo de texto:

```text
Functions
Exceptions
Files
```

```text
topic=Functions
level=2
active=true
```

```text
2026-08-26 | Files | completed
```

O programa e quem produz o arquivo precisam concordar sobre as regras.

## 4. Um contrato TXT simples pode ter um registro por linha

Se cada linha for um valor de texto independente, o formato pode permanecer intencionalmente simples:

```python
with open("topics.txt", "r", encoding="utf-8") as file:
    topics = [line.rstrip("\n") for line in file]
```

Aqui o parser é pequeno porque o contrato é pequeno: cada linha física representa um tópico.

## 5. Preserve espaços significativos deliberadamente

Evite usar `strip()` automaticamente quando espaços puderem fazer parte dos dados.

```python
clean_line = line.rstrip("\n")
```

Isso remove somente o caractere de nova linha definido pela decisão de formato acima.

Se o seu formato definir outras regras de normalização, aplique-as explicitamente em vez de tratar todo espaço em branco como descartável.

## 6. Separadores personalizados simples ainda formam um formato que precisa ser definido

Suponha que um arquivo controlado contenha um par chave-valor por linha:

```text
topic=Files
level=2
```

Um parser deliberado pode dividir apenas no primeiro separador:

```python
key, value = line.rstrip("\n").split("=", 1)
```

O `1` importa se o próprio valor puder conter `=` depois.

Quando aparecem escape, aspas, colunas opcionais, dados aninhados ou muitos casos de borda, um formato padrão normalmente é melhor do que fazer crescer uma minilinguagem privada.

## 7. CSV representa registros tabulares

CSV é útil quando os dados naturalmente se parecem com linhas que possuem as mesmas colunas:

```text
topic,score,status
Functions,91,complete
Files,88,complete
JSON,79,review
```

O nome significa valores separados por vírgula, mas dados CSV reais podem usar delimitadores e regras de aspas diferentes. Python modela essas escolhas por dialetos e opções de formatação CSV.

## 8. Não interprete CSV com `split(",")`

Isto parece tentador:

```python
columns = line.split(",")
```

mas um campo válido pode conter uma vírgula quando estiver entre aspas:

```text
topic,note
Files,"Read, write, and validate"
```

Um parser CSV entende delimitadores, aspas, novas linhas embutidas e outras regras do formato. Um simples split de string não entende.

## 9. Importe o módulo `csv` da biblioteca padrão

O módulo faz parte da biblioteca padrão do Python:

```python
import csv
```

Ele fornece APIs orientadas por linhas, como:

- `csv.reader()`;
- `csv.writer()`;
- `csv.DictReader()`;
- `csv.DictWriter()`.

Este capítulo ensina o núcleo prático. Uma fase posterior sobre Biblioteca Padrão poderá revisitar opções mais amplas e personalizações do módulo.

## 10. Abra arquivos CSV com `newline=""`

Quando um objeto arquivo é passado ao módulo `csv`, a documentação oficial recomenda abri-lo com `newline=""` para que o próprio módulo CSV faça corretamente o tratamento de novas linhas.

```python
with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
```

Mantenha `encoding="utf-8"` explícito quando UTF-8 fizer parte do contrato dos dados.

## 11. `csv.reader()` retorna linhas como listas

Um reader básico trata cada registro como uma sequência de campos:

```python
import csv

with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Com o exemplo anterior, as linhas são listas como:

```text
['topic', 'score', 'status']
['Functions', '91', 'complete']
```

Observe que `91` é uma string.

## 12. CSV normalmente não infere os tipos da sua aplicação

Por padrão, `csv.reader()` retorna campos como strings. `DictReader` também fornece valores string para campos comuns.

Seu programa precisa decidir quais conversões fazem parte do contrato:

```python
score = int(row[1])
```

A conversão pode falhar, portanto esta também é uma fronteira de validação.

## 13. `csv.writer()` formata as linhas para você

Não construa registros CSV manualmente juntando valores com vírgulas.

```python
import csv

rows = [
    ["topic", "score"],
    ["Functions", 91],
    ["Files", 88],
]

with open("scores.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

O writer aplica as regras configuradas de aspas e delimitadores CSV.

## 14. `DictReader` dá nomes às colunas

Quando a primeira linha é um cabeçalho, `DictReader` pode tornar o código mais fácil de ler:

```python
import csv

with open("scores.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["topic"], row["score"])
```

Os valores do cabeçalho tornam-se chaves do dicionário.

## 15. Nomes de cabeçalho fazem parte do contrato CSV

Código que espera `row["score"]` depende de uma coluna chamada exatamente `score`.

Se um produtor alterar o cabeçalho para `final_score`, seu parser poderá levantar `KeyError` ou sua validação poderá rejeitar o registro.

Trate nomes de colunas, requisitos de ordem, escolha de delimitador e campos obrigatórios como decisões explícitas de interface.

## 16. `DictWriter` torna explícitas as colunas de saída

`DictWriter` exige `fieldnames`, que definem a ordem das colunas:

```python
import csv

fieldnames = ["topic", "score", "status"]

with open("scores.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {"topic": "Files", "score": 88, "status": "complete"}
    )
```

Isso costuma ser mais claro que índices posicionais quando a tabela possui colunas nomeadas.

## 17. Delimitadores variam

Vírgula é o delimitador padrão do dialeto comum no estilo Excel, mas alguns contratos usam ponto e vírgula, tabulação ou outros delimitadores.

```python
reader = csv.reader(file, delimiter=";")
```

Não adivinhe com base em hábitos regionais nem em uma única linha de exemplo. Conheça ou documente o contrato sempre que possível.

## 18. Aspas protegem campos com caracteres especiais

O writer CSV pode colocar entre aspas campos que contenham delimitadores, caracteres de aspas ou terminadores de linha.

```python
import csv

row = ["Files", "Read, write, and validate"]
```

Com regras normais de quoting, a vírgula dentro da observação pode continuar fazendo parte de um único campo.

Esse é outro motivo para deixar `csv` gerar o texto serializado.

## 19. Parsing CSV e validação CSV são etapas diferentes

Uma linha pode ser CSV sintaticamente válido e ainda violar as regras da aplicação:

```text
topic,score
Files,one hundred
```

O parser CSV consegue retornar corretamente `"one hundred"`. Depois, sua aplicação decide se `score` precisa ser inteiro.

```text
texto CSV
   ↓ parser
campos da linha
   ↓ conversão + validação
registro confiável
```

## 20. JSON representa valores estruturados

JSON é útil para objetos e arrays aninhados, e não apenas tabelas planas.

```json
{
  "topic": "Files",
  "score": 88,
  "tags": ["io", "formats"],
  "complete": true
}
```

JSON é um formato de intercâmbio de dados. Ele lembra alguns literais Python, mas não é código-fonte Python.

## 21. Valores JSON centrais mapeiam para valores Python conhecidos

Um mapeamento útil para iniciantes é:

| JSON | Valor Python típico |
|---|---|
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` ou `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

O mapeamento é próximo o suficiente para parecer familiar, mas as sintaxes não são intercambiáveis.

## 22. Sintaxe JSON não é sintaxe de literal Python

Estes tokens JSON são minúsculos:

```json
{"active": true, "result": null}
```

Python usa:

```python
data = {"active": True, "result": None}
```

Não interprete JSON com `eval()`.

## 23. `json.loads()` interpreta uma string JSON

O `s` de `loads` é uma boa ajuda de memória para trabalhar com um valor string:

```python
import json

text = '{"topic": "Files", "score": 88}'
data = json.loads(text)

print(data["topic"])
```

`loads()` retorna valores Python criados a partir do documento JSON.

## 24. `json.dumps()` cria uma string JSON

`dumps()` serializa um valor Python compatível para uma string formatada como JSON:

```python
import json

data = {"topic": "Files", "score": 88}
text = json.dumps(data)

print(text)
```

Serialização significa converter um valor em memória para uma representação adequada a armazenamento ou transporte.

## 25. `json.load()` lê JSON de um objeto arquivo ou similar

Quando o documento JSON já está em um arquivo de texto, use `load()` com o arquivo aberto:

```python
import json

with open("profile.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

`open()` gerencia o acesso ao arquivo. `json.load()` interpreta o texto em valores Python.

## 26. `json.dump()` escreve um valor JSON em um objeto arquivo ou similar

```python
import json

data = {"topic": "Files", "complete": True}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
```

`json.dump()` escreve strings no alvo. No uso comum com arquivo, abra esse alvo em modo texto.

## 27. `ensure_ascii=False` mantém texto não ASCII legível

Por padrão, o encoder JSON escapa caracteres não ASCII. Quando um arquivo UTF-8 é o contrato explícito, `ensure_ascii=False` pode manter esses caracteres legíveis no documento serializado:

```python
import json

data = {"language": "Português"}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)
```

A escolha afeta a representação, não o valor da string Python depois de uma decodificação correta.

## 28. `indent` melhora a leitura humana

JSON formatado é útil para configuração, exemplos e arquivos inspecionados manualmente:

```python
json.dump(data, file, ensure_ascii=False, indent=2)
```

A indentação aumenta o tamanho do arquivo, então saída compacta pode ser melhor em algumas interfaces voltadas a máquinas. Escolha de acordo com o contrato, não apenas pela aparência.

## 29. JSON inválido levanta `JSONDecodeError`

Erros de sintaxe em um documento JSON são reportados com `json.JSONDecodeError`, uma subclasse de `ValueError`:

```python
import json

text = '{"topic": "Files",}'

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")
```

Capture a exceção somente onde o programa tiver uma política útil de recuperação ou relatório.


O decoder do Python também possui uma extensão deliberada de interoperabilidade: por padrão, `json.loads()` aceita `NaN`, `Infinity` e `-Infinity` e os converte em valores de ponto flutuante, embora esses tokens não sejam JSON válido segundo a especificação interoperável de JSON. Portanto, uma chamada bem-sucedida de `json.loads()` **não** prova, por si só, que a entrada está em conformidade com o padrão JSON.

Quando a conformidade estrita com o padrão fizer parte do contrato, forneça `parse_constant` com um callback que rejeite esses valores explicitamente:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


text = '{"value": NaN}'

try:
    data = json.loads(text, parse_constant=reject_nonstandard_constant)
except ValueError as error:
    print(error)
```

Aqui, o `ValueError` é levantado deliberadamente pelo callback. `JSONDecodeError` continua representando erros comuns de sintaxe JSON, como a vírgula final do exemplo anterior.


O encoder tem a preocupação de interoperabilidade correspondente no caminho inverso. Por padrão, `json.dumps()` e `json.dump()` usam `allow_nan=True`, então o Python pode serializar valores de ponto flutuante não finitos como `NaN`, `Infinity` e `-Infinity`. Esses tokens estão fora do JSON compatível com o padrão e podem ser rejeitados por consumidores estritos.

Quando a saída JSON estrita fizer parte do contrato, defina `allow_nan=False`:

```python
import json

data = {"value": float("nan")}

try:
    text = json.dumps(data, allow_nan=False)
except ValueError as error:
    print(error)
```

Com `allow_nan=False`, o Python levanta `ValueError` em vez de emitir uma constante JSON não padronizada. A mesma opção está disponível em `json.dump()`.

## 30. Nem todo objeto Python é serializável para JSON por padrão

O encoder padrão lida com estruturas comuns compatíveis com JSON, mas objetos arbitrários não são convertidos automaticamente.

```python
import json

values = {1, 2, 3}
json.dumps(values)
```

Um `set` não é um tipo JSON, então isso levanta `TypeError` sem uma transformação ou personalização deliberada.

Para código de iniciante, uma transformação explícita costuma ser mais clara que um encoder personalizado.

## 31. Um round trip JSON pode alterar estruturas específicas do Python

Arrays JSON voltam como listas. Portanto, uma tupla serializada como array não retorna automaticamente como tupla:

```python
import json

original = ("Files", "JSON")
restored = json.loads(json.dumps(original))

print(type(restored).__name__)
```

Saída:

```text
list
```

JSON representa tipos JSON, não todas as distinções do modelo de objetos do Python.

## 32. Chaves de objetos JSON são strings no modelo de dados

O encoder do Python aceita algumas chaves básicas que não são strings e as converte para JSON, mas nomes de membros de objetos JSON são strings.

Portanto, um dicionário com chaves não string pode não ser igual depois de um round trip dump/load.

Se o tipo da chave importar para a aplicação, projete essa representação explicitamente.

## 33. Não acrescente documentos JSON independentes com chamadas repetidas a `dump()`

JSON não é um protocolo enquadrado. Escrever dois valores JSON de topo em sequência não cria automaticamente um único documento JSON válido:

```python
json.dump(first, file)
json.dump(second, file)
```

Se você precisa de vários registros, escolha um contêiner definido, como um único array JSON, ou outro formato explicitamente especificado.

## 34. Parsing não é validação

Um parser responde se o texto segue a sintaxe do formato e reconstrói valores.

Validação responde se esses valores satisfazem as regras do programa.

```python
import json

data = json.loads('{"score": -50}')

if not 0 <= data["score"] <= 100:
    raise ValueError("score must be between 0 and 100")
```

O JSON é sintaticamente válido. O valor da aplicação é inválido.

## 35. Separe I/O, parsing e validação quando o programa crescer

Programas pequenos podem manter essas etapas próximas, mas funções claras ajudam quando a complexidade aumenta:

```text
ler bytes/texto
     ↓
interpretar formato
     ↓
validar valores
     ↓
transformar/usar dados
```

Essa separação facilita identificar se uma falha veio do acesso ao arquivo, da sintaxe do formato, da conversão de tipos ou de uma regra da aplicação.

## 36. Exemplo prático: um registro TXT por linha

O exemplo executável usa um diretório temporário apenas para manter os testes do repositório limpos:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "topics.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Functions\n")
        file.write("Files\n")
        file.write("JSON\n")

    with open(path, "r", encoding="utf-8") as file:
        topics = [line.rstrip("\n") for line in file]

    print(topics)
```

Saída:

```text
['Functions', 'Files', 'JSON']
```

Versão executável: [`examples/text_records.py`](examples/text_records.py).

## 37. Exemplo prático: dicionários CSV e conversão explícita

```python
import csv
import os
import tempfile


records = [
    {"topic": "Functions", "score": 91, "note": "Clear flow"},
    {"topic": "Files", "score": 88, "note": "Read, write, validate"},
]

with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "scores.csv")
    fieldnames = ["topic", "score", "note"]

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            score = int(row["score"])
            print(f'{row["topic"]}: {score} - {row["note"]}')
```

Saída:

```text
Functions: 91 - Clear flow
Files: 88 - Read, write, validate
```

Versão executável: [`examples/csv_records.py`](examples/csv_records.py).

## 38. Exemplo prático: escrever e ler um documento JSON

```python
import json
import os
import tempfile


profile = {
    "topic": "Files",
    "score": 88,
    "tags": ["io", "formats"],
    "complete": True,
}

with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "profile.json")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)

    print(restored["topic"])
    print(restored["tags"])
    print(restored["complete"])
```

Saída:

```text
Files
['io', 'formats']
True
```

Versão executável: [`examples/json_document.py`](examples/json_document.py).

## 39. Exemplo prático: tratar JSON inválido deliberadamente

```python
import json


text = '{"topic": "Files",}'

try:
    data = json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")
else:
    print(data)
```

Saída:

```text
Invalid JSON
```

Versão executável: [`examples/handle_invalid_json.py`](examples/handle_invalid_json.py).

## 40. Erro comum: tratar todo arquivo de texto como CSV

Um arquivo de texto com prosa, linhas de log ou um valor por linha não vira CSV apenas porque teoricamente seria possível separar campos.

Use CSV quando o contrato for realmente tabular e suas regras de aspas e delimitadores forem apropriadas.

Use texto mais simples quando texto simples for o formato real.

## 41. Erro comum: construir JSON manualmente

Evite este estilo:

```python
text = '{"name": "' + name + '", "score": ' + str(score) + '}'
```

Escapar aspas, barras invertidas, caracteres de controle, estruturas aninhadas, booleanos e `null` rapidamente se torna sujeito a erros.

Construa valores Python e deixe `json.dumps()` ou `json.dump()` serializá-los.

## 42. Erro comum: confiar automaticamente nos dados interpretados

Parsing bem-sucedido não prova que campos obrigatórios existem, tipos atendem ao contrato da aplicação, faixas numéricas são válidas ou strings são aceitáveis.

Trate dados de arquivos e rede como entrada:

```text
parsing bem-sucedido
      ≠
seguro e válido para todo uso
```

Valide as propriedades das quais seu programa realmente depende.

## 43. Escolhendo entre TXT, CSV e JSON

| Forma ou necessidade | Boa escolha inicial |
|---|---|
| Linhas simples e legíveis por pessoas | TXT |
| Linhas planas com colunas consistentes | CSV |
| Objetos aninhados, arrays, booleanos e nulls | JSON |
| Dados já governados por um contrato externo de formato | Use o formato exigido |

A extensão não é o fator decisivo. O modelo dos dados e o contrato de interoperabilidade são.

## 44. Quando evitar inventar um formato de texto personalizado

Um pequeno formato privado pode funcionar em uma tarefa minúscula e controlada. Ele se torna arriscado quando você começa a adicionar:

- regras de escape;
- campos opcionais ou repetidos;
- delimitadores entre aspas;
- valores aninhados;
- versionamento;
- vários produtores e consumidores independentes.

Nesse ponto, um formato padrão normalmente oferece parsers testados e interoperabilidade mais clara.

## 45. Exercício

Crie um programa chamado `study_export.py` com estes requisitos:

1. Comece com uma lista de dicionários contendo `topic`, `score` e `complete`.
2. Escreva os registros em `study.csv` com `csv.DictWriter`.
3. Reabra o CSV com `csv.DictReader`, converta `score` para `int` e converta `complete` de volta para `bool` com um mapeamento explícito como `{"True": True, "False": False}`; rejeite textos inesperados em vez de usar `bool()` diretamente.
4. Construa uma nova lista contendo os registros convertidos.
5. Escreva essa lista em `study.json` usando `json.dump()` com UTF-8, `ensure_ascii=False` e `indent=2`.
6. Reabra o JSON com `json.load()`.
7. Exiba somente os tópicos cujo score seja pelo menos 80.
8. Use `with` em toda operação real de arquivo.

Perguntas extras:

- Por que `newline=""` é usado no arquivo CSV?
- Por que o score do CSV precisa ser convertido explicitamente?
- Por que `bool(row["complete"])` estaria errado quando o texto do CSV fosse `"False"`?
- Qual exceção uma sintaxe JSON inválida levanta?
- Por que `split(",")` seria inseguro para uma observação contendo vírgulas?
- Qual etapa é parsing e qual etapa é validação da aplicação?

## 46. Checklist de revisão

Antes de continuar, confirme que você consegue responder sem chutar:

- Qual é a diferença entre uma extensão de arquivo e um formato de dados?
- `.txt` define uma única estrutura universal de registros?
- Por que CSV não deve ser interpretado com um split ingênuo por vírgula?
- Por que `newline=""` é recomendado quando um objeto arquivo é usado com `csv`?
- O que as linhas de `csv.reader()` contêm por padrão?
- Por que `DictReader` pode ser mais claro que índices numéricos de coluna?
- Qual é a diferença entre `json.load()` e `json.loads()`?
- Qual é a diferença entre `json.dump()` e `json.dumps()`?
- Qual valor JSON corresponde a `None` do Python?
- Qual exceção indica sintaxe JSON inválida?
- Todo objeto Python pode ser serializado automaticamente para JSON?
- Por que parsing e validação são conceitos separados?

## 47. Referência rápida

| Necessidade | Padrão |
|---|---|
| Ler texto UTF-8 simples | `open(path, "r", encoding="utf-8")` |
| Ler linhas CSV | `csv.reader(file)` |
| Escrever linhas CSV | `csv.writer(file)` |
| Ler CSV com colunas nomeadas | `csv.DictReader(file)` |
| Escrever CSV com colunas nomeadas | `csv.DictWriter(file, fieldnames=...)` |
| Abrir um objeto arquivo para CSV | `open(path, ..., encoding="utf-8", newline="")` |
| Interpretar string JSON | `json.loads(text)` |
| Criar string JSON | `json.dumps(data)` |
| Interpretar arquivo JSON | `json.load(file)` |
| Escrever arquivo JSON | `json.dump(data, file)` |
| Preservar Unicode legível na saída | `ensure_ascii=False` |
| Formatar JSON | `indent=2` |
| Sintaxe JSON inválida | `json.JSONDecodeError` |
| Objeto incompatível com JSON na serialização | `TypeError` |

Um pipeline padrão útil é:

```text
abrir com segurança
    ↓
interpretar com o parser do formato
    ↓
converter e validar valores da aplicação
    ↓
usar ou transformar dados confiáveis
```

## O que vem depois

O Capítulo 04 acrescenta formatos comuns de dados textuais à base de gerenciamento de arquivos. O último capítulo da Fase 7, **Imports, Módulos e Pacotes**, passará de dados armazenados em vários arquivos para código Python organizado em vários arquivos.

```text
exceções
    ↓
sinalização deliberada de exceções
    ↓
tempo de vida seguro de arquivos
    ↓
fronteiras de dados TXT / CSV / JSON
    ↓
imports / módulos / pacotes
```

## Referências oficiais

- Documentação `csv` do Python 3.14: <https://docs.python.org/3.14/library/csv.html>
- Documentação `json` do Python 3.14: <https://docs.python.org/3.14/library/json.html>
- Tutorial do Python 3.14, Reading and Writing Files: <https://docs.python.org/3.14/tutorial/inputoutput.html#reading-and-writing-files>
- Tutorial do Python 3.14, Saving structured data with `json`: <https://docs.python.org/3.14/tutorial/inputoutput.html#saving-structured-data-with-json>
