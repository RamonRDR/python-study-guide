# Revisão dos fundamentos de Python

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../02-live-coding-and-take-home/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../04-data-structures-and-algorithms-review/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Pré-requisitos

- [fundamentals/03-variables-and-naming](../../fundamentals/03-variables-and-naming/README.pt-BR.md)
- [fundamentals/04-built-in-data-types](../../fundamentals/04-built-in-data-types/README.pt-BR.md)
- [fundamentals/06-type-conversion](../../fundamentals/06-type-conversion/README.pt-BR.md)
- [strings-and-numbers/02-common-string-methods](../../strings-and-numbers/02-common-string-methods/README.pt-BR.md)
- [program-flow/01-conditions-comparisons-and-boolean-logic](../../program-flow/01-conditions-comparisons-and-boolean-logic/README.pt-BR.md)
- [program-flow/02-if-elif-and-else](../../program-flow/02-if-elif-and-else/README.pt-BR.md)
- [program-flow/04-for-loops-and-iteration](../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [functions/01-defining-and-calling-functions](../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [functions/02-parameters-and-arguments](../../functions/02-parameters-and-arguments/README.pt-BR.md)
- [functions/03-return-values](../../functions/03-return-values/README.pt-BR.md)
- [functions/04-scope](../../functions/04-scope/README.pt-BR.md)
- [functions/06-default-values](../../functions/06-default-values/README.pt-BR.md)
- [functions/09-data-flow-between-functions](../../functions/09-data-flow-between-functions/README.pt-BR.md)

## Revisão pelo raciocínio

Use as aulas vinculadas em vez de reaprender sua sintaxe aqui. Um nome é vinculado a um objeto; seu tipo determina operações suportadas. Conversões podem falhar: `int("12")` funciona, mas `int("twelve")` gera ValueError. Strings são imutáveis; métodos retornam resultados. Condições selecionam execução; loops repetem trabalho; funções têm parâmetros, retornos e vinculações locais. Explique uma regra, mostre um exemplo e descreva um limite.

```python
def add_tag(tags, tag):
    tags.append(tag)
    return tags

original = ["python"]
result = add_tag(original, "testing")
print(original, result)
```

Os dois nomes referenciam a lista modificada. Vincular o parâmetro a uma nova lista não vincularia novamente o nome do chamador. Uma lista padrão é avaliada na definição da função, não a cada chamada; use None quando omitir significa criar nova lista. Veja as aulas vinculadas de fluxo de dados e valores padrão.

## Prática independente

Preveja a saída antes de executar. Altere a função para retornar uma nova lista sem mutar a entrada. Teste uma lista vazia e tags repetidas. Explique se duplicados são permitidos pelo contrato escolhido. Revise LEGB, curto-circuito booleano, igualdade versus identidade e por que `is None` é adequado. Não deduza identidade por cache de inteiros ou strings.

**Referência rápida:** tipos, conversão, vinculação, mutação, condições, loops, funções, escopo e retornos.

<!-- chapter-navigation:bottom -->
[← Anterior](../02-live-coding-and-take-home/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../04-data-structures-and-algorithms-review/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
