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
