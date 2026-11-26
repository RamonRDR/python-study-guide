# Contratos de API, autenticação e autorização

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../16-http-rest-and-backend-fundamentals/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../18-relational-databases-and-sql/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [external-libraries/03-requests](../../external-libraries/03-requests/README.pt-BR.md)
- [standard-library/03-json](../../standard-library/03-json/README.pt-BR.md)
- [technical-interview-preparation/16-http-rest-and-backend-fundamentals](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.pt-BR.md)

## Validar a fronteira

Contrato de API descreve requisições, campos obrigatórios e opcionais, tipos, limites, respostas, erros e compatibilidade. Parsing JSON não é validação. Rejeite entradas grandes antes de parsing quando possível; valide formato e campos permitidos, tipos (booleanos não são inteiros de negócio por padrão), comprimentos e intervalos. Campos desconhecidos podem ser rejeitados ou ignorados conforme contrato documentado, não persistidos silenciosamente. Retorne erros consistentes sem vazar stack traces. Adicione campos de modo compatível quando clientes permitirem; versione ou migre mudanças incompatíveis.

Exemplo valida objeto já decodificado com exatamente um campo title, remove espaços externos e aceita 1–80 caracteres após trim. Não trata HTTP bruto, nomes JSON duplicados ou tamanho do corpo; são responsabilidade da fronteira de parsing/transporte.

## Autenticação versus autorização

Autenticação estabelece identidade verificada; autorização decide o que ela pode fazer em recurso específico. Use bibliotecas/provedores estabelecidos, HTTPS, verificação de assinatura do token e checagens de emissor/audiência/expiração quando aplicáveis. Nunca trate proprietário informado pelo cliente ou token decodificado sem verificação como identidade. Armazene credenciais com segurança, não as registre e aplique privilégio mínimo. Bearer token é credencial; posse só é significativa após verificação. Exemplo intencionalmente não emite nem valida tokens.

Autorização em nível de objeto é necessária em cada acesso protegido: login válido não basta para ler nota de outro proprietário. Exemplo recebe identidade confiável de camada anterior hipotética; None resulta 401 com desafio Bearer, ID inexistente 404 e proprietário diferente 403 sem conteúdo. 401 significa ausência de credenciais válidas de autenticação; 403 significa recusa de acesso. Alguns sistemas retornam 404 para recursos proibidos para não revelar existência; escolha e documente política consistente. Este exemplo deliberadamente revela existência a autenticados via 403 versus 404 e não é fronteira de segurança de produção.

## Prática

Teste anônimo, proprietário autorizado, outro proprietário, recurso ausente e payloads inválidos. Explique por que checar apenas papel pode não impor propriedade do objeto. Esboce onde autenticação, busca, autorização e serialização ocorreriam em serviço real. Adicione teste negativo antes de alterar política.

**Referência rápida:** parse e valide; identidade verificada primeiro; autorize ação e objeto; não confie em alegações do cliente.

## Exemplo executável compartilhado

[note_access.py](examples/note_access.py)

`python technical-interview-preparation/17-api-contracts-authentication-and-authorization/examples/note_access.py`

## Referências oficiais

- [www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html)
- [api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)
- [devguide.owasp.org/en/07-training-education/07-api-top-ten/](https://devguide.owasp.org/en/07-training-education/07-api-top-ten/)

<!-- chapter-navigation:bottom -->
[← Anterior](../16-http-rest-and-backend-fundamentals/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../18-relational-databases-and-sql/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
