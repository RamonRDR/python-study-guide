# Fundamentos de resolução de problemas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../../manual-programming-practices/04-professional-workflow/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../02-constraints-and-edge-cases/README.pt-BR.md)
<!-- /chapter-navigation:top -->

**Pré-requisitos:** [Program Flow](../../program-flow/08-choosing-and-combining-program-flow/README.pt-BR.md) · [Functions](../../functions/08-functions-working-together/README.pt-BR.md) · [SDD](../../manual-programming-practices/02-specification-driven-development/README.pt-BR.md)

## Objetivo

Transformar um pedido em um programa pequeno e testável antes de abrir o editor (25–35 minutos).

## 1. Ler, reformular e modelar

Um clube de leitura fictício registra minutos inteiros de estudo por dia. Dada uma lista de inteiros não negativos, retorne o total dos dias que atingiram a meta de 20 minutos. Aqui “total” significa **soma dos minutos**, não quantidade de dias. Entrada vazia resulta em zero; a lista original não muda. Esclareça requisitos ambíguos antes de programar. Para `[12, 20, 25]`, os valores elegíveis são 20 e 25, portanto a resposta é 45.

## 2. Decompor e rastrear

Divida em identificar um valor elegível, acumular os minutos elegíveis e retornar o resultado. Escreva pseudocódigo independente de linguagem: iniciar total em zero; para cada valor, se for pelo menos a meta, adicioná-lo; retornar total após a iteração. O rastreamento do exemplo é 0 → 0 → 20 → 45. O acumulador representa a soma dos valores elegíveis já processados. Use um loop em vez de três índices fixos e uma função em vez de imprimir dentro do loop, para permitir testar o retorno.

## 3. Implementar e verificar

O exemplo compartilhado usa meta configurável, padrão 20. Tente escrever primeiro; depois compare com o [exemplo](examples/study_minutes.py). O contrato assume entradas e meta inteiras não negativas; não exige validação adicional. Teste entrada vazia, exatamente o limite, ausência de correspondências e valores repetidos. Se retornar cedo demais e obter 0, rastreie a indentação e mova o retorno para fora do loop.

## Prática

Altere o requisito fictício: retorne a **quantidade** de dias elegíveis, não os minutos. Escreva dois exemplos calculados à mão, pseudocódigo e uma função antes de consultar solução. Explique por que os contratos diferem. Para o exemplo original, a nova resposta é 2.

**Referência rápida:** contrato → exemplos → decomposição → rastreamento → código → testes → explicação.

Execute a partir do diretório da aula (Python 3.13 como base):

```bash
python examples/study_minutes.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../../manual-programming-practices/04-professional-workflow/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../02-constraints-and-edge-cases/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
