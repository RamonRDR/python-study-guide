<div align="center">

# Projeto 06 · Organizador de Arquivos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

[← Voltar para Projetos Práticos](../README.pt-BR.md)

> **Fase 10 · Projetos Práticos**

Este projeto organiza arquivos filhos diretos em pastas por categoria, mantendo descoberta, planejamento, tratamento de colisões e mutação do filesystem explícitos e testáveis.

## Objetivos de aprendizagem

Ao concluir este projeto, você deverá ser capaz de:

- descobrir arquivos com `pathlib` sem percorrer uma árvore recursivamente;
- classificar nomes de arquivos de forma determinística por regras de sufixo sem diferenciar maiúsculas e minúsculas;
- modelar mudanças planejadas no filesystem com dataclasses imutáveis;
- separar uma fase de planejamento sem mutação de uma fase de execução com efeitos colaterais;
- detectar colisões exatas e colisões de destino ignorando diferenças de caixa;
- escolher uma política de colisão explícita em vez de sobrescrever dados silenciosamente;
- tratar symlinks como uma fronteira específica do filesystem;
- revalidar premissas imediatamente antes da mutação;
- garantir no próprio passo de mutação que um destino exato nunca seja substituído;
- verificar a identidade da origem através de fronteiras time-of-check/time-of-use;
- preservar estado incerto de destino em vez de executar rollback destrutivo;
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

O desafio importante não é apenas chamar uma função de movimento. O projeto precisa tornar visíveis as decisões destrutivas antes de alterar qualquer coisa.

## Requisitos

A implementação deve:

1. aceitar um diretório de origem existente que não seja symlink;
2. inspecionar apenas filhos diretos desse diretório;
3. ignorar diretórios aninhados;
4. registrar symlinks filhos diretos separadamente, sem segui-los;
5. classificar arquivos regulares pelo sufixo do nome;
6. preservar exatamente cada nome de arquivo;
7. criar pastas de destino somente quando necessárias;
8. produzir ordenação determinística;
9. construir um plano imutável antes da mutação;
10. rejeitar caminhos de categoria inválidos, inclusive diretórios de categoria que sejam symlinks;
11. detectar colisões de destino exatas e sem diferenciação de caixa;
12. oferecer políticas explícitas `ERROR` e `SKIP` durante o planejamento;
13. executar um preflight completo antes de qualquer movimento;
14. nunca substituir silenciosamente um destino exato que apareça depois do preflight;
15. rejeitar uma origem planejada cuja identidade no filesystem mude antes do commit;
16. nunca excluir um destino não verificado ao tratar falha na remoção da origem;
17. retornar um resultado estruturado após a execução bem-sucedida.

## Escopo deliberado

O pipeline é:

```text
diretório de origem
    -> descoberta de arquivos diretos
    -> classificação por sufixo
    -> plano seguro contra colisões
    -> preflight de execução
    -> pastas de categoria necessárias
    -> movimentos no-replace com identidade verificada
```

Este projeto intencionalmente **não** inclui:

- organização recursiva;
- inspeção MIME ou de conteúdo;
- renomeação automática de duplicados;
- hashing ou deduplicação;
- exclusão;
- transações de rollback para o plano inteiro;
- watchers de filesystem;
- interface gráfica;
- armazenamento em nuvem;
- organização entre filesystems diferentes.

Manter essas responsabilidades fora do escopo deixa as regras de segurança visíveis em vez de escondê-las dentro de um gerenciador de arquivos genérico.

## Categorias

`FileCategory` define cinco destinos:

| Categoria | Pasta | Sufixos representativos |
|---|---|---|
| Documentos | `documents/` | `.txt`, `.md`, `.pdf`, `.docx` |
| Dados | `data/` | `.csv`, `.json`, `.xml`, `.xlsx` |
| Imagens | `images/` | `.png`, `.jpg`, `.webp`, `.svg` |
| Arquivos compactados | `archives/` | `.zip`, `.7z`, `.tar.gz`, `.tar.xz` |
| Outros | `other/` | tudo o que não corresponder às regras acima |

A correspondência ignora diferenças entre maiúsculas e minúsculas. A classificação usa apenas o nome do arquivo e não abre seu conteúdo.

## Modelos centrais

### `MoveAction`

Representa um movimento planejado:

```text
arquivo de origem -> destino da categoria
```

Suas invariantes exigem caminhos absolutos, o mesmo nome na origem e no destino e uma pasta de destino correspondente à categoria escolhida.

### `OrganizationPlan`

Armazena:

- o diretório de origem absoluto;
- valores `MoveAction` ordenados;
- arquivos ignorados por colisão;
- symlinks filhos diretos ignorados.

O plano é imutável. Criá-lo não cria diretórios e não move arquivos.

### `OrganizationResult`

Registra exatamente os destinos planejados que foram movidos com sucesso.

## Descoberta intencionalmente rasa

`discover_files()` retorna somente arquivos regulares que são filhos diretos.

Diretórios aninhados não são percorridos. Isso importa porque movimento recursivo cria perguntas adicionais:

- o caminho relativo deve ser preservado?
- pastas de categoria dentro de subdiretórios devem ser revisitadas?
- como lidar com nomes duplicados vindos de subdiretórios diferentes?

Essas perguntas são úteis, mas pertencem a um projeto maior.

## Planejar antes de alterar

`plan_organization()` valida o diretório, varre os arquivos, classifica cada um e calcula os destinos sem modificar o filesystem.

Essa separação cria um padrão de engenharia útil:

```text
observar -> decidir -> validar -> alterar
```

É mais fácil testar e revisar uma operação proposta quando ela existe como dados antes de os efeitos colaterais começarem.

## Políticas de colisão

Duas políticas são explícitas:

### `CollisionPolicy.ERROR`

O planejamento para com `FileExistsError` quando um nome de destino já existe.

### `CollisionPolicy.SKIP`

Arquivos cujo destino colide permanecem no diretório de origem e são listados em `skipped_collisions`.

A política é aplicada no planejamento. A execução continua recusando colisões exatas novas que apareçam depois.

## Colisões sem diferenciação de caixa

O projeto compara nomes de destino com `casefold()` durante planejamento e preflight. Por exemplo:

```text
Report.TXT
report.txt
```

Esses nomes são tratados como uma colisão lógica.

## Fronteira de symlink

O organizador não segue symlinks filhos diretos.

Ele também rejeita:

- um diretório de origem que seja symlink;
- uma pasta de categoria implementada como symlink.

Em plataformas com suporte a descritores de diretório, a execução fixa a origem e as pastas de categoria usando `O_DIRECTORY | O_NOFOLLOW`. Assim, uma categoria que vire symlink depois do preflight não consegue redirecionar a mutação para fora do workspace.

## Por que o preflight não basta

Uma implementação inicial poderia fazer:

```python
if not destination.exists():
    source.rename(destination)
```

Isso contém uma corrida de time-of-check/time-of-use. Outro processo pode criar o destino depois da checagem e antes do rename.

Em POSIX, `rename()` pode substituir um destino existente. Além disso, uma origem planejada pode ser substituída depois do preflight. Por isso, a execução precisa validar tanto a disponibilidade do destino quanto a identidade da origem no momento da mutação.

## Mutação exata no-replace

A execução usa hard link no mesmo filesystem como proteção de destino:

```text
1. capturar a identidade da origem no preflight
2. revalidar que a origem continua sendo o mesmo arquivo regular
3. criar o hard link de destino sem substituição
4. verificar que o destino referencia a identidade esperada da origem
5. revalidar novamente a identidade da origem
6. remover o caminho de origem original
```

A identidade do filesystem é representada pelo par `(device, inode)` retornado por `stat`. Isso permite diferenciar “o mesmo nome” de “o mesmo objeto do filesystem”. Uma substituição tardia por symlink ou por outro arquivo regular aborta a execução em vez de ser relatada como movimento bem-sucedido.

`os.link()` não substitui um destino existente. Como toda pasta de destino fica dentro do mesmo diretório de origem, origem e destino permanecem intencionalmente no mesmo filesystem neste projeto.

Se a criação do link falhar, a origem permanece intacta. Se a remoção da origem falhar depois da criação do destino, a implementação deliberadamente **mantém o destino** e gera erro. Ela não executa um `unlink()` de rollback incondicional, porque outro processo poderia ter substituído aquela entrada de diretório nesse intervalo. Preservar estado incerto é mais seguro do que excluir algo cuja identidade não pode mais ser comprovada.

Isso não transforma o plano inteiro em uma transação. As garantias são mais estreitas: destinos exatos não são sobrescritos silenciosamente, origens planejadas são revalidadas por identidade e o tratamento de falha não exclui intencionalmente um destino não verificado.

## Fluxo de execução

`execute_plan()` realiza:

1. validação de tipo;
2. revalidação do diretório de origem;
3. revalidação dos caminhos de categoria;
4. captura das identidades das origens planejadas;
5. preflight de colisões de destino;
6. criação/abertura apenas das pastas necessárias;
7. movimentos exatos no-replace com identidade verificada;
8. construção de `OrganizationResult`.

Um plano antigo, portanto, não é aceito cegamente.

## Determinismo

Arquivos e ações são ordenados por:

```python
(path.name.casefold(), path.name)
```

Isso mantém exemplos, testes e revisão estáveis em vez de depender da ordem de iteração do filesystem.

## Executando o demo

A partir da raiz do repositório:

```bash
python practical-projects/06-file-organizer/demo.py
```

O demo usa `TemporaryDirectory`, cria apenas arquivos fictícios, mostra os movimentos planejados, executa o plano e exibe o layout final. Ele não toca em diretórios pessoais.

## Executando os testes

Suíte focada:

```bash
python -m pytest practical-projects/06-file-organizer/tests -q
```

Este capítulo evita embutir uma contagem fixa de cenários porque a cobertura de regressão cresce conforme findings de revisão são endurecidos.

A cobertura inclui:

- classificação por sufixo;
- validação de caminhos;
- descoberta determinística;
- varredura rasa;
- tratamento de symlinks;
- invariantes dos modelos imutáveis;
- colisões exatas e sem diferenciação de caixa;
- políticas `ERROR` e `SKIP`;
- origens ausentes ou obsoletas;
- mudanças em caminhos de categoria;
- preflight de colisões;
- destino criado entre preflight e mutação;
- categoria virando symlink durante a mutação;
- origem planejada virando symlink durante a mutação;
- falha na remoção da origem sem rollback destrutivo do destino;
- execução bem-sucedida;
- preservação de arquivos de destino não relacionados;
- planos vazios.

## Caminhos de falha importantes

### Diretório de origem ausente

Gera `FileNotFoundError`.

### Caminho de origem é um arquivo regular

Gera `NotADirectoryError`.

### Diretório de origem é symlink

É rejeitado antes da varredura.

### Caminho de categoria é arquivo ou symlink

É rejeitado antes do planejamento ou execução.

### Destino existe durante o planejamento

É tratado conforme a política de colisão selecionada.

### Destino aparece depois do planejamento

O preflight gera `FileExistsError` antes de qualquer movimento.

### Destino exato aparece depois do preflight

A operação de hard link no-replace falha com `FileExistsError`; o destino recém-criado é preservado e a origem permanece no lugar.

### Identidade da origem planejada muda durante a execução

A execução gera erro em vez de remover a entrada alterada ou relatar o movimento como sucesso.

### Remoção da origem falha depois da criação do destino

A execução gera erro e mantém o destino. Ela evita deliberadamente excluir um destino cuja identidade atual não pode ser comprovada com segurança durante rollback.

## Erros comuns

### Mover enquanto varre

Misturar descoberta e mutação torna falhas parciais difíceis de entender. Prefira construir um plano primeiro.

### Usar apenas `Path.exists()` antes de `rename()`

A checagem pode ficar obsoleta imediatamente, e a semântica POSIX de rename pode substituir o destino.

### Tratar nome de arquivo como identidade do objeto

Uma entrada de diretório pode ser substituída mantendo o mesmo nome. Quando concorrência importa, compare identidade do filesystem e tipo do arquivo na fronteira de mutação.

### Fazer rollback apagando cegamente o destino

O caminho de rollback também é um caminho de mutação. Se outro ator puder substituir a entrada de destino, uma exclusão incondicional pode destruir dados não relacionados.

### Inventar novos nomes silenciosamente

Renomear colisões para valores como `report_2.txt` esconde uma decisão de política.

### Seguir symlinks sem perceber

Um caminho aparentemente simples pode apontar para fora do workspace pretendido.

### Assumir ordem de iteração do diretório

A ordem de iteração do filesystem não é um contrato de ordenação da aplicação.

### Tratar um preflight bem-sucedido como transação

O filesystem pode mudar depois do preflight. Revalidação reduz o risco, mas não torna uma operação de múltiplos arquivos transacional.

## Exercício

Estenda o organizador com um **renderizador de dry run** sem alterar o comportamento de execução.

Requisitos:

1. aceitar um `OrganizationPlan`;
2. retornar texto determinístico e legível;
3. mostrar movimentos planejados, colisões ignoradas e symlinks ignorados;
4. nunca acessar nem modificar o filesystem;
5. adicionar testes para planos vazios e não vazios.

## Desafios de extensão

Depois do exercício, considere:

- mapeamento configurável de sufixos para categorias;
- alternativa com categorias definidas pelo usuário;
- exportação/importação JSON do plano com validação cuidadosa de plano obsoleto;
- journal de operações;
- descoberta recursiva com regras explícitas de caminho relativo;
- detecção de duplicidade por checksum;
- uma primitiva condicional de remoção de origem ainda mais forte e específica de plataforma;
- estratégia de rollback para planos parcialmente executados.

Cada extensão adiciona novas invariantes. Defina o contrato antes de adicionar o código.

## Discussão de portfólio

Uma explicação mais forte seria:

> Eu projetei um fluxo de filesystem com fase de planejamento sem mutação, classificação determinística, políticas explícitas de colisão, fronteiras de symlink, validação de identidade na execução, proteção exata no-replace do destino e tratamento conservador de falhas que nunca apaga cegamente um alvo de rollback não verificado.

Isso comunica decisões de engenharia, não apenas uso de API.

## Referência rápida

| Tarefa | Função/tipo |
|---|---|
| Classificar um nome de arquivo | `classify_path()` |
| Descobrir arquivos regulares diretos | `discover_files()` |
| Construir uma proposta segura | `plan_organization()` |
| Escolher comportamento de colisão | `CollisionPolicy` |
| Descrever um movimento | `MoveAction` |
| Manter o plano imutável | `OrganizationPlan` |
| Executar o plano | `execute_plan()` |
| Manter destinos bem-sucedidos | `OrganizationResult` |
| Verificar identidade do filesystem | `(st_dev, st_ino)` de `stat` |
| Garantir mutação exata no-replace | `os.link()` + `unlink()` da origem verificada |

## O que vem depois

O Projeto 05 gerou arquivos. O Projeto 06 assume a próxima fronteira: descobrir e organizar arquivos com segurança.

O Projeto 07 volta a subir de nível, combinando registros de domínio validados e estados explícitos de workflow em um **fluxo fictício de conciliação**.
