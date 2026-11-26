# HTTP, REST and Backend Fundamentals

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../15-exceptions-testing-and-debugging-review/README.md) · [Module index](../README.md) · [Next →](../17-api-contracts-authentication-and-authorization/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [external-libraries/03-requests](../../external-libraries/03-requests/README.md)
- [technical-interview-preparation/15-exceptions-testing-and-debugging-review](../../technical-interview-preparation/15-exceptions-testing-and-debugging-review/README.md)

## Client, server and resource contracts

HTTP is a request/response protocol: method, target, headers and optional content describe a request; status, headers and optional content describe the response. A backend typically routes, validates, authorizes, applies business rules, persists data and returns a representation. An endpoint is an operation exposed at an interface. REST is an architectural style with constraints including client/server separation, stateless requests, cacheability and a uniform interface; JSON over HTTP alone does not establish REST. Stateless requests carry the information necessary for the server to handle them; the server may still store resource data.

| Method | Intended semantics | Safe / idempotent |
| --- | --- | --- |
| GET | Retrieve a representation | Yes / yes |
| POST | Resource-specific processing, often creation | No / not guaranteed |
| PUT | Create or replace target state | No / yes |
| PATCH | Apply partial change | No / not guaranteed |
| DELETE | Remove target association | No / yes |

Safe means the client does not request a state change; idempotent concerns intended server effect, not identical responses or absence of logging. A retry can duplicate a POST side effect. For writes, require an explicit retry contract (such as a persisted idempotency key), bounded attempts and respect for Retry-After. Set timeouts at network boundaries.

## Response design

200 success; 201 created (often Location); 204 success without content; 400 malformed or invalid request; 404 missing resource; 405 method not supported for the target (include Allow); 409 conflict with current state; 429 rate limit; 500 unexpected server failure. 401 and 403 are addressed next. An error response should describe a stable error contract without internal secrets. Pagination limits response size; define stable ordering, page/cursor semantics and end-of-results behavior.

The shared example is a pure routing simulation for a GET-only teaching endpoint. It returns status, headers and Python objects representing JSON content, not actual HTTP bytes. A real framework must handle serialization, protocol details, HEAD/OPTIONS as supported, and security. Test missing path, unsupported method and independent response data.

## Practice

Sketch a resource /lessons/42, choose a method for retrieval and replacement, and state expected statuses. Explain why repeating DELETE may return a different status while remaining idempotent in intended effect. Test the shared routing example without network.

**Quick reference:** method expresses intent; status expresses outcome; retries depend on semantics; contract before framework.

## Shared executable example

[route_catalog.py](examples/route_catalog.py)

`python technical-interview-preparation/16-http-rest-and-backend-fundamentals/examples/route_catalog.py`

## Official references

- [www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html)

<!-- chapter-navigation:bottom -->
[← Previous](../15-exceptions-testing-and-debugging-review/README.md) · [Module index](../README.md) · [Next →](../17-api-contracts-authentication-and-authorization/README.md)
<!-- /chapter-navigation:bottom -->
