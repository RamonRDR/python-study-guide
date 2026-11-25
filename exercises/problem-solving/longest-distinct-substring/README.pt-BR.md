# Maior substring sem repetição

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.longest-distinct-substring` · **Dificuldade:** Difícil · 35 min

## Pré-requisitos

- [01-defining-and-calling-functions](../../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [02-parameters-and-arguments](../../../functions/02-parameters-and-arguments/README.pt-BR.md)
- [03-return-values](../../../functions/03-return-values/README.pt-BR.md)
- [05-type-hints](../../../functions/05-type-hints/README.pt-BR.md)
- [04-for-loops-and-iteration](../../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [01-problem-solving-fundamentals](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
- [02-constraints-and-edge-cases](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.pt-BR.md)
- [03-algorithmic-complexity](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)
- [01-string-creation-and-indexing](../../../strings-and-numbers/01-string-creation-and-indexing/README.pt-BR.md)
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.pt-BR.md)
- [05-range-enumerate-and-zip](../../../program-flow/05-range-enumerate-and-zip/README.pt-BR.md)
- [07-problem-solving-patterns](../../../problem-solving-and-live-coding/07-problem-solving-patterns/README.pt-BR.md)
- [08-strings-and-numbers](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.pt-BR.md)

## Contrato

Retorne o comprimento da maior substring contígua sem caracteres exatos repetidos. Entrada vazia retorna 0. Compare caracteres Python originais, sem normalizar. Busque tempo linear esperado.

Somente domínios declarados são avaliados. Retorne tipos e valores exatos; não imprima, altere entradas nem adicione dependências. Escolha algorítmica e complexidade exigem revisão manual; testes funcionais não as provam.

Copie o inicial para diretório pessoal; Python 3.13 é a base. Execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def longest_distinct_length(text: str) -> int:
    raise NotImplementedError("Implement longest_distinct_length")
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[""]` | `0` |
| `["abba"]` | `2` |
| `["abcabcbb"]` | `3` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Registre última posição de cada caractere.

</details>

<details>
<summary>Dica 2</summary>

Se repetição estiver dentro da janela atual, mova limite esquerdo após última ocorrência.

</details>

<details>
<summary>Dica 3</summary>

Nunca mova left para trás; atualize melhor comprimento após registrar posição atual.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

A janela atual tem caracteres únicos. Repetição invalida apenas posições até ocorrência anterior dentro da janela. max(left, previous + 1) preserva progresso monotônico. Cada extremo direito é visitado uma vez.

- Tempo: O(n) esperado
- Espaço auxiliar: O(k)

Modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado, comportamento hash esperado quando aplicável. n/m são tamanhos (em listas aninhadas n conta todos itens e nós de lista visitados), k chaves distintas, h profundidade. Saída exigida excluída de espaço auxiliar; recursividade usa O(h) quadros.

</details>

## Validação

Confira suas próprias chamadas manualmente e adicione casos de borda. Na raiz do repositório, comando abaixo testa referências e implementações incorretas conhecidas, não seu código pessoal. Soluções públicas são visíveis; sem correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
