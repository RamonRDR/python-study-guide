# Configurar o VS Code

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../01-install-python/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../03-run-your-first-program/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo e pré-requisitos

**Nível:** iniciante absoluto. **Tempo estimado:** 20–30 minutos, sem contar downloads. Conclua a aula anterior e guarde o comando Python verificado. VS Code é um editor de código desktop gratuito. Sua extensão Python ajuda o editor a se comunicar com o interpretador; não substitui o interpretador. Você pode usar outro editor de texto simples e um terminal. Não é necessária conta, ferramenta de IA ou pacote adicional.

## 1. Instale o Visual Studio Code

Use a [página oficial de download do VS Code](https://code.visualstudio.com/download). Escolha a versão para seu sistema e arquitetura.

- **Windows:** baixe o User Installer, abra-o e siga as instruções. Adicionar VS Code ao PATH, se oferecido, é opcional neste guia; habilita o comando separado `code`.
- **macOS:** baixe a versão apropriada, abra o arquivo baixado se necessário e mova Visual Studio Code para Aplicativos.
- **Linux:** escolha o pacote compatível com sua distribuição (por exemplo, .deb para Debian/Ubuntu ou .rpm para Fedora). Siga a configuração oficial para Linux, incluindo as etapas necessárias do gerenciador de pacotes.

Não use downloads não oficiais nem conceda privilégios administrativos desnecessariamente. Abra VS Code após instalar.

## 2. Instale a extensão Python

1. Abra a área Extensions na barra de atividades (ícone formado por quadrados).
2. Pesquise **Python**.
3. Escolha a extensão publicada pela **Microsoft** (identificador `ms-python.python`) e clique em Install.
4. Siga as instruções de reinicialização/recarga se necessárias. Extensões complementares podem ser instaladas automaticamente; não é necessária extensão de IA separada.

## 3. Abra uma pasta de estudos

Crie uma pasta vazia chamada `python-practice` em um local pessoal com permissão de escrita, usando o gerenciador de arquivos do sistema. No VS Code, escolha **File > Open Folder** e selecione-a. Este é seu workspace, não o diretório de instalação do Python. Se Workspace Trust perguntar sobre a pasta, confie nela apenas se você a criou ou entende seu conteúdo; não confie automaticamente em código desconhecido baixado.

## 4. Selecione o interpretador

Abra a Command Palette com `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS). Pesquise **Python: Select Interpreter** e selecione o interpretador instalado que você verificou antes. Se necessário, escolha Enter interpreter path e localize o executável informado na aula anterior. A versão exibida no editor deve corresponder ao Python desejado. Se já usa ambiente virtual, selecione deliberadamente seu interpretador; um novo ambiente não é necessário nesta aula.

## 5. Verifique no terminal integrado

Escolha **Terminal > New Terminal**. O terminal é onde você digita comandos do shell e vê seus resultados. Use o mesmo comando verificado antes:

Windows:

```powershell
py -3.13 --version
py -3.13 -c "import sys; print(sys.executable)"
```

macOS (instalação oficial 3.13):

```bash
python3.13 --version
python3.13 -c "import sys; print(sys.executable)"
```

Linux (ou outra instalação Python 3 verificada no macOS):

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

Se verificou outro comando, use-o. Compare o executável com o interpretador selecionado no VS Code. A seleção controla ações da extensão, mas um comando do shell ainda pode escolher outro Python instalado. Feche e reabra o terminal integrado após mudar o interpretador; se os caminhos ainda diferirem, escolha o comando verificado apropriado ou use o caminho do executável selecionado.

## 6. Solução de problemas

| Sintoma | Ação |
| --- | --- |
| Comando Python funciona só fora do VS Code | Reinicie VS Code completamente para herdar o ambiente atualizado. |
| Python: Select Interpreter não aparece | Confira se a extensão Python da Microsoft está instalada e habilitada. |
| Interpretador incorreto | Selecione o executável desejado e compare o caminho novamente. |
| Não consegue salvar | Abra uma pasta pessoal gravável; não trabalhe dentro da instalação Python. |
| Interface ou idioma diferente | Use a Command Palette e procure o comando traduzido equivalente. |

## Prática e referência rápida

Abra a pasta de prática, localize Explorer e terminal integrado, selecione o interpretador e confirme versão e caminho. Explique a diferença entre editor, interpretador e terminal. Deixe a pasta aberta para a próxima aula.

## Referências oficiais

- [Downloads VS Code](https://code.visualstudio.com/download)
- [Instalação VS Code](https://code.visualstudio.com/docs/getstarted/overview)
- [Configuração VS Code no Linux](https://code.visualstudio.com/docs/setup/linux)
- [Tutorial Python no VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Ambientes Python no VS Code](https://code.visualstudio.com/docs/python/environments)
- [Extensão Python da Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

<!-- chapter-navigation:bottom -->
[← Anterior](../01-install-python/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../03-run-your-first-program/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
