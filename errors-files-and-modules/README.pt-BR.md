<div align="center">

# Erros, Arquivos e Módulos

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Esta seção inicia a transição de pequenos programas que trabalham apenas em memória para programas que precisam lidar com falhas, dados persistentes e código organizado em vários arquivos.

A Fase 7 começa com tratamento de exceções, avança para a criação deliberada de exceções, trabalha com arquivos e dados de texto estruturados com segurança e termina organizando código Python com imports, módulos e pacotes.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. `try`, `except`, `else` e `finally`](01-try-except-else-finally/README.pt-BR.md) | Tratar falhas esperadas em runtime mantendo explícitos os caminhos normal e de limpeza | Iniciante a intermediário | Disponível |
| 02. Levantando Exceções e Exceções Personalizadas | Sinalizar estados inválidos deliberadamente com `raise` e introduzir exceções personalizadas simples | Intermediário | Planejado |
| 03. `open()` e `with` | Ler e escrever arquivos de texto gerenciando recursos com segurança | Iniciante a intermediário | Planejado |
| 04. TXT, CSV e JSON | Trabalhar com formatos comuns de dados baseados em texto e seus limites | Intermediário | Planejado |
| 05. Imports, Módulos e Pacotes | Dividir código em arquivos reutilizáveis e entender o modelo de importação do Python | Intermediário | Planejado |

## Orientação de pré-requisitos

Antes de iniciar esta fase, é recomendável estar confortável com:

- condições e lógica booleana;
- loops;
- funções, parâmetros e valores retornados;
- conversão básica de tipos;
- leitura conceitual de tracebacks simples;
- a diferença entre comentários no código-fonte e comportamento em runtime.

A trilha completa para iniciantes das Fases 1–6 fornece todas essas bases.

## Sequência recomendada

Ao seguir o currículo completo, estude os capítulos em ordem numérica:

```text
01. Tratar exceções
        ↓
02. Levantar exceções deliberadamente
        ↓
03. Abrir e gerenciar arquivos
        ↓
04. Ler e escrever formatos comuns de dados
        ↓
05. Organizar código com módulos e pacotes
```

A sequência é intencional. Antes de um programa começar a depender de arquivos e vários módulos, ele deve ter um modelo claro do que acontece quando uma operação não consegue terminar normalmente.

## Objetivos da seção

Ao final da Fase 7, você deverá conseguir:

- distinguir fluxo normal de controle de fluxo provocado por exceções;
- tratar exceções específicas de runtime sem esconder falhas não relacionadas;
- usar `else` e `finally` de forma deliberada;
- levantar exceções apropriadas quando uma função não consegue cumprir seu contrato;
- abrir, ler e escrever arquivos usando padrões seguros de gerenciamento de recursos;
- trabalhar com texto simples, CSV e JSON em nível introdutório;
- separar responsabilidades de parsing, validação, transformação e persistência;
- importar código de módulos e pacotes;
- explicar como arquivos, exceções, funções e módulos se conectam em um pequeno programa real.

## Capítulo atual

Comece por [Tratando Exceções com `try`, `except`, `else` e `finally`](01-try-except-else-finally/README.pt-BR.md).

O primeiro capítulo se concentra em **tratar exceções que já acontecem**. Criar exceções deliberadamente com `raise` fica reservado para o Capítulo 02, mantendo as duas responsabilidades fáceis de distinguir.

## Estrutura do diretório

```text
errors-files-and-modules/
├── README.md
├── README.pt-BR.md
├── README.es.md
└── 01-try-except-else-finally/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── parse_integer.py
        ├── safe_divide.py
        └── trace_try_else_finally.py
```

Os diretórios dos capítulos planejados são adicionados somente quando seu conteúdo é realmente publicado.
