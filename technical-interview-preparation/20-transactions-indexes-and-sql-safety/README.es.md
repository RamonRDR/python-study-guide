# Transacciones, índices y seguridad en SQL

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../19-joins-aggregations-and-data-relationships/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../21-software-engineering-and-technical-decisions/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [technical-interview-preparation/19-joins-aggregations-and-data-relationships](../../technical-interview-preparation/19-joins-aggregations-and-data-relationships/README.es.md)
- [technical-interview-preparation/15-exceptions-testing-and-debugging-review](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)

## Transacciones e integridad

Transacción agrupa operaciones en unidad: commit acepta cambios; rollback abandona cambios no confirmados. ACID: atomicidad (todo o nada), consistencia (restricciones/invariantes válidos), aislamiento (reglas de visibilidad entre transacciones concurrentes), durabilidad (cambios confirmados sobreviven fallos según garantías de base/almacenamiento). Niveles de aislamiento y garantías difieren por motor; base en memoria no es durable tras salida del proceso. Evita transacciones abiertas durante red. Restricciones son protección adicional, no sustituyen reglas de negocio.

Ejemplo transfiere créditos enteros entre dos cuentas distintas. Verifica origen y saldo disponible en UPDATE condicional, comprueba filas afectadas, acredita destino y hace rollback si destino no existe. Saldo entero no negativo se restringe en base. Llamador suministra conexión dedicada con autocommit=False, sin escrituras pendientes ajenas, y confirma setup antes de llamar. Gestor de contexto de conexión Python 3.13 hace commit al salir con éxito y rollback ante excepción (o fallo de commit); no cierra conexión. Con autocommit=True no suministra esa frontera. No reutilices ejemplo como API de transacciones anidadas ni sistema financiero de producción.

## Índices y plan de consulta

Índice es estructura auxiliar que puede acelerar búsquedas, joins u ordenación cuando planificador lo elige. Cuesta almacenamiento y mantenimiento de escrituras; no toda columna merece índice. Orden de columnas de índice compuesto importa para consultas. Índice no garantiza ejecución más rápida. Inspecciona plan representativo (SQLite EXPLAIN QUERY PLAN) y mide; tablas pequeñas pueden recorrerse legítimamente.

```sql
CREATE INDEX idx_accounts_name ON accounts(name);
EXPLAIN QUERY PLAN SELECT id FROM accounts WHERE name = 'A';
```

No exijas texto exacto del plan entre versiones o distribuciones de datos.

## Seguridad SQL

Enlaza valores con parámetros, no concatenación o f-strings. Placeholders no enlazan identificadores de tabla/columna; usa SQL fijo o mapeo allowlist a identificadores confiables. Privilegio mínimo y validación separada siguen necesarios. find_account enlaza cadena; entrada con comillas permanece dato, no sintaxis.

## Práctica

Transfiere 3 créditos de saldos 10 y 2; espera 7 y 5. Luego transfiere a destino inexistente y comprueba ambos sin cambio. Prueba saldo insuficiente, misma cuenta, cantidad inválida y búsqueda con comillas. Explica por qué rollback tras débito es esencial.

**Referencia rápida:** cambios atómicos; propiedad explícita de transacción; parametriza valores; mide índices; prueba fallos.

## Ejemplo ejecutable compartido

[credit_transfer.py](examples/credit_transfer.py)

`python technical-interview-preparation/20-transactions-indexes-and-sql-safety/examples/credit_transfer.py`

## Referencias oficiales

- [docs.python.org/3.13/library/sqlite3.html](https://docs.python.org/3.13/library/sqlite3.html)
- [www.sqlite.org/lang_transaction.html](https://www.sqlite.org/lang_transaction.html)
- [www.sqlite.org/queryplanner.html](https://www.sqlite.org/queryplanner.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../19-joins-aggregations-and-data-relationships/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../21-software-engineering-and-technical-decisions/README.es.md)
<!-- /chapter-navigation:bottom -->
