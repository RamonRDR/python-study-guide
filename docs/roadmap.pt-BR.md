# Roadmap do Python Study Guide

[🇺🇸 English](roadmap.en.md) · [🇧🇷 Português](roadmap.pt-BR.md) · [🇪🇸 Español](roadmap.es.md)

Este roadmap acompanha tanto a trilha educacional quanto a fundação do repositório que a sustenta. A numeração das fases representa a sequência de aprendizagem pretendida, mas o trabalho no repositório pode antecipar seções posteriores quando isso ajudar a estabelecer padrões úteis.

## Legenda de status

- **Concluída:** o escopo planejado está disponível e revisado.
- **Em andamento:** já existe material útil, mas o escopo planejado ainda não foi encerrado.
- **Planejada:** a fase ainda não começou como uma seção completa de aprendizagem.

## Progresso atual

| Fase | Status | Resultado atual |
|---|---|---|
| 0. Fundação do projeto | Concluída | Fundação disponível, auditada e oficialmente concluída |
| 1. Fundamentos | Concluída | Seis capítulos revisados cobrem execução, entrada e saída, variáveis e nomes, tipos de dados embutidos, inspeção de tipos e conversão de tipos |
| 2. Textos e números | Concluída | Quatro capítulos revisados cobrem criação de strings, métodos comuns, comportamento numérico e booleano, precisão de ponto flutuante e funções numéricas embutidas |
| 3. Coleções | Concluída | Seis capítulos revisados cobrem listas, tuplas, dicionários, conjuntos e escolha da coleção pela intenção |
| 4. Fluxo do programa | Concluída | Oito capítulos revisados cobrem condições, ramificações, correspondência de padrões estruturais, `for`, auxiliares de iteração, `while`, controle de loops e escolha e combinação das ferramentas de fluxo pela intenção |
| 5. Funções | Em andamento | Oito capítulos revisados cobrem `def`, chamadas, entradas obrigatórias, valores retornados, escopo, type hints, valores padrão seguros, coleta flexível de argumentos posicionais e nomeados e composição de funções |
| 6. Comentários, documentação e código limpo | Concluída | Seis capítulos revisados estão disponíveis e a seção educacional-piloto está oficialmente concluída |
| 7. Erros, arquivos e módulos | Planejada | Conteúdo ainda não iniciado |
| 8. Biblioteca padrão | Planejada | Conteúdo ainda não iniciado |
| 9. Bibliotecas externas | Planejada | Conteúdo ainda não iniciado |
| 10. Projetos práticos | Planejada | Conteúdo ainda não iniciado |

As Fases 0, 1, 2, 3, 4 e 6 estão concluídas. A Fase 5: Funções está em andamento com definição, chamada, fluxo de entrada, fluxo de retorno, escopo, interfaces com type hints, comportamento de valores padrão, coleta de quantidade variável de argumentos posicionais e nomeados e composição por funções que cooperam já estabelecidos; Fluxo de Dados Entre Funções é o próximo passo. A Fase 6 continua fornecendo o modelo editorial e de qualidade para as seções posteriores.

## Fase 0: Fundação do projeto

### Itens concluídos

- [x] READMEs principais multilíngues
- [x] Estrutura inicial escalável
- [x] Guias de contribuição multilíngues
- [x] Templates de pull request e issues no GitHub
- [x] Padrões da comunidade e orientações para relatos
- [x] Formato editorial consistente para os capítulos
- [x] Licença MIT
- [x] Registros de autoria e manutenção
- [x] Fluxo baseado em pull requests e branch `main` protegida
- [x] Instruções do repositório para colaboradores e agentes de IA
- [x] Guia de desenvolvimento responsável assistido por IA
- [x] Roadmap e documentação da estrutura em três idiomas
- [x] Validações automáticas para arquivos Python, exemplos aprovados, links internos e estrutura
- [x] Identidade visual original e recursos do repositório
- [x] Auditoria final de navegação, terminologia, acessibilidade e status
- [x] Marcação oficial da Fase 0 como concluída

### Acompanhamento planejado e não bloqueante

- Refinar e substituir os recursos visuais por exportações de alta qualidade após a conclusão do enquadramento final da logomarca.

## Fase 1: Fundamentos

- [x] [Como o Python executa um programa](../fundamentals/01-how-python-runs-a-program/README.pt-BR.md)
- [x] [`print()` e `input()`](../fundamentals/02-print-and-input/README.pt-BR.md)
- [x] [Variáveis e nomes](../fundamentals/03-variables-and-naming/README.pt-BR.md)
- [x] [Tipos de dados embutidos](../fundamentals/04-built-in-data-types/README.pt-BR.md)
- [x] [`type()` e `isinstance()`](../fundamentals/05-type-and-isinstance/README.pt-BR.md)
- [x] [Conversão de tipos](../fundamentals/06-type-conversion/README.pt-BR.md)

## Fase 2: Textos e números

- [x] [Criação e indexação de strings](../strings-and-numbers/01-string-creation-and-indexing/README.pt-BR.md)
- [x] [Métodos comuns de strings](../strings-and-numbers/02-common-string-methods/README.pt-BR.md)
- [x] [`int`, `float` e `bool`](../strings-and-numbers/03-int-float-and-bool/README.pt-BR.md)
- [x] [Funções numéricas embutidas: `round()`, `abs()`, `min()`, `max()` e `sum()`](../strings-and-numbers/04-numeric-builtins/README.pt-BR.md)

## Fase 3: Coleções

- [x] [Criação, indexação e fatiamento de listas](../collections/01-list-creation-and-indexing/README.pt-BR.md)
- [x] [Modificando listas e métodos comuns de listas](../collections/02-modifying-lists-and-methods/README.pt-BR.md)
- [x] [Tuplas e imutabilidade](../collections/03-tuples-and-immutability/README.pt-BR.md)
- [x] [Dicionários: chaves e valores](../collections/04-dictionaries-keys-and-values/README.pt-BR.md)
- [x] [Conjuntos e valores únicos](../collections/05-sets-and-unique-values/README.pt-BR.md)
- [x] [Escolhendo a coleção certa](../collections/06-choosing-the-right-collection/README.pt-BR.md)

## Fase 4: Fluxo do programa

Consulte a [trilha de aprendizagem da seção](../program-flow/README.pt-BR.md).

- [x] [Condições, comparações e lógica booleana](../program-flow/01-conditions-comparisons-and-boolean-logic/README.pt-BR.md)
- [x] [`if`, `elif` e `else`](../program-flow/02-if-elif-and-else/README.pt-BR.md)
- [x] [`match` e `case`: correspondência de padrões estruturais](../program-flow/03-match-and-case/README.pt-BR.md)
- [x] [Loops `for` e iteração](../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [x] [`range()`, `enumerate()` e `zip()`](../program-flow/05-range-enumerate-and-zip/README.pt-BR.md)
- [x] [Loops `while` e repetição guiada por estado](../program-flow/06-while-loops-and-state-driven-repetition/README.pt-BR.md)
- [x] [`break`, `continue` e `else` de loops](../program-flow/07-break-continue-and-loop-else/README.pt-BR.md)
- [x] [Escolhendo e combinando o fluxo do programa](../program-flow/08-choosing-and-combining-program-flow/README.pt-BR.md)

A Fase 4 constrói intencionalmente condições confiáveis primeiro, usa essas condições para ramificações condicionais, introduz correspondência de padrões estruturais, avança para repetição com `for`, adiciona auxiliares para progressões numéricas, posições e iteração paralela, introduz repetição guiada por estado com `while`, adiciona controle deliberado de loops com `break`, `continue` e `else` de loop e encerra ensinando como escolher e combinar essas ferramentas de acordo com a intenção. Os Capítulos 01–08 estão concluídos e a Fase 4 está oficialmente concluída.

## Fase 5: Funções

Consulte a [trilha de aprendizagem da seção](../functions/README.pt-BR.md).

- [x] [Definindo e chamando funções](../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [x] [Parâmetros e argumentos](../functions/02-parameters-and-arguments/README.pt-BR.md)
- [x] [Valores de retorno](../functions/03-return-values/README.pt-BR.md)
- [x] [Escopo](../functions/04-scope/README.pt-BR.md)
- [x] [Type hints](../functions/05-type-hints/README.pt-BR.md)
- [x] [Valores padrão](../functions/06-default-values/README.pt-BR.md)
- [x] [`*args` e `**kwargs`](../functions/07-args-and-kwargs/README.pt-BR.md)
- [x] [Funções trabalhando juntas](../functions/08-functions-working-together/README.pt-BR.md)
- [ ] Fluxo de dados entre funções

A Fase 5 está em andamento. O Capítulo 01 estabelece `def`, chamadas, reuso, ordem de execução, nomenclatura, `pass`, `None` implícito e a conexão com o fluxo do programa. O Capítulo 02 adiciona parâmetros obrigatórios, argumentos posicionais e nomeados básicos, expressões como argumentos, erros de chamada e rastreamento do fluxo de entrada. O Capítulo 03 adiciona `return`, resultados reutilizáveis, retornos por ramificação e antecipados, `None` e retornos em tupla. O Capítulo 04 adiciona nomes locais e globais, namespaces locais por chamada, busca, sombreamento, `NameError`, `UnboundLocalError` e uso cauteloso de `global`. O Capítulo 05 adiciona anotações de parâmetros e retorno, hints de tipos embutidos e coleções, `-> None`, `str | None`, metadados de anotações e a diferença entre informação estática de tipos, validação em runtime e conversão. O Capítulo 06 adiciona valores padrão, substituições posicionais e nomeadas seletivas, avaliação no momento da definição, a armadilha de padrões mutáveis e o padrão seguro com `None` para criar objetos mutáveis novos. O Capítulo 07 adiciona coleta de quantidade variável de argumentos posicionais e nomeados com `*args` e `**kwargs`, comportamento de tupla e dicionário dentro da função, assinaturas mistas simples, type hints básicos para valores coletados e a distinção entre coleta na definição e desempacotamento posterior na chamada. O Capítulo 08 compõe funções auxiliares e coordenadoras, passa resultados retornados entre etapas, mantém dependências explícitas por parâmetros e retornos, combina funções com condições e loops, distingue cálculo reutilizável de apresentação e introduz grafos simples de chamadas. Fluxo de Dados Entre Funções é o próximo passo.

## Fase 6: Comentários, documentação e código limpo

Consulte a [trilha de aprendizagem da seção](../comments-and-documentation/README.pt-BR.md).

- [x] Quando e por que comentar
- [x] Quando não comentar
- [x] Comentários úteis e prejudiciais
- [x] Docstrings
- [x] Nomes significativos e código autoexplicativo
- [x] `TODO`, `FIXME`, `NOTE` e marcadores relacionados
- [x] Comentários versus logging
- [x] PEP 8 e legibilidade

A Fase 6 está oficialmente concluída e fornece o modelo editorial e de qualidade para as demais seções de aprendizagem.

## Fase 7: Erros, arquivos e módulos

- `try`, `except`, `else` e `finally`
- `raise` e exceções personalizadas
- `open()` e `with`
- TXT, CSV e JSON
- Imports, módulos e pacotes

## Fase 8: Biblioteca padrão

- `pathlib`
- `datetime`
- `json`
- `csv`
- `logging`
- `collections`
- `itertools`
- `decimal`
- `os` e `shutil`

## Fase 9: Bibliotecas externas

- `pandas`
- `openpyxl`
- `requests`
- `pytest`

## Fase 10: Projetos práticos

- Calculadora de médias
- Cadastro de usuários
- Controle de despesas
- Analisador de CSV
- Gerador de relatórios
- Organizador de arquivos
- Fluxo fictício de conciliação
- Fluxo simulado de automação

Cada projeto deve incluir:

- requisitos;
- notas de design;
- implementação;
- explicação;
- ideias de testes;
- desafios de extensão;
- discussão de portfólio.

## Critérios contínuos de qualidade

Cada fase deve preservar:

- precisão técnica;
- consistência multilíngue;
- exemplos originais e seguros para publicação;
- dados seguros do ponto de vista de privacidade;
- exemplos Python executáveis quando apropriado;
- integridade da navegação interna;
- atenção à PEP 8;
- documentação de mudanças estruturais relevantes;
- transparência sobre dependências e pressupostos de versão.

O roadmap evoluirá à medida que o projeto crescer, mas as mudanças devem preservar a progressão dos conceitos iniciais até o trabalho prático integrado.
