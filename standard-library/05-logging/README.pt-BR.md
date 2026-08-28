<div align="center">

# Projetando Pipelines de Logging e Contratos de Contexto em Runtime

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Biblioteca Padrão](../README.pt-BR.md) · [← Capítulo anterior: CSV](../04-csv/README.pt-BR.md)

O capítulo anterior sobre logging na Fase 6 apresentou a finalidade do logging, os níveis padrão, loggers de módulo, configuração sob responsabilidade da aplicação, handlers, formatters, propagação, logging de exceções, privacidade e a diferença entre logs e comentários.

Este capítulo aprofunda o assunto. O foco deixa de ser apenas **qual mensagem devo registrar?** e passa a incluir:

```text
Como um LogRecord percorre o grafo de logging,
qual componente pode alterá-lo
e qual contrato de runtime a aplicação promete?
```

O pacote `logging` é flexível porque separa criação de eventos, filtragem, roteamento, formatação e saída. Essa flexibilidade só ajuda quando a configuração é tratada como um projeto explícito de sistema, e não como uma coleção de chamadas espalhadas a `basicConfig()`.

**Tempo estimado de estudo:** 150–190 minutos.

**Requisito de Python:** Python 3.10 ou mais recente para o conteúdo central e os exemplos executáveis. Seções específicas de versão identificam recursos adicionados no Python 3.12, 3.13 e 3.14.

**Base da documentação:** comportamentos e notas de versão foram conferidos com a documentação oficial do Python 3.14 para `logging`, `logging.config`, `logging.handlers`, Logging HOWTO e Logging Cookbook.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- modelar logging como um pipeline que transporta objetos `LogRecord`;
- distinguir limites de logger, níveis efetivos, limites de handler, filtros e propagação;
- explicar por que níveis de loggers ancestrais não são reaplicados durante a propagação;
- diagnosticar registros duplicados ou que desaparecem inesperadamente;
- usar `basicConfig(force=True)` deliberadamente ao substituir uma configuração existente do root;
- criar dicionários explícitos de `dictConfig()` sem desabilitar loggers preexistentes por acidente;
- explicar o que uma configuração incremental pode e não pode alterar;
- distinguir o estilo do formatter da interpolação da mensagem na chamada de logging;
- adicionar campos de contexto sem colidir com atributos nativos de `LogRecord`;
- escolher entre `extra`, `LoggerAdapter`, filtros, `contextvars` e uma record factory;
- preservar a identificação do chamador em helpers de logging com `stacklevel`;
- distinguir `exc_info` de `stack_info`;
- evitar trabalho caro para níveis de logging desabilitados;
- entender a política de erro dos handlers e `logging.raiseExceptions`;
- mover trabalho lento de handlers para trás de `QueueHandler` e `QueueListener` quando apropriado;
- raciocinar sobre threads, processos, rotação de arquivos e designs de writer único;
- reconhecer padrões inseguros de configuração dinâmica de logging;
- testar o comportamento de logging como contrato da aplicação, e não como texto incidental.

## 1. O que este capítulo acrescenta depois da Fase 6

A Fase 6 ensinou a interface do dia a dia:

```python
import logging


logger = logging.getLogger(__name__)
logger.info("Processed %s records", record_count)
```

Isso continua correto. Este capítulo estuda o que acontece ao redor dessa chamada:

```text
call site
   ↓
logger eligibility
   ↓
LogRecord creation
   ↓
logger filters
   ↓
handlers on this logger
   ↓
propagation to ancestor handlers
   ↓
handler levels and filters
   ↓
formatter
   ↓
destination
```

Os detalhes importam quando uma aplicação real tem vários pacotes, bibliotecas de terceiros, múltiplos destinos, trabalho assíncrono, worker threads, verbosidade dinâmica ou contexto estruturado.

## 2. Um evento de logging vira um `LogRecord`

Quando um logger aceita um evento, o Python representa esse evento como um `LogRecord`.

O registro carrega informações como:

- nome do logger;
- nível numérico e textual;
- template da mensagem e argumentos;
- pathname de origem, nome da função e número da linha;
- informações de processo e thread;
- informações opcionais de exceção ou stack;
- atributos personalizados fornecidos por mecanismos controlados de contexto.

Formatters e handlers consomem esse registro depois.

Um modelo mental útil é:

```text
logging call = event request
LogRecord    = event data object
handler      = delivery policy
formatter    = output representation
```

Não trate a linha de texto já renderizada como se fosse todo o sistema de logging. O registro existe antes da representação final.

## 3. Nomes de logger formam uma hierarquia

Nomes de logger usam uma hierarquia separada por pontos:

```python
import logging


root = logging.getLogger()
service = logging.getLogger("app.service")
worker = logging.getLogger("app.service.worker")
```

`app.service.worker` é descendente de `app.service`, que é descendente de `app`, que finalmente chega ao root logger.

Por isso `logging.getLogger(__name__)` combina naturalmente com pacotes Python. Um módulo como:

```text
catalog.importer.csv_reader
```

pode participar da hierarquia:

```text
catalog
catalog.importer
catalog.importer.csv_reader
```

A hierarquia é um namespace de roteamento. Isso não significa que objetos logger precisem ser passados como dependências. Chamadas repetidas a `getLogger()` com o mesmo nome retornam o mesmo objeto logger.

## 4. `NOTSET` significa herança em loggers que não são root

Novos loggers que não são root normalmente começam em `NOTSET`.

Para um logger não root, `NOTSET` não significa "não registre nada". Significa que o Python sobe pela hierarquia até encontrar um ancestral com nível explícito, ou chegar ao root.

```python
import logging


root = logging.getLogger()
root.setLevel(logging.WARNING)

logger = logging.getLogger("app.worker")
logger.setLevel(logging.NOTSET)

print(logger.getEffectiveLevel() == logging.WARNING)
```

O root logger começa em `WARNING`, a menos que a configuração o altere.

Essa distinção explica muitos bugs do tipo "por que meu registro INFO sumiu?".

## 5. A elegibilidade no logger acontece antes da entrega

Primeiro o logger decide se o evento está habilitado.

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug("Cache snapshot size=%s", cache_size)
```

`isEnabledFor()` considera:

1. o override global estabelecido por `logging.disable()`;
2. o nível efetivo do logger.

Se o evento não passar por essa etapa, um `LogRecord` normal não é criado para entrega aos handlers.

Isso é diferente de um handler rejeitar o registro depois.

## 6. Níveis de handler são um segundo limite

Um logger pode aceitar um registro enquanto um handler específico o rejeita.

```python
import logging


logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
```

Aqui:

```text
DEBUG event
  logger accepts it
  handler rejects it

WARNING event
  logger accepts it
  handler accepts it
```

Esse modelo em duas etapas permite designs como:

```text
logger: DEBUG
console handler: INFO
file handler: DEBUG
alert handler: ERROR
```

O logger controla se o evento entra no pipeline de entrega. Cada handler controla se aquele destino recebe o evento.

## 7. A propagação não verifica novamente os níveis dos loggers ancestrais

Esse detalhe é fácil de perder.

Quando um registro se propaga a partir de um logger filho, o Python o oferece diretamente aos handlers anexados aos loggers ancestrais. Os níveis e filtros desses objetos **logger ancestrais** não são reaplicados durante a propagação.

Os handlers continuam aplicando seus próprios níveis e filtros.

Conceitualmente:

```text
app.worker logger accepts INFO
        ↓
record created
        ↓
app.worker handlers
        ↓ propagate=True
app handlers receive record directly
        ↓
root handlers receive record directly
```

Não suponha que definir o logger ancestral como `ERROR` filtrará registros já aceitos pelos descendentes e propagados aos handlers dele. Coloque os limites de destino nos handlers quando essa for a política necessária.

## 8. Registros duplicados normalmente são um problema do grafo

Considere esta configuração:

```python
import logging


handler = logging.StreamHandler()

root = logging.getLogger()
root.addHandler(handler)

child = logging.getLogger("app.worker")
child.addHandler(handler)
child.propagate = True
```

Um registro emitido por `app.worker` pode chegar ao mesmo handler pelo filho e novamente pelo caminho do ancestral.

Um bom padrão inicial é:

```text
application entry point configures shared handlers high in the hierarchy
modules create loggers
modules do not attach duplicate visible handlers
propagation remains enabled unless isolation is intentional
```

Definir `propagate = False` pode resolver uma fronteira de roteamento deliberada, mas não é um botão universal de remover duplicidade. Um logger com propagação desativada também deixa de alcançar handlers ancestrais.

## 9. `hasHandlers()` acompanha as fronteiras de propagação

`logger.hasHandlers()` verifica o próprio logger e sobe pelos ancestrais.

A busca para ao encontrar um logger cujo `propagate` seja `False`.

```python
import logging


logger = logging.getLogger("app.worker")
print(isinstance(logger.hasHandlers(), bool))
```

Esse método responde se a hierarquia atual consegue encontrar um handler pelo caminho de propagação. Ele não promete que todo registro será emitido, porque níveis e filtros ainda podem rejeitá-lo.

## 10. `basicConfig()` é simples de propósito

`basicConfig()` é útil para aplicações pequenas e ferramentas de linha de comando, mas configura o root logger e tem um comportamento de ciclo de vida que importa.

Por padrão, se o root logger já tiver handlers, outra chamada a `basicConfig()` não faz nada.

```python
import logging


logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

print(logging.getLogger().level == logging.WARNING)
```

Isso pode surpreender em notebooks, processos de teste, hosts de plugins ou aplicações cujas dependências já tocaram em logging.

## 11. `force=True` substitui handlers existentes do root

Desde Python 3.8, `basicConfig(force=True)` remove e fecha handlers existentes do root antes de aplicar a nova configuração básica.

```python
import logging


logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.INFO, force=True)

print(logging.getLogger().level == logging.INFO)
```

Use `force=True` quando a aplicação deliberadamente controla a configuração global do processo e pretende substituí-la.

Não use isso casualmente dentro de bibliotecas reutilizáveis. Pode apagar configuração instalada pela aplicação hospedeira.

## 12. `dictConfig()` torna explícito o grafo de objetos

Para aplicações maiores, `logging.config.dictConfig()` pode descrever formatters, filters, handlers, loggers e root logger em um único objeto de configuração.

Um dicionário de configuração exige `version`, e a versão de schema suportada atualmente é `1`.

```python
import logging.config


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "brief": {
            "format": "%(levelname)s:%(name)s:%(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "brief",
            "level": "INFO",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
}

logging.config.dictConfig(config)
```

O benefício não é que dicionários sejam mágicos. O benefício é que o grafo de logging vira configuração inspecionável em vez de mutações espalhadas pelo código.

## 13. Seja explícito com `disable_existing_loggers`

Uma omissão perigosa em `dictConfig()` é esquecer esta chave:

```python
"disable_existing_loggers": False,
```

Se a chave estiver ausente, loggers existentes que não são root são tratados como desabilitados, salvo quando eles ou um ancestral são nomeados explicitamente conforme as regras da configuração.

Em uma aplicação que importa bibliotecas antes de configurar logging, o padrão histórico `True` pode silenciar loggers que já existem.

Orientação do projeto:

```text
If preserving pre-existing library loggers is intended,
write disable_existing_loggers=False explicitly.
```

Não dependa de alguém lembrar desse padrão histórico.

## 14. Configuração incremental é deliberadamente limitada

`dictConfig()` suporta:

```python
incremental_config = {
    "version": 1,
    "incremental": True,
    "handlers": {
        "console": {"level": "WARNING"},
    },
    "root": {
        "level": "WARNING",
    },
}
```

Mas o modo incremental **não** reconstrói todo o grafo de objetos de logging.

Quando `incremental` é verdadeiro, o Python ignora as entradas de `formatters` e `filters`. Ele processa `level` dos handlers e `level` mais `propagate` dos loggers/root.

Use configuração incremental para mudanças controladas de verbosidade, não como mecanismo geral de hot reload para topologia arbitrária de handlers e formatters.

## 15. Estilo do formatter e interpolação da mensagem são contratos diferentes

Um `Formatter` pode usar estilo `%`, `{` ou `$` para o **formato de saída**:

```python
import logging


formatter = logging.Formatter(
    "{levelname}:{name}:{message}",
    style="{",
)
```

Isso não altera o contrato normal de interpolação das chamadas de logger:

```python
logger.info("Processed %s records", record_count)
```

O template da mensagem e seus argumentos continuam usando a mesclagem `%` normal do pacote de logging.

Não conclua que isto:

```python
logger.info("Processed {} records", record_count)
```

passa a funcionar apenas porque o `Formatter(style="{")` do handler usa chaves. São camadas separadas.

## 16. `Formatter(validate=True)` detecta estilos incompatíveis

A validação do formatter fica habilitada por padrão.

```python
import logging


try:
    logging.Formatter("%(levelname)s:%(message)s", style="{")
except ValueError:
    print("format and style do not match")
```

A validação encontra o erro de configuração cedo, em vez de esperar um evento futuro expor o problema.

## 17. `Formatter(defaults=...)` pode definir campos de fallback seguros

Python 3.10 adicionou o argumento `defaults` ao `Formatter`.

```python
import logging


formatter = logging.Formatter(
    "%(request_id)s:%(message)s",
    defaults={"request_id": "-"},
)
```

Sem fallback, um formatter que exige um campo personalizado pode falhar ao receber registros que não possuem esse campo.

Defaults são úteis quando um handler recebe registros contextualizados e registros comuns. Não substituem a definição de um schema coerente quando sistemas consumidores exigem campos estruturados.

## 18. `extra` enriquece o `LogRecord`

Você pode adicionar atributos personalizados a um registro:

```python
logger.info(
    "Job started",
    extra={"job_id": "job-104", "component": "importer"},
)
```

Um formatter pode então referenciar esses campos:

```python
logging.Formatter(
    "%(levelname)s:%(job_id)s:%(component)s:%(message)s"
)
```

As chaves fornecidas por `extra` são inseridas no dicionário de atributos do registro.

## 19. Campos personalizados não podem colidir com atributos nativos do registro

Este é um design inválido:

```python
logger.info(
    "Job started",
    extra={"levelname": "CUSTOM"},
)
```

Nomes nativos como `levelname`, `name`, `message`, `pathname` e muitos outros pertencem ao `LogRecord`.

Escolha um namespace de aplicação claro e estável:

```text
request_id
job_id
component
tenant_code
operation
```

Não adicione segredos ou dados pessoais desnecessários apenas porque `extra` facilita isso.

## 20. `LoggerAdapter` carrega contexto repetido

Quando vários registros compartilham os mesmos valores de contexto, um adapter reduz repetição:

```python
import logging


logger = logging.getLogger("app.worker")
worker_logger = logging.LoggerAdapter(
    logger,
    {"job_id": "job-104"},
)

worker_logger.info("Started")
worker_logger.info("Validated input")
```

O adapter delega a um logger subjacente enquanto insere contexto.

Isso é útil para escopos como um job, request, conexão ou operação.

## 21. Python 3.13 adicionou `LoggerAdapter(merge_extra=True)`

Historicamente, o `extra` do próprio adapter prevalecia e um `extra` passado em uma chamada individual não era mesclado pela implementação padrão do adapter.

Python 3.13 adicionou `merge_extra`:

```python
import logging


base_logger = logging.getLogger("app.worker")
adapter = logging.LoggerAdapter(
    base_logger,
    {"job_id": "job-104"},
    merge_extra=True,
)

adapter.info(
    "Batch complete",
    extra={"batch_id": "batch-7"},
)
```

Se sua biblioteca ou aplicação suporta versões anteriores do Python, não publique configuração que silenciosamente dependa desse comportamento do 3.13.

## 22. Filters fazem mais do que responder sim ou não

Um logger ou handler pode possuir filtros.

Um filtro tradicional retorna um valor verdadeiro para manter um registro ou falso para rejeitá-lo:

```python
import logging


class IgnoreHealthChecks(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return getattr(record, "route", None) != "/health"
```

Filters são úteis quando limites de nível não conseguem expressar a política.

Exemplos incluem:

- descartar uma categoria muito ruidosa;
- permitir uma subárvore específica de loggers;
- injetar contexto controlado;
- contar registros que atravessam um destino específico.

## 23. Filters no Python 3.12 podem retornar um `LogRecord` substituto

A partir do Python 3.12, um filtro pode retornar uma instância de `LogRecord` para substituir o registro original no processamento seguinte daquele caminho.

Isso é especialmente útil em um handler quando você quer enriquecimento específico do destino sem alterar o registro visto por outros handlers.

```python
import copy
import logging


def add_destination(record: logging.LogRecord):
    cloned = copy.copy(record)
    cloned.destination = "console"
    return cloned
```

Poder substituir em vez de mutar um registro compartilhado reduz efeitos colaterais entre múltiplos handlers.

Documente o requisito de Python 3.12 se depender desse comportamento.

## 24. Uma factory de `LogRecord` pode adicionar contexto global do processo

O Python expõe a factory atual de registros:

```python
import logging


old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.application = "study-guide"
    return record


logging.setLogRecordFactory(record_factory)
```

Uma factory afeta a criação de registros globalmente dentro do processo.

Esse poder exige cuidado. Encadear factories adiciona overhead, e bibliotecas independentes podem colidir se escolherem os mesmos nomes de atributos personalizados.

Prefira um filter ou adapter quando o contexto pertence apenas a um destino ou escopo.

## 25. Escolha o mecanismo de contexto mais restrito que resolva o problema

Uma tabela prática:

| Necessidade | Prefira |
|---|---|
| Uma chamada possui campos extras | `extra={...}` |
| Muitas chamadas de uma operação compartilham campos | `LoggerAdapter` |
| Um handler precisa de enriquecimento específico do destino | filter no handler |
| Contexto de request/task precisa fluir em código async/thread-aware | `contextvars` + adapter/filter |
| Todo registro criado precisa de um atributo global do processo | factory de `LogRecord`, com cuidado |

O mecanismo mais global não é automaticamente o mais conveniente.

## 26. `contextvars` pode carregar contexto de request ou task

`contextvars.ContextVar` é útil quando dados de contexto precisam acompanhar a execução lógica sem passar manualmente um logger por todas as funções.

```python
import contextvars
import logging


request_id_var = contextvars.ContextVar("request_id", default="-")


class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get()
        return True
```

Um handler usando esse filtro pode formatar `%(request_id)s`.

Esse padrão pode funcionar através de threads e tarefas assíncronas quando o contexto é gerenciado corretamente. Também mantém nomes de logger ligados às áreas do código, em vez de criar um logger novo por request.

## 27. Não crie um logger por request, arquivo ou cliente

Instâncias de logger são armazenadas em cache por nome e não são liberadas durante a execução normal do script.

Este padrão cria namespaces de logger sem limite:

```python
logger = logging.getLogger(f"request.{request_id}")
```

Prefira um logger estável:

```python
logger = logging.getLogger("app.request")
logger.info("Request started", extra={"request_id": request_id})
```

Nomes de logger normalmente identificam áreas de software. Campos de contexto identificam entidades individuais de runtime.

## 28. `stacklevel` preserva o chamador real através de helpers

Sem cuidado, um wrapper de logging pode fazer todos os registros parecerem originados no próprio helper.

```python
import logging


logger = logging.getLogger("app")


def log_notice(message: str) -> None:
    logger.info(message, stacklevel=2)
```

O chamador:

```python
def run_job() -> None:
    log_notice("Job started")
```

pode então aparecer como a origem em vez de `log_notice()`.

Isso é valioso quando helpers padronizam o formato do evento, mas a atribuição de origem ainda precisa apontar para o call site da aplicação.

## 29. `exc_info` e `stack_info` respondem perguntas diferentes

`exc_info` captura informação do traceback da exceção.

```python
try:
    int("not-a-number")
except ValueError:
    logger.error("Parsing failed", exc_info=True)
```

`stack_info=True` captura a stack atual que levou à chamada de logging, mesmo sem exceção:

```python
logger.debug("Reached diagnostic checkpoint", stack_info=True)
```

Pense assim:

```text
exc_info   → which frames were unwound by this exception?
stack_info → how did execution reach this logging call?
```

Podem ser usados independentemente.

## 30. Evite registrar a mesma exceção em todas as camadas

Uma camada inferior pode registrar e relançar:

```python
try:
    load_document()
except OSError:
    logger.exception("Document load failed")
    raise
```

Se todo chamador repetir o mesmo padrão, uma falha vira vários tracebacks quase idênticos.

Escolha uma fronteira que seja dona do registro operacional. Outras camadas só devem adicionar informação quando realmente trazem contexto novo ou mudam a decisão de tratamento.

Registrar uma exceção e tratá-la são responsabilidades separadas.

## 31. Formatação adiada não adia o cálculo de argumentos caros

Isto usa parametrização:

```python
logger.debug("Graph summary=%s", build_graph_summary())
```

mas `build_graph_summary()` ainda executa antes de `logger.debug()` ser chamado.

Proteja diagnósticos caros:

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug("Graph summary=%s", build_graph_summary())
```

Use isso quando preparar os argumentos for realmente custoso. Não envolva toda variável trivial em um `isEnabledFor()`.

## 32. `logging.disable()` é um override global do processo

`logging.disable(level)` desabilita todas as chamadas de logging naquela severidade e abaixo, independentemente dos níveis individuais dos loggers.

```python
import logging


logging.disable(logging.INFO)
# DEBUG and INFO calls are disabled process-wide.

logging.disable(logging.NOTSET)
# Remove the override.
```

Isso é diferente de alterar o nível efetivo de um logger.

Use supressão global com cautela porque ela também afeta hierarquias de logger não relacionadas.

## 33. `lastResort` explica warnings inesperados sem configuração

Se nenhum handler puder ser encontrado, o Python fornece `logging.lastResort`.

Ele é um `StreamHandler` em `WARNING` que escreve a mensagem pura em `sys.stderr`.

Isso explica por que uma biblioteca reutilizável ainda pode parecer imprimir warnings mesmo quando a aplicação hospedeira não configurou logging.

Uma biblioteca que intencionalmente queira silêncio nessa situação pode anexar `logging.NullHandler()` ao seu logger de nível superior, mas ainda deve deixar a configuração dos destinos visíveis para a aplicação.

## 34. Falhas de handler têm sua própria política de erro

Erros podem acontecer ao emitir um registro: um stream pode falhar, um formatter pode estar incorreto, um destino de rede pode ficar indisponível ou um handler customizado pode levantar exceção.

`logging.raiseExceptions` é consultado por `Handler.handleError()` quando um handler capturou uma exceção durante a emissão e encaminhou explicitamente essa falha pelo caminho padrão de erro dos handlers:

```python
logging.raiseExceptions
```

O padrão é `True`, útil no desenvolvimento porque `handleError()` pode tornar falhas de logging visíveis em `sys.stderr`. Definir como `False` é comum em produção quando os diagnósticos desse caminho de erro devem permanecer silenciosos.

Essa flag **não é uma proteção global contra qualquer exceção de handler**. Se uma implementação customizada ou de terceiros de `emit()` deixar uma exceção escapar, em vez de capturá-la e chamar `handleError()`, `logging.raiseExceptions = False` não impede que essa exceção se propague de volta para a chamada de logging.

Não confunda a flag com suprimir exceções da aplicação. Ela controla os diagnósticos produzidos pelo caminho padrão de `handleError()`; handlers customizados robustos ainda precisam de uma política explícita de falha.

## 35. Implementações personalizadas de `emit()` precisam respeitar as travas

Handlers usam locks durante a emissão.

Um `Handler.emit()` customizado que chama APIs de configuração de logging ou outras operações de logging que adquirem locks pode criar problemas de ordem de travamento com outra thread configurando logging.

Mantenha implementações personalizadas de `emit()` focadas na entrega. Evite reentrar na maquinaria de configuração de dentro da emissão do handler.

Se um destino tiver comportamento bloqueante complexo, uma fronteira por fila pode ser um design melhor.

## 36. Logging é thread-safe, mas handlers lentos ainda bloqueiam o chamador

O módulo padrão de logging usa locks para que múltiplas threads possam compartilhar a infraestrutura de logging com segurança dentro de um processo.

Thread safety não significa latência zero.

Um handler que realiza disco lento, rede, SMTP ou outro I/O bloqueante pode manter a thread chamadora ocupada enquanto emite o registro.

Para caminhos sensíveis a latência, desacople a criação do evento da entrega lenta.

## 37. `QueueHandler` move registros para uma fila

`logging.handlers.QueueHandler` envia registros para uma fila:

```python
import logging
import queue
from logging.handlers import QueueHandler


log_queue = queue.Queue()
queue_handler = QueueHandler(log_queue)

logger = logging.getLogger("app")
logger.addHandler(queue_handler)
```

O chamador enfileira em vez de executar diretamente o trabalho lento do destino.

Uma fila limitada pode encher. `QueueHandler` usa enqueue não bloqueante por padrão, e falhas seguem a política de erro dos handlers.

Capacidade de fila e política de descarte/bloqueio são decisões operacionais, não detalhes a ignorar.

## 38. `QueueListener` executa o trabalho dos handlers em outra thread

Um listener consome registros enfileirados e os encaminha para handlers reais:

```python
import logging
import queue
from logging.handlers import QueueHandler, QueueListener


log_queue = queue.Queue()
output_handler = logging.StreamHandler()
listener = QueueListener(
    log_queue,
    output_handler,
    respect_handler_level=True,
)

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(QueueHandler(log_queue))

listener.start()
try:
    logger.info("Job queued")
finally:
    listener.stop()
```

Com `respect_handler_level=True`, o listener verifica o nível de cada handler de destino antes de encaminhar o registro.

Esse padrão é útil em web services, sistemas de workers e aplicações assíncronas onde I/O bloqueante do handler não deve rodar no caminho sensível a latência.

## 39. Python 3.14 tornou `QueueListener` um context manager

Python 3.14 permite:

```python
with QueueListener(log_queue, output_handler) as listener:
    logger.info("Job queued")
```

Entrar no contexto inicia o listener. Sair dele o encerra.

O exemplo executável deste repositório usa `start()` / `stop()` explicitamente para continuar compatível com Python 3.10+, enquanto esta seção documenta a API mais recente.

## 40. `QueueHandler.prepare()` altera o que atravessa a fronteira da fila

A implementação base de `QueueHandler.prepare()` formata o registro para que ele possa ser enfileirado e serializado com pickle nos cenários comuns.

Essa preparação mescla mensagem e argumentos e remove informações como `args`, `exc_info` e `exc_text` que podem não ser serializáveis ou causar problemas de formatação posterior.

Se o lado do listener precisar de formatação personalizada de exceções ou de outro schema serializado, crie uma subclasse de `QueueHandler` e sobrescreva `prepare()` deliberadamente.

A fronteira da fila é um contrato de serialização. Não suponha que o listener recebe uma cópia intacta de todos os atributos originais do registro.

## 41. Cuidado com `multiprocessing.Queue` e seu logger interno

O módulo `multiprocessing` possui um logger interno. Um `multiprocessing.Queue` pode emitir registros `DEBUG` enquanto operações de fila acontecem.

Se esses registros internos forem roteados por um `QueueHandler` que usa a **mesma** fila de multiprocessing, o sistema pode entrar em recursão ou deadlock.

Ao combinar multiprocessing e filas de logging, projete a topologia do listener deliberadamente e siga o warning documentado de `QueueHandler` para multiprocessing.

## 42. Vários processos não devem escrever independentemente no mesmo file handler padrão

Logging é thread-safe dentro de um processo, mas a biblioteca padrão não fornece lock compartilhado entre processos para um único `FileHandler` usado por processos independentes.

Processos diferentes escrevendo o mesmo arquivo podem misturar saída ou interferir com rotação.

Uma arquitetura mais segura é:

```text
worker process ─┐
worker process ─┼─> queue/socket ─> single listener/writer ─> file
worker process ─┘
```

Centralize a escrita real do arquivo quando múltiplos processos precisarem contribuir para um único fluxo de log.

## 43. Rotating handlers são ferramentas de retenção, não coordenação multiprocess

A biblioteca padrão inclui:

- `RotatingFileHandler` para rollover baseado em tamanho;
- `TimedRotatingFileHandler` para rollover baseado em tempo.

```python
from logging.handlers import RotatingFileHandler


handler = RotatingFileHandler(
    "application.log",
    maxBytes=1_000_000,
    backupCount=5,
    encoding="utf-8",
)
```

Rotação controla crescimento dos arquivos e formato de retenção. Não torna writers independentes de múltiplos processos seguros.

Também defina quem controla retenção externa, compressão, envio ou exclusão. Uma configuração de rollover não é uma política completa de retenção de observabilidade.

## 44. Timestamps fazem parte do contrato de saída

Formatters usam horário local por padrão em `asctime`.

Para sistemas que exigem um timezone consistente, um formatter pode usar conversão UTC:

```python
import logging
import time


formatter = logging.Formatter(
    "%(asctime)sZ %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
formatter.converter = time.gmtime
```

Seja explícito sobre timezone quando logs circulam entre máquinas ou regiões.

Em testes determinísticos, evite afirmar o timestamp real atual a menos que o comportamento temporal seja o próprio contrato testado.

## 45. Campos de identidade de runtime dependem da versão

`LogRecord` inclui campos de thread e processo, e Python 3.12 adicionou `taskName` para nomes de `asyncio.Task` quando disponíveis.

Antes de adicionar um campo a todos os formatters, verifique as versões suportadas do Python e se o valor é significativo para todos os modelos de execução.

Um formatter que exige cegamente contexto opcional pode falhar. Use schema estável ou defaults de formatter quando apropriado.

## 46. `logging.captureWarnings()` pode rotear `warnings` pelo logging

O Python pode redirecionar warnings emitidos pelo módulo `warnings` para logging:

```python
import logging


logging.captureWarnings(True)
```

Esses registros usam o logger `py.warnings`.

Isso pode unificar destinos, mas também altera como a saída de warnings é roteada. A aplicação deve controlar essa decisão.

Não confunda `warnings.warn()` com `logger.warning()`: são APIs diferentes e podem ter consumidores e regras de filtragem diferentes.

## 47. Configuração dinâmica por socket possui uma fronteira de segurança

`logging.config.listen()` pode iniciar um servidor de socket local que recebe configuração de logging.

Esse recurso é poderoso porque configuração de logging pode referenciar ou construir objetos Python. Configuração não confiável pode, portanto, virar risco de execução de código em ambientes onde outro usuário ou processo local consegue enviar dados maliciosos.

Se esse mecanismo for usado, estude o callback `verify` e autentique ou rejeite bytes de configuração não confiáveis.

Não exponha configuração dinâmica de logging apenas porque mudar verbosidade remotamente parece conveniente.

## 48. Bibliotecas devem documentar nomes de logger, não tomar posse dos destinos

Uma biblioteca reutilizável deve informar em qual namespace de logger emite:

```text
examplelib
examplelib.client
examplelib.parser
```

Normalmente deve evitar:

- chamar `basicConfig()`;
- anexar handlers visíveis de arquivo, console, e-mail ou rede;
- substituir handlers do root;
- desabilitar globalmente outros loggers.

A aplicação hospedeira controla destinos e formatação.

Isso mantém a biblioteca componível em ferramentas CLI, aplicações web, notebooks, testes e plataformas maiores.

## 49. Schemas de logging devem ser estáveis o suficiente para operação

Mesmo logs em texto simples ganham com nomes de campos intencionais:

```text
operation=import job_id=job-104 records=87
```

Contratos úteis definem:

- significado do evento;
- política de severidade;
- identificadores de contexto estáveis;
- classificação de privacidade;
- política de timestamp e timezone;
- política de destino e retenção;
- se consumidores de máquina dependem de nomes de campos.

Não transforme toda frase em uma API pública permanente, mas também não torne aleatórios os campos operacionalmente importantes.

## 50. Privacidade vem antes da formatação

Um formatter não consegue salvar um registro que já contém um segredo desnecessário.

Evite inserir:

- senhas;
- chaves de API;
- headers de autorização;
- tokens de sessão;
- dados pessoais ou de pagamento completos;
- objetos brutos de request ou configuração que contenham segredos.

Redação deve ser defesa em profundidade, não permissão para coletar tudo primeiro.

Mecanismos de contexto como `extra`, adapters, filters e record factories precisam da mesma revisão de privacidade.

## 51. Teste contratos semânticos de logging

Testes devem verificar comportamento que importa.

Por exemplo:

```python
import logging
import unittest


class ImportTests(unittest.TestCase):
    def test_fallback_logs_warning(self):
        logger = logging.getLogger("app.importer")

        with self.assertLogs(logger, level="WARNING") as captured:
            logger.warning("Using fallback parser")

        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].levelno, logging.WARNING)
```

Prefira verificar o registro, severidade, nome do logger ou campos seguros obrigatórios em vez de congelar pontuação incidental do texto renderizado.

## 52. Restaure o estado de logging com cuidado nos testes

Configuração de logging é global ao processo o suficiente para um teste vazar handlers ou níveis para outro.

Estratégias possíveis incluem:

- configurar uma vez para o processo de teste;
- criar loggers nomeados isolados e restaurar atributos alterados;
- remover handlers adicionados por um teste no cleanup;
- usar `basicConfig(force=True)` apenas quando o teste intencionalmente controla o estado do root;
- evitar depender da ordem de execução dos testes.

Uma suíte verde não deve precisar de uma configuração de logger deixada por sorte por um teste anterior.

## 53. Exemplo prático: rotear registros com `dictConfig()`

```python
import logging
import logging.config
import sys


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "brief": {
            "format": "%(levelname)s:%(name)s:%(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "brief",
            "level": "INFO",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "study.service": {
            "level": "INFO",
            "propagate": True,
        }
    },
    "root": {
        "level": "WARNING",
        "handlers": ["console"],
    },
}

logging.config.dictConfig(config)

service_logger = logging.getLogger("study.service")
dependency_logger = logging.getLogger("study.dependency")

service_logger.info("service started")
dependency_logger.info("hidden detail")
dependency_logger.warning("slow response")
```

Versão executável: [`examples/dict_config_routing.py`](examples/dict_config_routing.py).

## 54. Exemplo prático: injetar contexto de escopo

```python
import contextvars
import logging
import sys


request_id_var = contextvars.ContextVar("request_id", default="-")


class RequestContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_var.get()
        return True


logger = logging.getLogger("study.context")
logger.setLevel(logging.INFO)
logger.propagate = False

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(
    logging.Formatter("%(levelname)s:%(request_id)s:%(message)s")
)
handler.addFilter(RequestContextFilter())
logger.addHandler(handler)

request_id_var.set("req-104")
logger.info("request started")
```

Versão executável: [`examples/context_filter.py`](examples/context_filter.py).

## 55. Exemplo prático: preservar a atribuição do chamador

```python
import logging


class RecordCollector(logging.Handler):
    def __init__(self) -> None:
        super().__init__()
        self.records: list[logging.LogRecord] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.records.append(record)


logger = logging.getLogger("study.stacklevel")
logger.setLevel(logging.INFO)
logger.propagate = False
collector = RecordCollector()
logger.addHandler(collector)


def log_notice(message: str) -> None:
    logger.info(message, stacklevel=2)


def run_job() -> None:
    log_notice("job started")


run_job()
record = collector.records[0]
print(f"{record.levelname}:{record.funcName}:{record.getMessage()}")
```

Versão executável: [`examples/stacklevel_helper.py`](examples/stacklevel_helper.py).

## 56. Exemplo prático: mover a saída para trás de uma fila

```python
import logging
import queue
import sys
from logging.handlers import QueueHandler, QueueListener


log_queue = queue.Queue()
output_handler = logging.StreamHandler(sys.stdout)
output_handler.setFormatter(
    logging.Formatter("%(levelname)s:%(name)s:%(message)s")
)

logger = logging.getLogger("study.queue")
logger.setLevel(logging.INFO)
logger.propagate = False
logger.addHandler(QueueHandler(log_queue))

listener = QueueListener(
    log_queue,
    output_handler,
    respect_handler_level=True,
)
listener.start()
try:
    logger.info("queued event")
finally:
    listener.stop()
```

Versão executável: [`examples/queue_listener.py`](examples/queue_listener.py).

## 57. Erros comuns

### Definir apenas o nível de um logger ancestral e esperar que ele filtre registros propagados

Níveis dos loggers ancestrais não são reaplicados durante propagação. Configure o nível do handler relevante.

### Anexar o mesmo handler visível em vários níveis da hierarquia

Propagação pode gerar duplicatas.

### Chamar `basicConfig()` repetidamente e assumir que toda chamada reconfigura logging

Sem `force=True`, normalmente não faz nada depois que o root já possui handlers.

### Omitir `disable_existing_loggers` em `dictConfig()`

Loggers preexistentes que não são root podem ser desabilitados inesperadamente.

### Tratar configuração incremental como substituição completa de topologia

O modo incremental ignora definições de formatter e filter e altera apenas um subconjunto limitado de propriedades.

### Supor que `Formatter(style="{")` altera a interpolação da mensagem do logger

O estilo do formatter vale para o formato de saída, não para a mesclagem normal de argumentos da chamada de logger.

### Usar chaves de `extra` que colidem com `LogRecord`

Atributos nativos pertencem ao logging.

### Exigir campos personalizados em formatters para registros que talvez não os possuam

Use um contrato coerente de contexto ou `Formatter(defaults=...)` quando apropriado.

### Criar um logger por request ou entidade de runtime

Use nomes de logger estáveis e campos de contexto.

### Esconder o chamador real atrás de um helper

Use `stacklevel` quando a atribuição de origem deve apontar para o chamador do wrapper.

### Calcular diagnóstico caro para níveis desabilitados

Use `isEnabledFor()` ao preparar argumentos realmente caros.

### Enviar I/O lento diretamente a partir de código sensível a latência

Considere `QueueHandler` / `QueueListener`.

### Escrever o mesmo arquivo independentemente de vários processos

Os file handlers padrão não fornecem lock compartilhado entre processos.

### Tratar rotação como garantia de concorrência

Rollover gerencia arquivos; não coordena processos independentes.

### Confiar em configuração dinâmica enviada por origens não confiáveis

Configuração pode construir objetos e tem uma fronteira de segurança.

### Registrar segredos esperando que o formatter remova depois

Não coloque dados sensíveis desnecessários no registro desde o início.

## 58. Exercício: projete um contrato de logging para uma aplicação de workers

Projete uma pequena aplicação com estes namespaces de logger:

```text
worker
worker.fetch
worker.parse
```

Requisitos:

1. use `dictConfig()` com `version=1`;
2. defina `disable_existing_loggers=False` explicitamente;
3. configure um console handler em `INFO`;
4. configure um segundo handler que aceite `ERROR` ou superior;
5. permita que `worker.fetch` emita registros `DEBUG` sem transformar pacotes não relacionados globalmente em `DEBUG`;
6. anexe um campo estável `job_id` a todos os registros de um job;
7. preserve o chamador real ao usar um helper de logging;
8. garanta que um formatter não falhe quando um registro de terceiro não tiver `job_id`;
9. evite saída duplicada por propagação;
10. documente qual componente controla a configuração de logging;
11. explique como moveria I/O lento de destino para trás de uma fila;
12. explique o que muda se vários **processos** workers precisarem contribuir para um único arquivo;
13. liste pelo menos três campos que você intencionalmente se recusa a registrar por privacidade ou segurança.

Depois teste pelo menos estes cenários:

```text
DEBUG record from worker.fetch
INFO record from worker.parse
ERROR record reaching both intended destinations
third-party WARNING with no job_id
helper call preserving the caller function
exception record with one traceback only
```

O objetivo não é criar a maior configuração. O objetivo é tornar o contrato de roteamento e contexto explicável.

## 59. Referência rápida

| Necessidade | Ferramenta / política |
|---|---|
| Criar logger de módulo | `logging.getLogger(__name__)` |
| Inspecionar limite herdado | `logger.getEffectiveLevel()` |
| Verificar antes de diagnóstico caro | `logger.isEnabledFor(level)` |
| Definir limite de destino | `handler.setLevel(level)` |
| Parar entrega a ancestrais | `logger.propagate = False` |
| Verificar handlers na hierarquia | `logger.hasHandlers()` |
| Substituir configuração básica do root | `logging.basicConfig(..., force=True)` |
| Configurar grafo de objetos | `logging.config.dictConfig()` |
| Preservar loggers existentes de bibliotecas | `disable_existing_loggers=False` |
| Alterar apenas verbosidade em runtime incrementalmente | `incremental=True`, dentro da semântica limitada |
| Adicionar contexto a uma chamada | `extra={...}` |
| Reutilizar contexto de escopo | `logging.LoggerAdapter` |
| Mesclar contexto do adapter e da chamada no 3.13+ | `merge_extra=True` |
| Filtrar ou enriquecer um caminho | filter de logger/handler |
| Substituir registros em filter no 3.12+ | retornar novo `LogRecord` |
| Adicionar atributos globais do processo | `setLogRecordFactory()`, com cautela |
| Carregar contexto lógico de request/task | `contextvars` |
| Preservar chamador através de wrapper | `stacklevel=...` |
| Incluir traceback da exceção | `exc_info=True` / `logger.exception()` |
| Incluir stack atual | `stack_info=True` |
| Desabilitar níveis globalmente | `logging.disable(level)` |
| Fornecer fallback para campos personalizados | `Formatter(defaults=...)` |
| Mover entrega lenta para outra thread | `QueueHandler` + `QueueListener` |
| Iniciar/parar listener automaticamente no 3.14+ | `with QueueListener(...)` |
| Rotacionar por tamanho | `RotatingFileHandler` |
| Rotacionar por tempo | `TimedRotatingFileHandler` |
| Rotear warnings do Python para logging | `logging.captureWarnings(True)` |
| Controlar diagnóstico interno de handlers | `logging.raiseExceptions` |

## 60. Checklist de design

Antes de publicar uma configuração de logging, pergunte:

```text
Which code area owns each logger name?
Which component owns process-wide configuration?
What is each logger's effective level?
Which handler levels apply after logger eligibility?
Where does propagation stop?
Can one record reach the same destination twice?
Could dictConfig disable an existing logger accidentally?
Are custom fields present for every formatter that requires them?
Could custom field names collide with LogRecord attributes?
Should context be per call, per scope, per handler, or process-wide?
Does a helper preserve caller attribution?
Are exception tracebacks emitted exactly where they add value?
Is expensive diagnostic context guarded when the level is disabled?
Could a slow handler block latency-sensitive code?
What happens if a queue fills?
Are several processes writing one file independently?
Who owns rotation and retention?
What timezone do timestamps represent?
Could a logging failure affect application behavior?
Can untrusted input alter logging configuration?
Could any record contain secrets or unnecessary personal data?
Which logging behaviors are covered by tests?
```

Se essas perguntas tiverem respostas explícitas, o sistema de logging fica muito mais fácil de operar e manter.

## 61. Conexões com outros conceitos de Python

Este capítulo combina vários tópicos anteriores:

- **módulos e pacotes:** nomes de logger seguem naturalmente a hierarquia de módulos;
- **dicionários:** `dictConfig()` modela um grafo de configuração;
- **objetos e classes:** handlers, filters, formatters, adapters e records colaboram por interfaces;
- **exceções:** falhas de logging e falhas da aplicação têm políticas diferentes;
- **context managers:** Python 3.14 adiciona ciclo de vida via context manager ao `QueueListener`;
- **threads e filas:** entrega lenta pode ser desacoplada da criação de eventos;
- **processos:** um arquivo único exige estratégia deliberada de writer único;
- **variáveis de contexto:** contexto lógico de execução pode enriquecer registros sem nomes dinâmicos de logger;
- **testes:** registros podem ser verificados semanticamente em vez de comparar apenas strings renderizadas;
- **segurança:** tanto configuração quanto payloads de log atravessam fronteiras de confiança.

Por isso logging avançado é menos sobre imprimir mensagens e mais sobre projetar um grafo confiável de entrega de eventos.

## Referências

- [Referência Python de `logging`](https://docs.python.org/3/library/logging.html)
- [Referência Python de `logging.config`](https://docs.python.org/3/library/logging.config.html)
- [Referência Python de `logging.handlers`](https://docs.python.org/3/library/logging.handlers.html)
- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)

## Próximo capítulo

Continue para o [Capítulo 06: `collections`](../06-collections/README.pt-BR.md). Ele estuda contêineres especializados como `Counter`, `defaultdict`, `deque`, registros de tuplas nomeadas, mapeamentos em camadas, ferramentas de reordenação, bases wrapper e interfaces de coleção como escolhas explícitas de estrutura de dados, e não truques de conveniência.
