# Live coding cronometrado

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../15-mixed-challenges/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../technical-interview-preparation/01-understanding-technical-interviews/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Preparação antes de começar

Revise [fundamentos](../01-problem-solving-fundamentals/README.pt-BR.md), [casos de borda](../02-constraints-and-edge-cases/README.pt-BR.md), [complexidade](../03-algorithmic-complexity/README.pt-BR.md) e [padrões](../07-problem-solving-patterns/README.pt-BR.md). Use cronômetro pessoal e Python 3.13 local; não há executor no navegador. Pratique um exercício por vez. Leia enunciado e ferramentas permitidas; sem IA, dicas ou soluções na primeira tentativa. Pode rodar seu código e testes. Não sacrifique clareza ou correção por velocidade.

## Dois roteiros de prática

| Atividade | 10 min | 20 min |
| --- | ---: | ---: |
| Ler e esclarecer contrato, exemplos | 2 | 3 |
| Planejar e rastrear | 2 | 4 |
| Implementar | 4 | 9 |
| Testar e explicar | 2 | 4 |

Se travar, declare hipótese necessária ou escreva menor passo testável. No limite registre estado (não iniciado, parcial, completo), tempo e falhas conhecidas; pare cronômetro. Depois finalize sem pressão, revele dicas/referência e tente novamente mais tarde. Tempo autorrelatado, não nota nem medida de prontidão profissional.

## Sequências contíguas

Contar todos elegíveis difere de contar sequência contígua. Guarde comprimento atual e máximo. Estenda contador atual ao qualificar; zere na falha. Para condição >= 2 e [2, 3, 0, 2], comprimentos são 1, 2, 0, 1; melhor 2. Atual descreve sufixo elegível, não total. Combina acumulador e condição com variáveis auxiliares constantes.

## Autoavaliação após tentativa

Registre um ponto por critério atendido: contrato/casos de borda claros, plano justificado, comportamento correto nos seus casos, implementação legível e explicação de tempo/espaço. Use 0–5 apenas para feedback pessoal; sem avaliação automática de explicações ou tempo. Registre melhoria e próximo passo.

## Desafios disponíveis

- [Cronometrado: contar pelo limite](../../exercises/problem-solving/timed-threshold-count/README.pt-BR.md) · Fácil · 10 min
- [Cronometrado: maior sequência elegível](../../exercises/problem-solving/timed-longest-streak/README.pt-BR.md) · Média · 20 min

<!-- chapter-navigation:bottom -->
[← Anterior](../15-mixed-challenges/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../../technical-interview-preparation/01-understanding-technical-interviews/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
