<div align="center">

# Desenvolvimento Assistido por IA

[🇺🇸 English](README.en.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

A inteligência artificial pode acelerar pesquisas, organização, explicações, traduções, programação e revisões. Ela também pode produzir informações incorretas, incompletas, desatualizadas ou inventadas usando uma linguagem confiante.

Por isso, este projeto utiliza a IA como ferramenta de apoio, não como autoridade final.

O princípio orientador é simples:

> Use a IA para ampliar sua capacidade de pensar, construir, verificar e aprender. Não a utilize para abandonar a responsabilidade pelo resultado.

## Objetivo deste documento

Esta página explica:

- como a IA apoia o Python Study Guide;
- como uma pessoa iniciante pode conversar com um assistente de IA;
- como fornecer um contexto útil;
- como escrever e refinar prompts;
- como pedir ensino, e não apenas respostas;
- como transformar uma conversa em um briefing de implementação;
- como enviar um briefing revisado ao Codex;
- como validar um trabalho assistido por IA;
- como proteger informações privadas e confidenciais.

Não é necessário ter experiência anterior com ferramentas de IA.

## Como a IA apoia este projeto

ChatGPT e Codex podem auxiliar em atividades como:

- planejamento da estrutura do repositório;
- explicação de conceitos de Python;
- pesquisa e verificação de informações técnicas;
- elaboração e revisão de conteúdo educacional;
- alinhamento da documentação em inglês, português brasileiro e espanhol;
- criação de exemplos e exercícios originais;
- identificação de inconsistências;
- revisão de pull requests;
- edição de arquivos e manutenção do repositório.

Suas funções são relacionadas, mas não idênticas.

### ChatGPT

O ChatGPT é útil para conversas, explicações, estudos, levantamento de ideias, comparações, elaboração de textos, traduções e transformação de uma ideia ainda vaga em um plano estruturado.

### Codex

O Codex é um agente de programação com IA que pode trabalhar a partir de um prompt ou especificação para inspecionar um repositório, editar arquivos, executar comandos e testes, revisar código e preparar alterações para revisão humana.

As interfaces e os recursos disponíveis podem mudar. O fluxo duradouro é mais importante do que qualquer botão específico:

```text
Compreender o problema
        ↓
Conversar e aprender
        ↓
Definir os requisitos
        ↓
Criar um briefing de implementação
        ↓
Pedir ao Codex que implemente
        ↓
Revisar arquivos, testes e explicações
        ↓
Abrir e revisar um pull request
        ↓
Fazer o merge somente após a validação
```

## Responsabilidade humana

A IA não elimina a responsabilidade humana.

Uma resposta clara ou convincente não está automaticamente correta. O mantenedor e o colaborador continuam responsáveis por:

- compreender o que está sendo enviado;
- verificar afirmações técnicas;
- confirmar informações importantes em fontes confiáveis;
- testar exemplos executáveis;
- revisar traduções;
- identificar suposições sem fundamento;
- proteger informações privadas;
- decidir se uma alteração está pronta para o merge.

Não envie conteúdo que você não consiga explicar, revisar ou defender.

## Pense antes de escrever o prompt

Um prompt útil muitas vezes começa antes de a mensagem ser digitada.

Tente responder a estas perguntas com suas próprias palavras:

1. O que estou tentando realizar?
2. O que eu já sei?
3. Onde estou com dificuldade?
4. Quais restrições precisam ser respeitadas?
5. Qual resultado seria útil?
6. Como saberei se o resultado está correto?

As respostas não precisam ser perfeitas. O objetivo é dar uma direção à conversa.

## Anatomia de um prompt útil

Um prompt pode ser organizado com seis elementos simples:

| Elemento | Pergunta que responde |
|---|---|
| Contexto | Em qual situação estamos trabalhando? |
| Objetivo | O que desejo alcançar? |
| Estado atual | O que já possuo ou compreendo? |
| Restrições | Quais regras ou limites devem ser seguidos? |
| Resultado esperado | Em qual formato a resposta deve ser apresentada? |
| Validação | Como o resultado deve ser verificado? |

Isso é um guia, não uma fórmula obrigatória. Uma dúvida pequena pode precisar de apenas uma frase. Uma alteração em um repositório pode exigir uma especificação detalhada.

### Prompt fraco

```text
Faça um programa em Python.
```

A solicitação é ampla demais. A IA precisa adivinhar o público, a finalidade, as entradas, a saída, as restrições e o estilo de ensino desejado.

### Prompt de aprendizagem melhor

```text
Estou começando a estudar Python e ainda não aprendi funções.

Quero criar um pequeno programa que receba três notas e calcule uma média.

Primeiro, explique quais conceitos básicos preciso conhecer. Depois, mostre
um exemplo simples e explique linha por linha.

Não entregue um projeto completo imediatamente. Ao final, proponha um
exercício semelhante para eu resolver sozinho e mostre a resposta apenas
depois da minha tentativa.
```

Esse prompt fornece contexto, objetivo, nível atual da pessoa, uma restrição pedagógica e o resultado esperado.

## Peça à IA para ajudar você a pensar

A IA pode atuar como tutora, e não como uma máquina de entregar respostas prontas.

Instruções úteis incluem:

```text
Não forneça a resposta completa ainda. Dê uma pista por vez.
```

```text
Explique por que minha solução falha, mas permita que eu tente corrigi-la.
```

```text
Faça perguntas para verificar se compreendi o conceito.
```

```text
Compare minha solução com outra abordagem e explique as vantagens e limitações.
```

```text
Diga quais partes do meu raciocínio estão corretas antes de explicar o erro.
```

```text
Depois da explicação, peça que eu resuma o conceito com minhas próprias palavras.
```

O objetivo não é tornar o aprendizado desnecessariamente difícil. É manter a pessoa mentalmente envolvida.

## Refine a conversa

Um bom prompt não precisa ser perfeito na primeira tentativa.

Um ciclo produtivo é:

```text
Perguntar
  ↓
Ler criticamente
  ↓
Identificar o que está ausente ou pouco claro
  ↓
Adicionar contexto ou restrições
  ↓
Pedir uma revisão
  ↓
Verificar o resultado
```

Exemplos de mensagens de acompanhamento úteis:

```text
Use um vocabulário mais simples e defina cada termo técnico.
```

```text
Seu exemplo introduziu listas, mas ainda não estudei esse assunto. Reescreva
usando apenas variáveis, input, conversão, operações aritméticas e print.
```

```text
Mostre a fonte da afirmação técnica sobre o comportamento do Python.
```

```text
Crie dois casos de teste, incluindo um que possa revelar um erro comum.
```

Refinar não significa falhar. É parte da comunicação de requisitos.

## Do ChatGPT para o Codex

O ChatGPT pode ajudar a transformar uma ideia em um briefing de implementação revisado. O Codex pode então trabalhar a partir desse briefing dentro de um repositório.

Antes de enviar a tarefa ao Codex, confirme se o briefing descreve:

- o contexto do repositório;
- a tarefa;
- os arquivos ou a área que podem ser alterados;
- os requisitos;
- o que não deve ser feito;
- os critérios de aceitação;
- as etapas de validação;
- as regras de idioma e documentação.

### Exemplo de briefing de implementação para o Codex

```text
Contexto do repositório

Este é um repositório educacional multilíngue de Python para iniciantes.
Nomes de diretórios, arquivos, identificadores, comentários do código,
branches e mensagens de commit devem permanecer em inglês.
A documentação é mantida em inglês, português brasileiro e espanhol.

Tarefa

Crie um exemplo iniciante que calcule a média de três notas.

Requisitos

- Utilize apenas recursos nativos do Python.
- Mantenha o exemplo pequeno e executável.
- Utilize nomes de variáveis descritivos em inglês.
- Explique os conceitos necessários antes do exemplo.
- Crie documentação conceitualmente alinhada nos três idiomas suportados.
- Utilize apenas dados originais, fictícios e não confidenciais.
- Não modifique arquivos sem relação com a tarefa.

Critérios de aceitação

- O exemplo executa sem erros.
- A média é calculada corretamente.
- A explicação é adequada para alguém que ainda não estudou funções.
- As três versões de idioma preservam o mesmo significado e objetivo de aprendizagem.
- Links e caminhos relativos funcionam.

Validação

- Execute o exemplo com pelo menos dois casos de teste.
- Revise todos os arquivos alterados.
- Informe o que foi testado e declare qualquer item que não pôde ser verificado.
- Envie o trabalho por meio de uma branch e de um pull request focados.
```

Um prompt detalhado melhora a direção. Ele não garante que o resultado esteja correto.

## Revise o trabalho gerado por IA

Revise o resultado como se tivesse sido entregue por um colaborador competente, porém sujeito a erros.

### Revisão da documentação

Confirme se:

- a explicação está tecnicamente correta;
- afirmações importantes possuem fontes adequadas;
- o texto corresponde ao nível de aprendizagem pretendido;
- os exemplos são originais;
- os três idiomas permanecem conceitualmente alinhados;
- os links funcionam;
- incertezas são informadas em vez de escondidas.

### Revisão do código

Confirme se:

- o código executa conforme descrito;
- casos esperados e casos de borda foram considerados;
- os nomes são claros;
- o exemplo não introduz conceitos desnecessários;
- os comentários explicam motivos, e não operações óbvias;
- as dependências são justificadas;
- não existem segredos ou dados privados.

### Revisão do repositório

Confirme se:

- somente arquivos relevantes foram alterados;
- a branch foi criada a partir da versão atual da `main`;
- o pull request possui um único objetivo claro;
- comentários de revisões automáticas foram considerados;
- conversas foram resolvidas somente depois de o problema correspondente ser tratado.

## Privacidade e informações confidenciais

Nunca forneça a um sistema de IA uma informação que você não está autorizado a compartilhar com outra pessoa ou serviço externo.

Remova ou evite:

- nomes reais quando forem desnecessários;
- endereços de e-mail e números de telefone;
- senhas, chaves de API, tokens, cookies e credenciais;
- dados financeiros, médicos, profissionais ou de clientes;
- URLs privadas, nomes de hosts, caminhos e detalhes de infraestrutura;
- documentos internos e código-fonte privado;
- regras de negócio e fluxos confidenciais;
- detalhes identificáveis de projetos pessoais, familiares, profissionais ou de clientes.

Uma anonimização superficial pode não ser suficiente. A combinação de datas, cargos, nomes de sistemas, estruturas de contas, regras incomuns e detalhes do fluxo ainda pode revelar a origem.

Para materiais educacionais, crie um novo cenário fictício desde o início.

## Controles de dados e melhoria dos modelos

A escolha do plano, os controles de dados e a melhoria dos modelos são assuntos diferentes.

A OpenAI oferece Controles de Dados que permitem ao usuário escolher se conversas elegíveis do ChatGPT podem ajudar a melhorar seus modelos. As configurações e políticas disponíveis podem variar conforme o produto, o tipo de conta e o momento.

Independentemente da configuração selecionada, não envie informações confidenciais ou não autorizadas.

Consulte a documentação oficial atual antes de tomar decisões sobre privacidade ou uso de dados.

## Planos, disponibilidade e limites

A OpenAI oferece planos gratuitos e pagos do ChatGPT. A disponibilidade do Codex, as interfaces compatíveis, os recursos, os limites de uso e as opções de créditos podem variar conforme o plano e mudar ao longo do tempo.

Um plano pago pode ser útil quando seus recursos e limites atuais correspondem às necessidades de estudo ou desenvolvimento da pessoa. O pagamento não substitui compreensão, verificação, testes ou uso responsável.

Este repositório não publica preços nem limites fixos de planos. Consulte a documentação oficial atual da OpenAI antes de escolher um plano.

## Contribuições assistidas por IA

Contribuições assistidas por IA são bem-vindas quando o colaborador continua responsável pelo resultado.

O colaborador deve:

- compreender o conteúdo enviado;
- revisar e verificar o material;
- executar exemplos e testes relevantes;
- verificar todas as versões de idioma afetadas;
- informar incertezas;
- remover materiais privados ou proprietários;
- respeitar licenças e políticas do repositório.

Não envie conteúdo gerado automaticamente sem uma revisão humana significativa.

## Independência e marcas

ChatGPT, Codex e OpenAI são marcas da OpenAI.

O Python Study Guide é um projeto educacional independente. Ele não possui afiliação, patrocínio ou endosso da OpenAI.

As referências aos produtos da OpenAI são descritivas. A identidade própria do projeto deve permanecer como elemento principal.

## Recursos oficiais

Como capacidades e políticas dos produtos podem mudar, consulte sempre as páginas oficiais atuais:

- [Visão geral das capacidades do ChatGPT](https://help.openai.com/pt-br/articles/9260256-vis%C3%A3o-geral-das-capacidades-do-chatgpt)
- [Práticas recomendadas de engenharia de prompt para o ChatGPT](https://help.openai.com/pt-br/articles/10032626-prompt-engineering-best-practices-for-chatgpt)
- [Usando o Codex com seu plano ChatGPT](https://help.openai.com/pt-br/articles/11369540-using-codex-with-your-chatgpt-plan)
- [Instruções personalizadas com AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Perguntas frequentes sobre Controles de Dados](https://help.openai.com/pt-br/articles/7730893-data-controls-faq)
- [Diretrizes de marca da OpenAI](https://openai.com/pt-BR/brand/)

## Princípio final

Um fluxo útil com IA não termina quando uma resposta aparece. Ele termina quando a pessoa compreende o resultado, verifica, melhora e consegue assumir responsabilidade por ele.
