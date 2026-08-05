<div align="center">

# Nomes Significativos e Código Autoexplicativo

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Docstrings](../02-docstrings/README.pt-BR.md)

Um nome é uma das menores decisões de design de um programa, mas pode ser lido centenas de vezes. Bons nomes reduzem a quantidade de contexto que uma pessoa precisa reconstruir e ajudam o código a comunicar intenção antes que um comentário ou uma docstring sejam necessários.

> **Princípio orientador:** Nomeie um conceito de acordo com o que ele significa no programa, e não apenas de acordo com o valor armazenado nele naquele momento.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Recomenda-se familiaridade básica com variáveis e funções |
| Tempo estimado de estudo | 50 a 70 minutos |
| Conceitos principais | nomes que revelam intenção, `snake_case`, `PascalCase`, constantes, booleanos, unidades, coleções, escopo, vocabulário, built-ins, refatoração |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- escolher nomes que revelem propósito, significado no domínio, estado e unidades;
- seguir convenções comuns de nomes em Python sem tratá-las como regras de sintaxe;
- diferenciar brevidade útil de imprecisão prejudicial;
- nomear valores booleanos como perguntas ou condições;
- utilizar nomes no plural para coleções e no singular para elementos individuais;
- evitar sobrescrever nomes built-in e palavras reservadas;
- utilizar um vocabulário consistente para o mesmo conceito;
- reconhecer quando uma pequena função ou variável pode revelar intenção;
- compreender onde comentários e docstrings continuam necessários;
- renomear código com segurança, considerando interfaces públicas.

## 1. Por que os nomes importam

O Python executa identificadores sem se importar se eles são expressivos:

```python
x = 30
y = 0.10
z = x - (x * y)
```

Uma pessoa precisa deduzir o significado de cada valor. O mesmo cálculo pode comunicar muito mais:

```python
subtotal = 30
discount_rate = 0.10
discounted_total = subtotal - (subtotal * discount_rate)
```

A segunda versão não muda o algoritmo. Ela muda o esforço exigido de quem lê.

Nomes significativos ajudam a responder:

- O que este valor representa?
- Qual unidade ele utiliza?
- Trata-se de um item ou de uma coleção?
- O booleano representa estado, capacidade ou decisão?
- Qual ação esta função realiza?
- Qual conceito esta classe modela?

## 2. Sintaxe e convenções de nomes em Python

Na convenção ASCII mais comum, um identificador começa com uma letra ou underscore e continua com letras, dígitos ou underscores. A gramática léxica completa do Python é mais ampla: ela aceita diversos caracteres Unicode de acordo com as regras `XID_Start` e `XID_Continue`, e os identificadores diferenciam letras maiúsculas de minúsculas. Consulte a [referência léxica oficial](https://docs.python.org/pt-br/3/reference/lexical_analysis.html#identificadores).

Este projeto utiliza identificadores ASCII em inglês para favorecer portabilidade, pesquisa e consistência entre ferramentas e documentações internacionais.

Válidos:

```python
customer_name = "Mina"
invoice2_total = 125
_internal_cache = {}
```

Inválidos:

```python
2nd_invoice = 125
customer-name = "Mina"
```

Palavras reservadas do Python não podem ser utilizadas como identificadores comuns:

```python
class = "premium"
```

Quando um conceito externo conflita com uma palavra reservada, um underscore no final é uma opção comum:

```python
class_ = "premium"
```

### Convenções comuns de estilo

| Tipo de nome | Convenção comum | Exemplo |
|---|---|---|
| Variável | `snake_case` | `invoice_total` |
| Função | `snake_case` | `calculate_invoice_total()` |
| Classe | `PascalCase` | `InvoiceCalculator` |
| Constante | `UPPER_SNAKE_CASE` | `MAX_RETRY_ATTEMPTS` |
| Nome de uso interno | underscore inicial | `_load_cached_value()` |

Essas convenções facilitam o reconhecimento, mas o Python normalmente não as impõe. Um projeto pode adicionar linters ou verificações de estilo.

## 3. Revele intenção, não apenas conteúdo

Nomes fracos costumam descrever o recipiente, e não o conceito:

```python
data = ["Ana", "Diego", "Mina"]
value = 30
result = value * 60
```

Mais claro:

```python
customer_names = ["Ana", "Diego", "Mina"]
duration_minutes = 30
duration_seconds = duration_minutes * 60
```

`data`, `value`, `item` e `result` nem sempre estão errados. Eles se tornam prejudiciais quando o contexto ao redor não deixa seu significado evidente.

Uma pergunta útil ao nomear é:

> O que uma pessoa precisaria saber para utilizar este valor corretamente?

## 4. Inclua unidades e representação quando forem importantes

Um número sem unidade pode criar erros silenciosos:

```python
timeout = 30
total = 12_750
```

Não é possível saber se `timeout` está em segundos ou milissegundos, nem se `total` representa unidades monetárias ou centavos.

Mais claro:

```python
timeout_seconds = 30
invoice_total_cents = 12_750
```

Detalhes úteis de representação podem incluir:

- `_seconds`, `_minutes` ou `_milliseconds`;
- `_bytes` ou `_megabytes`;
- `_cents` quando se evita moeda em ponto flutuante;
- `_percentage` para valores de 0 a 100;
- `_rate` para valores fracionários como `0.15`;
- `_text`, `_path`, `_date` ou `_datetime` quando diferentes formas poderiam ser confundidas.

Não acrescente todo tipo a todo nome. Acrescente informações que previnam uma confusão realista.

## 5. Nomeie booleanos como perguntas ou condições

Um nome booleano deve tornar `True` e `False` legíveis.

Fraco:

```python
active = True
retry = False
```

Mais claro:

```python
is_active = True
should_retry = False
```

Prefixos comuns incluem:

- `is_` para estado ou classificação;
- `has_` para posse ou presença;
- `can_` para capacidade ou permissão;
- `should_` para decisão;
- `needs_` para uma ação necessária.

Exemplo:

```python
RETRYABLE_STATUS_CODES = {502, 503, 504}

is_status_configured_for_retry = (
    response_status_code in RETRYABLE_STATUS_CODES
)
has_retry_attempts_remaining = attempt_number < MAX_RETRY_ATTEMPTS
should_retry_request = (
    is_status_configured_for_retry and has_retry_attempts_remaining
)
```

Evite nomes negativos quando eles produzem dupla negação:

```python
if not is_not_ready:
    ...
```

Prefira um conceito positivo:

```python
if is_ready:
    ...
```

## 6. Coleções e elementos individuais

Nomes no plural ajudam a reconhecer coleções:

```python
customer_names = ["Ana", "Diego", "Mina"]

for customer_name in customer_names:
    print(customer_name)
```

As formas no plural e no singular mostram imediatamente a relação.

Para mapeamentos, nomeie os dois lados quando isso for útil:

```python
country_code_by_name = {
    "Brazil": "BR",
    "Spain": "ES",
}
```

Outros padrões legíveis incluem:

```python
users_by_id = {}
price_by_product_code = {}
errors_by_file_path = {}
```

Nomes como `mapping`, `dictionary` e `list_data` revelam o tipo do recipiente, mas frequentemente escondem a relação do domínio.

## 7. Funções, classes e constantes

### Funções geralmente descrevem ações

Nomes de funções normalmente começam com verbos:

```python
calculate_total()
load_configuration()
normalize_account_code()
is_supported_account()
```

O verbo deve corresponder ao comportamento. Uma função chamada `get_report()` não deve apagar arquivos ou enviar e-mails inesperadamente.

### Classes geralmente descrevem entidades ou responsabilidades

Nomes de classes normalmente utilizam substantivos:

```python
Invoice
ReportGenerator
ValidationResult
```

Evite sufixos vazios como `Manager`, `Helper` ou `Processor` quando eles não esclarecem a responsabilidade. Às vezes essas palavras são corretas, mas não devem virar máquinas de neblina.

### Constantes descrevem configuração ou política estável

```python
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
SUPPORTED_FILE_EXTENSIONS = {".csv", ".json"}
```

As letras maiúsculas comunicam que o valor deve permanecer estável por convenção. Isso não torna o objeto tecnicamente imutável.

## 8. O escopo determina quanto detalhe um nome precisa

Um nome curto pode ser claro dentro de um escopo local minúsculo:

```python
for row in rows:
    print(row)
```

O mesmo nome pode ser vago demais em uma função ou módulo grande.

Um índice de loop costuma ser compreensível como `index` ou até `i` em um loop matemático muito pequeno:

```python
for i in range(3):
    print(i)
```

Um escopo maior geralmente merece mais contexto:

```python
for retry_attempt_index in range(MAX_RETRY_ATTEMPTS):
    ...
```

Nomes longos não são automaticamente bons. Um nome deve carregar informação suficiente para seu escopo sem virar um parágrafo vestido de underscores.

## 9. Abreviações, siglas e vocabulário do projeto

Utilize uma abreviação quando ela for mais familiar que sua forma expandida ou quando o projeto a tiver definido claramente:

```python
url = "https://example.com"
user_id = 42
csv_file_path = "report.csv"
```

Evite quebra-cabeças particulares:

```python
usr_cfg_tmp = {}
```

Um vocabulário consistente é mais importante do que encontrar um sinônimo novo em cada linha.

Confuso:

```python
customer_id = 42
client_name = "Ana"
consumer_status = "active"
```

Quando esses nomes representam a mesma entidade do domínio, escolha um termo:

```python
customer_id = 42
customer_name = "Ana"
customer_status = "active"
```

Um glossário do projeto pode evitar a deriva de vocabulário em sistemas maiores.

## 10. Evite sobrescrever built-ins e nomes importantes

O Python oferece built-ins como `list`, `str`, `sum`, `id`, `input` e `type`.

Evite:

```python
list = ["Ana", "Diego"]
sum = 100
```

Depois dessas atribuições, chamar `list()` ou `sum()` no mesmo escopo deixa de acessar o built-in.

Prefira:

```python
customer_names = ["Ana", "Diego"]
invoice_total = 100
```

A sobrescrita também pode ocorrer com módulos ou funções importados:

```python
import logging

logging = True
```

A atribuição esconde o módulo importado. Escolha um nome diferente, como `is_logging_enabled`.

## 11. Não codifique informações de tipo desnecessárias

Nomes como estes costumam envelhecer mal:

```python
customer_name_string = "Ana"
invoice_items_list = []
settings_dictionary = {}
```

Type hints e as operações ao redor do valor já comunicam boa parte de sua estrutura:

```python
customer_name: str = "Ana"
invoice_items: list[str] = []
settings: dict[str, str] = {}
```

Inclua a representação no nome apenas quando ela evitar ambiguidade, como em `invoice_total_cents` ou `created_at_text`.

## 12. Pequenas abstrações podem revelar intenção

Uma expressão complicada pode receber um nome:

```python
is_priority_customer = (
    customer_status == "active"
    and annual_purchase_total >= 10_000
    and not has_overdue_invoice
)
```

Uma operação reutilizável pode se tornar uma função:

```python
def is_priority_customer(
    customer_status,
    annual_purchase_total,
    has_overdue_invoice,
):
    return (
        customer_status == "active"
        and annual_purchase_total >= 10_000
        and not has_overdue_invoice
    )
```

O nome cria uma alça conceitual. Ele não deve esconder complexidade arbitrária atrás de um rótulo enganoso.

Bons nomes de abstrações explicam **o que** a operação significa. A implementação explica **como** ela funciona.

## 13. Código autoexplicativo não elimina documentação

Nomes claros reduzem comentários que apenas traduzem a sintaxe:

```python
# Check whether the account is supported.
if account_code in supported_account_codes:
    ...
```

O comentário acrescenta pouco porque os nomes já explicam a condição.

Comentários continuam úteis para motivos e restrições:

```python
# Keep the legacy code for compatibility with exports created before 2024.
supported_account_codes.add("LEGACY")
```

Docstrings continuam úteis para contratos públicos, exceções, efeitos colaterais e expectativas de uso.

Código legível, comentários, docstrings, type hints, testes e documentação externa resolvem problemas diferentes.

## 14. Renomeando com segurança

Renomear é uma refatoração: o comportamento deve permanecer igual enquanto o código se torna mais fácil de compreender.

Um fluxo seguro é:

1. identificar o conceito representado pelo nome;
2. procurar todas as referências;
3. utilizar ferramentas de refatoração do editor quando disponíveis;
4. atualizar testes, exemplos, docstrings e documentação;
5. executar as verificações do projeto;
6. revisar a compatibilidade pública.

Renomear uma variável local geralmente possui risco baixo. Renomear uma função pública, classe, módulo, opção de linha de comando, chave de configuração, campo de banco de dados ou atributo serializado pode quebrar usuários.

Renomeações públicas podem exigir:

- período de descontinuação;
- alias;
- instruções de migração;
- versão de lançamento;
- coordenação com sistemas externos.

## 15. Exemplos neste repositório

| Arquivo | Finalidade |
|---|---|
| [`vague_and_clear_names.py`](examples/vague_and_clear_names.py) | Compara identificadores vagos com nomes que comunicam a intenção do cálculo |
| [`booleans_and_units.py`](examples/booleans_and_units.py) | Demonstra booleanos, unidades, coleções e constantes |
| [`refactor_for_intent.py`](examples/refactor_for_intent.py) | Mostra pequenas operações nomeadas revelando um fluxo |

Execute um exemplo a partir da raiz do repositório:

```bash
python comments-and-documentation/03-meaningful-names/examples/vague_and_clear_names.py
```

Em sistemas nos quais o comando se chama `python3`:

```bash
python3 comments-and-documentation/03-meaningful-names/examples/vague_and_clear_names.py
```

## 16. Exemplo prático

Antes:

```python
def f(p, d):
    t = sum(p)
    return t - (t * d)
```

Depois:

```python
def calculate_discounted_total(
    prices: list[float],
    discount_rate: float,
) -> float:
    subtotal = sum(prices)
    discount_amount = subtotal * discount_rate
    return subtotal - discount_amount
```

A segunda versão comunica:

- a ação da função;
- o que a coleção contém;
- que o desconto é uma taxa fracionária;
- o que os valores intermediários representam;
- o significado do valor retornado.

Consulte a comparação completa em [`examples/vague_and_clear_names.py`](examples/vague_and_clear_names.py).

## 17. Erros comuns

### Escolher um nome longo sem acrescentar significado

```python
the_value_that_we_are_currently_using = 10
```

Longo não significa preciso. Prefira o conceito do domínio:

```python
retry_delay_seconds = 10
```

### Utilizar um nome para vários significados

Reutilizar `result` para etapas não relacionadas dificulta depuração e revisão.

### Nomear pela implementação, e não pela responsabilidade

`json_dictionary` pode se tornar incorreto se a implementação mudar. `report_payload` pode descrever melhor sua função.

### Utilizar verbos enganosos

Uma função chamada `check_permissions()` que altera permissões viola a expectativa de quem lê.

### Misturar singular e plural

```python
customer = ["Ana", "Diego"]
```

Utilize `customers` ou `customer_names`.

### Esconder um built-in

```python
type = "premium"
```

Utilize `customer_type` ou outro nome específico do domínio.

### Manter nomes obsoletos depois de mudanças de comportamento

Uma variável chamada `discount_percentage` é enganosa quando o código passa a armazenar `0.15` como taxa.

## 18. Exercício

Refatore este código sem alterar seu resultado:

```python
def p(x, y, z):
    a = x * y
    if z:
        a = a * 1.15
    return a
```

Considere que:

- `x` é um valor por hora em centavos;
- `y` é uma quantidade de horas trabalhadas;
- `z` indica se um adicional fictício se aplica;
- `1.15` representa um multiplicador fictício de adicional.

Uma possível resposta:

```python
PREMIUM_PAY_MULTIPLIER = 1.15


def calculate_pay_cents(
    hourly_rate_cents,
    worked_hours,
    has_premium_pay,
):
    base_pay_cents = hourly_rate_cents * worked_hours

    if has_premium_pay:
        return base_pay_cents * PREMIUM_PAY_MULTIPLIER

    return base_pay_cents
```

Perguntas para revisão:

1. Cada nome revela um conceito, e não apenas um tipo?
2. As unidades estão explícitas quando existe possibilidade de confusão?
3. O booleano é lido naturalmente em uma condição?
4. A constante explica o número antes inexplicado?
5. A refatoração preservou o comportamento?

## 19. Checklist de revisão de nomes

Antes de aceitar um nome, pergunte:

- Uma pessoa consegue explicar o conceito sem percorrer várias linhas?
- O nome diferencia um item de uma coleção?
- Unidades ou representações estão explícitas quando necessário?
- Um booleano é lido naturalmente como verdadeiro ou falso?
- O nome da função corresponde aos seus efeitos?
- O mesmo termo do domínio é utilizado de maneira consistente?
- O nome evita sobrescrever um built-in ou import?
- A quantidade de detalhes é adequada ao escopo?
- Uma mudança de comportamento tornaria o nome falso?
- A compatibilidade pública exige um plano de migração?

## 20. Resumo para consulta rápida

| Situação | Prefira |
|---|---|
| Variável ou função | `snake_case` |
| Classe | `PascalCase` |
| Constante | `UPPER_SNAKE_CASE` |
| Estado booleano | `is_active`, `has_access`, `should_retry` |
| Coleção | substantivo no plural, como `customer_names` |
| Elemento individual | substantivo no singular, como `customer_name` |
| Unidade numérica | `timeout_seconds`, `total_cents` |
| Relação de mapeamento | `users_by_id`, `code_by_name` |
| Comportamento de função | verbo claro, como `calculate`, `load`, `normalize` |
| Conflito com palavra reservada | underscore final, como `class_` |
| Nome built-in | alternativa específica do domínio |
| Condição complexa repetida | variável ou função que revele intenção |

## Conclusão

Nomes significativos são documentação executável costurada diretamente no código. Eles não substituem design, comentários, docstrings, testes ou guias, mas tornam todas essas ferramentas mais fáceis de utilizar.

Escolha nomes que permaneçam verdadeiros, revelem o vocabulário do programa e reduzam a quantidade de suposições exigidas de quem lê.

[← Capítulo anterior: Docstrings](../02-docstrings/README.pt-BR.md) · [Voltar ao índice da seção](../README.pt-BR.md) · Próximo capítulo: Marcadores de tarefas
