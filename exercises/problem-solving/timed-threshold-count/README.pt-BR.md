# Cronometrado: contar pelo limite

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.timed-threshold-count` · **Dificuldade:** Fácil · 10 min

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
- [01-conditions-comparisons-and-boolean-logic](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.pt-BR.md)
- [16-timed-live-coding](../../../problem-solving-and-live-coding/16-timed-live-coding/README.pt-BR.md)

## Contrato

Retorne a quantidade de inteiros maiores ou iguais ao limite. Preserve lista; entrada vazia retorna zero. Conte ocorrências repetidas, não valores distintos.

Somente domínios declarados são avaliados. Retorne tipos e valores exatos; não imprima, altere entradas nem adicione dependências. Escolha algorítmica e complexidade exigem revisão manual; testes funcionais não as provam.

Use cronômetro pessoal. Trabalhe sozinho, sem dicas, referência ou IA na primeira tentativa. No limite registre progresso, pare o cronômetro, termine e compare. Tempo é autorrelatado, não avaliado pelo CI.

Copie o inicial para diretório pessoal; Python 3.13 é a base. Execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def count_at_least(values: list[int], threshold: int) -> int:
    raise NotImplementedError("Implement count_at_least")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],2]` | `0` |
| `[[2,2,3,1],2]` | `3` |
| `[[-3,-2,0],-2]` | `2` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Inicialize contador antes de iterar.

</details>

<details>
<summary>Dica 2</summary>

Use comparação inclusiva.

</details>

<details>
<summary>Dica 3</summary>

Retorne após processar toda lista.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Contador conta exatamente elementos elegíveis processados. Comparação inclusiva trata igualdade e loop vazio deixa zero.

- Tempo: O(n)
- Espaço auxiliar: O(1)

Modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado, comportamento hash esperado quando aplicável. n/m são tamanhos (em listas aninhadas n conta todos itens e nós de lista visitados), k chaves distintas, h profundidade. Saída exigida excluída de espaço auxiliar; recursividade usa O(h) quadros.

</details>

## Validação

Confira suas próprias chamadas manualmente e adicione casos de borda. Na raiz do repositório, comando abaixo testa referências e implementações incorretas conhecidas, não seu código pessoal. Soluções públicas são visíveis; sem correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/16-timed-live-coding/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
