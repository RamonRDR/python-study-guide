# Executar seu primeiro programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../02-configure-vscode/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../fundamentals/01-how-python-runs-a-program/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo e pré-requisitos

**Nível:** iniciante absoluto. **Tempo estimado:** 15–25 minutos. Python instalado e comando verificado; pasta de prática aberta no editor. Você vai escrever, salvar, executar, modificar e executar novamente um arquivo manualmente. Fundamentos explicará o significado do código com mais detalhes.

## 1. Crie um arquivo Python

No Explorer do VS Code, escolha New File e nomeie-o `first_program.py` dentro de `python-practice`. Alternativamente, use editor de texto simples e salve com esse nome exato. Certifique-se de que a extensão é .py, não .py.txt. Digite você mesmo o código:

```python
print("Python is ready!")
```

Salve com `Ctrl+S` (Windows/Linux) ou `Cmd+S` (macOS). Use aspas retas, não aspas tipográficas. Salvar não executa o programa.

## 2. Execute no terminal

Abra o terminal integrado ou o terminal do sistema. Confira se está na pasta de prática. No Windows PowerShell, use `Get-Location` e `Get-ChildItem`; no macOS/Linux, use `pwd` e `ls`. O arquivo deve aparecer na listagem. Se necessário, use `cd` seguido do caminho entre aspas para sua pasta, substituindo pelo seu próprio caminho.

Execute com o comando do interpretador verificado anteriormente:

Windows:

```powershell
py -3.13 first_program.py
```

macOS (instalação oficial 3.13):

```bash
python3.13 first_program.py
```

Linux (ou outra instalação Python 3 verificada no macOS):

```bash
python3 first_program.py
```

Se verificou outro comando, substitua-o, mantendo o nome do arquivo. Saída esperada:

```text
Python is ready!
```

Você também pode usar a ação **Run Python File in Terminal** da extensão Python no VS Code. Ela executa o arquivo com o interpretador selecionado. Prefira digitar o comando de terminal pelo menos uma vez para entender como começa a execução.

## 3. Modifique e repita

Mude a mensagem para `My first program!`, salve e execute novamente com o mesmo comando. Preveja a saída antes de executar. Escrever, salvar e executar são ações separadas. Não é necessária conta Git, conexão à internet, pacote externo ou assistente de IA para executar este exemplo após instalar Python.

## 4. Solução de problemas

| Sintoma | Ação |
| --- | --- |
| Can't open file / No such file | Confira pasta atual e nome exato; use aspas para caminhos com espaços. |
| Saída não mudou | Salve o arquivo e confira se executou o arquivo desejado. |
| `SyntaxError` | Confira pares de aspas e parênteses; leia a linha indicada. |
| Comando não encontrado | Volte à verificação do interpretador; não digite comandos shell no prompt Python `>>>`. |
| Terminal mostra `>>>` | Digite `exit()` e volte ao shell antes de executar o arquivo. |

## Prática e checklist de conclusão

- [ ] Criei e salvei um arquivo .py por conta própria.
- [ ] Consigo localizá-lo na pasta atual do terminal.
- [ ] Executei com interpretador verificado e vi a saída esperada.
- [ ] Modifiquei a mensagem, previ o resultado e executei novamente.

Para comparação, o repositório contém [o mesmo exemplo original](examples/first_program.py). A partir da raiz do repositório, execute-o com seu interpretador verificado seguido de `getting-started/03-run-your-first-program/examples/first_program.py`. Este arquivo não é necessário para concluir o exercício manual.

## Próximo passo

Siga para [Como o Python executa um programa](../../fundamentals/01-how-python-runs-a-program/README.pt-BR.md) para estudar código-fonte, interpretadores, ordem de execução, Hello World e erros de sintaxe em profundidade.

## Referências oficiais

- [Uso do interpretador Python](https://docs.python.org/3.13/tutorial/interpreter.html)
- [Execução de Python no VS Code](https://code.visualstudio.com/docs/python/run)

<!-- chapter-navigation:bottom -->
[← Anterior](../02-configure-vscode/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../fundamentals/01-how-python-runs-a-program/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
