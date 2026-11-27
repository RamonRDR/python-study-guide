# Manifesto curricular

[EN](README.md) · [PT-BR](README.pt-BR.md) · [ES](README.es.md)

O [manifest.json](manifest.json) versionado contém o inventário completo da Sprint 08B: 14 módulos, 107 aulas, oito projetos práticos, 345 caminhos localizados de capítulos/projetos, 42 índices localizados de módulos, 243 recursos compartilhados de capítulos e seis imagens globais. Referencia arquivos existentes e preserva IDs estáveis aprovados. Ordem, títulos de exibição e caminhos localizados seguem as três trilhas; a matriz histórica de avaliações é usada somente na verificação do baseline de autoria. Sem duplicação de conteúdo.

**Relacionamentos completos, aceite da revisão do consumidor pendente:** `association_status` é `complete`. IDs de quiz/exercício identificam propriedade por chapter_id. IDs de entrevista são vínculos reversos de aulas de pré-requisitos documentados, não propriedade; uma pergunta pode aparecer em vários capítulos. Os três simulados estão ligados à aula de simulados e mantêm referências indexadas de perguntas/exercícios. Versões dos bancos continuam 1.0.0 para quiz/exercício e 0.1.0 preliminar para entrevista/simulado. Todos os 253 registros estão cobertos; sem duplicação de corpos. Capítulos permanecem unverified exceto File Organizer (local_only com motivo); aulas de bibliotecas externas referenciam arquivo de dependências existente. Sem alegação de execução no navegador ou versão mínima exata de Python.

Execute verificação estrutural ou a verificação mais forte de inventário rastreado e relacionamentos na raiz do repositório após instalar a dependência de validação existente. A segunda valida todos os registros canônicos com JSON estrito, compara listas de associações exatas, mantém regressões de inventário e requer checkout Git. Sucesso estrutural sozinho não é aceite integral. `python scripts/curriculum_relationships.py` emite mapa determinístico dos bancos existentes sem alterar arquivos. Nenhum comando verifica identidade imutável da revisão do consumidor; isso permanece na 08D, com aceite final na 08E.

[Schema](../schemas/curriculum-manifest.schema.json) · [ADR 0004](../docs/adr/0004-curriculum-manifest.pt-BR.md) · [Contrato de integração](../docs/specs/learning-hub-foundation/integration-contract.pt-BR.md)

```bash
python scripts/validate_curriculum.py
python scripts/validate_curriculum.py --inventory
```

## Fixture de consumidor fixada (Sprint 08D)

O [lock do consumidor](../tests/fixtures/learning-hub/consumer-lock.json) externo, somente para testes, fixa o commit revisado da 08C `ffb53c7b64a602f09f9943489ec7741d72843831` e versões exatas suportadas. Não é release de produção nem autorreferência no manifesto. Em checkout Git com esse commit disponível, execute:

```bash
python scripts/curriculum_consumer.py
```

Código confiável do consumidor exporta a árvore Git fixada para staging temporário isolado, confere cada arquivo regular com a identidade de blob Git, rejeita revisões misturadas, arquivos ausentes/extras e symlinks, compara os cinco schemas com cópias locais confiáveis e valida versões exatas, navegação e todos os relacionamentos de avaliações com validadores do consumidor. Código do snapshot nunca é executado; matriz de autoria e parsing das trilhas não são necessários. Lock fica fora do snapshot. Candidato deve passar antes da seleção de seu pin; rollback significa selecionar e validar o pin aprovado anterior. Fixtures sintéticas de atualização/rollback não publicam revisões. Assume-se confiança no banco de objetos Git local e no código confiável do consumidor; não é verificação de assinatura nem sandbox contra mutação concorrente no filesystem. Histórico Git completo é obtido uma vez pelo checkout Linux do CI; sem requisições por visitante, novas dependências, execução no navegador ou deploy do site. AC-08 permanece aberto até 08E.

## Aceite consolidado (Sprint 08E)

A suíte de aceite consolidado compara inventário de autoria ao pin original 08C e pin temporário da revisão 08D aprovada. Todas as referências do manifesto e bytes dos registros canônicos devem coincidir. Commits Git reais locais com dados inválidos devem falhar no aceite semântico mesmo com identidade de bytes aprovada. Lock externo de teste permanece inalterado; sem release de produção, runtime de navegador ou site. Encerramento AC-08 registrado após gates finais; Sprint 09 realiza QA final e handoff de revisão. [Testes de aceite](../tests/test_curriculum_acceptance.py).
