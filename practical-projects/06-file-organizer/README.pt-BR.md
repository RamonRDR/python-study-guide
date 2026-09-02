<div align="center">

# Projeto 06 · Organizador de Arquivos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Projetos Práticos](../README.pt-BR.md)

> **Fase 10 · Projetos Práticos**

Este projeto organiza arquivos filhos diretos em pastas por categoria, mantendo descoberta, planejamento, tratamento de colisões e mutação do filesystem explícitos e testáveis.

## Objetivos de aprendizagem

Ao concluir este projeto, você deverá ser capaz de:

- descobrir arquivos diretos com `pathlib` sem travessia recursiva;
- classificar nomes de arquivos de forma determinística com regras de sufixo sem diferenciar maiúsculas e minúsculas;
- modelar mudanças planejadas no filesystem com dataclasses imutáveis;
- separar uma fase de planejamento sem mutação de uma fase de execução com efeitos colaterais;
- detectar colisões de destino exatas e sem diferenciação de caixa;
- escolher políticas de colisão explícitas em vez de sobrescrever dados silenciosamente;
- tratar symlinks e arquivos especiais como fronteiras do filesystem;
- raciocinar sobre corridas time-of-check/time-of-use;
- comparar objetos do filesystem pela identidade `(device, inode)`;
- ancorar diretórios com file descriptors no Linux;
- fixar origens sem bloquear diante de substituições tardias por FIFO;
- usar semântica atômica no-replace na fronteira final de commit do nome exato;
- distinguir checagens lógicas por `casefold()` de garantias atômicas de nome exato;
- preservar estado incerto em vez de apagar entradas cegamente durante recuperação;
- testar código de filesystem com segurança usando diretórios temporários.

## Problema

Imagine um workspace fictício contendo:

```text
workspace/
├── notes.txt
├── rows.csv
├── photo.png
├── backup.tar.gz
└── script.py
```

O organizador deve produzir:

```text
workspace/
├── documents/
│   └── notes.txt
├── data/
│   └── rows.csv
├── images/
│   └── photo.png
├── archives/
│   └── backup.tar.gz
└── other/
    └── script.py
```

O desafio importante não é apenas mover arquivos. O projeto torna as decisões de filesystem visíveis antes da mutação e se recusa a afirmar garantias de segurança que a plataforma atual não consegue aplicar.

## Requisitos

A implementação deve:

1. aceitar um diretório de origem existente que não seja symlink;
2. inspecionar apenas filhos diretos;
3. ignorar diretórios aninhados;
4. registrar symlinks filhos diretos separadamente, sem segui-los;
5. classificar arquivos regulares pelo sufixo do nome;
6. preservar exatamente os nomes dos arquivos;
7. criar pastas de destino somente quando necessárias;
8. produzir ordenação determinística;
9. construir um plano imutável antes da mutação;
10. rejeitar caminhos de categoria inválidos, inclusive diretórios de categoria que sejam symlinks;
11. detectar colisões de destino exatas e sem diferenciação de caixa durante planejamento/preflight;
12. oferecer políticas explícitas `ERROR` e `SKIP` durante o planejamento;
13. executar um preflight completo;
14. vincular a identidade de cada origem quando a execução começa, e não durante o planejamento;
15. nunca substituir silenciosamente um destino exato;
16. revalidar nomes de destino equivalentes por `casefold()` imediatamente antes do commit;
17. rejeitar mudanças da origem após o vínculo de identidade da execução e premissas obsoletas sobre raiz/categoria;
18. nunca executar `unlink()` cegamente em staging ou rollback cuja identidade possa ter mudado;
19. retornar resultado estruturado apenas após verificar o destino planejado.

## Escopo deliberado

O pipeline é:

```text
diretório de origem
    -> descoberta de arquivos diretos
    -> classificação por sufixo
    -> plano seguro contra colisões
    -> preflight de execução
    -> pastas de categoria ancoradas
    -> claim da origem
    -> nova checagem casefold na mutação
    -> commit atômico no-replace do nome exato no destino
```

Este projeto intencionalmente não inclui:

- organização recursiva;
- inspeção MIME ou de conteúdo;
- renomeação automática de duplicados;
- hashing ou deduplicação;
- exclusão como funcionalidade exposta ao usuário;
- transações de rollback para o plano inteiro;
- watchers de filesystem;
- interface gráfica;
- armazenamento em nuvem;
- movimentos entre filesystems diferentes.

Manter essas responsabilidades fora do escopo deixa as regras de segurança mais fáceis de inspecionar.

## Categorias

`FileCategory` define cinco destinos:

| Categoria | Pasta | Sufixos representativos |
|---|---|---|
| Documentos | `documents/` | `.txt`, `.md`, `.pdf`, `.docx` |
| Dados | `data/` | `.csv`, `.json`, `.xml`, `.xlsx` |
| Imagens | `images/` | `.png`, `.jpg`, `.webp`, `.svg` |
| Arquivos compactados | `archives/` | `.zip`, `.7z`, `.tar.gz`, `.tar.xz` |
| Outros | `other/` | tudo o que não corresponder acima |

A correspondência ignora diferenças entre maiúsculas e minúsculas. A classificação usa apenas nomes de arquivo e nunca abre o conteúdo.

## Modelos centrais

### `MoveAction`

Representa um movimento planejado:

```text
arquivo de origem -> destino da categoria
```

Suas invariantes exigem caminhos absolutos, o mesmo nome na origem e destino e uma pasta correspondente à categoria escolhida.

### `OrganizationPlan`

Armazena:

- o diretório de origem absoluto;
- valores `MoveAction` ordenados;
- arquivos ignorados por colisão;
- symlinks filhos diretos ignorados.

O plano é imutável. Criá-lo não cria diretórios e não move arquivos. Ele registra **intenção de pathname/categoria**, e não um descriptor aberto ou snapshot durável do objeto de filesystem por trás de cada pathname. Se um arquivo regular for substituído no mesmo pathname planejado antes de `execute_plan()` começar a pinar as origens, a substituição é o objeto atual selecionado por essa intenção de pathname. A identidade forte do objeto começa no pinning da execução.

### `OrganizationResult`

Registra exatamente os destinos planejados retornados após execução bem-sucedida.

## Descoberta intencionalmente rasa

`discover_files()` retorna somente arquivos regulares filhos diretos.

Movimento recursivo introduz contratos adicionais para caminhos relativos, categorias aninhadas e nomes duplicados entre diretórios. Esses temas pertencem a um projeto maior.

## Planejar antes de alterar

`plan_organization()` valida o workspace, varre arquivos diretos, classifica cada um e calcula destinos sem modificar o filesystem.

```text
observar -> decidir -> validar -> alterar
```

A proposta existe como dados antes de os efeitos colaterais começarem, facilitando revisão e testes. Essa separação deliberadamente **não** promete que um pathname ainda nomeie o mesmo objeto observado durante o planejamento; manter essa garantia exigiria descriptors de origem vivos dentro do plano. Em vez disso, a execução vincula o objeto regular atual em cada pathname planejado antes de criar categorias ou alterar origens.

## Políticas de colisão

### `CollisionPolicy.ERROR`

O planejamento gera `FileExistsError` quando um nome de destino já existe.

### `CollisionPolicy.SKIP`

Arquivos conflitantes permanecem na origem e são listados em `skipped_collisions`.

A execução revalida colisões depois do planejamento. A existência do nome exato é aplicada atomicamente no commit final do Linux; nomes equivalentes por `casefold()` são rechecados imediatamente antes desse commit.

## Colisões sem diferenciação de caixa

Filesystems variam quanto à sensibilidade de caixa. O organizador compara nomes lógicos de destino usando `casefold()`.

```text
Report.TXT
report.txt
```

Esses nomes são tratados como colisão lógica durante planejamento, preflight e a checagem imediatamente anterior ao commit, mesmo em filesystem case-sensitive.

Há uma fronteira importante: em um filesystem case-sensitive, a primitiva do kernel `RENAME_NOREPLACE` protege somente o **nome exato do destino**. Um processo externo que não coopere ainda pode criar outro nome equivalente por `casefold()` no pequeno intervalo após a última varredura. Por isso, o projeto não afirma unicidade atômica case-insensitive onde o filesystem não fornece essa garantia.

## Fronteiras de symlink e ancoragem de diretórios

O organizador não segue symlinks filhos diretos. Também rejeita diretório de origem ou pasta de categoria que seja symlink. No Windows, tanto o diretório de origem quanto as pastas de categoria são rejeitados quando são junctions NTFS: `is_dir()` segue um junction, então aceitá-lo poderia redirecionar descoberta ou movimentação para fora do workspace.

No caminho seguro do Linux, a raiz e as categorias necessárias são abertas com `O_DIRECTORY | O_NOFOLLOW`. Suas identidades `(device, inode)` são comparadas repetidamente com os caminhos que ainda deveriam alcançá-las.

Isso importa porque um file descriptor continua preso ao mesmo diretório mesmo quando outro processo renomeia esse diretório. O pinning impede redirecionamento por symlink; a validação de âncora impede continuar silenciosamente em um diretório que não está mais acessível pelo caminho planejado.

## Por que o preflight não basta

Uma implementação ingênua poderia fazer:

```python
if not destination.exists():
    source.rename(destination)
```

Essa checagem pode ficar obsoleta imediatamente. Outro processo pode criar o destino ou substituir uma origem ou diretório depois da validação.

O preflight reduz estados inseguros, mas garantias sensíveis a concorrência também precisam existir na fronteira de mutação.

## Identidade no filesystem

A implementação representa identidade com:

```text
(st_dev, st_ino)
```

O nome `notes.txt` é uma entrada de diretório, não a identidade do objeto do filesystem.

O planejamento registra intenção de pathname, e não identidade do objeto de origem. Portanto, um arquivo regular substituído no mesmo pathname **antes do pinning da execução** é aceito como o objeto atual selecionado pelo plano. Durante a execução segura no Linux, a identidade da origem só é aceita **depois que o arquivo atual já foi aberto** com `O_NOFOLLOW | O_NONBLOCK` quando `O_NONBLOCK` está disponível. O `fstat()` deriva `(device, inode)` desse descriptor já aberto, e todos os descriptors das origens planejadas permanecem abertos até o fim do plano. Assim, um inode aceito e depois desvinculado não pode ser liberado e imediatamente reutilizado enquanto a execução ainda depende da sua identidade. A flag nonblocking também impede que uma substituição tardia por FIFO trave o `open()`. O pinning estabiliza a identidade do objeto, não o conteúdo; escritas concorrentes no mesmo inode ficam fora das garantias de snapshot deste projeto.

## Nomes de staging com tamanho fixo

O caminho seguro do Linux reivindica temporariamente a entrada pública da origem com um nome interno:

```text
.fo-stage-<32 caracteres hexadecimais>
```

O staging tem tamanho fixo e nunca incorpora o nome original. Assim, um filename válido e longo não faz o nome interno ultrapassar um limite típico `NAME_MAX`.

## Commit atômico no-replace no Linux

O caminho seguro do Linux usa `renameat2(..., RENAME_NOREPLACE)` por meio de file descriptors ancorados.

Conceitualmente:

```text
1. validar caminhos e executar o preflight de colisões
2. abrir e ancorar a raiz
3. abrir o arquivo regular atual em cada pathname planejado e aceitar identidade pelo `fstat()` do descriptor pinado
4. manter todos os descriptors aceitos abertos até o fim do plano
5. abrir e ancorar as categorias necessárias
6. reivindicar origem -> staging curto com semântica no-replace
7. verificar identidade do staging e âncoras
8. varrer novamente a categoria ancorada por destino equivalente via casefold
9. renomear atomicamente staging -> destino exato com RENAME_NOREPLACE
10. verificar identidade do destino e âncoras
11. reportar sucesso
```

`RENAME_NOREPLACE` transforma a existência do **nome exato do destino** em parte da própria operação atômica. Não existe uma checagem `exists()` separada seguida de rename substitutivo. A varredura `casefold()` anterior captura colisões lógicas visíveis nessa fronteira, mas é documentada como rechecagem, não como lock atômico case-insensitive.

O caminho seguro normal não finaliza o movimento com `unlink()` do staging. Isso evita apenas transferir a mesma janela check-to-unlink do nome público para um nome interno.

## Recuperação conservadora

Erros concorrentes podem deixar estado incerto. A recuperação prioriza preservação em vez de limpeza destrutiva.

Se a execução já moveu a origem para staging e depois detecta condição insegura, ela pode criar um hard link no-replace de volta para o nome de origem quando possível. Ela não apaga cegamente o staging.

Um pathname de staging não funciona como lock de inode. Depois que a origem foi claimada, todo caminho de falha revalida se a entrada de staging ainda corresponde à identidade pinada da origem. Se corresponder, a execução pode tentar recriar o nome original por hard link no-replace a partir desse staging comprovado, mas a restauração só é aceita depois que o próprio pathname recriado da origem é relido e verificado com a identidade pinada. Se o link falhar, sofrer corrida para outro objeto, deixar o nome de origem ausente ou a identidade pós-link não corresponder, a execução deixa entradas incertas intactas e, antes de fechar o descritor ainda pinado da origem, copia os bytes planejados para um arquivo regular exclusivo `.fo-recovery-*`. Esse recovery não é reportado como preservado apenas porque seu descritor foi gravado e o `fsync()` terminou: a execução primeiro sincroniza o arquivo de recovery e depois sincroniza o diretório raiz ancorado para tornar durável, diante de crash, a entrada recém-criada no diretório. Ela fecha o descritor do recovery antes da prova final do pathname e então relê o pathname de recuperação pelo root ancorado, exigindo que ele aponte para o mesmo arquivo regular `(st_dev, st_ino)`. Se o pathname sumir, for renomeado ou substituído nesse ponto final de verificação, a execução falha em vez de afirmar falsamente que os dados foram retidos, sem excluir nem sobrescrever entradas incertas de terceiros. Essa é uma prova pontual do namespace: um processo externo não cooperativo com permissão para alterar o diretório ainda pode mudar o pathname depois da verificação, portanto o projeto não afirma retenção indefinida do pathname contra mudanças posteriores no namespace. Isso também cobre uma falha final de `RENAME_NOREPLACE` causada por um destino que aparece depois de uma corrida sobre o staging. Se um staging substituto for renomeado com sucesso e a verificação de identidade do destino detectar a divergência, o destino alheio também permanece intacto enquanto os bytes pinados são recuperados. A recuperação só é reportada quando o próprio pathname usado para informá-la é comprovado no ponto final de verificação.

Por isso, a execução segura no Linux exige deliberadamente permissão de leitura para cada arquivo regular planejado. A legibilidade é validada antes da criação das pastas de categoria e novamente ao pinar o inode da origem para a mutação; falhas de permissão são reportadas como `PermissionError`, e não como uma falsa mudança de identidade da origem.

Em cenários raros de corrida/falha, isso pode deixar uma entrada interna de recuperação. Os prefixos `.fo-stage-*` e `.fo-recovery-*` são namespaces internos reservados e ficam fora de descobertas futuras, evitando que evidências de recuperação sejam reorganizadas por acidente. É preferível a excluir ou reclassificar dados cuja identidade atual não pode ser comprovada.

O plano inteiro de múltiplos arquivos não é transacional.

## Contrato de plataforma

A implementação explicita as garantias por plataforma:

- **Linux:** execução segura com FDs ancorados usa `renameat2(RENAME_NOREPLACE)` quando disponível, com proteção atômica no-replace para o nome exato do destino e rechecagens `casefold()` na mutação;
- **Windows:** o caminho portátil protegido usa `os.rename()` recusando destino existente e realiza checagens best-effort de `casefold()`, redirecionamento e identidade. Ele **não** afirma possuir a mesma resistência a corridas adversariais baseada em descriptors pinados do caminho Linux;
- **outros POSIX:** a execução gera `NotImplementedError` quando não consegue aplicar a semântica no-replace exigida com segurança.

Um exemplo orientado a segurança deve falhar de forma honesta em vez de reduzir silenciosamente seu contrato.

## Fluxo de execução

`execute_plan()` realiza:

1. validação do tipo do plano;
2. revalidação do diretório de origem;
3. revalidação dos caminhos de categoria;
4. preflight de colisões;
5. seleção da capacidade da plataforma;
6. Linux: pinning de todas as origens antes de aceitar identidade e antes de mutar categorias;
7. preparação dos diretórios ancorados;
8. claim da origem;
9. rechecagem de colisão por `casefold()` na mutação;
10. commit atômico no-replace do nome exato;
11. verificação do destino e das âncoras;
12. construção de `OrganizationResult`.

## Determinismo

Arquivos e ações são ordenados por:

```python
(path.name.casefold(), path.name)
```

Isso mantém exemplos, testes e revisão estáveis.

## Executando o demo

A partir da raiz do repositório:

```bash
python practical-projects/06-file-organizer/demo.py
```

O demo usa `TemporaryDirectory`, cria apenas arquivos fictícios, imprime o plano, executa e mostra as pastas resultantes.

## Executando os testes

Suíte focada:

```bash
python -m pytest practical-projects/06-file-organizer/tests -q
```

O capítulo evita contagem fixa de testes porque a cobertura de regressão evolui conforme os reviews.

A cobertura inclui:

- classificação por sufixo;
- descoberta rasa e determinística;
- tratamento de symlinks;
- invariantes dos modelos imutáveis;
- colisões exatas e sem diferenciação de caixa;
- políticas `ERROR` e `SKIP`;
- origens ausentes ou obsoletas;
- destinos exatos tardios;
- destinos tardios equivalentes por `casefold()` antes do commit final;
- substituição tardia da origem por symlink/arquivo/FIFO;
- pinning nonblocking da origem;
- corridas de symlink e rename da categoria;
- corridas de rename da raiz;
- staging com tamanho fixo;
- finalização do staging sem `unlink()`;
- verificação da identidade do destino;
- execução bem-sucedida e planos vazios.

## Caminhos de falha importantes

### Diretório de origem ausente

Gera `FileNotFoundError`.

### Caminho de origem é arquivo regular

Gera `NotADirectoryError`.

### Diretório de origem é symlink

É rejeitado antes da varredura.

### Caminho de categoria é arquivo ou symlink

É rejeitado antes do planejamento ou execução.

### Destino aparece depois do planejamento

O preflight e a rechecagem `casefold()` na mutação geram `FileExistsError` para colisões que observam. O `RENAME_NOREPLACE` final do Linux rejeita atomicamente um destino com nome exato que apareça na fronteira do commit.

### Origem planejada vira FIFO ou outro arquivo especial

O pinning no Linux usa flags nonblocking e depois o `fstat()` rejeita a substituição por não ser arquivo regular, em vez de travar a execução.

### Origem planejada muda

Uma substituição por outro arquivo regular antes do vínculo de identidade da execução é aceita como o objeto atual selecionado pelo plano. Mudanças após esse vínculo são rejeitadas em vez de serem tratadas como a origem vinculada.

### Raiz ou categoria é renomeada/substituída

A validação de âncora gera erro em vez de retornar um caminho que não identifica mais o destino comprometido.

### Primitiva atômica no-replace indisponível

A plataforma não suportada gera erro em vez de enfraquecer silenciosamente o contrato.

## Erros comuns

### Mover enquanto varre

Misturar descoberta e mutação torna falhas parciais difíceis de raciocinar. Construa o plano primeiro.

### Tratar nome como identidade

Entradas de diretório podem ser substituídas mantendo o mesmo nome. Use identidade do filesystem quando essa diferença importa.

### Abrir um caminho substituível em modo bloqueante

`O_NOFOLLOW` rejeita symlinks, mas não impede que um FIFO bloqueie um `open()` read-only. Use pinning nonblocking antes de validar o tipo do arquivo.

### Assumir que uma varredura `casefold()` é um lock atômico

Uma varredura em user space detecta colisões lógicas sem diferenciação de caixa, mas em filesystem case-sensitive não consegue impedir que outro nome com caixa diferente apareça depois. Mantenha a garantia atômica limitada ao nome exato aplicado pela primitiva do kernel.

### Verificar imediatamente antes de `unlink()`

Ainda existe uma janela check-to-unlink. Quando a identidade da exclusão importa, reestruture a operação em vez de adicionar outra checagem.

### Assumir que um FD aberto ainda tem o mesmo pathname

O descriptor acompanha o inode do diretório após rename. Verifique sua âncora contra o caminho planejado.

### Embutir o nome completo da origem no staging

Nomes válidos podem já estar próximos do `NAME_MAX`. Mantenha nomes internos limitados independentemente.

### Limpar cegamente depois de uma corrida

Cleanup também é mutação. Preserve entradas incertas em vez de apagar algo que pode pertencer a outro ator.

### Tratar preflight como transação

O filesystem pode mudar depois. Um plano de vários arquivos continua sendo uma sequência de commits individualmente protegidos.

## Exercício

Estenda o organizador com um **renderizador de dry run** sem alterar o comportamento de execução.

Requisitos:

1. aceitar um `OrganizationPlan`;
2. retornar texto legível e determinístico;
3. mostrar movimentos planejados, colisões ignoradas e symlinks ignorados;
4. nunca acessar ou modificar o filesystem;
5. adicionar testes para planos vazios e não vazios.

## Desafios de extensão

Considere:

- mapeamento configurável de sufixos;
- categorias definidas pelo usuário;
- exportação/importação JSON com validação de plano obsoleto;
- journal de operações;
- descoberta recursiva com regras explícitas de caminho relativo;
- deduplicação por checksum;
- tooling de recuperação/auditoria para entradas de staging preservadas;
- design transacional para outro domínio de problema.

Cada extensão introduz novas invariantes. Defina o contrato antes de adicionar código.

## Discussão de portfólio

Uma explicação útil não é “eu escrevi um script que move arquivos”.

Uma versão mais forte é:

> Eu projetei um fluxo de filesystem com planejamento determinístico, políticas explícitas de colisão, fronteiras de symlink/arquivo especial, identidade por inode, diretórios ancorados por descriptors, nomes de staging limitados, rechecagens `casefold()` na mutação e commit atômico no-replace do nome exato no Linux com `renameat2(RENAME_NOREPLACE)`. O tratamento de falhas preserva estado incerto em vez de apagar entradas cegamente.

Isso comunica decisões de engenharia, não apenas uso de APIs.

## Referência rápida

| Tarefa | Função/tipo |
|---|---|
| Classificar filename | `classify_path()` |
| Descobrir arquivos regulares diretos | `discover_files()` |
| Construir uma proposta segura | `plan_organization()` |
| Escolher comportamento de colisão | `CollisionPolicy` |
| Descrever um movimento | `MoveAction` |
| Manter o plano imutável | `OrganizationPlan` |
| Executar o plano | `execute_plan()` |
| Manter destinos bem-sucedidos | `OrganizationResult` |
| Identificar objetos do filesystem | `(st_dev, st_ino)` |
| Rechecagem lógica por `casefold()` | `listdir()` no diretório ancorado |
| Commit seguro do nome exato no Linux | `renameat2(RENAME_NOREPLACE)` |

## O que vem depois

O Projeto 05 gerou arquivos. O Projeto 06 assume a próxima fronteira: descobrir e organizar arquivos com segurança.

O Projeto 07 sobe novamente de nível, combinando registros de domínio validados e estados explícitos de workflow em um **fluxo fictício de conciliação**.
