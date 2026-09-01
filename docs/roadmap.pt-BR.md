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
| 5. Funções | Concluída | Nove capítulos revisados cobrem `def`, chamadas, entradas obrigatórias, valores retornados, escopo, type hints, valores padrão seguros, argumentos flexíveis, composição de funções e fluxo explícito de dados |
| 6. Comentários, documentação e código limpo | Concluída | Seis capítulos revisados estão disponíveis e a seção educacional-piloto está oficialmente concluída |
| 7. Erros, arquivos e módulos | Concluída | Cinco capítulos revisados cobrem tratamento de exceções, sinalização deliberada, I/O seguro de arquivos, formatos TXT/CSV/JSON e imports/módulos/pacotes |
| 8. Biblioteca padrão | Concluída | Nove capítulos revisados cobrem caminhos, data/hora, JSON, CSV, logging, coleções especializadas, iteração lazy, aritmética decimal e operações de OS/filesystem |
| 9. Bibliotecas externas | Concluída | Quatro capítulos revisados cobrem pandas, openpyxl, requests e pytest com contratos explícitos de dependências e exemplos determinísticos |
| 10. Projetos práticos | Em andamento | Projetos 01–05 estão concluídos; o Projeto 06 Organizador de Arquivos está em andamento com planejamento determinístico, segurança de colisões, identidade de filesystem, diretórios ancorados e commit atômico no-replace |

As Fases 0–9 estão concluídas. A Fase 10: Projetos Práticos está em andamento com Controle de Despesas, Calculadora de Notas, Cadastro de Usuários, Analisador CSV e Gerador de Relatórios concluídos como Projetos 01–05, enquanto o Organizador de Arquivos é o atual Projeto 06. A fase transforma conceitos já estudados em fluxos completos com requisitos, decisões de design, implementação, validação, caminhos de extensão e discussão de portfólio.

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
- [x] [Fluxo de dados entre funções](../functions/09-data-flow-between-functions/README.pt-BR.md)

A Fase 5 está concluída. O Capítulo 01 estabelece `def`, chamadas, reuso, ordem de execução, nomenclatura, `pass`, `None` implícito e a conexão com o fluxo do programa. O Capítulo 02 adiciona parâmetros obrigatórios, argumentos posicionais e nomeados básicos, expressões como argumentos, erros de chamada e rastreamento do fluxo de entrada. O Capítulo 03 adiciona `return`, resultados reutilizáveis, retornos por ramificação e antecipados, `None` e retornos em tupla. O Capítulo 04 adiciona nomes locais e globais, namespaces locais por chamada, busca, sombreamento, `NameError`, `UnboundLocalError` e uso cauteloso de `global`. O Capítulo 05 adiciona anotações de parâmetros e retorno, hints de tipos embutidos e coleções, `-> None`, `str | None`, metadados de anotações e a diferença entre informação estática de tipos, validação em runtime e conversão. O Capítulo 06 adiciona valores padrão, substituições posicionais e nomeadas seletivas, avaliação no momento da definição, a armadilha de padrões mutáveis e o padrão seguro com `None` para criar objetos mutáveis novos. O Capítulo 07 adiciona coleta de quantidade variável de argumentos posicionais e nomeados com `*args` e `**kwargs`, comportamento de tupla e dicionário dentro da função, assinaturas mistas simples, type hints básicos para valores coletados e a distinção entre coleta na definição e desempacotamento posterior na chamada. O Capítulo 08 compõe funções auxiliares e coordenadoras, passa resultados retornados entre etapas, mantém dependências explícitas por parâmetros e retornos, combina funções com condições e loops, distingue cálculo reutilizável de apresentação e introduz grafos simples de chamadas. O Capítulo 09 encerra a fase rastreando o fluxo chamador-parâmetro-retorno, vínculos locais de parâmetros, reatribuição versus mutação, resultados em tupla e `None`, pipelines explícitos, transformações de coleções e a diferença entre grafos de chamadas e rastreamentos de fluxo de dados.

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

Consulte a [trilha de aprendizagem da seção](../errors-files-and-modules/README.pt-BR.md).

- [x] [`try`, `except`, `else` e `finally`](../errors-files-and-modules/01-try-except-else-finally/README.pt-BR.md)
- [x] [`raise` e exceções personalizadas](../errors-files-and-modules/02-raise-and-custom-exceptions/README.pt-BR.md)
- [x] [`open()` e `with`](../errors-files-and-modules/03-open-and-with/README.pt-BR.md)
- [x] [TXT, CSV e JSON](../errors-files-and-modules/04-txt-csv-and-json/README.pt-BR.md)
- [x] [Imports, módulos e pacotes](../errors-files-and-modules/05-imports-modules-and-packages/README.pt-BR.md)

A Fase 7 está concluída. Os Capítulos 01–02 estabelecem tratamento e sinalização deliberada de exceções. O Capítulo 03 acrescenta I/O seguro de arquivos e gerenciamento de recursos. O Capítulo 04 acrescenta parsing e escrita de TXT, CSV e JSON com fronteiras explícitas de dados. O Capítulo 05 encerra a fase com módulos, pacotes regulares, namespaces e cache de imports, `__name__`, main guard, contexto de busca, imports absolutos e relativos, `python -m` e design de dependências.

## Fase 8: Biblioteca padrão

Veja a [trilha de aprendizagem da seção](../standard-library/README.pt-BR.md).

- [x] [`pathlib`](../standard-library/01-pathlib/README.pt-BR.md)
- [x] [`datetime`](../standard-library/02-datetime/README.pt-BR.md)
- [x] [`json`](../standard-library/03-json/README.pt-BR.md)
- [x] [`csv`](../standard-library/04-csv/README.pt-BR.md)
- [x] [`logging`](../standard-library/05-logging/README.pt-BR.md)
- [x] [`collections`](../standard-library/06-collections/README.pt-BR.md)
- [x] [`itertools`](../standard-library/07-itertools/README.pt-BR.md)
- [x] [`decimal`](../standard-library/08-decimal/README.pt-BR.md)
- [x] [`os` e `shutil`](../standard-library/09-os-shutil/README.pt-BR.md)

A Fase 8 está concluída. Os Capítulos 01–08 constroem contratos para caminhos, data/hora, formatos estruturados, logging, coleções especializadas, iteração lazy e aritmética decimal. O Capítulo 09 encerra a fase conectando essas bases a estado do ambiente do processo, interfaces path-like, varredura e travessia de diretórios, metadados, cópia, movimento, remoção recursiva, capacidades de plataforma e segurança de archives.

## Fase 9: Bibliotecas externas

Veja a [trilha de aprendizagem da seção](../external-libraries/README.pt-BR.md).

- [x] [`pandas`](../external-libraries/01-pandas/README.pt-BR.md)
- [x] [`openpyxl`](../external-libraries/02-openpyxl/README.pt-BR.md)
- [x] [`requests`](../external-libraries/03-requests/README.pt-BR.md)
- [x] [`pytest`](../external-libraries/04-pytest/README.pt-BR.md)

A Fase 9 está concluída. O Capítulo 01 introduz pandas 3.0.x para dados tabulares rotulados. O Capítulo 02 acrescenta automação de workbooks com openpyxl 3.1.x. O Capítulo 03 acrescenta contratos HTTP/API com Requests 2.34.x. O Capítulo 04 encerra a fase com contratos de testes automatizados em pytest 9.1.x, cobrindo descoberta, assertions, fixtures, parametrização, recursos temporários, monkeypatching, captura, marks, isolamento determinístico e CI. Os exemplos executáveis usam o contrato declarado em [`requirements-external.txt`](../requirements-external.txt).

## Fase 10: Projetos práticos

Veja o [índice da seção Projetos Práticos](../practical-projects/README.pt-BR.md).

- [x] [Controle de Despesas](../practical-projects/01-expense-tracker/README.pt-BR.md)
- [x] [Calculadora de Notas](../practical-projects/02-grade-calculator/README.pt-BR.md)
- [x] [Cadastro de Usuários](../practical-projects/03-user-registration/README.pt-BR.md)
- [x] [Analisador CSV](../practical-projects/04-csv-analyzer/README.pt-BR.md)
- [x] [Gerador de Relatórios](../practical-projects/05-report-generator/README.pt-BR.md)
- [ ] [Organizador de Arquivos](../practical-projects/06-file-organizer/README.pt-BR.md) — projeto atual
- [ ] Fluxo Fictício de Conciliação
- [ ] Fluxo Simulado de Automação

O Projeto 01 estabelece o contrato da Fase 10 com requisitos explícitos, modelagem de dados validada, dinheiro exato com `Decimal`, persistência, demonstração determinística, cobertura automatizada com pytest, desafios de extensão e discussão de portfólio. O Projeto 02 estende o contrato com regras configuráveis de notas, agregação ponderada exata, relatórios parcial/final explícitos e validação focada em fronteiras. O Projeto 03 adiciona dados de identidade canônicos, normalização Unicode e IDNA, prevenção de duplicidade, índices secundários de lookup, atualizações seguras de campos indexados, transições explícitas de ciclo de vida e cobertura pytest focada em mutação sem introduzir autenticação. O Projeto 04 adiciona schemas CSV estritos, conversão tipada, tratamento de falhas estruturais versus falhas por linha, parsing com sucesso parcial, identificadores aceitos duplicados, agregação determinística e filtragem usando mecanismos CSV da biblioteca padrão de forma explícita. O Projeto 05 adiciona janelas inclusivas de datas, validação de identidade de origem, métricas de resumo exatas e determinísticas, construção imutável de relatórios, renderização TXT/Markdown, escape específico do formato e saída UTF-8. O Projeto 06 adiciona descoberta rasa determinística, planejamento imutável, categorias por sufixo, políticas explícitas de colisão, fronteiras de symlink, identidade `(device, inode)`, ancoragem de descriptors de raiz/categorias, nomes de staging limitados e commits atômicos no-replace sensíveis à plataforma com `renameat2(RENAME_NOREPLACE)` no Linux.

Cada projeto deve incluir:

- requisitos;
- notas de design;
- implementação;
- explicação;
- cobertura automatizada para comportamentos importantes;
- desafios de extensão;
- discussão de portfólio.

## Gates contínuos de qualidade

Cada fase deve preservar:

- precisão técnica;
- consistência multilíngue;
- exemplos originais e seguros para publicação;
- dados seguros para privacidade;
- exemplos Python executáveis quando apropriado;
- integridade de navegação interna;
- atenção ao PEP 8;
- documentação de mudanças estruturais relevantes;
- premissas honestas sobre dependências e versões.

O roadmap evoluirá conforme o projeto crescer, mas as mudanças devem preservar a progressão de conceitos iniciantes para trabalho prático integrado.
