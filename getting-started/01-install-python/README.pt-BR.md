# Instalar o Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[Índice do módulo](../README.pt-BR.md) · [Próximo →](../02-configure-vscode/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo e pré-requisitos

**Nível:** iniciante absoluto. **Tempo estimado:** 20–40 minutos, sem contar downloads. Você precisa de um sistema desktop compatível e permissão para instalar programas. Ao final, terá um comando de terminal que identifica o Python e seu executável.

Python é a linguagem; o interpretador é o aplicativo que executa código Python. Baixar apenas um editor não instala o interpretador. Use fontes oficiais, não anúncios de downloads de terceiros. Este guia testa Python 3.13 no CI. Prefira uma versão de correção 3.13 suportada para consistência; outra versão suportada de Python 3 pode executar este exercício introdutório, mas capítulos e dependências posteriores podem diferir.

## 1. Verifique antes de instalar

Abra PowerShell no Windows, Terminal no macOS ou um terminal no Linux. Digite o comando e pressione Enter. Não digite símbolos do prompt como `PS>` ou `$`.

Windows:

```powershell
py -3.13 --version
```

macOS ou Linux:

```bash
python3 --version
```

Se já tiver a versão desejada, pule a instalação. Se o comando não existir ou a versão for diferente, siga as instruções do seu sistema. Uma versão como `Python 3.13.x` é ilustrativa; o último número identifica a versão de correção.

## 2. Windows

Abra a [página oficial de downloads do Python](https://www.python.org/downloads/). Escolha o gerenciador de instalação do Python para Windows em sistema compatível, instale-o e siga as instruções de configuração. Abra uma nova janela do PowerShell. Com o gerenciador instalado, execute:

```powershell
py install 3.13
py -3.13 --version
py -3.13 -c "import sys; print(sys.executable)"
```

O segundo comando informa a versão; o terceiro mostra o caminho real do interpretador. Em uma máquina com instalador tradicional anterior, `py -3.13` pode funcionar sem o gerenciador. Se usar um instalador tradicional oficial que ofereça **Add Python to PATH**, marque a opção antes de instalar para facilitar a localização de comandos. Não instale uma versão antiga insegura só por essa opção. Se o launcher existente não reconhecer `py install`, consulte o guia de solução de problemas do gerenciador antes de alterá-lo.

`PATH` é uma lista de diretórios em que o shell procura comandos. O launcher pode escolher uma versão instalada específica mesmo quando `python` se refere a outra versão. Continue usando o comando verificado.

## 3. macOS

Baixe o instalador macOS de uma versão 3.13 suportada em [Python.org](https://www.python.org/downloads/), compatível com o sistema e a arquitetura. Abra o instalador, siga as etapas e, quando fornecido pelo instalador, execute `Install Certificates.command` na pasta do aplicativo Python instalado para concluir a configuração de certificados. Abra uma nova janela do Terminal:

```bash
python3.13 --version
python3.13 -c "import sys; print(sys.executable)"
```

Se usar outra instalação suportada, o comando pode ser `python3`. Confira versão e caminho. Não substitua nem exclua o Python do sistema operacional.

## 4. Linux

Muitas distribuições já incluem Python. Verifique primeiro `python3 --version`. Se estiver ausente, use o gerenciador de pacotes oficial da distribuição. Para Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3
```

Para Fedora (se ainda não estiver instalado):

```bash
sudo dnf install python3
```

Use comandos administrativos apenas em máquina que você tem autorização para gerenciar. Confirme:

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

A distribuição pode fornecer outra versão suportada de Python 3. Se não for 3.13, consulte opções documentadas de instalação paralela ou o administrador; não substitua o interpretador do sistema, altere links simbólicos do sistema nem execute instalador não confiável. Se `python3.13` separado estiver disponível, verifique e use-o. O primeiro programa funciona em versões suportadas de Python 3; exemplos posteriores podem exigir a versão testada pelo guia.

## 5. Solução de problemas

| Sintoma | O que verificar |
| --- | --- |
| Comando não encontrado | Reabra o terminal; verifique instalação e comando do sistema. |
| Windows abre uma loja ou outro Python | Use `py -3.13 --version`; consulte solução oficial de aliases/launcher se falhar. |
| Versão diferente da esperada | Confira o caminho do executável; selecione o interpretador desejado em vez de reinstalar às cegas. |
| Aparece `>>>` | Você entrou no prompt interativo do Python. Digite `exit()` e pressione Enter para voltar ao shell. |
| Falha de permissão ou instalação | Consulte instruções oficiais ou o administrador; nunca contorne controles de segurança. |

## Prática e referência rápida

Execute as verificações de versão e caminho no seu sistema e anote o resultado. Explique com suas palavras o que o interpretador faz. Guarde o comando verificado para as próximas aulas. Não é necessário instalar pacotes neste módulo.

## Referências oficiais

- [Downloads Python](https://www.python.org/downloads/)
- [Gerenciador de instalação e solução de problemas no Windows](https://docs.python.org/3.14/using/windows.html)
- [Instalação e launcher Python 3.13 no Windows](https://docs.python.org/3.13/using/windows.html)
- [Python 3.13 no macOS](https://docs.python.org/3.13/using/mac.html)
- [Configuração Python no Ubuntu](https://documentation.ubuntu.com/ubuntu-for-developers/howto/python-setup/)
- [Python no Fedora](https://developer.fedoraproject.org/tech/languages/python/python-installation.html)

<!-- chapter-navigation:bottom -->
[Índice do módulo](../README.pt-BR.md) · [Próximo →](../02-configure-vscode/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
