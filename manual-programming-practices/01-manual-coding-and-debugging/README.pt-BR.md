# Programação manual e depuração

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Anterior](../../practical-projects/08-simulated-automation-flow/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../02-specification-driven-development/README.pt-BR.md)
<!-- /chapter-navigation:top -->

## Objetivo e pré-requisitos

**Nível:** iniciante após o currículo central. **Tempo estimado:** 35–50 minutos. Revise [funções](../../functions/README.pt-BR.md), [exceções](../../errors-files-and-modules/01-try-except-else-finally/README.pt-BR.md) e [Git básico](../../getting-started/06-git-and-version-control/README.pt-BR.md) se necessário. Aprenda a reproduzir, diagnosticar e corrigir um erro pequeno por conta própria. Use pasta de prática separada, não os arquivos-fonte do repositório.

## 1. Pense antes de digitar

Anote entrada, saída e um pequeno exemplo à mão. Um controle de leitura deve informar páginas restantes: total 20, lidas 7, esperado 13. Preveja antes de executar. Divida em etapas, escreva o código mais simples, execute, observe e explique. Registre tentativas; uma tentativa que falhou é evidência útil.

## 2. Reproduza um defeito

Crie `practice.py` e digite este exemplo intencionalmente incorreto (não é uma solução executável publicada):

```python
def remaining_pages(total_pages, pages_read):
    return total_pages + pages_read

print(remaining_pages(20, 7))
```

Execute `python practice.py` com o interpretador verificado. O esperado é 13; o código imprime 27. É erro de lógica: a execução terminou, mas o comportamento está errado. Inspecione operandos, acompanhe a expressão no papel e corrija o operador por conta própria. Tente (20, 0) e (20, 20). Um caso aprovado não prova correção.

## 3. Leia erros de baixo para cima

Erro de sintaxe impede análise; exceção em execução interrompe o fluxo; erro de lógica pode produzir saída plausível, porém errada. Em arquivo descartável, altere a chamada para `remaining_pages(20, "7")` após corrigir o operador. Leia o traceback: comece pelo tipo e mensagem da exceção no final, depois encontre o frame relevante e a linha de código. Mensagens e números de linha dependem do interpretador e arquivo. Confira valores e tipos em vez de suprimir a exceção.

Use `print(repr(value), type(value).__name__)` com um nome de variável real para inspecionar um valor; remova diagnósticos temporários após corrigir. Opcionalmente, coloque um breakpoint no VS Code, use o depurador Python e inspecione variáveis locais. O depurador ajuda a investigar; não decide o comportamento desejado.

## 4. Consulte documentação e teste uma hipótese

Leia o [tutorial Python sobre erros e exceções](https://docs.python.org/3.13/tutorial/errors.html) ou use `help()` para um objeto conhecido. Identifique primeiro a pergunta exata. Mude uma coisa por vez; compare esperado e obtido. Se travar, procure dica ou explicação, não resposta pronta. Tente novamente sem olhar a referência. Nunca envie código privado, credenciais ou dados a serviço público.

## 5. Prática independente

- Preveja resultados para (0, 0), (20, 0), (20, 20).
- Identifique o comportamento ausente para valores negativos, excessivos e não inteiros; não invente a regra. Registre perguntas para a próxima aula.
- Em arquivo separado, reproduza erro de sintaxe (por exemplo, parêntese sem fechamento) e corrija.
- Explique a diferença entre erros de sintaxe, execução e lógica sem ler a resposta.

**Referência rápida:** reproduzir, prever, inspecionar, formular hipótese, mudar uma coisa, executar novamente, testar limites, explicar. A seguir, especifique o significado do comportamento válido.

<!-- chapter-navigation:bottom -->
[← Anterior](../../practical-projects/08-simulated-automation-flow/README.pt-BR.md) · [Índice do módulo](../README.pt-BR.md) · [Próximo →](../02-specification-driven-development/README.pt-BR.md)
<!-- /chapter-navigation:bottom -->
