# Transferência para o Learning Hub

[🇺🇸 English](handoff.md) · [🇧🇷 Português](handoff.pt-BR.md) · [🇪🇸 Español](handoff.es.md)

Status: 09B em revisão; referência de implementação, não aprovação final do AC-09 nem deploy de produção. A revisão de conteúdo 09A foi integrada e aprovada no CI; validação exata do candidato, revisão 09B e aprovação do mantenedor precedem o encerramento.

## 1. Fonte e revisão imutável

Repositório: [RamonRDR/python-study-guide](https://github.com/RamonRDR/python-study-guide), público e com licença MIT. Preservar autoria e licença. Candidato de conteúdo (SHA Git completo e imutável): `03e91ff9952f2b02293f16a11260d166eb00ea8a`, árvore `f1cbf0689a8bf1f26539ed1b330b5c51ce7ce4e6`. É o squash da 09A, não o commit documental da 09B, nome de branch ou tag de release. Nenhuma tag/release criada. O próprio handoff é revisado em commit posterior; não inserir o SHA do próprio commit em si. Selecionar pin de consumo aprovado somente após validação e aprovação do mantenedor.

[PR #113](https://github.com/RamonRDR/python-study-guide/pull/113) · [CI #46059023528](https://github.com/RamonRDR/python-study-guide/actions/runs/46059023528) · [Codex](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226444778) · [Final Pre-Merge Audit](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226469107) · [09A closure](https://github.com/RamonRDR/python-study-guide/pull/113#issuecomment-7226902203)

## 2. Arquitetura e responsabilidades

O guia é a fonte única da verdade; site externo consome um commit validado no build, sem scraping HTML ou chamadas à API GitHub por aluno. Preservar estudo independente no GitHub/local. Markdown e Python compartilhado são canônicos; JSON estruturado orienta a UI. Fora de escopo: serviço pago, Python no servidor, correção por IA e entrevistador IA. Progresso local do navegador é específico do dispositivo, sem sincronização de conta. ADRs aceitos: 0001 fonte da verdade, 0002 contrato de conteúdo, 0003 direção de runtime futuro (implementação não verificada), 0004 manifesto. Consultar índice ADR e contrato.

[ADR](../../adr/README.pt-BR.md) · [Integration contract](integration-contract.pt-BR.md) · [Assessment contract](assessment-contract.pt-BR.md)

## 3. Contrato canônico e inventário

| Entrada canônica | Versão | Schema / validador | Quantidade |
| --- | --- | --- | --- |
| `curriculum/manifest.json` | 1.0.0 | `schemas/curriculum-manifest.schema.json` | 14 / 115 |
| `quizzes/quiz-index.json` | 1.0.0 | `schemas/quiz-index.schema.json`, `schemas/quiz.schema.json` | 160 |
| `exercises/problem-solving/exercise-index.json` | 1.0.0 | `schemas/exercise-index.schema.json`, `schemas/exercise.schema.json` | 30 |
| `interviews/interview-index.json` | 0.1.0 | `scripts/validate_interviews.py` | 60 |
| `interviews/mocks/mock-index.json` | 0.1.0 | `scripts/validate_interviews.py` | 3 |

Cinco schemas JSON usam Draft 2020-12; registros de entrevista/simulado permanecem preliminares e usam validadores Python confiáveis, sem inventar schemas JSON. association_status deve ser complete. Inventário: 107 aulas + oito projetos = 115 entradas, 345 caminhos de conteúdo localizado, 42 índices de módulo, 243 recursos de capítulo, seis assets globais. 253 registros canônicos; 268 associações (160 quiz, 30 exercício, 75 links de pré-requisitos de entrevistas, três de simulados). Dificuldade easy/medium/hard: quizzes 64/67/29, 2.850 XP; exercícios 12/12/6, 192 casos; entrevistas junior/mid/senior 24/24/12; simulados 30/45/60 minutos. Testes existentes sustentam contagens; consultar QA.

## 4. Navegação, idiomas e recursos

Usar arrays de módulos/capítulos e ordem explícita zero-based, previous_id/next_id globais (null nas pontas), IDs estáveis e mapas de índice/conteúdo/título por idioma. Padrão en; suportados en, pt-BR, es. Não usar títulos, caminhos ou ordem de diretórios como identidade. Fase não é número da sprint de engenharia. chapter_id de quiz/exercício indica propriedade; interview_ids são referências reversas a pré-requisitos; mock_ids pertencem à aula de simulados. Seguir índices e referências tipadas; não interpretar matriz de autoria ou trilhas mestras. Resolver links/assets na mesma revisão validada, sanitizar Markdown/HTML, preservar troca de idioma e fallback/erros acessíveis. Recursos não são lista de execução; apenas scripts/example_manifest.txt lista exemplos autorizados do repositório. Dependência opcional ausente significa não especificada; quatro aulas externas declaram requirements-external.txt.

## 5. Exemplos de registros reais

- Capítulo `getting-started.install-python`: order 0, previous_id null, next_id `getting-started.configure-vscode`, quiz `quiz.interpreter-purpose`, execution unverified.
- Quiz `quiz.absolute-distance-zero`: `quizzes/questions/quiz.absolute-distance-zero.json`, string exata aceita `abs`, `magnitude = ____(-11)`, 10 XP. Resultado 11.
- Exercício `problem-solving.ascii-digit-counter`: `exercises/problem-solving/ascii-digit-counter/exercise.json`; starter.py e solution.py referenciados; entrada `a12-3` retorna inteiro 3; ignora dígitos Unicode fora de ASCII.
- Entrevista `interview.allowed-tools`: `interviews/questions/interview.allowed-tools.json`; resposta esperada, explicação, follow-ups e rubrica; respeitar restrições de IA/ferramentas.
- Simulado `mock.junior-30`: `interviews/mocks/mock.junior-30.json`; 30 minutos, quatro perguntas indexadas, `problem-solving.label-counts`, rubrica de autoavaliação de 100 pontos.

## 6. Correção determinística

Usar scripts/assessment_grading.py confiável como referência de comportamento, não código do snapshot. Quiz multiple_choice/error_identification aceita string de ID de alternativa conhecida; true_false aceita booleano real; output_prediction/objective_code_completion aceita string dos valores explícitos. Comparação exact ou normalize_lf (somente CRLF/CR para LF), sem trim/case folding implícitos, sem eval. Tipos inválidos/IDs desconhecidos geram erro de validação; distinguir inválido de incorreto. XP indicativo. Exercícios chamam função declarada com cópias profundas independentes de args JSON e comparam retorno recursivamente por tipo/valor exato (bool, int, float distintos, chaves string); preservar entradas finais, rejeitar stdout/stderr e exceções, impedir alias de containers de entrada aninhados se new_container true. Não avalia automaticamente complexidade/refatoração ou mutação transitória; timeout declarado não é imposto pelo corretor de fixtures confiáveis. Usar parser JSON estrito sem perda, preservando distinção entre inteiro e float (ex. 9007199254740993 e 2432902008176640000), rejeitar chaves duplicadas/não finitos e não arredondar via JavaScript Number. Entrevistas/simulados abertos usam respostas de referência e rubricas de autoavaliação; sem correção semântica automática. Testes/soluções públicos são inspecionáveis; revelar sob demanda não é sigilo.

## 7. Execução e compatibilidade de navegador

30 exercícios não verificados para navegador, sem dependências externas permitidas; local_python 3.13. 114 capítulos unverified, File Organizer local_only com motivo localizado. Não promover status nem executar automaticamente conteúdo unverified/local_only. ADR 0003 escolhe Pyodide fixado + Web Worker como direção do site futuro, não implementação verificada. Antes de habilitar exercício individual, testar versão, compatibilidade, correção determinística, limites de tempo/saída, cancelamento e recriação de worker; avaliar memória, filesystem, armazenamento, rede e exposição de credenciais com isolamento de origem quando necessário. Worker não é fronteira de segurança. Manter instruções locais. Comportamento de navegador/SO/plataforma/rede não comprovado por fixtures Linux ou testes File Organizer Windows.

## 8. Importação, validação de candidato e rollback

Usar banco de objetos Git confiável (histórico completo, sem objetos substitutos), checkout de tooling confiável independente e seus cinco schemas fora do snapshot. Instalar requirements-assessment.txt confiável (jsonschema 4.26.0 nesta revisão). Obter commit aprovado uma vez no build e verificar SHA completo. Copiar JSON estrito abaixo para lock fora do snapshot. Arquivo idêntico tests/fixtures/learning-hub/handoff-lock.json pertence ao tooling 09B, não ao snapshot 09A nem à configuração ativa do site; consumidor deve aprovar/armazenar seu lock independentemente. tests/fixtures/learning-hub/consumer-lock.json histórico fixa 08C e permanece intacto.

```json
{
  "lock_version": "1.0.0",
  "revision": "03e91ff9952f2b02293f16a11260d166eb00ea8a",
  "versions": {
    "manifest": "1.0.0",
    "quizzes": "1.0.0",
    "exercises": "1.0.0",
    "interviews": "0.1.0",
    "mocks": "0.1.0"
  }
}
```

```bash
# From the independently trusted tooling checkout (Python 3.13).
python -m pip install -r requirements-assessment.txt
python scripts/curriculum_consumer.py --repository /path/to/trusted-source-git --lock /path/to/external/handoff-lock.json
```

Comando é validador de referência (Git archive e staging temporário isolado; sem deploy persistente). Caminhos são placeholders a substituir, não diretórios reais. Não executar scripts do conteúdo exportado. Validador verifica cada arquivo/diretório regular rastreado, confinamento, cobertura exata de árvore/blob Git, bytes de schemas confiáveis, versões, JSON estrito, IDs/navegação únicos e relacionamentos completos. Rejeitar arquivos ausentes/extras/modificados, symlinks/submodules, SHA desconhecido/abreviado, versões não suportadas e associações incompletas. Novo test_ac09_handoff_content_pin em tests/test_curriculum_acceptance.py copia lock para fora do snapshot, valida 09A exata, compara manifesto/caminhos/bytes canônicos à fixture histórica aprovada e registra evidência no CI. Execução no PR pendente na autoria. Identidade Git não é assinatura; banco Git confiável e staging isolado são premissas, não proteção concorrente de filesystem. Só selecionar candidato ativo após aprovação da validação; em falha manter pin e conteúdo anteriores, registrar motivo e falhar build sem publicação parcial. Rollback: selecionar SHA completo + versões anteriores válidas, repetir validação/build e publicar com deploy atômico controlado pelo consumidor. Rollback sintético local comprovado antes; deploy/rollback atômico real não testado.

## 9. Evidências, aceite e limites

CI push exato da 09A passou ambos jobs: 180 unittest de qualidade, sete unittest de engenharia, 406 testes práticos aprovados/um skipped, Windows 63/17 skipped, 210 exemplos, 9.282 links internos em 583 Markdown, 345 documentos de navegação. Windows sobrepõe Linux; não somar. Codex 09A sem findings, auditoria final registrada. 09B exige novo CI no HEAD exato com teste de pin, Codex sem findings não resolvidos, auditoria final distinta, autorização explícita de squash e CI de push exato. Sem AC-09 concluído antes dos gates. QA mapeia AC-00–09, PRs prévios e limites de revisão: amostra de 42 documentos localizados, 314 blocos Python por idioma e quatro registros, não auditoria semântica/humana exaustiva. Execução local indisponível por acesso ao GitHub do container; sem certificação integral de links externos, segredos no conteúdo/histórico, instalações em plataformas ou navegador/segurança. Sem infra paga, runtime ou site externo implementado. Publicação/links entre guias requerem aprovação separada.

[Final QA](final-qa.pt-BR.md) · [AC](acceptance-criteria.pt-BR.md) · [Tasks](tasks.pt-BR.md)

## 10. Checklist de implementação do consumidor

- [ ] Verificar SHA exato aprovado, versões do lock, confiança independente em validador/schemas; falhar de forma fechada antes de renderizar.
- [ ] Importar apenas dados canônicos indicados pelo manifesto/índices a partir do snapshot validado; preservar idiomas, IDs, links, assets e acessibilidade.
- [ ] Implementar UI de correção determinística sem perda numérica ou coerção implícita; entrevistas/simulados por autoavaliação.
- [ ] Manter execução unverified/local_only desabilitada até verificações por exercício de runtime/isolamento; preservar prática manual/local.
- [ ] Guardar progresso local por ID estável e versão/revisão; tratar migração/reset explicitamente; sem sincronização de conta presumida.
- [ ] Validar atualizações antes de trocar conteúdo ativo, reter lock anterior e provar rollback no ambiente de deploy; nunca buscar por visitante.
- [ ] Revisar renderizador seguro, licença/autoria, pin de dependências/runtime, testes, navegadores e limites operacionais no projeto separado do site.
- [ ] Obter revisão final do PR/aprovação do mantenedor e CI pós-merge; registrar revisão documental do handoff separada do pin de conteúdo.
