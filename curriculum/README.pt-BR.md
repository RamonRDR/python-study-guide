# Manifesto curricular

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

O [manifest.json](manifest.json) versionado contém o inventário completo da Sprint 08B: 14 módulos, 107 aulas, oito projetos práticos, 345 caminhos localizados de capítulos/projetos, 42 índices localizados de módulos, 243 recursos compartilhados de capítulos e seis imagens globais. Referencia arquivos existentes e preserva IDs estáveis aprovados. Ordem, títulos de exibição e caminhos localizados seguem as três trilhas; a matriz histórica de avaliações é usada somente na verificação do baseline de autoria. Sem duplicação de conteúdo.

**Apenas snapshot de desenvolvimento:** association_status é pending; todas as listas de referências de quiz/exercício/entrevista/simulado estão vazias até 08C. Consumidores não devem importá-lo como snapshot completo aprovado. Capítulos são unverified exceto File Organizer (local_only com motivo); aulas de bibliotecas externas referenciam o arquivo compartilhado de dependências existente. Não se afirma execução no navegador ou versão mínima exata de Python.

Execute a verificação estrutural ou a verificação mais forte de inventário rastreado abaixo na raiz do repositório, após instalar a dependência existente de validação de avaliações. A segunda compara manifesto com trilhas fonte, IDs estáveis do baseline, recursos rastreados, assets e navegação global. Requer checkout Git. Nenhum comando verifica integridade da revisão do consumidor ou associações completas de avaliações.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.pt-BR.md) · [Contrato de integração](../docs/specs/learning-hub-foundation/integration-contract.pt-BR.md)

```bash
python scripts/validate_curriculum.py
python scripts/validate_curriculum.py --inventory
```
