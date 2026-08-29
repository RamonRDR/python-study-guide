<div align="center">

# Consuming HTTP APIs with `requests`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Back to External Libraries](../README.md) · [← Previous: `openpyxl`](../02-openpyxl/README.md)

Local files are only one kind of boundary. Modern Python programs also exchange data with web services, internal APIs, SaaS platforms, authentication servers, storage endpoints, and other systems over HTTP. The `requests` package gives Python a compact, readable HTTP client while still exposing the protocol concepts that reliable integrations need.

This chapter targets **Requests 2.34.x** and was researched against the current **Requests 2.34.2** documentation and release metadata. Requests 2.34.2 requires Python 3.10 or newer; this repository validates examples on Python 3.13.

**Estimated study time:** 270–360 minutes.

## Learning goals

By the end of this chapter, you should be able to:

- explain the HTTP request/response model without treating an API call as a magical function call;
- issue GET, POST, PUT, PATCH, and DELETE requests intentionally;
- send query parameters, headers, form data, JSON bodies, files, and authentication data;
- distinguish transport success, HTTP success, and payload validity;
- configure connect/read timeouts and understand what they do not guarantee;
- handle Requests exceptions without hiding useful failure context;
- use `Session` for connection reuse, cookies, and shared request defaults;
- understand redirects, TLS verification, CA bundles, proxies, and environment settings;
- stream large responses safely and close resources deterministically;
- add retries only when the operation is safe to repeat;
- protect credentials and avoid logging secrets;
- validate API response contracts instead of trusting arbitrary JSON;
- build deterministic HTTP tests without depending on a public internet service.

## 1. Why `requests` exists

Python's standard library can speak HTTP, but `requests` provides a higher-level interface for common client work: URLs, query parameters, headers, cookies, authentication, request bodies, TLS verification, sessions, streaming, and exceptions.

The convenience is valuable, but the network is still a distributed-system boundary. A readable API does not remove latency, partial failure, authentication rules, server errors, retries, or security decisions.

## 2. Think in requests and responses

A client sends an HTTP request containing some combination of:

```text
method + URL + headers + optional body
```

The server returns an HTTP response containing:

```text
status code + headers + body
```

Your Python code must reason about both halves.

## 3. External libraries need a version contract

This repository declares Phase 9 dependencies in `requirements-external.txt`.

For this chapter the contract is:

```text
requests >= 2.34 and < 2.35
```

The 2.34 series also introduced inline typing in Requests itself, so current type checkers can consume public API types without depending on a separate stubs package.

## 4. Install the repository dependency set

Create and activate a virtual environment, then install:

```bash
python -m pip install -r requirements-external.txt
```

For isolated experimentation, `python -m pip install requests` is valid, but a project should record its supported dependency range.

## 5. Import the package

The conventional import is:

```python
import requests
```

The top-level module exposes convenience functions such as `get()`, `post()`, and `delete()`, plus classes such as `Session` and exception types under `requests.exceptions`.

## 6. A URL is part of your input contract

An HTTP URL commonly contains:

```text
scheme://host:port/path?query#fragment
```

For an HTTP client, the scheme, host, port, path, and query parameters affect the actual request. Fragments are generally interpreted client-side and are not sent as the HTTP request target.

Do not concatenate untrusted URL fragments carelessly.

## 7. Start with a GET request

A basic GET looks like this:

```python
import requests


response = requests.get("https://example.com/api/items", timeout=(3, 10))
print(response.status_code)
```

This snippet is illustrative because it depends on an external endpoint. Published executable examples later in the chapter use a local test server instead.

## 8. Status codes communicate HTTP outcomes

Common classes are:

```text
1xx -> informational
2xx -> successful response
3xx -> redirection
4xx -> client-side request problem
5xx -> server-side failure
```

A `200` is not the only successful status. A POST may correctly return `201 Created`, and a DELETE may return `204 No Content`.

## 9. Use `raise_for_status()` when non-success HTTP codes are failures

```python
response = requests.get(url, timeout=(3, 10))
response.raise_for_status()
```

For unsuccessful HTTP status codes, `raise_for_status()` raises `requests.HTTPError` and keeps the response attached to the exception.

Do not throw away that context when reporting a failure.

## 10. Transport success is not application success

An HTTP exchange can succeed at the network layer while the server returns `404`, `429`, or `500`.

Conversely, a `200` response may contain data that violates your business contract.

A robust client checks more than “did `requests.get()` return?”

## 11. `response.text` is decoded text

```python
text = response.text
```

Requests decodes response bytes according to response encoding information and its own detection rules.

Use text when the body is genuinely textual and you want a `str`.

## 12. `response.content` gives raw bytes

```python
payload = response.content
```

Use bytes for binary files, checksums, image data, compressed artifacts, or any format where decoding to text would be incorrect.

## 13. Decode JSON with `response.json()`

```python
response = requests.get(url, timeout=(3, 10))
response.raise_for_status()
data = response.json()
```

`response.json()` parses the response body. It does not prove that the HTTP status was successful.

## 14. Invalid JSON has its own failure mode

Requests exposes `requests.exceptions.JSONDecodeError` for JSON decoding failures.

```python
try:
    data = response.json()
except requests.exceptions.JSONDecodeError as exc:
    raise RuntimeError("API returned invalid JSON") from exc
```

A `204 No Content` response, an HTML error page, or malformed JSON can make decoding fail.

## 15. JSON shape still needs validation

Even valid JSON can be wrong for your program:

```python
if not isinstance(data, dict) or "items" not in data:
    raise ValueError("Unexpected API response shape")
```

Parsing answers “is this JSON?” Contract validation answers “is this the JSON our application expects?”

## 16. Send query parameters with `params`

Do not hand-build query strings when Requests can encode them:

```python
response = requests.get(
    url,
    params={"status": "open", "limit": 20},
    timeout=(3, 10),
)
```

Requests handles query encoding and exposes the final URL through `response.url`.

## 17. Repeated query parameters may use sequences

APIs sometimes expect repeated keys. Requests accepts sequence values or a list of two-tuples.

```python
params = [("tag", "python"), ("tag", "http")]
response = requests.get(url, params=params, timeout=(3, 10))
```

Follow the target API's documented parameter contract.

## 18. Request headers are metadata

```python
headers = {
    "Accept": "application/json",
    "User-Agent": "study-client/1.0",
}
response = requests.get(url, headers=headers, timeout=(3, 10))
```

Headers can communicate representation preferences, authentication, conditional requests, tracing, and other protocol metadata.

## 19. Do not confuse request and response headers

Request headers are what your client sends. Response headers are what the server returns.

```python
content_type = response.headers.get("Content-Type")
```

Requests response headers behave like a case-insensitive mapping.

## 20. Use a descriptive `User-Agent` when appropriate

Many APIs appreciate a client identifier for operations and support diagnostics.

Avoid pretending to be an unrelated browser unless the integration contract explicitly requires it.

## 21. POST form data with `data=`

For form-style data:

```python
response = requests.post(
    url,
    data={"username": "demo", "mode": "compact"},
    timeout=(3, 10),
)
```

Requests encodes a mapping passed through `data=` as form data.

## 22. POST JSON with `json=`

For JSON APIs, prefer the dedicated parameter:

```python
payload = {"name": "Nova", "active": True}
response = requests.post(url, json=payload, timeout=(3, 10))
response.raise_for_status()
```

`json=` serializes the value and sets an appropriate JSON content type.

## 23. Do not manually serialize JSON without a reason

This is usually less clear:

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

Use `json=` unless you need precise control over the serialized bytes.

## 24. PUT and PATCH express different update contracts

The HTTP specification and an API's own documentation determine semantics. Commonly:

```text
PUT   -> replace or set a representation at a target
PATCH -> partially modify a representation
```

Do not infer server behavior from method names alone. Read the API contract.

## 25. DELETE may succeed without a body

```python
response = requests.delete(url, timeout=(3, 10))
response.raise_for_status()
```

A successful `204 No Content` should not be followed by unconditional `response.json()`.

## 26. Idempotency matters before retries

An operation is idempotent when repeating the same intended request has the same intended effect as performing it once.

GET, HEAD, PUT, and DELETE are defined with idempotent semantics at the HTTP method level; POST generally is not. Application behavior and idempotency keys can add further guarantees.

## 27. Nearly all production requests need a timeout

Requests does **not** time out by default.

```python
response = requests.get(url, timeout=10)
```

Without an explicit timeout, a program may wait indefinitely for network activity.

## 28. Separate connect and read timeouts when useful

Requests accepts a tuple:

```python
response = requests.get(url, timeout=(3, 15))
```

The first value is the connect timeout. The second is the read timeout.

This is often clearer than one number for integrations where establishing a connection and waiting for response bytes have different expectations.

## 29. A Requests timeout is not a total wall-clock deadline

The documented timeout behavior is based on socket inactivity, not a guaranteed maximum duration for the complete download.

A slow response that keeps delivering bytes may last longer than the nominal read-timeout value.

If a workflow needs a hard overall deadline, design that deadline separately.

## 30. Requests has a useful exception hierarchy

Requests-specific exceptions inherit from `requests.exceptions.RequestException`.

Important subclasses include:

```text
HTTPError
ConnectionError
Timeout
TooManyRedirects
JSONDecodeError
SSLError
```

Catch narrowly when you have distinct recovery behavior.

## 31. `Timeout` deserves explicit handling

```python
try:
    response = requests.get(url, timeout=(3, 10))
except requests.Timeout as exc:
    raise RuntimeError("Remote service timed out") from exc
```

A timeout is different from an HTTP `500`: the client may not know whether the server processed the request.

That uncertainty is crucial before retrying a write operation.

## 32. `ConnectionError` covers network connection failures

DNS resolution failures, refused connections, and related transport failures may surface as `requests.ConnectionError`.

Do not turn these into an empty successful result. Preserve the failure signal or apply an explicit recovery policy.

## 33. `HTTPError` gives access to the response

```python
try:
    response.raise_for_status()
except requests.HTTPError as exc:
    status = exc.response.status_code
    raise RuntimeError(f"API returned HTTP {status}") from exc
```

Avoid including arbitrary response bodies in logs because they may contain secrets or personal data.

## 34. A top-level `RequestException` boundary can add context

At an application boundary, a wrapper can add the service operation name:

```python
try:
    response = requests.get(url, timeout=(3, 10))
    response.raise_for_status()
except requests.RequestException as exc:
    raise RuntimeError("Could not load catalog") from exc
```

Do not catch `Exception` merely to make a network failure disappear.

## 35. Redirects have history

Requests follows redirects for common GET-style requests and exposes prior responses through:

```python
for previous in response.history:
    print(previous.status_code, previous.url)
```

The final response URL is available as `response.url`.

## 36. Limit or disable redirects when the contract requires it

```python
response = requests.get(
    url,
    allow_redirects=False,
    timeout=(3, 10),
)
```

Redirect behavior can matter for authentication, auditing, SSRF defenses, and signed URLs.

## 37. Basic authentication has a dedicated helper

```python
from requests.auth import HTTPBasicAuth


response = requests.get(
    url,
    auth=HTTPBasicAuth("demo-user", "demo-password"),
    timeout=(3, 10),
)
```

Never hard-code real credentials in source code, examples, commits, or logs.

## 38. Bearer tokens are usually headers

```python
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, headers=headers, timeout=(3, 10))
```

The token should come from a secure runtime source such as a secret manager or protected environment variable, not from a repository file.

## 39. Redact secrets from observability

Do not log full values of:

```text
Authorization
Proxy-Authorization
Cookie
Set-Cookie
API keys
signed URLs
client certificates or private keys
```

Useful logging can include the HTTP method, sanitized host/path, status code, elapsed time, retry count, and correlation identifiers.

## 40. `Session` keeps state across requests

```python
import requests


with requests.Session() as session:
    session.headers.update({"Accept": "application/json"})
    response = session.get(url, timeout=(3, 10))
```

A Session can persist defaults and cookies across calls.

## 41. Sessions also reuse connections

Requests Sessions use urllib3 connection pooling. Multiple calls to the same host can reuse underlying connections instead of establishing a new TCP/TLS connection every time.

This can materially reduce overhead in repeated API workflows.

## 42. Session defaults can be overridden per request

Session-level headers, authentication, cookies, proxies, and other parameters are convenient defaults, not immutable globals.

Keep shared configuration intentional so one request does not accidentally inherit credentials intended for another service.

## 43. Close Sessions deterministically

Use a context manager or call `close()`:

```python
with requests.Session() as session:
    response = session.get(url, timeout=(3, 10))
    response.raise_for_status()
```

Resource ownership should be visible in long-running processes.

## 44. Cookies can persist in a Session

A server may set cookies in one response and expect them in later requests. A Session maintains a cookie jar across calls.

For API clients, explicit token-based authentication is often easier to reason about, but cookie-based workflows still exist.

## 45. Prepared requests expose the exact outgoing request

Requests can build a `PreparedRequest` before sending it:

```python
from requests import Request, Session


with Session() as session:
    request = Request("GET", url, headers={"X-Trace": "demo"})
    prepared = session.prepare_request(request)
    print(prepared.method, prepared.url)
```

This is useful for advanced signing, inspection, or controlled request mutation.

## 46. Prefer `Session.prepare_request()` when Session state matters

Calling `Request.prepare()` directly does not automatically apply all Session-level state.

If cookies, default headers, or authentication from a Session are part of the contract, prepare the request through that Session.

## 47. Prepared-request flows need environment awareness

The advanced Requests documentation notes that manually sending a prepared request can bypass environment-derived settings unless they are merged explicitly.

This matters for settings such as CA bundles and proxies.

Advanced request preparation should therefore be deliberate, not a default pattern for ordinary calls.

## 48. HTTPS certificate verification is enabled by default

Requests verifies server TLS certificates for HTTPS connections.

```python
response = requests.get("https://example.com", timeout=(3, 10))
```

If certificate verification fails, Requests raises `SSLError` rather than silently trusting the peer.

## 49. `verify=False` disables an important security guarantee

```python
response = requests.get(url, verify=False, timeout=(3, 10))
```

This accepts certificates that may be expired, self-signed, or for the wrong hostname and can enable man-in-the-middle attacks.

Do not solve a production certificate problem by globally disabling verification.

## 50. Private PKI should use an explicit CA bundle

Requests lets `verify` point to a trusted CA bundle:

```python
response = requests.get(
    url,
    verify="/path/to/company-ca-bundle.pem",
    timeout=(3, 10),
)
```

Requests also recognizes `REQUESTS_CA_BUNDLE`, with `CURL_CA_BUNDLE` as a fallback in its documented environment behavior.

## 51. Client certificates support mutual TLS workflows

The `cert` parameter can point to a client certificate or a certificate/key pair:

```python
response = requests.get(
    url,
    cert=("client.crt", "client.key"),
    timeout=(3, 10),
)
```

Private-key files are secrets. Protect them as credentials.

## 52. Proxies may come from arguments or the environment

Requests supports per-request proxy configuration and environment-derived proxy settings.

```python
proxies = {"https": "http://proxy.example:8080"}
response = requests.get(url, proxies=proxies, timeout=(3, 10))
```

Do not place real proxy credentials in source code.

## 53. `Session.trust_env` controls environment integration

Sessions default to trusting relevant environment configuration such as proxies and authentication sources.

If a client must operate independently of ambient process configuration, evaluate `session.trust_env` explicitly and document the consequences.

## 54. Streaming avoids loading an entire body immediately

```python
with requests.get(url, stream=True, timeout=(3, 30)) as response:
    response.raise_for_status()
    for chunk in response.iter_content(chunk_size=64 * 1024):
        if chunk:
            process(chunk)
```

Streaming is useful for large downloads and incremental processing.

## 55. Streamed responses must be consumed or closed

Connection reuse depends on releasing the underlying connection.

Using the response as a context manager makes the ownership boundary explicit even when processing raises an exception.

## 56. `iter_content()` is usually better than reading `raw` directly

`iter_content()` cooperates with Requests' decoding behavior and chunked iteration.

Choose a chunk size based on the use case rather than assuming each chunk corresponds to a server-side message boundary.

## 57. Streaming lines is useful for line-oriented protocols

`response.iter_lines()` can process a streaming response line by line.

Be careful with keep-alive blank lines, partial application records, and reconnect semantics defined by the specific streaming API.

## 58. Write large downloads safely

For an important artifact, a safer pattern is:

```text
download to temporary path
-> verify status / size / checksum if available
-> flush and close
-> atomically move into final location
```

This prevents a partial download from masquerading as a completed file.

## 59. Multipart uploads use `files=`

```python
with open("report.txt", "rb") as file_handle:
    response = requests.post(
        url,
        files={"file": ("report.txt", file_handle, "text/plain")},
        timeout=(3, 30),
    )
```

The file object should be opened in binary mode for predictable byte handling.

## 60. Requests does not retry failed connections by default

The built-in `HTTPAdapter` defaults to no connection retries.

Retries are an application policy, not something to assume happened automatically.

## 61. `HTTPAdapter` can add a retry policy

For granular behavior, Requests documents using urllib3's `Retry` class:

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

Retry policy should be designed with the API contract, not copied blindly.

## 62. Never retry a write merely because it failed

A timeout after sending a POST can mean:

```text
client does not know whether server committed the operation
```

Blindly repeating it may create duplicates.

Use idempotency keys, operation identifiers, safe methods, or reconciliation logic when the service supports them.

## 63. Respect `Retry-After` and rate-limit contracts

A `429 Too Many Requests` response often means the client should slow down.

The exact headers and retry behavior are API-specific. Read the service contract and avoid tight retry loops that amplify an outage.

## 64. Backoff reduces retry storms

Retries should normally wait between attempts. Exponential backoff and jitter help many clients avoid synchronizing their retries against the same recovering service.

The exact policy belongs to your system reliability design.

## 65. Response hooks can add cross-cutting behavior

Requests supports `response` hooks:

```python
def record_status(response: requests.Response, *args: object, **kwargs: object) -> None:
    print(response.status_code)


response = requests.get(
    url,
    hooks={"response": record_status},
    timeout=(3, 10),
)
```

Hooks should remain small and must handle their own assumptions and failures.

## 66. Pagination is an API contract, not a Requests feature

APIs may paginate with:

```text
page/limit query parameters
cursor tokens
Link headers
next URLs in JSON
```

Your client should stop on the service's documented terminal condition and defend against accidental infinite loops.

## 67. Link headers are parsed for you

When a response contains standard Web Linking headers, Requests exposes parsed links through:

```python
next_link = response.links.get("next")
```

Do not assume every API uses Link headers for pagination.

## 68. Validate response media type when it matters

If an endpoint promises JSON, inspect the response contract as needed:

```python
content_type = response.headers.get("Content-Type", "")
if "application/json" not in content_type.lower():
    raise ValueError("Expected a JSON response")
```

Be precise enough for the API you integrate with; media types may include parameters or vendor-specific `+json` forms.

## 69. Logging HTTP calls requires redaction

A useful structured record may contain:

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

Avoid logging full URLs when query parameters may contain secrets or personal information.

## 70. Deterministic tests should not depend on the public internet

A public endpoint can be slow, unavailable, rate-limited, geo-blocked, or changed independently of your repository.

The executable examples in this chapter start a local `ThreadingHTTPServer` on `127.0.0.1`, exercise Requests against it, then shut it down. That tests real HTTP behavior without external network dependence.

## 71. Practical example: GET with query parameters

[`examples/get_with_query.py`](examples/get_with_query.py) sends a real local HTTP GET request, lets Requests encode query parameters, checks the status, decodes JSON, and prints the parsed query contract.

Expected output:

```text
status: 200
path: /items
query: {'status': ['open'], 'limit': ['2']}
```

## 72. Practical example: POST JSON

[`examples/post_json.py`](examples/post_json.py) verifies that `json=` sends a JSON payload with the expected content type.

Expected output:

```text
status: 201
created: {'name': 'Nova', 'active': True}
content-type: application/json
```

## 73. Practical example: Session defaults

[`examples/session_defaults.py`](examples/session_defaults.py) uses a Session to apply shared headers, then confirms that the local server received them.

Expected output:

```text
client: python-study-guide
auth-scheme: Bearer
```

The token is fictional and exists only inside the local example process.

## 74. Practical example: visible HTTP errors

[`examples/http_error_handling.py`](examples/http_error_handling.py) intentionally receives `404` and demonstrates `raise_for_status()` preserving the response on `HTTPError`.

Expected output:

```text
caught: HTTPError
status: 404
```

## 75. Practical example: streaming download

[`examples/stream_download.py`](examples/stream_download.py) streams deterministic local bytes with `iter_content()` and closes the response through a context manager.

Expected output:

```text
bytes: 12
content: chunked-data
```

## 76. Common mistakes

Avoid these patterns:

| Mistake | Why it is risky | Better approach |
|---|---|---|
| omit `timeout` | request may wait indefinitely | define connect/read expectations |
| call `json()` and assume success | error responses can contain valid JSON | check HTTP status and payload contract |
| use `verify=False` in production | disables TLS identity verification | fix trust chain or provide CA bundle |
| retry every exception | may duplicate writes or worsen outages | retry only safe, classified failures |
| create a new Session for every call | loses connection reuse | own a Session for a logical client lifetime |
| log Authorization headers | leaks credentials | redact secrets |
| trust arbitrary JSON shape | schema drift becomes hidden bugs | validate required fields/types |
| test against a public demo API | CI becomes externally fragile | use a local server or controlled test double |

## 77. Decision table

| Need | Prefer |
|---|---|
| one simple request | top-level `requests.get/post/...` |
| repeated calls to one service | `requests.Session()` |
| JSON request body | `json=` |
| form request body | `data=` |
| query parameters | `params=` |
| large response | `stream=True` + `iter_content()` |
| HTTP failure should stop flow | `raise_for_status()` |
| custom retry behavior | `HTTPAdapter` + explicit `Retry` policy |
| private CA | `verify=<CA bundle path>` |
| deterministic CI test | local HTTP server / controlled test double |

## 78. Quick reference

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

Before production, add the service-specific authentication, schema validation, observability, pagination, retry, and security rules your integration requires.

## 79. HTTP client design checklist

Before publishing an integration, answer:

1. Which HTTP methods and routes are allowed?
2. Where do base URLs come from?
3. Are all external URLs trusted or validated?
4. What are the connect and read timeouts?
5. Which status codes are expected?
6. Which response media types and fields are required?
7. How are credentials sourced, rotated, and redacted?
8. Is TLS verification enabled and is private PKI configured correctly?
9. Does the client reuse a Session?
10. Which failures are retryable?
11. Are repeated write operations idempotent or protected by idempotency keys?
12. How are pagination and rate limits handled?
13. Are streamed responses always closed?
14. What telemetry is safe to record?
15. Can tests run without a public network dependency?

## 80. Integrated exercise

Build a fictional **inventory API client** against a local HTTP test server.

Requirements:

1. Create a reusable `InventoryClient` class that owns a `requests.Session`.
2. Accept a base URL in the constructor.
3. Apply an `Accept: application/json` header at Session level.
4. Add a method that lists items with `status` and `limit` query parameters.
5. Add a method that creates an item with a JSON body.
6. Use explicit connect/read timeouts.
7. Call `raise_for_status()` before decoding a success payload.
8. Validate that item objects contain an integer `id` and string `name`.
9. Translate Requests exceptions into one application-specific exception while preserving the original exception with `raise ... from`.
10. Never log the Authorization value.
11. Add a local test server that returns 200, 201, 404, 429, and malformed JSON cases.
12. Test that a `204` response is not decoded as JSON.
13. Add pagination with a documented terminal condition.
14. Explain which operations you would retry and why.
15. Add one extension challenge using an idempotency key for a write request.

Extension challenges:

- stream a generated export into a temporary file and atomically rename it;
- configure a safe GET retry policy with backoff;
- add response timing logs with a correlation ID;
- use a prepared request to inspect the exact headers before sending;
- define a small typed data model after validating the JSON contract.

## 81. Connections to earlier concepts

`requests` builds directly on earlier material:

- **dictionaries:** headers, query parameters, cookies, and JSON objects;
- **functions/classes:** reusable service clients and explicit boundaries;
- **exceptions:** transport, HTTP, and decoding failures;
- **JSON:** payload serialization and decoding;
- **`pathlib`:** safe download destinations and CA/certificate paths;
- **logging:** observable calls with secret redaction;
- **`datetime`:** timestamps, cache validators, and API date fields;
- **`os`:** environment variables for runtime configuration;
- **`pandas`:** transform tabular data received from an API;
- **`openpyxl`:** turn API data into controlled Excel workbooks.

## 82. Primary references

- [Requests documentation](https://requests.readthedocs.io/en/latest/)
- [Requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Requests Advanced Usage](https://requests.readthedocs.io/en/latest/user/advanced/)
- [Requests Developer Interface](https://requests.readthedocs.io/en/latest/api/)
- [Requests on PyPI](https://pypi.org/project/requests/)
- [Requests release history](https://github.com/psf/requests/releases)

At the time this chapter was prepared, Requests 2.34.2 was the latest stable release. The curriculum targets the 2.34.x series instead of relying on an unbounded future version.

## 83. Next chapter

Phase 9 now connects three practical boundaries:

```text
pandas   -> transform tabular data
openpyxl -> construct and maintain Excel workbooks
requests -> exchange data with HTTP services and APIs
```

The next planned library is **`pytest`**, where the focus moves from using external libraries to systematically proving that Python behavior remains correct.

Before moving on, build at least one client against a local HTTP server. Reliable API code starts when network behavior becomes something you can reproduce, inspect, and test.
