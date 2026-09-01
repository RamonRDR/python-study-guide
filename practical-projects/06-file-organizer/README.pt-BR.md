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
- tratar symlinks como uma fronteira do filesystem;
- raciocinar sobre corridas time-of-check/time-of-use;
- comparar objetos do filesystem pela identidade `(device, inode)`;
- ancorar diretórios com file descriptors no Linux;
- usar semântica atômica no-replace na fronteira final de commit;
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
11. detectar colisões de destino exatas e sem diferenciação de caixa;
12. oferecer políticas explícitas `ERROR` e `SKIP` durante o planejamento;
13. executar um preflight completo;
14. capturar a identidade das origens planejadas;
15. nunca substituir silenciosamente um destino exato;
16. rejeitar premissas obsoletas sobre origem, raiz ou categoria durante a execução;
17. nunca executar `unlink()` cegamente em staging ou rollback cuja identidade possa ter mudado;
18. retornar resultado estruturado apenas após verificar o destino planejado.

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
    -> commit atômico no-replace no destino
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

O plano é imutável. Criá-lo não cria diretórios e não move arquivos.

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

A proposta existe como dados antes de os efeitos colaterais começarem, facilitando revisão e testes.

## Políticas de colisão

### `CollisionPolicy.ERROR`

O planejamento gera `FileExistsError` quando um nome de destino já existe.

### `CollisionPolicy.SKIP`

Arquivos conflitantes permanecem na origem e são listados em `skipped_collisions`.

A execução ainda recusa colisões que apareçam depois do planejamento.

## Colisões sem diferenciação de caixa

Filesystems variam quanto à sensibilidade de caixa. O organizador compara nomes lógicos de destino usando `casefold()`.

```text
Report.TXT
report.txt
```

Esses nomes são tratados como colisão lógica mesmo em um filesystem case-sensitive.

## Fronteiras de symlink e ancoragem de diretórios

O organizador não segue symlinks filhos diretos. Também rejeita diretório de origem ou pasta de categoria que seja symlink.

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

Durante a execução segura no Linux, a origem planejada também é aberta com `O_NOFOLLOW`, fixando o inode esperado enquanto o commit ocorre. Isso evita que um inode liberado seja reutilizado e confundido com a origem planejada.

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
1. executar preflight e capturar identidade da origem
2. abrir e ancorar a raiz
3. abrir e ancorar as categorias necessárias
4. fixar o inode da origem com O_NOFOLLOW
5. reivindicar atomicamente origem -> staging curto
6. verificar identidade do staging e âncoras
7. renomear atomicamente staging -> destino com RENAME_NOREPLACE
8. verificar identidade do destino e âncoras
9. reportar sucesso
```

`RENAME_NOREPLACE` transforma a existência do destino em parte da própria operação atômica. Não existe uma checagem `exists()` separada seguida de rename substitutivo.

O caminho seguro normal não finaliza o movimento com `unlink()` do staging. Isso evita apenas transferir a mesma janela check-to-unlink do nome público para um nome interno.

## Recuperação conservadora

Erros concorrentes podem deixar estado incerto. A recuperação prioriza preservação em vez de limpeza destrutiva.

Se a execução já moveu a origem para staging e depois detecta condição insegura, ela pode criar um hard link no-replace de volta para o nome de origem quando possível. Ela não apaga cegamente o staging.

Em cenários raros de corrida/falha, isso pode deixar uma entrada interna de recuperação. É preferível a excluir dados cuja identidade atual não pode ser comprovada.

O plano inteiro de múltiplos arquivos não é transacional.

## Contrato de plataforma

A implementação explicita as garantias por plataforma:

- **Linux:** execução segura com FDs ancorados usa `renameat2(RENAME_NOREPLACE)` quando disponível;
- **Windows:** o fallback usa o comportamento de `os.rename()` que recusa destino existente e verifica identidades ao redor da operação;
- **outros POSIX:** a execução gera `NotImplementedError` quando não consegue aplicar a semântica no-replace exigida com segurança.

Um exemplo orientado a segurança deve falhar de forma honesta em vez de reduzir silenciosamente seu contrato.

## Fluxo de execução

`execute_plan()` realiza:

1. validação do tipo do plano;
2. revalidação do diretório de origem;
3. revalidação dos caminhos de categoria;
4. captura das identidades das origens planejadas;
5. preflight de colisões;
6. seleção da capacidade da plataforma;
7. preparação dos diretórios ancorados;
8. claim da origem e commit atômico no-replace;
9. verificação do destino e das âncoras;
10. construção de `OrganizationResult`.

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
- substituição tardia da origem por symlink/arquivo;
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

O preflight ou o commit atômico no-replace gera `FileExistsError`.

### Origem planejada muda

A execução gera erro em vez de tratar a substituição como o arquivo planejado.

### Raiz ou categoria é renomeada/substituída

A validação de âncora gera erro em vez de retornar um caminho que não identifica mais o destino comprometido.

### Primitiva atômica no-replace indisponível

A plataforma não suportada gera erro em vez de enfraquecer silenciosamente o contrato.

## Erros comuns

### Mover enquanto varre

Misturar descoberta e mutação torna falhas parciais difíceis de raciocinar. Construa o plano primeiro.

### Tratar nome como identidade

Entradas de diretório podem ser substituídas mantendo o mesmo nome. Use identidade do filesystem quando essa diferença importa.

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

> Eu projetei um fluxo de filesystem com planejamento determinístico, políticas explícitas de colisão, fronteiras de symlink, identidade por inode, diretórios ancorados por descriptors, nomes de staging limitados e commit atômico no-replace no Linux com `renameat2(RENAME_NOREPLACE)`. O tratamento de falhas preserva estado incerto em vez de apagar entradas cegamente.

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
| Commit seguro no Linux | `renameat2(RENAME_NOREPLACE)` |

## O que vem depois

O Projeto 05 gerou arquivos. O Projeto 06 assume a próxima fronteira: descobrir e organizar arquivos com segurança.

O Projeto 07 sobe novamente de nível, combinando registros de domínio validados e estados explícitos de workflow em um **fluxo fictício de conciliação**.
