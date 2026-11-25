# Desafios de funções e recursividade

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../09-collections/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../11-searching-and-sorting/README.pt-BR.md)
<!-- /chapter-navigation:top -->

Revise parâmetros, retornos e casos base recursivos. Fatorial multiplica inteiros positivos até n; potência inteira multiplica a mesma base repetidamente. Zero tem resultado base explicitamente definido como um em ambas tarefas.

Leia contrato e aulas de pré-requisitos vinculadas, preveja resultados, tente o inicial em arquivo pessoal e verifique limites. Abra dicas progressivamente; compare referência só após tentar. Não há executor no navegador.

### Percurso recursivo de listas aninhadas

Lista aninhada é hierarquia finita: elemento é inteiro folha ou outra lista. Na auxiliar recursiva, percorra elementos; acrescente inteiro em resultado compartilhado ou visite lista recursivamente antes de continuar próximo elemento. Lista vazia retorna naturalmente após zero iterações. Use isinstance(item, list) para distinguir nós de lista; passe o mesmo acumulador à auxiliar ou defina auxiliar dentro da função para acrescentar à lista. Em [1, [2, [3]], 4], visite 1, desça em [2, [3]], acrescente 2 e 3, retorne e acrescente 4. Não acrescente lista inteira nem concatene cópias a cada nível. Assuma entrada finita sem ciclos e aninhamento limitado. Pilha cresce com profundidade, não quantidade de folhas.

## Desafios disponíveis

- [Limitar um valor](../../exercises/problem-solving/clamp-value/README.pt-BR.md) · Fácil · 10 min
- [Fatorial recursivo](../../exercises/problem-solving/recursive-factorial/README.pt-BR.md) · Média · 18 min
- [Potência inteira recursiva](../../exercises/problem-solving/recursive-power/README.pt-BR.md) · Média · 20 min

- [Achatar listas aninhadas](../../exercises/problem-solving/recursive-flatten/README.pt-BR.md) · Difícil · 35 min

<!-- chapter-navigation:bottom -->
[← Anterior](../09-collections/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../11-searching-and-sorting/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
