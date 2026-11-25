# Recursividade

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../03-algorithmic-complexity/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../05-searching-algorithms/README.pt-BR.md)
<!-- /chapter-navigation:top -->

**Pré-requisitos:** [Valores de retorno](../../functions/03-return-values/README.pt-BR.md) · [Escopo](../../functions/04-scope/README.pt-BR.md) · [Funções](../../functions/08-functions-working-together/README.pt-BR.md) · [Complexidade](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)

## Objetivo

Entender chamadas à própria função, caso base, progresso e pilha de chamadas (35–45 minutos).

## 1. Uma instância menor do mesmo problema

Recursividade resolve um problema chamando a mesma função para uma instância menor. O caso base retorna sem nova chamada; o passo recursivo deve avançar até ele. Para somar inteiros de 1 até n, use sum(0) = 0 e sum(n) = n + sum(n - 1) para n positivo. Cada chamada tem variáveis locais próprias; chamadas anteriores aguardam resultados posteriores.

Para n = 3: as chamadas descem 3 → 2 → 1 → 0. Os retornos desenrolam 0 → 1 → 3 → 6. Ausência de caso base ou chamada com n + 1 não termina para n positivo.

## 2. Implementação Python

O [exemplo](examples/recursive_sum.py) aceita inteiros exatos de 0 a 100. Rejeita valores fora do domínio antes de recursar e usa função auxiliar privada para não repetir validação. O limite é uma restrição didática, não uma garantia para toda configuração de pilha Python. Python limita a profundidade e pode gerar RecursionError; não aumente o limite só para resolver um problema linear. Um acumulador iterativo evita crescimento da pilha.

No modelo de aritmética de custo fixo, ambas as versões levam O(n) de tempo; a recursiva usa O(n) de espaço auxiliar na pilha, e a iterativa O(1). Uma fórmula fechada evita iteração, mas o objetivo aqui é compreender estrutura recursiva.

## Prática

Rastreie n = 4 em uma tabela de chamadas pendentes e valores retornados. Implemente uma função recursiva de contagem regressiva que retorne a quantidade de passos até zero para n de 0 a 100. Teste 0 e 1; compare com loop. Explique por que o argumento decrescente prova progresso e por que validar negativos importa.

**Referência rápida:** caso base + entrada menor + combinar retornos; conte quadros da pilha como espaço auxiliar.

Execute a partir do diretório da aula (Python 3.13 como base):

```bash
python examples/recursive_sum.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../03-algorithmic-complexity/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../05-searching-algorithms/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
