# Critérios de aceite

[🇺🇸 English](acceptance-criteria.md) · [🇧🇷 Português](acceptance-criteria.pt-BR.md) · [🇪🇸 Español](acceptance-criteria.es.md)

Status: proposta para revisão. Critérios são requisitos, não resultados.

| ID | Sprint | Condição de aceite |
| --- | --- | --- |
| AC-00 | 00 | Especificação, constituição, plano, tarefas, critérios, contrato preliminar, ADRs e estrutura de handoff existem nos três idiomas; AGENTS referencia os documentos; conteúdo educacional existente preservado; CI, paridade estrutural e evidências de revisão registrados; aprovação antes do merge. |
| AC-01 | 01 | Cada idioma de capítulo/projeto tem anterior/índice/próximo corretos, exceto vizinhos ausentes nos extremos; links resolvem no mesmo idioma, fronteiras recíprocas; testes rejeitam destinos incorretos e links ausentes. |
| AC-02 | 02 | Onboarding localizado cobre FR-02; downloads oficiais e comandos por SO verificados; estudante consegue instalar, selecionar interpretador, criar e executar arquivo; sem renumeração; navegação inclui módulo. As seis aulas explicam isolamento local ao projeto, ativação/execução direta, verificação de interpretador e pip, .gitignore, instalação e recriação de dependências com requirements.txt; o panorama vincula os quatro capítulos existentes e identifica candidatos futuros, incluindo instalação separada de navegadores Playwright. Verificar instruções em fontes oficiais e declarar plataformas/etapas de rede não testadas. A sexta aula inclui exercício local seguro com dois commits, staging explícito, exclusões, sincronização remota opcional e breve fluxo profissional. Referências futuras entre guias são mapeadas sem links a destinos não publicados; Git avançado fica adiado. |
| AC-03 | 03 | Três READMEs, índices e estrutura afetados condizem com caminhos/status reais; banner/licença preservados; cada badge numérico identifica evidência genuína, sem somar suítes sobrepostas. |
| AC-04 | 04 | Orientação trilíngue de prática manual e SDD/TDD inclui exemplos originais, requisitos/aceite explícitos e prática independente; distingue estudo de manutenção por IA. |
| AC-05 | 05 | Desafios cobrem FR-05 em dificuldade adequada; cada um tem ID estável, enunciado localizado, tempo, conceitos, restrições, exemplos, código inicial, dicas progressivas, referência, explicação, complexidade, testes e casos de borda quando relevantes; testes locais passam e detectam soluções incorretas representativas. Um mapa documentado cobre os pré-requisitos de todos os tópicos FR-05; conceitos ausentes (incluindo recursão, busca/ordenação e complexidade de algoritmos) são ensinados em EN/PT-BR/ES e vinculados antes da publicação dos desafios piloto ou expandidos correspondentes. A revisão verifica esse critério por desafio; nenhum desafio pode depender de conceitos não ensinados. |
| AC-06 | 06 | Tópicos FR-06 com pré-requisitos documentados; perguntas incluem respostas esperadas, explicação, objetivo, erros comuns, complementares e exemplos; simulações 30/45/60 com rubricas explícitas; sem entrevistador IA ou alegação de avaliação semântica automática. |
| AC-07 | 07 | Registros válidos de tipos suportados; schema inválido, ID duplicado, idioma ausente, resposta inválida ou referência órfã falham na validação; correção determinística e testes de soluções incorretas passam; sem duplicação Python por idioma. |
| AC-08 | 08 | Manifesto fornece ordem estável, caminhos, idiomas, títulos, relações, associações e compatibilidade; validadores rejeitam caminhos inseguros, conteúdo ausente e versões não suportadas; fixture do consumidor resolve revisão imutável sem scraping HTML. |
| AC-09 | 09 | Verificações aplicáveis aprovadas na revisão aprovada; paridade revisada; limitações e verificações não executadas informadas; handoff inclui contrato, caminhos, schemas, exemplos, correção, ADRs, pendências e evidências; Codex Review final e aprovação. |

## Definition of Done global

Toda documentação pública nova ou alterada deve estar disponível nos três idiomas, com equivalência conceitual. Links e testes verificados; sem regressões conhecidas, findings relevantes pendentes, credenciais ou dados privados; documentação e tarefas atualizadas; mantenedor aprova merge. Se validação não puder ser executada, registrar motivo em vez de aprovar. Revisão semântica é humana; verificação estrutural não garante equivalência.
