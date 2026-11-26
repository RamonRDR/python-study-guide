# Joins, agregações e relacionamentos de dados

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../18-relational-databases-and-sql/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../20-transactions-indexes-and-sql-safety/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [technical-interview-preparation/18-relational-databases-and-sql](../../technical-interview-preparation/18-relational-databases-and-sql/README.pt-BR.md)

## Relacionamentos e cardinalidade de joins

Um-para-muitos: grupo tem várias tarefas, cada tarefa pertence a um grupo. Chave estrangeira impede referências órfãs quando fiscalização está ativa. Muitos-para-muitos usa tabela associativa (ex.: matrícula com learner_id e lesson_id como chave primária composta). Um-para-um pode usar chave estrangeira única. Normalização separa fatos repetidos para reduzir anomalias de atualização; desnormalização é trade-off deliberado, não correção padrão de desempenho. No SQLite ative foreign_keys por conexão antes de qualquer transação e verifique.

INNER JOIN mantém linhas correspondentes. LEFT JOIN mantém toda linha esquerda e preenche colunas direitas sem correspondência com NULL. Mais de um filho correspondente gera mais de uma linha; juntar múltiplas relações um-para-muitos pode multiplicar contagens. Agrupe na granularidade correta ou pré-agregue. Exemplo conta tarefas concluídas de todo grupo, mesmo sem tarefas ou sem concluídas.

```sql
SELECT groups.name, COUNT(tasks.id)
FROM groups LEFT JOIN tasks
    ON groups.id = tasks.group_id AND tasks.done = 1
GROUP BY groups.id, groups.name
ORDER BY groups.name, groups.id;
```

Filtro em ON limita correspondências preservando linhas esquerdas; tasks.done = 1 em WHERE elimina linhas estendidas com NULL. COUNT(*) conta linhas incluindo linha estendida com NULL; COUNT(coluna) exclui NULL. Use ID não nulo do filho aqui.

## Agregações

SUM soma valores não nulos, AVG calcula média, MIN/MAX encontram extremos; COUNT conta conforme acima. Entrada vazia pode resultar NULL em SUM/AVG; decida se COALESCE(..., 0) corresponde ao significado de negócio. WHERE filtra linhas antes de agrupar; HAVING filtra grupos após agregar (ex.: HAVING COUNT(tasks.id) >= 2). GROUP BY identificador estável, não somente nome de exibição não único. Resultados não têm ordem garantida sem ORDER BY.

## Prática

Crie três grupos: duas tarefas concluídas para A, somente incompletas para B e nenhuma para C. Espere A=2, B=0, C=0. Mova filtro para WHERE e observe grupos ausentes em sua cópia. Teste tarefa referenciando grupo inexistente e explique importância da fiscalização.

**Referência rápida:** join por chaves; escolha cardinalidade; filtre na etapa correta; conte filhos não nulos.

## Exemplo executável compartilhado

[group_progress.py](examples/group_progress.py)

`python technical-interview-preparation/19-joins-aggregations-and-data-relationships/examples/group_progress.py`

## Referências oficiais

- [www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)
- [www.sqlite.org/lang_aggfunc.html](https://www.sqlite.org/lang_aggfunc.html)
- [www.sqlite.org/foreignkeys.html](https://www.sqlite.org/foreignkeys.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../18-relational-databases-and-sql/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../20-transactions-indexes-and-sql-safety/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
