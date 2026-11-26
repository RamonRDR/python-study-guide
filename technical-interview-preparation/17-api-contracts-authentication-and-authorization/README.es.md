# Contratos de API, autenticación y autorización

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../16-http-rest-and-backend-fundamentals/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../18-relational-databases-and-sql/README.es.md)
<!-- /chapter-navigation:top -->

## Requisitos previos

- [external-libraries/03-requests](../../external-libraries/03-requests/README.es.md)
- [standard-library/03-json](../../standard-library/03-json/README.es.md)
- [technical-interview-preparation/16-http-rest-and-backend-fundamentals](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.es.md)

## Validar la frontera

Contrato de API describe solicitudes, campos requeridos y opcionales, tipos, límites, respuestas, errores y compatibilidad. Parsing JSON no es validación. Rechaza entradas grandes antes de parsing cuando sea posible; valida forma y campos permitidos, tipos (booleanos no son enteros de negocio por defecto), longitudes y rangos. Campos desconocidos pueden rechazarse o ignorarse según contrato documentado, no persistirse silenciosamente. Devuelve errores consistentes sin filtrar stack traces. Añade campos de forma compatible cuando clientes permitan; versiona o migra cambios incompatibles.

Ejemplo valida objeto ya decodificado con exactamente un campo title, quita espacios externos y acepta 1–80 caracteres tras trim. No trata HTTP bruto, nombres JSON duplicados ni tamaño del cuerpo; corresponden a frontera de parsing/transporte.

## Autenticación frente a autorización

Autenticación establece identidad verificada; autorización decide qué puede hacer en recurso específico. Usa bibliotecas/proveedores establecidos, HTTPS, firma verificada del token y comprobaciones de emisor/audiencia/expiración cuando correspondan. Nunca trates propietario indicado por cliente o token decodificado sin verificar como identidad. Almacena credenciales de forma segura, no las registres y aplica privilegio mínimo. Bearer token es credencial; posesión solo es significativa tras verificación. Ejemplo intencionalmente no emite ni valida tokens.

Autorización a nivel de objeto es necesaria en cada acceso protegido: login válido no basta para leer nota de otro propietario. Ejemplo recibe identidad confiable de capa anterior hipotética; None produce 401 con desafío Bearer, ID inexistente 404 y propietario diferente 403 sin contenido. 401 significa ausencia de credenciales válidas de autenticación; 403 significa rechazo de acceso. Algunos sistemas devuelven 404 para recursos prohibidos para no revelar existencia; elige y documenta política consistente. Este ejemplo revela existencia deliberadamente a autenticados vía 403 frente a 404 y no es frontera de seguridad de producción.

## Práctica

Prueba anónimo, propietario autorizado, otro propietario, recurso ausente y payloads inválidos. Explica por qué comprobar solo rol puede no imponer propiedad del objeto. Esboza dónde autenticación, búsqueda, autorización y serialización ocurrirían en servicio real. Añade prueba negativa antes de cambiar política.

**Referencia rápida:** parsea y valida; identidad verificada primero; autoriza acción y objeto; no confíes en afirmaciones del cliente.

## Ejemplo ejecutable compartido

[note_access.py](examples/note_access.py)

`python technical-interview-preparation/17-api-contracts-authentication-and-authorization/examples/note_access.py`

## Referencias oficiales

- [www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html)
- [api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)
- [devguide.owasp.org/en/07-training-education/07-api-top-ten/](https://devguide.owasp.org/en/07-training-education/07-api-top-ten/)

<!-- chapter-navigation:bottom -->
[← Anterior](../16-http-rest-and-backend-fundamentals/README.es.md) · [Índice del módulo](../README.es.md) · [Siguiente →](../18-relational-databases-and-sql/README.es.md)
<!-- /chapter-navigation:bottom -->
