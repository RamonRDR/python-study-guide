# Bases de datos relacionales y SQL

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../17-api-contracts-authentication-and-authorization/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../19-joins-aggregations-and-data-relationships/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [technical-interview-preparation/13-context-managers](../../technical-interview-preparation/13-context-managers/README.es.md)
- [technical-interview-preparation/17-api-contracts-authentication-and-authorization](../../technical-interview-preparation/17-api-contracts-authentication-and-authorization/README.es.md)

## Modelo relacional y restricciones

Base relacional organiza datos en tablas de filas y columnas con relaciones y restricciones. Clave primaria identifica fila; UNIQUE restringe duplicados, NOT NULL exige valor, CHECK impone predicado y claves foráneas conectan filas (siguiente lección). NULL representa información ausente/desconocida; usa IS NULL, no = NULL. Comparaciones SQL con NULL generalmente resultan desconocidas, y WHERE conserva filas verdaderas. CHECK por sí solo no prohíbe NULL; combina con NOT NULL cuando se necesite.

SQLite es base SQL embebida; módulo sqlite3 de Python funciona con archivo local o base :memory:. Otros motores difieren en tipos, sintaxis, aislamiento e implementación. SQLite tiene tipado flexible: INTEGER declarado no es comprobación universal estricta, así que ejemplo verifica tipo almacenado y positividad. SQL puede convertir entradas antes de almacenar; valida tipos del dominio también en aplicación.

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

Resultado: SQL, 20. CREATE altera schema; INSERT crea filas; SELECT lee; UPDATE cambia filas seleccionadas; DELETE elimina filas seleccionadas. UPDATE/DELETE sin WHERE pueden afectar todas. ORDER BY es necesario para orden garantizado; LIMIT solo no define cuáles llegan primero. Selecciona columnas necesarias en lugar de datos innecesarios.

## Conectar con Python

Usa conexión y execute con placeholders para valores, por ejemplo `db.execute("SELECT title FROM lessons WHERE minutes <= ?", (20,))`. Tupla de un elemento necesita coma. Usa fetchall para resultados pequeños; itera cursor para mayores. Ejemplo usa autocommit=True explícitamente para instrucciones independientes y contextlib.closing para liberar recurso; gestor de contexto de conexión no la cierra. Transacciones en lección 20.

## Práctica

Añade lecciones, filtra duración, comprueba orden determinista y verifica fallos de título duplicado, nulo y duración cero. Explica restricción de schema frente a validación de aplicación. Usa Python 3.13 local; no necesita servidor de base.

**Referencia rápida:** modela filas y claves; restringe integridad; consulta explícitamente; enlaza valores; cierra conexiones.

## Ejemplo ejecutable compartido

[lesson_catalog.py](examples/lesson_catalog.py)

`python technical-interview-preparation/18-relational-databases-and-sql/examples/lesson_catalog.py`

## Referencias oficiales

- [docs.python.org/3.13/library/sqlite3.html](https://docs.python.org/3.13/library/sqlite3.html)
- [www.sqlite.org/lang_createtable.html](https://www.sqlite.org/lang_createtable.html)
- [www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../17-api-contracts-authentication-and-authorization/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../19-joins-aggregations-and-data-relationships/README.es.md)
<!-- /chapter-navigation:bottom -->
