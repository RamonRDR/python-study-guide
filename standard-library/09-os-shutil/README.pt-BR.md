<div align="center">

# Projetando Operações de Sistema Operacional e Arquivos com `os` e `shutil`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Standard Library](../README.pt-BR.md) · [← Anterior: `decimal`](../08-decimal/README.pt-BR.md)

O capítulo anterior de `pathlib` apresentou objetos de caminho como a forma padrão de alto nível para representar e manipular caminhos do sistema de arquivos. Este capítulo desce um nível e amplia o alcance.

O módulo `os` expõe interfaces do sistema operacional, como estado do ambiente do processo, diretório de trabalho atual, varredura de diretórios, metadados de arquivos, renomeação, travessia de árvores, capacidades relacionadas a permissões e operações de caminho em nível mais baixo. O módulo `shutil` constrói operações de arquivos e diretórios de nível mais alto sobre essas primitivas, incluindo cópia, movimentação, remoção recursiva, manipulação de arquivos compactados, descoberta de executáveis e inspeção de uso de disco.

O objetivo não é substituir `pathlib`. É entender os contratos que aparecem quando um programa cruza a fronteira do sistema operacional.

**Tempo estimado de estudo:** 220–300 minutos.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar os papéis diferentes de `pathlib`, `os`, `os.path` e `shutil`;
- ler e modificar variáveis de ambiente do processo de forma deliberada;
- explicar por que o diretório de trabalho atual é estado compartilhado do processo;
- usar `os.PathLike` e `os.fspath()` nas fronteiras de APIs de sistema de arquivos;
- distinguir separadores de caminho de separadores da variável `PATH`;
- criar diretórios com segurança usando `mkdir()` e `makedirs()`;
- escolher entre `listdir()` e `scandir()`;
- usar metadados de `DirEntry` sem assumir que permanecem atualizados para sempre;
- inspecionar metadados de arquivos com `stat()`;
- remover arquivos e diretórios vazios com a primitiva correta;
- distinguir `rename()` de `replace()`, orientado a substituição;
- percorrer árvores de diretórios com `walk()` e podar recursão com segurança;
- entender o risco de seguir links simbólicos durante travessia recursiva;
- reconhecer APIs avançadas de `dir_fd` e detecção de capacidades sem assumir suporte universal entre plataformas;
- distinguir `copyfile()`, `copy()` e `copy2()`;
- copiar árvores de diretórios com políticas explícitas de mesclagem, exclusão e links simbólicos;
- mover arquivos e diretórios entendendo o comportamento no mesmo sistema de arquivos e os fallbacks;
- usar `rmtree()` somente por trás de uma fronteira cuidadosamente validada para operações destrutivas;
- explicar por que preservação de metadados nunca é uma garantia total;
- inspecionar uso de disco e resolver executáveis por meio de `PATH`;
- criar e extrair arquivos compactados com uma política explícita de confiança;
- usar exceções em vez de pré-verificações sujeitas a corrida ao fazer I/O de sistema de arquivos;
- tornar o processamento de arquivos determinístico quando a ordem de enumeração de diretórios não é especificada;
- projetar fluxos de gerenciamento de arquivos seguros e revisáveis.

## 1. `os` é uma ponte para serviços do sistema operacional

`os` contém interfaces para várias categorias de comportamento do sistema operacional. Este capítulo foca nas partes mais relevantes para código de aplicação portável:

```text
process environment
current working directory
filesystem paths
files and directories
metadata
directory traversal
filesystem capabilities
```

O módulo também expõe APIs de gerenciamento de processos e específicas de plataforma. Elas são partes reais de `os`, mas estão intencionalmente fora do escopo deste capítulo.

## 2. `shutil` opera em um nível mais alto do sistema de arquivos

`shutil` fornece operações sobre arquivos e coleções de arquivos:

```text
copy one file
copy a directory tree
move files or trees
remove directory trees
inspect disk usage
find executables
create and unpack archives
```

Um modelo mental útil é:

```text
pathlib  -> model paths and perform convenient path-oriented operations
os       -> operating-system primitives and lower-level filesystem interfaces
shutil   -> high-level file and directory workflows
```

## 3. Não trate os três módulos como concorrentes

Eles se sobrepõem porque resolvem problemas vizinhos.

Para composição e inspeção comuns de caminhos, `pathlib.Path` costuma ser a interface mais clara. `os` continua importante quando você precisa de estado do ambiente, descritores de diretório, caminhos em bytes, conjuntos de capacidades ou APIs de nível mais baixo. `shutil` continua útil para cópia recursiva, remoção recursiva, operações de archive, uso de disco e descoberta de executáveis.

O Python 3.14 também adicionou `Path.copy()`, `Path.copy_into()`, `Path.move()` e `Path.move_into()`. Isso aumenta a sobreposição, mas não torna `os` ou `shutil` obsoletos.

## 4. Muitas APIs de sistema de arquivos aceitam objetos path-like

Desde a introdução do protocolo de caminhos, muitas funções de `os` e `shutil` aceitam objetos que implementam `os.PathLike`.

```python
import os
from pathlib import Path


path = Path("reports") / "summary.txt"
print(os.fspath(path))
```

Objetos `Path` podem, portanto, atravessar diretamente para muitas APIs de nível mais baixo sem conversão manual para strings.

## 5. `os.fspath()` expõe a representação do sistema de arquivos

```python
import os
from pathlib import Path


path = Path("data") / "input.csv"
raw_path = os.fspath(path)
print(type(raw_path).__name__)
```

Para um `Path` normal, o resultado é uma string.

Use `os.fspath()` quando uma fronteira de API realmente exigir a representação de baixo nível em `str` ou `bytes`. Não espalhe conversões pelo código quando a API já aceita objetos path-like.

## 6. `os.PathLike` é um protocolo, não um modelo concreto de caminho

Um objeto path-like implementa `__fspath__()` e retorna `str` ou `bytes`.

```python
import os


class ReportPath:
    def __fspath__(self):
        return "reports/output.txt"


print(os.fspath(ReportPath()))
```

Em código de aplicação, `pathlib.Path` normalmente é preferível a inventar classes de caminho próprias. O protocolo importa principalmente porque explica a interoperabilidade entre APIs de sistema de arquivos.

## 7. Caminhos `str` geralmente são o padrão mais portável

Muitas funções de `os` suportam caminhos em `str` e `bytes`. Caminhos em bytes são úteis em situações especializadas de baixo nível, especialmente no Unix, mas trazem complexidade de codificação.

Prefira strings Unicode e objetos `Path`, a menos que o programa tenha uma razão específica para preservar bytes brutos do sistema de arquivos.

## 8. `fsencode()` e `fsdecode()` são fronteiras explícitas de codificação

```python
import os


encoded = os.fsencode("notes.txt")
decoded = os.fsdecode(encoded)

print(decoded)
```

Essas funções usam a codificação do sistema de arquivos e o tratador de erros configurados pelo Python.

Elas são ferramentas de fronteira, não uma recomendação para converter todos os caminhos em bytes.

## 9. `os.name` fornece informação ampla sobre a plataforma

```python
import os


print(os.name)
```

Valores comuns incluem `"posix"` e `"nt"`.

Não construa ramificações grandes por plataforma quando a detecção de recurso for mais precisa. O sistema operacional exato pode importar menos do que saber se uma operação específica oferece suporte a `dir_fd`, tratamento de links simbólicos ou outra capacidade.

## 10. O diretório de trabalho atual é estado do processo

```python
import os


current = os.getcwd()
print(type(current).__name__)
```

Caminhos relativos são interpretados em relação ao diretório de trabalho atual do processo.

Isso significa que um caminho relativo não é autocontido. Seu significado depende de estado ambiente.

## 11. `os.chdir()` altera esse estado ambiente

```python
import os


original = os.getcwd()
# os.chdir("another-directory")
# work happens relative to the new current directory
# os.chdir(original)
```

Alterar o diretório de trabalho afeta operações posteriores com caminhos relativos no processo. Em código concorrente ou reutilizável, uma mudança oculta de diretório pode tornar o comportamento difícil de entender.

Prefira caminhos absolutos ou bases explícitas sempre que possível.

## 12. Restaurar o diretório de trabalho não elimina o risco de concorrência

Um padrão de restauração com `try/finally` evita uma classe de bug:

```python
import os


original = os.getcwd()
try:
    pass
    # os.chdir(target)
finally:
    os.chdir(original)
```

Mas, enquanto o diretório estiver alterado, outro código no mesmo processo ainda pode observar esse estado. Restaurar ao final é útil, mas não é isolamento.

## 13. `os.environ` modela o ambiente do processo

`os.environ` é um mapeamento mutável de nomes de variáveis de ambiente para valores string.

```python
import os


mode = os.environ.get("APP_MODE", "development")
print(mode)
```

Variáveis de ambiente costumam ser fronteiras de configuração. Trate-as como entrada externa, não como constantes automaticamente confiáveis.

## 14. `os.getenv()` é conveniente para leituras com valor padrão

```python
import os


timeout_text = os.getenv("APP_TIMEOUT", "30")
print(timeout_text)
```

O resultado continua sendo texto. Converta e valide conforme o contrato da aplicação.

```python
import os


timeout = int(os.getenv("APP_TIMEOUT", "30"))
```

Uma variável ausente e uma variável inválida são condições diferentes. Um valor padrão resolve apenas o caso de ausência.

## 15. Modifique `os.environ` em vez de chamar `putenv()` diretamente

```python
import os


KEY = "APP_MODE"
previous_value = os.environ.get(KEY)

try:
    os.environ[KEY] = "test"
    print(os.getenv(KEY))
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value
```

O exemplo restaura qualquer valor preexistente, então executá-lo em um REPL, notebook ou outro processo de longa duração não apaga o estado de ambiente de quem chamou o código.

Atribuições em `os.environ` atualizam o ambiente do processo por meio do mecanismo apropriado da plataforma.

Chamadas diretas a `os.putenv()` não atualizam o mapeamento Python `os.environ`, por isso modificar o mapeamento normalmente é o contrato mais claro.

## 16. Mudanças no ambiente não reescrevem o processo pai

Um processo Python pode modificar seu próprio ambiente e o ambiente herdado por processos filhos criados depois. Ele não pode alterar retroativamente o mapeamento de ambiente do shell ou processo pai que o iniciou.

Pense na herança de ambiente como configuração descendente de processos, não como armazenamento mutável compartilhado entre processos independentes.

## 17. Valores de ambiente são strings

```python
import os


KEY = "WORKER_COUNT"
previous_value = os.environ.get(KEY)

try:
    os.environ[KEY] = "4"
    worker_count = int(os.environ[KEY])
    print(worker_count + 1)
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value
```

A mesma regra de restauração vale quando um valor de ambiente é alterado temporariamente apenas para demonstrar parsing.

Use parsing explícito para inteiros, booleanos, listas, caminhos, URLs e outras configurações estruturadas.

## 18. `os.environ` é um mapeamento em cache

O mapeamento é capturado quando `os` é importado, normalmente durante a inicialização do interpretador. Alterações feitas por `os.environ` permanecem sincronizadas, mas modificações do ambiente realizadas fora desse mapeamento podem não aparecer automaticamente.

Essa distinção importa principalmente em cenários avançados de embedding ou integração nativa.

## 19. `os.reload_environ()` é novo no Python 3.14

O Python 3.14 adiciona:

```python
import os


# os.reload_environ()
```

A função atualiza `os.environ` e `os.environb` a partir do ambiente atual do processo.

A documentação oficial alerta que `os.reload_environ()` **não é thread-safe**. Não use casualmente em um processo no qual outras threads possam ler ou modificar o ambiente simultaneamente.

## 20. `os.sep` e `os.pathsep` resolvem problemas diferentes

```python
import os


print(repr(os.sep))
print(repr(os.pathsep))
```

`os.sep` é o separador de componentes de caminho, como `/` ou `\`.

`os.pathsep` separa entradas em variáveis de ambiente que contêm listas de caminhos, como `PATH`, normalmente `:` em POSIX e `;` no Windows.

Confundir os dois é um bug clássico de portabilidade.

## 21. Prefira composição consciente de caminhos a separadores manuais

Evite:

```python
base = "reports"
filename = "summary.txt"
path = base + "/" + filename
```

Prefira `Path` ou, ao trabalhar com a interface procedural de `os.path`, `os.path.join()`:

```python
import os


path = os.path.join("reports", "summary.txt")
print(path)
```

O separador é uma preocupação da plataforma, não uma regra de concatenação de strings.

## 22. `os.path` continua sendo um toolkit útil de baixo nível

Funções comuns incluem:

```text
os.path.join()
os.path.basename()
os.path.dirname()
os.path.splitext()
os.path.abspath()
os.path.realpath()
os.path.exists()
os.path.isfile()
os.path.isdir()
```

Use `pathlib` quando código orientado a objetos de caminho for mais claro. Use `os.path` ao trabalhar com APIs existentes baseadas em strings, caminhos em bytes ou código de nível mais baixo onde seu estilo procedural seja natural.

## 23. Normalização não é uma única operação universal

`abspath()`, `realpath()` e manipulação lexical de caminhos respondem perguntas diferentes. Links simbólicos podem tornar uma aparente limpeza de segmentos `..` semanticamente importante.

Não normalize um caminho apenas para ele parecer mais bonito. Decida se você precisa de um caminho lexical, absoluto ou resolvido por meio dos links do sistema de arquivos.

## 24. Crie um diretório com `os.mkdir()`

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "reports")
    os.mkdir(path)
    print(os.path.isdir(path))
```

`mkdir()` cria um nível de diretório. Pais ausentes causam erro.

## 25. Crie diretórios pais ausentes com `os.makedirs()`

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "year", "month", "reports")
    os.makedirs(path)
    print(os.path.isdir(path))
```

`makedirs()` cria recursivamente os diretórios intermediários necessários.

## 26. `exist_ok=True` expressa criação idempotente de diretório

```python
import os
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = os.path.join(temp_dir, "output")
    os.makedirs(path, exist_ok=True)
    os.makedirs(path, exist_ok=True)
    print(os.path.isdir(path))
```

Use quando um diretório já existente for uma pré-condição aceitável. Não use quando a existência prévia deveria ser tratada como conflito.

## 27. `os.listdir()` retorna nomes em ordem arbitrária

```python
import os


names = os.listdir(".")
print(type(names).__name__)
```

A API não promete resultados ordenados.

Quando saída, testes, archives, manifests ou ordem de processamento precisarem ser determinísticos, ordene explicitamente:

```python
import os


for name in sorted(os.listdir(".")):
    pass
```

## 28. `os.scandir()` produz entradas de diretório mais ricas

```python
import os


with os.scandir(".") as entries:
    for entry in entries:
        if entry.is_file():
            pass
```

`scandir()` produz objetos `os.DirEntry` que podem expor tipo de arquivo e metadados de forma eficiente. Código que precisa desses atributos pode evitar buscas repetidas de caminho em comparação com `listdir()` seguido de chamadas separadas a `stat()`.

## 29. Use o iterador de `scandir()` como context manager

```python
import os


with os.scandir(".") as entries:
    first_names = sorted(entry.name for entry in entries)[:3]

print(type(first_names).__name__)
```

O context manager garante que recursos da varredura de diretório sejam fechados prontamente mesmo quando a iteração termina cedo.

## 30. Metadados de `DirEntry` podem ser armazenados em cache

Um `DirEntry` pode armazenar em cache informações obtidas do sistema operacional.

Isso é ótimo para uma varredura curta de diretório. Não é uma promessa de que o objeto permaneça uma visão ao vivo para sempre.

Se os metadados puderem ter mudado desde a varredura, chame `os.stat(entry.path)` novamente em vez de tratar um `DirEntry` antigo como verdade atual.

## 31. `os.stat()` retorna metadados estruturados do sistema de arquivos

```python
import os
from tempfile import NamedTemporaryFile


with NamedTemporaryFile() as temp_file:
    info = os.stat(temp_file.name)
    print(info.st_size)
```

Campos úteis incluem tamanho do arquivo e vários timestamps. O significado exato e a disponibilidade podem variar por plataforma e sistema de arquivos.

## 32. Prefira campos de timestamp em nanossegundos quando precisão inteira exata importar

`stat_result` expõe variantes em nanossegundos como `st_mtime_ns` onde suportado.

```python
import os
from tempfile import NamedTemporaryFile


with NamedTemporaryFile() as temp_file:
    info = os.stat(temp_file.name)
    print(isinstance(info.st_mtime_ns, int))
```

Campos de timestamp em ponto flutuante são convenientes, mas nanossegundos inteiros evitam uma etapa desnecessária de representação binária em float.

## 33. Não interprete `st_ctime` como horário universal de criação

A semântica de timestamps varia entre plataformas. Historicamente, `st_ctime` representa tempo de alteração de metadados no Unix e informação relacionada à criação no Windows.

Quando horário de criação ou nascimento for requisito, consulte os campos específicos da plataforma e a documentação em vez de atribuir um significado universal a `ctime`.

## 34. Remova um arquivo com `os.remove()` ou `os.unlink()`

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "temporary.txt"
    path.write_text("temporary", encoding="utf-8")
    os.remove(path)
    print(path.exists())
```

Para caminhos comuns do sistema de arquivos, `os.remove()` e `os.unlink()` são aliases com o mesmo comportamento.

## 35. `os.rmdir()` remove apenas um diretório vazio

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    child = Path(temp_dir) / "empty"
    child.mkdir()
    os.rmdir(child)
    print(child.exists())
```

Essa restrição é útil. Remoção recursiva é uma operação muito maior e pertence a uma API mais explícita como `shutil.rmtree()`.

## 36. `os.rename()` não possui comportamento idêntico de sobrescrita em todas as plataformas

```python
import os


# os.rename(source, destination)
```

Renomear depende das regras do sistema operacional, do tipo do destino e das fronteiras do sistema de arquivos. O comportamento diante de um destino existente varia entre plataformas.

Se sobrescrever o destino fizer parte do contrato, use uma API cujas semânticas de substituição expressem essa intenção.

## 37. `os.replace()` expressa intenção de substituição

```python
import os


# os.replace(source, destination)
```

Se o destino for um arquivo existente e as permissões permitirem substituição, `replace()` foi projetado para substituí-lo sem exigir uma etapa separada de exclusão.

A operação pode falhar entre sistemas de arquivos diferentes. Em POSIX, uma substituição bem-sucedida por semântica de rename deve ser atômica.

## 38. Evite corridas de check-then-act

Este padrão é frágil:

```python
import os


path = "report.txt"
if os.path.exists(path):
    pass
    # open(path)
```

O sistema de arquivos pode mudar entre a verificação e a operação.

Prefira executar a operação e tratar a exceção relevante:

```python
try:
    with open("report.txt", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    content = ""
```

Esse é um exemplo de EAFP: é mais fácil pedir perdão do que permissão.

## 39. `os.access()` não é um teste geral de autorização antes da operação

`os.access()` possui usos especializados, incluindo verificações de permissão com IDs reais no Unix.

Não o use como pré-verificação universal de "posso abrir este arquivo com segurança?". A documentação oficial alerta que check-then-open cria uma janela de corrida, e sistemas de arquivos de rede podem ter semânticas de permissão além do modelo local de bits.

## 40. `os.walk()` percorre uma árvore de diretórios

```python
import os


for root, dirnames, filenames in os.walk("."):
    print(root, len(dirnames), len(filenames))
    break
```

Cada iteração produz:

```text
(root path, child directory names, child file names)
```

As listas de filhos contêm nomes, não caminhos completos.

## 41. Percurso top-down permite podar a recursão

Quando `topdown=True`, modifique `dirnames` in-place para controlar quais diretórios serão visitados:

```python
import os


for root, dirnames, filenames in os.walk(".", topdown=True):
    dirnames[:] = [name for name in dirnames if name != "__pycache__"]
```

Atribuir uma nova lista local sem modificar `dirnames` não poda o percurso.

## 42. Ordene nomes de diretórios quando a ordem de travessia importar

```python
import os


for root, dirnames, filenames in os.walk("."):
    dirnames.sort()
    filenames.sort()
```

A ordem de enumeração de diretórios não é um contrato determinístico. Ordene quando o comportamento posterior depender da ordem.

## 43. Seguir symlinks de diretório pode criar ciclos

Por padrão, `os.walk()` não segue links simbólicos que apontam para diretórios.

Com `followlinks=True`, um link pode apontar de volta para um ancestral e criar recursão sem limite. `os.walk()` não mantém automaticamente um registro completo de todos os diretórios já visitados.

Seguir links deve ser uma decisão deliberada de travessia de grafo, não uma flag de conveniência.

## 44. `onerror` torna explícita a política de falha na travessia

```python
import os


def handle_error(error: OSError) -> None:
    print(type(error).__name__)


for _ in os.walk(".", onerror=handle_error):
    break
```

Sem `onerror`, erros de varredura são ignorados por `walk()`. Um callback pode registrar o erro e continuar, ou levantá-lo novamente para abortar.

## 45. `os.fwalk()` adiciona um descritor de arquivo de diretório

`fwalk()` produz:

```text
(dirpath, dirnames, filenames, dirfd)
```

O descritor permite operações relativas ao diretório atualmente visitado sem reconstruir caminhos completos.

É uma ferramenta avançada. O descritor produzido só é válido até a próxima etapa da iteração, a menos que seja duplicado.

## 46. Suporte a `dir_fd` depende das capacidades da plataforma

Várias APIs de `os` podem operar em relação a um descritor de diretório aberto.

Não assuma que toda plataforma oferece suporte a toda combinação de `dir_fd`. Python expõe conjuntos de capacidades como:

```python
import os


print(isinstance(os.supports_dir_fd, set))
print(isinstance(os.supports_follow_symlinks, set))
```

Detecção de recurso é melhor do que fingir que todos os sistemas operacionais expõem primitivas idênticas de sistema de arquivos.

## 47. Comportamento de links simbólicos precisa de política explícita

Muitas APIs de sistema de arquivos aceitam `follow_symlinks` ou opções equivalentes.

A escolha altera se uma operação atinge:

```text
the symbolic link itself
or
the object referenced by the link
```

Essa distinção pode afetar metadados, fronteiras de exclusão, segurança e portabilidade.

## 48. Use `shutil.copyfile()` para conteúdo de arquivo apenas

```python
import shutil


# shutil.copyfile("source.txt", "destination.txt")
```

`copyfile()` copia os dados para um nome completo de arquivo de destino. Não promete preservação de metadados.

Se origem e destino identificarem o mesmo arquivo, `SameFileError` será levantada.

## 49. `shutil.copy()` também copia o modo de permissão

```python
import shutil


# shutil.copy("source.txt", "backup/")
```

`copy()` pode aceitar um diretório de destino. Além dos dados do arquivo, copia o modo de permissão.

Não tenta a preservação mais ampla de metadados de `copy2()`.

## 50. `shutil.copy2()` tenta preservar mais metadados

```python
import shutil


# shutil.copy2("source.txt", "destination.txt")
```

`copy2()` usa `copystat()` para tentar preservar metadados como bits de permissão, tempo de acesso, tempo de modificação, flags e alguns atributos estendidos onde suportados.

A palavra **tenta** importa.

## 51. Nenhuma cópia de `shutil` é um clone completo de metadados

A documentação oficial alerta explicitamente que funções de cópia de alto nível não conseguem preservar todos os tipos de metadados em todas as plataformas.

Exemplos de metadados que podem não ser preservados incluem proprietário, ACLs, resource forks ou alternate data streams, dependendo do sistema operacional.

Se replicação exata de metadados do sistema de arquivos for requisito, verifique a plataforma-alvo e use ferramentas projetadas para esse contrato.

## 52. `follow_symlinks` altera a semântica da cópia

Com uma origem que é symlink:

```text
follow_symlinks=True  -> copy the referenced object's contents
follow_symlinks=False -> recreate a symbolic link where supported
```

Não escolha a flag depois que o código estiver pronto. Primeiro decida se links são topologia ou indireção no modelo de dados.

## 53. `copymode()` e `copystat()` separam operações de metadados

```python
import shutil


# shutil.copymode(source, destination)
# shutil.copystat(source, destination)
```

`copymode()` copia bits de permissão.

`copystat()` tenta copiar um conjunto mais amplo de metadados sem copiar conteúdo do arquivo, proprietário ou grupo.

Esses helpers são úteis quando cópia de dados e cópia de metadados são etapas diferentes do fluxo.

## 54. `shutil.copytree()` copia uma árvore de diretórios

```python
import shutil


# shutil.copytree(source_dir, destination_dir)
```

Por padrão, `copytree()` cria recursivamente a árvore de destino e usa `copy2()` para arquivos individuais.

Uma cópia recursiva é um fluxo, não uma única operação de arquivo. Defina conscientemente políticas de existência do destino, symlink, exclusão e erro.

## 55. `dirs_exist_ok` controla a mesclagem com o destino

```python
import shutil


# shutil.copytree(source, destination, dirs_exist_ok=True)
```

Quando `False`, o padrão, um diretório de destino já existente é um conflito.

Quando `True`, diretórios existentes podem ser reutilizados e arquivos correspondentes no destino podem ser sobrescritos.

Essa chave pode transformar uma operação de "criar backup" em "mesclar na árvore existente", então nomeie e documente a política claramente.

## 56. `ignore_patterns()` cria um filtro de cópia reutilizável

```python
import shutil


ignore = shutil.ignore_patterns("*.tmp", "__pycache__")
# shutil.copytree(source, destination, ignore=ignore)
```

Padrões de exclusão são aplicados recursivamente por nome em cada diretório visitado por `copytree()`.

Trate dados ignorados como parte do contrato de backup ou implantação. Um padrão que omite arquivos necessários silenciosamente continua sendo um bug de correção.

## 57. `copytree()` pode agregar erros de múltiplos arquivos

Uma cópia recursiva pode encontrar mais de uma falha. `shutil.Error` pode conter múltiplas tuplas `(source, destination, exception)` coletadas durante a operação.

Quando confiabilidade importa, não reduza uma falha multi-arquivo a uma mensagem genérica de "copy failed". Preserve contexto suficiente para diagnosticar quais caminhos falharam.

## 58. `shutil.move()` manipula arquivos e árvores de diretórios

```python
import shutil


# final_path = shutil.move(source, destination)
```

Se o destino for um diretório existente, a origem normalmente é movida para dentro dele.

O contrato exato de destino deve estar explícito no código porque "mover para este caminho" e "mover para dentro deste diretório" são operações diferentes.

## 59. Mover pode virar copiar-e-excluir

`shutil.move()` prefere uma operação do tipo rename quando possível. Quando isso não puder ser usado, como entre sistemas de arquivos, pode fazer fallback para copiar e depois remover a origem.

Isso significa que um move não é universalmente uma única operação atômica de metadados.

Para fluxos que exigem substituição atômica, garantias de mesmo sistema de arquivos e uma API como `os.replace()` podem ser mais adequadas.

## 60. Exclusão recursiva merece uma fronteira rígida

```python
import shutil


# shutil.rmtree(target_directory)
```

`rmtree()` exclui uma árvore inteira de diretórios.

Antes de chamá-la em software real, valide o alvo a partir de estado confiável. Um erro de digitação, valor de configuração vazio, diretório-base incorreto ou erro de fronteira com symlink pode transformar limpeza em perda de dados.

## 61. Prefira validação positiva do alvo antes de operações destrutivas

Um fluxo destrutivo pode validar se o alvo resolvido pertence a um workspace esperado antes de excluir.

```python
from pathlib import Path


workspace = Path("build").resolve()
target = (workspace / "temporary").resolve()

if target.parent != workspace:
    raise ValueError("unexpected cleanup target")
```

Este exemplo é intencionalmente estrito. Políticas reais com níveis aninhados podem precisar de `Path.is_relative_to()` ou outra regra explícita de contenção.

A validação reduz erros acidentais de escopo, mas corridas do sistema de arquivos e comportamento de symlinks ainda exigem projeto cuidadoso em ambientes hostis.

## 62. `rmtree()` tem resistência a ataques de symlink dependente da plataforma

Em plataformas com as APIs necessárias baseadas em descritores de arquivo, Python usa por padrão uma implementação de `rmtree()` resistente a ataques de symlink.

Você pode inspecionar:

```python
import shutil


print(isinstance(shutil.rmtree.avoids_symlink_attacks, bool))
```

Uma aplicação sensível à segurança não deve assumir que toda plataforma suportada fornece a mesma proteção.

## 63. `onexc` é o callback moderno de erro de `rmtree()`

O Python 3.12 adicionou `onexc` e depreciou o callback antigo `onerror`.

```python
import shutil


def handle_remove_error(function, path, exception):
    print(type(exception).__name__)


# shutil.rmtree(target, onexc=handle_remove_error)
```

O callback pode inspecionar a operação, caminho e exceção. Exceções levantadas pelo callback propagam.

## 64. `rmtree()` mudou o tratamento de arquivo ausente no Python 3.13

Desde o Python 3.13, `rmtree()` ignora `FileNotFoundError` para entradas abaixo do alvo de nível superior enquanto a travessia está em andamento.

Um caminho raiz solicitado que esteja ausente continua importando.

Isso torna o desaparecimento concorrente de entradas internas menos disruptivo sem transformar uma raiz ausente em sucesso silencioso.

## 65. `shutil.disk_usage()` relata capacidade do sistema de arquivos

```python
import shutil


usage = shutil.disk_usage(".")
print(hasattr(usage, "free"))
```

A named tuple contém contagens de bytes total, usados e livres.

Os valores reais dependem do ambiente. Não os fixe em testes ou exemplos de documentação.

## 66. `shutil.which()` resolve executáveis por um caminho de busca

```python
import shutil


python_path = shutil.which("python")
print(python_path is None or isinstance(python_path, str))
```

Por padrão, `which()` consulta a variável de ambiente `PATH` do processo e usa `os.pathsep` para interpretar sua lista de diretórios.

O resultado exato depende do ambiente, então código de aplicação precisa lidar com `None`.

## 67. `copyfileobj()` copia entre objetos file-like abertos

```python
import io
import shutil


source = io.StringIO("alpha\nbeta\n")
destination = io.StringIO()
shutil.copyfileobj(source, destination)
print(destination.getvalue())
```

Isso trabalha no nível de streams em vez de receber nomes de caminhos.

Para objetos de arquivo reais com buffer, `copyfileobj()` não garante que o destino foi descarregado ao retornar. Faça flush ou feche antes de outro consumidor precisar observar os dados copiados.

## 68. Funções de cópia de alto nível podem usar chamadas rápidas do sistema

Desde o Python 3.8, várias operações de cópia de `shutil` podem usar internamente syscalls específicas da plataforma para cópia rápida.

A otimização é um detalhe de implementação por trás da mesma API pública. Não duplique manualmente um loop de leitura/escrita apenas supondo que será mais rápido.

O Python 3.14 expandiu algumas dessas otimizações de plataforma, incluindo possibilidades adicionais de copy-on-write ou cópia no lado do servidor em sistemas suportados.

## 69. `make_archive()` cria uma árvore empacotada

```python
import shutil


# archive_path = shutil.make_archive("backup", "zip", root_dir="workspace")
```

O caminho retornado inclui a extensão escolhida pelo formato.

Criar um archive é diferente de clonar o sistema de arquivos byte a byte. Metadados e capacidades do formato variam.

## 70. Extração de archive é uma fronteira de confiança

```python
import shutil


# shutil.unpack_archive("backup.zip", "restored")
```

Nunca trate extração de um archive não confiável como uma simples cópia inofensiva.

Entradas de archive podem tentar influenciar caminhos de destino, links, permissões ou outros comportamentos do sistema de arquivos. Os padrões de extração incorporados do Python 3.14 bloqueiam os casos de caminho mais perigosos, mas a documentação oficial ainda recomenda inspeção e uma política explícita de confiança.

## 71. Filtros de extração tar ficaram mais seguros por padrão no Python 3.14

Para formatos baseados em tar, `shutil.unpack_archive()` passa a filtragem de extração para a implementação de tar subjacente. O filtro `"data"` é o padrão a partir do Python 3.14.

```python
import shutil


# shutil.unpack_archive("backup.tar", "restored", filter="data")
```

Extração ZIP não aceita esse argumento `filter`.

Um padrão mais seguro reduz risco. Não torna archives arbitrários e não confiáveis automaticamente seguros para toda aplicação.

## 72. Exceções de sistema de arquivos fazem parte do design

Exceções comuns incluem:

```text
FileNotFoundError
FileExistsError
PermissionError
NotADirectoryError
IsADirectoryError
OSError
shutil.SameFileError
shutil.SpecialFileError
shutil.Error
```

Capture a exceção mais estreita que represente um ramo esperado do fluxo. Deixe falhas inesperadas continuarem visíveis.

## 73. Um contrato prático de ambiente

```python
import os


KEY = "PYTHON_STUDY_GUIDE_MODE"
MISSING_KEY = "PYTHON_STUDY_GUIDE_MISSING"
previous_value = os.environ.get(KEY)
previous_missing = os.environ.pop(MISSING_KEY, None)

try:
    os.environ[KEY] = "practice"
    print(f"configured: {os.getenv(KEY)}")
    print(f"fallback: {os.getenv(MISSING_KEY, 'default')}")
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value

    if previous_missing is not None:
        os.environ[MISSING_KEY] = previous_missing
```

```text
configured: practice
fallback: default
```

O exemplo modifica apenas o ambiente do próprio processo e restaura qualquer valor anterior.

## 74. Uma varredura determinística de diretório

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    (workspace / "alpha.txt").write_text("alpha\n", encoding="utf-8")
    (workspace / "data").mkdir()
    (workspace / "data" / "values.txt").write_text("1\n2\n", encoding="utf-8")

    with os.scandir(workspace) as entries:
        for entry in sorted(entries, key=lambda item: item.name):
            kind = "dir" if entry.is_dir() else "file"
            print(f"{entry.name}: {kind}")
```

```text
alpha.txt: file
data: dir
```

O detalhe importante é o sort explícito. `scandir()` por si só não promete ordem de diretório.

## 75. Um `walk` prático com poda

```python
import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    (workspace / "src").mkdir()
    (workspace / "src" / "app.py").write_text("print('ready')\n", encoding="utf-8")
    (workspace / "cache").mkdir()
    (workspace / "cache" / "ignored.bin").write_bytes(b"ignored")

    for root, dirnames, filenames in os.walk(workspace, topdown=True):
        dirnames[:] = sorted(name for name in dirnames if name != "cache")
        filenames.sort()

        relative_root = Path(root).relative_to(workspace)
        label = "." if relative_root == Path(".") else relative_root.as_posix()
        print(f"{label}: {filenames}")
```

```text
.: []
src: ['app.py']
```

O diretório `cache` é removido de `dirnames` antes que a recursão chegue até ele.

## 76. Um fluxo prático de cópia de árvore e movimentação

```python
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source = workspace / "source"
    destination = workspace / "backup"
    archive = workspace / "archive"

    (source / "reports").mkdir(parents=True)
    (source / "reports" / "summary.txt").write_text("ready\n", encoding="utf-8")
    (source / "scratch.tmp").write_text("temporary\n", encoding="utf-8")

    shutil.copytree(source, destination, ignore=shutil.ignore_patterns("*.tmp"))
    archive.mkdir()
    moved_path = Path(shutil.move(destination / "reports" / "summary.txt", archive))

    copied_names = sorted(path.name for path in destination.iterdir())
    print(f"backup entries: {copied_names}")
    print(f"moved file: {moved_path.name}")
    print(f"content: {moved_path.read_text(encoding='utf-8').strip()}")
```

```text
backup entries: ['reports']
moved file: summary.txt
content: ready
```

O arquivo temporário ignorado nunca entra na árvore copiada, e o caminho retornado pelo move é tratado como dado em vez de ser adivinhado.

## 77. Erros comuns

### Erro: separadores manuais de caminho

```python
path = "reports/" + "summary.txt"
```

Prefira `Path` ou `os.path.join()`.

### Erro: alterar o diretório de trabalho dentro de um helper reutilizável

Um `os.chdir()` oculto pode mudar o significado de caminhos relativos em código não relacionado.

### Erro: tratar strings do ambiente como configuração já validada

```python
import os


workers = os.getenv("WORKERS", "4")
# workers + 1  # TypeError
```

Converta o texto externo para o tipo necessário e valide sua faixa.

### Erro: depender da ordem de enumeração de diretórios

`listdir()`, `scandir()` e travessia do sistema de arquivos não devem ser presumidos como alfabéticos.

### Erro: usar `os.access()` antes de `open()` como garantia de segurança

O caminho pode mudar entre a verificação e o uso. Tente o I/O e trate a exceção.

### Erro: dizer que `copy2()` copia tudo

Ela tenta preservar mais metadados que `copy()`, mas as garantias continuam dependentes da plataforma.

### Erro: usar `dirs_exist_ok=True` sem perceber que isso faz merge

Essa flag pode sobrescrever arquivos em uma árvore de destino existente.

### Erro: ativar `followlinks=True` sem tratamento de ciclos

Um symlink para um ancestral pode produzir travessia sem limite.

### Erro: chamar `rmtree()` com um caminho montado a partir de entrada externa não verificada

Exclusão recursiva deve operar sobre um alvo validado sob uma base confiável.

### Erro: extrair archives não confiáveis diretamente em um diretório sensível

Extração de archive é uma fronteira de validação de entrada e segurança do sistema de arquivos.

## 78. Tabela de decisão

| Requisito | Prefira |
|---|---|
| modelar e compor caminhos | `pathlib.Path` |
| manipulação procedural de caminho em baixo nível | `os.path` |
| ler ambiente do processo | `os.environ` / `os.getenv()` |
| converter objeto path-like para `str` ou `bytes` | `os.fspath()` |
| criar um diretório | `os.mkdir()` |
| criar diretórios pais recursivamente | `os.makedirs()` |
| listar apenas nomes | `os.listdir()` |
| varrer nomes mais pistas de tipo ou metadados | `os.scandir()` |
| inspecionar metadados | `os.stat()` |
| remover um arquivo | `os.remove()` / `os.unlink()` |
| remover um diretório vazio | `os.rmdir()` |
| substituir destino por semântica de rename | `os.replace()` |
| percorrer árvore de diretórios | `os.walk()` |
| copiar somente conteúdo do arquivo | `shutil.copyfile()` |
| copiar arquivo mais modo de permissão | `shutil.copy()` |
| tentar preservação mais ampla de metadados | `shutil.copy2()` |
| copiar árvore de diretórios | `shutil.copytree()` |
| mover arquivo ou árvore | `shutil.move()` |
| remover árvore recursivamente | `shutil.rmtree()` com validação rígida do alvo |
| inspecionar capacidade | `shutil.disk_usage()` |
| resolver um executável | `shutil.which()` |
| criar archive | `shutil.make_archive()` |
| extrair archive confiável ou validado | `shutil.unpack_archive()` |

## 79. Referência rápida

```text
os.getcwd()
os.chdir(path)

os.environ["KEY"]
os.environ.get("KEY")
os.getenv("KEY", default)
os.reload_environ()                 # Python 3.14+, not thread-safe

os.fspath(path)
os.fsencode(path)
os.fsdecode(path)
os.sep
os.pathsep
os.path.join(...)
os.path.abspath(path)
os.path.realpath(path)

os.mkdir(path)
os.makedirs(path, exist_ok=True)
os.listdir(path)
os.scandir(path)
os.stat(path)
os.remove(path)
os.unlink(path)
os.rmdir(path)
os.rename(src, dst)
os.replace(src, dst)
os.walk(path)
os.fwalk(path)

os.supports_dir_fd
os.supports_follow_symlinks
os.supports_fd

shutil.copyfile(src, dst)
shutil.copy(src, dst)
shutil.copy2(src, dst)
shutil.copymode(src, dst)
shutil.copystat(src, dst)
shutil.copytree(src, dst)
shutil.ignore_patterns(...)
shutil.move(src, dst)
shutil.rmtree(path)
shutil.disk_usage(path)
shutil.which(command)
shutil.copyfileobj(source, destination)
shutil.make_archive(...)
shutil.unpack_archive(...)
```

## 80. Checklist de design

Antes que um fluxo de sistema de arquivos atravesse para `os` ou `shutil`, pergunte:

- `Path` já é suficiente para a parte de modelagem de caminhos?
- O caminho de entrada é confiável, validado ou fornecido externamente?
- A operação depende do diretório de trabalho atual?
- Posso tornar o caminho-base explícito?
- O texto do ambiente é convertido e validado antes do uso?
- Saída determinística exige ordenar entradas de diretório?
- Estou mantendo dados de `DirEntry` além das premissas de atualização deles?
- O sistema de arquivos pode mudar entre uma pré-verificação e a operação real?
- Devo tentar a operação e tratar uma exceção em vez disso?
- O destino pode existir previamente?
- Sobrescrita ou substituição é intencional?
- Origem e destino podem estar em sistemas de arquivos diferentes?
- Qual é a política de links simbólicos?
- A travessia pode seguir um ciclo?
- A cópia recursiva faz merge com árvore existente?
- Quais metadados realmente precisam ser preservados?
- A exclusão recursiva está restrita a uma base validada positivamente?
- O archive é confiável, inspecionado ou extraído em local isolado?
- A plataforma-alvo suporta a capacidade avançada que pretendo usar?
- Um comportamento específico de versão do Python está documentado?
- Caminhos destrutivos foram testados primeiro com diretórios temporários?

## 81. Exercício

Construa uma ferramenta fictícia de backup de workspace com estes requisitos:

1. Leia os diretórios-base de origem e destino por argumentos de função, não por `chdir()`.
2. Aceite uma variável de ambiente opcional `BACKUP_MODE` com padrão documentado.
3. Valide que o modo pertence a um pequeno conjunto permitido.
4. Percorra recursivamente a árvore de origem.
5. Ignore diretórios chamados `cache` e `__pycache__` podando `dirnames` em um `os.walk()` top-down.
6. Ordene diretórios e arquivos antes de produzir um manifest.
7. Recuse copiar quando o diretório de origem não existir.
8. Copie a árvore com `shutil.copytree()` e política explícita para ignorar `*.tmp`.
9. Decida se destino existente é erro ou merge e documente a escolha.
10. Retorne um resumo com quantidade de arquivos copiados e caminho de destino.
11. Não exclua nada recursivamente a menos que o alvo seja comprovadamente interno a um workspace temporário dedicado.
12. Capture somente exceções esperadas de sistema de arquivos e deixe erros inesperados visíveis.

Desafios de extensão:

- adicione modo dry-run que liste ações planejadas sem modificar o sistema de arquivos;
- registre tamanhos com `os.stat()`;
- resolva um compressor externo opcional com `shutil.which()` e lide com `None`;
- crie um ZIP com `shutil.make_archive()`;
- escreva testes com `tempfile.TemporaryDirectory()` para não tocar arquivos reais do usuário;
- documente como links simbólicos devem ser tratados.

## 82. Conexões com conceitos anteriores de Python

`os` e `shutil` conectam vários tópicos anteriores:

- **Arquivos e context managers:** operações de sistema de arquivos ainda dependem do ciclo de vida correto dos recursos.
- **Exceções:** subclasses de `OSError` são fronteiras normais de controle para falhas esperadas de I/O.
- **`pathlib`:** objetos de caminho compõem naturalmente com APIs de `os` e `shutil` que aceitam path-like.
- **Strings:** variáveis de ambiente e várias fronteiras de caminho chegam como texto.
- **Coleções:** `os.environ` se comporta como mapping, `walk()` produz listas e travessias frequentemente constroem manifests.
- **Funções:** operações seguras de arquivos se beneficiam de helpers pequenos com origem, destino e políticas explícitas.
- **Logging:** fluxos recursivos de cópia, movimentação e limpeza são lugares naturais para evidência operacional estruturada.
- **`datetime`:** metadados de arquivo contêm timestamps cuja semântica de plataforma precisa ser interpretada com cuidado.
- **`json` e `csv`:** utilitários de sistema de arquivos frequentemente descobrem, movem ou arquivam arquivos que depois são analisados sob contratos separados de formato.
- **`itertools`:** listas grandes de arquivos podem ser processadas de forma lazy após descoberta, mas o sistema de arquivos ainda pode mudar durante a iteração.
- **`decimal`:** timestamps inteiros `st_*_ns` mostram novamente que a escolha de representação faz parte do contrato de dados.

## Referências

Referências primárias usadas neste capítulo:

- [Documentação Python 3.14: `os` - interfaces diversas de sistema operacional](https://docs.python.org/3.14/library/os.html)
- [Documentação Python 3.14: `shutil` - operações de arquivo de alto nível](https://docs.python.org/3.14/library/shutil.html)
- [Documentação Python 3.14: `pathlib` - caminhos de sistema de arquivos orientados a objetos](https://docs.python.org/3.14/library/pathlib.html)
- [Documentação Python 3.14: `os.path` - manipulações comuns de caminhos](https://docs.python.org/3.14/library/os.path.html)
- [Glossário Python: EAFP](https://docs.python.org/3.14/glossary.html#term-EAFP)

## Fase 8 concluída

Este capítulo encerra a **Fase 8: Standard Library**.

A fase começou com modelagem orientada a objetos em `pathlib` e avançou por contratos de data e hora, formatos estruturados de dados, logging, coleções especializadas, iteração lazy, aritmética decimal e finalmente a própria fronteira do sistema operacional.

A próxima fase planejada é a **Fase 9: Bibliotecas Externas**, começando por `pandas` quando essa fase estiver disponível.
