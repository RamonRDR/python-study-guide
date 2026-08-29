<div align="center">

# Consumiendo APIs HTTP con `requests`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Volver a Bibliotecas Externas](../README.es.md) · [← Anterior: `openpyxl`](../02-openpyxl/README.es.md)

Los archivos locales son solo un tipo de frontera. Los programas Python modernos también intercambian datos con servicios web, APIs internas, plataformas SaaS, servidores de autenticación, endpoints de almacenamiento y otros sistemas mediante HTTP. El paquete `requests` ofrece a Python un cliente HTTP compacto y legible, manteniendo visibles los conceptos de protocolo necesarios para integraciones confiables.

Este capítulo apunta a la serie **Requests 2.34.x** y fue investigado contra la documentación y los metadatos actuales de **Requests 2.34.2**. Requests 2.34.2 requiere Python 3.10 o superior; este repositorio valida los ejemplos en Python 3.13.

**Tiempo estimado de estudio:** 270–360 minutos.

## Objetivos de aprendizaje

Al finalizar este capítulo, deberías poder:

- explicar el modelo HTTP de solicitud/respuesta sin tratar una llamada de API como una función mágica;
- ejecutar GET, POST, PUT, PATCH y DELETE de forma intencional;
- enviar parámetros de query, headers, datos de formulario, cuerpos JSON, archivos y datos de autenticación;
- distinguir éxito de transporte, éxito HTTP y validez del payload;
- configurar timeouts de conexión/lectura y entender lo que no garantizan;
- manejar excepciones de Requests sin ocultar contexto útil;
- usar `Session` para reutilización de conexiones, cookies y valores predeterminados compartidos;
- comprender redirects, verificación TLS, bundles de CA, proxies y configuración de entorno;
- procesar respuestas grandes mediante streaming y cerrar recursos de forma determinista;
- añadir retries solo cuando una operación pueda repetirse con seguridad;
- proteger credenciales y evitar registrar secretos;
- validar contratos de respuesta en vez de confiar en JSON arbitrario;
- construir pruebas HTTP deterministas sin depender de un servicio público de internet.

## 1. Por qué existe `requests`

La biblioteca estándar de Python puede hablar HTTP, pero `requests` ofrece una interfaz de mayor nivel para tareas habituales de cliente: URLs, parámetros de query, headers, cookies, autenticación, cuerpos de solicitud, verificación TLS, Sessions, streaming y excepciones.

La comodidad es valiosa, pero la red sigue siendo una frontera de sistema distribuido. Una API legible no elimina latencia, fallas parciales, reglas de autenticación, errores del servidor, retries ni decisiones de seguridad.

## 2. Piensa en solicitudes y respuestas

Un cliente envía una solicitud HTTP que contiene alguna combinación de:

```text
method + URL + headers + optional body
```

El servidor devuelve una respuesta HTTP que contiene:

```text
status code + headers + body
```

Tu código Python debe razonar sobre ambas mitades.

## 3. Las bibliotecas externas necesitan un contrato de versión

Este repositorio declara las dependencias de la Fase 9 en `requirements-external.txt`.

Para este capítulo el contrato es:

```text
requests >= 2.34 and < 2.35
```

La serie 2.34 también introdujo tipado inline dentro de Requests, de modo que los type checkers actuales pueden consumir los tipos de la API pública sin depender de un paquete separado de stubs.

## 4. Instala el conjunto de dependencias del repositorio

Crea y activa un entorno virtual y luego instala:

```bash
python -m pip install -r requirements-external.txt
```

Para experimentación aislada, `python -m pip install requests` es válido, pero un proyecto debe registrar el rango de dependencias compatible.

## 5. Importa el paquete

El import convencional es:

```python
import requests
```

El módulo de nivel superior expone funciones cómodas como `get()`, `post()` y `delete()`, además de clases como `Session` y tipos de excepción bajo `requests.exceptions`.

## 6. Una URL forma parte del contrato de entrada

Una URL HTTP normalmente contiene:

```text
scheme://host:port/path?query#fragment
```

Para un cliente HTTP, scheme, host, port, path y parámetros de query afectan la solicitud real. Los fragments normalmente se interpretan del lado cliente y no se envían como objetivo de la solicitud HTTP.

No concatenes fragmentos de URL no confiables de forma descuidada.

## 7. Empieza con una solicitud GET

Un GET básico se ve así:

```python
import requests


response = requests.get("https://example.com/api/items", timeout=(3, 10))
print(response.status_code)
```

Este snippet es ilustrativo porque depende de un endpoint externo. Los ejemplos ejecutables publicados más adelante usan un servidor local de prueba.

## 8. Los status codes comunican resultados HTTP

Clases comunes:

```text
1xx -> informational
2xx -> successful response
3xx -> redirection
4xx -> client-side request problem
5xx -> server-side failure
```

`200` no es el único resultado exitoso. Un POST puede devolver correctamente `201 Created`, y un DELETE puede devolver `204 No Content`.

## 9. Usa `raise_for_status()` cuando los códigos HTTP no exitosos sean fallas

```python
response = requests.get(url, timeout=(3, 10))
response.raise_for_status()
```

Para status HTTP no exitosos, `raise_for_status()` lanza `requests.HTTPError` y conserva la respuesta asociada a la excepción.

No descartes ese contexto al informar una falla.

## 10. Éxito de transporte no es éxito de aplicación

Un intercambio HTTP puede funcionar a nivel de red mientras el servidor devuelve `404`, `429` o `500`.

Del mismo modo, una respuesta `200` puede contener datos que violan tu contrato de negocio.

Un cliente robusto verifica más que “¿`requests.get()` devolvió algo?”.

## 11. `response.text` es texto decodificado

```python
text = response.text
```

Requests decodifica los bytes de respuesta según información de encoding y sus reglas de detección.

Usa texto cuando el cuerpo sea realmente textual y necesites un `str`.

## 12. `response.content` entrega bytes crudos

```python
payload = response.content
```

Usa bytes para archivos binarios, checksums, imágenes, artefactos comprimidos o cualquier formato donde decodificar a texto sería incorrecto.

## 13. Decodifica JSON con `response.json()`

```python
response = requests.get(url, timeout=(3, 10))
response.raise_for_status()
data = response.json()
```

`response.json()` analiza el cuerpo. No demuestra que el status HTTP haya sido exitoso.

## 14. JSON inválido tiene su propio modo de falla

Requests expone `requests.exceptions.JSONDecodeError` para errores de decodificación JSON.

```python
try:
    data = response.json()
except requests.exceptions.JSONDecodeError as exc:
    raise RuntimeError("API returned invalid JSON") from exc
```

Una respuesta `204 No Content`, una página HTML de error o JSON malformado pueden hacer fallar la decodificación.

## 15. La forma del JSON todavía debe validarse

Incluso JSON válido puede ser incorrecto para tu programa:

```python
if not isinstance(data, dict) or "items" not in data:
    raise ValueError("Unexpected API response shape")
```

El parsing responde “¿esto es JSON?”. La validación de contrato responde “¿es el JSON que espera nuestra aplicación?”.

## 16. Envía parámetros de query con `params`

No construyas query strings a mano cuando Requests puede codificarlos:

```python
response = requests.get(
    url,
    params={"status": "open", "limit": 20},
    timeout=(3, 10),
)
```

Requests maneja el encoding de query y expone la URL final mediante `response.url`.

## 17. Parámetros repetidos pueden usar secuencias

Algunas APIs esperan claves repetidas. Requests acepta valores secuenciales o una lista de tuplas de dos elementos.

```python
params = [("tag", "python"), ("tag", "http")]
response = requests.get(url, params=params, timeout=(3, 10))
```

Sigue el contrato documentado de la API objetivo.

## 18. Los headers de solicitud son metadatos

```python
headers = {
    "Accept": "application/json",
    "User-Agent": "study-client/1.0",
}
response = requests.get(url, headers=headers, timeout=(3, 10))
```

Los headers pueden comunicar preferencias de representación, autenticación, solicitudes condicionales, tracing y otros metadatos de protocolo.

## 19. No confundas headers de solicitud y respuesta

Los headers de solicitud son los que envía el cliente. Los headers de respuesta son los que devuelve el servidor.

```python
content_type = response.headers.get("Content-Type")
```

Los headers de respuesta de Requests se comportan como un mapping case-insensitive.

## 20. Usa un `User-Agent` descriptivo cuando corresponda

Muchas APIs valoran un identificador de cliente para operaciones y diagnóstico de soporte.

Evita fingir que eres un navegador no relacionado salvo que el contrato de integración lo exija explícitamente.

## 21. Envía datos de formulario con `data=`

Para datos estilo formulario:

```python
response = requests.post(
    url,
    data={"username": "demo", "mode": "compact"},
    timeout=(3, 10),
)
```

Requests codifica un mapping pasado mediante `data=` como datos de formulario.

## 22. Envía JSON con `json=`

Para APIs JSON, prefiere el parámetro dedicado:

```python
payload = {"name": "Nova", "active": True}
response = requests.post(url, json=payload, timeout=(3, 10))
response.raise_for_status()
```

`json=` serializa el valor y configura un content type JSON apropiado.

## 23. No serialices JSON manualmente sin una razón

Esto suele ser menos claro:

```python
import json

body = json.dumps(payload)
response = requests.post(
    url,
    data=body,
    headers={"Content-Type": "application/json"},
    timeout=(3, 10),
)
```

Usa `json=` salvo que necesites control preciso sobre los bytes serializados.

## 24. PUT y PATCH expresan contratos de actualización distintos

La especificación HTTP y la documentación de cada API determinan la semántica. Comúnmente:

```text
PUT   -> replace or set a representation at a target
PATCH -> partially modify a representation
```

No deduzcas el comportamiento del servidor únicamente por el nombre del método. Lee el contrato de la API.

## 25. DELETE puede tener éxito sin cuerpo

```python
response = requests.delete(url, timeout=(3, 10))
response.raise_for_status()
```

Un `204 No Content` exitoso no debe ir seguido por un `response.json()` incondicional.

## 26. La idempotencia importa antes de los retries

Una operación es idempotente cuando repetir la misma solicitud pretendida tiene el mismo efecto pretendido que ejecutarla una vez.

GET, HEAD, PUT y DELETE tienen semántica idempotente al nivel del método HTTP; POST en general no. El comportamiento de aplicación y las claves de idempotencia pueden agregar garantías adicionales.

## 27. Casi toda solicitud de producción necesita timeout

Requests **no** aplica timeout por defecto.

```python
response = requests.get(url, timeout=10)
```

Sin timeout explícito, un programa puede esperar indefinidamente actividad de red.

## 28. Separa timeouts de conexión y lectura cuando sea útil

Requests acepta una tupla:

```python
response = requests.get(url, timeout=(3, 15))
```

El primer valor es el connect timeout. El segundo es el read timeout.

Esto suele ser más claro en integraciones donde establecer la conexión y esperar bytes de respuesta tienen expectativas distintas.

## 29. Un timeout de Requests no es un deadline total de reloj

El comportamiento documentado se basa en inactividad del socket, no en una duración máxima garantizada para la descarga completa.

Una respuesta lenta que continúa enviando bytes puede durar más que el read timeout nominal.

Si un flujo necesita un deadline global rígido, diseña ese deadline por separado.

## 30. Requests tiene una jerarquía útil de excepciones

Las excepciones específicas de Requests heredan de `requests.exceptions.RequestException`.

Subclases importantes incluyen:

```text
HTTPError
ConnectionError
Timeout
TooManyRedirects
JSONDecodeError
SSLError
```

Captura de manera específica cuando exista comportamiento de recuperación diferente.

## 31. `Timeout` merece manejo explícito

```python
try:
    response = requests.get(url, timeout=(3, 10))
except requests.Timeout as exc:
    raise RuntimeError("Remote service timed out") from exc
```

Un timeout es distinto de un HTTP `500`: el cliente puede no saber si el servidor procesó la solicitud.

Esa incertidumbre es crucial antes de reintentar una escritura.

## 32. `ConnectionError` cubre fallas de conexión de red

Fallas de DNS, conexiones rechazadas y problemas de transporte relacionados pueden aparecer como `requests.ConnectionError`.

No conviertas esto en un resultado vacío y exitoso. Conserva la señal de falla o aplica una política de recuperación explícita.

## 33. `HTTPError` da acceso a la respuesta

```python
try:
    response.raise_for_status()
except requests.HTTPError as exc:
    status = exc.response.status_code
    raise RuntimeError(f"API returned HTTP {status}") from exc
```

Evita incluir cuerpos arbitrarios de respuesta en logs porque pueden contener secretos o datos personales.

## 34. Un límite superior con `RequestException` puede añadir contexto

En una frontera de aplicación, un wrapper puede agregar el nombre de la operación del servicio:

```python
try:
    response = requests.get(url, timeout=(3, 10))
    response.raise_for_status()
except requests.RequestException as exc:
    raise RuntimeError("Could not load catalog") from exc
```

No captures `Exception` solo para hacer desaparecer una falla de red.

## 35. Los redirects tienen historial

Requests sigue redirects en solicitudes GET comunes y expone respuestas previas mediante:

```python
for previous in response.history:
    print(previous.status_code, previous.url)
```

La URL final queda disponible en `response.url`.

## 36. Limita o desactiva redirects cuando el contrato lo requiera

```python
response = requests.get(
    url,
    allow_redirects=False,
    timeout=(3, 10),
)
```

Los redirects pueden importar para autenticación, auditoría, defensas SSRF y URLs firmadas.

## 37. La autenticación Basic tiene un helper dedicado

```python
from requests.auth import HTTPBasicAuth


response = requests.get(
    url,
    auth=HTTPBasicAuth("demo-user", "demo-password"),
    timeout=(3, 10),
)
```

Nunca codifiques credenciales reales en código fuente, ejemplos, commits o logs.

## 38. Los Bearer tokens normalmente son headers

```python
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers, timeout=(3, 10))
```

El token debe provenir de una fuente segura en runtime, como un secret manager o variable de entorno protegida, no de un archivo del repositorio.

## 39. Redacta secretos de la observabilidad

No registres valores completos de:

```text
Authorization
Proxy-Authorization
Cookie
Set-Cookie
API keys
signed URLs
client certificates or private keys
```

Un logging útil puede incluir método HTTP, host/path sanitizado, status code, tiempo transcurrido, número de retry e identificadores de correlación.

## 40. `Session` conserva estado entre solicitudes

```python
import requests


with requests.Session() as session:
    session.headers.update({"Accept": "application/json"})
    response = session.get(url, timeout=(3, 10))
```

Una Session puede conservar valores predeterminados y cookies entre llamadas.

## 41. Las Sessions también reutilizan conexiones

Requests Sessions usan connection pooling de urllib3. Varias llamadas al mismo host pueden reutilizar conexiones subyacentes en vez de establecer una conexión TCP/TLS nueva cada vez.

Esto puede reducir de manera importante el overhead en flujos repetidos de API.

## 42. Los defaults de Session pueden sobrescribirse por solicitud

Headers, autenticación, cookies, proxies y otros parámetros a nivel de Session son defaults convenientes, no globales inmutables.

Mantén la configuración compartida intencional para evitar heredar por accidente credenciales destinadas a otro servicio.

## 43. Cierra Sessions de forma determinista

Usa un context manager o llama `close()`:

```python
with requests.Session() as session:
    response = session.get(url, timeout=(3, 10))
    response.raise_for_status()
```

La propiedad de recursos debe ser visible en procesos de larga duración.

## 44. Las cookies pueden persistir en una Session

Un servidor puede configurar cookies en una respuesta y esperarlas en solicitudes posteriores. Una Session mantiene un cookie jar entre llamadas.

Para clientes de API, la autenticación explícita basada en tokens suele ser más fácil de razonar, pero los flujos basados en cookies todavía existen.

## 45. Las prepared requests exponen la solicitud exacta de salida

Requests puede construir un `PreparedRequest` antes de enviarlo:

```python
from requests import Request, Session


with Session() as session:
    request = Request("GET", url, headers={"X-Trace": "demo"})
    prepared = session.prepare_request(request)
    print(prepared.method, prepared.url)
```

Esto es útil para firma avanzada, inspección o mutación controlada de la solicitud.

## 46. Prefiere `Session.prepare_request()` cuando el estado de Session importa

Llamar `Request.prepare()` directamente no aplica automáticamente todo el estado a nivel de Session.

Si cookies, headers predeterminados o autenticación de Session forman parte del contrato, prepara la solicitud mediante esa Session.

## 47. Los flujos con prepared requests necesitan considerar el entorno

La documentación avanzada de Requests advierte que enviar manualmente una prepared request puede omitir configuraciones derivadas del entorno si no se combinan explícitamente.

Esto importa para settings como CA bundles y proxies.

La preparación avanzada de solicitudes debe ser deliberada, no el patrón predeterminado para llamadas normales.

## 48. La verificación de certificados HTTPS está habilitada por defecto

Requests verifica certificados TLS del servidor para conexiones HTTPS.

```python
response = requests.get("https://example.com", timeout=(3, 10))
```

Si falla la verificación del certificado, Requests lanza `SSLError` en vez de confiar silenciosamente en el peer.

## 49. `verify=False` desactiva una garantía importante de seguridad

```python
response = requests.get(url, verify=False, timeout=(3, 10))
```

Esto acepta certificados que pueden estar expirados, ser autofirmados o corresponder a otro hostname y puede permitir ataques man-in-the-middle.

No resuelvas un problema de certificado en producción desactivando globalmente la verificación.

## 50. PKI privada debe usar un CA bundle explícito

Requests permite que `verify` apunte a un CA bundle confiable:

```python
response = requests.get(
    url,
    verify="/path/to/company-ca-bundle.pem",
    timeout=(3, 10),
)
```

Requests también reconoce `REQUESTS_CA_BUNDLE`, con `CURL_CA_BUNDLE` como fallback en su comportamiento documentado de entorno.

## 51. Los certificados de cliente soportan flujos de mTLS

El parámetro `cert` puede apuntar a un certificado de cliente o a un par certificado/clave:

```python
response = requests.get(
    url,
    cert=("client.crt", "client.key"),
    timeout=(3, 10),
)
```

Los archivos de clave privada son secretos. Protégelos como credenciales.

## 52. Los proxies pueden provenir de argumentos o del entorno

Requests soporta configuración de proxy por solicitud y settings derivados del entorno.

```python
proxies = {"https": "http://proxy.example:8080"}
response = requests.get(url, proxies=proxies, timeout=(3, 10))
```

No coloques credenciales reales de proxy en el código fuente.

## 53. `Session.trust_env` controla la integración con el entorno

Las Sessions confían por defecto en configuración relevante del entorno, como proxies y fuentes de autenticación.

Si un cliente debe operar independientemente de la configuración ambiente del proceso, evalúa `session.trust_env` explícitamente y documenta las consecuencias.

## 54. Streaming evita cargar el cuerpo completo de inmediato

```python
with requests.get(url, stream=True, timeout=(3, 30)) as response:
    response.raise_for_status()
    for chunk in response.iter_content(chunk_size=64 * 1024):
        if chunk:
            process(chunk)
```

Streaming es útil para descargas grandes y procesamiento incremental.

## 55. Las respuestas en streaming deben consumirse o cerrarse

La reutilización de conexión depende de liberar la conexión subyacente.

Usar la respuesta como context manager hace explícito el límite de propiedad incluso si el procesamiento lanza una excepción.

## 56. `iter_content()` suele ser mejor que leer `raw` directamente

`iter_content()` coopera con el comportamiento de decodificación de Requests y con la iteración por chunks.

Elige el tamaño del chunk según el caso de uso en vez de asumir que cada chunk coincide con un mensaje lógico del servidor.

## 57. Streaming por líneas es útil para protocolos orientados a líneas

`response.iter_lines()` puede procesar una respuesta de streaming línea por línea.

Ten cuidado con líneas vacías de keep-alive, registros parciales y semántica de reconexión definida por la API concreta.

## 58. Escribe descargas grandes de forma segura

Para un artefacto importante, un patrón más seguro es:

```text
download to temporary path
-> verify status / size / checksum if available
-> flush and close
-> atomically move into final location
```

Esto evita que una descarga parcial se haga pasar por un archivo completo.

## 59. Los uploads multipart usan `files=`

```python
with open("report.txt", "rb") as file_handle:
    response = requests.post(
        url,
        files={"file": ("report.txt", file_handle, "text/plain")},
        timeout=(3, 30),
    )
```

El archivo debe abrirse en modo binario para un manejo predecible de bytes.

## 60. Requests no reintenta conexiones fallidas por defecto

El `HTTPAdapter` incorporado tiene cero retries de conexión por defecto.

Los retries son una política de aplicación, no algo que debas asumir que ocurrió automáticamente.

## 61. `HTTPAdapter` puede añadir una política de retry

Para comportamiento granular, la documentación de Requests usa la clase `Retry` de urllib3:

```python
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


retry_policy = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[429, 502, 503, 504],
    allowed_methods={"GET", "HEAD"},
)

with Session() as session:
    session.mount("https://", HTTPAdapter(max_retries=retry_policy))
    response = session.get(url, timeout=(3, 10))
```

La política de retry debe diseñarse junto al contrato de API, no copiarse a ciegas.

## 62. Nunca reintentes una escritura solo porque falló

Un timeout después de enviar un POST puede significar:

```text
client does not know whether server committed the operation
```

Repetirlo ciegamente puede crear duplicados.

Usa idempotency keys, identificadores de operación, métodos seguros o lógica de reconciliación cuando el servicio lo permita.

## 63. Respeta `Retry-After` y los contratos de rate limit

Una respuesta `429 Too Many Requests` normalmente indica que el cliente debe bajar el ritmo.

Los headers exactos y el comportamiento de retry dependen de la API. Lee el contrato del servicio y evita loops cerrados que amplifiquen una caída.

## 64. Backoff reduce tormentas de retry

Los retries normalmente deben esperar entre intentos. Backoff exponencial y jitter ayudan a que muchos clientes no sincronicen sus reintentos contra el mismo servicio en recuperación.

La política exacta pertenece al diseño de confiabilidad del sistema.

## 65. Los response hooks pueden añadir comportamiento transversal

Requests soporta hooks de `response`:

```python
def record_status(response: requests.Response, *args: object, **kwargs: object) -> None:
    print(response.status_code)


response = requests.get(
    url,
    hooks={"response": record_status},
    timeout=(3, 10),
)
```

Los hooks deben permanecer pequeños y manejar sus propias suposiciones y fallas.

## 66. La paginación es un contrato de API, no una función de Requests

Las APIs pueden paginar mediante:

```text
page/limit query parameters
cursor tokens
Link headers
next URLs in JSON
```

Tu cliente debe detenerse en la condición terminal documentada por el servicio y protegerse de loops infinitos accidentales.

## 67. Los Link headers ya se analizan

Cuando una respuesta contiene headers estándar de Web Linking, Requests expone los links analizados mediante:

```python
next_link = response.links.get("next")
```

No asumas que todas las APIs usan Link headers para paginación.

## 68. Valida el media type de la respuesta cuando sea importante

Si un endpoint promete JSON, inspecciona el contrato cuando corresponda:

```python
content_type = response.headers.get("Content-Type", "")
if "application/json" not in content_type.lower():
    raise ValueError("Expected a JSON response")
```

Sé lo suficientemente preciso para la API integrada; los media types pueden incluir parámetros o formas vendor-specific `+json`.

## 69. Registrar llamadas HTTP exige redactar datos sensibles

Un registro estructurado útil puede contener:

```text
service name
operation
HTTP method
sanitized route
status code
elapsed time
retry attempt
correlation ID
```

Evita registrar URLs completas cuando los parámetros de query puedan incluir secretos o datos personales.

## 70. Las pruebas deterministas no deben depender de internet pública

Un endpoint público puede ser lento, estar caído, limitado por rate limit, bloqueado geográficamente o cambiar sin relación con tu repositorio.

Los ejemplos ejecutables de este capítulo inician un `ThreadingHTTPServer` local en `127.0.0.1`, ejercitan Requests contra él y luego lo apagan. Así se prueba HTTP real sin dependencia externa de red.

## 71. Ejemplo práctico: GET con parámetros de query

[`examples/get_with_query.py`](examples/get_with_query.py) envía un GET HTTP local real, deja que Requests codifique parámetros de query, verifica el status, decodifica JSON e imprime el contrato de query analizado.

Salida esperada:

```text
status: 200
path: /items
query: {'status': ['open'], 'limit': ['2']}
```

## 72. Ejemplo práctico: POST JSON

[`examples/post_json.py`](examples/post_json.py) verifica que `json=` envía un payload JSON con el content type esperado.

Salida esperada:

```text
status: 201
created: {'name': 'Nova', 'active': True}
content-type: application/json
```

## 73. Ejemplo práctico: defaults de Session

[`examples/session_defaults.py`](examples/session_defaults.py) usa una Session para aplicar headers compartidos y confirma que el servidor local los recibió.

Salida esperada:

```text
client: python-study-guide
auth-scheme: Bearer
```

El token es ficticio y existe solo dentro del proceso local del ejemplo.

## 74. Ejemplo práctico: errores HTTP visibles

[`examples/http_error_handling.py`](examples/http_error_handling.py) recibe `404` intencionalmente y demuestra que `raise_for_status()` conserva la respuesta en `HTTPError`.

Salida esperada:

```text
caught: HTTPError
status: 404
```

## 75. Ejemplo práctico: descarga por streaming

[`examples/stream_download.py`](examples/stream_download.py) transmite bytes locales deterministas con `iter_content()` y cierra la respuesta mediante context manager.

Salida esperada:

```text
bytes: 12
content: chunked-data
```

## 76. Errores comunes

Evita estos patrones:

| Error | Por qué es riesgoso | Mejor enfoque |
|---|---|---|
| omitir `timeout` | la solicitud puede esperar indefinidamente | definir expectativas de conexión/lectura |
| llamar `json()` y asumir éxito | respuestas de error pueden contener JSON válido | verificar status HTTP y contrato del payload |
| usar `verify=False` en producción | desactiva verificación de identidad TLS | reparar la cadena de confianza o proporcionar CA bundle |
| reintentar cualquier excepción | puede duplicar escrituras o empeorar caídas | reintentar solo fallas seguras y clasificadas |
| crear una Session nueva para cada llamada | pierde reutilización de conexión | mantener Session durante la vida lógica del cliente |
| registrar Authorization | filtra credenciales | redactar secretos |
| confiar en forma JSON arbitraria | drift de schema se vuelve bug oculto | validar campos/tipos requeridos |
| probar contra API pública de demostración | CI se vuelve externamente frágil | usar servidor local o test double controlado |

## 77. Tabla de decisión

| Necesidad | Prefiere |
|---|---|
| una solicitud simple | `requests.get/post/...` de nivel superior |
| llamadas repetidas a un servicio | `requests.Session()` |
| cuerpo JSON | `json=` |
| cuerpo de formulario | `data=` |
| parámetros de query | `params=` |
| respuesta grande | `stream=True` + `iter_content()` |
| una falla HTTP debe detener el flujo | `raise_for_status()` |
| retry personalizado | `HTTPAdapter` + política explícita de `Retry` |
| CA privada | `verify=<ruta del CA bundle>` |
| prueba determinista en CI | servidor HTTP local / test double controlado |

## 78. Referencia rápida

```python
import requests


with requests.Session() as session:
    response = session.get(
        "https://example.com/api/items",
        params={"limit": 20},
        headers={"Accept": "application/json"},
        timeout=(3, 10),
    )
    response.raise_for_status()
    data = response.json()
```

Antes de producción, añade las reglas específicas de autenticación, validación de schema, observabilidad, paginación, retry y seguridad que requiera tu integración.

## 79. Checklist de diseño de cliente HTTP

Antes de publicar una integración, responde:

1. ¿Qué métodos HTTP y rutas están permitidos?
2. ¿De dónde provienen las base URLs?
3. ¿Todas las URLs externas son confiables o validadas?
4. ¿Cuáles son los connect y read timeouts?
5. ¿Qué status codes se esperan?
6. ¿Qué media types y campos de respuesta son obligatorios?
7. ¿Cómo se obtienen, rotan y redactan las credenciales?
8. ¿La verificación TLS está habilitada y la PKI privada está correctamente configurada?
9. ¿El cliente reutiliza una Session?
10. ¿Qué fallas son retryable?
11. ¿Las escrituras repetidas son idempotentes o están protegidas por idempotency keys?
12. ¿Cómo se manejan paginación y rate limits?
13. ¿Las respuestas en streaming siempre se cierran?
14. ¿Qué telemetría es segura de registrar?
15. ¿Las pruebas pueden ejecutarse sin depender de una red pública?

## 80. Ejercicio integrado

Construye un **cliente ficticio de API de inventario** contra un servidor HTTP local de prueba.

Requisitos:

1. Crea una clase reutilizable `InventoryClient` que posea una `requests.Session`.
2. Acepta una base URL en el constructor.
3. Aplica un header `Accept: application/json` a nivel de Session.
4. Añade un método que liste items con parámetros `status` y `limit`.
5. Añade un método que cree un item con cuerpo JSON.
6. Usa timeouts explícitos de conexión/lectura.
7. Llama `raise_for_status()` antes de decodificar un payload de éxito.
8. Valida que los objetos item contengan un `id` entero y un `name` string.
9. Traduce excepciones de Requests a una excepción propia de aplicación preservando la original con `raise ... from`.
10. Nunca registres el valor de Authorization.
11. Añade un servidor local que devuelva casos 200, 201, 404, 429 y JSON malformado.
12. Prueba que una respuesta `204` no se decodifique como JSON.
13. Añade paginación con una condición terminal documentada.
14. Explica qué operaciones reintentarías y por qué.
15. Añade un desafío con idempotency key para una escritura.

Desafíos de extensión:

- transmitir un export generado a un archivo temporal y renombrarlo atómicamente;
- configurar una política segura de retry para GET con backoff;
- añadir logs de tiempo de respuesta con correlation ID;
- usar una prepared request para inspeccionar los headers exactos antes de enviar;
- definir un pequeño modelo tipado después de validar el contrato JSON.

## 81. Conexiones con conceptos anteriores

`requests` se apoya directamente en material anterior:

- **diccionarios:** headers, query params, cookies y objetos JSON;
- **funciones/clases:** clientes reutilizables y fronteras explícitas;
- **excepciones:** fallas de transporte, HTTP y decodificación;
- **JSON:** serialización y decodificación de payloads;
- **`pathlib`:** destinos seguros de descarga y rutas de CA/certificados;
- **logging:** llamadas observables con redacción de secretos;
- **`datetime`:** timestamps, validators de caché y campos de fecha en APIs;
- **`os`:** variables de entorno para configuración en runtime;
- **`pandas`:** transformar datos tabulares recibidos desde una API;
- **`openpyxl`:** convertir datos de API en workbooks Excel controlados.

## 82. Referencias primarias

- [Documentación de Requests](https://requests.readthedocs.io/en/latest/)
- [Requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Requests Advanced Usage](https://requests.readthedocs.io/en/latest/user/advanced/)
- [Requests Developer Interface](https://requests.readthedocs.io/en/latest/api/)
- [Requests en PyPI](https://pypi.org/project/requests/)
- [Historial de releases de Requests](https://github.com/psf/requests/releases)

Cuando se preparó este capítulo, Requests 2.34.2 era la versión estable más reciente. El currículo apunta a la serie 2.34.x en lugar de depender de una versión futura sin límite.

## 83. Próximo capítulo

La Fase 9 ahora conecta cuatro fronteras prácticas:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
requests -> exchange data with HTTP services and APIs
pytest   -> verify behavior repeatedly and automatically
```

El siguiente capítulo ya está publicado: [`pytest`: Ingeniería de Pruebas Automatizadas](../04-pytest/README.es.md). Pasa del consumo de servicios externos a demostrar sistemáticamente que el comportamiento de Python continúa siendo correcto.

Antes de continuar, construye al menos un cliente contra un servidor HTTP local. El código de API confiable comienza cuando el comportamiento de red se convierte en algo que puedes reproducir, inspeccionar y probar.
