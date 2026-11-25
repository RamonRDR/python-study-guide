# Herança, polimorfismo e composição

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../06-attributes-methods-and-object-behavior/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../08-encapsulation-abstraction-and-solid/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [Aula anterior de OOP](../06-attributes-methods-and-object-behavior/README.pt-BR.md)
- [errors-files-and-modules/01-try-except-else-finally](../../errors-files-and-modules/01-try-except-else-finally/README.pt-BR.md)

## Herança e substituição

Herança cria uma subclasse, escrita `class Child(Parent):`. Ela pode reutilizar ou sobrescrever comportamento herdado. Use quando o subtipo respeita o contrato da base, não apenas porque duas implementações têm linhas similares. Em exemplo de herança simples, `super().__init__(...)` pode inicializar a parte base; de forma geral super segue a ordem de resolução de métodos, não simplesmente um pai fixo.

## Polimorfismo e composição

Polimorfismo permite ao chamador usar operação comum com implementações diferentes. Python frequentemente permite duck typing: um objeto pode atender um contrato comportamental sem compartilhar classe base. Composição armazena ou recebe um colaborador em vez de herdar sua implementação. No exemplo compartilhado, Notifier delega ao método send do canal. O canal retorna texto, não uma mensagem real de rede. Ele pode ser substituído por outro canal compatível ou fake em teste. TextChannel e EmailChannel sobrescrevem Channel.send, enquanto o contrato base declara que subclasses devem fornecer a operação. Uma classe independente com o mesmo contrato também pode funcionar.

Evite hierarquias profundas escolhidas só para reutilizar código; não suponha que nomes de métodos iguais garantem semântica igual. Composição adiciona dependência explícita, que pode ser mais fácil de substituir, mas pode acrescentar indireção.

## Prática

Adicione um canal fictício de log que retorne `"log: Ready"` para mensagem `"Ready"` sem alterar Notifier. Teste um fake e explique o contrato que todos os canais devem respeitar. Explique um caso em que herança é adequada e outro em que composição é mais simples.

**Referência rápida:** herança = relação de subtipo; polimorfismo = comportamento intercambiável; composição = colaboração.

[Exemplo executável compartilhado](examples/notifications.py)

`python technical-interview-preparation/07-inheritance-polymorphism-and-composition/examples/notifications.py`

## Referências oficiais (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../06-attributes-methods-and-object-behavior/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../08-encapsulation-abstraction-and-solid/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
