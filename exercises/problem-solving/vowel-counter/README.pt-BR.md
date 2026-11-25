# Contador de vogais

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.vowel-counter` · **Dificuldade:** Fácil · **Tempo estimado:** 10 min

## Pré-requisitos

- [Strings e acesso a caracteres](../../../strings-and-numbers/01-string-creation-and-indexing/README.pt-BR.md)
- [Pertinência e normalização de strings](../../../strings-and-numbers/02-common-string-methods/README.pt-BR.md)
- [Pertinência e condições booleanas](../../../program-flow/01-conditions-comparisons-and-boolean-logic/README.pt-BR.md)
- [Iteração com for](../../../program-flow/04-for-loops-and-iteration/README.pt-BR.md)
- [Definição de funções](../../../functions/01-defining-and-calling-functions/README.pt-BR.md)
- [Parâmetros](../../../functions/02-parameters-and-arguments/README.pt-BR.md)
- [Valores de retorno](../../../functions/03-return-values/README.pt-BR.md)
- [Anotações de tipo](../../../functions/05-type-hints/README.pt-BR.md)
- [Acumulador e decomposição](../../../problem-solving-and-live-coding/01-problem-solving-fundamentals/README.pt-BR.md)
- [Testes de borda](../../../problem-solving-and-live-coding/02-constraints-and-edge-cases/README.pt-BR.md)
- [Complexidade](../../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)

## Objetivo

Implemente count_vowels(text) e retorne a quantidade de vogais ASCII A, E, I, O, U (maiúsculas ou minúsculas) na string de entrada. Conte ocorrências repetidas; ignore todos os demais caracteres.

- A entrada é uma str Python, inclusive vazia; outros tipos estão fora do contrato.
- Apenas os dez caracteres ASCII literais aeiouAEIOU contam. Letras acentuadas, y/Y, dígitos, pontuação, espaços e outros caracteres Unicode não contam.
- Retorne um int, não string, booleano ou saída impressa. Não são necessárias dependências externas nem operações de entrada/saída.

Tente de forma independente primeiro. Copie o código inicial para um diretório pessoal de prática; não edite a solução de referência do repositório. Python 3.13 é a base; o exercício usa apenas a linguagem padrão. Execução no navegador não foi verificada. Testes e soluções públicos são visíveis, não secretos.

[Código inicial](starter.py) · [Registro estruturado](exercise.json)

```python
def count_vowels(text: str) -> int:
    raise NotImplementedError("Implement count_vowels")
```

## Exemplos

| Entrada | Esperado | Motivo |
| --- | ---: | --- |
| `"Hello, World!"` | 3 | e, o e o contam. |
| `"AEIOU"` | 5 | As cinco vogais maiúsculas contam. |
| `""` | 0 | Não há caracteres para contar. |
| `"Aéİu🙂"` | 2 | Apenas A e u contam. |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Qual deve ser o valor do contador antes de ler qualquer caractere?

</details>

<details>
<summary>Dica 2</summary>

Percorra a string original com for; teste pertinência na string literal de vogais ASCII.

</details>

<details>
<summary>Dica 3</summary>

Incremente apenas quando houver correspondência e retorne o contador após o loop.

</details>

## Referência e explicação

<details>
<summary>Revelar após sua tentativa</summary>

[Solução de referência](solution.py)

Comece em zero. Para cada caractere original, incremente uma vez se pertencer a aeiouAEIOU. Retorne a contagem acumulada após o loop. Isso conta repetições e trata maiúsculas sem conversão de caixa Unicode. Converter a string inteira com lower() pode transformar U+0130 (İ) em i ASCII seguido de uma marca combinante, alterando o contrato. Retornar dentro do loop ignoraria caracteres posteriores.

- Tempo: O(n), uma passagem pelos n caracteres da string Python; pertinência em uma string fixa de dez caracteres tem custo limitado.
- Espaço: O(1) variáveis auxiliares no modelo usual de custo fixo; o contador usa O(log n) bits se contabilizado armazenamento de inteiros arbitrários.

</details>

## Validação

Teste seu próprio arquivo manualmente chamando count_vowels com as entradas acima e comparando os inteiros retornados. Adicione pelo menos dois casos antes de olhar a referência. O comando abaixo, executado na raiz, verifica a referência e implementações incorretas conhecidas, não seu arquivo pessoal. Não executa código arbitrário de estudantes.

```bash
python -m unittest discover -s tests -p "test_problem_solving_pilot.py"
```

[Código dos testes](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/08-strings-and-numbers/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
