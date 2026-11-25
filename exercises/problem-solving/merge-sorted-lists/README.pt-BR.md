# Intercalar listas ordenadas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.merge-sorted-lists` · **Dificuldade:** Difícil · 30 min

## Pré-requisitos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.pt-BR.md)
- [03-return-values](../../../functions/03-return-values/README.pt-BR.md)
- [05-type-hints](../../../functions/05-type-hints/README.pt-BR.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.pt-BR.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)
- [01-list-creation-and-indexing](../../../collections/01-list-creation-and-indexing/README.pt-BR.md)
- [02-modifying-lists-and-methods](../../../collections/02-modifying-lists-and-methods/README.pt-BR.md)
- [06-while-loops-and-state-driven-repetition](../../../program-flow/06-while-loops-and-state-driven-repetition/README.pt-BR.md)
- [06-sorting-algorithms](../../../problem-solving-and-live-coding/06-sorting-algorithms/README.pt-BR.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)
- [11-searching-and-sorting](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.pt-BR.md)

## Contrato

Dadas duas listas crescentes de inteiros, retorne nova lista crescente contendo cada ocorrência de ambas. Preserve entradas e duplicados; use intercalação com dois ponteiros em O(n+m), não ordene concatenação.

Somente domínios declarados são avaliados. Retorne tipos e valores exatos; não imprima, altere entradas nem adicione dependências. Escolha algorítmica e complexidade exigem revisão manual; testes funcionais não as provam.

Copie o inicial para diretório pessoal; Python 3.13 é a base. Execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    raise NotImplementedError("Implement merge_sorted")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],[]]` | `[]` |
| `[[1,3],[2,4]]` | `[1,2,3,4]` |
| `[[1,1],[1,2]]` | `[1,1,1,2]` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Mantenha ponteiro para primeiro elemento não consumido de cada lista.

</details>

<details>
<summary>Dica 2</summary>

Acrescente menor elemento atual e avance apenas seu ponteiro.

</details>

<details>
<summary>Dica 3</summary>

Quando uma lista acabar, acrescente elementos restantes da outra.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Prefixo da saída está sempre ordenado e contém exatamente elementos consumidos. Selecionar menor cabeça preserva ordem; consumir restante preserva multiplicidades. Cada posição avança uma vez.

- Tempo: O(n+m)
- Espaço auxiliar: O(1)

Modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado, comportamento hash esperado quando aplicável. n/m são tamanhos (em listas aninhadas n conta todos itens e nós de lista visitados), k chaves distintas, h profundidade. Saída exigida excluída de espaço auxiliar; recursividade usa O(h) quadros.

</details>

## Validação

Confira suas próprias chamadas manualmente e adicione casos de borda. Na raiz do repositório, comando abaixo testa referências e implementações incorretas conhecidas, não seu código pessoal. Soluções públicas são visíveis; sem correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
