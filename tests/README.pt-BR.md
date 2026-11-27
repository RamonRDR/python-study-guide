# Testes

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

Este diretório contém testes de regressão das ferramentas de qualidade do repositório, incluindo o contrato de avaliações. Instale `requirements-assessment.txt` em ambiente virtual antes da suíte. GitHub Actions a executa com:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Os testes protegem o processamento de links Markdown e a validação da estrutura, incluindo metadados de recursos visuais, acessibilidade SVG e referências locais seguras.

A documentação histórica previa conteúdo educacional de testes, começando com assertions simples e depois introduzindo `pytest` para exemplos executáveis e projetos práticos.

Os testes de regressão de navegação exigem a mesma ordem da trilha principal nos três idiomas, links exatos de anterior/índice/próximo no início e no final, transições entre módulos e cobertura dos READMEs versionados de capítulos/projetos. Execute `python scripts/check_chapter_navigation.py` na raiz do repositório para verificar todo o currículo.

Os testes de fundamentos exigem alocação aprovada por aula/dificuldade, cobertura exata do índice e correção determinística; executam fixtures literais confiáveis, nunca código arbitrário carregado dos registros. Regressões do piloto continuam cobertas.

A suíte de expansão verifica a matriz completa de 160 questões, 2.850 XP, 82 novos fixtures de respostas, fixtures literais de código confiáveis, diversidade de tipos e os três índices localizados. Regressões de fundamentos e piloto permanecem ativas; nenhum código do aluno é executado.

A suíte de migração verifica o índice completo de 30 registros, os 192 casos existentes, flags explícitos de ausência de alias, inteiros grandes exatos, modalidades, metadados de tempo e referências/candidatos incorretos confiáveis. O índice histórico de 29 entradas e sua suíte de regressão permanecem intactos. Runtime de navegador e aplicação de timeout não são testados aqui.

Os testes consolidados AC-07 verificam em conjunto os dois índices canônicos, 190 IDs únicos, 160 fixtures independentes de respostas corretas/incorretas de quiz, inventário de código Python compartilhado e rejeição de registros inválidos nos dois carregadores. Suítes anteriores de discriminação de exercícios confiáveis, fixtures e regressão permanecem ativas. Veja [evidências AC-07](../docs/specs/learning-hub-foundation/acceptance-criteria.pt-BR.md).

Sprint 08A adiciona [test_curriculum_manifest.py](test_curriculum_manifest.py). Aceite da Sprint 08A: schema Draft 2020-12 e validação estrutural/de caminhos estrita com fixtures sintéticas positivas e negativas, incluindo versões independentes dos bancos, caminhos localizados, metadados de execução e JSON inválido. Inventário e navegação (B), relações dos bancos (C), consumidor fixado (D) e aceite consolidado (E) permanecem pendentes. Validador estrutural sozinho não certifica snapshot publicado. CI e review no head exato são obrigatórios; nenhum novo resultado de teste é alegado aqui.

Sprint 08B adiciona [test_curriculum_inventory.py](test_curriculum_inventory.py). Testes verificam inventário rastreado completo, IDs históricos, ordem, navegação, títulos localizados, assets, recursos, metadados de dependências e rejeição de violações das associações pendentes. CI também executa CLI de inventário de autoria. Sem alegação de teste de revisão do consumidor ou execução no navegador.

Sprint 08C adiciona [test_curriculum_relationships.py](test_curriculum_relationships.py). Testes exigem associações canônicas completas, JSON estrito e versões exatas; casos negativos cobrem vínculos ausentes, duplicados, deslocados e inventados e ordem dos simulados. Inventário pendente permanece fixture histórica; gate de inventário publicado exige relacionamentos completos. Sem prova de revisão do consumidor ou runtime do navegador.
