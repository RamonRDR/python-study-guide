<div align="center">

# PEP 8 e Legibilidade em Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Comentários versus logging](../05-comments-vs-logging/README.pt-BR.md)

A PEP 8 é o guia de estilo do código Python da biblioteca padrão e uma referência amplamente utilizada em projetos Python. Seu objetivo não é tornar todos os arquivos visualmente idênticos. Seu objetivo é melhorar a legibilidade e a consistência para que o leitor gaste menos esforço decifrando a apresentação e mais esforço compreendendo o comportamento.

> **Princípio orientador:** a consistência favorece a legibilidade, mas o contexto do projeto e a correção vêm primeiro.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante a intermediário |
| Pré-requisitos | Sintaxe básica de Python; recomendam-se os capítulos de comentários e nomes significativos |
| Tempo estimado | 60 a 85 minutos |
| Conceitos principais | PEP 8, indentação, comprimento de linha, imports, espaços, nomes, comparações, exceções, ferramentas e convenções do projeto |

## Objetivos de aprendizagem

Ao final deste capítulo, você deverá ser capaz de:

- explicar o que a PEP 8 é e o que ela não é;
- aplicar convenções de indentação, espaços, quebras e linhas em branco;
- organizar imports e escolher nomes convencionais;
- escrever comparações comuns e tratamento de exceções de forma legível;
- diferenciar formatador, linter, verificador de tipos e testes;
- seguir as convenções do projeto sem realizar reformas de estilo fora do escopo;
- reconhecer quando uma exceção deliberada é mais clara ou segura que a conformidade rígida.

## 1. PEP 8 é orientação, não sintaxe do Python

Um programa pode ser Python válido mesmo ignorando diversas recomendações de estilo. Da mesma forma, um código lindamente formatado ainda pode conter lógica incorreta.

A PEP 8 trata principalmente de disposição do código, nomes, comentários, imports e algumas recomendações de programação. Um formatador ou linter pode aplicar o subconjunto escolhido pelo projeto, mas o Python não rejeita uma função apenas porque faltam duas linhas em branco.

As orientações específicas do projeto prevalecem dentro dele. Compatibilidade, correção e clareza são mais importantes que conformidade cosmética.

## 2. A consistência possui níveis

Uma ordem de prioridade útil é:

1. preservar correção e compatibilidade;
2. seguir as convenções documentadas do projeto;
3. manter consistência com o módulo ao redor;
4. usar a PEP 8 como padrão quando não houver regra local mais forte.

Não reformate um arquivo sem relação com a tarefa apenas porque percebeu uma diferença de estilo. Diffs cosméticos extensos escondem alterações comportamentais e dificultam a revisão.

## 3. Use quatro espaços por nível de indentação

Python utiliza indentação como sintaxe, portanto a estrutura visual e a estrutura do programa estão conectadas. A PEP 8 recomenda quatro espaços por nível.

```python
def calculate_total(amount: float, tax_rate: float) -> float:
    tax_amount = amount * tax_rate
    return amount + tax_amount
```

Não misture tabulações e espaços. Configure o editor para inserir espaços e exibir caracteres invisíveis ao diagnosticar problemas de indentação.

## 4. Quebre expressões longas dentro de delimitadores

Prefira continuação implícita dentro de parênteses, colchetes ou chaves:

```python
total = calculate_total(
    amount=1250.00,
    tax_rate=0.18,
)
```

Evite barras invertidas em que delimitadores tornem a estrutura mais clara. Alinhe as linhas continuadas para distinguir argumentos do bloco ao redor.

## 5. Quebre antes dos operadores binários

Em expressões multilinha, colocar o operador antes do operando continuado mantém operadores e operandos relacionados visualmente unidos:

```python
total_amount = (
    subtotal
    - discount_amount
    + shipping_amount
)
```

Não divida uma expressão apenas para satisfazer um número. Primeiro considere um nome mais claro, uma variável intermediária ou uma função menor.

## 6. Trate o comprimento da linha como orçamento de leitura

A PEP 8 recomenda no máximo 79 caracteres para código e 72 para comentários corridos e docstrings. Ela também reconhece que equipes podem combinar limites maiores, normalmente até 99 caracteres para código.

A regra deve reduzir leitura horizontal e melhorar diffs. Ela não deve produzir uma escada de fragmentos artificiais. URLs, textos gerados, identificadores longos de sistemas externos e dados de teste podem exigir discernimento.

## 7. Use linhas em branco para revelar estrutura

Use duas linhas em branco ao redor de funções e classes no nível do módulo. Dentro de uma classe, separe métodos com uma linha. Dentro de uma função, use linhas em branco com moderação para separar etapas lógicas.

Poucas linhas transformam o código em parede. Linhas demais fazem etapas relacionadas parecerem desconectadas.

## 8. Organize imports deliberadamente

Imports normalmente aparecem perto do topo e são agrupados em biblioteca padrão, pacotes de terceiros e imports locais, com uma linha em branco entre grupos:

```python
import json
from pathlib import Path

import requests

from project.reports import build_report
```

Coloque um `import` comum por linha. Evite imports curinga, pois escondem a origem dos nomes. A posição pode variar quando dependências opcionais, custo de inicialização ou ciclos exigirem exceção documentada.

## 9. Espaços devem esclarecer, não decorar

Use espaços ao redor de atribuições, comparações e operadores binários, além de depois das vírgulas. Evite espaços imediatamente dentro de delimitadores ou antes dos parênteses de uma chamada:

```python
result = calculate_total(amount, tax_rate=0.18)
coordinates = (10, 20)
mapping["account"] = account_code
```

Argumentos nomeados e valores padrão sem anotação normalmente não usam espaços ao redor de `=`, como em `tax_rate=0.18` e `def calculate(tax_rate=0.18):`. Quando uma anotação de parâmetro é combinada com um valor padrão, use espaços ao redor de `=`, como em `def calculate(tax_rate: float = 0.18):`.

## 10. Use estilos de nomes convencionais

Convenções comuns incluem:

- `snake_case` para funções, métodos e variáveis;
- `PascalCase` para classes e exceções;
- `UPPER_SNAKE_CASE` para constantes;
- sublinhado inicial para detalhes internos;
- `self` no primeiro parâmetro de método de instância e `cls` em métodos de classe.

```python
MAX_RETRY_COUNT = 3


class InvoiceProcessor:
    def process_invoice(self, invoice_id: str) -> None:
        is_ready = self._validate_invoice(invoice_id)
        if is_ready:
            self._save_invoice(invoice_id)
```

Essas convenções não substituem nomes significativos. `processed_invoice_count` comunica mais que uma variável perfeitamente estilizada chamada `x`.

## 11. Escreva comparações de forma idiomática e explícita

Use identidade para `None`, valores booleanos diretamente nas condições e teste de valor-verdade para recipientes vazios quando a pergunta for sobre vazio:

```python
if result is None:
    handle_missing_result()

if is_active:
    start_worker()

if not records:
    return []
```

Use `isinstance()` quando a verificação de tipo for realmente necessária. Não use `is` para comparar números ou textos.

## 12. Prefira fluxo de controle legível

Cláusulas de guarda podem manter o caminho principal visível:

```python
def calculate_discount(customer: Customer) -> float:
    if not customer.is_eligible:
        return 0.0

    if customer.is_premium:
        return 0.15

    return 0.05
```

Aninhamento profundo costuma indicar condições, responsabilidades ou nomes a refatorar. Não achate mecanicamente se retornos antecipados ocultarem limpeza ou limites transacionais.

## 13. Trate exceções de forma restrita

Capture as exceções que você consegue tratar ou traduzir de maneira significativa:

```python
try:
    report = load_report(path)
except OSError as error:
    raise ReportLoadError(path) from error
```

Evite `except:` sem tipo em código comum, pois também captura `KeyboardInterrupt` e `SystemExit`. Mantenha o bloco `try` focado para mostrar qual operação pode falhar.

## 14. Legibilidade é maior que formatação

Este código é compacto, porém vago:

```python
def f(x):
    if x and len(x)>0:
        return sum(x)/len(x)
    return 0
```

Uma versão legível revela intenção:

```python
def calculate_average(values: list[float]) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)
```

Formatação não corrige abstração confusa, nome enganoso, efeito colateral oculto ou função enorme. A PEP 8 trabalha com design, comentários, docstrings, testes e type hints.

## 15. Formatadores, linters, verificadores de tipo e testes são diferentes

Um formatador reescreve a apresentação. Um linter relata problemas de estilo e padrões suspeitos. Um verificador de tipos analisa contratos de tipo. Testes verificam comportamentos definidos pelo projeto.

As ferramentas se sobrepõem, mas nenhuma prova que o código está correto ou compreensível. Configure-as em arquivos versionados e evite introduzi-las sem documentar escopo e versão de Python suportada.

## 16. Refatore o estilo com segurança

Antes de uma refatoração de estilo:

1. confirme se o comportamento deve permanecer igual;
2. limite o diff ao escopo declarado;
3. execute testes antes e depois;
4. separe formatação mecânica de mudanças lógicas quando possível;
5. preserve nomes e interfaces públicas, salvo alteração intencional;
6. trate código gerado, migrações, código incorporado e snapshots por regras próprias.

Um diff menor é mais fácil de compreender, revisar, reverter e confiar.

## 17. Saiba quando desviar

Uma exceção deliberada pode ser justificada quando a conformidade rígida reduzir a legibilidade, quebrar compatibilidade, conflitar com convenção consolidada ou exigir alterações sem relação.

Quando a razão não for óbvia e continuar relevante, documente-a na configuração do projeto ou junto ao código. Evite preferências pessoais que façam um arquivo destoar do restante.

## 18. Exemplos neste repositório

| Arquivo | Objetivo |
|---|---|
| [`readable_layout.py`](examples/readable_layout.py) | Mostra indentação, quebra de linhas, espaços e um pequeno ponto de entrada |
| [`imports_and_names.py`](examples/imports_and_names.py) | Demonstra imports da biblioteca padrão, constantes e nomes descritivos |
| [`refactor_for_readability.py`](examples/refactor_for_readability.py) | Substitui lógica densa por funções focadas que revelam intenção |

Execute a partir da raiz:

```bash
python comments-and-documentation/06-pep8-and-readability/examples/readable_layout.py
```

## 19. Exercício

Refatore o código abaixo sem alterar seu resultado:

```python
def calc(x,y,z=False):
    if x!=None:
        if len(x)>0:
            r=sum(x)/len(x)
            if z==True:r=r-(r*y)
            return r
    return 0
```

Sua revisão deve:

1. escolher nomes descritivos;
2. usar verificações idiomáticas de `None`, booleanos e vazio;
3. reduzir aninhamento desnecessário;
4. adicionar type hints compatíveis com as entradas;
5. quebrar linhas com clareza;
6. preservar o comportamento original, inclusive para entrada vazia;
7. explicar qualquer desvio deliberado das regras do projeto.

## 20. Erros comuns

- tratar a PEP 8 como sintaxe;
- reformatar código sem relação dentro de um PR comportamental;
- obedecer ao limite de linha tornando expressões mais difíceis;
- usar formatador como substituto de design;
- misturar tabs e espaços;
- agrupar imports sem considerar restrições opcionais ou locais;
- renomear interfaces públicas apenas por estética;
- adicionar `# noqa` ou supressões sem compreender o alerta;
- assumir que todos os projetos usam a mesma configuração.

## 21. Checklist de revisão

Antes de aprovar uma mudança de legibilidade, verifique:

- indentação e continuação são inequívocas;
- nomes revelam intenção e seguem o projeto;
- imports são compreensíveis e mínimos;
- espaços e linhas em branco revelam estrutura;
- comparações e exceções expressam a semântica pretendida;
- comentários explicam decisões, não formatação;
- nenhuma interface pública mudou sem intenção;
- o diff não contém limpeza fora do escopo;
- ferramentas e testes passaram;
- supressões e desvios possuem razão durável.

## 22. Resumo para consulta rápida

| Situação | Padrão |
|---|---|
| Indentação | Quatro espaços |
| Continuação | Parênteses, colchetes ou chaves |
| Comprimento do código | 79 na PEP 8; o projeto pode definir outro |
| Definições no módulo | Duas linhas em branco |
| Métodos em classe | Uma linha em branco |
| Funções e variáveis | `snake_case` |
| Classes e exceções | `PascalCase` |
| Constantes | `UPPER_SNAKE_CASE` |
| Comparar com `None` | `is None` / `is not None` |
| Recipiente vazio | `if not items:` quando vazio é a intenção |
| Ordem de imports | Biblioteca padrão, terceiros, local |
| Prioridade máxima | Correção, compatibilidade e consistência do projeto |

## 23. Execute as verificações do repositório

A partir da raiz:

```bash
python -m compileall .
python scripts/run_examples.py
python scripts/check_internal_links.py
python scripts/validate_repository_structure.py
```

Um resultado limpo de formatador ou linter é evidência útil, não substituto da revisão humana.

## Referências oficiais

- [PEP 8 — Guia de Estilo para Código Python](https://peps.python.org/pep-0008/)
- [Tutorial do Python — Estilo de codificação](https://docs.python.org/pt-br/3/tutorial/controlflow.html#intermezzo-estilo-de-codificacao)

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Comentários versus logging](../05-comments-vs-logging/README.pt-BR.md)
