<div align="center">

# Docstrings em Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Comentários](../01-comments/README.pt-BR.md)

Uma docstring explica a finalidade e o uso público de um módulo, função, classe ou método Python. Diferentemente de um comentário comum, a docstring é armazenada como documentação do objeto e pode ser lida por pessoas, editores, geradores de documentação, `help()` e ferramentas de introspecção.

> **Princípio orientador:** Escreva uma docstring para a pessoa que precisa utilizar o objeto corretamente sem ler toda a sua implementação.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante |
| Pré-requisitos | Recomenda-se familiaridade básica com funções. Os exemplos de módulos, classes e métodos podem ser compreendidos conceitualmente antes que esses temas sejam estudados em profundidade |
| Tempo estimado de estudo | 45 a 65 minutos |
| Conceitos principais | docstring, `__doc__`, `help()`, `inspect.getdoc()`, módulos, funções, classes, métodos, parâmetros, valores de retorno, exceções, PEP 257 |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- diferenciar uma docstring de um comentário e de um literal de string sem função documental;
- posicionar docstrings corretamente em módulos, funções, classes e métodos;
- escrever docstrings úteis de uma linha e de várias linhas;
- documentar comportamento, parâmetros, retornos, exceções, efeitos colaterais e restrições quando forem relevantes;
- acessar documentação por meio de `__doc__`, `help()` e `inspect.getdoc()`;
- compreender a relação entre docstrings, type hints, arquivos README e documentação externa;
- reconhecer que a PEP 257 define convenções gerais, mas não impõe um único estilo universal de marcação;
- revisar docstrings considerando exatidão, clareza, privacidade e facilidade de manutenção.

## 1. O que é uma docstring

Uma docstring é um literal de string que aparece como a primeira instrução dentro de um módulo, função, classe ou método.

```python
def greet(name):
    """Return a greeting for the provided name."""
    return f"Hello, {name}!"
```

Como a string está na posição correta, o Python a armazena no atributo `__doc__` da função:

```python
print(greet.__doc__)
```

Saída:

```text
Return a greeting for the provided name.
```

O mesmo texto com aspas triplas em outra posição é apenas uma expressão de string:

```python
def greet(name):
    result = f"Hello, {name}!"
    """This is not the function docstring."""
    return result
```

Nesse caso, `greet.__doc__` é `None`, pois a string não é a primeira instrução.

### Aspas triplas não criam automaticamente uma docstring

Aspas triplas criam um literal de string. A posição é o que atribui a essa string a função de documentação.

```python
message = """A regular multi-line string."""
```

Esse é um valor comum atribuído a `message`, não uma docstring.

## 2. Por que docstrings existem

A assinatura e a implementação de uma função podem mostrar como o código funciona, mas quem utiliza a função ainda precisa de uma explicação estável sobre como chamá-la com segurança.

Considere:

```python
def calculate_fee(amount, priority=False):
    ...
```

A assinatura não responde completamente:

- O que `amount` representa?
- Qual unidade ou moeda é esperada?
- O que muda quando `priority` é `True`?
- O que é retornado?
- A função pode gerar uma exceção?
- Ela altera algum estado externo?

Uma docstring pode descrever esse contrato público sem obrigar cada pessoa a inspecionar a implementação.

```python
def calculate_fee(amount_cents, priority=False):
    """Return the fictional service fee in cents.

    Args:
        amount_cents: Positive base amount expressed in cents.
        priority: Whether to apply the fictional priority rate.

    Returns:
        The calculated fee in cents.

    Raises:
        ValueError: If amount_cents is not positive.
    """
```

O código continua sendo a fonte do comportamento executável. A docstring é o mapa legível do uso pretendido da interface.

## 3. Posicionamento correto

### Docstrings de módulos

Uma docstring de módulo normalmente aparece no início de um arquivo Python, depois de um *shebang* ou declaração de codificação quando algum deles existir, e antes dos imports.

```python
"""Utilities for the fictional reading-progress examples."""

from pathlib import Path
```

A docstring de módulo pode resumir a finalidade do arquivo e seus principais objetos públicos.

### Docstrings de funções

A docstring de uma função é a primeira instrução depois do cabeçalho da função.

```python
def convert_minutes_to_seconds(minutes):
    """Return the provided duration converted to seconds."""
    return minutes * 60
```

### Docstrings de classes

A docstring de uma classe descreve sua responsabilidade, comportamento importante e expectativas públicas.

```python
class ReadingProgress:
    """Track completed pages in a fictional reading session."""
```

### Docstrings de métodos

A docstring de um método explica o que o método faz do ponto de vista de quem o chama.

```python
class ReadingProgress:
    """Track completed pages in a fictional reading session."""

    def record_pages(self, pages):
        """Add completed pages without exceeding the total page count."""
```

A docstring da classe explica o objeto como um todo. As docstrings dos métodos explicam operações individuais.

## 4. Docstrings de uma linha

Utilize uma docstring de uma linha quando a finalidade do objeto for simples e puder ser descrita com exatidão em uma frase curta.

```python
def is_even(value):
    """Return whether value is an even integer."""
    return value % 2 == 0
```

Convenções úteis da PEP 257 incluem:

- utilizar aspas duplas triplas mesmo em uma única linha;
- manter as aspas de abertura e fechamento na mesma linha;
- escrever uma frase completa terminada por ponto;
- descrever o efeito ou resultado em vez de repetir a assinatura.

Evite:

```python
def is_even(value):
    """is_even(value) -> bool"""
```

A assinatura já expõe o nome do parâmetro, e type hints podem expor os tipos esperados. A docstring deve acrescentar significado.

## 5. Docstrings de várias linhas

Utilize uma docstring de várias linhas quando quem usa o objeto precisar de mais do que um resumo.

```python
def calculate_average(values):
    """Return the arithmetic mean of a non-empty sequence.

    Args:
        values: Numeric values included in the calculation.

    Returns:
        The arithmetic mean.

    Raises:
        ValueError: If values is empty.
    """
```

Uma estrutura prática é:

1. uma linha curta de resumo;
2. uma linha em branco;
3. uma explicação adicional;
4. seções estruturadas quando o projeto as utilizar.

O resumo deve permanecer útil isoladamente, pois editores e ferramentas de documentação podem exibir apenas essa primeira linha.

## 6. O que pertence a uma docstring útil

Nem toda função precisa de todas as seções possíveis. Documente o que a pessoa que chama o objeto precisa saber.

### Finalidade e comportamento

Informe o que o objeto oferece.

```python
def normalize_identifier(raw_value):
    """Normalize a fictional identifier for display."""
```

### Parâmetros

Explique significado, unidades, formatos aceitos e restrições importantes que nomes e type hints não expressem completamente.

```python
def schedule_retry(delay_seconds):
    """Schedule a retry after a non-negative delay.

    Args:
        delay_seconds: Waiting time in seconds. Zero schedules an immediate retry.
    """
```

### Valor de retorno

Explique o significado do valor retornado, principalmente quando `None`, valores sentinela, unidades ou resultados diferentes forem possíveis.

```python
def find_label(code):
    """Return the matching label, or None when the code is unknown."""
```

### Exceções

Documente exceções que façam parte do contrato público e que possam ser tratadas de forma razoável por quem chama a função.

```python
def load_percentage(text):
    """Convert text to a percentage from 0 through 100.

    Raises:
        ValueError: If text is not numeric or is outside the accepted range.
    """
```

Não prometa todas as exceções internas que possam escapar em qualquer situação. Concentre-se no comportamento intencional e relevante.

### Efeitos colaterais

Mencione alterações importantes que ocorram além do valor de retorno.

```python
def save_report(path, content):
    """Write content to path, replacing an existing file."""
```

O comportamento de substituição importa, mesmo que a implementação seja simples.

### Restrições e premissas

Documente requisitos que não possam ser inferidos com segurança.

```python
def compare_snapshots(left, right):
    """Compare snapshots created with the same schema version."""
```

## 7. Docstrings para diferentes objetos

| Objeto | Foco típico da documentação |
|---|---|
| Módulo | Finalidade, principais objetos públicos, observações importantes de uso ou configuração |
| Função | Comportamento, parâmetros, retorno, exceções, efeitos colaterais e restrições |
| Classe | Responsabilidade, expectativas de construção, estado importante e comportamento público |
| Método | Operação realizada, alterações de estado, resultado e exceções |
| Propriedade | Significado do valor exposto e restrições relevantes |
| Script | Finalidade, uso pela linha de comando, entradas, saídas, ambiente e comportamento de encerramento quando relevante |

Objetos públicos normalmente exigem documentação mais forte do que pequenos auxiliares privados cujos nomes e contexto já sejam claros. A política do projeto determina o limite exato.

## 8. Docstrings, comentários, type hints e arquivos README

Esses recursos cooperam em vez de competir.

```python
def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers."""
```

- O **nome** comunica a intenção principal.
- Os **type hints** descrevem os formatos de dados esperados.
- A **docstring** explica o comportamento e as expectativas públicas.
- Um **comentário** pode explicar uma decisão de implementação não evidente.
- Um **README ou guia** pode ensinar um fluxo maior envolvendo vários objetos.

Não duplique a mesma frase em todos os lugares. Coloque cada informação onde seu público naturalmente procurará por ela.

## 9. Acessando docstrings durante a execução

### `__doc__`

Objetos documentados expõem o texto por meio de `__doc__`.

```python
print(calculate_average.__doc__)
```

Quando não houver uma docstring válida, `__doc__` normalmente será `None`.

### `help()`

O sistema de ajuda embutido utiliza a documentação e os metadados disponíveis do objeto.

```python
help(calculate_average)
```

Isso é útil em uma sessão interativa do Python. A apresentação completa pode variar conforme o ambiente.

### `inspect.getdoc()`

`inspect.getdoc()` recupera e limpa o texto da documentação.

```python
from inspect import getdoc

print(getdoc(calculate_average))
```

A função remove a indentação comum e pode recuperar documentação herdada para algumas categorias de objetos quando uma docstring própria não tiver sido definida.

## 10. Estilos e ferramentas de documentação

O Python define o que é uma docstring, mas não exige um único formato universal para seções como parâmetros e retornos.

Ecossistemas comuns incluem:

- texto simples seguindo a PEP 257;
- seções no estilo Google, como `Args`, `Returns` e `Raises`;
- cabeçalhos no estilo NumPy;
- campos em reStructuredText utilizados por ferramentas como Sphinx.

Esses são padrões de documentação, não sintaxes diferentes do Python.

Este guia utiliza uma estrutura compacta inspirada no estilo Google nos exemplos maiores, pois ela é acessível para iniciantes. Um projeto real deve escolher um estilo, registrar a escolha e aplicá-lo de maneira consistente.

### PEP 257 e ferramentas de formatação

A PEP 257 descreve convenções gerais e a semântica das docstrings. Linters e geradores de documentação podem acrescentar regras mais rigorosas e específicas do projeto. Um alerta de ferramenta deve ser compreendido no contexto da configuração dessa ferramenta, não confundido com um erro de sintaxe do Python.

## 11. Quando uma docstring é desnecessária ou prejudicial

### Não repita o nome

```python
def add(a, b):
    """Add a and b."""
    return a + b
```

Isso pode ser aceitável em um exemplo didático deliberadamente pequeno, mas acrescenta pouco valor em documentação de produção.

Uma docstring melhor adicionaria um contrato não evidente, ou a função poderia ficar sem docstring se fosse um auxiliar privado e trivial segundo a política do projeto.

### Não documente um comportamento falso

```python
def retry():
    """Retry the operation three times."""
    max_attempts = 5
```

Uma docstring desatualizada é uma armadilha bem polida. Atualize a documentação sempre que o comportamento mudar.

### Não copie a implementação para o texto

Evite narrar cada linha. Documente a interface e as garantias não evidentes.

### Não exponha informações privadas

Docstrings fazem parte do código-fonte. Elas podem aparecer em editores, sites gerados, pacotes, logs ou repositórios públicos.

Nunca inclua credenciais, URLs privadas, dados pessoais, regras de negócio confidenciais ou detalhes internos proprietários. Utilize exemplos originais e fictícios.

### Não utilize uma docstring como desculpa para uma interface confusa

Nomes melhores, funções menores, type hints e um desenho mais simples podem resolver o problema antes que a documentação seja adicionada.

## 12. Exemplo básico

```python
def format_name(first_name, last_name):
    """Return a display name with surrounding whitespace removed."""
    return f"{first_name.strip()} {last_name.strip()}"
```

A docstring acrescenta uma garantia útil: os espaços externos são removidos. Ela não narra a f-string.

## 13. Exemplo prático

```python
def calculate_average(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers.

    Args:
        values: Numbers included in the calculation.

    Returns:
        The arithmetic mean of the provided values.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)
```

A docstring comunica:

- a entrada não pode estar vazia;
- o resultado representa uma média aritmética;
- quem chama a função pode esperar um `ValueError` para uma sequência vazia.

Consulte o exemplo executável completo em [`examples/function_docstrings.py`](examples/function_docstrings.py).

## 14. Erros comuns

### Posicionar a string depois de código executável

Apenas a primeira instrução se torna a docstring do objeto.

### Confundir comentários com docstrings

Um comentário não fica disponível por meio da documentação normal do objeto:

```python
# Return the arithmetic mean.
def calculate_average(values):
    ...
```

### Repetir type hints sem acrescentar significado

Fraco:

```python
def load_items(limit: int) -> list[str]:
    """limit is an int and returns a list of strings."""
```

Melhor:

```python
def load_items(limit: int) -> list[str]:
    """Return at most limit fictional item labels in display order."""
```

### Documentar detalhes internos como garantias permanentes

Evite prometer um algoritmo interno específico, a menos que quem utiliza o objeto possa depender dele.

### Misturar estilos sem consistência no mesmo projeto

A consistência ajuda leitores e ferramentas. Siga a convenção registrada no repositório.

### Esquecer construtores e métodos públicos

Uma classe bem descrita, mas com requisitos de construção inexplicados, ainda será difícil de utilizar.

## 15. Exemplos neste repositório

| Arquivo | Objetivo |
|---|---|
| [`function_docstrings.py`](examples/function_docstrings.py) | Mostra docstrings de módulo e função, parâmetros, retornos, exceções e `__doc__` |
| [`class_docstrings.py`](examples/class_docstrings.py) | Mostra docstrings de classe, construtor e métodos |
| [`inspect_docstrings.py`](examples/inspect_docstrings.py) | Mostra o acesso limpo durante a execução com `inspect.getdoc()` |

Execute um exemplo a partir da raiz do repositório:

```bash
python comments-and-documentation/02-docstrings/examples/function_docstrings.py
```

Em sistemas onde o comando se chama `python3`:

```bash
python3 comments-and-documentation/02-docstrings/examples/function_docstrings.py
```

## 16. Exercício

Revise esta função:

```python
def reserve_seats(available, requested):
    if requested <= 0:
        raise ValueError("requested must be positive")
    if requested > available:
        return False
    return True
```

Escreva uma docstring que explique:

1. a finalidade da função;
2. o que `available` e `requested` representam;
3. o que `True` e `False` significam;
4. quando `ValueError` é gerado;
5. nenhuma regra fictícia além do que o código realmente garante.

Uma possível resposta:

```python
def reserve_seats(available, requested):
    """Return whether the requested number of fictional seats is available.

    Args:
        available: Number of seats currently available.
        requested: Positive number of seats requested.

    Returns:
        True when all requested seats are available; otherwise False.

    Raises:
        ValueError: If requested is not positive.
    """
    if requested <= 0:
        raise ValueError("requested must be positive")
    if requested > available:
        return False
    return True
```

Várias redações podem estar corretas. A exatidão importa mais do que detalhes decorativos.

## 17. Checklist de revisão de docstrings

Antes de aprovar uma docstring, pergunte:

- Ela está na posição correta?
- O resumo explica finalidade ou comportamento?
- A documentação corresponde ao código atual?
- Unidades, intervalos, valores sentinela e restrições importantes estão claros?
- Retornos, exceções e efeitos colaterais relevantes foram documentados?
- Ela evita repetir a assinatura e a implementação evidente?
- Ela segue o estilo escolhido pelo projeto?
- Um nome melhor ou uma interface mais simples poderia eliminar parte da explicação?
- Existe alguma informação privada, proprietária, pessoal ou identificável?
- Uma pessoa saberia utilizar o objeto corretamente sem ler todas as linhas?

## 18. Resumo para consulta rápida

| Situação | Abordagem preferida |
|---|---|
| Função pública simples com contrato evidente | Utilize uma docstring curta de uma linha |
| O comportamento exige explicar parâmetros, retornos ou exceções | Utilize uma docstring de várias linhas |
| A informação trata de uma decisão de implementação | Utilize um comentário |
| A informação trata dos tipos esperados | Utilize type hints e esclareça na docstring quando ainda faltar significado |
| Um fluxo envolve vários módulos ou etapas de configuração | Utilize um README ou guia |
| A documentação precisa ser consultada interativamente | Utilize `help()`, `__doc__` ou `inspect.getdoc()` |
| A docstring repete a assinatura | Substitua a repetição por comportamento e garantias |
| A implementação muda | Revise e atualize a docstring na mesma alteração |
| Um projeto utiliza o estilo Google, NumPy ou reStructuredText | Siga a convenção escolhida de forma consistente |

## Referências oficiais

- [Modelo de dados do Python: atributos `__doc__`](https://docs.python.org/pt-br/3/reference/datamodel.html)
- [Função embutida do Python: `help()`](https://docs.python.org/pt-br/3/library/functions.html#help)
- [Python `inspect.getdoc()`](https://docs.python.org/pt-br/3/library/inspect.html#inspect.getdoc)
- [PEP 257: convenções de docstrings](https://peps.python.org/pep-0257/)
- [PEP 8: strings de documentação](https://peps.python.org/pep-0008/#documentation-strings)

## Princípio final

Uma docstring útil descreve o contrato de que a pessoa leitora precisa. Ela deve revelar a finalidade e as garantias importantes sem transformar a implementação em uma segunda cópia frágil escrita em prosa.
