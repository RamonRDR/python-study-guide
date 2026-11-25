# Instruções do repositório

[🇺🇸 English](../../AGENTS.md) · [🇧🇷 Português](AGENTS.pt-BR.md) · [🇪🇸 Español](AGENTS.es.md)

## Finalidade do projeto

Python Study Guide é um projeto educacional independente, público, colaborativo e multilíngue. Seu objetivo é ajudar pessoas a estudar Python, entender como seus conceitos se conectam e praticar com exemplos claros, precisos, originais e executáveis. Presuma que alguns leitores não têm experiência em programação. Explique termos necessários, evite saltos sem explicação e não confunda brevidade com clareza.

## Responsabilidade pelo projeto

Python Study Guide foi criado e é mantido por [Ramon Estevez Rodriguez](https://github.com/RamonRDR). Preserve registros de autoria e licença. Não remova, sobrescreva nem deturpe créditos de colaboradores em metadados de commits, histórico Git ou PRs. Consulte [AUTHORS](AUTHORS.pt-BR.md).

## Ordem de prioridades

1. Precisão técnica
2. Clareza educacional
3. Privacidade e segurança
4. Consistência entre idiomas
5. Manutenibilidade
6. Velocidade de entrega

Não sacrifique precisão, verificação ou clareza para terminar rápido. Velocidade só ganha prioridade se o mantenedor solicitar resultado rápido ou provisório; informações confidenciais, alegações inventadas e mudanças sem revisão continuam inaceitáveis.

## Idiomas

A documentação é mantida em inglês, português brasileiro e espanhol. Inglês é padrão para diretórios, arquivos, branches, identificadores, comentários de código e mensagens de commit. Traduções devem preservar significado técnico, exemplos, alertas, pré-requisitos, objetivos e links, sem exigir literalidade.

Toda documentação pública deste repositório, incluindo arquitetura, engenharia, governança e orientação a colaboradores, deve estar disponível e conceitualmente alinhada nos três idiomas. Atualize versões afetadas no mesmo PR; traduções ausentes bloqueiam conclusão. Notas realmente privadas ficam fora do repositório público, preferencialmente em inglês (português é permitido). Identificadores técnicos, arquivos, código, chaves JSON e valores enum permanecem inalterados entre idiomas.

## Conteúdo educacional

Capítulos devem explicar: o que é o conceito, por que existe, sintaxe, quando usar, quando evitar, conexões, exemplo básico, exemplo prático, erros comuns, exercício e referência rápida. Distinguir fatos verificáveis de recomendações ou convenções; não apresentar opinião como regra Python.

Preferir fontes primárias e oficiais: documentação Python, PEPs e documentação oficial de bibliotecas/produtos. Verificar documentação atual para informações mutáveis; evitar fixar preços, limites de planos, disponibilidade de versões e outros detalhes mutáveis, salvo documentos destinados a acompanhá-los.

## Exemplos, originalidade e privacidade

Usar apenas exemplos originais, genéricos, fictícios e não confidenciais. Nunca incluir, reproduzir, resumir ou adaptar:

- Informações privadas de empregadores/clientes ou processos internos de empresas.
- Material de projetos pessoais/familiares.
- Credenciais, segredos, tokens ou URLs privadas.
- Código proprietário, dados pessoais ou documentos confidenciais.
- Detalhes identificadores de conversas privadas ou arquivos enviados.
- Exemplos protegidos por direitos autorais sem permissão/licença adequada.

Trocar nome real por fictício não basta se regras, datas, papéis, sistemas ou fluxo identificarem a fonte. Crie exemplo independente.

## Qualidade do código

- Seguir PEP 8, identificadores descritivos em inglês e type hints quando melhorarem entendimento.
- Exemplos pequenos para estudo e realistas para uso; evitar dependências desnecessárias.
- Não depender de comportamento específico de versão sem identificar e verificar a versão Python.
- Comentar decisões, restrições e motivos não óbvios; não narrar código autoexplicativo.
- Executar ou validar exemplos sempre que possível; nunca alegar execução ou testes não realizados.

## Fluxo do repositório

- Nunca alterar main diretamente; criar branch focada a partir da main atual.
- PR com um propósito claro; branches e commits em inglês; evitar formatação/refatoração sem relação.
- Revisar todos os arquivos alterados antes de solicitar merge; tratar feedback antes de resolver conversa.
- Não contornar proteções; usar squash merge salvo alteração da configuração.

## Trabalho assistido por IA

IA pode apoiar pesquisa, planejamento, redação, tradução, explicação, geração de código, testes, revisão e manutenção. Resultado de IA é proposta, não autoridade; fluência, detalhes ou persuasão não bastam para aceitar.

Colaborador e mantenedor são responsáveis por entender o trabalho, verificar precisão técnica, fontes e links, revisar traduções, executar exemplos/testes relevantes, identificar informações sem suporte ou inventadas, proteger informações privadas/proprietárias e confirmar conformidade com licença e políticas.

Use IA para apoiar pensamento, não evitá-lo. Ao ensinar, prefira dicas, perguntas, comparações e explicações graduais quando ajudarem a compreensão. Declare incerteza e verifique; não invente fatos, testes, citações, arquivos ou comportamento.

## Checklist de conclusão

Confirmar propósito único; alegações técnicas precisas e com fontes adequadas; exemplos originais, genéricos e sem informações confidenciais; exemplos executáveis funcionam ou ausência de teste é declarada; documentação pública com três versões conceitualmente alinhadas; terminologia e links consistentes; nenhum arquivo sem relação alterado; discussões de review tratadas; resultado ensina em vez de apenas fornecer resposta.

## Phase II: desenvolvimento orientado a especificações

Antes de implementar, consultar [constituição](../specs/constitution.pt-BR.md), [especificação](../specs/learning-hub-foundation/specification.pt-BR.md), [plano](../specs/learning-hub-foundation/implementation-plan.pt-BR.md), [tarefas](../specs/learning-hub-foundation/tasks.pt-BR.md), [critérios](../specs/learning-hub-foundation/acceptance-criteria.pt-BR.md), [contrato](../specs/learning-hub-foundation/integration-contract.pt-BR.md) e [ADRs](../adr/README.pt-BR.md).

Manter especificações públicas e conteúdo educacional nos três idiomas. Preservar caminhos curriculares; separar numeração de sprints de ordem educacional. Não implementar Learning Hub externo aqui, contratar serviços pagos ou introduzir correção por IA. O repositório é fonte oficial.

Usar branches e PRs focados, solicitar Codex Review, resolver findings relevantes, declarar verificações não executadas e obter aprovação explícita antes de merge. Atualizar especificações e tarefas com evidências quando escopo/contratos mudarem. Propostas não autorizam implementação antes da aprovação.

## Auditoria final pré-merge (Final Pre-Merge Audit)

Após GitHub Actions aplicável e Codex Review aprovarem o head exato atual do PR, realize uma auditoria técnica distinta antes de pedir aprovação explícita do mantenedor para squash merge. É uma nova rodada de revisão, não alegação de revisor independente quando o mesmo contribuinte a realiza. Verifique escopo e critérios de aceitação, código e exemplos alterados, discriminação de testes e casos de borda, pré-requisitos de ensino, alinhamento semântico nos três idiomas, navegação, regressões, privacidade e restrições de segurança. Para riscos não verificáveis, registre limitação e impacto; não marque como aprovado. Registre no PR SHA auditado, execução do CI, evidência do Codex Review, verificações realizadas, findings e bloqueios pendentes. Se qualquer correção alterar o head, execute novamente CI aplicável e Codex Review, depois repita auditoria final nesse head. Sem aprovação ou merge baseado em auditoria desatualizada; reconfirme head e gates imediatamente antes do squash merge. O mantenedor conserva aprovação final; auditoria não substitui julgamento humano.
