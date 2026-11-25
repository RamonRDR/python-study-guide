# Conciliar registros de estoque

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.inventory-reconciliation` · **Dificuldade:** Difícil · 40 min

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
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.pt-BR.md)
- [02-modifying-lists-and-methods](../../../collections/02-modifying-lists-and-methods/README.pt-BR.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)
- [09-data-flow-between-functions](../../../functions/09-data-flow-between-functions/README.pt-BR.md)
- [15-mixed-challenges](../../../problem-solving-and-live-coding/15-mixed-challenges/README.pt-BR.md)

## Contrato

Cada entrada é lista de linhas [label, quantity], com rótulos de string exatos e quantidades inteiras não negativas. Agregue duplicados separadamente e retorne linhas [label, expected_total, actual_total, actual_total - expected_total] somente para totais diferentes. Ordene por primeira ocorrência em expected, seguida da primeira ocorrência de rótulos exclusivos de actual. Quantidades ausentes são zero; preserve entradas.

Somente domínios declarados são avaliados. Retorne tipos e valores exatos; não imprima, altere entradas nem adicione dependências. Escolha algorítmica e complexidade exigem revisão manual; testes funcionais não as provam.

Copie o inicial para diretório pessoal; Python 3.13 é a base. Execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def reconcile(expected: list[list], actual: list[list]) -> list[list]:
    raise NotImplementedError("Implement reconcile")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],[]]` | `[]` |
| `[[["a",2],["a",3]],[["a",4]]]` | `[["a",5,4,-1]]` |
| `[[["b",2],["a",1]],[["a",1],["c",3]]]` | `[["b",2,0,-2],["c",0,3,3]]` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Monte dois dicionários independentes de totais.

</details>

<details>
<summary>Dica 2</summary>

Monte sequência ordenada de rótulos únicos nas duas entradas.

</details>

<details>
<summary>Dica 3</summary>

Compare totais com padrão zero e acrescente apenas diferenças não zero.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Separe agregação de ordenação e comparação. Set de vistos evita linhas duplicadas; preservar primeira ocorrência não exige ordenar. Padrão zero torna ausência equivalente a quantidade explicitamente zero.

- Tempo: O(n+m) esperado
- Espaço auxiliar: O(k)

Modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado, comportamento hash esperado quando aplicável. n/m são tamanhos (em listas aninhadas n conta todos itens e nós de lista visitados), k chaves distintas, h profundidade. Saída exigida excluída de espaço auxiliar; recursividade usa O(h) quadros.

</details>

## Validação

Confira suas próprias chamadas manualmente e adicione casos de borda. Na raiz do repositório, comando abaixo testa referências e implementações incorretas conhecidas, não seu código pessoal. Soluções públicas são visíveis; sem correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/15-mixed-challenges/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
