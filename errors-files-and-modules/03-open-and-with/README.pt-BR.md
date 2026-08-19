<div align="center">

# Abrindo Arquivos com Segurança com `open()` e `with`

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Erros, Arquivos e Módulos](../README.pt-BR.md) · [← Anterior: Levantando Exceções e Criando Exceções Personalizadas](../02-raise-and-custom-exceptions/README.pt-BR.md)

Programas frequentemente precisam que os dados continuem existindo depois que o processo termina. Um arquivo de texto pode armazenar anotações, configuração, exportações, logs ou resultados intermediários que uma execução futura poderá ler novamente.

A função embutida `open()` do Python cria um **objeto arquivo** conectado a um arquivo ou a outro recurso semelhante a arquivo. A instrução `with` dá a esse recurso um tempo de vida claro, garantindo seu fechamento mesmo quando o bloco termina por causa de uma exceção.

Este capítulo se concentra em **arquivos de texto simples e gerenciamento seguro de recursos**. O Capítulo 04 usará essa base para trabalhar com TXT, CSV e JSON como formatos de dados.

**Tempo estimado de estudo:** 100–130 minutos.

**Requisito de Python:** Python 3.10 ou mais recente. O comportamento de arquivos ensinado aqui foi verificado na documentação oficial do Python 3.14.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que `open()` retorna e por que um objeto arquivo é um recurso que deve ser fechado;
- abrir arquivos de texto com modos explícitos e uma codificação explícita;
- explicar as diferenças práticas entre `r`, `w`, `a` e `x`;
- ler um arquivo pequeno inteiro, uma linha ou linhas de forma incremental;
- escrever e acrescentar texto controlando caracteres de nova linha deliberadamente;
- usar `with` para que um arquivo seja fechado tanto em saídas normais quanto excepcionais;
- conectar `with` ao papel de limpeza visto anteriormente com `finally`;
- tratar exceções comuns de arquivos na fronteira apropriada;
- explicar por que caminhos relativos dependem do diretório de trabalho atual;
- evitar truncamento acidental, surpresas de codificação e leituras completas desnecessárias;
- distinguir modo texto de modo binário em nível introdutório;
- escolher um padrão básico seguro para tarefas comuns com arquivos.

## 1. Arquivos introduzem persistência

Variáveis vivem na memória enquanto um processo Python está em execução. Quando o processo termina, variáveis locais comuns desaparecem.

Um arquivo oferece ao programa um lugar para armazenar dados fora desse processo:

```text
memória do programa
        ↓ escrita
arquivo de texto no armazenamento
        ↓ leitura posterior
outra execução do programa
```

Essa persistência é útil, mas também introduz novas possibilidades de falha: um caminho pode não existir, a permissão pode ser negada, o texto pode usar uma codificação inesperada ou o programa pode abrir um arquivo existente em um modo destrutivo.

## 2. `open()` retorna um objeto arquivo

Uma chamada comum em modo texto se parece com isto:

```python
file = open("notes.txt", "r", encoding="utf-8")
```

`open()` não retorna diretamente o texto do arquivo. Ele retorna um **objeto arquivo** que oferece operações como `read()`, iteração, `write()` e `close()`.

O objeto também acompanha estado, como se está aberto e qual é a posição atual de leitura ou escrita.

## 3. O modelo simplificado de `open()`

A função embutida completa possui mais parâmetros, mas um bom modelo para iniciantes é:

```python
open(file, mode="r", encoding=None)
```

Para arquivos de texto, pense em três perguntas antes de abrir qualquer coisa:

1. **Qual caminho?**
2. **Qual operação é desejada: ler, substituir, acrescentar ou criar somente se não existir?**
3. **Qual codificação de texto o arquivo utiliza?**

Tornar essas escolhas explícitas é mais seguro do que tratar `open()` como uma operação mágica de "pegar o conteúdo do arquivo".

## 4. Modo `r`: ler um arquivo existente

`"r"` significa leitura de texto. Também é o modo padrão quando o argumento de modo é omitido.

```python
file = open("notes.txt", "r", encoding="utf-8")
```

O alvo precisa existir. Se não existir, `open()` levanta `FileNotFoundError`.

Ser explícito com `"r"` costuma ser útil em código educacional e de aplicação porque a operação pretendida fica imediatamente visível.

## 5. Modo `w`: escrever e substituir

`"w"` abre um arquivo de texto para escrita.

```python
file = open("notes.txt", "w", encoding="utf-8")
```

Se o arquivo não existir, ele será criado. Se já existir, seu conteúdo anterior será **truncado** antes da nova escrita.

Esse comportamento destrutivo torna a escolha do modo uma decisão de correção, não um detalhe cosmético.

```text
arquivo existente + "w"
        ↓
conteúdo antigo removido
        ↓
novas escritas viram o conteúdo
```

## 6. Modo `a`: acrescentar ao final

`"a"` abre para acréscimo. Novas escritas são colocadas no final em vez de substituir o conteúdo existente.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Files\n")
```

Se o arquivo não existir, o modo de acréscimo o cria.

O modo append é útil quando o conteúdo anterior deve permanecer intacto e cada nova escrita pertence ao final.

## 7. Modo `x`: criar somente se o arquivo for novo

`"x"` solicita criação exclusiva.

```python
with open("notes.txt", "x", encoding="utf-8") as file:
    file.write("First version\n")
```

Se o caminho já existir, o Python levanta `FileExistsError` em vez de substituí-lo.

Use esse modo quando sobrescrever acidentalmente um arquivo existente seria um erro.

## 8. Escolha o modo pela intenção

Uma tabela compacta de decisão:

| Intenção | Modo típico | Arquivo existente |
|---|---|---|
| Ler | `r` | mantido |
| Substituir conteúdo | `w` | truncado |
| Acrescentar ao final | `a` | mantido |
| Criar somente se ausente | `x` | levanta `FileExistsError` |

Existem combinações como `r+`, `w+` e `a+` para leitura e escrita com o mesmo objeto arquivo. Elas são válidas, mas também combinam regras de posição e de modo que iniciantes raramente precisam.

Prefira o modo mais simples que corresponda ao trabalho real.

## 9. Modo texto exige uma decisão de codificação

Arquivos de texto armazenam bytes, enquanto strings Python contêm texto Unicode. Uma **codificação** define como essas duas representações se relacionam.

```text
str no Python
    ↓ codificar
bytes no arquivo
    ↓ decodificar
str no Python
```

Se `encoding` for omitido, `open()` usa um padrão que depende do ambiente de execução. Isso pode fazer o mesmo código-fonte se comportar de maneira diferente em sistemas distintos.

Quando o formato é conhecido como UTF-8, declare isso explicitamente:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

## 10. Por que `with` é o padrão normal para arquivos

Um objeto arquivo usa um recurso do sistema operacional. Ele deve ser fechado quando o programa termina de utilizá-lo.

O padrão manual funciona:

```python
file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

Mas existe um problema: se uma exceção ocorrer entre `open()` e `close()`, a chamada final pode nunca executar.

A solução usual é `with`:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Quando a execução sai do bloco `with`, o protocolo de gerenciador de contexto do arquivo executa o trabalho de saída necessário e fecha o arquivo.

## 11. `with` se conecta diretamente a `finally`

O Capítulo 01 introduziu `finally` para limpeza. Um gerenciador de contexto empacota esse padrão de limpeza em um protocolo reutilizável.

Conceitualmente:

```text
adquirir recurso
      ↓
executar bloco
      ↓
liberar recurso
```

Mesmo se o bloco levantar uma exceção, o gerenciador de contexto recebe a oportunidade de executar seu trabalho de saída antes que a exceção continue para fora.

Para objetos arquivo comuns, isso significa fechar o arquivo. `with` **não** significa "ignorar erros de arquivo"; significa "gerenciar o tempo de vida do recurso de forma confiável".

## 12. O arquivo fica fechado após o bloco

O nome atribuído por `as file` ainda existe após o bloco, mas o objeto arquivo subjacente está fechado:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(file.closed)
```

Saída:

```text
True
```

Tentar realizar I/O normal nesse objeto arquivo fechado levanta `ValueError`.

Não projete código esperando continuar usando o arquivo fora do bloco `with`. Mova os dados necessários para objetos Python comuns.

## 13. Leia um arquivo pequeno com `read()`

`read()` sem um argumento de tamanho lê da posição atual até o fim do arquivo.

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Isso é simples e apropriado para um arquivo que sabemos ser pequeno.

Para um arquivo muito grande ou sem limite conhecido, ler tudo de uma vez pode consumir memória desnecessariamente. Nesse caso, processe o arquivo de forma incremental.

## 14. `read(size)` avança a posição atual

Um tamanho positivo solicita no máximo aquela quantidade de caracteres em modo texto:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first = file.read(5)
    second = file.read(5)
```

A segunda chamada continua de onde a primeira parou. Leituras de arquivo mantêm estado.

No fim do arquivo, outro `read()` em modo texto retorna uma string vazia.

Esse modelo de posição se torna importante sempre que várias leituras são feitas pelo mesmo objeto arquivo.

## 15. Leia uma linha com `readline()`

`readline()` lê uma linha por vez:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()
```

Quando uma linha termina com uma nova linha no arquivo, esse `\n` normalmente faz parte da string retornada.

No fim do arquivo, `readline()` retorna `""`.

Uma linha vazia contendo somente a quebra de linha é `"\n"`, o que é diferente do fim do arquivo.

## 16. Itere sobre o arquivo para trabalhar por linhas

Para processamento comum linha por linha, itere sobre o objeto arquivo:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

Isso evita criar primeiro uma lista contendo todas as linhas e é o padrão simples preferido para processamento incremental por linhas.

O objeto arquivo é um iterável. O loop consome linhas a partir da posição atual.

## 17. Seja deliberado ao remover quebras de linha

Um padrão tentador é:

```python
clean = line.strip()
```

Mas `strip()` remove espaços em branco do início e do fim, não apenas a quebra de linha. Isso pode alterar dados significativos.

Se a única mudança desejada for remover um caractere de nova linha no final, seja mais específico:

```python
clean = line.rstrip("\n")
```

Remover ou não outros espaços em branco é uma decisão do formato dos dados, não uma regra universal de arquivos.

## 18. `readlines()` cria uma lista

`readlines()` retorna as linhas restantes como uma lista:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

Isso pode ser conveniente quando o conjunto completo de linhas é pequeno e você realmente precisa de operações de lista depois.

Não use automaticamente. Se cada linha puder ser processada de forma independente, iterar sobre o arquivo mantém o uso de memória mais simples e escalável.

## 19. Escreva texto com `write()`

Em modo texto, `write()` espera uma string:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Functions\n")
    file.write("Exceptions\n")
```

`write()` **não** adiciona uma quebra de linha automaticamente. Se o arquivo deve conter quebras de linha, inclua-as explicitamente.

O método retorna a quantidade de caracteres escritos em modo texto:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    count = file.write("Python\n")

print(count)
```

## 20. Converta valores não string antes de escrever texto

`write()` em modo texto não formata objetos Python arbitrários por você:

```python
score = 92

with open("score.txt", "w", encoding="utf-8") as file:
    file.write(str(score))
```

Uma f-string costuma ser mais clara quando rótulos ou formatação são necessários:

```python
with open("score.txt", "w", encoding="utf-8") as file:
    file.write(f"score={score}\n")
```

O Capítulo 04 introduzirá formatos estruturados que oferecem convenções melhores para armazenar dados mais complexos.

## 21. `writelines()` não inventa separadores

`writelines()` escreve strings de um iterável, mas não adiciona caracteres de nova linha entre elas:

```python
lines = ["Functions\n", "Exceptions\n", "Files\n"]

with open("notes.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

Se as strings ainda não contiverem separadores, o resultado ficará concatenado.

Para iniciantes, chamadas repetidas de `write()` costumam ser mais fáceis de inspecionar até que o formato exato dos dados esteja claro.

## 22. Caminhos relativos dependem do diretório de trabalho atual

Um caminho como:

```python
open("data/notes.txt", "r", encoding="utf-8")
```

é **relativo**. O Python o resolve a partir do diretório de trabalho atual do processo, que não é garantido ser o mesmo diretório que contém o arquivo `.py`.

Isso explica uma surpresa comum para iniciantes:

```text
mesmo código-fonte
+ diretório de trabalho diferente
= caminho resolvido diferente
```

Capítulos posteriores introduzirão `pathlib`, que oferece uma API de caminhos mais rica. Por enquanto, saiba sempre de qual diretório seu processo está sendo executado ao usar caminhos relativos.

## 23. Caminhos absolutos identificam um local a partir da raiz do sistema de arquivos

Um caminho absoluto não depende do diretório de trabalho atual da mesma maneira. Sua sintaxe exata é específica da plataforma.

Colocar no código-fonte reutilizável um caminho absoluto fixo de um único computador costuma ser um problema de portabilidade.

Prefira receber caminhos por configuração, argumentos ou uma estratégia de construção de caminhos apropriada ao programa em vez de embutir no código o layout da máquina de um desenvolvedor.

## 24. Exceções comuns de arquivos

Operações de arquivo podem levantar vários tipos úteis de exceção:

| Exceção | Significado típico |
|---|---|
| `FileNotFoundError` | um caminho necessário não existe |
| `FileExistsError` | criação exclusiva apontou para um caminho existente |
| `PermissionError` | a operação não é permitida |
| `IsADirectoryError` | uma operação de arquivo apontou para um diretório |
| `UnicodeDecodeError` | bytes não puderam ser decodificados com a codificação de texto escolhida |
| `OSError` | falhas mais amplas de I/O do sistema operacional |

Esses tipos são sinais, não instruções para capturar tudo. Trate uma exceção somente onde o programa possui uma resposta significativa.

## 25. Coloque `try` ao redor da fronteira que você consegue tratar

Se um arquivo opcional ausente possui um fallback claro, capture essa falha específica:

```python
try:
    with open("preferences.txt", "r", encoding="utf-8") as file:
        preferences = file.read()
except FileNotFoundError:
    preferences = ""
```

O `with` continua cuidando do fechamento sempre que a abertura é bem-sucedida.

Um `except OSError:` amplo pode ser apropriado quando várias falhas do sistema operacional realmente possuem a mesma política, mas não deve ser usado apenas para fazer todos os problemas de arquivo desaparecerem.

## 26. Se o corpo falhar, a limpeza ocorre antes da propagação

Considere:

```python
with open("scores.txt", "r", encoding="utf-8") as file:
    score = int(file.readline())
```

Se a linha contiver texto inválido para inteiro, `int()` levanta `ValueError`.

O gerenciador de contexto do arquivo executa seu trabalho de saída enquanto o bloco é encerrado, e a exceção continua para fora a menos que algum código ao redor a trate.

Essa é a composição principal:

```text
abertura bem-sucedida
    ↓
corpo levanta exceção
    ↓
arquivo é fechado
    ↓
exceção se propaga
```

## 27. Separe acesso ao arquivo da interpretação dos dados quando for útil

Um desenho útil é deixar uma função ler o texto e outra interpretá-lo:

```python
def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def parse_score(text: str) -> int:
    score = int(text)
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    return score
```

Agora falhas de arquivo e falhas de validação do conteúdo são conceitualmente distintas.

Essa separação se torna especialmente útil no Capítulo 04 ao interpretar dados estruturados.

## 28. Valide antes de escritas destrutivas quando for prático

Como `"w"` trunca um arquivo existente quando ele é aberto, valide os dados que puderem ser validados **antes** de abrir o destino em modo de escrita.

Prefira esta ordem:

```text
construir ou validar dados de saída
        ↓
abrir destino com "w"
        ↓
escrever texto validado
```

em vez de abrir o destino primeiro e somente depois descobrir que os dados são inválidos.

Isso não torna a escrita atômica nem protege contra todas as falhas possíveis, mas reduz uma classe evitável de perda acidental de dados.

## 29. Modo texto e modo binário são interfaces diferentes

Modo texto é o padrão e trabalha com `str`.

Modo binário adiciona `"b"` ao modo e trabalha com `bytes`:

```python
with open("image.bin", "rb") as file:
    data = file.read()
```

Em modo binário, codificação de texto não é usada porque o Python não está convertendo entre `str` e bytes do arquivo.

Este capítulo se concentra em modo texto. Use modo binário quando o formato dos dados é fundamentalmente bytes, como muitas imagens, arquivos compactados ou payloads de protocolos.

## 30. Não passe `encoding` em modo binário

Esta combinação é conceitualmente errada:

```python
open("data.bin", "rb", encoding="utf-8")
```

Modo binário expõe bytes diretamente, então um parâmetro de codificação não faz parte dessa interface.

Escolha um modelo:

```text
modo texto   → str + encoding
modo binário → bytes
```

## 31. Vários gerenciadores de contexto podem compartilhar um `with`

O Python pode gerenciar mais de um contexto em uma única instrução:

```python
with (
    open("input.txt", "r", encoding="utf-8") as source,
    open("output.txt", "w", encoding="utf-8") as destination,
):
    destination.write(source.read())
```

Ambos os recursos recebem seu tratamento de saída correspondente.

Para iniciantes, instruções `with` aninhadas ou com vários itens são mais úteis quando a operação realmente precisa dos dois recursos ao mesmo tempo. Não abra arquivos antes da hora nem os mantenha abertos por mais tempo do que o necessário.

## 32. Exemplo prático: escrever e depois ler

O primeiro exemplo executável cria um diretório temporário apenas para que o teste do repositório exercite I/O real de arquivos sem deixar arquivos gerados para trás.

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "topics.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Functions\n")
        file.write("Exceptions\n")
        file.write("Files\n")

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))
```

Saída:

```text
Functions
Exceptions
Files
```

Os auxiliares `tempfile` e `os.path` servem apenas para organização do exemplo executável. O alvo de aprendizagem do capítulo são os dois blocos `with open(...)`.

Versão executável: [`examples/write_and_read_text.py`](examples/write_and_read_text.py).

## 33. Exemplo prático: acrescentar sem substituir

O segundo exemplo torna visível a diferença entre `"w"` e `"a"`:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "history.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write("Chapter 01\n")

    with open(path, "a", encoding="utf-8") as file:
        file.write("Chapter 02\n")
        file.write("Chapter 03\n")

    with open(path, "r", encoding="utf-8") as file:
        print(file.read(), end="")
```

Saída:

```text
Chapter 01
Chapter 02
Chapter 03
```

Versão executável: [`examples/append_text.py`](examples/append_text.py).

## 34. Exemplo prático: tratar um arquivo opcional ausente

O terceiro exemplo conecta acesso a arquivos ao modelo de exceções dos Capítulos 01 e 02:

```python
import os
import tempfile


with tempfile.TemporaryDirectory() as directory:
    path = os.path.join(directory, "optional.txt")

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        content = "default settings"

    print(content)
```

Saída:

```text
default settings
```

O fallback é significativo porque esse arquivo é explicitamente opcional. Um arquivo obrigatório normalmente precisaria de uma política diferente.

Versão executável: [`examples/handle_missing_file.py`](examples/handle_missing_file.py).

## 35. Erro comum: abrir com `w` quando você queria `a`

Isto substitui o conteúdo anterior:

```python
with open("history.txt", "w", encoding="utf-8") as file:
    file.write("new entry\n")
```

Se a intenção era preservar o histórico antigo e adicionar uma entrada, use `"a"`.

Antes de cada `open()` capaz de escrever, pergunte se o conteúdo existente deve ser substituído, preservado ou protegido contra sobrescrita.

## 36. Erro comum: esquecer a codificação

Isto depende da codificação de texto padrão do ambiente:

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

Se o formato do arquivo é definido como UTF-8, diga isso:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Codificação explícita torna a intenção visível e evita uma fonte importante de surpresas entre plataformas.

## 37. Erro comum: fechamento manual com uma lacuna para exceções

Isto possui uma lacuna de limpeza:

```python
file = open("scores.txt", "r", encoding="utf-8")
score = int(file.readline())
file.close()
```

Se `int()` levantar uma exceção, `close()` será pulado.

Prefira:

```python
with open("scores.txt", "r", encoding="utf-8") as file:
    score = int(file.readline())
```

Agora a limpeza do recurso está ligada ao tempo de vida do bloco.

## 38. Erro comum: tratar todo problema de arquivo como se fosse igual

Evite colapsar falhas não relacionadas sem motivo:

```python
try:
    with open("settings.txt", "r", encoding="utf-8") as file:
        settings = file.read()
except Exception:
    settings = ""
```

Isso pode esconder erros de programação e falhas inesperadas.

Escolha uma exceção específica quando a política de recuperação for específica. Se várias subclasses de `OSError` realmente tiverem a mesma política, documente essa decisão mais ampla.

## 39. Erro comum: usar `read()` automaticamente para todo arquivo

Ler o arquivo inteiro é conveniente, não universalmente ideal.

Se a tarefa é "processar cada linha de forma independente", isto costuma ser melhor:

```python
with open("events.txt", "r", encoding="utf-8") as file:
    for line in file:
        process(line)
```

do que carregar primeiro todas as linhas em uma string gigante.

Escolha a estratégia de leitura a partir do tamanho e do modelo de processamento dos dados.

## 40. Caminhos vindos de usuários são uma fronteira de entrada

Se um programa aceita um caminho vindo de um usuário, requisição de API, arquivo de configuração ou argumento de linha de comando, esse caminho é entrada.

Uma operação capaz de escrever pode modificar ou criar dados no local resolvido.

Aplicações com requisitos de segurança ou proteção de dados devem validar ou limitar os locais permitidos de acordo com sua própria política. A política exata depende do programa e está além deste capítulo introdutório.

A lição geral é simples: **um caminho não é apenas metadado inofensivo quando o programa vai ler ou escrever nele.**

## 41. Quando não usar arquivos de texto brutos como todo o modelo de dados

Texto simples é excelente para conteúdo simples, mas inventar manualmente separadores e regras de parsing se torna frágil conforme os dados ganham estrutura.

Por exemplo:

```text
name|score|date|notes
```

levanta perguntas sobre escape de `|`, campos ausentes, tipos e quebras de linha embutidas.

O Capítulo 04 introduz TXT, CSV e JSON para que a escolha do formato corresponda à forma dos dados em vez de forçar todo problema a um parsing de texto improvisado.

## 42. Exercício

Crie um pequeno programa chamado `study_notes.py` com estes requisitos:

1. Comece com três nomes de tópicos em uma lista.
2. Abra `study_notes.txt` com `"w"` e `encoding="utf-8"`.
3. Escreva um tópico por linha.
4. Reabra o arquivo com `"a"` e adicione mais um tópico.
5. Reabra com `"r"` e itere sobre as linhas.
6. Exiba cada tópico sem uma linha em branco extra.
7. Use `with` para toda operação de arquivo.
8. Explique em um comentário por que `"w"` é apropriado na primeira abertura e `"a"` na segunda.

Perguntas extras:

- O que aconteceria se o primeiro modo fosse `"x"` e o arquivo já existisse?
- Qual exceção você esperaria ao tentar ler um arquivo ausente?
- Por que `read()` poderia ser uma escolha ruim se o arquivo pudesse conter milhões de linhas?

## 43. Checklist de revisão

Antes de seguir, confirme que você consegue responder sem chutar:

- O que `open()` retorna?
- Por que `with open(...)` é mais seguro do que um par manual `open()` / `close()`?
- O que `"w"` faz com um arquivo existente?
- Como `"a"` é diferente?
- Quando `"x"` levanta `FileExistsError`?
- Por que UTF-8 frequentemente deve ser escrito explicitamente como `encoding="utf-8"`?
- O que `read()` retorna no fim do arquivo em modo texto?
- Por que iterar sobre um arquivo pode ser preferível a `readlines()`?
- `write()` adiciona `\n` automaticamente?
- O que acontece com o arquivo quando uma exceção sai do corpo do `with`?
- A partir de qual diretório um caminho relativo é resolvido?
- Qual é a diferença básica entre modo texto e modo binário?

## 44. Referência rápida

| Necessidade | Padrão |
|---|---|
| Ler texto UTF-8 | `with open(path, "r", encoding="utf-8") as file:` |
| Substituir texto UTF-8 | `with open(path, "w", encoding="utf-8") as file:` |
| Acrescentar texto UTF-8 | `with open(path, "a", encoding="utf-8") as file:` |
| Criar somente se ausente | `with open(path, "x", encoding="utf-8") as file:` |
| Ler todo o texto restante | `file.read()` |
| Ler uma linha | `file.readline()` |
| Processar linhas incrementalmente | `for line in file:` |
| Escrever texto | `file.write(text)` |
| Remover somente `\n` final | `line.rstrip("\n")` |
| Caminho necessário ausente | `FileNotFoundError` |
| Caminho existente com `x` | `FileExistsError` |
| Categoria geral de I/O do SO | `OSError` |
| Leitura binária | `with open(path, "rb") as file:` |

Padrão inicial recomendado:

```python
with open(path, "r", encoding="utf-8") as file:
    content = file.read()
```

Escolha o modo de acordo com a intenção, especifique uma codificação de texto conhecida, mantenha o tempo de vida do arquivo curto e capture somente falhas para as quais o código ao redor possui uma política real.

## O que vem depois

O Capítulo 03 estabelece acesso seguro a arquivos de texto e tempo de vida de recursos. O próximo capítulo, **TXT, CSV e JSON**, se concentrará em como os dados são representados dentro dos arquivos e qual parser ou escritor deve ser responsável por cada fronteira de formato.

```text
exceções
    ↓
levantamento deliberado
    ↓
tempo de vida seguro com open() + with
    ↓
formatos TXT / CSV / JSON
    ↓
módulos e pacotes
```

## Referências oficiais

- Documentação do Python 3.14 para `open()` embutido: <https://docs.python.org/3.14/library/functions.html#open>
- Tutorial do Python 3.14, Reading and Writing Files: <https://docs.python.org/3.14/tutorial/inputoutput.html#reading-and-writing-files>
- Referência da linguagem Python 3.14, instrução `with`: <https://docs.python.org/3.14/reference/compound_stmts.html#the-with-statement>
- Documentação `io` do Python 3.14, Text Encoding: <https://docs.python.org/3.14/library/io.html#text-encoding>
