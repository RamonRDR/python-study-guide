# Contar pares não ordenados

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.unordered-pair-count` · **Dificuldade:** Fácil · 12 min

## Pré-requisitos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.pt-BR.md)
- [03-return-values](../../../functions/03-return-values/README.pt-BR.md)
- [05-type-hints](../../../functions/05-type-hints/README.pt-BR.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.pt-BR.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [03-int-float-and-bool](../../../strings-and-numbers/03-int-float-and-bool/README.pt-BR.md)
- [04-numeric-builtins](../../../strings-and-numbers/04-numeric-builtins/README.pt-BR.md)

## Contrato

Dado inteiro não negativo size <= 10**6, retorne quantidade de pares distintos de posições diferentes, sem considerar ordem. Cada posição combina com size-1 outras; isso conta cada par duas vezes. Use aritmética, não loops.

Somente o domínio declarado é avaliado; retorne valor e tipos exatos, sem imprimir, dependências externas nem modificar argumentos mutáveis. Não use a referência durante a tentativa independente.

Escreva pseudocódigo e implemente de forma independente antes de abrir a referência.

Copie o código inicial para diretório pessoal de prática. Python 3.13 é a base; execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def pair_count(size: int) -> int:
    raise NotImplementedError("Implement pair_count")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[0]` | `0` |
| `[1]` | `0` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Conte primeiro pares ordenados de posições diferentes.

</details>

<details>
<summary>Dica 2</summary>

Cada par não ordenado aparece duas vezes; divida por dois.

</details>

<details>
<summary>Dica 3</summary>

Use divisão inteira para retornar inteiro, inclusive tamanhos zero e um.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

O produto n(n-1) conta pares ordenados; divisão exata por dois elimina orientações duplicadas. Não há iteração no modelo de inteiros limitados declarado.

- Tempo: O(1)
- Espaço auxiliar: O(1)

Complexidade usa modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado; n é tamanho da entrada, m tamanho da segunda, k valores distintos, d dígitos decimais, e expoente, conforme aplicável. Armazenamento da saída é excluído do espaço auxiliar. Tempos com hash são esperados, não limites de pior caso.

</details>

## Validação

Confira suas próprias chamadas manualmente com os casos declarados e adicione pelo menos dois casos de borda. O comando a seguir na raiz testa apenas referências e implementações incorretas conhecidas, não seu arquivo pessoal. Respostas públicas são visíveis; não há correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
