# Git e fundamentos do controle de versão

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../05-packages-and-dependencies/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../fundamentals/01-how-python-runs-a-program/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Nível:** iniciante absoluto. **Tempo estimado:** 30–45 minutos, sem contar instalação e configuração da conta. Use um projeto pessoal de prática, não um repositório de trabalho. Ao final, você consegue registrar e inspecionar uma versão do código Python e entender como sincronizá-la com um repositório remoto.

Git é uma ferramenta de controle de versão. Registra versões (commits) dos arquivos selecionados para inspecionar mudanças e colaborar. GitHub e GitLab hospedam repositórios Git e oferecem ferramentas de colaboração. Git funciona localmente sem conta ou internet. Uma conta remota é necessária somente para o exercício opcional de publicação.

## 1. Instale e configure Git

Use a [página oficial de instalação do Git](https://git-scm.com/install/). No Windows, instale Git for Windows e reabra PowerShell ou VS Code. No macOS, siga as opções documentadas, incluindo as ferramentas de linha de comando Xcode quando aplicável. No Linux, use o gerenciador de pacotes oficial da distribuição.

```shell
git --version
```

No terminal, abra a pasta python-practice existente. Confira a pasta atual com Get-Location (PowerShell) ou pwd (macOS/Linux). Execute primeiro git status. Se já pertencer a um repositório, use outra pasta de prática fora dele; não crie acidentalmente um repositório aninhado. Se Git informar que a pasta não é um repositório, inicialize:

```shell
git init -b main
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

Substitua a identidade ilustrativa pelo nome desejado nos commits e e-mail apropriado (um endereço no-reply verificado pelo provedor é uma opção). Esses comandos de configuração afetam apenas este repositório. Nomes e e-mails dos commits ficam no histórico; evite expor dados pessoais. Se sua versão de Git não reconhecer -b, atualize-a pelas instruções oficiais.

## 2. Decida o que deve ser versionado

Crie um arquivo de texto simples chamado .gitignore na raiz do projeto (sem extensão .txt), contendo:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

Esses padrões excluem ambientes gerados, caches Python e um arquivo comum de configuração local. Não protegem arquivos já rastreados nem removem segredos do histórico. Revise cada alteração; nunca versione credenciais, dados privados ou um .env real.

Mantenha first_program.py, .gitignore e requirements.txt revisado do capítulo 05. Não versione .venv. Se requirements.txt contiver URLs privadas ou caminhos locais, corrija antes de selecionar o arquivo.

## 3. Registre o primeiro commit

Execute git status para inspecionar os arquivos. Selecione apenas os arquivos desejados pelo nome:

```shell
git add .gitignore first_program.py requirements.txt
git diff --cached
git status
git commit -m "feat: add first Python program"
git log --oneline
```

Se pulou o exercício opcional de dependências, crie um requirements.txt revisado contendo apenas as dependências realmente necessárias (um arquivo vazio serve para o primeiro programa). Um arquivo em staging está selecionado para o próximo commit. O commit registra uma versão e mensagem localmente. Nada foi enviado.

Altere a mensagem de first_program.py, salve e execute com o interpretador verificado do ambiente. Depois inspecione e faça o commit:

```shell
git diff
git add first_program.py
git diff --cached
git commit -m "feat: update greeting"
git log --oneline
git status
```

Você deve ver dois commits e, se não houver outras alterações, uma área de trabalho limpa. git diff mostra mudanças não selecionadas; git diff --cached mostra mudanças selecionadas; git log mostra o histórico. Se o resultado for diferente, inspecione status em vez de repetir comandos às cegas.

## 4. Entenda remotos (prática opcional)

Um remoto é uma conexão nomeada com outro repositório. GitHub e GitLab têm interfaces web diferentes, mas usam os mesmos comandos básicos Git. Se quiser publicar, crie um repositório vazio no provedor escolhido, sem README, licença ou .gitignore inicial. Prefira um repositório privado de prática, confira visibilidade e conteúdo e siga a orientação de autenticação do provedor. Nunca coloque senhas ou tokens de acesso em URLs de remotos ou commits.

Copie a URL HTTPS de clone do seu próprio repositório. Substitua o marcador abaixo antes de executar:

```shell
git remote add origin YOUR_REPOSITORY_HTTPS_URL
git remote -v
git push -u origin main
```

Se origin já existir, inspecione em vez de sobrescrever. O primeiro push envia commits locais e configura a branch upstream. A autenticação pode abrir navegador ou gerenciador de credenciais. Se o remoto já tiver histórico ou o push for rejeitado, pare e investigue; não force o push.

Para atualizações seguintes, confirme primeiro que git status está limpo e você está na branch desejada. Neste repositório simples de prática com uma única branch:

```shell
git pull --ff-only
git log --oneline
```

pull obtém commits remotos e os integra; --ff-only recusa criar merge quando os históricos divergiram. Se recusar, pare e peça ajuda em vez de resetar ou sobrescrever trabalho. Após novo commit local revisado, git push o publica. git clone copia um repositório remoto existente para outra pasta; execute fora do repositório original:

```shell
git clone YOUR_REPOSITORY_HTTPS_URL python-practice-copy
```

Recrie o ambiente virtual a partir de requirements.txt na cópia usando os capítulos 04–05; Git não transfere a .venv ignorada.

## 5. O fluxo profissional, em resumo

Em projeto compartilhado, uma branch isola uma alteração, um pull request (GitHub) ou merge request (GitLab) propõe a alteração, a revisão a verifica e CI executa verificações automáticas. Merge integra alterações aprovadas. Não envie diretamente para a main protegida de projeto compartilhado. O material posterior de práticas de engenharia aplicará essas ideias a Python. Branches em profundidade, conflitos, recuperação de histórico, GitHub Actions, GitLab CI e colaboração pertencem ao futuro Git Study Guide independente; nenhum curso externo é exigido aqui.

## Prática e referência rápida

- [ ] Verificar Git e configurar repositório de prática.
- [ ] Criar .gitignore e confirmar que .venv não foi selecionada.
- [ ] Revisar e versionar o primeiro programa, modificá-lo e fazer novo commit.
- [ ] Inspecionar os dois commits e explicar diferença entre commit local e push remoto.
- [ ] Opcionalmente publicar no próprio repositório vazio de prática e cloná-lo em outra pasta.

Se um comando falhar, leia a mensagem, confira a pasta atual, verifique git status e consulte a documentação oficial. Não use reset destrutivo, force-push nem alternativas inseguras de credenciais.

## Referências oficiais

- [Instalação Git](https://git-scm.com/install/)
- [Fundamentos Git: registro de alterações](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [Repositórios remotos Git](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Autenticação GitHub](https://docs.github.com/en/authentication)
- [Autenticação GitLab](https://docs.gitlab.com/user/gitlab_com/#authentication)

<!-- chapter-navigation:bottom -->
[← Anterior](../05-packages-and-dependencies/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../fundamentals/01-how-python-runs-a-program/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
