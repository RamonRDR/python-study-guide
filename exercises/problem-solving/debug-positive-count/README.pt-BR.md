# Depurar contador de positivos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.debug-positive-count` · **Dificuldade:** Fácil · 12 min

## Pré-requisitos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.pt-BR.md)
- [03-return-values](../../../functions/03-return-values/README.pt-BR.md)
- [05-type-hints](../../../functions/05-type-hints/README.pt-BR.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.pt-BR.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [01-conditions-comparisons-and-boolean-logic](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.pt-BR.md)
- [01-manual-coding-and-debugging](../../../manual-programming-practices/01-manual-coding-and-debugging/README.pt-BR.md)

## Contrato

Corrija a implementação fornecida para retornar quantidade de inteiros estritamente positivos de uma lista. Zero não é positivo. Preserve entrada; retorne zero para lista vazia.

Somente o domínio declarado é avaliado; retorne valor e tipos exatos, sem imprimir, dependências externas nem modificar argumentos mutáveis. Não use a referência durante a tentativa independente.

Reproduza o defeito, rastreie estado, faça correção mínima e repita os casos.

Copie o código inicial para diretório pessoal de prática. Python 3.13 é a base; execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def count_positive(values: list[int]) -> int:
    count = 0
    for value in values:
        if value >= 0:
            count += 1
    return count
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `0` |
| `[[0]]` | `0` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Reproduza bug com lista unitária contendo zero.

</details>

<details>
<summary>Dica 2</summary>

Rastreie condição para negativos, zero e positivos.

</details>

<details>
<summary>Dica 3</summary>

Altere comparação para incrementar apenas positivos estritos.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

O original inclui zero por causa de >=. Alteração mínima para > atende especificação; caso só com zero distingue as implementações.

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
