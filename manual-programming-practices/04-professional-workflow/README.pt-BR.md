# Fluxo profissional de Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../03-test-driven-development/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Tempo estimado:** 35–50 minutos. Aplique as aulas anteriores a uma alteração Python pequena. Precisa de Git local, repositório de prática e interpretador verificado. Veja [Git básico](../../getting-started/06-git-and-version-control/README.pt-BR.md). Conta de hospedagem é opcional; não crie serviço pago nem use o repositório real do guia para experimentos.

## 1. Torne o trabalho revisável

Use seu próprio repositório local com baseline versionado. Salve requisitos, plano e ADR de progresso de leitura da aula SDD no repositório de prática. Se ainda não versionados, revise e faça commit no baseline antes de criar branch. Confira `git status` limpo. Crie branch focada:

```shell
git switch -c feat/reading-progress
```

Implemente e teste manualmente conforme aula anterior. Mantenha arquivos gerados e segredos fora do Git. Antes do commit, execute testes na pasta de prática:

```shell
python -m unittest discover -s . -p 'test_*.py' -v
git status
git diff
git add reading_progress.py test_reading_progress.py
git diff --cached
git commit -m "feat: calculate remaining reading pages"
```

Use arquivos reais que deseja alterar; inspecione staging primeiro. Se houver falha, investigue e execute novamente em vez de informar sucesso.

## 2. Escreva descrição revisável

Em nota local, prepare um pull request: propósito; requisitos R1–R4; resumo da implementação; evidências AC1–AC5; comandos e resultados reais; limitações; fora do escopo. Code review é exercício de raciocínio: compare código com especificação, confira limites, nomes, tratamento de erros, testes e privacidade. CI aprovado é necessário quando exigido, não garantia de correção.

## 3. Prática GitHub opcional

Somente se possui remoto de prática e entende sua visibilidade, envie branch com `git push -u origin feat/reading-progress`. Abra pull request para main de prática. No GitLab, a revisão equivalente é merge request. Nunca envie a repositório alheio sem permissão. Aprofundamento Git e plataformas pertence ao futuro Git Study Guide; esta aula exemplifica fluxo Python.

CI executa verificações configuradas sobre mudanças. Um workflow mínimo ilustrativo de GitHub Actions para esse repositório isolado pode ser salvo como .github/workflows/python-tests.yml **na branch de funcionalidade**:

```yaml
name: Python tests
on: [pull_request]
permissions:
  contents: read
jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.13"
      - run: python -m unittest discover -s . -p 'test_*.py' -v
```

É workflow mínimo ilustrativo, não instrução para substituir o [workflow existente](../../.github/workflows/quality-checks.yml) do guia. Pressupõe arquivos de teste na raiz de prática e ausência de dependências externas. Revise arquivo antes de adicionar e fazer commit separado; envie novamente. Confira disponibilidade e cotas de hospedagem antes de executar CI remoto; testes locais bastam ao exercício obrigatório. Não informe que o workflow ilustrativo rodou se não rodou. Revise resultados, trate feedback, execute testes novamente e faça merge apenas com aprovação. Se CI falhar ou histórico conflitar, pare e investigue; não contorne proteções. Sem remoto, simule review local com `git diff main...HEAD`; mantenha branch sem merge até revisão.

## 4. Trabalho independente e limites da IA

Primeiro resolva e explique sem implementação ou correção gerada por IA. Use docs oficiais, testes, depuração e feedback humano. Se usar IA para aprender, peça dica após tentativa genuína; verifique respostas e não compartilhe dados privados. O [guia de manutenção assistida por IA](../../docs/ai-assisted-development/README.pt-BR.md) separado explica como colaboradores podem usar ChatGPT/Codex com responsabilidade humana. Manutenção assistida não é prática independente do estudante.

## 5. Checklist de conclusão

- Requisito e critérios explícitos.
- Escrevi e entendi código; testes demonstram casos normais, limites e inválidos.
- Conferi diff, commit e resultados reais dos testes.
- Consigo explicar uma decisão e uma contrapartida.
- Feedback tratado; merge exige aprovação.
- Consigo reproduzir fluxo em outro problema pequeno.

**Referência rápida:** necessidade → spec → plano → branch → teste/código/refatoração → revisão do diff → commit → PR/CI opcionais → aprovação humana → merge. Para regras de contribuição, leia [CONTRIBUTING](../../docs/localized/CONTRIBUTING.pt-BR.md).

<!-- chapter-navigation:bottom -->
[← Anterior](../03-test-driven-development/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
