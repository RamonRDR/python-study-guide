# Concorrência, paralelismo e GIL

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../13-context-managers/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [technical-interview-preparation/10-python-memory-management](../../technical-interview-preparation/10-python-memory-management/README.pt-BR.md)
- [technical-interview-preparation/13-context-managers](../../technical-interview-preparation/13-context-managers/README.pt-BR.md)

## Concorrência e paralelismo

Concorrência significa que várias tarefas podem progredir em períodos sobrepostos; paralelismo significa executar trabalho simultaneamente. Trabalho I/O-bound espera principalmente entrada/saída; CPU-bound gasta tempo computando. Threads compartilham memória do processo; processos normalmente têm espaços de endereçamento separados e exigem comunicação ou serialização. Asyncio usa escalonamento cooperativo de corrotinas: `async def` cria função corrotina, chamá-la produz objeto corrotina, e `await` pode suspendê-la para outra tarefa escalonada executar. Trabalho síncrono bloqueante pode travar event loop.

## GIL em Python 3.13

Em builds convencionais CPython, global interpreter lock (GIL) permite somente uma thread de cada vez executar bytecode Python no mesmo interpretador. I/O e algumas extensões nativas o liberam, então threads podem sobrepor espera e trabalho nativo. Não torna operações compostas da aplicação atômicas nem garante ausência de races. CPython 3.13 também oferece build experimental free-threaded; código compatível pode executar threads Python em paralelo, e algumas extensões podem reativar GIL. Depende de implementação/build, não é garantia da linguagem Python.

| Abordagem | Bom ponto de partida | Trade-off |
| --- | --- | --- |
| Threads | I/O bloqueante com colaboradores thread-safe | Sincronização de estado compartilhado |
| Processos | Computação pesada em Python puro | Inicialização, memória, serialização |
| Asyncio | Muitas operações I/O cooperativas | APIs async e cancelamento |

Meça cargas antes de escolher; trabalho sequencial pequeno pode ganhar overhead sem benefício.

## Exemplo de estado compartilhado

Race condition ocorre quando comportamento depende de intercalação não sincronizada. Exemplo compartilhado usa `Lock` com gerenciador de contexto ao redor do incremento leitura-modificação-escrita. Aguarda todos futures e propaga exceções dos workers com result. Ordem das threads não é verificada. Locks protegem invariante escolhido, não acessos externos arbitrários; evite manter locks durante I/O lento e adquira vários locks em ordem consistente para reduzir risco de deadlock.

## Prática

Execute quatro workers com 250 atualizações cada; total esperado 1000. Teste zero atualizações e contagens inválidas. Explique por que observar resultado correto sem lock não prova segurança e por que contador protegido demonstra correção, não benchmark de velocidade. Use Python 3.13 local; suporte a threads e processos no navegador não é presumido nem verificado.

**Referência rápida:** concorrência sobrepõe; paralelismo simultâneo; GIL depende do build; sincronize invariantes compartilhados; escolha pela carga.

## Exemplo executável compartilhado

[safe_counter.py](examples/safe_counter.py)

`python technical-interview-preparation/14-concurrency-parallelism-and-the-gil/examples/safe_counter.py`

## Referências oficiais (Python 3.13)

- [Python 3.13: library/threading.html](https://docs.python.org/3.13/library/threading.html)
- [Python 3.13: howto/free-threading-python.html](https://docs.python.org/3.13/howto/free-threading-python.html)
- [Python 3.13: library/concurrent.futures.html](https://docs.python.org/3.13/library/concurrent.futures.html)
- [Python 3.13: library/asyncio-task.html](https://docs.python.org/3.13/library/asyncio-task.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../13-context-managers/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
