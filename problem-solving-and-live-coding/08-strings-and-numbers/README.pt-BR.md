# Desafios de strings e números

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../07-problem-solving-patterns/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../09-collections/README.pt-BR.md)
<!-- /chapter-navigation:top -->

Revise pertinência literal de caracteres, índices, divisão inteira e resto. No palíndromo médio, reutilize dois ponteiros comparando posições simétricas em vez de soma de par.

Leia contrato e aulas de pré-requisitos vinculadas, preveja resultados, tente o inicial em arquivo pessoal e verifique limites. Abra dicas progressivamente; compare referência só após tentar. Não há executor no navegador.

### Janela variável com últimas posições

Janela fixa tem comprimento constante; variável pode diminuir ou crescer conforme restrição. Para caracteres únicos, mantenha fronteira esquerda inclusiva e percorra direita um caractere por vez. Dicionário guarda último índice de cada caractere. Se esse índice for pelo menos left, a ocorrência antiga deve sair: mova left para índice mais um. Senão mantenha left. Comprimento válido é right - left + 1. Guarde o melhor. Em "abba", após segundo b a janela começa no índice 2; no a final, índice anterior 0 está fora, portanto não mova left para trás. Máximo 2. Sob hashing usual, tempo linear esperado e espaço proporcional a caracteres distintos. Regra específica de unicidade, não universal para janelas variáveis.

## Desafios disponíveis

- [Contador de vogais](../../exercises/problem-solving/vowel-counter/README.pt-BR.md) · Fácil · 10 min
- [Contador de dígitos ASCII](../../exercises/problem-solving/ascii-digit-counter/README.pt-BR.md) · Fácil · 10 min
- [Soma dos dígitos](../../exercises/problem-solving/sum-digits/README.pt-BR.md) · Fácil · 12 min
- [Palíndromo literal](../../exercises/problem-solving/literal-palindrome/README.pt-BR.md) · Média · 18 min

- [Maior substring sem repetição](../../exercises/problem-solving/longest-distinct-substring/README.pt-BR.md) · Difícil · 35 min

<!-- chapter-navigation:bottom -->
[← Anterior](../07-problem-solving-patterns/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../09-collections/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
