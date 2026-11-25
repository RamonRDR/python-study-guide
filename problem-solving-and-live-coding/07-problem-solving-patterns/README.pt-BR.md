# Padrões de resolução de problemas

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../06-sorting-algorithms/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:top -->

**Pré-requisitos:** [Dicionários](../../collections/04-dictionaries-keys-and-values/README.pt-BR.md) · [Sets](../../collections/05-sets-and-unique-values/README.pt-BR.md) · [Complexidade](../../problem-solving-and-live-coding/03-algorithmic-complexity/README.pt-BR.md)

## Objetivo

Reconhecer padrões reutilizáveis e escolhê-los conforme o contrato (40–55 minutos).

## 1. Acumulador e mapa de frequências

Acumulador resume valores processados em uma variável (por exemplo soma). Mapa de frequências guarda contagens por chave distinta. Para ["a", "b", "a"], atualize dicionário com `counts.get(item, 0) + 1`; resultado {"a": 2, "b": 1}. Contagens crescem durante a varredura; lista vazia gera dicionário vazio. Tempo esperado O(n) sob hashing normal e armazenamento O(k) para k chaves distintas (a saída exigida neste exemplo). Para pertinência apenas, set pode bastar. Não use set para contar ocorrências, pois elimina duplicidades.

## 2. Dois ponteiros

Para lista crescente ordenada de inteiros, determine se dois **índices diferentes** somam um alvo. Inicie left em 0 e right em len(values)-1. Se a soma for pequena, mova left para a direita; se grande, mova right para a esquerda; igualdade é sucesso. Pare quando left >= right. A ordenação justifica descartar uma fronteira: se menor mais maior é pequeno, esse menor não pode formar par com nenhum valor restante. [1, 3, 6, 8], alvo 9, tem sucesso em 1+8. [4], alvo 8, falha. O(n) de tempo e O(1) de espaço auxiliar, assumindo ordenação sem validá-la.

## 3. Janela deslizante fixa

Para obter soma máxima de k inteiros consecutivos (1 <= k <= len(values)), some os primeiros k valores uma vez; a cada movimento, subtraia o valor que sai e adicione o que entra. Guarde a melhor soma. Para [4, -1, 3, 2], k=2, somas são 3, 2, 5; resultado 5. Inicie melhor com a primeira soma, não zero, pois todos os valores podem ser negativos. A implementação compartilhada calcula a primeira soma com loop, sem fatia; O(n) de tempo e O(1) de espaço auxiliar. O exemplo exige k inteiro exato e gera TypeError para tipo errado ou ValueError para tamanho fora do intervalo permitido. Janela fixa não é subconjunto arbitrário; a aula também não afirma que regras de janela variável funcionam com negativos.

## Prática

Rastreie cada padrão com os exemplos acima. Antes de abrir o [exemplo compartilhado](examples/patterns.py), implemente mapa de frequências para lista de rótulos; teste duplicidades e entrada vazia. Tente um par ausente e um par de dois valores duplicados; teste janela com todos negativos e k igual ao tamanho. Explique por que força bruta pode ser uma referência de correção antes de otimizar.

**Referência rápida:** acumulador para resumos; mapa para contagens; dois ponteiros quando ordenação permite eliminação; janela fixa para intervalos adjacentes.

Execute a partir do diretório da aula (Python 3.13 como base):

```bash
python examples/patterns.py
```

<!-- chapter-navigation:bottom -->
[← Anterior](../06-sorting-algorithms/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
