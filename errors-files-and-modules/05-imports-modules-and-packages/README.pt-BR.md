<div align="center">

# Organizando Código com Imports, Módulos e Pacotes

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Erros, Arquivos e Módulos](../README.pt-BR.md) · [← Anterior: Trabalhando com TXT, CSV e JSON](../04-txt-csv-and-json/README.pt-BR.md)

À medida que os programas crescem, manter cada função, constante, parser e fluxo de trabalho em um único arquivo fica mais difícil de entender e manter. O sistema de importação do Python permite dividir o código em **módulos** e organizar módulos relacionados em **pacotes**.

O objetivo deste capítulo não é memorizar cada detalhe do mecanismo de importação do Python. É construir um modelo mental confiável para programas pequenos e médios: de onde vêm os nomes importados, qual código roda durante um import, como pacotes organizam módulos, por que o contexto de execução importa e quais hábitos mantêm as dependências compreensíveis.

**Tempo estimado de estudo:** 120–160 minutos.

**Requisito de Python:** Python 3.10 ou mais recente. O comportamento de importação ensinado aqui foi conferido com o tutorial, a referência da linguagem e a documentação de linha de comando oficiais do Python 3.14.

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá conseguir:

- explicar o que é um módulo Python em projetos comuns de código-fonte;
- distinguir um objeto módulo dos nomes importados para outro módulo;
- usar `import module`, `from module import name` e `as` de forma deliberada;
- explicar por que o acesso qualificado pelo módulo muitas vezes melhora a clareza;
- descrever o que acontece com o código no nível superior quando um módulo é importado;
- explicar o papel introdutório de `sys.modules` no cache de imports;
- usar `if __name__ == "__main__":` para separar definições importáveis da execução direta;
- descrever o propósito de `sys.path` sem tratá-lo como uma lista para remendar casualmente;
- distinguir `ModuleNotFoundError` da família mais ampla de `ImportError`;
- explicar o que é um pacote regular e o que `__init__.py` faz;
- usar nomes pontuados de pacotes e imports absolutos básicos;
- reconhecer imports relativos e explicar por que o contexto de execução importa para eles;
- usar `python -m` quando um módulo deve rodar dentro do contexto de pacote/import;
- distinguir um pacote de importação de uma distribuição instalável;
- evitar imports com curinga, colisões acidentais de nomes de módulos, efeitos colaterais no import e designs simples com imports circulares;
- organizar um pequeno programa Python em vários arquivos com dependências explícitas.

## 1. Por que dividir o código entre arquivos?

Um único arquivo é útil enquanto o programa é pequeno. À medida que responsabilidades se acumulam, esse arquivo pode virar uma sala lotada onde ideias sem relação competem por atenção.

Módulos criam fronteiras:

```text
tratamento de entrada
      ↓
validação
      ↓
cálculo
      ↓
formatação
```

Cada responsabilidade pode viver em um arquivo cujo nome comunica seu propósito.

Dividir código não é automaticamente melhor. Uma função auxiliar de três linhas não precisa de seu próprio módulo apenas porque Python suporta módulos. Crie uma fronteira quando ela melhorar reuso, navegação, testes, propriedade de uma responsabilidade ou clareza das dependências.

## 2. Em código-fonte Python comum, um arquivo `.py` pode ser um módulo

O tutorial do Python introduz um módulo como um arquivo contendo definições e instruções Python.

Por exemplo:

```text
study_tools.py
```

pode conter:

```python
def build_label(topic: str, level: int) -> str:
    return f"{topic} | level {level}"
```

e outro arquivo pode importar esse módulo.

Esse modelo baseado em arquivos é o ponto de partida correto para iniciantes. O sistema completo de importação do Python também pode carregar módulos implementados de outras formas, incluindo módulos embutidos e de extensão. Portanto, no modelo completo da linguagem, "módulo" é mais amplo do que "um arquivo `.py`".

## 3. `import module` vincula o nome do módulo

Suponha que `grade_tools.py` contenha:

```python
def classify_score(score: int) -> str:
    if score >= 80:
        return "ready"
    return "review"
```

Outro arquivo pode importá-lo:

```python
import grade_tools

status = grade_tools.classify_score(84)
print(status)
```

O nome `grade_tools` agora se refere ao objeto módulo importado no namespace do módulo que fez o import.

## 4. O acesso qualificado pelo módulo torna visível a origem de um nome

Com:

```python
import grade_tools
```

você chama:

```python
grade_tools.classify_score(84)
```

Esse prefixo extra é informação útil. Quem lê consegue ver imediatamente que `classify_score` vem de outro módulo.

Essa é uma das razões pelas quais `import module` costuma ser um padrão claro quando o nome do módulo é curto e significativo.

## 5. `from module import name` vincula nomes selecionados diretamente

Python também permite:

```python
from grade_tools import classify_score

status = classify_score(84)
```

Aqui, `classify_score` é vinculado diretamente no namespace do módulo importador. O nome `grade_tools` não é vinculado automaticamente por essa instrução.

O módulo de origem ainda precisa ser encontrado e carregado. `from ... import ...` muda quais nomes são vinculados no importador; ele não ignora o sistema de importação.

## 6. `as` cria um alias local deliberado

Um módulo pode ser importado com outro nome local:

```python
import statistics as stats

mean_score = stats.mean([80, 90, 100])
```

Um nome selecionado também pode receber alias:

```python
from math import sqrt as square_root

print(square_root(81))
```

Use aliases quando forem convencionais ou realmente melhorarem a legibilidade. Evite aliases enigmáticos que tornem o código mais difícil de pesquisar e entender.

## 7. Escolha o estilo de import pela legibilidade, não pela menor quantidade de digitação

Compare:

```python
import decimal

value = decimal.Decimal("0.1")
```

com:

```python
from decimal import Decimal

value = Decimal("0.1")
```

Os dois podem ser adequados.

Perguntas úteis:

- O nome do módulo fornece contexto importante?
- Vários nomes virão do mesmo módulo?
- Um nome importado diretamente poderia colidir com outro nome local?
- A forma mais curta já é uma convenção forte naquele ecossistema?

A linha mais curta nem sempre representa a dependência mais clara.

## 8. Imports são instruções executáveis

Um import não é uma operação de copiar texto. Python localiza e carrega um módulo, cria ou obtém um objeto módulo e executa o código no nível superior quando a inicialização é necessária.

Considere um módulo contendo:

```python
print("Loading helpers")


def build_message() -> str:
    return "Ready"
```

Importar esse módulo pode imprimir `Loading helpers` durante a inicialização.

É por isso que trabalho executável no nível superior deve ser intencional.

## 9. Definições do módulo são criadas pela execução do código do módulo

Uma definição de função também é uma instrução. Quando um módulo é inicializado, Python executa instruções que vinculam nomes como funções, classes e constantes no namespace daquele módulo.

Um fluxo simplificado útil é:

```text
localizar módulo
    ↓
criar/obter objeto módulo
    ↓
executar código de inicialização quando necessário
    ↓
namespace do módulo contém suas definições
```

Esse modelo mental explica por que erros de sintaxe, dependências ausentes e exceções no nível superior podem fazer um import falhar.

## 10. Imports normais reutilizam módulos por meio de `sys.modules`

Durante uma sessão normal do interpretador, módulos importados ficam em cache em `sys.modules`.

Isso significa que instruções repetidas como:

```python
import math
import math
```

normalmente não reexecutam do zero a inicialização do módulo a cada vez.

Esse é um modelo introdutório útil, não uma regra dizendo que o código de um módulo nunca pode rodar novamente. Operações avançadas, como reload explícito ou alterações manuais do estado de importação, podem mudar esse comportamento.

## 11. Evite usar efeitos colaterais de import como fluxo escondido da aplicação

Isto é frágil:

```python
# settings.py
print("Connecting to something...")
```

porque qualquer código que importar `settings` agora dispara esse trabalho.

Prefira definições no nível do módulo e execução explícita por funções:

```python
def initialize_settings() -> None:
    print("Settings initialized")
```

Assim, o chamador decide quando aquela ação pertence ao fluxo do programa.

Alguns módulos realizam legitimamente uma pequena inicialização no import. O alerta de design é sobre trabalho surpreendente, caro, irreversível ou dependente de ordem.

## 12. Todo módulo possui um `__name__`

Um módulo pode inspecionar seu próprio valor global `__name__`.

Quando um módulo é importado normalmente, `__name__` reflete seu nome de importação.

Por exemplo, dentro de `grade_tools.py` importado como `grade_tools`, o valor normalmente é:

```text
grade_tools
```

Quando o código é executado como programa de nível superior, Python dá a esse ambiente de execução o nome:

```text
__main__
```

## 13. O main guard separa definições da execução direta

Um padrão comum é:

```python
def main() -> None:
    print("Program started")


if __name__ == "__main__":
    main()
```

Se o arquivo for executado como programa principal, `main()` roda.

Se o arquivo for importado, a função é definida, mas a chamada protegida não roda.

## 14. Coloque o trabalho reutilizável em funções antes do main guard

Prefira:

```python
def build_report() -> str:
    return "Study report"


def main() -> None:
    print(build_report())


if __name__ == "__main__":
    main()
```

a colocar a aplicação inteira diretamente dentro do guard.

As funções continuam reutilizáveis e testáveis, enquanto o guard responde apenas a uma pergunta: o comportamento de entrada direta deve começar agora?

## 15. `__name__ == "__main__"` não bloqueia o import

O guard não impede que o arquivo seja importado.

Ele impede apenas que o bloco protegido rode quando o módulo é importado com outro nome.

As definições acima do guard ainda são executadas como instruções do módulo e ficam disponíveis no namespace do módulo.

## 16. Python precisa de locais de busca para encontrar módulos

Quando você escreve:

```python
import study_tools
```

Python precisa determinar a que `study_tools` se refere.

O sistema completo de importação suporta vários tipos de finders e loaders. No nível introdutório, a ideia importante é que Python pesquisa locais de importação de acordo com seu mecanismo de import e com o ambiente de execução.

Esses locais de busca aparecem em `sys.path` para imports comuns baseados em caminhos.

## 17. `sys.path` é uma lista de locais de busca de módulos

Você pode inspecioná-la:

```python
import sys

for location in sys.path:
    print(location)
```

Seu conteúdo exato depende de como Python foi iniciado, do ambiente, da configuração da instalação e de outras definições.

Não memorize uma ordem universal de `sys.path` a partir de uma captura de tela. Aprenda o conceito: ela informa ao mecanismo de importação baseado em caminhos onde módulos e pacotes podem ser encontrados.

## 18. Não trate `sys.path.append(...)` como a correção normal para a estrutura do projeto

Isto pode parecer resolver rapidamente um import:

```python
import sys

sys.path.append("../somewhere")
```

mas faz os imports dependerem de uma cirurgia de caminhos em runtime e muitas vezes esconde uma estrutura de projeto ou comando de execução pouco claros.

Prefira uma estrutura coerente de pacotes, um ambiente de trabalho/instalação adequado e uma forma de execução que dê ao Python o contexto de import pretendido.

Existem casos avançados para personalizar caminhos de importação, mas mutar `sys.path` casualmente não deve ser a primeira ferramenta de design.

## 19. Nomes de módulos podem colidir com outros módulos

Imagine criar um arquivo de estudo chamado:

```text
json.py
```

e depois escrever:

```python
import json
```

Dependendo do contexto de busca, seu arquivo local pode sombrear o módulo da biblioteca padrão que você pretendia importar.

Evite dar aos seus arquivos nomes de módulos da biblioteca padrão ou de dependências importantes usadas pelo mesmo projeto.

## 20. `ModuleNotFoundError` normalmente significa que o módulo solicitado não foi encontrado

Por exemplo:

```python
import module_that_does_not_exist
```

normalmente levanta `ModuleNotFoundError`.

`ModuleNotFoundError` é uma subclasse de `ImportError`.

A mensagem e o nome exato que falhou importam porque um import pode encontrar seu primeiro módulo e ainda falhar ao importar uma dependência dele.

## 21. `ImportError` é a exceção mais ampla relacionada a imports

Um módulo pode existir enquanto um nome solicitado não existe:

```python
from math import name_that_does_not_exist
```

Isso levanta `ImportError` porque `math` está disponível, mas o nome importado solicitado não está.

Não capture `ImportError` em volta de um bloco grande apenas para fazer falhas desaparecerem. Capture exceções de importação somente quando o programa tiver uma política deliberada, como uma dependência realmente opcional com fallback documentado.

## 22. Um pacote organiza módulos sob um namespace pontuado

Pacotes permitem que módulos relacionados usem nomes hierárquicos como:

```text
study_tools.formatting
study_tools.validation
study_tools.reports
```

Um pacote pode conter módulos e subpacotes.

No modelo completo de importação do Python, um pacote é um tipo especial de módulo capaz de conter submódulos. A analogia com diretórios é útil em projetos comuns de código-fonte, mas o modelo da linguagem é baseado em objetos de módulo/pacote, não apenas em pastas.

## 23. Um pacote regular normalmente usa `__init__.py`

Um pacote regular simples pode ter:

```text
study_tools/
├── __init__.py
├── formatting.py
└── validation.py
```

A presença de `__init__.py` torna esse diretório um pacote regular no layout convencional de sistema de arquivos.

`__init__.py` pode estar vazio. Ele também pode definir comportamento de inicialização ou expor deliberadamente nomes selecionados no nível do pacote.

## 24. Namespace packages são uma exceção avançada à regra de `__init__.py`

Python moderno também suporta **namespace packages**, que podem existir sem `__init__.py` e podem abranger vários locais.

Portanto, esta afirmação é ampla demais:

```text
"Todo pacote Python precisa ter __init__.py."
```

Para projetos de iniciantes, pacotes regulares com `__init__.py` costumam ser o ponto de partida mais claro. Namespace packages podem esperar até que um projeto realmente precise desse modelo.

## 25. `__init__.py` é código, então mantenha seu comportamento deliberado

Isto é válido:

```python
from .formatting import build_label

__all__ = ["build_label"]
```

Agora o pacote pode fornecer intencionalmente um nome público conveniente:

```python
from study_tools import build_label
```

Mas um `__init__.py` grande, cheio de configuração cara e imports surpreendentes, pode tornar o comportamento do pacote mais difícil de entender.

Trate a inicialização do pacote como parte do design de dependências.

## 26. Nomes pontuados expressam a hierarquia do pacote

Este import:

```python
import study_tools.formatting
```

carrega o submódulo usando seu nome pontuado completo.

Depois você acessa:

```python
study_tools.formatting.build_label("Modules", 2)
```

Outro estilo é:

```python
from study_tools import formatting

print(formatting.build_label("Modules", 2))
```

Os dois deixam explícita a relação com o pacote.

## 27. Importe a interface estável mais estreita que mantenha a intenção clara

Suponha que um pacote exponha intencionalmente `build_label` a partir de `__init__.py`:

```python
from study_tools import build_label
```

Isso pode ser uma API de pacote limpa.

Se o pacote não promete esse atalho público, importar o módulo que define o nome pode ser mais honesto:

```python
from study_tools.formatting import build_label
```

A melhor escolha depende da interface documentada pelo pacote, não de quantos caracteres o import economiza.

## 28. Um pacote de importação não é a mesma coisa que uma distribuição

A palavra **pacote** é sobrecarregada em conversas sobre Python.

Um **pacote de importação** faz parte do namespace de módulos do Python, como:

```text
study_tools
```

Uma **distribuição** é algo instalado e gerenciado por ferramentas de empacotamento e pode fornecer um ou mais pacotes de importação ou módulos.

O nome de instalação e o nome de importação podem até ser diferentes.

Este capítulo ensina pacotes de importação. Empacotamento e publicação de distribuições são assuntos separados.

## 29. Imports absolutos nomeiam explicitamente o caminho do pacote

Dentro de um pacote de projeto, um import absoluto pode ser:

```python
from study_tools.formatting import build_label
```

Ele nomeia o pacote a partir do namespace de importação de nível superior.

Imports absolutos costumam ser fáceis de pesquisar e entender porque o caminho da dependência fica explícito.

## 30. Imports relativos usam pontos iniciais dentro de pacotes

Um módulo dentro de `study_tools` pode importar um vizinho com:

```python
from .formatting import build_label
```

Um ponto inicial se refere ao pacote atual. Pontos adicionais podem se referir a níveis de pacote pai.

Imports relativos são úteis para relações internas de um pacote, mas dependem de Python conhecer o contexto de pacote do módulo.

## 31. Imports relativos não são baseados no diretório de trabalho atual

Essa distinção é importante.

Um import relativo como:

```python
from .formatting import build_label
```

é resolvido a partir das informações de pacote do módulo atual, não caminhando a partir de qualquer diretório em que o terminal esteja.

É por isso que "estou na pasta certa" não é uma explicação completa para dizer se um import relativo vai funcionar.

## 32. Executar diretamente um módulo de pacote pode remover o contexto de pacote que ele espera

Suponha que um módulo contenha um import relativo e tenha sido criado para viver dentro de um pacote.

Executá-lo pelo caminho do arquivo:

```text
python study_tools/cli.py
```

pode executá-lo como o módulo de nível superior `__main__`, e não como `study_tools.cli`. O import relativo pode então falhar porque o pacote pai esperado não é conhecido.

Quando o módulo foi projetado para rodar no contexto do pacote, `python -m` costuma ser a ferramenta correta.

## 33. `python -m` localiza um módulo pelo sistema de importação e o executa

Por exemplo:

```text
python -m study_tools.cli
```

Python localiza `study_tools.cli` usando o mecanismo padrão de importação e executa seu conteúdo como o módulo `__main__`.

Isso preserva o fato de que o código pertence ao pacote `study_tools` enquanto ainda o transforma no ponto de entrada do programa.

O comando usa um **nome de módulo**, não um nome de arquivo `.py`.

## 34. Um pacote pode definir `__main__.py` para `python -m package_name`

Se um pacote contém:

```text
study_tools/
├── __init__.py
├── __main__.py
└── formatting.py
```

então:

```text
python -m study_tools
```

executa `study_tools.__main__` como o módulo principal.

Isso é útil quando o próprio pacote possui comportamento de entrada por linha de comando. Um pacote não ganha esse comportamento apenas porque `__init__.py` existe.

## 35. Imports tornam dependências visíveis

Se `reports.py` importa `formatting.py`, então `reports` depende de `formatting`.

Um desenho útil das dependências é:

```text
cli
 ↓
reports
 ↓
formatting
```

Manter a direção das dependências compreensível ajuda a evitar módulos emaranhados em que tudo importa todo o resto.

## 36. Imports circulares muitas vezes são um sinal de design

Uma relação circular simples é:

```text
module_a importa module_b
        ↑         ↓
        └─────────┘
```

Python pode encontrar um módulo enquanto ele ainda está apenas parcialmente inicializado, produzindo erros de nomes ausentes ou comportamento confuso.

Correções comuns de design incluem:

- mover definições compartilhadas para um terceiro módulo;
- passar valores ou callables como parâmetros em vez de importar de volta para cima;
- esclarecer qual módulo é dono de uma responsabilidade;
- reduzir trabalho no nível superior que dependa do outro módulo estar totalmente inicializado.

Mover um import para dentro de uma função às vezes pode quebrar o ciclo, mas também pode apenas esconder o problema arquitetural. Entenda a dependência antes de aplicar esse contorno.

## 37. Imports dentro de funções são permitidos, mas imports no nível superior são o padrão legível mais comum

Isto é Python válido:

```python
def calculate_root(value: float) -> float:
    import math

    return math.sqrt(value)
```

A maioria das dependências comuns fica mais fácil de ver quando os imports aparecem próximos ao topo do módulo.

Imports locais podem ser deliberados para dependências opcionais, carregamento adiado ou ciclos bem compreendidos. Use-os por uma razão, não por reflexo.

## 38. Evite imports com curinga em módulos comuns

Esta sintaxe existe:

```python
from math import *
```

mas torna o namespace local menos explícito. Quem lê precisa saber quais nomes a origem exporta, e novos nomes exportados podem criar colisões.

Prefira imports explícitos:

```python
from math import pi, sqrt
```

`__all__` pode influenciar o que um import com curinga expõe, mas não transforma wildcard imports no padrão mais claro para código de aplicação.

## 39. Agrupe imports para melhorar a legibilidade

Uma organização comum e legível é:

```python
import csv
import json

from study_tools import build_label
```

A convenção da PEP 8 separa imports da biblioteca padrão, de terceiros e locais da aplicação quando esses grupos existem.

O objetivo mais profundo é visibilidade: quem lê deve conseguir entender as principais dependências de um módulo sem caçar pelo código não relacionado.

## 40. Exemplo prático: importar a biblioteca padrão

```python
import math


number = 81
root = math.sqrt(number)

print(f"Square root: {root}")
```

Saída:

```text
Square root: 9.0
```

Versão executável: [`examples/import_standard_library.py`](examples/import_standard_library.py).

## 41. Exemplo prático: importar seu próprio módulo

Módulo auxiliar `grade_tools.py`:

```python
def classify_score(score: int) -> str:
    if score >= 80:
        return "ready"
    return "review"
```

Módulo executável `module_demo.py`:

```python
import grade_tools


score = 84
status = grade_tools.classify_score(score)

print(f"Score {score}: {status}")
```

Saída:

```text
Score 84: ready
```

Versão executável: [`examples/module_demo.py`](examples/module_demo.py). Módulo de apoio: [`examples/grade_tools.py`](examples/grade_tools.py).

## 42. Exemplo prático: importar de um pacote regular

Layout do pacote:

```text
examples/
├── package_demo.py
└── study_tools/
    ├── __init__.py
    └── formatting.py
```

`formatting.py` define a função reutilizável:

```python
def build_label(topic: str, level: int) -> str:
    return f"{topic} | level {level}"
```

`__init__.py` a expõe intencionalmente no nível do pacote:

```python
from .formatting import build_label

__all__ = ["build_label"]
```

O arquivo executável importa a API do pacote:

```python
from study_tools import build_label


print(build_label("Modules", 2))
```

Saída:

```text
Modules | level 2
```

Versão executável: [`examples/package_demo.py`](examples/package_demo.py). Pacote de apoio: [`examples/study_tools/`](examples/study_tools/).

## 43. Exemplo prático: main guard

```python
def main() -> None:
    print("Main guard executed")


if __name__ == "__main__":
    main()
```

Saída quando executado diretamente:

```text
Main guard executed
```

Versão executável: [`examples/main_guard.py`](examples/main_guard.py).

## 44. Erro comum: nomear um arquivo como uma dependência

Arquivos como estes podem criar sombreamentos confusos:

```text
json.py
csv.py
math.py
random.py
```

se o mesmo projeto também espera os módulos da biblioteca padrão com esses nomes.

Escolha nomes de módulos que representem sua própria responsabilidade e que não colidam com dependências importadas.

## 45. Erro comum: esconder a inicialização da aplicação dentro de um import

Evite transformar isto em arquitetura da aplicação:

```text
import app
    ↓
app lê arquivos, conecta serviços e inicia loops imediatamente
```

Prefira um ponto de entrada explícito:

```text
importar definições
    ↓
main() inicia deliberadamente o comportamento da aplicação
```

Uma inicialização explícita é mais fácil de testar, reutilizar e compreender.

## 46. Erro comum: assumir que execução por arquivo e execução por módulo são idênticas

Estes comandos podem criar contextos de import diferentes:

```text
python path/to/tool.py
python -m package.tool
```

Os dois executam código Python, mas `-m` localiza um módulo nomeado pelo sistema de importação e o executa como `__main__`.

A diferença importa especialmente para pacotes e imports relativos.

## 47. Erro comum: usar pacotes apenas para criar árvores profundas de pastas

Isto não é automaticamente um bom design:

```text
app/core/services/helpers/utils/common/
```

Uma hierarquia de pacotes deve comunicar namespaces e responsabilidades significativas.

Mais níveis adicionam mais caminhos de importação, navegação e fronteiras para entender. Crie níveis que justifiquem sua complexidade.

## 48. Um projeto pequeno pode crescer por etapas

Comece simples:

```text
app.py
```

Depois extraia uma responsabilidade realmente reutilizável:

```text
app.py
grade_tools.py
```

Depois agrupe módulos relacionados quando o namespace se tornar útil:

```text
app.py
study_tools/
├── __init__.py
├── grades.py
└── formatting.py
```

A estrutura deve seguir as responsabilidades, não o desejo de parecer "enterprise" antes de o programa precisar disso.

## 49. Exercício

Crie uma pequena aplicação de estudos baseada em pacote com esta estrutura:

```text
study_app/
├── __init__.py
├── grading.py
└── formatting.py
run_study_app.py
```

Requisitos:

1. Em `grading.py`, crie `classify_score(score: int) -> str`, que retorna `"ready"` para notas de pelo menos 80 e `"review"` caso contrário.
2. Em `formatting.py`, crie `format_result(topic: str, status: str) -> str`.
3. Em `study_app/__init__.py`, mantenha a inicialização mínima. Você pode deixá-lo vazio ou expor deliberadamente um nome documentado no nível do pacote.
4. Em `run_study_app.py`, importe explicitamente a funcionalidade do pacote e imprima resultados para pelo menos três tópicos fictícios.
5. Coloque o comportamento executável em uma função `main()`.
6. Chame `main()` apenas sob `if __name__ == "__main__":`.
7. Não altere `sys.path`.
8. Não use `from ... import *`.
9. Renomeie qualquer arquivo que sombreie um módulo da biblioteca padrão que você utiliza.

Perguntas extras:

- Quais nomes são vinculados por `import study_app.grading`?
- Como o namespace local seria diferente com `from study_app.grading import classify_score`?
- O que roda quando `study_app.grading` é importado pela primeira vez em uma sessão normal do interpretador?
- O que `__name__` contém no arquivo de entrada executado diretamente?
- Por que um import relativo pode se comportar de forma diferente quando um módulo de pacote é executado pelo caminho do arquivo?
- Quando `python -m package.module` seria preferível?
- Por que `__init__.py` de um pacote regular pode ficar vazio?

## 50. Checklist de revisão

Antes de avançar para a fase da biblioteca padrão, confirme que você consegue responder sem adivinhar:

- O que é um módulo em um projeto comum baseado em arquivos `.py`?
- Qual nome `import grade_tools` vincula?
- O que muda com `from grade_tools import classify_score`?
- O que um alias com `as` muda?
- Código no nível superior pode rodar durante um import?
- Qual é o papel introdutório de `sys.modules`?
- Qual é o valor de `__name__` quando um arquivo é o programa de nível superior?
- Qual problema o main guard resolve?
- O que `sys.path` representa?
- Por que nomear seu arquivo `json.py` pode causar problemas?
- Como `ModuleNotFoundError` e `ImportError` se relacionam?
- O que torna reconhecível um pacote regular baseado em diretório no layout convencional?
- Namespace packages precisam conter `__init__.py`?
- O que pontos iniciais significam em um import relativo?
- Por que `python -m package.module` pode ser útil?
- Qual é a diferença entre pacote de importação e distribuição?
- Por que wildcard imports normalmente são evitados?
- O que imports circulares podem revelar sobre o design dos módulos?

## 51. Consulta rápida

| Necessidade | Padrão ou ideia |
|---|---|
| Importar um módulo | `import module_name` |
| Acessar um nome do módulo | `module_name.item` |
| Importar nome selecionado | `from module_name import item` |
| Dar alias a um módulo | `import module_name as alias` |
| Dar alias a um nome selecionado | `from module_name import item as alias` |
| Guard de entrada direta | `if __name__ == "__main__":` |
| Locais de busca de módulos | inspecionar `sys.path` |
| Cache normal de imports | `sys.modules` |
| Módulo solicitado ausente | normalmente `ModuleNotFoundError` |
| Falha de import mais ampla | `ImportError` |
| Marcador convencional de pacote regular | `__init__.py` |
| Importar submódulo de pacote | `import package.submodule` |
| Import absoluto de pacote | `from package.module import item` |
| Import relativo de módulo vizinho | `from .module import item` |
| Executar módulo pelo nome de import | `python -m package.module` |
| Executar entrada do pacote | `python -m package` com `package/__main__.py` |
| Evitar namespace escondido | preferir nomes explícitos a `import *` |
| Evitar cirurgia casual de caminhos | não usar mutação de `sys.path` como estrutura normal |

Um modelo útil de dependências é:

```text
ponto de entrada
    ↓ importa
módulos coordenadores
    ↓ importam
módulos reutilizáveis focados
```

Busque uma direção de dependências que o estudante consiga desenhar sem formar um nó.

## Fase 7 concluída

Este capítulo encerra a **Fase 7: Erros, Arquivos e Módulos**.

A fase agora conecta tratamento de falhas, fronteiras de persistência, dados textuais estruturados e organização do código:

```text
exceções
    ↓
sinalização deliberada de exceções
    ↓
tempo de vida seguro de arquivos
    ↓
fronteiras de dados TXT / CSV / JSON
    ↓
imports / módulos / pacotes
```

Agora você consegue criar um pequeno programa que falha deliberadamente quando um contrato é violado, trata falhas externas esperadas, persiste dados textuais com segurança, interpreta formatos comuns e separa código reutilizável entre módulos e pacotes.

## O que vem depois

A **Fase 8: Biblioteca Padrão** aproveitará o modelo de importação para explorar ferramentas úteis que acompanham o Python, começando por módulos como `pathlib` e `datetime` de acordo com o roadmap do projeto.

A transição importante é:

```text
aprender como imports organizam dependências
        ↓
usar deliberadamente módulos da biblioteca padrão do Python
```

## Referências oficiais

- Tutorial do Python 3.14, Modules: <https://docs.python.org/3.14/tutorial/modules.html>
- Referência da linguagem Python 3.14, The import system: <https://docs.python.org/3.14/reference/import.html>
- Referência da linguagem Python 3.14, The import statement: <https://docs.python.org/3.14/reference/simple_stmts.html#import>
- Documentação de linha de comando do Python 3.14, `-m`: <https://docs.python.org/3.14/using/cmdline.html#cmdoption-m>
- Documentação do Python 3.14 sobre `__main__`: <https://docs.python.org/3.14/library/__main__.html>