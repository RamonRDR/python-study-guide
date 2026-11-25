# Contrato de integração do Learning Hub

[🇺🇸 English](integration-contract.md) · [🇧🇷 Português](integration-contract.pt-BR.md) · [🇪🇸 Español](integration-contract.es.md)

Status: preliminar, direção normativa para pilotos; JSON Schema exato e fixtures finalizados nas Sprints 07–08. Não há integração de runtime implementada aqui.

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
