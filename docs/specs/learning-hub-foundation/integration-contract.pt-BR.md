# Contrato de integração do Learning Hub

[🇺🇸 English](integration-contract.md) · [🇧🇷 Português](integration-contract.pt-BR.md) · [🇪🇸 Español](integration-contract.es.md)

Status: preliminar para manifesto do consumidor e fixtures de integração na Sprint 08. Os schemas e registros versionados de avaliação seguem o [contrato de avaliações](assessment-contract.pt-BR.md). Não há integração de runtime implementada aqui.

## Versão e transporte

O repositório público é oficial. O consumidor importa conteúdo no build usando SHA de commit Git imutável aprovado (tag pode identificar SHA). Registra revisão e schema_version, rejeita versões major não suportadas e falha no build com dados inválidos em vez de misturar revisões silenciosamente. JSON e Markdown UTF-8, sem scraping HTML GitHub. Sem chamadas à API por visitante ou serviços pagos.

## Convenções compartilhadas

- Locales: en (padrão), pt-BR, es. Campos visíveis ao estudante exigem três traduções; arquivos Python e IDs compartilhados em inglês.
- IDs: strings ASCII minúsculas com pontos/hífens; estáveis, independentes de título/ordem; nunca reutilizar ID para item diferente. Unicidade por tipo, referências tipadas por campo.
- Caminhos POSIX relativos ao repositório; sem absolutos, travessia, barras invertidas, esquemas URL ou escape via symlink. Verificar existência/confinamento antes da importação. Renderizar Markdown/HTML com segurança, resolver links/recursos na mesma revisão e sanitizar conteúdo não confiável.
- Ordens: inteiros não negativos explícitos, únicos entre irmãos; anterior/próximo segue ordem curricular, não lexicográfica. Extremos com vizinhos null.
- Metadados opcionais com padrões explícitos documentados; não presumir capacidade não suportada.

## Modelo preliminar de registros

| Entidade | Campos obrigatórios no piloto |
| --- | --- |
| Currículo | schema_version, default_locale, supported_locales, modules |
| Módulo | id, order, slug, title (mapa de idiomas), index (mapa de caminhos por idioma), chapters |
| Capítulo | id, order, slug, title, content (mapa de caminhos por idioma), assets, previous_id, next_id, exercise_ids, quiz_ids, interview_ids, execution |
| Quiz | id, chapter_id, difficulty, type, prompt (mapa de idiomas), choices (IDs estáveis e texto traduzido quando aplicável), answer, explanation, hints, xp |
| Exercício | id, chapter_id, difficulty, estimated_minutes, title, prompt, concepts, constraints, examples, starter_path ou texto inicial, hints, solution_path, explanation, complexity (tempo/espaço quando significativo), tests, execution, allowed_dependencies |
| Pergunta de entrevista | id, topic, level, prompt, expected_answer, explanation, intent, common_errors, follow_ups, examples, rubric |
| Simulação | id, level, duration_minutes (30/45/60), question_ids, exercise_ids, rubrica de pontuação |

Campos localizados incluem explicações visíveis, alternativas, exemplos com prosa, dicas, descrições de pontuação e rubricas. Usar IDs para referências internas quando possível. Tipos: multiple_choice, true_false, error_identification, output_prediction, objective_code_completion. Dificuldade: easy/medium/hard. Respostas usam IDs estáveis de alternativas, booleanos ou strings aceitas explícitas conforme tipo. XP é inteiro não negativo, indicativo, não certificação.

## Exemplo (ilustrativo, não manifesto publicado)

```json
{
  "id": "fundamentals.print-and-input",
  "order": 2,
  "slug": "print-and-input",
  "content": {
    "en": "fundamentals/02-print-and-input/README.md",
    "pt-BR": "fundamentals/02-print-and-input/README.pt-BR.md",
    "es": "fundamentals/02-print-and-input/README.es.md"
  },
  "previous_id": "fundamentals.how-python-runs-a-program",
  "next_id": "fundamentals.variables-and-naming",
  "execution": "unverified"
}
```

O fragmento omite outros metadados obrigatórios e não é registro completo válido por schema. Caminhos existentes; IDs propostos.

## Correção e execução

Correção de quizzes determinística. Comparar valores canônicos exatos por padrão; normalizar quebras de linha ou espaços somente quando a pergunta permite explicitamente. Testes de código declaram interface de chamada de função ou stdin/stdout, entradas/saídas JSON-compatíveis, regras de comparação (tolerância apenas quando especificada), casos de borda e limites de execução. Validar poder discriminatório com soluções de referência e incorretas representativas. Não executar código arbitrário do estudante no CI do repositório.

Valores execution: browser_compatible (verificado em runtime fixado), local_only (documentar motivo), unverified (padrão; sem execução automática no navegador). Python local e dependências permitidas explícitos. Compatibilidade por exercício, não inferida de todo código do capítulo. Arquivos, rede, bibliotecas externas e exemplos específicos de SO requerem avaliação individual.

Consumidor: executar código fora da thread de UI em Web Worker dedicado; limitar tempo e saída, terminar/recriar em timeout ou cancelamento, evitar exposição de credenciais privilegiadas e isolar da origem principal quando necessário. Worker sozinho não é fronteira de segurança; avaliar acesso à rede/armazenamento e sandbox antes do deploy. Sem alegar isolamento rígido de memória. Testar versão e suporte do navegador no projeto do site. Sem execução em servidor nesta fase.

Soluções e testes públicos são inspecionáveis; revelar dicas/soluções sob demanda, não como garantia de segurança. Perguntas abertas usam referências e rubricas de autoavaliação, nunca correção semântica automática.

## Responsabilidades

Guia: Markdown, metadados, exemplos, soluções, testes, rubricas e validação de schema. Site: renderizador seguro, editor, runtime, UI de correção determinística, progresso local, acessibilidade e deploy. Armazenamento local é específico do dispositivo e pode ser apagado; sem sincronização backend presumida.

## Decisões pendentes

Finalizar layout, schemas completos, política de versões, semântica exata de pontuação/comparação, renderização segura e runtime fixado após pilotos. Documentar compatibilidade e exemplos de migração no handoff final. Ver [ADRs](../../adr/README.pt-BR.md).

## Sprint 08A · Manifesto curricular 1.0.0

As decisões específicas do manifesto abaixo substituem o modelo preliminar acima; contratos dos bancos permanecem inalterados.

Publicar `curriculum/manifest.json` com `schemas/curriculum-manifest.schema.json` (Draft 2020-12, versão 1.0.0 do manifesto). Reutilizar a dependência jsonschema e os auxiliares estritos de JSON/caminhos das avaliações. O manifesto referencia arquivos fonte, sem duplicar aulas ou avaliações. Os 115 IDs estáveis vêm da matriz de avaliações; ordem e títulos vêm das três trilhas. Preservar a fundação histórica separada da ordem curricular 00, fases educacionais 1–12 e módulo complementar. As ordens de módulos e capítulos são inteiros a partir de zero, contíguos entre irmãos e independentes dos IDs; previous/next atravessa todo o currículo.

O manifesto inclui títulos localizados, caminhos de índice/conteúdo, tipo de capítulo, recursos e assets, metadados de execução, referências tipadas de avaliação e descritores dos bancos canônicos. Os quatro bancos mantêm versões independentes: quiz/exercício 1.0.0, entrevista/simulado 0.1.0. Referências de entrevistas nos capítulos indicam pré-requisitos documentados, não propriedade; referências de simulados indicam a aula de simulados. Quiz/exercício usa chapter_id existente. Sem associações pedagógicas inferidas. Execução do capítulo é unverified ou local_only com motivo localizado; browser_compatible exige evidência real em runtime fixado no nível do exercício. Metadados opcionais de Python local/dependências significam não especificado quando ausentes, não irrestrito.

Manifesto com association_status pending é artefato de desenvolvimento; consumidores exigem complete e validação referencial integral. A valida schema e arquivos confinados com fixtures sintéticas; B publica inventário com associações pendentes; C completa e valida associações; D demonstra consumo por revisão fixada; E encerra AC-08. Versões suportadas são explícitas (inicialmente exatas); dados desconhecidos ou incompatíveis falham explicitamente. Preservar tokens inteiros, rejeitar chaves duplicadas e números não finitos, sem arredondamento JavaScript. Consumidores registram SHA completo aprovado e versões suportadas fora do snapshot; verificam o commit e importam somente seus arquivos. Nunca inserir o próprio SHA ou consultar por estudante. Guias relacionados são opcionais e adiados até verificação. Sem implementação de site ou runtime aqui.

[ADR 0004](../../adr/0004-curriculum-manifest.pt-BR.md).

## Sprint 08B · Inventário curricular

08B publica o primeiro inventário curricular completo: 14 módulos, 107 aulas e oito projetos práticos, 115 IDs estáveis e 345 caminhos de conteúdo localizados. Ordem e títulos devem corresponder às três trilhas mestras (texto simples de exibição; remover somente delimitadores de código inline). Nomes dos módulos vêm dos títulos de seção localizados, sem prefixos de fase/status. Preservar IDs da matriz como baseline revisado, incluindo as três exceções históricas de problem-solving; matriz é evidência de planejamento, não entrada do consumidor. Usar ordens de módulos e capítulos contíguas a partir de zero, previous/next global explícito, metadados de fase distintos da ordem curricular e índices localizados canônicos. Verificar todos os caminhos e cobertura de capítulos rastreados. Inventário inclui cada arquivo rastreado não pertencente ao conteúdo sob cada capítulo como recurso, ou asset para extensões de imagem suportadas; assets globais são imagens rastreadas em assets/. Recursos são referências, não allowlist de execução. Caminhos opcionais de dependências são declarados nas quatro aulas de bibliotecas externas usando o arquivo compartilhado existente; File Organizer é local_only por exercitar comportamento de sistema de arquivos específico de plataforma. Demais capítulos são unverified, sem alegação de compatibilidade no navegador. B exige association_status pending e listas tipadas de associações vazias; C preencherá e validará as relações. CI verifica o manifesto versionado real e fixtures negativas de regressão; usar arquivos rastreados pelo Git no inventário de autoria, não caches não rastreados ou API de runtime do consumidor. Sem duplicar fonte, novas dependências ou site.

## Sprint 08C · Relacionamentos de avaliações

08C completa listas de associações tipadas na ordem dos índices canônicos. Cada quiz/exercício pertence exatamente ao chapter_id existente; interview_ids em um capítulo são referências reversas a perguntas cujos caminhos localizados de pré-requisitos documentados identificam esse capítulo, não propriedade. mock_ids pertencem exclusivamente à aula de simulados; cada simulado deve referenciar perguntas indexadas e exercício canônico indexado, preservando ordem e dificuldade existentes. Todos os 253 registros únicos dos bancos devem estar representados, sem associações ausentes, duplicadas, deslocadas, inventadas ou pendentes. Ler os quatro índices e registros com JSON estrito (rejeitar chaves duplicadas e números não finitos, preservar inteiros exatos); verificar versões declaradas, caminhos canônicos, cobertura dos índices e validadores existentes, inclusive caminhos/títulos de pré-requisitos e metadados de execução. Índices de entrevistas/simulados permanecem preliminares 0.1.0; nenhum schema novo de registro é implicado. Sem alterar corpos dos bancos ou índice legado. Manter verificações estruturais e de inventário de autoria; gate completo rejeita relações pendentes ou parciais. Gerar listas de associações deterministicamente a partir dos bancos validados e comparar manifesto versionado, não somente saída gerada. Sem promover compatibilidade de navegador, site, runtime, nova dependência ou alegação de revisão de consumidor; D estabelece consumo imutável.

## Sprint 08D · Fixtures imutáveis do consumidor

08D fornece uma fixture de referência do consumidor, não o site. Um lock JSON estrito externo fixa o SHA completo de 40 caracteres e versões exatas suportadas do manifesto/bancos. Implementação confiável do consumidor e seus cinco schemas confiáveis ficam fora do snapshot exportado. Resolver somente objeto commit completo existente em banco de objetos Git local confiável, com objetos de substituição desabilitados. Exportar árvore rastreada para staging isolado, sem filtros de checkout, symlinks ou submódulos; rejeitar caminhos inseguros, entradas não regulares, arquivos ausentes/extras e hashes de blobs Git divergentes. Verificar toda árvore preparada contra commit fixado, inclusive bytes dos schemas contra schemas confiáveis. Não carregar ou executar código do snapshot. Usar JSON estrito, validadores estruturais/de bancos confiáveis existentes e checagens independentes de ordem de módulos/capítulos, IDs únicos e navegação global, sem matriz de autoria ou parsing das trilhas. Validar candidato antes de mudar pin ativo; manter pin aprovado anterior se validação falhar e demonstrar rollback selecionando-o novamente. Testes cobrem revisão 08C aprovada real, rejeição da 08B pendente, revisões desconhecidas/abreviadas, arquivos misturados/modificados/ausentes/extras, symlinks, divergência de schema e versões exatas, atualização/rollback sintéticos válidos. Confiança no banco de objetos Git e staging isolado são premissas; sem verificação de assinatura, sandbox contra concorrência no filesystem, runtime de navegador, publicação ou site. CI obtém histórico uma vez no build, não por visitante. AC-08 permanece aberto até E.
