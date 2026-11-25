# Ambientes virtuais

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../03-run-your-first-program/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../05-packages-and-dependencies/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Nível:** iniciante absoluto. **Tempo estimado:** 25–40 minutos. Conclua a aula do primeiro programa. Um ambiente virtual é um ambiente Python específico de um projeto. Normalmente mantém os pacotes externos instalados separados dos outros projetos. Não é máquina virtual, sandbox de segurança nem cópia independente do sistema operacional.

Imagine dois projetos que precisam de versões diferentes do mesmo pacote. Dê a cada um seu ambiente, em vez de alterar o Python do sistema:

```text
workspace/
├── project_a/
│   ├── .venv/
│   └── main.py
└── project_b/
    ├── .venv/
    └── main.py
```

## 1. Crie o ambiente dentro do projeto

Abra a pasta existente `python-practice` no VS Code ou terminal. Confira a pasta atual com `Get-Location` no PowerShell ou `pwd` no macOS/Linux. Crie **um** ambiente nela, usando o interpretador verificado no capítulo 01.

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
```

macOS (instalação oficial 3.13):

```bash
python3.13 -m venv .venv
```

Linux (ou outra instalação verificada no macOS):

```bash
python3 -m venv .venv
```

Substitua pelo comando do interpretador base verificado se for diferente. Não crie um ambiente dentro de outra .venv. No Debian/Ubuntu, se a criação falhar porque ensurepip está indisponível, instale o pacote venv correspondente da distribuição (para o interpretador padrão, geralmente `sudo apt install python3-venv`) com autorização administrativa. Para versão instalada separadamente, use o pacote correspondente documentado. Nunca substitua o Python do sistema.

## 2. Ative e verifique

A ativação muda a busca de comandos no shell atual. Não é obrigatória se você chamar diretamente o Python do ambiente.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Prompt de Comando Windows (cmd.exe, não PowerShell):

```bat
.venv\Scripts\activate.bat
```

macOS/Linux (bash ou zsh):

```bash
source .venv/bin/activate
```

O prompt pode mostrar `(.venv)`, mas confirme:

```shell
python --version
python -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
python -m pip --version
```

O executável e o caminho do pip devem apontar para a .venv deste projeto; a comparação deve imprimir True. Use `python -m pip` com esse interpretador verificado, não pip isolado ou o launcher base. Se o PowerShell bloquear scripts, não enfraqueça a política de segurança; use diretamente o executável:

```powershell
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe first_program.py
```

No macOS/Linux sem ativação:

```bash
.venv/bin/python -m pip --version
.venv/bin/python first_program.py
```

## 3. Selecione .venv no VS Code

Abra Command Palette > **Python: Select Interpreter**. Selecione o interpretador dentro da .venv deste projeto (Windows: .venv/Scripts/python.exe; macOS/Linux: .venv/bin/python). Abra novo terminal integrado e repita a verificação. Se não houver ativação automática, ative manualmente ou use o caminho direto. Execute seu first_program.py existente com esse interpretador.

## 4. Saia e recrie

No shell ativado, digite `deactivate`. Fechar o shell também encerra sua ativação. A pasta e os pacotes permanecem. Não copie nem mova .venv entre máquinas; recrie com Python base e arquivo de dependências. Para recriar, feche terminais que o utilizam, confirme a pasta exata e remova somente o ambiente pelo gerenciador de arquivos; preserve código e requirements.

Adicione `.venv/` ao .gitignore da raiz do projeto (este repositório já ignora .venv). Nunca versione o ambiente gerado. Mantenha o código fora dele. Variáveis de ambiente, binários de navegadores, bibliotecas do SO e serviços podem ficar em outros locais; venv isola pacotes Python, não todos os recursos.

## 5. Prática e solução de problemas

Crie duas pastas de prática separadas, cada uma com sua .venv. Selecione e confirme o caminho de cada executável e rode o primeiro programa em uma delas. Não é necessário baixar pacotes para este exercício. Se aparecer o interpretador errado, reabra a pasta correta, selecione novamente e confirme. Se faltar pip, consulte instruções da instalação Python correspondente; não instale no Python do sistema como alternativa.

**Referência rápida:** criar com interpretador base verificado + `-m venv .venv`; ativar ou usar caminho direto; verificar executável e pip; desativar ao terminar. A seguir, aprenda a instalar e registrar pacotes.

## Referências oficiais

- [Python venv](https://docs.python.org/pt-br/3.13/library/venv.html)
- [Python Packaging User Guide](https://packaging.python.org/pt-br/latest/guides/installing-using-pip-and-virtual-environments/)
- [Ambientes no VS Code](https://code.visualstudio.com/docs/python/environments)

<!-- chapter-navigation:bottom -->
[← Anterior](../03-run-your-first-program/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../05-packages-and-dependencies/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
