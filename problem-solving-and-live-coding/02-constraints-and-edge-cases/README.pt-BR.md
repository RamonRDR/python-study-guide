# Restrições e casos de borda

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../01-problem-solving-fundamentals/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../03-algorithmic-complexity/README.pt-BR.md)
<!-- /chapter-navigation:top -->

**Pré-requisitos:** [Parameters](../../functions/02-parameters-and-arguments/README.pt-BR.md) · [Return values](../../functions/03-return-values/README.pt-BR.md) · [pytest](../../external-libraries/04-pytest/README.pt-BR.md) · [TDD](../../manual-programming-practices/03-test-driven-development/README.pt-BR.md)

## Objetivo

Transformar restrições de entrada em comportamento explícito e testes úteis (25–35 minutos).

## 1. Domínio e limites

Uma oficina fictícia aceita um grupo se o tamanho estiver entre 1 e a capacidade da sala, inclusive. Ambos os argumentos devem ser inteiros exatos (não booleanos); capacidade deve ser pelo menos 1 e tamanho não negativo. Retorne booleano para argumentos válidos, gere TypeError para tipos errados antes de verificar valores e ValueError para valores inválidos. Não imponha limites arbitrários alheios ao contrato.

| Grupo | Capacidade | Esperado |
| --- | --- | --- |
| 0 | 5 | False |
| 1 | 5 | True |
| 5 | 5 | True |
| 6 | 5 | False |
| -1 | 5 | ValueError |
| 2 | 0 | ValueError |
| True | 5 | TypeError |

Caso de borda é um limite ou condição válida incomum; entrada inválida viola o contrato. Teste abaixo, no e acima de cada limite relevante. Erro de tipo difere de uma reserva válida, porém rejeitada.

## 2. Converter exemplos em testes

Escreva o resultado esperado independentemente da implementação. Use igualdade exata para booleanos e verifique tipos de exceção para entradas inválidas. Em Python, `isinstance(True, int)` é verdadeiro; o requisito de inteiro exato exige `type(value) is int`. Use comparação inclusiva somente após validar argumentos. Veja o [exemplo](examples/capacity.py). Uma solução com limite superior estrito falharia no teste em que tamanho iguala capacidade; isso verifica a capacidade de detectar erros. Evite testar texto de exceções salvo exigência do contrato.

## Prática

Monte uma tabela de limites para um armário fictício que aceita pesos de 1 a 10 unidades inteiras, inclusive. Especifique quais entradas geram erros e quais retornam False antes de programar. Adicione um caso que detecte trocar `<=` por `<`. Explique por que testar apenas valores típicos é insuficiente.

**Referência rápida:** defina domínio válido, resultado esperado, política de entradas inválidas e testes de limites antes de programar.

Execute a partir do diretório da aula (Python 3.13 como base):

```bash
python examples/capacity.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../01-problem-solving-fundamentals/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../03-algorithmic-complexity/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
