# Engenharia de software e decisões técnicas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../20-transactions-indexes-and-sql-safety/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [manual-programming-practices/02-specification-driven-development](../../manual-programming-practices/02-specification-driven-development/README.pt-BR.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.pt-BR.md)
- [technical-interview-preparation/08-encapsulation-abstraction-and-solid](../../technical-interview-preparation/08-encapsulation-abstraction-and-solid/README.pt-BR.md)
- [technical-interview-preparation/20-transactions-indexes-and-sql-safety](../../technical-interview-preparation/20-transactions-indexes-and-sql-safety/README.pt-BR.md)

## Decisões começam no requisito

Separe comportamento funcional de atributos de qualidade (latência, confiabilidade, manutenibilidade, segurança, custo). Esclareça restrições e exemplos de aceite antes de código. SDD transforma necessidades em especificação, plano, tarefas e critérios observáveis; TDD testa comportamento primeiro, observa falha, implementa e refatora com testes verdes. Não alegue Red observado sem executar. ADR registra contexto, alternativas, decisão e consequências. Prefira design pequeno manutenível a abstrações prematuras.

Para relatório fictício de progresso, requisito é contar IDs únicos de aulas concluídas para aluno fornecido. Histórico vazio retorna zero, IDs inválidos falham, falha de armazenamento propaga. Exemplo injeta callable que carrega IDs, tornando regra testável sem banco real. É regra de relatório somente leitura, não API autenticada. Autorização pertence à fronteira protegida. Testes unitários usam loaders falsos; testes de integração de repositório real verificariam consulta e mapeamento com banco real.

## Trade-offs e operação

| Decisão | Pergunta a fazer |
| --- | --- |
| Monólito modular vs serviços | Escala/deploy independentes valem complexidade de rede e operação? |
| Cache vs leitura direta | Que defasagem, invalidação e orçamento de memória são aceitáveis? |
| Sync vs async | Carga medida espera I/O, e dependências são compatíveis? |
| SQL vs outro modelo | Que padrões de integridade, consulta e acesso predominam? |

Defina baseline e sucesso mensurável; não deduza velocidade de rótulos de arquitetura. Use controle de versão com mudanças focadas, checks automatizados de CI, revisão e plano testado de deploy/rollback. Separe configuração de código, não comite segredos e aplique privilégio mínimo. Observabilidade combina logs estruturados, métricas e traces para investigar falhas; registre contexto útil sem dados privados, observe latência/erros e distinga sintomas de causas. Implante migrações compatíveis deliberadamente; rollback de código pode não desfazer mudanças em dados.

## Prática

Escreva critérios de aceite do relatório, compare chamadas de banco dentro da regra com loader injetado, registre ADR curto e teste falha de dependência. Explique alternativa, trade-off, medição e estratégia de rollback. Estude guia Git dedicado separadamente para fluxos aprofundados de plataforma; nenhum pré-requisito externo obrigatório.

**Referência rápida:** esclareça; especifique; teste; escolha por trade-offs; observe; revise e verifique.

## Exemplo executável compartilhado

[progress_report.py](examples/progress_report.py)

`python technical-interview-preparation/21-software-engineering-and-technical-decisions/examples/progress_report.py`

## Referências oficiais

- [docs.python.org/3.13/library/unittest.html](https://docs.python.org/3.13/library/unittest.html)
- [docs.python.org/3.13/library/logging.html](https://docs.python.org/3.13/library/logging.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../20-transactions-indexes-and-sql-safety/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
