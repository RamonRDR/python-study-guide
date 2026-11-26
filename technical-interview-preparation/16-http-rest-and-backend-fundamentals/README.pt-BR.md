# HTTP, REST e fundamentos de backend

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../15-exceptions-testing-and-debugging-review/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../17-api-contracts-authentication-and-authorization/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [external-libraries/03-requests](../../external-libraries/03-requests/README.pt-BR.md)
- [technical-interview-preparation/15-exceptions-testing-and-debugging-review](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)

## Contratos cliente, servidor e recurso

HTTP é protocolo requisição/resposta: método, alvo, headers e conteúdo opcional descrevem requisição; status, headers e conteúdo opcional descrevem resposta. Backend geralmente roteia, valida, autoriza, aplica regras, persiste dados e retorna representação. Endpoint é operação exposta em interface. REST é estilo arquitetural com restrições incluindo separação cliente/servidor, requisições stateless, cacheabilidade e interface uniforme; só JSON sobre HTTP não estabelece REST. Requisições stateless carregam informação necessária ao tratamento; servidor ainda pode armazenar dados de recursos.

| Método | Semântica pretendida | Seguro / idempotente |
| --- | --- | --- |
| GET | Recuperar representação | Sim / sim |
| POST | Processamento específico, frequentemente criação | Não / não garantido |
| PUT | Criar ou substituir estado do alvo | Não / sim |
| PATCH | Aplicar alteração parcial | Não / não garantido |
| DELETE | Remover associação do alvo | Não / sim |

Seguro significa cliente não solicitar mudança de estado; idempotente refere-se ao efeito pretendido no servidor, não respostas idênticas ou ausência de logs. Retry pode duplicar efeito de POST. Para escritas, exija contrato explícito de retry (como chave de idempotência persistida), tentativas limitadas e respeito a Retry-After. Defina timeouts nas fronteiras de rede.

## Design de resposta

200 sucesso; 201 criado (frequentemente Location); 204 sucesso sem conteúdo; 400 requisição malformada ou inválida; 404 recurso ausente; 405 método não suportado no alvo (inclua Allow); 409 conflito com estado atual; 429 limite de taxa; 500 falha inesperada do servidor. 401 e 403 na próxima aula. Resposta de erro deve descrever contrato estável sem segredos internos. Paginação limita tamanho; defina ordenação estável, semântica de página/cursor e fim de resultados.

Exemplo compartilhado é simulação pura de roteamento para endpoint didático somente GET. Retorna status, headers e objetos Python que representam conteúdo JSON, não bytes HTTP reais. Framework real precisa cuidar de serialização, detalhes de protocolo, HEAD/OPTIONS conforme suporte e segurança. Teste caminho ausente, método não suportado e dados de resposta independentes.

## Prática

Esboce recurso /lessons/42, escolha método de leitura e substituição e declare status esperados. Explique por que repetir DELETE pode retornar status diferente mantendo idempotência no efeito pretendido. Teste roteamento sem rede.

**Referência rápida:** método expressa intenção; status expressa resultado; retries dependem de semântica; contrato antes de framework.

## Exemplo executável compartilhado

[route_catalog.py](examples/route_catalog.py)

`python technical-interview-preparation/16-http-rest-and-backend-fundamentals/examples/route_catalog.py`

## Referências oficiais

- [www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../15-exceptions-testing-and-debugging-review/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../17-api-contracts-authentication-and-authorization/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
