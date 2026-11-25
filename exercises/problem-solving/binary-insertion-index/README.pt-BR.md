# Índice de inserção binária

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.binary-insertion-index` · **Dificuldade:** Média · 22 min

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
- [06-while-loops-and-state-driven-repetition](../../../program-flow/06-while-loops-and-state-driven-repetition/README.pt-BR.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.pt-BR.md)

## Contrato

Dada lista crescente ordenada de inteiros, retorne primeiro índice onde alvo pode ser inserido sem quebrar ordem, antes dos iguais. Retorne len(values) se todos menores. Use busca binária; não altere nem valide ordenação por varredura.

Somente o domínio declarado é avaliado; retorne valor e tipos exatos, sem imprimir, dependências externas nem modificar argumentos mutáveis. Não use a referência durante a tentativa independente.

Escreva pseudocódigo e implemente de forma independente antes de abrir a referência.

Copie o código inicial para diretório pessoal de prática. Python 3.13 é a base; execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def insertion_index(values: list[int], target: int) -> int:
    raise NotImplementedError("Implement insertion_index")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],3]` | `0` |
| `[[2,4,4,7],4]` | `1` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Use intervalo semiaberto de zero a len(values).

</details>

<details>
<summary>Dica 2</summary>

Descarte até mid apenas quando valor central for estritamente menor.

</details>

<details>
<summary>Dica 3</summary>

Quando limites se igualarem, retorne índice sem acessar lista novamente.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Intervalo decrescente mantém primeira posição cujo valor não é menor, ou sentinela final. Ao contrário da busca exata, valor ausente ainda tem índice de inserção.

- Tempo: O(log n)
- Espaço auxiliar: O(1)

Complexidade usa modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado; n é tamanho da entrada, m tamanho da segunda, k valores distintos, d dígitos decimais, e expoente, conforme aplicável. Armazenamento da saída é excluído do espaço auxiliar. Tempos com hash são esperados, não limites de pior caso.

</details>

## Validação

Confira suas próprias chamadas manualmente com os casos declarados e adicione pelo menos dois casos de borda. O comando a seguir na raiz testa apenas referências e implementações incorretas conhecidas, não seu arquivo pessoal. Respostas públicas são visíveis; não há correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
