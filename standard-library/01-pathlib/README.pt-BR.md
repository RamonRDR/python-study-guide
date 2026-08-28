# Trabalhando com Caminhos do Sistema de Arquivos Usando `pathlib`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

`pathlib` é o módulo da biblioteca padrão para representar e manipular caminhos do sistema de arquivos como objetos.

Nos capítulos anteriores, usamos strings como `"notes.txt"` e `"reports/data.csv"` ao abrir arquivos. Isso funciona, mas caminhos possuem estrutura: diretórios, nomes, stems, sufixos, pais e separadores que dependem da plataforma. `pathlib` oferece uma API própria para essa estrutura.

Para a maior parte do trabalho cotidiano, comece com:

```python
from pathlib import Path
```

Depois, crie objetos `Path` e combine-os em vez de concatenar strings manualmente.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que um objeto `Path` representa;
- criar caminhos relativos e absolutos;
- combinar segmentos com `/`;
- inspecionar nomes, sufixos, pais e partes;
- usar `Path.cwd()` e `Path.home()` de forma intencional;
- criar diretórios com `mkdir()`;
- ler e escrever texto por meio de um caminho;
- verificar se um caminho aponta atualmente para arquivo ou diretório;
- percorrer diretórios com `iterdir()`;
- pesquisar com `glob()` e `rglob()`;
- transformar nomes com `with_name()` e `with_suffix()`;
- entender por que verificar existência não garante que uma operação posterior terá sucesso;
- distinguir `Path` das classes de caminhos puros em nível introdutório;
- evitar separadores de caminho fixos quando a portabilidade importa.

## 1. Que problema o `pathlib` resolve?

Um caminho é mais do que texto.

Considere:

```text
reports/2026/summary.txt
```

Esse caminho possui partes com significado:

- `reports` é um segmento de diretório;
- `2026` é outro segmento;
- `summary.txt` é o nome final;
- `summary` é o stem;
- `.txt` é o sufixo.

Seria possível manipular tudo com métodos de string, mas o código também teria de entender separadores e convenções do sistema operacional.

`pathlib` coloca comportamento de caminhos em objetos específicos para caminhos.

```python
from pathlib import Path

report_path = Path("reports") / "2026" / "summary.txt"

print(report_path)
print(report_path.name)
print(report_path.stem)
print(report_path.suffix)
print(report_path.parent)
```

O separador exibido por `print(report_path)` depende do sistema operacional. Esse é justamente um dos benefícios: o código expressa a estrutura do caminho sem inserir manualmente `/` ou `\\`.

## 2. `Path` normalmente é a classe certa

O módulo `pathlib` possui várias classes.

Para trabalho normal com o sistema de arquivos, use `Path`:

```python
from pathlib import Path

config_path = Path("config") / "settings.json"
```

`Path` é uma classe concreta. Ela pode manipular a estrutura do caminho e também executar operações no sistema de arquivos, como ler um arquivo, criar um diretório ou consultar o que existe.

Também existem classes puras, como `PurePath`, `PurePosixPath` e `PureWindowsPath`. Elas manipulam a sintaxe do caminho sem acessar o sistema de arquivos.

Normalmente você **não** precisa escolher `PosixPath` ou `WindowsPath` diretamente. `Path` seleciona a variante concreta adequada para a plataforma em execução.

## 3. Criando caminhos

Um caminho pode ser criado a partir de uma string:

```python
from pathlib import Path

file_path = Path("notes.txt")
```

Também pode receber vários segmentos:

```python
from pathlib import Path

file_path = Path("reports", "2026", "summary.txt")
```

Ou podemos combinar objetos e segmentos com `/`:

```python
from pathlib import Path

reports_dir = Path("reports")
file_path = reports_dir / "2026" / "summary.txt"
```

Nesse contexto, `/` não executa divisão. `Path` define esse operador como uma forma conveniente de unir segmentos.

Prefira:

```python
file_path = Path("reports") / "2026" / "summary.txt"
```

em vez de construir separadores manualmente:

```python
file_path = "reports/" + "2026/" + "summary.txt"
```

A versão com `Path` comunica a intenção e evita amarrar o programa ao separador de uma única plataforma.

## 4. Caminhos relativos e absolutos

Um **caminho relativo** é interpretado em relação a algum contexto, normalmente o diretório de trabalho atual do processo.

```python
from pathlib import Path

relative_path = Path("reports") / "summary.txt"

print(relative_path.is_absolute())
```

Um **caminho absoluto** identifica uma localização a partir da raiz ou do contexto de unidade do sistema de arquivos.

Não suponha que um caminho relativo é relativo ao arquivo `.py`. Normalmente ele é interpretado a partir do diretório de trabalho atual do processo.

Essa diferença explica muitos casos de "o arquivo existe, mas o Python não encontra".

## 5. Diretório de trabalho e diretório home

`Path.cwd()` retorna o diretório de trabalho atual:

```python
from pathlib import Path

current_dir = Path.cwd()
print(current_dir)
```

`Path.home()` retorna o diretório home do usuário atual:

```python
from pathlib import Path

home_dir = Path.home()
print(home_dir)
```

Use esses métodos quando o programa realmente depende dessas localizações.

Não os utilize apenas para fazer um caminho "parecer absoluto". Primeiro defina em relação a que localização o caminho deve existir.

## 6. Inspecionando a estrutura do caminho

`Path` expõe componentes comuns como atributos.

```python
from pathlib import Path

path = Path("archive") / "report.final.csv"

print(path.name)
print(path.stem)
print(path.suffix)
print(path.suffixes)
print(path.parent)
print(path.parts)
```

Significados comuns:

| Atributo | Significado |
|---|---|
| `.name` | componente final do caminho |
| `.stem` | nome final sem o último sufixo |
| `.suffix` | último sufixo |
| `.suffixes` | lista de sufixos |
| `.parent` | caminho pai lógico |
| `.parents` | sequência de ancestrais lógicos |
| `.parts` | tupla com os componentes |

O sufixo é baseado na sintaxe do caminho, não no conteúdo real do arquivo. Um arquivo chamado `table.csv` não é necessariamente um CSV válido.

## 7. Transformando nomes sem cirurgia de strings

Use métodos de caminho quando a operação diz respeito à estrutura do caminho.

```python
from pathlib import Path

source = Path("exports") / "report.csv"

print(source.with_suffix(".json"))
print(source.with_name("summary.csv"))
```

`with_suffix()` retorna um novo caminho. Ele não renomeia um arquivo no disco.

Da mesma forma, `with_name()` retorna outro objeto de caminho com um nome final diferente.

A distinção é:

```text
construir ou transformar um Path
        !=
alterar o sistema de arquivos
```

## 8. Lendo e escrevendo texto

`Path.read_text()` e `Path.write_text()` são atalhos convenientes para arquivos de texto pequenos.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    notes_dir = workspace / "notes"
    notes_dir.mkdir()

    notes_path = notes_dir / "pathlib.txt"
    notes_path.write_text("Paths are objects.\n", encoding="utf-8")

    print(notes_path.read_text(encoding="utf-8").strip())
```

Informe um encoding explícito quando o formato ou contrato da aplicação exigir.

Para dados portáveis do projeto, UTF-8 costuma ser uma boa escolha explícita:

```python
text = path.read_text(encoding="utf-8")
```

e:

```python
path.write_text(text, encoding="utf-8")
```

### Importante: `write_text()` substitui o conteúdo existente

`Path.write_text()` abre o destino para escrita. Se o arquivo já existir, o conteúdo anterior é substituído.

Isso é perigoso quando o arquivo existente precisa ser preservado.

Use esse método somente quando a substituição for intencional.

Para acrescentar conteúdo ou usar modos especiais, utilize `open()` ou `Path.open()` com o modo adequado.

## 9. `Path.open()` e o `open()` embutido

Um objeto `Path` pode ser passado diretamente ao `open()` embutido porque implementa o protocolo path-like do Python.

```python
from pathlib import Path

path = Path("notes.txt")

with open(path, "r", encoding="utf-8") as file:
    text = file.read()
```

Também é possível usar o método do próprio caminho:

```python
with path.open("r", encoding="utf-8") as file:
    text = file.read()
```

As duas formas são válidas. Procure manter um estilo consistente no mesmo projeto.

## 10. Criando diretórios com `mkdir()`

`Path.mkdir()` cria um diretório.

```python
from pathlib import Path

output_dir = Path("output")
output_dir.mkdir()
```

Para criar também pais ausentes:

```python
output_dir = Path("build") / "reports" / "daily"
output_dir.mkdir(parents=True)
```

Quando um diretório já existente for aceitável:

```python
output_dir.mkdir(parents=True, exist_ok=True)
```

Seja preciso sobre `exist_ok=True`: ele indica que um diretório já existente naquele caminho é aceitável. Isso não transforma todo problema de sistema de arquivos em sucesso. Erros de permissão e objetos incompatíveis ainda podem causar falhas.

## 11. Consultando o sistema de arquivos

Consultas comuns:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    file_path = workspace / "lesson.txt"
    file_path.write_text("pathlib", encoding="utf-8")

    print(file_path.exists())
    print(file_path.is_file())
    print(workspace.is_dir())
```

Métodos centrais:

| Método | Pergunta |
|---|---|
| `.exists()` | este caminho existe agora? |
| `.is_file()` | ele aponta atualmente para um arquivo regular? |
| `.is_dir()` | ele aponta atualmente para um diretório? |
| `.is_symlink()` | ele é um link simbólico? |

Esses métodos informam o resultado da consulta ao sistema de arquivos no momento em que ela é executada, mas um resultado `False` nem sempre prova que uma entrada está ausente. No Python 3.14, métodos booleanos de estado como `exists()`, `is_file()` e `is_dir()` retornam `False` quando um `OSError` impede a inspeção. Com o padrão `follow_symlinks=True`, `exists()` também retorna `False` quando o destino de um link simbólico está ausente. Se você precisar distinguir entre caminho ausente, inacessível, inválido ou outra falha de consulta de estado, use `stat()` e trate sua exceção em vez de depender apenas da consulta booleana.

Portanto, essas verificações são fotografias úteis daquilo que a consulta conseguiu estabelecer, e não garantias autoritativas sobre o sistema de arquivos. A operação que você realmente precisa executar, e qualquer exceção que ela gerar, continua sendo a fronteira autoritativa.

## 12. Uma verificação não é uma garantia

Este código parece cuidadoso:

```python
if path.exists():
    text = path.read_text(encoding="utf-8")
```

Mas o sistema de arquivos pode mudar entre a verificação e a leitura. Permissões podem mudar. Outro processo pode remover ou substituir o arquivo. Um recurso de rede pode ficar indisponível.

Por isso, `exists()` é útil quando o **estado atual** é relevante, mas não deve ser tratado como promessa de que a operação seguinte não falhará.

Na fronteira da operação, trate a exceção que a própria operação pode gerar:

```python
from pathlib import Path

settings_path = Path("settings.json")

try:
    text = settings_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("Settings file is missing")
else:
    print(text)
```

Essa ideia se conecta diretamente à Fase 7: APIs de sistema de arquivos e tratamento de exceções trabalham juntas.

## 13. Percorrendo um diretório

`iterdir()` produz os filhos diretos de um diretório.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)

    for name in ("gamma.txt", "alpha.txt", "beta.txt"):
        (workspace / name).write_text(name, encoding="utf-8")

    for path in sorted(workspace.iterdir()):
        print(path.name)
```

O sistema de arquivos não promete uma ordem útil. Se a ordem determinística fizer parte do resultado, ordene explicitamente.

Isso é especialmente importante em:

- testes;
- relatórios gerados;
- tutoriais;
- automações reproduzíveis.

`iterdir()` não é recursivo.

## 14. Pesquisando com `glob()` e `rglob()`

`glob()` encontra caminhos usando um padrão relativo ao caminho atual.

```python
from pathlib import Path

for path in Path("src").glob("*.py"):
    print(path)
```

Essa busca considera o nível correspondente ao padrão.

`rglob()` pesquisa recursivamente:

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source_dir = workspace / "src"
    nested_dir = source_dir / "tools"
    nested_dir.mkdir(parents=True)

    (source_dir / "app.py").write_text("print('app')\n", encoding="utf-8")
    (nested_dir / "helper.py").write_text("VALUE = 1\n", encoding="utf-8")
    (nested_dir / "notes.txt").write_text("notes\n", encoding="utf-8")

    for path in sorted(source_dir.rglob("*.py")):
        print(path.relative_to(workspace))
```

Novamente, a ordem não é garantida. Use `sorted()` quando a ordem fizer parte do contrato.

Buscas recursivas podem ficar caras em árvores grandes. Restrinja o padrão e a raiz de busca conforme a necessidade real.

## 15. Tornando um caminho relativo a outro

`relative_to()` expressa um caminho em relação a um pai conhecido:

```python
from pathlib import Path

workspace = Path("/project")
file_path = Path("/project/docs/guide.md")

print(file_path.relative_to(workspace))
```

Conceitualmente, o resultado é:

```text
docs/guide.md
```

`relative_to()` trabalha com uma relação entre caminhos. Não é equivalente a consultar o diretório de trabalho atual.

Ele pode gerar `ValueError` quando a relação solicitada não pode ser formada de acordo com suas regras.

## 16. Resolvendo caminhos

`resolve()` retorna um caminho absoluto, resolvendo componentes `..` e links simbólicos conforme a semântica do sistema de arquivos.

```python
from pathlib import Path

path = Path("docs") / ".." / "README.md"
resolved = path.resolve()

print(resolved)
```

Como `resolve()` envolve semântica do sistema de arquivos, não o confunda com simples limpeza de string.

Use-o quando realmente precisar de um caminho resolvido, e não automaticamente em todo `Path`.

## 17. Caminhos puros

Classes de caminhos puros são úteis quando queremos a semântica de um caminho sem acessar o sistema de arquivos.

Por exemplo, um programa executando em Linux pode analisar sintaxe de caminhos do Windows:

```python
from pathlib import PureWindowsPath

windows_path = PureWindowsPath("C:/Users/Ana/Documents/report.txt")

print(windows_path.name)
print(windows_path.parent)
```

`PureWindowsPath` não verifica se esse caminho existe.

Para código comum que trabalha com o sistema de arquivos local, `Path` continua sendo o ponto de partida.

## 18. Pensando em portabilidade

Evite separadores fixos quando o caminho precisa ser portável.

Frágil:

```python
path = "reports\\2026\\summary.txt"
```

Melhor:

```python
from pathlib import Path

path = Path("reports") / "2026" / "summary.txt"
```

Mas "multiplataforma" não significa que todo caminho possui o mesmo significado em qualquer sistema. Unidades, caminhos UNC, permissões, sensibilidade a maiúsculas, links simbólicos, nomes reservados e regras de filesystem podem variar.

`pathlib` oferece uma abstração consciente da plataforma. Ele não apaga o sistema operacional.

## 19. Objetos `Path` funcionam com muitas APIs do Python

APIs modernas do Python frequentemente aceitam objetos path-like.

```python
from pathlib import Path
import json

path = Path("config.json")

with path.open("r", encoding="utf-8") as file:
    data = json.load(file)
```

Por isso `pathlib` se integra bem aos capítulos anteriores de arquivos e módulos.

Normalmente não é necessário converter todo `Path` para `str`.

Converta apenas quando uma API externa exigir especificamente uma representação textual.

## 20. Exceções comuns

Operações de sistema de arquivos ainda podem falhar.

| Exceção | Situação típica |
|---|---|
| `FileNotFoundError` | arquivo solicitado ou algum caminho pai está ausente |
| `FileExistsError` | a criação exigia ausência, mas já existe uma entrada |
| `PermissionError` | a operação não é permitida |
| `IsADirectoryError` | uma operação de arquivo recebeu um diretório |
| `NotADirectoryError` | um componente esperado como diretório não é diretório |
| `OSError` | falhas mais amplas do sistema operacional ou filesystem |

Capture a exceção mais específica que você realmente consegue tratar.

Não envolva toda chamada de `Path` em `except Exception:` apenas porque operações de filesystem podem falhar.

## 21. Quando usar `pathlib`

Use `pathlib` quando:

- estiver construindo caminhos a partir de segmentos;
- precisar de nomes, stems, sufixos ou relações de parentesco;
- estiver lendo ou escrevendo arquivos;
- estiver criando diretórios;
- estiver descobrindo arquivos;
- precisar de construção portável de caminhos;
- quiser tornar explícita a intenção de caminho em interfaces.

Exemplo:

```python
from pathlib import Path

def load_template(template_path: Path) -> str:
    return template_path.read_text(encoding="utf-8")
```

Um type hint `Path` pode tornar claro um contrato que espera especificamente um objeto `Path`.

Dependendo da interface, aceitar uma entrada path-like mais ampla também pode fazer sentido. Isso é uma decisão de design de API, não uma regra universal.

## 22. Quando não forçar `pathlib`

Não introduza objetos de caminho onde não existe um problema de caminho.

Algumas APIs de baixo nível ou legadas continuam organizadas em torno de `os`, `os.path`, descritores de arquivo ou strings.

A Fase 8 ainda abordará `os` e `shutil`. Esses módulos não se tornam obsoletos porque `pathlib` existe. Há sobreposição, mas também responsabilidades em níveis diferentes.

## 23. Erros comuns

### Erro 1: assumir que relativo significa relativo ao arquivo-fonte

```python
Path("data.json")
```

normalmente parte do diretório de trabalho do processo.

### Erro 2: verificar `exists()` e assumir que a próxima operação está garantida

O estado do sistema de arquivos pode mudar.

### Erro 3: esquecer que `write_text()` substitui conteúdo

Se preservar dados existentes for necessário, escolha outra estratégia de abertura.

### Erro 4: concatenar separadores manualmente

Prefira composição estrutural.

### Erro 5: supor que o sufixo valida o formato

`.json` no nome não prova JSON válido.

### Erro 6: depender da ordem de iteração de diretório

Ordene quando a saída precisa ser determinística.

### Erro 7: chamar `resolve()` automaticamente em todo lugar

Resolva somente quando precisar dessa semântica.

### Erro 8: converter todo `Path` para `str`

Muitas APIs do Python aceitam objetos path-like diretamente.

## 24. Exemplo prático

Imagine um programa pequeno que cria um workspace, escreve um relatório e descobre arquivos de texto gerados.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    reports_dir = workspace / "reports"
    reports_dir.mkdir()

    report_path = reports_dir / "summary.txt"
    report_path.write_text("status=ready\n", encoding="utf-8")

    for path in sorted(reports_dir.glob("*.txt")):
        print(path.name, path.read_text(encoding="utf-8").strip())
```

A ideia principal não é apenas uma sintaxe menor.

O programa usa uma única abstração de caminho para:

```text
construir
    ↓
criar
    ↓
escrever
    ↓
descobrir
    ↓
ler
```

Isso deixa a intenção do filesystem visível de ponta a ponta.

## 25. Exercício

Crie um programa usando `TemporaryDirectory` e `Path` que:

1. crie um diretório chamado `study`;
2. crie `notes` e `archive` dentro dele;
3. escreva dois arquivos `.txt` dentro de `notes`;
4. liste os filhos diretos de `notes` em ordem;
5. encontre todos os `.txt` abaixo de `study` recursivamente;
6. imprima cada caminho encontrado de forma relativa a `study`;
7. leia um arquivo usando UTF-8;
8. não deixe arquivos permanentes.

Depois responda:

- Quais caminhos são relativos?
- Quais operações deste exercício realmente acessam ou alteram o sistema de arquivos, e quais são apenas operações estruturais de caminho, como composição de caminhos ou `relative_to()`?
- Por que verificar `.exists()` antes não garante que `.read_text()` funcionará depois?
- Quando `PureWindowsPath` seria útil no lugar de `Path`?

## 26. Checklist de revisão

Antes de avançar, confirme que você consegue explicar:

- o que um objeto `Path` representa;
- por que `/` é útil para composição;
- caminhos relativos e absolutos;
- diretório de trabalho versus localização do arquivo-fonte;
- `.name`, `.stem`, `.suffix`, `.parent` e `.parts`;
- `read_text()` e `write_text()`;
- `mkdir(parents=True, exist_ok=True)`;
- `.exists()`, `.is_file()` e `.is_dir()`;
- por que verificações não são garantias;
- `iterdir()`, `glob()` e `rglob()`;
- por que uma saída determinística pode exigir `sorted()`;
- `with_name()` e `with_suffix()`;
- a finalidade de `resolve()`;
- a diferença entre `Path` e caminhos puros;
- por que `pathlib` complementa, em vez de substituir totalmente, `os` e `shutil`.

## Referência rápida

```python
from pathlib import Path

path = Path("reports") / "summary.txt"

path.name
path.stem
path.suffix
path.parent
path.parts

Path.cwd()
Path.home()

path.exists()
path.is_file()
path.is_dir()

path.read_text(encoding="utf-8")
path.write_text("text\n", encoding="utf-8")

directory.mkdir(parents=True, exist_ok=True)

list(directory.iterdir())
list(directory.glob("*.txt"))
list(directory.rglob("*.txt"))

path.with_name("other.txt")
path.with_suffix(".json")
path.resolve()
```

## Exemplos executáveis

- [`examples/path_parts.py`](examples/path_parts.py)
- [`examples/text_workspace.py`](examples/text_workspace.py)
- [`examples/discover_python_files.py`](examples/discover_python_files.py)
- [`examples/inspect_paths.py`](examples/inspect_paths.py)

Os exemplos são determinísticos e usam apenas operações estruturais de caminhos ou diretórios temporários, então não deixam arquivos persistentes.

## Próximo capítulo

Continue com **[Capítulo 02: `datetime` e Cálculos de Tempo](../02-datetime/README.pt-BR.md)**, onde a biblioteca padrão adiciona objetos explícitos para datas, horários, durações, parsing, formatação e aritmética de datas.

## Referências oficiais

- [Python 3.14 `pathlib` - caminhos de sistema de arquivos orientados a objetos](https://docs.python.org/3.14/library/pathlib.html)
- [Python 3.14 `os.PathLike` e `os.fspath()`](https://docs.python.org/3.14/library/os.html#os.PathLike)
- [Python 3.14 função embutida `open()`](https://docs.python.org/3.14/library/functions.html#open)
