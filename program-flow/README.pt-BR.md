<div align="center">

# Fluxo do Programa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Trilha completa de estudos](../docs/learning-path.pt-BR.md) · [Roadmap](../docs/roadmap.pt-BR.md)

Fluxo do Programa é a Fase 4 da sequência principal de aprendizagem do Python Study Guide.

As fases anteriores ensinaram como valores são criados, inspecionados, transformados e organizados. Esta fase ensina como esses valores influenciam **o que é executado, quantas vezes é executado, quando uma repetição termina e como ferramentas de fluxo podem ser combinadas de forma deliberada**.

## Pré-requisito

Conclua primeiro a [Fase 3: Coleções](../collections/README.pt-BR.md).

Você já deve estar confortável com:

- variáveis e tipos de dados embutidos;
- strings e expressões numéricas;
- valores booleanos e comparações básicas;
- listas, tuplas, dicionários e conjuntos;
- `in` e `not in` como testes de pertencimento;
- escolha de uma coleção de acordo com a relação entre os valores.

## Trilha de aprendizagem

| Capítulo | Foco principal | Status |
|---|---|---|
| [01. Condições, Comparações e Lógica Booleana](01-conditions-comparisons-and-boolean-logic/README.pt-BR.md) | Construir expressões de verdade confiáveis antes de usá-las para controlar a execução | Disponível |
| [02. `if`, `elif` e `else`](02-if-elif-and-else/README.pt-BR.md) | Escolher qual bloco de código é executado | Disponível |
| [03. `match` e `case`: Correspondência de Padrões Estruturais](03-match-and-case/README.pt-BR.md) | Comparar valores e estruturas de dados com padrões | Disponível |
| [04. Loops `for` e Iteração](04-for-loops-and-iteration/README.pt-BR.md) | Repetir trabalho para itens de um iterável | Disponível |
| [05. `range()`, `enumerate()` e `zip()`](05-range-enumerate-and-zip/README.pt-BR.md) | Contar, acompanhar posições e coordenar iterações | Disponível |
| [06. Loops `while` e Repetição Guiada por Estado](06-while-loops-and-state-driven-repetition/README.pt-BR.md) | Repetir enquanto uma condição permanecer verdadeira e o estado evoluir | Disponível |
| [07. `break`, `continue` e `else` de Loops](07-break-continue-and-loop-else/README.pt-BR.md) | Encerrar cedo, pular uma iteração e distinguir encerramento normal de `break` | Disponível |
| [08. Escolhendo e Combinando o Fluxo do Programa](08-choosing-and-combining-program-flow/README.pt-BR.md) | Selecionar e combinar ferramentas de fluxo de acordo com a intenção | Disponível |

Estude os capítulos em ordem ao seguir a trilha completa para iniciantes.

## Por que condições vêm antes de `if`

Uma estrutura de decisão só é tão clara quanto a condição que a controla.

Por isso, esta fase começa separando duas ideias:

```text
condition = a question Python can interpret for truth
decision = what the program does because of that condition
```

O Capítulo 01 se concentra na primeira ideia. O Capítulo 02 usa essas condições para selecionar qual bloco é executado. O Capítulo 03 introduz correspondência de padrões estruturais quando a forma ou o padrão de um valor é a pergunta importante. O Capítulo 04 avança da seleção para repetição guiada por iterável. O Capítulo 05 adiciona auxiliares para progressões numéricas, posições e iteração paralela. O Capítulo 06 adiciona repetição controlada por estado em mudança. O Capítulo 07 adiciona saída antecipada deliberada, salto de iteração e tratamento da conclusão de loops. O Capítulo 08 encerra a fase escolhendo e combinando todas essas ferramentas de acordo com a intenção.

## Progressão da fase

```text
conditions
    ↓
decisions
    ↓
pattern matching
    ↓
for each item
    ↓
iteration helpers
    ↓
while a condition holds
    ↓
loop control
    ↓
choose and combine flow
```

## Limite de escopo

A Fase 4 ensina fluxo do programa sem tornar assuntos posteriores pré-requisitos.

Ela não exige:

- funções definidas pelo usuário com `def`;
- tratamento de exceções com `try` e `except`;
- manipulação de arquivos;
- comprehensions como atalho para loops;
- bibliotecas externas.

Esses conceitos aparecem mais adiante no roadmap.

## Comece aqui

Comece por [01. Condições, Comparações e Lógica Booleana](01-conditions-comparisons-and-boolean-logic/README.pt-BR.md).

Depois do Capítulo 01, continue com [02. `if`, `elif` e `else`](02-if-elif-and-else/README.pt-BR.md).

Depois do Capítulo 02, continue com [03. `match` e `case`: Correspondência de Padrões Estruturais](03-match-and-case/README.pt-BR.md).

Depois do Capítulo 03, continue com [04. Loops `for` e Iteração](04-for-loops-and-iteration/README.pt-BR.md).

Depois do Capítulo 04, continue com [05. `range()`, `enumerate()` e `zip()`](05-range-enumerate-and-zip/README.pt-BR.md).

Depois do Capítulo 05, continue com [06. Loops `while` e Repetição Guiada por Estado](06-while-loops-and-state-driven-repetition/README.pt-BR.md).

Depois do Capítulo 06, continue com [07. `break`, `continue` e `else` de Loops](07-break-continue-and-loop-else/README.pt-BR.md).

Depois do Capítulo 07, encerre a fase com [08. Escolhendo e Combinando o Fluxo do Programa](08-choosing-and-combining-program-flow/README.pt-BR.md).

**A Fase 4 está concluída com oito capítulos revisados.** A próxima fase de aprendizagem planejada é a Fase 5: Funções.
