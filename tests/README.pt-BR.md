# Testes

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

Este diretório já contém testes de regressão das ferramentas de qualidade do repositório sem dependências externas. GitHub Actions os executa com:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Os testes protegem o processamento de links Markdown e a validação da estrutura, incluindo metadados de recursos visuais, acessibilidade SVG e referências locais seguras.

A documentação histórica previa conteúdo educacional de testes, começando com assertions simples e depois introduzindo `pytest` para exemplos executáveis e projetos práticos.

Os testes de regressão de navegação exigem a mesma ordem da trilha principal nos três idiomas, links exatos de anterior/índice/próximo no início e no final, transições entre módulos e cobertura dos READMEs versionados de capítulos/projetos. Execute `python scripts/check_chapter_navigation.py` na raiz do repositório para verificar todo o currículo.
