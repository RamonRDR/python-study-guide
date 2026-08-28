<div align="center">

# Controlando Contratos de Serialização e Decodificação JSON

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Biblioteca Padrão](../README.pt-BR.md) · [← Anterior: Trabalhando com Datas e Cálculos de Tempo Usando `datetime`](../02-datetime/README.pt-BR.md)

A Phase 7 apresentou JSON como formato de dados estruturados e ensinou a diferença prática entre `load()`, `loads()`, `dump()` e `dumps()`. Este capítulo desce uma camada a mais.

O módulo `json` não serve apenas para ler e escrever arquivos `.json`. Ele também é uma ferramenta de fronteira. Suas opções decidem quais valores Python são aceitos, como números são reconstruídos, se valores fora do padrão são tolerados, como tipos personalizados são representados, como nomes duplicados em objetos são tratados e quão estável é a representação serializada.

O objetivo é transformar "JSON funciona" em uma pergunta mais precisa:

```text
Qual contrato JSON este programa aceita e produz?
```

**Tempo estimado de estudo:** 120–160 minutos.

**Requisito de Python:** Python 3.10 ou mais recente para as APIs centrais. O comando direto `python -m json` mostrado mais adiante está disponível no Python 3.14; versões suportadas anteriores podem usar `python -m json.tool`.

**Base de documentação:** comportamento e exemplos foram conferidos na documentação oficial do módulo `json` do Python 3.14.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- tratar serialização JSON como contrato de interface e não apenas como operação de arquivo;
- distinguir texto JSON de codificação em bytes;
- produzir saída estável com `sort_keys` quando ordenação determinística for útil;
- controlar espaços com `indent` e `separators`;
- explicar o que `ensure_ascii` altera e o que ele não altera;
- rejeitar valores de ponto flutuante não finitos com `allow_nan=False`;
- rejeitar constantes não padronizadas do decoder do Python com `parse_constant`;
- decodificar números JSON com funções personalizadas como `decimal.Decimal`;
- reconhecer limites de interoperabilidade envolvendo faixa e precisão numérica;
- entender por que nomes de membros de objetos JSON são strings;
- evitar descartar silenciosamente chaves incompatíveis com `skipkeys=True` quando essa política não for intencional;
- serializar valores Python personalizados selecionados com `default` ou `JSONEncoder`;
- reconstruir representações selecionadas com `object_hook`;
- inspecionar pares nome-valor ordenados com `object_pairs_hook`;
- detectar nomes duplicados em objetos JSON quando unicidade fizer parte do contrato;
- manter a verificação de referências circulares habilitada salvo motivo específico;
- usar detalhes de `JSONDecodeError` para diagnósticos úteis;
- limitar entrada JSON não confiável de acordo com a fronteira controlada;
- usar a interface de linha de comando JSON do Python para validação e formatação;
- distinguir documentos JSON comuns de formatos JSON delimitados por linha.

## 1. O que muda em relação à introdução de JSON da Phase 7?

Você já conhece as quatro operações centrais:

```python
import json

text = json.dumps({"topic": "JSON"})
data = json.loads(text)
```

e as variantes orientadas a arquivo:

```python
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

A Phase 7 focou na fronteira de formato:

```text
texto JSON
   ↓ parsing
valores Python
```

Este capítulo foca na política ao redor dessa fronteira:

```text
valores Python
   ↓ política de serialização
representação JSON
   ↓ transporte / armazenamento
representação JSON
   ↓ política de decodificação
valores Python
```

As APIs são familiares. Os contratos são mais profundos.

## 2. Serialização faz parte de um contrato de interface

Duas strings JSON podem representar o mesmo objeto lógico e ainda diferir em espaços ou ordem dos membros:

```json
{"topic":"JSON","score":88}
```

```json
{
  "score": 88,
  "topic": "JSON"
}
```

Isso significa que o texto serializado pode ter pelo menos dois tipos de requisito:

- **requisitos semânticos**, como campos obrigatórios e tipos de valores aceitos;
- **requisitos de representação**, como espaços, ordem, escaping ou sintaxe numérica estrita.

Não assuma que um implica o outro.

## 3. `dumps()` produz texto, não bytes

`json.dumps()` retorna uma `str` do Python:

```python
import json

text = json.dumps({"topic": "JSON"})
print(type(text).__name__)
```

Saída:

```text
str
```

Se um protocolo de rede ou camada de armazenamento precisar de bytes, a codificação é uma etapa separada:

```python
payload = text.encode("utf-8")
```

Mantenha as camadas distintas:

```text
valores Python
   ↓ json.dumps()
texto Unicode
   ↓ .encode("utf-8")
bytes
```

O lado de encoding de `json` trabalha com texto: `json.dumps()` retorna `str`, e `json.dump()` escreve texto em um objeto file-like compatível. O lado de decoding aceita um conjunto mais amplo de entradas: `json.loads()` aceita `str`, `bytes` e `bytearray`, enquanto `json.load()` pode consumir um objeto file-like compatível cujo `read()` retorne uma dessas formas suportadas. Se a aplicação controla uma fronteira de bytes de rede ou armazenamento, uma política explícita de encoding ainda torna essa fronteira mais fácil de compreender.

## 4. Ordem determinística de membros com `sort_keys=True`

Dicionários Python preservam ordem de inserção, mas essa ordem nem sempre é a política de representação desejada.

Para testes, snapshots, exemplos ou arquivos de configuração gerados, ordenar chaves pode facilitar comparações:

```python
import json

record = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(record, sort_keys=True)

print(text)
```

`sort_keys=True` ordena as chaves dos dicionários na saída serializada.

Isso pode melhorar o determinismo, mas **não** transforma JSON arbitrário em uma forma canônica universal. Padrões de canonicalização podem definir regras adicionais para números, Unicode, escaping e outros detalhes de representação.

## 5. Saída legível para pessoas com `indent`

Use `indent` quando pessoas precisarem inspecionar a saída:

```python
import json

record = {"topic": "JSON", "score": 88}
print(json.dumps(record, indent=2))
```

Pretty printing aumenta espaços e normalmente aumenta o tamanho da representação.

Escolha isso porque a interface se beneficia de legibilidade, não porque JSON indentado seja mais correto.

## 6. Saída compacta com `separators`

Para uma representação compacta, remova espaços opcionais ao redor dos separadores:

```python
import json

record = {"topic": "JSON", "score": 88}
text = json.dumps(record, separators=(",", ":"))

print(text)
```

Isso produz:

```text
{"topic":"JSON","score":88}
```

Uma receita comum para saída determinística orientada a máquina é:

```python
import json

record = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(
    record,
    sort_keys=True,
    separators=(",", ":"),
)
```

Novamente, saída estável para sua aplicação não é automaticamente uma representação JSON canônica definida por padrão externo.

## 7. `ensure_ascii` controla escaping, não a codificação do texto

Por padrão, caracteres não ASCII são escapados:

```python
import json

record = {"language": "Português"}
print(json.dumps(record))
```

Com `ensure_ascii=False`, esses caracteres podem permanecer visíveis diretamente na `str` retornada:

```python
import json

record = {"language": "Português"}
print(json.dumps(record, ensure_ascii=False))
```

Isso **não** significa que o módulo JSON escolheu bytes UTF-8. O resultado continua sendo uma `str` do Python.

Se você escrever em um arquivo de texto UTF-8, a decisão de encoding pertence à fronteira do arquivo:

```python
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(record, file, ensure_ascii=False)
```

## 8. Saída JSON estrita e floats não finitos

O encoder do Python permite deliberadamente estes valores de ponto flutuante por padrão:

- `NaN`;
- `Infinity`;
- `-Infinity`.

Esses tokens não são JSON válido segundo a especificação interoperável de JSON.

Quando saída compatível com o padrão for exigida, use `allow_nan=False`:

```python
import json

record = {"value": float("nan")}

try:
    json.dumps(record, allow_nan=False)
except ValueError:
    print("Non-finite float rejected")
```

Isso é uma decisão de contrato. Um `json.dumps()` padrão bem-sucedido não prova que o texto gerado evita a extensão numérica não padronizada do Python.

## 9. Entrada JSON estrita e `parse_constant`

O decoder tem a extensão correspondente. Por padrão, Python aceita `NaN`, `Infinity` e `-Infinity`.

Para rejeitá-los, forneça um callback em `parse_constant`:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


text = '{"value": NaN}'

try:
    json.loads(text, parse_constant=reject_nonstandard_constant)
except ValueError as error:
    print(error)
```

`JSONDecodeError` continua representando erros comuns de sintaxe JSON. O `ValueError` acima vem do callback que você forneceu deliberadamente.

Uma interface estrita costuma precisar das duas direções:

```text
encoding: allow_nan=False
decoding: parse_constant=callback que rejeita
```

## 10. Números JSON não definem a política de precisão da aplicação

JSON possui uma sintaxe de números, mas implementações diferentes podem mapear esses números para tipos numéricos e limites de precisão diferentes.

Python normalmente decodifica:

- números JSON em forma inteira, sem fração nem expoente, para `int`;
- números JSON contendo fração ou expoente para `float`.

```python
import json

data = json.loads('{"count": 3, "ratio": 0.1}')

print(type(data["count"]).__name__)
print(type(data["ratio"]).__name__)
```

Para interfaces que trocam inteiros muito grandes ou decimais de alta precisão, os limites do sistema receptor também importam. Um `int` do Python pode representar valores que outra implementação talvez não preserve exatamente.

Interoperabilidade é uma propriedade das duas pontas da interface.

## 11. Decodifique números JSON de ponto flutuante com `parse_float`

O decoder pode entregar cada número JSON de ponto flutuante a uma função escolhida por você. Isso inclui tokens com parte fracionária, como `19.90`, e formas exponenciais como `1e2`.

Por exemplo, `decimal.Decimal` pode preservar exatamente o texto decimal:

```python
import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
```

Isso é útil quando a aplicação precisa de semântica decimal em vez de semântica de ponto flutuante binário.

Isso não transforma `Decimal` em um tipo JSON nativo. É uma escolha de decodificação dentro do Python.

## 12. `parse_int` também pode personalizar inteiros

`parse_int` recebe o texto de cada inteiro JSON:

```python
import json


def tagged_integer(text: str):
    return ("integer", text)


data = json.loads('{"count": 42}', parse_int=tagged_integer)
print(data["count"])
```

Personalizar parsing de inteiros é menos comum em aplicações iniciantes, mas mostra um princípio importante: decodificação é reconstrução configurável, não conversão mágica um-para-um.

Use um hook numérico personalizado somente quando o comportamento fizer parte de um contrato documentado.

## 13. Nomes de objetos JSON são strings

Nomes de membros de objetos JSON são strings.

O encoder do Python aceita algumas chaves básicas que não são strings e as converte, portanto um round trip pode não preservar tipos de chave:

```python
import json

original = {1: "one", 2: "two"}
restored = json.loads(json.dumps(original))

print(original)
print(restored)
print(original == restored)
```

As chaves decodificadas são strings.

Se o tipo da chave carrega significado na aplicação, represente esse significado explicitamente em vez de depender de round trip de chaves de dicionário.

## 14. Prefira falhas visíveis a `skipkeys=True`

Por padrão, tipos de chave não suportados geram `TypeError`:

```python
import json

record = {(1, 2): "coordinate"}

try:
    json.dumps(record)
except TypeError:
    print("Unsupported key type")
```

`skipkeys=True` pode omitir silenciosamente chaves não suportadas:

```python
text = json.dumps(record, skipkeys=True)
```

Isso só é apropriado quando descartar tais entradas é uma política explícita.

Para a maioria dos contratos de dados, perder informação silenciosamente é mais perigoso que receber uma exceção que obriga a representação a ser projetada corretamente.

## 15. Serialização personalizada com `default`

Objetos Python arbitrários não são serializáveis em JSON por padrão.

Um callback `default` pode converter objetos selecionados não suportados em estruturas compatíveis com JSON:

```python
import json
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def encode_custom(value):
    if isinstance(value, Point):
        return {"type": "point", "x": value.x, "y": value.y}
    raise TypeError(f"unsupported type: {type(value).__name__}")


text = json.dumps(Point(4, 7), default=encode_custom, sort_keys=True)
print(text)
```

Um bom callback trata somente os tipos que suporta deliberadamente e gera `TypeError` para os demais.

Não transforme `default` em uma solução genérica que adivinha como qualquer objeto deve ser serializado.

## 16. Representações com tags são seu schema, não o schema do JSON

Esta representação:

```json
{"type": "point", "x": 4, "y": 7}
```

é JSON comum. O significado de `"type": "point"` pertence à sua aplicação.

Isso significa que o contrato deve responder perguntas como:

- `type` é obrigatório?
- Quais nomes de tipo são permitidos?
- `x` e `y` são inteiros obrigatórios?
- O que acontece com campos extras?
- Qual versão do schema produziu o documento?

A sintaxe JSON não responde essas perguntas de negócio.

## 17. Um `JSONEncoder` personalizado pode centralizar comportamento

Para política de encoding reutilizável, herde de `json.JSONEncoder` e sobrescreva `default()`:

```python
import json
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class StudyEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, Point):
            return {"type": "point", "x": value.x, "y": value.y}
        return super().default(value)


text = json.dumps(Point(4, 7), cls=StudyEncoder)
print(text)
```

Use um encoder personalizado quando a aplicação realmente se beneficiar de uma política reutilizável. Para uma única conversão, transformação explícita ou função `default` costuma ser mais simples de entender.

## 18. Reconstrução personalizada com `object_hook`

`object_hook` é chamado para cada objeto JSON decodificado depois que ele foi transformado em dicionário.

```python
import json


def decode_custom(record):
    if record.get("type") == "point":
        return (record["x"], record["y"])
    return record


text = '{"type": "point", "x": 4, "y": 7}'
data = json.loads(text, object_hook=decode_custom)

print(data)
```

O valor retornado pelo hook substitui aquele dicionário no resultado decodificado.

Isso é poderoso, então mantenha a política restrita e explícita.

## 19. Não deixe tags não confiáveis escolherem caminhos arbitrários de código

Um `object_hook` é código Python executado durante a decodificação.

Evite designs em que uma string não confiável possa selecionar dinamicamente imports, classes, funções ou construtores arbitrários.

Prefira uma allowlist fixa de representações conhecidas:

```text
tag de entrada
   ↓ validar contra valores conhecidos
conversão conhecida
```

JSON em si é um formato de dados. O risco aparece quando a aplicação concede autoridade excessiva ao dado não confiável sobre qual código será executado em seguida.

## 20. Nomes duplicados em objetos são aceitos por padrão

Considere este texto JSON:

```json
{"topic": "JSON", "topic": "CSV"}
```

O decoder padrão do Python aceita nomes repetidos e mantém apenas o último valor:

```python
import json

text = '{"topic": "JSON", "topic": "CSV"}'
data = json.loads(text)

print(data)
```

Saída:

```text
{'topic': 'CSV'}
```

Se unicidade for importante para sua interface, a decodificação padrão não basta para garanti-la.

## 21. Inspecione pares com `object_pairs_hook`

`object_pairs_hook` recebe os pares nome-valor de cada objeto JSON em ordem, antes de eles virarem um dicionário comum.

Isso torna possível detectar duplicatas:

```python
import json


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


text = '{"topic": "JSON", "topic": "CSV"}'

try:
    json.loads(text, object_pairs_hook=reject_duplicate_keys)
except ValueError as error:
    print(error)
```

Este é outro exemplo de transformar uma suposição vaga em contrato aplicado.

## 22. `object_pairs_hook` tem prioridade sobre `object_hook`

Se os dois forem fornecidos, `object_pairs_hook` tem prioridade na decodificação de objetos.

Evite combinar hooks de forma casual. Se uma política precisa detectar duplicatas e fazer reconstrução personalizada, projete as etapas de forma que ordem e responsabilidades fiquem óbvias.

Uma política clara de decoder é mais fácil de auditar que um conjunto de hooks que se sobrepõem por acidente.

## 23. Mantenha a verificação de referências circulares habilitada

Containers Python podem conter ciclos:

```python
items = []
items.append(items)
```

JSON não representa diretamente esse grafo de objetos.

O encoder verifica referências circulares por padrão. Mantenha `check_circular=True` a menos que exista motivo medido e bem compreendido para desabilitar.

Desligar a verificação não torna ciclos serializáveis. Apenas remove a proteção que os detecta e pode levar a falha por recursão.

## 24. Use detalhes de `JSONDecodeError` para diagnóstico

`JSONDecodeError` inclui informações úteis de localização:

```python
import json

text = '{"topic": "JSON",}'

try:
    json.loads(text)
except json.JSONDecodeError as error:
    print(error.msg)
    print(error.lineno)
    print(error.colno)
```

Campos úteis incluem:

- `msg` para a mensagem do decoder;
- `lineno` para o número da linha;
- `colno` para o número da coluna;
- `pos` para a posição do caractere no documento de origem.

Exponha apenas o nível de detalhe apropriado à interface. Diagnóstico de ferramenta para desenvolvedor e diagnóstico retornado por serviço público não precisam ser idênticos.

## 25. Fazer parsing de JSON válido ainda não é validar schema

Isto é JSON válido:

```json
{"score": -500, "status": "banana"}
```

O trabalho do decoder é reconstruir valores. A aplicação ainda precisa validar regras de domínio:

```python
import json

record = json.loads('{"score": -500}')

if not 0 <= record["score"] <= 100:
    raise ValueError("score must be between 0 and 100")
```

Mantenha as perguntas separadas:

```text
O texto é JSON válido?
        ↓
A forma decodificada corresponde ao schema da interface?
        ↓
Os valores satisfazem as regras da aplicação?
```

## 26. Limite entrada não confiável

A documentação oficial do Python alerta que JSON malicioso pode consumir CPU e memória consideráveis durante a decodificação.

O módulo `json` não é um sistema geral de quota de recursos. Em fronteiras sob seu controle, considere limites como:

- tamanho máximo de request ou arquivo;
- profundidade máxima aceita definida pela aplicação ou gateway ao redor;
- timeouts na camada de transporte ou worker;
- limites de schema para tamanho de arrays e strings.

Não aceite payload ilimitado apenas porque a sintaxe é JSON.

## 27. Encoding de texto é uma preocupação separada de transporte

JSON trocado como bytes precisa de uma codificação de caracteres acordada. UTF-8 é o padrão de interoperabilidade em sistemas modernos.

Quando você controla I/O de arquivo, deixe a codificação explícita:

```python
import json

record = {"language": "Português"}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(record, file, ensure_ascii=False)
```

O serializer do Python não adiciona byte-order mark à saída JSON. Mantenha decisões de encoding de transporte fora do modelo lógico de dados sempre que possível.

## 28. O valor JSON de nível superior não precisa ser um objeto

Todos estes são valores JSON válidos no nível superior pelas especificações modernas:

```json
42
```

```json
"ready"
```

```json
true
```

```json
[1, 2, 3]
```

Sua API ainda pode exigir objeto ou array. Isso seria um **contrato da aplicação**, não uma regra universal da sintaxe JSON.

Valide a forma de nível superior que você realmente espera.

## 29. A interface de linha de comando pode validar e formatar JSON

Python inclui uma ferramenta JSON de linha de comando.

No Python 3.14, a forma direta preferida é:

```text
python -m json data.json
```

Para compatibilidade com versões anteriores, esta forma continua disponível:

```text
python -m json.tool data.json
```

O comando é útil para validação rápida e formatação legível.

A interface do Python 3.14 também oferece opções como:

```text
--sort-keys
--no-ensure-ascii
--json-lines
--indent
--tab
--compact
```

Use `python -m json --help` para consultar as opções exatas no interpretador em execução.

## 30. JSON Lines é outro contrato de framing

Um documento JSON único contém um valor JSON no nível superior.

Isto não é um documento JSON comum único:

```text
{"id": 1}
{"id": 2}
{"id": 3}
```

Porém, pode ser um contrato válido de **JSON Lines / JSON delimitado por linhas** quando cada linha é definida independentemente como um valor JSON.

A CLI JSON do Python 3.14 possui suporte a `--json-lines`, mas sua aplicação ainda precisa declarar que consome um formato delimitado por linhas.

Não confunda:

```text
um documento JSON contendo um array
```

com:

```text
múltiplos valores JSON delimitados por linhas
```

A regra de framing faz parte da interface.

## 31. Chamadas repetidas de `dump()` ainda não criam framing

Esta continua sendo uma fronteira importante da Phase 7:

```python
json.dump(first, file)
json.dump(second, file)
```

Chamadas repetidas não adicionam automaticamente separador ou container que transforme os valores em um documento JSON válido.

Escolha uma estrutura explícita:

- um array contendo vários valores;
- um objeto contendo coleções nomeadas;
- um formato JSON delimitado por linhas documentado;
- outro protocolo que defina framing.

## 32. Saída estável não é canonicalização criptográfica

Uma receita local útil como:

```python
json.dumps(
    data,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)
```

pode tornar snapshots e diffs estáveis em uma aplicação Python controlada.

Não use automaticamente essa string para assinaturas, hashes compartilhados entre implementações ou protocolos de canonicalização entre linguagens.

Esses casos exigem uma especificação de canonicalização que defina todas as regras relevantes de representação.

## 33. Uma política prática de decodificação estrita

Para uma interface que quer rejeitar constantes numéricas não padronizadas do Python e nomes duplicados de objetos, combine hooks estreitos de propósito deliberado:

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


def load_strict_json(text: str):
    return json.loads(
        text,
        parse_constant=reject_nonstandard_constant,
        object_pairs_hook=reject_duplicate_keys,
    )
```

Isso ainda não valida seu schema de negócio. Apenas endurece duas políticas de decodificação JSON.

## 34. Uma política prática de encoding determinístico

Para snapshots independentes de leitura humana ou artefatos gerados em que saída compacta e estável ajuda:

```python
import json


def dump_stable_json(data):
    return json.dumps(
        data,
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
```

A política agora comunica várias decisões explicitamente:

- rejeitar floats não finitos;
- manter caracteres Unicode legíveis no texto Python;
- ordenar chaves de dicionário;
- remover espaços opcionais dos separadores.

Isso é muito mais fácil de revisar que depender de defaults não documentados espalhados pelo código.

## 35. Erros comuns

### Erro 1: tratar parsing bem-sucedido como validação de schema

Sintaxe válida não prova que campos obrigatórios, tipos, faixas ou regras de negócio estão corretos.

### Erro 2: assumir que JSON padrão do Python é estrito nas duas direções

Por padrão, Python aceita e emite `NaN`, `Infinity` e `-Infinity`.

### Erro 3: assumir que round trip preserva todo tipo Python

Tuplas viram arrays e retornam como listas; nomes de objetos são strings; objetos personalizados precisam de representação explícita.

### Erro 4: habilitar `skipkeys=True` para fazer erros desaparecerem

Isso pode remover dados silenciosamente.

### Erro 5: usar `default=str` sem definir contrato

Transformar todo objeto não suportado em string de exibição arbitrária pode fazer a serialização funcionar enquanto destrói significado de tipo.

### Erro 6: usar `sort_keys=True` e chamar o resultado de JSON canônico

Ordenar chaves resolve apenas uma dimensão da representação.

### Erro 7: decodificar entrada não confiável sem limite

Parsers de sintaxe ainda podem consumir CPU e memória.

### Erro 8: construir objetos Python arbitrários dinamicamente a partir de tags não confiáveis

Mantenha reconstrução personalizada em allowlist explícita e valide campos antes de usá-los.

## 36. Exemplo prático: saída JSON determinística

```python
import json


data = {"status": "ready", "score": 88, "topic": "JSON"}
text = json.dumps(
    data,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)

print(text)
```

Saída esperada:

```text
{"score":88,"status":"ready","topic":"JSON"}
```

Versão executável: [`examples/deterministic_json.py`](examples/deterministic_json.py).

## 37. Exemplo prático: tratamento estrito de números não finitos

```python
import json


def reject_nonstandard_constant(value: str):
    raise ValueError(f"non-standard JSON constant: {value}")


try:
    json.dumps({"value": float("nan")}, allow_nan=False)
except ValueError:
    print("Encoding rejected non-finite float")

try:
    json.loads('{"value": NaN}', parse_constant=reject_nonstandard_constant)
except ValueError:
    print("Decoding rejected non-standard constant")
```

Versão executável: [`examples/strict_numbers.py`](examples/strict_numbers.py).

## 38. Exemplo prático: decodificação decimal

```python
import json
from decimal import Decimal


data = json.loads(
    '{"price": 19.90, "quantity": 3}',
    parse_float=Decimal,
)

print(data["price"])
print(type(data["price"]).__name__)
print(type(data["quantity"]).__name__)
```

Versão executável: [`examples/decimal_decode.py`](examples/decimal_decode.py).

## 39. Exemplo prático: rejeitar nomes duplicados de objetos

```python
import json


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object name: {key}")
        result[key] = value
    return result


samples = [
    '{"topic": "JSON", "score": 88}',
    '{"topic": "JSON", "topic": "CSV"}',
]

for text in samples:
    try:
        data = json.loads(text, object_pairs_hook=reject_duplicate_keys)
    except ValueError as error:
        print(error)
    else:
        print(data)
```

Versão executável: [`examples/reject_duplicate_keys.py`](examples/reject_duplicate_keys.py).

## 40. Exercício

Crie uma função chamada `decode_settings(text)` para um contrato de configuração de aplicação.

Requisitos:

1. Faça parsing da string JSON.
2. Rejeite `NaN`, `Infinity` e `-Infinity`.
3. Rejeite nomes duplicados em objetos.
4. Exija que o valor de nível superior seja um dicionário.
5. Exija exatamente estes campos: `theme`, `refresh_seconds` e `enabled`.
6. Exija `theme` como string não vazia.
7. Exija `refresh_seconds` como inteiro de 1 a 3600. Lembre que `bool` é subclasse de `int`, então rejeite booleanos explicitamente se eles não forem válidos aqui.
8. Exija `enabled` como booleano.
9. Retorne o dicionário validado.

Depois crie uma segunda função, `encode_settings(data)`, que:

1. serialize com `allow_nan=False`;
2. use `ensure_ascii=False`;
3. ordene chaves;
4. use separadores compactos.

Teste pelo menos estes casos:

```text
configuração válida
campo ausente
campo duplicado
valor NaN
tipo incorreto no nível superior
refresh_seconds = true
refresh_seconds = 0
```

A parte importante não é apenas fazer a entrada válida funcionar. Torne cada fronteira explícita o bastante para que uma pessoa futura consiga explicar **por que** a entrada inválida é rejeitada.

## 41. Referência rápida

| Necessidade | Ferramenta / política |
|---|---|
| Valor Python → texto JSON | `json.dumps()` |
| Texto JSON / bytes → valor Python | `json.loads()` |
| Ler JSON de objeto file-like compatível de texto ou binário | `json.load()` |
| Escrever JSON em objeto file-like de texto | `json.dump()` |
| Saída legível | `indent=2` ou outro indent explícito |
| Saída compacta | `separators=(",", ":")` |
| Ordem estável de chaves | `sort_keys=True` |
| Manter caracteres não ASCII visíveis | `ensure_ascii=False` |
| Rejeitar floats não finitos ao serializar | `allow_nan=False` |
| Rejeitar `NaN` / infinitos ao decodificar | `parse_constant=...` |
| Decodificar números JSON de ponto flutuante de outra forma | `parse_float=...` |
| Decodificar inteiros de outra forma | `parse_int=...` |
| Converter valores personalizados não suportados | `default=...` |
| Encoder personalizado reutilizável | `cls=YourJSONEncoder` |
| Transformar objetos JSON decodificados | `object_hook=...` |
| Inspecionar pares ordenados / duplicatas | `object_pairs_hook=...` |
| Diagnóstico de sintaxe do decoder | `json.JSONDecodeError` |
| Validar / pretty-print via CLI no Python 3.14 | `python -m json` |
| Forma de CLI compatível com versões anteriores | `python -m json.tool` |

## 42. Checklist de design

Antes de publicar uma interface JSON, pergunte:

```text
Qual forma de nível superior é aceita?
Quais campos são obrigatórios?
Nomes duplicados são rejeitados?
NaN e infinitos são rejeitados?
Qual precisão numérica é necessária?
Qual o tamanho máximo do documento?
Como tipos personalizados são representados?
A ordem de chaves é relevante apenas para apresentação ou para outro protocolo?
Qual encoding de caracteres transporta o texto JSON como bytes?
Isto é um documento JSON único ou um formato delimitado por linhas?
```

Se essas respostas forem explícitas, a fronteira JSON fica muito mais fácil de testar e manter.

## Referências

- [Documentação Python 3.14: `json` — JSON encoder and decoder](https://docs.python.org/3.14/library/json.html)
- [Documentação Python 3.14: interface de linha de comando JSON](https://docs.python.org/3.14/library/json.html#module-json.tool)
- [RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259)

## Próximo capítulo

Continue com o [**Capítulo 04: Controlando Dialetos CSV e Contratos de Texto Tabular**](../04-csv/README.pt-BR.md). Ele aprofunda dialetos, quoting, escaping, validação do formato das linhas, sniffing, fronteiras de encoding e considerações para consumidores em planilhas.
