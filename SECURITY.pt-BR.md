<div align="center">

# Política de Segurança

[🇺🇸 English](SECURITY.md) · [🇧🇷 Português](SECURITY.pt-BR.md) · [🇪🇸 Español](SECURITY.es.md)

</div>

## Conteúdo com suporte

O Python Study Guide é um repositório educacional, não um serviço implantado. Correções de segurança são aplicadas à branch `main` atual e, quando existirem versões publicadas, à versão mais recente mantida sempre que for viável.

Commits históricos, branches excluídas, forks, materiais copiados e ferramentas externas sem suporte não são mantidos por este projeto.

## Relate vulnerabilidades de forma privada

Não abra uma issue pública para uma vulnerabilidade que possa expor usuários, credenciais, informações privadas, permissões do repositório ou a integridade da cadeia de fornecimento.

Quando a aba **Security** do repositório apresentar a opção **Report a vulnerability**, utilize-a para enviar o relato de forma privada pelo GitHub.

Caso o relato privado de vulnerabilidades não esteja disponível, utilize o formulário [**Private contact request**](https://github.com/RamonRDR/python-study-guide/issues/new?template=private-contact-request.yml). Esse formulário serve apenas para estabelecer um canal privado. **Não** inclua na solicitação pública detalhes da vulnerabilidade, segredos afetados, passos de exploração, nomes, capturas de tela ou outras informações sensíveis.

Inclua apenas no relato privado final as informações necessárias para compreender o problema:

- arquivo, workflow, orientação de dependência ou recurso do repositório afetado;
- impacto potencial;
- passos seguros de reprodução ou uma prova de conceito mínima;
- versões, commits ou ambientes afetados;
- mitigação sugerida, quando disponível;
- informação sobre qualquer divulgação pública já realizada.

Não inclua credenciais reais, tokens, URLs privadas, dados pessoais, dados de empregadores, código proprietário ou informações obtidas sem autorização.

## O que pertence a um relato de segurança

Exemplos:

- workflow ou configuração que possa permitir execução de código não autorizada ou uso indevido de privilégios;
- instruções que exponham credenciais ou incentivem práticas inseguras com segredos;
- arquivos maliciosos ou comprometidos apresentados como conteúdo confiável do projeto;
- recomendação de dependência com impacto de segurança conhecido, relevante e reproduzível;
- vulnerabilidade em código mantido pelo projeto que gere risco de segurança realista.

## O que não é uma vulnerabilidade de segurança

Utilize os templates normais de issue para:

- explicações ou traduções incorretas;
- links quebrados ou problemas de formatação;
- erros comuns de Python sem impacto de segurança;
- dúvidas sobre o material de aprendizagem;
- vulnerabilidades em produtos externos ou projetos pessoais não relacionados;
- preocupações hipotéticas sem caminho plausível de ataque ou componente afetado do projeto.

## Processo de resposta

Este projeto é mantido em regime de melhor esforço e não oferece um acordo garantido de nível de serviço.

O mantenedor pretende:

1. confirmar o recebimento de um relato válido em até sete dias corridos;
2. verificar o escopo e a gravidade;
3. coordenar uma correção e um plano de divulgação quando necessário;
4. creditar quem relatou, quando solicitado e seguro;
5. publicar informações relevantes de remediação depois que pessoas afetadas puderem se proteger.

Conceda um prazo razoável para investigação antes da divulgação pública. O mantenedor poderá contatar o GitHub, mantenedores de pacotes ou outras partes responsáveis quando houver necessidade de coordenação.

## Expectativas para pesquisa segura

Pesquisas de segurança devem ser realizadas de boa-fé e em ambientes autorizados. Não:

- acesse, altere ou retenha dados que não pertençam a você;
- interrompa serviços ou prejudique outras pessoas;
- utilize engenharia social, roubo de credenciais ou testes destrutivos;
- explore uma descoberta além do necessário para demonstrar o impacto;
- exija pagamento, emprego ou favores como condição para não realizar uma divulgação prejudicial.

Este projeto não mantém atualmente um programa de recompensa por vulnerabilidades nem promete compensação financeira.
