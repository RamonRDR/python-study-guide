<div align="center">

# Funções

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Trilha completa](../docs/learning-path.pt-BR.md) · [Roadmap](../docs/roadmap.pt-BR.md)

Funções é a Fase 5 da sequência principal do Python Study Guide.

Fluxo do Programa ensinou como a execução toma decisões e repete trabalho. Esta fase ensina como **dar nome a comportamentos, passar dados para eles, devolver resultados, controlar escopo, descrever interfaces e combinar pequenas partes em programas mais claros**.

## Pré-requisito

Conclua primeiro a [Fase 4: Fluxo do Programa](../program-flow/README.pt-BR.md).

Você já deve estar confortável com:

- variáveis e tipos nativos;
- strings, números e coleções;
- condições booleanas;
- `if`, `elif` e `else`;
- `match` e `case`;
- `for` e `while`;
- `range()`, `enumerate()` e `zip()`;
- `break`, `continue` e `else` de loop;
- escolha e combinação de ferramentas de fluxo por intenção.

## Trilha de aprendizagem

| Capítulo | Foco principal | Status |
|---|---|---|
| [01. Definindo e Chamando Funções](01-defining-and-calling-functions/README.pt-BR.md) | Criar comportamento nomeado com `def`, chamar, reutilizar e rastrear a execução | Disponível |
| [02. Parâmetros e Argumentos](02-parameters-and-arguments/README.pt-BR.md) | Receber entradas obrigatórias com argumentos posicionais e nomeados básicos | Disponível |
| 03. Valores de Retorno | Enviar resultados úteis de volta ao chamador | Planejado |
| 04. Escopo | Entender onde nomes são visíveis e como a busca funciona | Planejado |
| 05. Type Hints | Descrever entradas e saídas esperadas sem alterar sozinhos o comportamento em runtime | Planejado |
| 06. Valores Padrão | Projetar argumentos opcionais com clareza e segurança | Planejado |
| 07. `*args` e `**kwargs` | Receber quantidades variáveis de argumentos posicionais e nomeados | Planejado |
| 08. Funções Trabalhando Juntas | Compor funções mantendo responsabilidades claras | Planejado |
| 09. Fluxo de Dados Entre Funções | Rastrear entradas, transformações, saídas e responsabilidade entre chamadas | Planejado |

Estude os capítulos em ordem ao seguir a trilha completa para iniciantes.

## Por que definição e chamada vêm primeiro

Uma função fica muito mais simples quando duas ideias estão firmes:

```text
definition = describe and name behavior
call       = execute that behavior now
```

O Capítulo 01 isola essas ideias antes de adicionar troca de dados.

O Capítulo 02 adiciona parâmetros obrigatórios, argumentos posicionais e argumentos nomeados básicos para que uma função trabalhe com entradas diferentes. O Capítulo 03 adicionará valores de retorno. Os capítulos seguintes construirão escopo, type hints, padrões, coleta flexível de argumentos, composição e fluxo explícito de dados sobre o mesmo modelo de definição/chamada.

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

A Fase 5 foca funções normais definidas pelo usuário e o movimento da execução e dos dados ao redor delas.

Ela não exige:

- tratamento de exceções com `try` e `except`;
- manipulação de arquivos;
- módulos e pacotes como assunto principal;
- bibliotecas externas;
- decorators;
- generators;
- padrões avançados de programação funcional.

Esses conceitos aparecem depois ou exigem tratamento próprio.

## Comece aqui

Comece com [01. Definindo e Chamando Funções](01-defining-and-calling-functions/README.pt-BR.md) e depois continue com [02. Parâmetros e Argumentos](02-parameters-and-arguments/README.pt-BR.md).

Depois do Capítulo 02, o próximo capítulo planejado é **03. Valores de Retorno**.

**A Fase 5 agora está em andamento com dois capítulos revisados disponíveis.**
