# Intervalo do alvo por busca binária

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.binary-target-range` · **Dificuldade:** Difícil · 32 min

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
- [05-searching-algorithms](../../../problem-solving-and-live-coding/05-searching-algorithms/README.pt-BR.md)
- [11-searching-and-sorting](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.pt-BR.md)

## Contrato

Dada lista crescente de inteiros, retorne índices inclusivos [first, last] do alvo, ou [-1, -1] se ausente. Use duas buscas binárias de fronteira, não varredura linear; preserve entrada. Ordenação garantida.

Somente domínios declarados são avaliados. Retorne tipos e valores exatos; não imprima, altere entradas nem adicione dependências. Escolha algorítmica e complexidade exigem revisão manual; testes funcionais não as provam.

Copie o inicial para diretório pessoal; Python 3.13 é a base. Execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def target_range(values: list[int], target: int) -> list[int]:
    raise NotImplementedError("Implement target_range")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[],3]` | `[-1,-1]` |
| `[[2,4,4,4,7],4]` | `[1,3]` |
| `[[1,1,1],1]` | `[0,2]` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Encontre primeira posição cujo valor é pelo menos alvo.

</details>

<details>
<summary>Dica 2</summary>

Se ausente ou além da lista, retorne par de ausência.

</details>

<details>
<summary>Dica 3</summary>

Encontre primeira posição estritamente maior; subtraia um para último encontro.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

As duas buscas semiabertas encontram fronteiras do bloco contíguo de iguais. Fronteira direita é exclusiva. Conferir esquerda evita reportar alvo inexistente.

- Tempo: O(log n)
- Espaço auxiliar: O(1)

Modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado, comportamento hash esperado quando aplicável. n/m são tamanhos (em listas aninhadas n conta todos itens e nós de lista visitados), k chaves distintas, h profundidade. Saída exigida excluída de espaço auxiliar; recursividade usa O(h) quadros.

</details>

## Validação

Confira suas próprias chamadas manualmente e adicione casos de borda. Na raiz do repositório, comando abaixo testa referências e implementações incorretas conhecidas, não seu código pessoal. Soluções públicas são visíveis; sem correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/11-searching-and-sorting/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
