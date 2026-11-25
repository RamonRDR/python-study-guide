# Refatorar taxa de entrega

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

**ID:** `problem-solving.refactor-shipping-fee` · **Dificuldade:** Fácil · 15 min

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
- [02-if-elif-and-else](../../../program-flow/02-if-elif-and-else/README.pt-BR.md)
- [06-pep8-and-readability](../../../comments-and-documentation/06-pep8-and-readability/README.pt-BR.md)
- [03-test-driven-development](../../../manual-programming-practices/03-test-driven-development/README.pt-BR.md)

## Contrato

Refatore código inicial funcional sem mudar comportamento. Para totais não negativos em unidades fictícias, entrega é grátis em total >= 100 ou para membros; senão custa 12. Use condição combinada clara e evite retornos duplicados.

Somente o domínio declarado é avaliado; retorne valor e tipos exatos, sem imprimir, dependências externas nem modificar argumentos mutáveis. Não use a referência durante a tentativa independente.

O inicial já passa testes funcionais. Preserve comportamento, faça mudança estrutural solicitada e inspecione o diff. Testes de saída não avaliam legibilidade nem escolha de algoritmo.

Copie o código inicial para diretório pessoal de prática. Python 3.13 é a base; execução no navegador não verificada.

[Código inicial](starter.py) · [Registro](exercise.json)

```python
def shipping_fee(total: int, member: bool) -> int:
    if total >= 100:
        return 0
    if member:
        return 0
    return 12
```

## Exemplos (argumentos posicionais)

| Argumentos (JSON) | Esperado (JSON) |
| --- | --- |
| `[99,false]` | `12` |
| `[100,false]` | `0` |

## Dicas progressivas

<details>
<summary>Dica 1</summary>

Escreva casos de limite antes de editar.

</details>

<details>
<summary>Dica 2</summary>

Identifique dois ramos com mesmo retorno.

</details>

<details>
<summary>Dica 3</summary>

Combine condições com or e mantenha taxa alternativa.

</details>

## Referência e explicação

<details>
<summary>Revelar após tentativa</summary>

[Solução de referência](solution.py)

As duas condições de gratuidade formam OR inclusivo. Consolidá-las preserva saída e evidencia regra de negócio.

- Tempo: O(1)
- Espaço auxiliar: O(1)

Complexidade usa modelo de custo fixo para inteiros limitados e rótulos de comprimento limitado; n é tamanho da entrada, m tamanho da segunda, k valores distintos, d dígitos decimais, e expoente, conforme aplicável. Armazenamento da saída é excluído do espaço auxiliar. Tempos com hash são esperados, não limites de pior caso.

</details>

## Validação

Confira suas próprias chamadas manualmente com os casos declarados e adicione pelo menos dois casos de borda. O comando a seguir na raiz testa apenas referências e implementações incorretas conhecidas, não seu arquivo pessoal. Respostas públicas são visíveis; não há correção por IA.

```bash
python -m unittest discover -s tests -p "test_problem_solving_expansion.py"
```

[Fixture de teste](test_solution.py) · [Voltar à aula](../../../problem-solving-and-live-coding/14-refactoring-challenges/README.pt-BR.md) · [Índice de exercícios](../../README.pt-BR.md)
