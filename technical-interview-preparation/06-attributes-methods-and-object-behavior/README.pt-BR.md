# Atributos, métodos e comportamento de objetos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../05-classes-and-objects/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../07-inheritance-polymorphism-and-composition/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [functions/06-default-values](../../functions/06-default-values/README.pt-BR.md)
- [collections/02-modifying-lists-and-methods](../../collections/02-modifying-lists-and-methods/README.pt-BR.md)

## Atributos e vinculação

Um atributo de instância armazena dados por objeto; um atributo de classe normalmente fornece dados compartilhados acessíveis pelas instâncias. Atribuir atributo de instância com mesmo nome costuma sombrear o atributo de classe. Um atributo mutável de classe, como lista, é erro comum de compartilhamento acidental; inicialize listas independentes em `__init__`.

| Tipo de método | Recebe implicitamente | Finalidade |
| --- | --- | --- |
| Instância | self | Ler ou alterar estado da instância |
| Classe | cls | Construtores alternativos ou comportamento da classe |
| Estático | Nenhum | Utilitário relacionado sem estado implícito |

Os marcadores nativos `@classmethod` e `@staticmethod` alteram vinculação; o mecanismo geral de decorators é ensinado depois. No exemplo, `from_label` chama cls para poder construir uma subclasse; `valid_label` não precisa de instância. Um método estático não é automaticamente puro.

## Métodos especiais

Nomes como `__len__`, `__str__` e `__repr__` integram objetos às operações Python. `len(group)` usa o protocolo de comprimento; `str(group)` é voltado ao usuário; repr ajuda no debugging e não precisa ser Python executável. Respeite contratos documentados (comprimento deve ser inteiro não negativo). Igualdade e hashing exigem semânticas compatíveis; contratos aprofundados aparecem na aula de identidade. Evite inventar nomes dunder.

## Prática

Execute o exemplo compartilhado de grupo de estudo. Crie dois grupos, adicione um membro apenas a um e confira ambos os comprimentos. Explique por que a lista members é por instância e category é compartilhado. Adicione teste de rótulo vazio. Compare str e repr.

**Referência rápida:** self = instância; cls = classe; estático = sem argumento implícito; métodos especiais implementam protocolos.

[Exemplo executável compartilhado](examples/study_group.py)

`python technical-interview-preparation/06-attributes-methods-and-object-behavior/examples/study_group.py`

## Referências oficiais (Python 3.13)

- [Classes](https://docs.python.org/3.13/tutorial/classes.html)
- [Data model](https://docs.python.org/3.13/reference/datamodel.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../05-classes-and-objects/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../07-inheritance-polymorphism-and-composition/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
