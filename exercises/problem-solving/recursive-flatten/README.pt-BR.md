# Achatar listas aninhadas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.recursive-flatten` · **Dificuldade:** Difícil · 35 min

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
- [05-type-and-isinstance](../../../fundamentals/05-type-and-isinstance/README.pt-BR.md)
- [04-recursion](../../../problem-solving-and-live-coding/04-recursion/README.pt-BR.md)
- [09-data-flow-between-functions](../../../functions/09-data-flow-between-functions/README.pt-BR.md)
- [10-functions-and-recursion](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.pt-BR.md)
- [04-scope](../../../functions/04-scope/README.pt-BR.md)
- [08-functions-working-together](../../../functions/08-functions-working-together/README.pt-BR.md)

## Contrato

Dada lista aninhada finita contendo apenas inteiros e listas, com até 10 níveis de listas abaixo da externa, retorne nova lista plana de inteiros em ordem esquerda-direita em profundidade. Preserve duplicados e entrada. Use recursividade; não há ciclos nem referências mutáveis compartilhadas.

Somente domínios declarados são avaliados. Retorne tipos e valores exatos; não imprima, altere entradas nem adicione dependências. Escolha algorítmica e complexidade exigem revisão manual; testes funcionais não as provam.

Copie o inicial para diretório pessoal; Python 3.13 é a base. Execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def flatten(values: list) -> list[int]:
    raise NotImplementedError("Implement flatten")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `[]` |
| `[[1,[2,[3]],4]]` | `[1,2,3,4]` |
| `[[[[]],[],[0]]]` | `[0]` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Use uma lista de resultado compartilhada por função auxiliar recursiva.

</details>

<details>
<summary>Dica 2</summary>

Para cada item, diferencie lista de inteiro.

</details>

<details>
<summary>Dica 3</summary>

Visite lista interna imediatamente; acrescente inteiro diretamente.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Auxiliar percorre cada lista em ordem e acrescenta cada inteiro folha uma vez. Listas vazias não acrescentam nada. Um acumulador de saída evita cópias repetidas; profundidade de pilha é profundidade de aninhamento.

- Tempo: O(n)
- Espaço auxiliar: O(h)

Modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado, comportamento hash esperado quando aplicável. n/m são tamanhos (em listas aninhadas n conta todos itens e nós de lista visitados), k chaves distintas, h profundidade. Saída exigida excluída de espaço auxiliar; recursividade usa O(h) quadros.

</details>

## Validação

Confira suas próprias chamadas manualmente e adicione casos de borda. Na raiz do repositório, comando abaixo testa referências e implementações incorretas conhecidas, não seu código pessoal. Soluções públicas são visíveis; sem correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/10-functions-and-recursion/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
