# Fluxo Fictício de Conciliação

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Voltar para Projetos Práticos](../README.pt-BR.md)

Este é o **Projeto 07 da Fase 10: Projetos Práticos**. Ele transforma duas coleções fictícias de registros em um relatório de conciliação explícito e determinístico.

O exemplo é original e fictício. Ele não reproduz nenhuma empresa real, cliente, sistema contábil ou fluxo privado.

## O que você vai praticar

Este projeto combina conceitos das fases anteriores:

- modelagem imutável com `dataclass`;
- estados controlados com `StrEnum`;
- dinheiro exato com `Decimal`;
- dicionários como índices de consulta;
- sets para a união das chaves de conciliação;
- ordenação determinística;
- validação e exceções deliberadas;
- funções com fronteiras claras de entrada e saída;
- cobertura com pytest;
- separação entre lógica de domínio e apresentação.

## Cenário fictício

Duas fontes imaginárias deveriam conter as mesmas referências e valores.

Fonte Norte:

| Referência | Valor |
|---|---:|
| `REF-001` | `150.00` |
| `REF-002` | `275.50` |
| `REF-003` | `100.00` |

Fonte Sul:

| Referência | Valor |
|---|---:|
| `REF-001` | `150.00` |
| `REF-002` | `270.50` |
| `REF-004` | `100.00` |

As classificações esperadas são:

```text
REF-001 -> matched
REF-002 -> amount_mismatch
REF-003 -> left_only
REF-004 -> right_only
```

Para registros encontrados nos dois lados, a diferença com sinal é:

```text
difference = left.amount - right.amount
```

Assim, `275.50 - 270.50` resulta em `5.00`.

## Requisitos

O fluxo deve:

1. aceitar dois iteráveis de `ReconciliationRecord`;
2. rejeitar identificadores de referência vazios;
3. exigir valores `Decimal` finitos;
4. aceitar somente valores exatamente representáveis em precisão de centavos;
5. remover espaços ao redor dos identificadores;
6. canonicalizar os valores aceitos para duas casas decimais;
7. rejeitar referências duplicadas dentro de qualquer fonte;
8. comparar identificadores de forma exata e sensível a maiúsculas/minúsculas;
9. classificar cada referência como `matched`, `amount_mismatch`, `left_only` ou `right_only`;
10. preservar a diferença com sinal nas divergências de valor;
11. ordenar a saída pelo identificador;
12. gerar contagens de resumo determinísticas;
13. calcular a magnitude absoluta total das divergências;
14. renderizar um relatório de texto estável.

## Escopo deliberado

A primeira versão começa **depois da ingestão**.

Ela não faz parsing de CSV, planilhas, APIs, bancos de dados nem dados privados. Essas camadas podem ser adicionadas depois como extensões.

Separar a ingestão mantém visível a pergunta principal:

> Dadas duas coleções já validadas, como a conciliação deve se comportar?

## Estrutura

```text
07-fictional-reconciliation-workflow/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── demo.py
├── reconciliation.py
└── tests/
    ├── conftest.py
    └── test_reconciliation.py
```

## Modelo principal

### `ReconciliationRecord`

```python
ReconciliationRecord(
    reference_id="REF-001",
    amount=Decimal("150.00"),
)
```

O registro:

- remove espaços ao redor do identificador;
- rejeita identificadores vazios;
- exige um `Decimal` real;
- rejeita `NaN` e infinitos;
- rejeita valores além da precisão de centavos;
- armazena valores aceitos no formato canônico de duas casas.

Valores negativos são permitidos porque um fluxo genérico pode representar estornos ou ajustes.

### `ReconciliationStatus`

Os estados controlados são:

```python
MATCHED
AMOUNT_MISMATCH
LEFT_ONLY
RIGHT_ONLY
```

### `ReconciliationItem`

Cada chave conciliada possui uma forma válida:

| Status | Esquerda | Direita | Diferença |
|---|---|---|---|
| `MATCHED` | sim | sim | zero |
| `AMOUNT_MISMATCH` | sim | sim | diferente de zero |
| `LEFT_ONLY` | sim | não | ausente |
| `RIGHT_ONLY` | não | sim | ausente |

A dataclass valida essas invariantes em vez de confiar que o chamador monte um resultado consistente.

### `ReconciliationSummary`

O resumo armazena:

- total de itens;
- itens conciliados;
- divergências de valor;
- itens exclusivos da esquerda;
- itens exclusivos da direita;
- diferença absoluta total das divergências.

As diferenças individuais mantêm seu sinal. O agregado usa valores absolutos para que uma divergência de `+5.00` e outra de `-5.00` não se anulem incorretamente.

### `ReconciliationReport`

O relatório agrupa os nomes das fontes, os itens ordenados e o resumo. A renderização acontece depois, então a lógica de comparação não fica presa ao texto.

## Pipeline de conciliação

```text
validar rótulos das fontes
        ↓
indexar fonte esquerda
        ↓
indexar fonte direita
        ↓
rejeitar duplicados
        ↓
unir todos os identificadores
        ↓
ordenar identificadores
        ↓
classificar cada identificador
        ↓
calcular diferenças
        ↓
construir resumo
        ↓
retornar relatório imutável
```

Dicionários são úteis porque fornecem consulta direta pela chave de conciliação e tornam a detecção de duplicados explícita.

## Contrato de matching

Os identificadores são comparados depois da remoção dos espaços ao redor.

O matching é exato e sensível a maiúsculas/minúsculas:

```text
REF-001 != ref-001
```

Essa é uma decisão do projeto, não uma regra universal. Se um domínio exigir normalização de caixa, chaves compostas ou outra regra, ela deve ser declarada antes da conciliação.

## Por que `Decimal`?

Para valores monetários, o projeto usa:

```python
Decimal("275.50")
```

em vez de `float`.

Criar `Decimal` a partir de texto preserva o valor decimal pretendido. O registro então aplica a fronteira monetária de duas casas do projeto.

## Exemplo básico

```python
from decimal import Decimal

from reconciliation import ReconciliationRecord, reconcile

left = (
    ReconciliationRecord("REF-001", Decimal("150.00")),
    ReconciliationRecord("REF-002", Decimal("275.50")),
)

right = (
    ReconciliationRecord("REF-001", Decimal("150.00")),
    ReconciliationRecord("REF-002", Decimal("270.50")),
)

report = reconcile(left, right)

for item in report.items:
    print(item.reference_id, item.status)
```

Saída lógica:

```text
REF-001 matched
REF-002 amount_mismatch
```

## Demonstração

Execute a partir desta pasta:

```bash
python demo.py
```

A demo é determinística, não interativa, sem rede e usa apenas dados fictícios em memória.

Ela produz os quatro estados importantes e um resumo.

## Caminhos de falha

O fluxo falha deliberadamente quando seu contrato de entrada é ambíguo ou inválido.

Exemplos:

```python
ReconciliationRecord("", Decimal("10.00"))
```

gera `ValueError`.

```python
ReconciliationRecord("REF-001", 10.00)
```

gera `TypeError`, pois floats não são convertidos silenciosamente.

```python
ReconciliationRecord("REF-001", Decimal("10.001"))
```

gera `ValueError`, pois o valor ultrapassa a precisão de centavos.

Referências duplicadas dentro de uma fonte também geram `ValueError`. O fluxo não tenta adivinhar se o primeiro ou o último duplicado deve prevalecer.

## Erros comuns

### Comparar linhas pela posição

Os mesmos registros lógicos podem chegar em ordens diferentes. Concilie por uma chave estável, não pela posição na lista.

### Sobrescrever duplicados silenciosamente

Uma atribuição normal em dicionário pode esconder registros duplicados. Este projeto detecta a duplicidade antes que a inserção sobrescreva silenciosamente.

### Usar valor absoluto cedo demais

`abs(left - right)` remove a direção. Preserve a diferença com sinal em cada item e use valores absolutos somente na métrica de resumo.

### Misturar comparação e impressão

Retornar resultados estruturados facilita testes e permite outros renderizadores no futuro.

### Adicionar normalização sem contrato

Alterar caixa, usar fuzzy matching, remover pontuação ou zeros à esquerda pode unir identificadores diferentes. Trate normalização como decisão explícita de domínio.

## Testes

Execute a suíte focada a partir da raiz do repositório:

```bash
python -m pytest -q practical-projects/07-fictional-reconciliation-workflow/tests
```

Os testes iniciais cobrem validação, duplicidade, os quatro status, diferenças positivas e negativas, generators, ordenação determinística, rótulos de fonte, sensibilidade a caixa, invariantes dos itens, entrada vazia, resumos e renderização determinística.

## Exercício

Adicione `REF-005` às duas fontes da demo com valores diferentes.

Antes de executar, preveja:

1. o status;
2. a diferença com sinal;
3. a nova quantidade de divergências;
4. a nova diferença absoluta total.

Depois execute a demo e compare sua previsão com o relatório real.

## Desafios de extensão

Depois que o contrato base estiver claro, tente uma extensão por vez:

1. Adicione uma tolerância `Decimal` configurável e teste exatamente sua fronteira.
2. Adicione uma camada de ingestão CSV que produza registros validados antes da conciliação.
3. Substitua a referência simples por uma chave composta como `(reference_id, period)`.
4. Adicione um renderer Markdown sem alterar `reconcile()`.
5. Exporte somente itens não resolvidos, preservando o relatório canônico completo.
6. Introduza um objeto de política de conciliação em vez de muitos flags booleanos sem relação.

## Discussão de portfólio

Este projeto demonstra como transformar um problema genérico de comparação em contratos explícitos de software.

Pontos úteis para explicar em um portfólio:

- chaves de domínio estáveis;
- valores monetários exatos;
- rejeição de duplicados;
- consulta indexada;
- estados e ordenação determinísticos;
- diferenças com sinal e métricas agregadas;
- resultados imutáveis;
- separação entre conciliação e renderização;
- testes automatizados focados em fronteiras.

## Referência rápida

```text
Entrada:      dois iteráveis de ReconciliationRecord
Chave:        reference_id normalizado
Matching:     exato e sensível a maiúsculas/minúsculas
Dinheiro:     Decimal finito em precisão de centavos
Status:       matched / amount_mismatch / left_only / right_only
Diferença:    left.amount - right.amount
Ordenação:    reference_id crescente
Duplicados:   rejeitados dentro de cada fonte
Saída:        ReconciliationReport imutável
```

## Próximo projeto

Depois que este projeto for revisado, a Fase 10 continua com o **Projeto 08: Fluxo Simulado de Automação**.
