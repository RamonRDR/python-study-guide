# API Contracts, Authentication and Authorization

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../16-http-rest-and-backend-fundamentals/README.md) · [Module index](../README.md) · [Next →](../18-relational-databases-and-sql/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [external-libraries/03-requests](../../external-libraries/03-requests/README.md)
- [standard-library/03-json](../../standard-library/03-json/README.md)
- [technical-interview-preparation/16-http-rest-and-backend-fundamentals](../../technical-interview-preparation/16-http-rest-and-backend-fundamentals/README.md)

## Validate the boundary

An API contract describes requests, required and optional fields, types, bounds, responses, errors and compatibility. Parsing JSON is not validation. Reject oversized inputs before parsing where possible; validate shape and allowed fields, types (booleans are not business integers by default), lengths and ranges. Unknown fields may be rejected or ignored according to a documented contract, not silently persisted. Return consistent errors and avoid leaking stack traces. Add fields compatibly where clients permit; version or migrate breaking changes.

The example validates an already decoded object with exactly one title field, trims whitespace and accepts 1–80 characters after trimming. It does not handle raw HTTP, duplicate JSON names or body size; these belong at the parsing/transport boundary.

## Authentication versus authorization

Authentication establishes a verified identity; authorization decides what that identity may do to a specific resource. Use established authentication libraries/providers, HTTPS, verified token signature and appropriate issuer/audience/expiry checks when applicable. Never treat a client-supplied owner or decoded-but-unverified token as identity. Store credentials securely, avoid logging them and apply least privilege. A bearer token is a credential; possession alone is meaningful only after verification. The example intentionally implements no token issuance or validation.

Object-level authorization is required for every protected resource access: a valid login is insufficient to read another owner's note. The example receives a trusted principal from a hypothetical prior layer; None yields 401 with a Bearer challenge, nonexistent ID yields 404, and a different owner yields 403 without note content. 401 means valid authentication credentials are missing; 403 means the server refuses access. Some systems deliberately return 404 for forbidden resources to avoid revealing existence; choose and document the policy consistently. This example deliberately exposes existence to authenticated users via 403 versus 404 and is not a production security boundary.

## Practice

Test anonymous, authorized owner, other owner, missing resource and malformed payloads. Explain why checking a role alone might not enforce object ownership. Sketch where authentication, object lookup, authorization and serialization would occur in a real service. Add a negative test before changing any policy.

**Quick reference:** parse then validate; verified identity first; authorize action and object; never trust client claims.

## Shared executable example

[note_access.py](examples/note_access.py)

`python technical-interview-preparation/17-api-contracts-authentication-and-authorization/examples/note_access.py`

## Official references

- [www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html)
- [api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)
- [devguide.owasp.org/en/07-training-education/07-api-top-ten/](https://devguide.owasp.org/en/07-training-education/07-api-top-ten/)

<!-- chapter-navigation:bottom -->
[← Previous](../16-http-rest-and-backend-fundamentals/README.md) · [Module index](../README.md) · [Next →](../18-relational-databases-and-sql/README.md)
<!-- /chapter-navigation:bottom -->
