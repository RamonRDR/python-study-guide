# Primeiro rótulo repetido

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.first-repeated-label` · **Dificuldade:** Média · 18 min

## Pré-requisitos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.pt-BR.md)
- [03-return-values](../../../functions/03-return-values/README.pt-BR.md)
- [05-type-hints](../../../functions/05-type-hints/README.pt-BR.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.pt-BR.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [05-sets-and-unique-values](../../../collections/05-sets-and-unique-values/README.pt-BR.md)
- [07-break-continue-and-loop-else](../../../program-flow/07-break-continue-and-loop-else/README.pt-BR.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)

## Contrato

Retorne o rótulo cuja segunda ocorrência aparece primeiro na varredura da esquerda para a direita. Retorne None se não houver repetição; string vazia é válida. Preserve a entrada.

Somente o domínio declarado é avaliado; retorne valor e tipos exatos, sem imprimir, dependências externas nem modificar argumentos mutáveis. Não use a referência durante a tentativa independente.

Escreva pseudocódigo e implemente de forma independente antes de abrir a referência.

Copie o código inicial para diretório pessoal de prática. Python 3.13 é a base; execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def first_repeated_label(labels: list[str]) -> str | None:
    raise NotImplementedError("Implement first_repeated_label")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `null` |
| `[["a","b","b","a"]]` | `"b"` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Registre rótulos já vistos.

</details>

<details>
<summary>Dica 2</summary>

Teste pertinência antes de adicionar rótulo atual.

</details>

<details>
<summary>Dica 3</summary>

Retorne imediatamente na primeira repetição; senão retorne None após o loop.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

O set representa rótulos de posições anteriores. O primeiro encontro é a segunda ocorrência mais cedo, não a primeira posição original.

- Tempo: O(n) esperado
- Espaço auxiliar: O(k)

Complexidade usa modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado; n é tamanho da entrada, m tamanho da segunda, k valores distintos, d dígitos decimais, e expoente, conforme aplicável. Armazenamento da saída é excluído do espaço auxiliar. Tempos com hash são esperados, não limites de pior caso.

</details>

## Validação

Confira suas próprias chamadas manualmente com os casos declarados e adicione pelo menos dois casos de borda. O comando a seguir na raiz testa apenas referências e implementações incorretas conhecidas, não seu arquivo pessoal. Respostas públicas são visíveis; não há correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/09-collections/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
