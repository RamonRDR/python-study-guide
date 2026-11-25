# Contar pares-alvo com duplicados

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.sorted-pair-multiplicity` · **Dificuldade:** Difícil · 40 min

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
- [06-while-loops-and-state-driven-repetition](../../../program-flow/06-while-loops-and-state-driven-repetition/README.pt-BR.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.pt-BR.md)
- [12-algorithms-and-complexity](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.pt-BR.md)

## Contrato

Dada lista crescente de inteiros, conte pares de índices i < j cujos valores somam alvo. Valores iguais em índices diferentes são ocorrências distintas; preserve entrada. Use dois ponteiros agrupados em O(n) e espaço auxiliar constante.

Somente domínios declarados são avaliados. Retorne tipos e valores exatos; não imprima, altere entradas nem adicione dependências. Escolha algorítmica e complexidade exigem revisão manual; testes funcionais não as provam.

Copie o inicial para diretório pessoal; Python 3.13 é a base. Execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def count_target_pairs(values: list[int], target: int) -> int:
    raise NotImplementedError("Implement count_target_pairs")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],4]` | `0` |
| `[[1,1,3,3,3],4]` | `6` |
| `[[2,2,2,2],4]` | `6` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Compare soma dos valores extremos com alvo.

</details>

<details>
<summary>Dica 2</summary>

Na igualdade com extremos distintos, conte cada grupo de iguais e multiplique contagens.

</details>

<details>
<summary>Dica 3</summary>

Se extremos iguais, todas posições restantes têm esse valor: some k(k-1)//2 e pare.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Ordenação permite descartar extremo impossível. Grupos distintos correspondentes com tamanhos a e b geram a*b pares cruzados. Com extremos iguais, todo par das k posições restantes conta uma vez. Cada ponteiro avança monotonicamente.

- Tempo: O(n)
- Espaço auxiliar: O(1)

Modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado, comportamento hash esperado quando aplicável. n/m são tamanhos (em listas aninhadas n conta todos itens e nós de lista visitados), k chaves distintas, h profundidade. Saída exigida excluída de espaço auxiliar; recursividade usa O(h) quadros.

</details>

## Validação

Confira suas próprias chamadas manualmente e adicione casos de borda. Na raiz do repositório, comando abaixo testa referências e implementações incorretas conhecidas, não seu código pessoal. Soluções públicas são visíveis; sem correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/12-algorithms-and-complexity/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
