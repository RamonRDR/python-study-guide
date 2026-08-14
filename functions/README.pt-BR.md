<div align="center">

# Funções

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Trilha completa](../docs/learning-path.pt-BR.md) · [Roadmap](../docs/roadmap.pt-BR.md)

Funções é a Fase 5 da sequência principal do Python Study Guide.

Fluxo do Programa ensinou como a execução toma decisões e repete trabalho. Esta fase ensina a dar nome a comportamentos, passar dados para eles, devolver resultados, controlar escopo, descrever interfaces, combinar pequenas partes em programas mais claros e rastrear dados através das fronteiras entre funções.

## Pré-requisito

Conclua primeiro a [Fase 4: Fluxo do Programa](../program-flow/README.pt-BR.md).

Antes de continuar, você já deve estar confortável com variáveis e tipos nativos, strings, números, coleções, condições booleanas, `if`, `elif`, `else`, `match`, `case`, `for`, `while`, `range()`, `enumerate()`, `zip()`, `break`, `continue`, `else` de loop e com escolher e combinar ferramentas de fluxo de acordo com a intenção.

## Trilha de aprendizagem

| Capítulo | Foco principal | Status |
|---|---|---|
| [01. Definindo e Chamando Funções](01-defining-and-calling-functions/README.pt-BR.md) | Criar comportamento nomeado com `def`, chamar, reutilizar e rastrear a execução | Disponível |
| [02. Parâmetros e Argumentos](02-parameters-and-arguments/README.pt-BR.md) | Receber entradas obrigatórias com argumentos posicionais e nomeados básicos | Disponível |
| [03. Valores de Retorno](03-return-values/README.pt-BR.md) | Enviar resultados úteis ao chamador e rastrear o fluxo completo de entrada e saída | Disponível |
| [04. Escopo](04-scope/README.pt-BR.md) | Entender nomes locais e globais, busca, sombreamento e religação global explícita | Disponível |
| [05. Type Hints](05-type-hints/README.pt-BR.md) | Descrever entradas e saídas esperadas sem impor tipos em runtime por conta própria | Disponível |
| [06. Valores Padrão](06-default-values/README.pt-BR.md) | Projetar argumentos opcionais com segurança, incluindo avaliação na definição e padrões mutáveis | Disponível |
| [07. `*args` e `**kwargs`](07-args-and-kwargs/README.pt-BR.md) | Receber quantidades intencionalmente variáveis de argumentos posicionais e nomeados | Disponível |
| [08. Funções Trabalhando Juntas](08-functions-working-together/README.pt-BR.md) | Compor funções auxiliares e coordenadoras mantendo responsabilidades e dependências claras | Disponível |
| [09. Fluxo de Dados Entre Funções](09-data-flow-between-functions/README.pt-BR.md) | Rastrear entradas do chamador, vínculos de parâmetros, transformações, mutação, saídas retornadas e propriedade dos dados entre chamadas | Disponível |

Estude os capítulos em ordem ao seguir a trilha completa para iniciantes.

## Por que definição e chamada vêm primeiro

Uma função fica mais simples quando duas ideias estão firmes:

```text
definition = describe and name behavior
call       = execute that behavior now
```

O Capítulo 01 separa essas ideias antes de adicionar troca de dados. O Capítulo 02 adiciona entradas com parâmetros e argumentos. O Capítulo 03 completa a primeira viagem de ida e volta com valores de retorno, `None`, retornos por ramificação e a diferença entre retornar e imprimir. O Capítulo 04 adiciona escopo local e global, busca de nomes, sombreamento, comportamento de escopo de instruções comuns e uso cauteloso de `global`. O Capítulo 05 adiciona type hints de parâmetros e retorno, anotações de coleções, uniões com `None` e a diferença fundamental entre informação estática de tipos e enforcement em runtime. O Capítulo 06 adiciona valores padrão, substituições seletivas, avaliação no momento da definição e o padrão seguro com `None` para criar objetos mutáveis novos. O Capítulo 07 adiciona coleta de quantidade variável de argumentos posicionais e nomeados com `*args` e `**kwargs`, seus modelos de tupla/dicionário, assinaturas mistas simples e o limite entre coleta na definição e desempacotamento posterior na chamada. O Capítulo 08 conecta essas habilidades individuais ao compor funções auxiliares e coordenadoras, passar resultados retornados entre etapas, expor dependências por parâmetros e ler grafos simples de chamadas. O Capítulo 09 encerra a fase rastreando o fluxo chamador-parâmetro-retorno, vínculos locais de parâmetros, reatribuição versus mutação, resultados em tupla e `None`, pipelines explícitos e a diferença entre grafos de chamadas e rastreamentos de fluxo de dados.

## Progressão da fase

```text
define and call
    ↓
parameters and arguments
    ↓
return values
    ↓
scope
    ↓
type hints
    ↓
default values
    ↓
*args and **kwargs
    ↓
functions working together
    ↓
data flow between functions
```

## Limite de escopo

A Fase 5 trata de funções normais definidas pelo usuário e do movimento da execução e dos dados ao redor delas. Tratamento de erros, arquivos, módulos, bibliotecas externas, decorators, generators e recursos avançados de tipagem como generics, protocols e overloads aparecem depois ou exigem tratamento próprio.

## Trilha completa

Comece com [01. Definindo e Chamando Funções](01-defining-and-calling-functions/README.pt-BR.md), continue com [02. Parâmetros e Argumentos](02-parameters-and-arguments/README.pt-BR.md), depois estude [03. Valores de Retorno](03-return-values/README.pt-BR.md), [04. Escopo](04-scope/README.pt-BR.md), [05. Type Hints](05-type-hints/README.pt-BR.md), [06. Valores Padrão](06-default-values/README.pt-BR.md), [07. `*args` e `**kwargs`](07-args-and-kwargs/README.pt-BR.md), [08. Funções Trabalhando Juntas](08-functions-working-together/README.pt-BR.md) e [09. Fluxo de Dados Entre Funções](09-data-flow-between-functions/README.pt-BR.md).

Depois de concluir os nove capítulos, continue com a já publicada [Fase 6: Comentários, Documentação e Código Limpo](../comments-and-documentation/README.pt-BR.md).

**A Fase 5 está concluída com nove capítulos revisados disponíveis.**
