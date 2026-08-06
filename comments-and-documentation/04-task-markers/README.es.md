<div align="center">

# Marcadores de Tareas y Seguimiento Técnico

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver al índice de la sección](../README.es.md) · [← Capítulo anterior: Nombres significativos](../03-meaningful-names/README.es.md)

Los marcadores de tareas son etiquetas breves dentro de comentarios que llaman la atención sobre trabajos, restricciones, riesgos o decisiones temporales. Pueden hacer visible el trabajo pendiente, pero los marcadores vagos o abandonados se convierten rápidamente en parte del decorado.

> **Principio rector:** Un marcador debe indicar al siguiente mantenedor qué debe ocurrir, por qué importa y cómo saber cuándo puede eliminarse.

## Información del capítulo

| Elemento | Detalles |
|---|---|
| Nivel | Principiante a intermedio |
| Requisitos previos | Se recomienda el capítulo de comentarios; la familiaridad con issues y control de versiones resulta útil |
| Tiempo estimado de estudio | 45 a 65 minutos |
| Conceptos principales | `TODO`, `FIXME`, `NOTE`, `HACK`, `XXX`, referencias de issues, condiciones de eliminación, búsqueda, revisión, marcadores obsoletos |

## Objetivos de aprendizaje

Al terminar este capítulo, deberías poder:

- explicar que los marcadores de tareas son convenciones del proyecto, no sintaxis de Python;
- diferenciar trabajo futuro, defectos conocidos, notas de contexto y soluciones temporales;
- escribir marcadores que incluyan una acción, razón, referencia o condición de eliminación;
- decidir cuándo una issue debe reemplazar o acompañar un marcador en el código fuente;
- evitar esconder pruebas fallidas, problemas de seguridad o incidentes de producción detrás de comentarios;
- buscar y revisar marcadores de forma coherente;
- reconocer marcadores obsoletos, vagos, privados o engañosos;
- definir una convención pequeña que herramientas y colaboradores puedan seguir.

## 1. Qué son los marcadores de tareas

Python trata un marcador como un comentario común. `TODO`, `FIXME` y palabras similares no tienen un significado especial para el intérprete.

```python
# TODO(#128): Remove the compatibility branch after every client uses API v2.
```

El valor proviene de una convención compartida. Editores, herramientas de búsqueda, sistemas de revisión de código y colaboradores pueden reconocer la etiqueta y dirigir atención hacia ella.

Un marcador resulta útil cuando la ubicación en el código importa. No debe sustituir la planificación, las pruebas, la respuesta a incidentes ni un gestor de issues.

## 2. Vocabulario habitual de los marcadores

Los proyectos utilizan estas etiquetas de maneras distintas, por lo que la convención del repositorio es la fuente de verdad.

| Marcador | Significado habitual | Intención de ejemplo |
|---|---|---|
| `TODO` | mejora planificada o trabajo incompleto | añadir una función cuando una dependencia esté preparada |
| `FIXME` | comportamiento conocido como incorrecto o inseguro | corregir un defecto antes de una versión |
| `NOTE` | contexto importante, no necesariamente trabajo pendiente | explicar una representación o restricción externa |
| `HACK` | solución alternativa deliberada con una razón | admitir temporalmente un formato heredado |
| `XXX` | pregunta o riesgo que requiere atención especial | solicitar revisión de una suposición incierta |

```python
# FIXME(#241): Reject duplicate invoice numbers before saving the batch.
```

```python
# NOTE: Amounts in this module are stored in cents.
```

```python
# HACK(#305): Keep the legacy padding until the old export format is retired.
```

```python
# XXX: Review this concurrency assumption before enabling parallel workers.
```

Estos significados son convenciones, no leyes universales. Un proyecto puede prohibir `XXX`, preferir `BUG` o utilizar otro formato de referencia.

## 3. La convención utilizada en esta guía

Este proyecto recomienda la siguiente forma:

```text
# MARCADOR(referencia): Acción clara o contexto importante.
# Continuación opcional que explica la razón o la condición de eliminación.
```

La referencia es opcional para una `NOTE` puramente explicativa, pero los marcadores de trabajo normalmente deberían apuntar a un elemento duradero, como una issue.

Ejemplos recomendados:

```python
# TODO(#128): Replace the temporary parser after escaped fields are supported.
# FIXME(#241): Preserve leading zeroes in account codes.
# NOTE: Amounts are represented in cents.
# HACK(#305): Keep legacy padding until the old export format is retired.
```

Utiliza etiquetas en mayúsculas para que las búsquedas sean previsibles. Escribe una frase específica y coloca el marcador inmediatamente encima del código relacionado.

## 4. Haz que el marcador sea accionable

Un marcador débil registra frustración, pero no define una tarea:

```python
# TODO: improve this
```

Un marcador útil responde a varias preguntas:

1. ¿Qué debe cambiar?
2. ¿Por qué el cambio no se realiza ahora?
3. ¿Qué issue o decisión sigue el trabajo?
4. ¿Qué condición permite eliminar el marcador?
5. ¿Existe una versión, plazo o dependencia que cambie la urgencia?

```python
# TODO(#128): Replace the temporary CSV parser after the vendor publishes
# escaped-field support. Remove this branch when issue #128 is closed.
```

No todos los marcadores necesitan todos los campos. Cuanto mayor sea el coste o el riesgo del trabajo pendiente, más contexto merece.

## 5. Prefiere referencias duraderas a la propiedad personal

El nombre de una persona puede quedar obsoleto cuando cambian los roles. Una issue, ticket o decisión documentada es más fácil de seguir.

Débil:

```python
# TODO(Ramon): revisit later
```

Más sólido:

```python
# TODO(#128): Add pagination after the API contract defines the cursor format.
```

La responsabilidad puede seguir definida en el gestor de issues. El comentario en el código debe continuar siendo útil aunque el autor original no esté disponible.

Evita direcciones de correo, enlaces a conversaciones privadas, tickets inaccesibles o información que identifique clientes en repositorios públicos.

## 6. `TODO`: trabajo planificado, no posibilidades ilimitadas

Utiliza `TODO` para una mejora concreta que se aplaza de manera intencionada.

Los buenos usos incluyen:

- una dependencia todavía no ha publicado la API necesaria;
- una migración está en curso;
- una optimización no crítica tiene un criterio de aceptación registrado;
- una rama temporal debe eliminarse después de un despliegue.

No añadas un `TODO` para cada función imaginable. Las posibilidades sin prioridad pertenecen a notas de planificación, discusiones o issues.

Un `TODO` sin referencia puede ser aceptable en un ejercicio pequeño, pero el código de producción se beneficia de un seguimiento duradero.

## 7. `FIXME`: un defecto conocido requiere un tratamiento más fuerte

`FIXME` señala que el comportamiento es conocido como incorrecto, engañoso, incompleto o inseguro.

```python
# FIXME(#241): Preserve leading zeroes in account codes.
```

Un `FIXME` no neutraliza el defecto. Según la gravedad, el código también puede necesitar:

- una prueba de regresión o actualmente fallida;
- una issue con prioridad e impacto;
- un bloqueo de versión;
- un feature flag;
- una alerta o incidente;
- retirada inmediata de producción.

No utilices un comentario para silenciar evidencias:

```python
# FIXME: the test is failing, so skip it
```

Una prueba omitida debe explicar la razón registrada, la condición esperada de recuperación y el riesgo. Los defectos críticos no deberían esperar educadamente dentro de un comentario.

## 8. `NOTE`: contexto en lugar de trabajo sin terminar

Una `NOTE` conserva información que un lector futuro podría pasar por alto.

```python
# NOTE: The upstream service returns dates in UTC.
created_at = parse_utc_timestamp(payload["created_at"])
```

Utilízala para contratos externos, unidades, reglas de compatibilidad o decisiones que no sean evidentes en el código.

No etiquetes contexto como tarea:

```python
# TODO: Dates come from the upstream service in UTC.
```

Cuando no se requiere ninguna acción, `NOTE` comunica la intención con más precisión que `TODO`.

Un comentario explicativo normal puede ser más claro cuando la etiqueta `NOTE` no aporta valor para búsqueda o revisión.

## 9. `HACK`: documenta la solución temporal y su salida

Una solución alternativa puede ser ingeniería responsable cuando una restricción externa impide la solución ideal. El peligro consiste en permitir que el código temporal se vuelva permanente sin explicación.

```python
# HACK(#305): Legacy exports pad account codes to eight characters.
# Remove this normalization after the pre-2024 export format is retired.
account_code = raw_account_code.lstrip("0")
```

Un `HACK` útil indica:

- qué restricción obligó a utilizar la solución;
- qué comportamiento depende de ella;
- la referencia de seguimiento;
- la condición de eliminación;
- cualquier riesgo que introduzca.

Evita:

```python
# HACK: weird fix
account_code = raw_account_code.lstrip("0")
```

`HACK` no es permiso para escribir código descuidado. La implementación todavía debe estar probada, limitada y ser comprensible.

## 10. `XXX` y marcadores personalizados

`XXX` suele significar “esto merece una atención poco habitual”, pero su significado varía mucho.

```python
# XXX(#411): Confirm whether this cache may be shared between tenants.
```

Utilízalo solamente cuando el proyecto defina su interpretación. De lo contrario, elige algo más preciso, como `FIXME`, `SECURITY`, `PERF` o `DEPRECATED`.

Los marcadores personalizados pueden ser útiles cuando corresponden a un proceso real de revisión. Demasiadas etiquetas crean un dialecto privado que las herramientas y los colaboradores no pueden predecir.

## 11. Los marcadores y los gestores de issues resuelven problemas distintos

Un marcador en el código responde:

> ¿En qué punto del código se aplica esta preocupación?

Una issue responde:

> ¿Cómo se prioriza, discute, asigna, prueba y completa el trabajo?

Para una tarea pequeña y local, un marcador puede ser suficiente. Para trabajos que involucran varios archivos, equipos, versiones, riesgos o decisiones, crea una issue y vincula el marcador con ella.

Cierra el ciclo:

1. actualiza o cierra la issue;
2. elimina o revisa el marcador;
3. actualiza pruebas y documentación;
4. comprueba que no queden referencias obsoletas.

## 12. Las fechas son contexto complementario, no una estrategia de salida

Una fecha puede ayudar a explicar el momento, pero “eliminar después” y “revisar el próximo mes” son condiciones débiles.

Prefiere un evento observable:

- después de que todos los clientes migren a la API v2;
- cuando se cierre la issue `#128`;
- después de cambiar la versión mínima compatible de Python;
- cuando las pruebas de regresión cubran el reemplazo;
- antes de una versión con nombre.

Una condición de eliminación permite comprobar el marcador durante la revisión.

## 13. No coloques secretos ni datos sensibles en marcadores

Los comentarios quedan almacenados en el historial de Git y pueden seguir siendo recuperables después de eliminarlos.

Nunca incluyas:

- contraseñas, tokens, claves de API o credenciales;
- nombres de clientes o identificadores privados;
- detalles confidenciales de incidentes;
- direcciones internas que no deberían ser públicas;
- información personal de contacto.

Incorrecto:

```python
# SECURITY: Temporary token for production: abc123
```

Utiliza el proceso privado de seguridad o incidentes del proyecto. Rotar una credencial expuesta es necesario aunque el comentario se elimine inmediatamente.

## 14. Mantén los marcadores cerca y con un alcance reducido

Coloca el marcador justo encima del bloque relevante más pequeño.

```python
# TODO(#128): Replace the temporary parser.
```

Evita un marcador al comienzo de un módulo grande cuando solamente una rama está afectada. Un marcador distante puede interpretarse mal después de una refactorización.

Cuando la preocupación abarque varios módulos, el gestor de issues debe conservar la explicación general mientras los marcadores locales identifican los puntos exactos del código.

## 15. Busca y revisa marcadores

Una búsqueda sencilla en el repositorio puede revelar trabajo acumulado:

```bash
rg -n "#\s*(TODO|FIXME|NOTE|HACK|XXX)\b" .
```

Los editores y la búsqueda de código de GitHub también pueden encontrar etiquetas. Mantén las etiquetas y la puntuación coherentes para que las herramientas no pierdan variantes.

Para un análisis que comprenda la sintaxis de Python, utiliza el módulo `tokenize` de la biblioteca estándar. Distingue los comentarios reales del texto parecido a un marcador dentro de strings.

```python
from io import StringIO
import tokenize


source = '''
message = "# TODO: this is text, not a comment"
# TODO(#128): Replace the temporary parser.
'''

for token in tokenize.generate_tokens(StringIO(source).readline):
    if token.type == tokenize.COMMENT:
        print(token.string)
```

El ejemplo de este capítulo muestra un pequeño escáner para una convención sencilla. Es educativo, no reemplaza un linter maduro ni un flujo de gestión de issues.

## 16. La coherencia permite automatización

Un formato estable permite:

- resaltado en el editor;
- informes del repositorio;
- reglas de CI para marcadores prohibidos;
- validación de referencias de issues;
- comprobaciones de versiones;
- paneles de deuda técnica.

Coherente:

```python
# TODO(#128): Replace the temporary parser after escaped fields are supported.
# FIXME(#241): Preserve leading zeroes in account codes.
# NOTE: Amounts are represented in cents.
# HACK(#305): Keep legacy padding until the old export format is retired.
```

Más difícil de buscar de forma fiable:

```python
# TODO-128 replace parser
# todo: maybe later
# FixMe(issue 241): zeros
```

La automatización debe apoyar el criterio, no fomentar números de issues sin significado ni comentarios escritos únicamente para cumplir un patrón.

## 17. Ejemplos de este repositorio

| Archivo | Objetivo |
|---|---|
| [`actionable_markers.py`](examples/actionable_markers.py) | Muestra marcadores con referencias, contexto y condición de eliminación |
| [`temporary_workaround.py`](examples/temporary_workaround.py) | Documenta una solución limitada para un formato heredado ficticio |
| [`scan_markers.py`](examples/scan_markers.py) | Utiliza `tokenize` para encontrar marcadores en comentarios reales de Python |

Ejecuta un ejemplo desde la raíz del repositorio:

```bash
python comments-and-documentation/04-task-markers/examples/actionable_markers.py
```

En sistemas donde el comando se llama `python3`:

```bash
python3 comments-and-documentation/04-task-markers/examples/actionable_markers.py
```

## 18. Ejemplo práctico de refactorización

Antes:

```python
def load_report(file_path):
    # TODO: make this better
    return file_path.read_text()
```

Después:

```python
def load_report(file_path):
    # TODO(#512): Stream files larger than 50 MB to avoid loading them at once.
    # Remove this marker after the streaming reader is covered by regression tests.
    return file_path.read_text()
```

El marcador mejorado identifica la limitación, el impacto, la issue y la condición de finalización. El código todavía puede requerir un rediseño inmediato si el comportamiento actual resulta inseguro para las entradas compatibles.

## 19. Errores comunes

### Escribir un marcador sin acción

“Mejorar esto” no define cuándo el trabajo estará terminado.

### Utilizar `TODO` para un defecto conocido

Un defecto puede requerir `FIXME`, una prueba y seguimiento urgente.

### Tratar `NOTE` como deuda técnica

Una nota puede permanecer para siempre porque documenta una restricción estable.

### Crear un marcador en lugar de una issue

El trabajo entre equipos o crítico para una versión necesita priorización fuera del código fuente.

### Mantener la referencia a una issue cerrada

Cuando el trabajo se completa, elimina o actualiza el marcador en el código.

### Registrar solamente una fecha o el nombre de una persona

Las fechas y los responsables cambian. Prefiere referencias duraderas y condiciones de salida observables.

### Ocultar riesgo detrás de `HACK`

Una solución alternativa todavía necesita pruebas, límites y revisión.

### Incluir información privada

El historial de Git no es un cuaderno privado.

### Reformatear código no relacionado al añadir marcadores

Mantén el pull request enfocado para que los revisores puedan evaluar el cambio real.

## 20. Ejercicio

Reescribe estos marcadores vagos o incompletos usando la convención recomendada en el capítulo:

```python
# TODO: improve parser
```

```python
# TODO(Ramon): fix leading zeroes later
```

```python
# TODO: rates are fractions
```

```python
# HACK: temporary workaround
```

```python
# XXX: check tenant isolation
```

Para cada marcador, decide:

1. ¿La etiqueta es correcta?
2. ¿Hace falta una referencia de issue?
3. ¿La acción está clara?
4. ¿Se documentó la razón o el riesgo?
5. ¿Existe una condición observable de eliminación?
6. ¿La preocupación debería bloquear la versión en lugar de permanecer como comentario?

Después, busca marcadores en un pequeño proyecto de práctica y clasifica cada uno como activo, obsoleto, resuelto o innecesario.

## 21. Lista de revisión

Antes de aceptar un marcador, comprueba:

- [ ] la etiqueta coincide con el significado;
- [ ] la acción o el contexto son específicos;
- [ ] el marcador está junto al código relevante;
- [ ] el trabajo registrado incluye una referencia duradera;
- [ ] el trabajo arriesgado incluye impacto y urgencia;
- [ ] el trabajo temporal incluye una condición de eliminación;
- [ ] no aparecen datos secretos, personales ni confidenciales;
- [ ] el marcador no sustituye una prueba o issue necesaria;
- [ ] la escritura y la puntuación siguen la convención del proyecto;
- [ ] el trabajo completado elimina o actualiza el marcador.

## 22. Resumen de consulta rápida

| Necesidad | Enfoque recomendado |
|---|---|
| Mejora concreta aplazada | `TODO(referencia): acción y condición` |
| Comportamiento conocido como incorrecto | `FIXME(referencia): defecto e impacto` más el seguimiento adecuado |
| Contexto importante y estable | `NOTE: contexto` o un comentario explicativo normal |
| Solución temporal | `HACK(referencia): razón y condición de eliminación` |
| Suposición incierta que requiere mucha atención | `XXX` definido por el proyecto o una etiqueta más precisa |
| Planificación entre archivos | gestor de issues, con marcadores locales donde la ubicación importa |
| Búsqueda | etiquetas coherentes, búsqueda del editor, `rg` o `tokenize` de Python |
| Trabajo completado | eliminar o actualizar tanto el marcador como su elemento de seguimiento |

Los marcadores de tareas son útiles cuando construyen un puente entre el código y un seguimiento responsable. Sin contexto y cierre, ese puente se convierte en andamiaje decorativo.
