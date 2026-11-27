# ADR 0003: Execução e avaliação no navegador

[🇺🇸 English](0003-browser-execution.md) · [🇧🇷 Português](0003-browser-execution.pt-BR.md) · [🇪🇸 Español](0003-browser-execution.es.md)

Status: direção arquitetural aceita ([PR #87](https://github.com/RamonRDR/python-study-guide/pull/87)); execução no navegador permanece não verificada.

## Contexto

A prática interativa não deve exigir infraestrutura paga adicional. O guia inclui Python portátil e exemplos específicos de plataforma.

## Decisão

Usar Pyodide com runtime fixado e Web Worker no projeto separado do site, somente para exercícios com compatibilidade verificada. Manter execução local. Usar testes determinísticos, comparação objetiva de quizzes e rubricas de autoavaliação. Não implementar entrevistador ou correção semântica por IA. Por padrão, armazenar progresso localmente no navegador.

## Alternativas

Docker/Python remoto (rejeitado por custo e operação); avaliação por IA (fora do escopo); guia exclusivamente no navegador (rejeitado, pois material específico de plataforma deve continuar utilizável).

## Consequências

O projeto do site precisa validar inicialização do runtime, pacotes, diferenças de SO, isolamento, interrupção e limites de saída. Workers sozinhos não garantem isolamento seguro. Respostas públicas podem ser inspecionadas; progresso local pode ser perdido. Custos dependem dos limites da hospedagem existente; não se promete capacidade ilimitada.
