# Depurar janela negativa

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.debug-negative-window` · **Dificuldade:** Média · 22 min

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
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)
- [01-manual-coding-and-debugging](../../../manual-programming-practices/01-manual-coding-and-debugging/README.pt-BR.md)

## Contrato

Corrija algoritmo de janela fixa fornecido. Dados lista de inteiros e size válido 1 <= size <= len(values), retorne maior soma de exatamente size elementos consecutivos. Listas só negativas são válidas. Preserve entrada e use uma janela móvel.

Somente o domínio declarado é avaliado; retorne valor e tipos exatos, sem imprimir, dependências externas nem modificar argumentos mutáveis. Não use a referência durante a tentativa independente.

Reproduza o defeito, rastreie estado, faça correção mínima e repita os casos.

Copie o código inicial para diretório pessoal de prática. Python 3.13 é a base; execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def max_window_sum(values: list[int], size: int) -> int:
    total = 0
    for index in range(size):
        total += values[index]
    best = max(0, total)
    for index in range(size, len(values)):
        total += values[index] - values[index - size]
        best = max(best, total)
    return best
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[-4,-2,-3],2]` | `-5` |
| `[[4,-1,3,2],2]` | `5` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Execute inicial em [-4, -2, -3] com size 2.

</details>

<details>
<summary>Dica 2</summary>

Zero não é soma de nenhuma janela válida nesse caso.

</details>

<details>
<summary>Dica 3</summary>

Inicialize best com soma da primeira janela real e atualize ao mover.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Inicializar best em zero inventa janela inexistente quando todas somas são negativas. Primeira soma real estabelece base válida.

- Tempo: O(n)
- Espaço auxiliar: O(1)

Complexidade usa modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado; n é tamanho da entrada, m tamanho da segunda, k valores distintos, d dígitos decimais, e expoente, conforme aplicável. Armazenamento da saída é excluído do espaço auxiliar. Tempos com hash são esperados, não limites de pior caso.

</details>

## Validação

Confira suas próprias chamadas manualmente com os casos declarados e adicione pelo menos dois casos de borda. O comando a seguir na raiz testa apenas referências e implementações incorretas conhecidas, não seu arquivo pessoal. Respostas públicas são visíveis; não há correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/13-debugging-challenges/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
