<div align="center">

# Projeto 03 · Cadastro de Usuários

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Projetos Práticos](../README.pt-BR.md)

Este é o terceiro projeto da **Fase 10: Projetos Práticos**. O foco está em validação de dados semelhantes a identidade, valores canônicos, prevenção de duplicidade, busca indexada, atualizações seguras, estados explícitos de conta e limites claros de serviço, sem introduzir autenticação real ou dados pessoais.

**Tempo estimado de estudo e implementação:** 180–240 minutos.

## Objetivos de aprendizagem

Ao concluir este projeto, você deverá conseguir:

- transformar regras de entrada em funções explícitas de validação;
- diferenciar dados de exibição de identificadores canônicos;
- normalizar Unicode e espaços de forma intencional;
- impedir duplicidades depois da normalização;
- manter múltiplos índices de busca sem expor dicionários internos;
- atualizar campos indexados sem deixar chaves antigas para trás;
- modelar o ciclo de vida de uma conta com enum e transições explícitas;
- separar snapshots imutáveis de usuário de um serviço de registro mutável;
- testar segurança de mutação, buscas, limites e transições inválidas.

## 1. Desafio do projeto

Construa um registro em memória capaz de:

1. cadastrar usuários fictícios;
2. atribuir IDs positivos sequenciais;
3. normalizar nome, username e identificador de e-mail;
4. impedir usernames e e-mails duplicados após canonicalização;
5. localizar usuários por ID, username ou e-mail;
6. pesquisar nos campos de identidade;
7. atualizar nome, username e e-mail com segurança;
8. manter os índices de username e e-mail sincronizados após mudanças;
9. suspender, reativar ou desativar usuários seguindo regras explícitas;
10. comprovar sucessos e falhas com testes automatizados.

## 2. Contrato de dados

Cada usuário contém:

```text
user_id   -> inteiro positivo gerado pelo registro
full_name -> texto normalizado e não vazio, com até 80 caracteres
username  -> identificador canônico de 3 a 30 caracteres
email     -> identificador canônico de e-mail segundo as regras do projeto
status    -> active, suspended ou deactivated
```

O projeto utiliza somente dados fictícios de demonstração.

## 3. Por que valores canônicos importam

Estas entradas devem representar o mesmo username:

```text
Maya.Chen
maya.chen
  MAYA.CHEN  
```

Se a unicidade for verificada antes da normalização, valores equivalentes podem entrar como contas diferentes.

`normalize_username(...)` transforma a entrada em uma representação canônica antes de buscas ou verificações de duplicidade.

## 4. Normalização Unicode

O projeto usa normalização Unicode **NFKC** antes de validar textos semelhantes a identidade.

Por exemplo:

```text
ＡＢＣ
```

vira:

```text
ABC
```

NFKC é uma decisão de aplicação neste projeto. Sistemas reais devem escolher sua política de normalização de acordo com seus próprios requisitos de identidade.

## 5. Normalização do nome

O nome preserva a capitalização de leitura, mas normaliza espaços:

```python
normalize_full_name("  Maya   Chen  ")
# "Maya Chen"
```

Valores vazios e nomes acima do limite do projeto são rejeitados.

O nome é dado de exibição e não é usado como chave única.

## 6. Contrato de username

Usernames são:

- normalizados com NFKC;
- limpos nas extremidades;
- convertidos com `casefold()`;
- limitados a 3–30 caracteres ASCII;
- obrigados a começar com letra ou dígito;
- permitidos apenas com letras, dígitos, `.`, `_` e `-`.

Exemplos:

```text
Maya.Chen -> maya.chen
NOAH-R    -> noah-r
```

Essas são regras deste projeto, não regras universais de username.

## 7. Contrato de e-mail

Este projeto implementa intencionalmente uma **política restrita de identificador de e-mail em nível de aplicação**, e não um parser completo de todos os padrões RFC de e-mail.

O registro:

- remove espaços nas extremidades;
- aplica NFKC e `casefold()`;
- exige exatamente um `@`;
- rejeita espaços dentro do endereço;
- valida um conjunto restrito de caracteres ASCII na parte local;
- rejeita pontos iniciais, finais ou repetidos na parte local;
- converte domínios Unicode usando o codec IDNA do Python;
- exige domínio separado por pontos com labels válidos;
- aplica limites de tamanho definidos pelo projeto.

Exemplo:

```python
normalize_email("MAYA@Example.COM")
# "maya@example.com"
```

Um domínio Unicode pode ser convertido para a forma ASCII IDNA:

```python
normalize_email("user@bücher.example")
# "user@xn--bcher-kva.example"
```

O projeto trata todo o e-mail canônico como case-insensitive para fins de unicidade. Sistemas reais podem precisar de requisitos diferentes.

## 8. Modelo imutável `User`

`User` é uma dataclass congelada:

```python
@dataclass(frozen=True, slots=True)
class User:
    user_id: int
    full_name: str
    username: str
    email: str
    status: UserStatus = UserStatus.ACTIVE
```

A validação também ocorre quando o construtor da dataclass é usado diretamente.

O registro não altera um objeto `User` existente. Mudanças criam um novo snapshot.

## 9. Limites do serviço de registro

`UserRegistry` concentra o comportamento mutável da coleção:

```text
cadastro
lookup
pesquisa
mudança de campos indexados
mudança de nome de exibição
transições de estado
```

`User` descreve um snapshot válido. O registro coordena relações entre vários usuários.

Isso evita esconder regras globais de unicidade dentro de um único registro que não conhece a coleção inteira.

## 10. IDs sequenciais sem lacunas por cadastros rejeitados

`register(...)` cria e valida um candidato antes de alterar o estado do registro.

Se username ou e-mail já estiverem ocupados, o cadastro falha e o próximo ID **não** é consumido.

```text
usuário válido -> ID 1
duplicidade rejeitada -> nenhum ID consumido
próximo usuário válido -> ID 2
```

Esse comportamento é uma convenção do projeto para deixar a ordem de mutação visível e testável.

## 11. Prevenção de duplicidade

O registro mantém índices canônicos:

```text
username -> user_id
email    -> user_id
```

Portanto estes usernames colidem:

```text
maya.chen
MAYA.CHEN
```

E estes e-mails também colidem segundo a política do projeto:

```text
maya@example.com
MAYA@EXAMPLE.COM
```

Uma duplicidade gera `DuplicateUserError` antes de qualquer alteração do estado.

## 12. Busca indexada

O registro oferece:

```python
registry.get_by_id(1)
registry.get_by_username("MAYA.CHEN")
registry.get_by_email("maya@EXAMPLE.COM")
```

As entradas de lookup passam pelas mesmas funções de canonicalização usadas no cadastro.

Valores ausentes geram `UserNotFoundError` em vez de expor um `KeyError` bruto de dicionário.

## 13. Pesquisa

`search(...)` faz busca case-insensitive por substring em:

- nome completo;
- username canônico;
- e-mail canônico.

Os resultados preservam a ordem de cadastro.

Um filtro opcional de `UserStatus` pode restringir o resultado:

```python
registry.search("example", status=UserStatus.ACTIVE)
```

É uma implementação simples em memória para aprendizado, não um mecanismo de busca completo.

## 14. Atualizando campos indexados com segurança

Alterar username ou e-mail envolve duas responsabilidades:

1. validar e verificar se o novo valor está disponível;
2. substituir a chave antiga do índice pela nova.

O projeto valida primeiro e só depois altera os índices.

Uma atualização rejeitada por duplicidade mantém a chave antiga funcionando.

## 15. Ciclo de vida da conta

Estados suportados:

```text
active
suspended
deactivated
```

Transições permitidas:

```text
active    -> suspended
suspended -> active
active    -> deactivated
suspended -> deactivated
```

`deactivated` é terminal nesta versão.

Transições inválidas geram `InvalidUserTransitionError`.

## 16. Por que usar enum

`UserStatus` é um enum, não texto arbitrário.

Isso impede estados como:

```text
"actve"
"paused-ish"
"disabled maybe"
```

de entrarem silenciosamente no modelo.

Enums são úteis quando um campo possui um conjunto pequeno e explícito de valores válidos.

## 17. Estrutura do projeto

```text
03-user-registration/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── user_registration.py
├── demo.py
└── tests/
    ├── conftest.py
    └── test_user_registration.py
```

## 18. Executar a demo determinística

A partir da raiz do repositório:

```bash
python practical-projects/03-user-registration/demo.py
```

Saída esperada:

```text
users: 3
active: 2
suspended: 1
lookup: maya.chen
search-example: 3
```

## 19. Executar os testes

```bash
python -m pytest -q practical-projects/03-user-registration/tests
```

A suíte inicial contém **46 cenários pytest** cobrindo normalização, regras restritas de e-mail, duplicidade, IDs gerados, registros inicializados, lookup, pesquisa, atualizações seguras, snapshots imutáveis e transições de ciclo de vida.

## 20. Caminhos de falha para testar manualmente

Experimente:

```python
registry.register("Maya Chen", "ab", "maya@example.com")
registry.register("Maya Chen", "maya", "not-an-email")
registry.register("Other User", "MAYA", "other@example.com")
registry.get_by_id(999)
registry.reactivate(1)
```

Leia as exceções e confira o estado do registro após cada operação rejeitada.

## 21. Nota de design: validação e unicidade são problemas diferentes

Um username pode ser sintaticamente válido e ainda estar indisponível porque outro usuário já possui o mesmo valor canônico.

Validação responde:

> Este valor tem uma estrutura aceitável?

Unicidade responde:

> Este valor aceitável está disponível nesta coleção?

Separar essas perguntas deixa o código mais claro e testável.

## 22. Nota de design: índices são estado derivado

Os dicionários de username e e-mail são índices secundários derivados dos valores canônicos de `User`.

Quando um campo indexado muda, o mapa principal de usuários e o índice correspondente precisam continuar consistentes.

Esse é um pequeno exemplo de invariante: diferentes partes do estado precisam concordar o tempo todo.

## 23. Nota de design: validar antes de mutar

Cadastro e atualização de identidade seguem a mesma sequência:

```text
normalizar -> validar -> verificar conflitos -> criar substituição -> mutar
```

Essa ordem reduz bugs de atualização parcial.

## 24. O que o projeto não inclui

Esta versão não inclui:

- senhas;
- hash de senhas;
- sessões de login;
- autenticação;
- autorização ou roles;
- dados pessoais reais;
- envio de e-mail ou links de verificação;
- persistência ou banco de dados;
- provedores externos de identidade;
- API web;
- GUI.

Esses assuntos introduzem outras preocupações de segurança e infraestrutura. O projeto permanece focado em regras de domínio em memória.

## 25. Nota de segurança

Um sistema real de cadastro não deve armazenar senhas em texto puro e exigiria muito mais trabalho de segurança do que este registro educacional oferece.

Não trate este projeto como uma implementação de autenticação pronta para produção.

## 26. Desafio de extensão: eventos de auditoria

Registre eventos fictícios como:

```text
user_registered
username_changed
user_suspended
user_reactivated
user_deactivated
```

Mantenha o registro de eventos separado do snapshot principal de usuário.

## 27. Desafio de extensão: política configurável de username

Extraia as regras de username para um objeto de política configurável com:

- intervalo de tamanho;
- separadores permitidos;
- permissão ou não de dígito como primeiro caractere.

Mantenha a lógica de unicidade independente da política de sintaxe.

## 28. Desafio de extensão: adaptador de persistência

Adicione uma interface de repositório e um adaptador JSON ou SQLite sem mover as regras de validação para a camada de persistência.

O registro em memória deve continuar testável sem I/O.

## 29. Discussão de portfólio

Ao apresentar este projeto, explique as decisões de engenharia, e não apenas “ele cadastra usuários”:

- identificadores canônicos antes da verificação de unicidade;
- política explícita e restrita de e-mail;
- normalização Unicode e IDNA;
- snapshots imutáveis;
- responsabilidades separadas entre modelo e serviço;
- índices secundários para lookup;
- atualização atômica de campos indexados;
- máquina de estados explícita;
- exceções de domínio;
- testes focados em mutação.

## 30. Checklist de revisão

Antes de considerar sua implementação concluída, confira:

- Usernames equivalentes conseguem burlar duplicidade por mudança de caixa ou espaços?
- Lookup e duplicidade de e-mail usam o mesmo contrato de canonicalização?
- Um cadastro rejeitado preserva a sequência de IDs?
- Mudanças de username e e-mail removem índices antigos?
- Uma atualização rejeitada mantém o índice válido anterior?
- Estados são limitados a valores explícitos do enum?
- Transições inválidas são rejeitadas?
- Os dicionários internos ficam escondidos dos chamadores?
- Senhas e dados pessoais reais estão propositalmente ausentes?
- Os testes provam caminhos de sucesso e falha?

## 31. Próximo projeto

O Projeto 03 adiciona identidade canônica, prevenção de duplicidade, índices secundários, atualizações seguras e transições de ciclo de vida à progressão da Fase 10.

O próximo projeto planejado é **CSV Analyzer**, que mudará o foco para entrada tabular, expectativas de schema, validação por linha, agregações, dados malformados e análise determinística.
