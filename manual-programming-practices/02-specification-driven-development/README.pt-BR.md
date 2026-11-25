# Desenvolvimento orientado por especificações

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../01-manual-coding-and-debugging/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../03-test-driven-development/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo

**Tempo estimado:** 40–60 minutos. Transforme um pedido ambíguo em contrato pequeno e testável antes de implementar. Desenvolvimento orientado por especificações (SDD) é usado aqui como fluxo leve, não como ferramenta universal ou formato obrigatório. A especificação descreve comportamento observável; implementação é uma forma de satisfazê-lo.

## 1. Do pedido aos requisitos

Pedido fictício: "Mostrar quantas páginas faltam em um livro." Pergunte: e se houver zero páginas, todas estiverem lidas ou a entrada for inválida? Para este exercício escolhemos explicitamente o contrato abaixo, não porque Python o exija.

| ID | Requisito |
| --- | --- |
| R1 | Função `remaining_pages(total_pages, pages_read)` retorna inteiro igual ao total menos lidas. |
| R2 | Aceita apenas valores do tipo int nativo (não bool nem subclasses de int); caso contrário lança TypeError. |
| R3 | Ambos inteiros não negativos e pages_read não pode exceder total_pages; caso contrário lança ValueError. |
| R4 | Sem prompts, impressão, arquivos ou rede dentro da função; quem chama cuida da exibição. |

Fora do escopo: banco, interface, porcentagens, progresso entre livros. Erros de tipo têm precedência sobre erros de valor se ambos ocorrerem. A restrição ao tipo exato é uma escolha deliberada do exercício: evita comportamento sobrescrito por subclasses. Sem conversão de strings ou floats.

## 2. Critérios de aceite

| ID | Entrada | Esperado |
| --- | --- | --- |
| AC1 | (20, 7) | 13 |
| AC2 | (20, 0); (20, 20); (0, 0) | 20; 0; 0 |
| AC3 | (-1, 0); (20, -1); (20, 21) | ValueError |
| AC4 | ("20", 7); (20, 7.0); (True, 0); (20, False) | TypeError |
| AC5 | chamada válida | sem saída em stdout ou stderr |

Critérios conectam requisitos a evidências observáveis. Testes podem codificá-los; testes sozinhos não comprovam todos os requisitos possíveis.

## 3. Plano, tarefas e decisão

Crie um `specification.md` na sua pasta de prática com contrato, exemplos e exclusões. Crie `plan.md`: validar tipos, validar intervalos, calcular resultado, verificar testes. Divida em tarefas com condições de conclusão. Não implemente tudo de uma vez; use os testes incrementais da próxima aula.

Uma ADR (registro de decisão de arquitetura) registra contexto, decisão e consequências. Exemplo: escolher função pura em vez de script interativo para reutilizar e testar o resultado sem I/O de terminal. Contrapartida: quem chama precisa exibir ou coletar dados. Registre em `adr-0001.md`; projetos maiores podem usar diretório. ADRs registram decisões significativas, não cada linha.

## 4. Controle de mudanças e prática independente

Imagine pedido para aceitar string "20". Não mude a implementação silenciosamente: esclareça a necessidade, atualize contrato e critérios, revise testes, implemente e revise. Por enquanto o contrato rejeita strings. Escreva especificação própria de outra função simples, com casos normais, de limite e inválidos; troque com alguém ou releia como revisor. Conseguem implementar sem adivinhar?

SDD responde **o quê e por quê**. TDD ajuda a verificar **como o comportamento é implementado** em pequenas etapas. Nenhum substitui entendimento, design ou revisão humana. Consulte a [especificação](../../docs/specs/learning-hub-foundation/specification.pt-BR.md) e o [índice de ADRs](../../docs/adr/README.pt-BR.md) do projeto como exemplo real maior, não formato obrigatório para todo programa pequeno.

**Referência rápida:** pedido → esclarecer → requisitos e exclusões → critérios → plano/tarefas → decisões → testes e implementação → revisão.

<!-- chapter-navigation:bottom -->
[← Anterior](../01-manual-coding-and-debugging/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../03-test-driven-development/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
