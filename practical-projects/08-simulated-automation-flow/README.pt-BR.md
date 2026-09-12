# Fluxo Simulado de Automação

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

[← Voltar para Projetos Práticos](../README.pt-BR.md)

Este é o **Projeto 08 da Fase 10: Projetos Práticos** e o último projeto planejado da fase.

O projeto modela um pequeno orquestrador de automação com validação real, transições de estado, logs, evidências, propagação de falhas e contratos do resultado final, mantendo todas as integrações externas simuladas.

O cenário é original e fictício. Ele não reproduz nenhuma empresa, cliente, sistema, credencial ou fluxo privado real.

## O que você vai praticar

Este projeto combina conceitos de toda a trilha:

- modelagem imutável com `dataclass`;
- estados controlados com `StrEnum`;
- contratos explícitos de entrada e normalização;
- orquestração determinística;
- planos de execução ordenados;
- comportamento fail-fast;
- logs estruturados de eventos;
- evidências estruturadas;
- validação de invariantes;
- simulação local pura em vez de integrações externas;
- renderização textual estável;
- cobertura de regressão com pytest.

## Cenário fictício

Uma requisição local contém um identificador e uma tupla de itens fictícios de trabalho:

```python
AutomationRequest(
    request_id="DEMO-001",
    items=("alpha", "beta", "gamma"),
)
```

O orquestrador executa quatro etapas fixas:

```text
prepare
   ↓
process
   ↓
verify
   ↓
finalize
```

Uma execução bem-sucedida publica os itens em letras maiúsculas. Uma política controlada de simulação pode forçar uma etapa a falhar para demonstrar propagação de falha sem depender de APIs, arquivos, credenciais, agendadores ou sistemas remotos reais.

## Requisitos

O fluxo deve:

1. aceitar apenas um `AutomationRequest` validado;
2. exigir um identificador imprimível e não vazio;
3. exigir uma tupla não vazia de itens imprimíveis;
4. remover espaços externos do identificador e dos itens;
5. rejeitar itens duplicados após normalização;
6. executar a ordem canônica `prepare → process → verify → finalize`;
7. emitir eventos determinísticos de `started` e término para etapas executadas;
8. produzir evidência estruturada apenas para etapas bem-sucedidas;
9. permitir injeção determinística de falha em exatamente uma etapa escolhida;
10. interromper a execução após falha e marcar etapas posteriores como `skipped`;
11. preservar evidências produzidas antes da falha;
12. publicar saída somente quando toda a execução for bem-sucedida;
13. validar invariantes do resultado mesmo quando objetos forem construídos diretamente;
14. renderizar relatório textual estável sem timestamps, aleatoriedade ou endereços de memória.

## Escopo deliberado

O projeto usa esta regra:

> **Orquestrador real, integrações simuladas.**

O fluxo de controle é real e testável. O mundo externo fica propositalmente fora.

Fora do escopo:

- SAP ou qualquer sistema corporativo;
- APIs HTTP;
- credenciais ou segredos;
- bancos de dados;
- acesso à rede;
- automação via subprocessos;
- GUI ou RPA;
- threads ou `asyncio`;
- agendadores;
- retry e backoff;
- aleatoriedade;
- atrasos reais.

Assim, o foco permanece nos contratos de orquestração e não na infraestrutura.

## Estrutura

```text
08-simulated-automation-flow/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── automation_flow.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_automation_flow.py
```

## Modelo principal

### `AutomationRequest`

Armazena a entrada imutável e validada:

```python
AutomationRequest("RUN-001", ("alpha", "beta"))
```

O modelo remove espaços externos, rejeita texto vazio ou não imprimível, exige uma tupla com pelo menos um item e rejeita duplicidades após normalização.

### `StepName`

O plano canônico é fixo:

```text
PREPARE
PROCESS
VERIFY
FINALIZE
```

Uma ordem fixa torna execução e testes determinísticos.

### `StepStatus`

Cada etapa termina em exatamente um estado:

```text
SUCCEEDED
FAILED
SKIPPED
```

Uma etapa `skipped` não foi executada porque uma etapa anterior falhou.

### `RunStatus`

A execução completa é:

```text
SUCCEEDED
FAILED
```

Sucesso exige todas as etapas bem-sucedidas. Falha exige exatamente uma etapa com falha, todas as anteriores bem-sucedidas e todas as posteriores puladas.

### `AutomationEvent`

Os eventos funcionam como log determinístico.

Em vez de timestamps, cada evento recebe uma sequência contínua:

```text
001 prepare started
002 prepare succeeded
003 process started
004 process succeeded
```

Isso evita que duas execuções idênticas produzam logs diferentes apenas por causa do relógio.

### `Evidence`

Etapas bem-sucedidas produzem evidências estruturadas, por exemplo:

```text
prepare.input_count=3
process.transformation=uppercase
verify.verification=count-and-uniqueness
finalize.result=ready
```

Etapas com falha ou puladas não podem publicar evidência.

### `AutomationResult`

O resultado imutável contém:

- requisição validada original;
- status final;
- resultados das quatro etapas;
- log ordenado de eventos;
- itens de saída quando houver sucesso.

A propriedade `evidence` expõe todas as evidências bem-sucedidas na ordem de execução.

## Pipeline da automação

```text
entrada
  ↓
validação da requisição
  ↓
plano canônico
  ↓
prepare
  ↓
process
  ↓
verify
  ↓
finalize
  ↓
status + eventos + evidências + saída
```

Se uma etapa falhar:

```text
etapas anteriores com sucesso
            ↓
        etapa falha
            ↓
   etapas restantes puladas
            ↓
      resultado failed
```

Evidências anteriores são preservadas, mas a saída não é publicada.

## Contrato de processamento

Nesta simulação educacional, `process` transforma cada item em maiúsculas:

```text
alpha -> ALPHA
beta  -> BETA
```

A transformação é simples de propósito. O aprendizado está na orquestração em volta do trabalho.

## Injeção controlada de falha

`SimulationPolicy` pode escolher uma etapa para falhar:

```python
SimulationPolicy(fail_at=StepName.VERIFY)
```

A política é explícita e determinística. Ela substitui falhas aleatórias ou timeouts artificiais.

Exemplo:

```text
prepare   -> succeeded
process   -> succeeded
verify    -> failed
finalize  -> skipped
run       -> failed
```

As evidências de `prepare` e `process` permanecem disponíveis.

## Exemplo básico

```python
from automation_flow import AutomationRequest, run_automation

request = AutomationRequest(
    request_id="RUN-001",
    items=("alpha", "beta"),
)

result = run_automation(request)

print(result.status)
print(result.output_items)
```

Saída lógica:

```text
succeeded
('ALPHA', 'BETA')
```

## Demo

Execute a partir deste diretório:

```bash
python demo.py
```

O demo executa dois cenários determinísticos:

1. execução completa com sucesso;
2. falha controlada em `verify`.

Ele é não interativo, sem rede e usa apenas dados fictícios em memória.

## Caminhos de falha

Entrada inválida falha antes da orquestração:

```python
AutomationRequest("", ("alpha",))
```

gera `ValueError`.

```python
AutomationRequest("RUN-001", [])
```

gera `TypeError`, porque listas mutáveis não são aceitas silenciosamente.

```python
AutomationRequest("RUN-001", (" alpha ", "alpha"))
```

gera `ValueError`, porque a normalização criaria duplicidade.

Uma falha simulada durante a execução é diferente de entrada inválida. Ela retorna um `AutomationResult` válido com `RunStatus.FAILED`.

A distinção é importante:

- **contrato inválido** → exceção;
- **requisição válida com falha de execução** → resultado estruturado de falha.

## Invariantes do resultado

O próprio resultado valida sua consistência.

Estados impossíveis rejeitados incluem:

- sucesso com etapa falha;
- falha sem exatamente uma etapa falha;
- etapa bem-sucedida depois da falha;
- saída publicada por execução falha;
- ordem incorreta de etapas;
- sequência de eventos não contínua;
- eventos incompatíveis com os estados das etapas;
- evidência em etapas falhas ou puladas.

O objetivo é dificultar a representação de estados inválidos.

## Erros comuns

### Usar `print()` como único log

Texto impresso ajuda pessoas, mas é fraco como contrato de programa. Armazene eventos estruturados primeiro e renderize depois.

### Adicionar timestamps reais a um exercício determinístico

Tempo cria ruído em testes de igualdade. Sequências numéricas mostram ordem sem introduzir não determinismo.

### Continuar após falha sem política declarada

Quando etapas posteriores dependem das anteriores, continuar silenciosamente pode gerar resultados enganosos. O projeto usa fail-fast explícito.

### Perder evidências anteriores

Uma falha não deve apagar o que já foi concluído. Preservar evidência torna a execução explicável.

### Misturar validação com falha de runtime

Entrada ruim deve falhar imediatamente. Uma requisição válida que falha durante execução deve retornar um resultado de falha estruturado.

### Simular sistemas externos de forma literal demais

Credenciais falsas, telas SAP falsas, `sleep()` e mocks de rede podem desviar a atenção da lição principal. Este projeto modela a fronteira de orquestração em vez de imitar sistemas externos.

## Testes

Execute a suíte focada a partir da raiz do repositório:

```bash
python -m pytest -q practical-projects/08-simulated-automation-flow/tests
```

A suíte inicial cobre normalização, duplicidades, fronteiras imutáveis, sucesso determinístico, os quatro pontos de falha, fail-fast, etapas puladas, preservação de evidência, regras de saída, invariantes, sequência de eventos, contratos de tipo e renderização estável.

## Exercício

Troque os itens do demo para:

```python
("north", "south", "west", "east")
```

Antes de executar, preveja:

1. `input_count`;
2. `processed_count`;
3. a tupla final de saída;
4. a quantidade de eventos em uma execução bem-sucedida.

Depois injete falha em `PROCESS` e preveja quais etapas serão puladas e quais evidências permanecerão.

## Desafios de extensão

1. Adicione uma quinta etapa e atualize as invariantes.
2. Troque uppercase por uma função pura de processamento configurável.
3. Adicione uma política de retry mantendo a ordem de eventos determinística.
4. Adicione durações fornecidas por um relógio falso.
5. Adicione serialização JSON do resultado.
6. Adicione outro renderer sem alterar a orquestração.
7. Evolua de fluxo linear para dependências explícitas entre etapas.

## Discussão para portfólio

Este projeto mostra como modelar automação como contratos de software em vez de uma sequência de efeitos colaterais improvisados.

Pontos úteis para explicar:

- estado explícito de orquestração;
- modelos imutáveis de requisição e resultado;
- execução determinística;
- logs e evidências estruturados;
- propagação fail-fast;
- semântica de etapas puladas;
- distinção entre validação e falha de execução;
- design orientado a invariantes;
- limites seguros de simulação;
- testes de caminhos de sucesso e falha.

## Referência rápida

```text
Entrada:       AutomationRequest
Etapas:        prepare -> process -> verify -> finalize
Processamento: transformação para maiúsculas
Estados etapa: succeeded / failed / skipped
Estados run:   succeeded / failed
Logs:          AutomationEvent ordenado
Evidência:     apenas etapas bem-sucedidas
Falha:         SimulationPolicy determinística
Após falha:    etapas restantes são puladas
Saída:         publicada somente após sucesso completo
I/O externo:   nenhum
```

## Linha de chegada da Fase 10

Este é o último projeto prático planejado da Fase 10. Depois que implementação, documentação, CI e ciclo de review estiverem concluídos, a fase de projetos práticos poderá ser marcada como concluída.
