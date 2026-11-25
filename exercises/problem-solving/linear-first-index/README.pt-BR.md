# Primeiro índice correspondente

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.linear-first-index` · **Dificuldade:** Fácil · 12 min

## Pré-requisitos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.pt-BR.md)
- [03-return-values](../../../functions/03-return-values/README.pt-BR.md)
- [05-type-hints](../../../functions/05-type-hints/README.pt-BR.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.pt-BR.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.pt-BR.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.pt-BR.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.pt-BR.md)

## Contrato

Dada lista desordenada de inteiros e alvo, retorne o primeiro índice correspondente ou -1 se ausente. Não altere a entrada nem use list.index.

Somente o domínio declarado é avaliado; retorne valor e tipos exatos, sem imprimir, dependências externas nem modificar argumentos mutáveis. Não use a referência durante a tentativa independente.

Escreva pseudocódigo e implemente de forma independente antes de abrir a referência.

Copie o código inicial para diretório pessoal de prática. Python 3.13 é a base; execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def first_index(values: list[int], target: int) -> int:
    raise NotImplementedError("Implement first_index")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],3]` | `-1` |
| `[[8,4,4,9],4]` | `1` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Use enumerate para obter índice e valor.

</details>

<details>
<summary>Dica 2</summary>

Compare o valor com o alvo.

</details>

<details>
<summary>Dica 3</summary>

Retorne no primeiro encontro; retorne -1 só após varrer.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Varrer em ordem torna a primeira ocorrência definitiva. Ausência é diferente do índice zero.

- Tempo: O(n)
- Espaço auxiliar: O(1)

Complexidade usa modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado; n é tamanho da entrada, m tamanho da segunda, k valores distintos, d dígitos decimais, e expoente, conforme aplicável. Armazenamento da saída é excluído do espaço auxiliar. Tempos com hash são esperados, não limites de pior caso.

</details>

## Validação

Confira suas próprias chamadas manualmente com os casos declarados e adicione pelo menos dois casos de borda. O comando a seguir na raiz testa apenas referências e implementações incorretas conhecidas, não seu arquivo pessoal. Respostas públicas são visíveis; não há correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
