# Manifesto curricular

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

Este diretório é reservado a manifest.json. Não há manifesto publicado na Sprint 08A.

Aceite da Sprint 08A: schema Draft 2020-12 e validação estrutural/de caminhos estrita com fixtures sintéticas positivas e negativas, incluindo versões independentes dos bancos, caminhos localizados, metadados de execução e JSON inválido. Inventário e navegação (B), relações dos bancos (C), consumidor fixado (D) e aceite consolidado (E) permanecem pendentes. Validador estrutural sozinho não certifica snapshot publicado. CI e review no head exato são obrigatórios; nenhum novo resultado de teste é alegado aqui.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.pt-BR.md) · [Contrato de integração](../docs/specs/learning-hub-foundation/integration-contract.pt-BR.md)

Execute verificações estruturais em um snapshot existente (não validação integral do consumidor):

```bash
python scripts/validate_curriculum.py --root . --manifest curriculum/manifest.json
```

O comando exige o manifesto introduzido em B. A usa fixtures unitárias sintéticas e o workflow de qualidade existente.
