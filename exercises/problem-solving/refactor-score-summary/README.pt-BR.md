# Refatorar resumo de notas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.refactor-score-summary` · **Dificuldade:** Média · 22 min

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
- [04-dictionaries-keys-and-values](../../../collections/04-dictionaries-keys-and-values/README.pt-BR.md)
- [06-pep8-and-readability](../../../comments-and-documentation/06-pep8-and-readability/README.pt-BR.md)
- [03-test-driven-development](../../../manual-programming-practices/03-test-driven-development/README.pt-BR.md)

## Contrato

Refatore inicial funcional para notas inteiras 0–100. Retorne dicionário com contagens total, passed e failed; nota >= 60 aprova. Preserve entrada. Use nomes descritivos e uma passagem de classificação; revise clareza manualmente.

Somente o domínio declarado é avaliado; retorne valor e tipos exatos, sem imprimir, dependências externas nem modificar argumentos mutáveis. Não use a referência durante a tentativa independente.

O inicial já passa testes funcionais. Preserve comportamento, faça mudança estrutural solicitada e inspecione o diff. Testes de saída não avaliam legibilidade nem escolha de algoritmo.

Copie o código inicial para diretório pessoal de prática. Python 3.13 é a base; execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def summarize_scores(scores: list[int]) -> dict[str, int]:
    a = 0
    for x in scores:
        if x >= 60:
            a += 1
    b = 0
    for x in scores:
        if x < 60:
            b += 1
    return {"total": len(scores), "passed": a, "failed": b}
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[[]]` | `{"total":0,"passed":0,"failed":0}` |
| `[[59,60,61]]` | `{"total":3,"passed":2,"failed":1}` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Preserve contrato e escreva testes de borda em torno de 60.

</details>

<details>
<summary>Dica 2</summary>

Conte aprovados em um loop com variável descritiva.

</details>

<details>
<summary>Dica 3</summary>

Calcule failed como total menos passed; verifique casos originais.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

Cada nota é aprovada ou reprovada, logo failed é total menos passed. Um loop de classificação evita repetição. Testes verificam comportamento, não legibilidade.

- Tempo: O(n)
- Espaço auxiliar: O(1)

Complexidade usa modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado; n é tamanho da entrada, m tamanho da segunda, k valores distintos, d dígitos decimais, e expoente, conforme aplicável. Armazenamento da saída é excluído do espaço auxiliar. Tempos com hash são esperados, não limites de pior caso.

</details>

## Validação

Confira suas próprias chamadas manualmente com os casos declarados e adicione pelo menos dois casos de borda. O comando a seguir na raiz testa apenas referências e implementações incorretas conhecidas, não seu arquivo pessoal. Respostas públicas são visíveis; não há correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/14-refactoring-challenges/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
