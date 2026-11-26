# Transações, índices e segurança em SQL

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../19-joins-aggregations-and-data-relationships/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../21-software-engineering-and-technical-decisions/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [technical-interview-preparation/19-joins-aggregations-and-data-relationships](../../technical-interview-preparation/19-joins-aggregations-and-data-relationships/README.pt-BR.md)
- [technical-interview-preparation/15-exceptions-testing-and-debugging-review](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.pt-BR.md)

## Transações e integridade

Transação agrupa operações numa unidade: commit aceita mudanças; rollback abandona mudanças não confirmadas. ACID: atomicidade (tudo ou nada), consistência (restrições/invariantes válidos), isolamento (regras de visibilidade entre transações concorrentes), durabilidade (mudanças confirmadas sobrevivem falhas conforme garantias de banco/armazenamento). Níveis de isolamento e garantias diferem por motor; banco em memória não é durável após saída do processo. Evite manter transações abertas durante rede. Restrições são proteção adicional, não substituem regras de negócio.

Exemplo transfere créditos inteiros entre duas contas distintas. Verifica origem e saldo disponível em UPDATE condicional, confere linhas afetadas, credita destino e faz rollback se destino não existe. Saldo inteiro não negativo é restringido no banco. Chamador fornece conexão dedicada com autocommit=False, sem escritas pendentes alheias, e confirma setup antes de chamar. Gerenciador de contexto da conexão Python 3.13 faz commit ao sair com sucesso e rollback em exceção (ou falha no commit); não fecha conexão. Com autocommit=True não fornece essa fronteira. Não reutilize exemplo como API de transações aninhadas nem sistema financeiro de produção.

Para verificar commit e não apenas saldo alterado no escritor, use banco SQLite temporário em arquivo. Abra conexão leitora separada em modo autocommit após confirmar setup; confira saldos novos após transferência. Na falha, verifique saldos intactos nas duas conexões; reabra banco para confirmar que alteração confirmada sobrevive ao fechamento da conexão. É teste de persistência/transação, não prova de durabilidade sob toda falha. Conexões independentes em memória normalmente não compartilham banco.

## Índices e plano de consulta

Índice é estrutura auxiliar que pode acelerar buscas, joins ou ordenação quando planejador escolhe. Custa armazenamento e manutenção de escritas; nem toda coluna merece índice. Ordem de colunas em índice composto importa para consultas. Índice não garante execução mais rápida. Inspecione plano representativo (SQLite EXPLAIN QUERY PLAN) e meça; tabelas pequenas podem legitimamente sofrer varredura.

```sql
CREATE INDEX idx_accounts_name ON accounts(name);
EXPLAIN QUERY PLAN SELECT id FROM accounts WHERE name = 'A';
```

Não exija texto exato do plano entre versões ou distribuições de dados.

## Segurança SQL

Vincule valores com parâmetros, não concatenação ou f-strings. Placeholders não vinculam identificadores de tabela/coluna; use SQL fixo ou mapeamento allowlist para identificadores confiáveis. Privilégio mínimo e validação separada continuam necessários. find_account vincula string; entrada com aspas permanece dado, não sintaxe.

## Prática

Transfira 3 créditos de saldos 10 e 2; espere 7 e 5. Depois transfira para destino inexistente e confira ambos inalterados. Teste saldo insuficiente, mesma conta, quantia inválida e busca com aspas. Explique por que rollback após débito é essencial.

**Referência rápida:** mudanças atômicas; ownership explícito da transação; parametrize valores; meça índices; teste falhas.

## Exemplo executável compartilhado

[credit_transfer.py](examples/credit_transfer.py)

`python technical-interview-preparation/20-transactions-indexes-and-sql-safety/examples/credit_transfer.py`

## Referências oficiais

- [docs.python.org/3.13/library/sqlite3.html](https://docs.python.org/3.13/library/sqlite3.html)
- [www.sqlite.org/lang_transaction.html](https://www.sqlite.org/lang_transaction.html)
- [www.sqlite.org/queryplanner.html](https://www.sqlite.org/queryplanner.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../19-joins-aggregations-and-data-relationships/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../21-software-engineering-and-technical-decisions/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
