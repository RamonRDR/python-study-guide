# Encapsulamento, abstração e SOLID

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../07-inheritance-polymorphism-and-composition/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [manual-programming-practices/02-specification-driven-development](../../manual-programming-practices/02-specification-driven-development/README.pt-BR.md)
- [manual-programming-practices/03-test-driven-development](../../manual-programming-practices/03-test-driven-development/README.pt-BR.md)
- [practical-projects/03-user-registration](../../practical-projects/03-user-registration/README.pt-BR.md)

## Encapsulamento e abstração

Encapsulamento expõe operações que preservam estado válido. No exemplo de estoque, remove valida antes de alterar quantidade. Um sublinhado inicial indica detalhe não público por convenção; dois sublinhados iniciais ativam name mangling, não segurança. Uma property pode expor leitura sem setter normal; chamadores ainda podem contornar convenções, então isso não é uma fronteira de controle de acesso.

Abstração define o que um colaborador promete sem obrigar chamadores a saber como funciona. `ABC` e `@abstractmethod` da biblioteca padrão expressam contrato abstrato explícito: uma subclasse concreta deve implementar os métodos abstratos antes da instanciação normal. `StockReader` define available; um leitor de memória ou outra fonte pode respeitar o mesmo contrato. Type hint sozinho não impõe comportamento em runtime.

## SOLID como perguntas de design

| Princípio | Pergunta prática |
| --- | --- |
| Responsabilidade única (SRP) | Este componente tem uma razão coerente para mudar? |
| Aberto/fechado (OCP) | Uma variação planejada pode ser suportada por ponto de extensão estável sem alterar todos os chamadores? |
| Substituição de Liskov (LSP) | Um subtipo pode substituir a base sem quebrar o comportamento prometido? |
| Segregação de interfaces (ISP) | O chamador depende apenas das operações necessárias? |
| Inversão de dependência (DIP) | A política de alto nível pode depender de abstração útil em vez de detalhe concreto de infraestrutura? |

O exemplo de estoque separa regras de estado de leitura; o leitor expõe apenas available; remaining depende desse contrato. Um leitor fake apoia testes. SOLID é um conjunto de heurísticas de design, não sintaxe Python nem exigência de cinco classes. Um cálculo pontual pode precisar apenas de uma função. Introduza abstrações quando reduzirem acoplamento relevante ou apoiarem variação real.

## Prática

Adicione leitor fake retornando 7 e verifique remaining sem modificá-lo. Tente retirar mais do que o estoque contém; teste que quantidade não muda. Explique quais dois princípios SOLID se aplicam e um custo de introduzir uma abstração adicional.

**Referência rápida:** proteja invariantes, exponha contratos pequenos, favoreça substituição útil, justifique complexidade.

[Exemplo executável compartilhado](examples/stock.py)

`python technical-interview-preparation/08-encapsulation-abstraction-and-solid/examples/stock.py`

## Referências oficiais (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)
- [abc](https://docs.python.org/3.13/library/abc.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../07-inheritance-polymorphism-and-composition/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
