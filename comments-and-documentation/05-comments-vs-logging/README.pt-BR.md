<div align="center">

# Comentários versus Logging em Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Marcadores de tarefas](../04-task-markers/README.pt-BR.md)

Comentários e logs comunicam informações, mas falam sobre momentos diferentes. Um comentário explica o código-fonte para quem o lê. Um log registra um evento ocorrido enquanto o programa estava em execução.

> **Princípio orientador:** Coloque o raciocínio estável ao lado do código. Coloque fatos variáveis da execução nos registros de log.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Intermediário |
| Pré-requisitos | Recomenda-se o capítulo de comentários; familiaridade básica com funções, exceções e módulos ajuda |
| Tempo estimado de estudo | 55 a 75 minutos |
| Conceitos principais | comentários, `print()`, `logging`, níveis, loggers por módulo, configuração da aplicação, handlers, formatters, propagação, exceções, privacidade |

## Objetivos de aprendizagem

Ao concluir este capítulo, você deverá ser capaz de:

- diferenciar explicação no código-fonte de observação durante a execução;
- escolher entre comentário, saída para o usuário, registro de log e exceção;
- usar `logging.getLogger(__name__)` nos módulos;
- selecionar um nível padrão apropriado;
- configurar logging no ponto de entrada da aplicação;
- impedir que bibliotecas reutilizáveis controlem a configuração global;
- escrever mensagens parametrizadas com contexto útil e não sensível;
- registrar exceções sem esconder ou duplicar o tratamento de erros;
- reconhecer registros duplicados, ruído excessivo e riscos de privacidade;
- revisar uma alteração de logging considerando clareza e valor operacional.

## 1. Comentários e logs respondem a perguntas diferentes

Um comentário útil responde a perguntas como:

- Por que esta regra existe?
- Qual restrição externa moldou esta implementação?
- Por que a alternativa aparentemente óbvia é insegura?
- Qual premissa estável poderia passar despercebida?

```python
# The partner API returns monetary values in cents.
amount_cents = payload["amount"]
```

Um log útil responde a perguntas como:

- O que aconteceu nesta execução?
- Qual operação iniciou, terminou, tentou novamente ou falhou?
- Qual identificador seguro ajuda a correlacionar o evento?
- Qual severidade deve ser atribuída?

```python
logger.info("Processed invoice invoice_id=%s", invoice_id)
```

Comentários permanecem no código-fonte. Logs são emitidos durante a execução e podem ser filtrados, formatados, armazenados, pesquisados ou encaminhados.

## 2. Uma tabela de decisão compacta

| Necessidade | Prefira |
|---|---|
| Explicar uma decisão estável de design | Comentário |
| Documentar módulo, função, classe ou método público | Docstring |
| Mostrar resultado ou instrução diretamente ao usuário | `print()` ou a camada de interface da aplicação |
| Registrar evento de execução para diagnóstico ou operação | Logging |
| Sinalizar que a operação atual não pode continuar normalmente | Exceção |
| Medir taxas, latência, contagens ou saúde do serviço | Métricas |
| Preservar histórico empresarial controlado ou resistente a adulteração | Trilha de auditoria específica |

Nenhum mecanismo substitui todos os demais.

## 3. `print()` não é um logger defeituoso

`print()` é adequado quando o texto faz parte da saída destinada ao usuário:

```python
print("Report saved successfully.")
```

Uma ferramenta de linha de comando pode imprimir tabela, resposta ou instrução. Uma aplicação gráfica pode exibir o equivalente em componentes visuais. Logging normalmente se destina a desenvolvedores, operação, suporte ou sistemas de diagnóstico.

Não substitua todo `print()` por logging. Primeiro decida quem precisa da mensagem e se ela faz parte da interface do programa.

## 4. Crie um logger no nível do módulo

O padrão recomendado é:

```python
import logging


logger = logging.getLogger(__name__)


def process_order(order_id: str) -> None:
    logger.info("Processing order order_id=%s", order_id)
```

Usar `__name__` cria nomes que acompanham a hierarquia de pacotes e módulos. Assim a aplicação pode habilitar, suprimir ou encaminhar registros de partes específicas.

Não instancie `logging.Logger` diretamente no uso comum. Chamadas repetidas a `logging.getLogger()` com o mesmo nome retornam o mesmo logger.

## 5. A aplicação controla a configuração

A maioria dos módulos deve emitir registros. O ponto de entrada da aplicação decide:

- nível mínimo;
- destinos como console, arquivo ou handler remoto;
- formato;
- inclusão de horário, processo ou identificador de correlação;
- políticas diferentes para desenvolvimento, testes e produção.

```python
import logging


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s:%(name)s:%(message)s",
    )
```

`basicConfig()` é conveniente para aplicações pequenas e exemplos. Aplicações maiores podem usar `dictConfig()`, opções de linha de comando, configurações por ambiente ou recursos do framework.

## 6. Bibliotecas reutilizáveis não devem tomar a configuração global

Uma biblioteca não sabe como a aplicação deseja encaminhar ou formatar logs. Isto é invasivo:

```python
# Inside a reusable library module:
logging.basicConfig(level=logging.DEBUG)
```

Uma biblioteca reutilizável normalmente deve:

1. criar logger com `logging.getLogger(__name__)`;
2. emitir registros em níveis significativos;
3. evitar configurar o logger raiz ou adicionar handlers visíveis;
4. opcionalmente adicionar `logging.NullHandler()` ao logger principal.

```python
import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
```

`NullHandler` impede que a biblioteca presuma um destino. Os registros ainda podem propagar para handlers configurados pela aplicação.

## 7. Níveis padrão de logging

Python oferece cinco níveis comuns:

| Nível | Significado típico |
|---|---|
| `DEBUG` | informação diagnóstica detalhada para investigação |
| `INFO` | marcos esperados e operações normais relevantes |
| `WARNING` | situação inesperada ou degradada, mas o trabalho pode continuar |
| `ERROR` | uma operação falhou ou produziu resultado inutilizável |
| `CRITICAL` | a aplicação ou subsistema importante talvez não consiga continuar |

```python
logger.debug("Validated %s columns", column_count)
logger.info("Imported %s records", record_count)
logger.warning("Retrying after timeout attempt=%s", attempt)
logger.error("Could not save report report_id=%s", report_id)
logger.critical("Database is unavailable; stopping worker")
```

Esses significados são políticas, não leis matemáticas. O projeto deve definir exemplos do próprio domínio para classificar eventos semelhantes com consistência.

## 8. `DEBUG` deve revelar detalhes sem virar despejo de dados

Registros úteis de debug podem mostrar:

- estratégia ou caminho selecionado;
- contagens e dimensões seguras;
- acertos ou falhas de cache;
- tentativas;
- identificadores sanitizados de requisição ou tarefa.

Evite registrar payloads completos por padrão. Objetos grandes criam ruído, aumentam custos, dificultam diagnóstico e podem expor informações sensíveis.

Um registro de debug ainda deve ser escrito para uma pessoa, não usado como substituto da compreensão do código.

## 9. `INFO` registra eventos normais relevantes

Bons eventos de `INFO` frequentemente descrevem fronteiras:

- tarefa iniciada ou concluída;
- relatório gerado;
- migração processou um lote;
- versão de configuração foi ativada;
- integração externa concluiu com sucesso.

Não registre cada iteração de loop em `INFO` apenas porque logging existe. Um evento normal de alto volume pode pertencer a `DEBUG`, a uma métrica ou a lugar nenhum.

## 10. `WARNING`, `ERROR` e `CRITICAL` exigem julgamento

Use `WARNING` quando o programa pode continuar, mas o evento merece atenção, como fallback, nova tentativa, entrada obsoleta ou capacidade reduzida.

Use `ERROR` quando uma operação específica falhou. O processo ainda pode continuar com outros trabalhos.

Reserve `CRITICAL` para condições que ameaçam a aplicação ou um subsistema importante. Se toda falha de validação for crítica, o nível deixa de comunicar severidade.

O nível deve refletir a consequência, não a frustração de quem desenvolveu.

## 11. Registre exceções durante o tratamento

`logger.exception()` cria um registro `ERROR` e inclui o traceback da exceção atual. Use dentro de um tratador:

```python
try:
    save_report(report)
except OSError:
    logger.exception("Could not save report report_id=%s", report.id)
    raise
```

Registrar a exceção não decide se o programa deve recuperar, traduzir, tentar novamente ou relançar. Tratamento de erro e observabilidade são responsabilidades relacionadas, mas diferentes.

Evite registrar a mesma exceção em todas as camadas. Quando uma camada inferior registra e relança e todos os chamadores registram novamente, uma falha vira uma parede de tracebacks repetidos.

## 12. Prefira mensagens parametrizadas

Escreva:

```python
logger.info("Processed %s records", record_count)
```

Em vez de formatar antecipadamente:

```python
logger.info(f"Processed {record_count} records")
```

A chamada guarda o template e os argumentos separadamente e realiza a interpolação quando o registro é formatado. Mensagens parametrizadas também mantêm um formato estável para pessoas e algumas ferramentas.

Não aplique `%` manualmente antes de chamar o logger:

```python
logger.info("Processed %s records" % record_count)
```

Isso formata antecipadamente e perde o benefício.

## 13. Inclua contexto que permita agir

O registro deve ser compreensível sem uma caça ao tesouro:

```python
logger.info(
    "Payment authorized order_id=%s provider=%s",
    order_id,
    provider_name,
)
```

Contexto útil pode incluir:

- identificadores internos estáveis;
- nomes de operações ou tarefas;
- contagens e unidades seguras;
- nomes de provedores ou componentes;
- número da tentativa;
- duração quando medida corretamente.

Prefira campos explícitos como `order_id=` ou `attempt=`. Um número isolado possui significado fraco.

## 14. Nunca registre segredos ou dados pessoais desnecessários

Isto é inseguro:

```python
logger.debug("Authenticated with token=%s", access_token)
```

Não registre:

- senhas, tokens, chaves de API ou cookies de sessão;
- dados completos de pagamento;
- conteúdo privado de clientes;
- identificadores pessoais sem necessidade documentada;
- cabeçalhos brutos de autenticação;
- segredos escondidos em objetos completos de requisição ou configuração.

Redação ajuda, mas não justifica coletar dados que o log nunca precisou. A política deve seguir os requisitos de privacidade, segurança e retenção.

## 15. Handlers, formatters e filters

Um registro percorre um pequeno pipeline:

```text
logging call → logger → filters → handler → formatter → destination
```

- **Logger:** cria e encaminha o registro.
- **Handler:** envia registros aceitos para um destino.
- **Formatter:** converte o registro em texto ou outra representação.
- **Filter:** aplica regras adicionais ou adiciona contexto controlado.

Aplicações pequenas podem precisar apenas de `basicConfig()`. Compreender as peças ajuda quando é necessário console em `INFO`, arquivo em `DEBUG` ou políticas diferentes por pacote.

## 16. Propagação e registros duplicados

Os nomes formam uma hierarquia. Normalmente, registros propagam de um logger filho para handlers ancestrais.

Duplicações aparecem quando o mesmo handler é anexado ao logger do módulo e ao logger raiz:

```python
logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)

root_logger = logging.getLogger()
root_logger.addHandler(stream_handler)
```

Prefira configurar handlers em um nível suficientemente alto e permitir a propagação natural.

Isto interrompe a propagação:

```python
logger.propagate = False
```

Use deliberadamente. Desativar sem anexar um handler apropriado pode fazer os registros desaparecerem.

## 17. Contexto estruturado e adapters

Texto com campos `chave=valor` estáveis costuma bastar em projetos pequenos. Aplicações também podem adicionar contexto com `extra`:

```python
logger.info(
    "Started request",
    extra={"request_id": request_id},
)
```

Um `LoggerAdapter` pode incluir contexto repetido:

```python
request_logger = logging.LoggerAdapter(
    logger,
    {"request_id": request_id},
)
request_logger.info("Started request")
```

Escolha nomes que não colidam com atributos nativos de `LogRecord`. Bibliotecas de logging estruturado e integrações de plataforma podem oferecer esquemas mais ricos, mas os princípios de privacidade e severidade permanecem.

## 18. Logging não é métrica, tracing ou auditoria

Logging registra eventos discretos. Outros instrumentos respondem a perguntas diferentes:

- **Métricas:** Com que frequência? Quanto? Quão rápido?
- **Tracing:** Como uma requisição percorreu os componentes?
- **Trilha de auditoria:** Quem alterou um objeto controlado, quando e sob qual política?
- **Relato de exceções:** Quais falhas precisam ser agrupadas, alertadas e analisadas?

Um projeto pode derivar métricas de logs, mas depender apenas de mensagens em prosa é frágil. Auditorias de segurança ou finanças normalmente precisam de garantias mais fortes que logs comuns.

## 19. Testando comportamento de logging

Testes devem focar contratos relevantes, não pontuação incidental.

Afirmações úteis incluem:

- warning emitido para fallback documentado;
- segredo nunca aparece;
- biblioteca não configura o logger raiz;
- registro de erro contém identificador seguro necessário;
- evento ruidoso de debug é filtrado em produção.

`unittest` oferece `assertLogs()`. Projetos com pytest frequentemente usam `caplog`. Evite congelar cada palavra de uma mensagem interna, exceto quando a redação fizer parte da interface suportada.

## 20. Exemplos deste repositório

| Arquivo | Objetivo |
|---|---|
| [`comments_vs_logging.py`](examples/comments_vs_logging.py) | Coloca raciocínio estável em comentário e valores de execução em log |
| [`logging_levels.py`](examples/logging_levels.py) | Emite exemplos determinísticos dos cinco níveis padrão |
| [`application_and_library_logging.py`](examples/application_and_library_logging.py) | Mostra configuração da aplicação e uso no estilo de biblioteca |

Execute um exemplo a partir da raiz:

```bash
python comments-and-documentation/05-comments-vs-logging/examples/comments_vs_logging.py
```

Em sistemas que usam `python3`:

```bash
python3 comments-and-documentation/05-comments-vs-logging/examples/comments_vs_logging.py
```

## 21. Exemplo prático de refatoração

Antes:

```python
def import_file(file_path):
    # The import started.
    print("Importing...")
    try:
        return parse_file(file_path)
    except OSError:
        print("Import failed")
        return None
```

Depois:

```python
import logging


logger = logging.getLogger(__name__)


def import_file(file_path):
    logger.info("Starting import file_name=%s", file_path.name)
    try:
        return parse_file(file_path)
    except OSError:
        logger.exception("Import failed file_name=%s", file_path.name)
        raise
```

A refatoração remove comentário que descrevia evento de execução, substitui prints diagnósticos por registros, preserva a exceção e inclui nome de arquivo seguro. A política de recuperação correta ainda depende da aplicação.

## 22. Erros comuns

### Comentar estado de execução

Um comentário no código não informa se a execução de hoje iniciou, tentou novamente ou falhou.

### Registrar raciocínio estável apenas no log

Um log desaparece quando o código não executa e não deve ser o único lugar que explica uma regra de negócio.

### Chamar `basicConfig()` em todos os módulos

A configuração fica imprevisível, bibliotecas se tornam invasivas e testes ficam mais difíceis.

### Registrar e engolir uma exceção

Um traceback no log não transforma uma operação falha em sucesso.

### Registrar a mesma exceção repetidamente

Uma falha vira vários registros ruidosos sem valor adicional.

### Usar `ERROR` para feedback comum de validação

A severidade deve corresponder à consequência operacional.

### Formatar mensagens antecipadamente

F-strings são convenientes, mas argumentos parametrizados preservam formatação adiada e template estável.

### Incluir segredos para “debug temporário”

O histórico do Git pode esquecer a alteração, mas o armazenamento de logs pode preservar o segredo.

### Adicionar handlers em vários níveis

A propagação pode produzir duplicações.

### Tratar logs como interface de usuário

Registros operacionais não substituem mensagens claras para o usuário.

## 23. Exercício

Classifique e reescreva cada linha. Decida se pertence a comentário, saída para usuário, log, exceção ou deve ser removida:

```python
# The job started at runtime.
# TODO: print every processed customer.
print(f"Could not import {file_name}")
logger.info("The tax rate is fixed by regulation.")
logger.error("Customer password=%s", password)
```

Para cada decisão, explique:

1. Quem precisa da informação?
2. É raciocínio estável ou fato da execução?
3. Qual nível é apropriado?
4. Qual contexto seguro torna o evento acionável?
5. A mensagem pode expor dados sensíveis?
6. A operação deve continuar, recuperar ou lançar uma exceção?

Depois, configure um script pequeno com logger de módulo e verifique como a mudança do nível configurado altera os registros exibidos.

## 24. Checklist de revisão

Antes de aceitar uma alteração de logging, verifique:

- [ ] comentários explicam decisões estáveis, não eventos de execução;
- [ ] saída para usuário permanece separada do diagnóstico;
- [ ] módulos usam `logging.getLogger(__name__)`;
- [ ] a aplicação controla handlers, formatters e níveis globais;
- [ ] bibliotecas reutilizáveis não chamam `basicConfig()`;
- [ ] níveis correspondem à consequência;
- [ ] mensagens usam argumentos parametrizados;
- [ ] registros incluem contexto seguro suficiente;
- [ ] segredos e dados pessoais desnecessários foram excluídos;
- [ ] exceções são registradas apenas onde o traceback agrega valor;
- [ ] propagação não duplica registros;
- [ ] eventos de alto volume não sufocam os logs normais;
- [ ] logs não substituem métricas, auditoria ou tratamento de erros.

## 25. Resumo para consulta rápida

| Situação | Abordagem recomendada |
|---|---|
| Motivo estável ao lado da implementação | Comentário |
| Contrato público de módulo ou callable | Docstring |
| Saída destinada a quem usa o programa | `print()` ou camada de interface |
| Evento diagnóstico detalhado | `DEBUG` |
| Marco normal relevante | `INFO` |
| Condição recuperável ou degradada | `WARNING` |
| Operação falhou | `ERROR` |
| Subsistema importante talvez não continue | `CRITICAL` |
| Traceback atual dentro de `except` | `logger.exception()` |
| Logger em módulo reutilizável | `logging.getLogger(__name__)` |
| Destinos e formato da aplicação | Configurar no ponto de entrada |
| Contexto repetido | Campos parametrizados, `extra` ou `LoggerAdapter` |
| Senhas, tokens e payloads privados | Nunca registrar |

Comentários preservam raciocínio no código-fonte. Logging preserva evidências selecionadas da execução. Software de qualidade precisa dos dois, com uma fronteira clara.

## Referências oficiais

- [Python Logging HOWTO](https://docs.python.org/pt-br/3/howto/logging.html)
- [Referência do módulo `logging`](https://docs.python.org/pt-br/3/library/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
