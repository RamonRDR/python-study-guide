<div align="center">

# Marcadores de Tarefas e Acompanhamento Técnico

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar ao índice da seção](../README.pt-BR.md) · [← Capítulo anterior: Nomes significativos](../03-meaningful-names/README.pt-BR.md)

Marcadores de tarefas são rótulos curtos inseridos em comentários para destacar trabalhos, restrições, riscos ou decisões temporárias. Eles podem tornar pendências visíveis, mas marcadores vagos ou abandonados rapidamente viram papel de parede.

> **Princípio orientador:** Um marcador deve informar ao próximo mantenedor o que precisa acontecer, por que isso importa e como saber quando o marcador poderá ser removido.

## Informações do capítulo

| Item | Detalhes |
|---|---|
| Nível | Iniciante a intermediário |
| Pré-requisitos | Recomenda-se o capítulo de comentários; familiaridade com issues e controle de versão ajuda |
| Tempo estimado de estudo | 45 a 65 minutos |
| Conceitos principais | `TODO`, `FIXME`, `NOTE`, `HACK`, `XXX`, referências de issues, condições de remoção, busca, revisão, marcadores obsoletos |

## Objetivos de aprendizagem

Ao concluir este capítulo, você deverá ser capaz de:

- explicar que marcadores de tarefas são convenções do projeto, não sintaxe do Python;
- diferenciar trabalho futuro, defeitos conhecidos, notas de contexto e soluções temporárias;
- escrever marcadores com ação, motivo, referência ou condição de remoção;
- decidir quando uma issue deve substituir ou acompanhar um marcador no código-fonte;
- evitar esconder testes falhando, problemas de segurança ou incidentes de produção atrás de comentários;
- pesquisar e revisar marcadores de forma consistente;
- reconhecer marcadores obsoletos, vagos, privados ou enganosos;
- definir uma pequena convenção que ferramentas e colaboradores possam seguir.

## 1. O que são marcadores de tarefas

O Python trata um marcador como um comentário comum. `TODO`, `FIXME` e palavras semelhantes não possuem significado especial para o interpretador.

```python
# TODO(#128): Remove the compatibility branch after every client uses API v2.
```

O valor vem de uma convenção compartilhada. Editores, ferramentas de busca, sistemas de revisão de código e colaboradores podem reconhecer o rótulo e direcionar atenção para ele.

Um marcador é útil quando a localização no código importa. Ele não deve substituir planejamento, testes, tratamento de incidentes ou um rastreador de issues.

## 2. Vocabulário comum dos marcadores

Os projetos utilizam esses rótulos de maneiras diferentes, portanto a convenção do repositório é a referência principal.

| Marcador | Significado típico | Intenção de exemplo |
|---|---|---|
| `TODO` | melhoria planejada ou trabalho incompleto | adicionar um recurso depois que uma dependência estiver pronta |
| `FIXME` | comportamento conhecido como incorreto ou inseguro | corrigir um defeito antes de uma versão |
| `NOTE` | contexto importante, não necessariamente uma tarefa | explicar uma representação ou restrição externa |
| `HACK` | solução alternativa deliberada e justificada | suportar temporariamente um formato legado |
| `XXX` | dúvida ou risco que exige atenção elevada | solicitar revisão de uma suposição incerta |

```python
# FIXME(#241): Reject duplicate invoice numbers before saving the batch.
```

```python
# NOTE: Amounts in this module are stored in cents.
```

```python
# HACK(#305): Keep the legacy padding until the old export format is retired.
```

```python
# XXX: Review this concurrency assumption before enabling parallel workers.
```

Esses significados são convenções, não leis universais. Um projeto pode proibir `XXX`, preferir `BUG` ou utilizar outro formato de referência.

## 3. A convenção utilizada neste guia

Este projeto recomenda o seguinte formato:

```text
# MARCADOR(referência): Ação clara ou contexto importante.
# Continuação opcional explicando o motivo ou a condição de remoção.
```

A referência é opcional para uma `NOTE` puramente explicativa, mas marcadores de trabalho normalmente devem apontar para um item durável, como uma issue.

Exemplos recomendados:

```python
# TODO(#128): Replace the temporary parser after escaped fields are supported.
# FIXME(#241): Preserve leading zeroes in account codes.
# NOTE: Amounts are represented in cents.
# HACK(#305): Keep legacy padding until the old export format is retired.
```

Utilize rótulos em letras maiúsculas para manter as buscas previsíveis. Escreva uma frase específica e coloque o marcador imediatamente acima do código relacionado.

## 4. Torne o marcador acionável

Um marcador fraco registra frustração, mas não define uma tarefa:

```python
# TODO: improve this
```

Um marcador útil responde a várias perguntas:

1. O que deve mudar?
2. Por que a mudança não está sendo feita agora?
3. Qual issue ou decisão acompanha o trabalho?
4. Qual condição permite remover o marcador?
5. Existe uma versão, prazo ou dependência que altera a urgência?

```python
# TODO(#128): Replace the temporary CSV parser after the vendor publishes
# escaped-field support. Remove this branch when issue #128 is closed.
```

Nem todo marcador precisa conter todos os campos. Quanto maior o custo ou o risco da pendência, mais contexto ela merece.

## 5. Prefira referências duráveis à propriedade pessoal

O nome de uma pessoa pode ficar obsoleto quando funções e equipes mudam. Uma issue, ticket ou decisão documentada é mais fácil de acompanhar.

Fraco:

```python
# TODO(Ramon): revisit later
```

Mais forte:

```python
# TODO(#128): Add pagination after the API contract defines the cursor format.
```

A responsabilidade ainda pode ser definida no rastreador de issues. O comentário no código deve continuar útil mesmo quando o autor original não estiver disponível.

Evite endereços de e-mail, links de conversas privadas, tickets inacessíveis ou informações que identifiquem clientes em repositórios públicos.

## 6. `TODO`: trabalho planejado, não possibilidades ilimitadas

Utilize `TODO` para uma melhoria concreta que foi adiada intencionalmente.

Bons usos incluem:

- uma dependência ainda não publicou a API necessária;
- uma migração está em andamento;
- uma otimização não crítica possui critério de aceitação rastreado;
- um ramo temporário deverá ser removido após uma implantação.

Não adicione um `TODO` para cada recurso imaginado. Possibilidades sem prioridade pertencem a notas de planejamento, discussões ou issues.

Um `TODO` sem referência pode ser aceitável em um exercício pequeno, mas código de produção se beneficia de acompanhamento durável.

## 7. `FIXME`: um defeito conhecido exige tratamento mais forte

`FIXME` sinaliza que o comportamento é conhecido como incorreto, enganoso, incompleto ou inseguro.

```python
# FIXME(#241): Preserve leading zeroes in account codes.
```

Um `FIXME` não neutraliza o defeito. Dependendo da gravidade, o código também poderá precisar de:

- um teste de regressão ou atualmente falhando;
- uma issue com prioridade e impacto;
- bloqueio de versão;
- feature flag;
- alerta ou incidente;
- remoção imediata da produção.

Não utilize um comentário para silenciar evidências:

```python
# FIXME: the test is failing, so skip it
```

Um teste ignorado deve explicar o motivo rastreado, a condição esperada de recuperação e o risco. Defeitos críticos não devem esperar educadamente dentro de um comentário.

## 8. `NOTE`: contexto em vez de trabalho inacabado

Uma `NOTE` preserva informações que um leitor futuro poderia não perceber.

```python
# NOTE: The upstream service returns dates in UTC.
created_at = parse_utc_timestamp(payload["created_at"])
```

Utilize-a para contratos externos, unidades, regras de compatibilidade ou decisões que não sejam evidentes no código.

Não rotule contexto como tarefa:

```python
# TODO: Dates come from the upstream service in UTC.
```

Quando nenhuma ação for necessária, `NOTE` comunica a intenção com mais precisão do que `TODO`.

Um comentário explicativo comum poderá ser mais claro quando o rótulo `NOTE` não acrescentar valor para busca ou revisão.

## 9. `HACK`: documente a solução temporária e sua saída

Uma solução alternativa pode representar engenharia responsável quando uma restrição externa impede a solução ideal. O perigo está em permitir que código temporário se torne permanente sem explicação.

```python
# HACK(#305): Legacy exports pad account codes to eight characters.
# Remove this normalization after the pre-2024 export format is retired.
account_code = raw_account_code.lstrip("0")
```

Um `HACK` útil informa:

- qual restrição obrigou a solução alternativa;
- qual comportamento depende dela;
- a referência de acompanhamento;
- a condição de remoção;
- qualquer risco introduzido.

Evite:

```python
# HACK: weird fix
account_code = raw_account_code.lstrip("0")
```

`HACK` não é autorização para código descuidado. A implementação ainda deve ser testada, limitada e compreensível.

## 10. `XXX` e marcadores personalizados

`XXX` frequentemente significa “isto merece atenção incomum”, mas seu significado varia bastante.

```python
# XXX(#411): Confirm whether this cache may be shared between tenants.
```

Utilize-o apenas quando o projeto definir sua interpretação. Caso contrário, escolha algo mais preciso, como `FIXME`, `SECURITY`, `PERF` ou `DEPRECATED`.

Marcadores personalizados podem ser úteis quando correspondem a um processo real de revisão. Rótulos demais criam um dialeto privado que ferramentas e colaboradores não conseguem prever.

## 11. Marcadores e rastreadores de issues resolvem problemas diferentes

Um marcador no código-fonte responde:

> Em qual ponto do código esta preocupação se aplica?

Uma issue responde:

> Como o trabalho será priorizado, discutido, atribuído, testado e concluído?

Para um trabalho local e pequeno, o marcador poderá ser suficiente. Para atividades envolvendo vários arquivos, equipes, versões, riscos ou decisões, crie uma issue e conecte o marcador a ela.

Feche o ciclo:

1. atualize ou encerre a issue;
2. remova ou revise o marcador;
3. atualize testes e documentação;
4. confirme que não restaram referências obsoletas.

## 12. Datas são contexto complementar, não estratégia de saída

Uma data pode ajudar a explicar o momento, mas “remover depois” e “verificar no próximo mês” são condições fracas.

Prefira um evento observável:

- depois que todos os clientes migrarem para a API v2;
- quando a issue `#128` for encerrada;
- depois da alteração da versão mínima suportada do Python;
- quando testes de regressão cobrirem a substituição;
- antes de uma versão nomeada.

Uma condição de remoção torna o marcador verificável durante a revisão.

## 13. Não coloque segredos ou dados sensíveis em marcadores

Comentários ficam armazenados no histórico do Git e podem continuar recuperáveis depois da exclusão.

Nunca inclua:

- senhas, tokens, chaves de API ou credenciais;
- nomes de clientes ou identificadores privados;
- detalhes confidenciais de incidentes;
- URLs internas que não deveriam ser públicas;
- informações pessoais de contato.

Ruim:

```python
# SECURITY: Temporary token for production: abc123
```

Utilize o processo privado de segurança ou incidentes do projeto. A rotação de uma credencial exposta é necessária mesmo que o comentário seja removido imediatamente.

## 14. Mantenha os marcadores próximos e restritos

Coloque o marcador imediatamente acima do menor bloco relevante.

```python
# TODO(#128): Replace the temporary parser.
```

Evite um marcador no início de um módulo extenso quando apenas um ramo estiver afetado. Um marcador distante pode ser interpretado incorretamente depois de uma refatoração.

Quando a preocupação envolver vários módulos, o rastreador de issues deve manter a explicação ampla enquanto marcadores locais identificam os pontos exatos do código.

## 15. Pesquise e revise marcadores

Uma busca simples no repositório pode revelar trabalho acumulado:

```bash
rg -n "#\s*(TODO|FIXME|NOTE|HACK|XXX)\b" .
```

Editores e a busca de código do GitHub também podem procurar os rótulos. Mantenha marcadores e pontuação consistentes para que ferramentas não ignorem variações.

Para uma análise consciente da sintaxe Python, utilize o módulo `tokenize` da biblioteca padrão. Ele diferencia comentários reais de textos semelhantes a marcadores dentro de strings.

```python
from io import StringIO
import tokenize


source = '''
message = "# TODO: this is text, not a comment"
# TODO(#128): Replace the temporary parser.
'''

for token in tokenize.generate_tokens(StringIO(source).readline):
    if token.type == tokenize.COMMENT:
        print(token.string)
```

O exemplo deste capítulo demonstra um pequeno scanner para uma convenção simples. Ele é educacional, não substitui um linter maduro nem um fluxo de gestão de issues.

## 16. Consistência permite automação

Um formato estável permite:

- destaque no editor;
- relatórios do repositório;
- regras de CI para marcadores proibidos;
- validação de referências de issues;
- verificações de versão;
- painéis de dívida técnica.

Consistente:

```python
# TODO(#128): Replace the temporary parser after escaped fields are supported.
# FIXME(#241): Preserve leading zeroes in account codes.
# NOTE: Amounts are represented in cents.
# HACK(#305): Keep legacy padding until the old export format is retired.
```

Mais difícil de pesquisar com confiança:

```python
# TODO-128 replace parser
# todo: maybe later
# FixMe(issue 241): zeros
```

A automação deve apoiar o discernimento, não incentivar números de issues sem significado ou comentários escritos apenas para satisfazer um padrão.

## 17. Exemplos deste repositório

| Arquivo | Objetivo |
|---|---|
| [`actionable_markers.py`](examples/actionable_markers.py) | Mostra marcadores com referências, contexto e condição de remoção |
| [`temporary_workaround.py`](examples/temporary_workaround.py) | Documenta uma solução limitada para um formato legado fictício |
| [`scan_markers.py`](examples/scan_markers.py) | Utiliza `tokenize` para localizar marcadores em comentários Python reais |

Execute um exemplo a partir da raiz do repositório:

```bash
python comments-and-documentation/04-task-markers/examples/actionable_markers.py
```

Em sistemas nos quais o comando é chamado `python3`:

```bash
python3 comments-and-documentation/04-task-markers/examples/actionable_markers.py
```

## 18. Exemplo prático de refatoração

Antes:

```python
def load_report(file_path):
    # TODO: make this better
    return file_path.read_text()
```

Depois:

```python
def load_report(file_path):
    # TODO(#512): Stream files larger than 50 MB to avoid loading them at once.
    # Remove this marker after the streaming reader is covered by regression tests.
    return file_path.read_text()
```

O marcador melhorado identifica a limitação, o impacto, a issue e a condição de conclusão. O código ainda poderá exigir redesenho imediato quando o comportamento atual for inseguro para entradas suportadas.

## 19. Erros comuns

### Escrever um marcador sem ação

“Melhorar isto” não define quando o trabalho estará concluído.

### Utilizar `TODO` para um defeito conhecido

Um defeito poderá exigir `FIXME`, teste e acompanhamento urgente.

### Tratar `NOTE` como dívida técnica

Uma nota poderá permanecer para sempre porque documenta uma restrição estável.

### Criar um marcador no lugar de uma issue

Trabalhos entre equipes ou críticos para uma versão precisam de priorização fora do código-fonte.

### Manter referência para uma issue encerrada

Quando o trabalho for concluído, remova ou atualize o marcador no código.

### Registrar apenas data ou nome de uma pessoa

Datas e responsáveis mudam. Prefira referências duráveis e condições de saída observáveis.

### Esconder risco atrás de `HACK`

Uma solução alternativa ainda precisa de testes, limites e revisão.

### Incluir informações privadas

O histórico do Git não é um caderno privado.

### Reformatar código não relacionado ao adicionar marcadores

Mantenha o pull request focado para que os revisores consigam avaliar a mudança real.

## 20. Exercício

Reescreva estes marcadores vagos ou incompletos usando a convenção recomendada no capítulo:

```python
# TODO: improve parser
```

```python
# TODO(Ramon): fix leading zeroes later
```

```python
# TODO: rates are fractions
```

```python
# HACK: temporary workaround
```

```python
# XXX: check tenant isolation
```

Para cada marcador, decida:

1. O rótulo está correto?
2. É necessária uma referência de issue?
3. A ação está clara?
4. O motivo ou risco foi documentado?
5. Existe uma condição observável de remoção?
6. A preocupação deveria bloquear a versão em vez de permanecer como comentário?

Depois, pesquise marcadores em um pequeno projeto de prática e classifique cada um como ativo, obsoleto, resolvido ou desnecessário.

## 21. Checklist de revisão

Antes de aceitar um marcador, verifique:

- [ ] o rótulo corresponde ao significado;
- [ ] a ação ou o contexto é específico;
- [ ] o marcador está próximo do código relevante;
- [ ] trabalhos rastreados possuem referência durável;
- [ ] trabalhos arriscados incluem impacto e urgência;
- [ ] trabalhos temporários incluem condição de remoção;
- [ ] não há dados secretos, pessoais ou confidenciais;
- [ ] o marcador não substitui um teste ou issue necessária;
- [ ] grafia e pontuação seguem a convenção do projeto;
- [ ] trabalhos concluídos removem ou atualizam o marcador.

## 22. Resumo para consulta rápida

| Necessidade | Abordagem recomendada |
|---|---|
| Melhoria concreta adiada | `TODO(referência): ação e condição` |
| Comportamento conhecido como incorreto | `FIXME(referência): defeito e impacto` mais o acompanhamento adequado |
| Contexto importante e estável | `NOTE: contexto` ou comentário explicativo comum |
| Solução temporária | `HACK(referência): motivo e condição de remoção` |
| Suposição incerta que exige muita atenção | `XXX` definido pelo projeto ou rótulo mais preciso |
| Planejamento entre arquivos | rastreador de issues, com marcadores locais onde a localização importa |
| Busca | rótulos consistentes, busca do editor, `rg` ou `tokenize` do Python |
| Trabalho concluído | remover ou atualizar tanto o marcador quanto o item de acompanhamento |

Marcadores de tarefas são úteis quando criam uma ponte entre o código e o acompanhamento responsável. Sem contexto e encerramento, essa ponte vira apenas um andaime decorativo.
