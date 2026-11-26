# HTTP, REST y fundamentos de backend

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../15-exceptions-testing-and-debugging-review/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../17-api-contracts-authentication-and-authorization/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [external-libraries/03-requests](../../external-libraries/03-requests/README.es.md)
- [technical-interview-preparation/15-exceptions-testing-and-debugging-review](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.es.md)

## Contratos cliente, servidor y recurso

HTTP es protocolo solicitud/respuesta: método, destino, headers y contenido opcional describen solicitud; estado, headers y contenido opcional describen respuesta. Backend normalmente enruta, valida, autoriza, aplica reglas, persiste datos y devuelve representación. Endpoint es operación expuesta en interfaz. REST es estilo arquitectónico con restricciones incluyendo separación cliente/servidor, solicitudes stateless, cacheabilidad e interfaz uniforme; solo JSON sobre HTTP no establece REST. Solicitudes stateless llevan información necesaria para tratarlas; servidor aún puede almacenar datos de recursos.

| Método | Semántica pretendida | Seguro / idempotente |
| --- | --- | --- |
| GET | Recuperar representación | Sí / sí |
| POST | Procesamiento específico, a menudo creación | No / no garantizado |
| PUT | Crear o sustituir estado del destino | No / sí |
| PATCH | Aplicar cambio parcial | No / no garantizado |
| DELETE | Eliminar asociación del destino | No / sí |

Seguro significa cliente no solicitar cambio de estado; idempotente se refiere al efecto pretendido en servidor, no respuestas idénticas ni ausencia de logs. Reintentar puede duplicar efecto de POST. Para escrituras, exige contrato explícito de reintento (como clave de idempotencia persistida), intentos limitados y respeto a Retry-After. Define timeouts en fronteras de red.

## Diseño de respuesta

200 éxito; 201 creado (a menudo Location); 204 éxito sin contenido; 400 solicitud malformada o inválida; 404 recurso ausente; 405 método no soportado para destino (incluye Allow); 409 conflicto con estado actual; 429 límite de tasa; 500 fallo inesperado del servidor. 401 y 403 en siguiente lección. Respuesta de error debe describir contrato estable sin secretos internos. Paginación limita tamaño; define orden estable, semántica de página/cursor y fin de resultados.

Ejemplo compartido es simulación pura de enrutamiento para endpoint didáctico solo GET. Devuelve estado, headers y objetos Python que representan contenido JSON, no bytes HTTP reales. Framework real debe gestionar serialización, detalles de protocolo, HEAD/OPTIONS según soporte y seguridad. Prueba ruta ausente, método no soportado y datos de respuesta independientes.

## Práctica

Esboza recurso /lessons/42, elige método de lectura y sustitución y declara estados esperados. Explica por qué repetir DELETE puede devolver estado diferente manteniendo idempotencia en efecto pretendido. Prueba enrutamiento sin red.

**Referencia rápida:** método expresa intención; estado expresa resultado; reintentos dependen de semántica; contrato antes de framework.

## Ejemplo ejecutable compartido

[route_catalog.py](examples/route_catalog.py)

`python technical-interview-preparation/16-http-rest-and-backend-fundamentals/examples/route_catalog.py`

## Referencias oficiales

- [www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html)

<!-- chapter-navigation:bottom -->
[← Anterior](../15-exceptions-testing-and-debugging-review/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../17-api-contracts-authentication-and-authorization/README.es.md)
<!-- /chapter-navigation:bottom -->
