# Joins, agregaciones y relaciones de datos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../18-relational-databases-and-sql/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../20-transactions-indexes-and-sql-safety/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [technical-interview-preparation/18-relational-databases-and-sql](../../technical-interview-preparation/18-relational-databases-and-sql/README.es.md)

## Relaciones y cardinalidad de joins

Uno-a-muchos: grupo tiene varias tareas, cada tarea pertenece a un grupo. Clave foránea impide referencias huérfanas cuando se aplica la restricción. Muchos-a-muchos usa tabla asociativa (p. ej. matrícula con learner_id y lesson_id como clave primaria compuesta). Uno-a-uno puede usar clave foránea única. Normalización separa hechos repetidos para reducir anomalías de actualización; desnormalización es compromiso deliberado, no solución predeterminada de rendimiento. En SQLite activa foreign_keys por conexión antes de cualquier transacción y verifica.

INNER JOIN conserva filas coincidentes. LEFT JOIN conserva toda fila izquierda y rellena columnas derechas sin coincidencia con NULL. Más de un hijo coincidente produce más de una fila; unir múltiples relaciones uno-a-muchos puede multiplicar conteos. Agrupa a granularidad correcta o preagrega. Ejemplo cuenta tareas completadas de todo grupo, incluso sin tareas o sin completadas.

```sql
SELECT groups.name, COUNT(tasks.id)
FROM groups LEFT JOIN tasks
    ON groups.id = tasks.group_id AND tasks.done = 1
GROUP BY groups.id, groups.name
ORDER BY groups.name, groups.id;
```

Filtro en ON limita coincidencias preservando filas izquierdas; tasks.done = 1 en WHERE elimina filas extendidas con NULL. COUNT(*) cuenta filas incluyendo fila extendida con NULL; COUNT(columna) excluye NULL. Usa ID no nulo del hijo aquí.

## Agregaciones

SUM suma valores no nulos, AVG calcula media, MIN/MAX encuentran extremos; COUNT cuenta como arriba. Entrada vacía puede resultar NULL en SUM/AVG; decide si COALESCE(..., 0) corresponde al significado de negocio. WHERE filtra filas antes de agrupar; HAVING filtra grupos después de agregar (p. ej. HAVING COUNT(tasks.id) >= 2). GROUP BY identificador estable, no solo nombre de visualización no único. Resultados no tienen orden garantizado sin ORDER BY.

## Práctica

Crea tres grupos: dos tareas completadas para A, solo incompletas para B y ninguna para C. Espera A=2, B=0, C=0. Mueve filtro a WHERE y observa grupos ausentes en tu copia. Prueba tarea referenciando grupo inexistente y explica importancia de la restricción.

**Referencia rápida:** join por claves; elige cardinalidad; filtra en etapa correcta; cuenta hijos no nulos.

## Ejemplo ejecutable compartido

[group_progress.py](examples/group_progress.py)

`python technical-interview-preparation/19-joins-aggregations-and-data-relationships/examples/group_progress.py`

## Referencias oficiales

- [www.sqlite.org/lang_select.html](https://www.sqlite.org/lang_select.html)
- [www.sqlite.org/lang_aggfunc.html](https://www.sqlite.org/lang_aggfunc.html)
- [www.sqlite.org/foreignkeys.html](https://www.sqlite.org/foreignkeys.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../18-relational-databases-and-sql/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../20-transactions-indexes-and-sql-safety/README.es.md)
<!-- /chapter-navigation:bottom -->
