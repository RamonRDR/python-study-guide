# Bancos de dados relacionais e SQL

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../17-api-contracts-authentication-and-authorization/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../19-joins-aggregations-and-data-relationships/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [technical-interview-preparation/13-context-managers](../../technical-interview-preparation/13-context-managers/README.pt-BR.md)
- [technical-interview-preparation/17-api-contracts-authentication-and-authorization](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.pt-BR.md)

## Modelo relacional e restrições

Banco relacional organiza dados em tabelas de linhas e colunas com relacionamentos e restrições. Chave primária identifica linha; UNIQUE restringe duplicados, NOT NULL exige valor, CHECK impõe predicado e chaves estrangeiras conectam linhas (próxima aula). NULL representa informação ausente/desconhecida; use IS NULL, não = NULL. Comparações SQL com NULL geralmente resultam desconhecido, e WHERE mantém linhas verdadeiras. CHECK sozinho não proíbe NULL; combine com NOT NULL quando necessário.

SQLite é banco SQL embarcado; módulo sqlite3 do Python funciona com arquivo local ou banco :memory:. Outros motores diferem em tipos, sintaxe, isolamento e implantação. SQLite tem tipagem flexível: INTEGER declarado não é verificação universal estrita, então exemplo verifica tipo armazenado e positividade. SQL pode converter entradas antes de armazenar; valide tipos do domínio também na aplicação.

```sql
CREATE TABLE lessons (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL UNIQUE,
    minutes INTEGER NOT NULL CHECK (minutes > 0)
);
INSERT INTO lessons(title, minutes) VALUES ('SQL', 20);
SELECT title, minutes FROM lessons
WHERE minutes <= 20 ORDER BY minutes, title;
```

Resultado: SQL, 20. CREATE altera schema; INSERT cria linhas; SELECT lê; UPDATE altera linhas selecionadas; DELETE remove linhas selecionadas. UPDATE/DELETE sem WHERE podem afetar todas. ORDER BY é necessário para ordem garantida; LIMIT sozinho não define quais vêm primeiro. Selecione colunas necessárias em vez de dados desnecessários.

## Conectar com Python

Use conexão e execute com placeholders para valores, por exemplo `db.execute("SELECT title FROM lessons WHERE minutes <= ?", (20,))`. Tupla de um elemento precisa da vírgula. Use fetchall para resultados pequenos; itere cursor para maiores. Exemplo usa autocommit=True explicitamente para instruções independentes e contextlib.closing para liberar recurso; gerenciador de contexto da conexão não a fecha. Transações na aula 20.

## Prática

Adicione aulas, filtre duração, confira ordem determinística e verifique falhas para título duplicado, nulo e duração zero. Explique restrição de schema versus validação de aplicação. Use Python 3.13 local; não precisa servidor de banco.

**Referência rápida:** modele linhas e chaves; restrinja integridade; consulte explicitamente; vincule valores; feche conexões.

## Exemplo executável compartilhado

[lesson_catalog.py](examples/lesson_catalog.py)

`python technical-interview-preparation/18-relational-databases-and-sql/examples/lesson_catalog.py`

## Referências oficiais

- [docs.python.org/3.13/library/sqlite3.html](https://docs.python.org/3.13/library/sqlite3.html)
- [www.sqlite.org/lang_createtable.html](https://www.sqlite.org/lang_createtable.html)
- [www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../17-api-contracts-authentication-and-authorization/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../19-joins-aggregations-and-data-relationships/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
