<div align="center">

# Biblioteca Padrão

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

O Python inclui uma biblioteca padrão ampla. Esses módulos resolvem problemas comuns sem exigir instalação de terceiros, mas cada ferramenta ainda possui contratos, trade-offs e modos de falha próprios.

A Fase 8 parte do modelo de imports aprendido na Fase 7 e estuda um conjunto focado de módulos muito presentes em programas Python reais.

## Trilha de aprendizagem

| Capítulo | Foco principal | Nível | Status |
|---|---|---|---|
| [01. `pathlib`](01-pathlib/README.pt-BR.md) | Representar, compor, inspecionar, criar, ler e descobrir caminhos do sistema de arquivos com objetos próprios para caminhos | Intermediário | Disponível |
| [02. `datetime`](02-datetime/README.pt-BR.md) | Trabalhar com datas, horários, durações, parsing, formatação, consciência de timezone e aritmética | Intermediário | Disponível |
| [03. `json`](03-json/README.pt-BR.md) | Controlar contratos de serialização e decodificação, comportamento numérico estrito, hooks, valores personalizados, nomes duplicados e saída determinística | Intermediário | Disponível |
| [04. `csv`](04-csv/README.pt-BR.md) | Controlar dialetos, quoting, escaping, formato das linhas, sniffing e contratos de texto tabular | Intermediário | Disponível |
| 05. `logging` | Configurar loggers, handlers, formatters, níveis e logging de aplicação versus biblioteca | Intermediário | Planejado |
| 06. `collections` | Usar contêineres especializados como `Counter`, `defaultdict` e `deque` | Intermediário | Planejado |
| 07. `itertools` | Construir pipelines eficientes de iteradores com ferramentas reutilizáveis | Intermediário | Planejado |
| 08. `decimal` | Executar aritmética decimal exata com arredondamento e contexto explícitos | Intermediário | Planejado |
| 09. `os` e `shutil` | Trabalhar com ambiente, operações de filesystem de nível mais baixo, cópia, movimentação e árvores de diretórios | Intermediário | Planejado |

## Pré-requisitos

Antes de iniciar esta fase, é importante estar confortável com:

- funções e valores de retorno;
- coleções e iteração;
- exceções;
- arquivos e context managers;
- imports, módulos e pacotes.

A trilha completa pelas Fases 1-7 fornece essa base.

## Sequência recomendada

Ao seguir o currículo completo, estude em ordem:

```text
01. Modelar caminhos com pathlib
        ↓
02. Modelar datas e durações com datetime
        ↓
03. Aprofundar JSON
        ↓
04. Aprofundar CSV
        ↓
05. Configurar logging em runtime
        ↓
06. Usar coleções especializadas
        ↓
07. Compor pipelines de iteradores
        ↓
08. Usar aritmética decimal exata
        ↓
09. Trabalhar com utilitários de OS e filesystem
```

A ordem é intencional. Ela parte de um trabalho já familiar com arquivos e avança por tempo, formatos de dados, diagnóstico, contêineres, iteração, precisão numérica e utilitários de sistema de nível mais baixo.

## Objetivos da seção

Ao final da Fase 8, você deverá conseguir:

- escolher ferramentas da biblioteca padrão em vez de reinventar infraestrutura comum;
- ler a documentação oficial dos módulos com mais segurança;
- entender que o nome de um módulo não é um contrato completo de uso;
- combinar módulos da biblioteca padrão com funções, exceções, arquivos e pacotes;
- reconhecer APIs que se sobrepõem e escolher pela intenção;
- preservar comportamento determinístico quando ordem e ambiente podem variar;
- escrever programas pequenos que dependam apenas do Python e de sua biblioteca padrão.

## Status da fase

A Fase 8 está em andamento. O Capítulo 01 introduz [`pathlib`](01-pathlib/README.pt-BR.md), o Capítulo 02 acrescenta [`datetime`](02-datetime/README.pt-BR.md), o Capítulo 03 aprofunda [`json`](03-json/README.pt-BR.md), e o Capítulo 04 aprofunda [`csv`](04-csv/README.pt-BR.md) com políticas explícitas de dialeto, quoting, escaping, cabeçalho, formato das linhas, sniffing, fronteira de encoding e consumidores de planilha. O próximo capítulo planejado é `logging`.

Os Capítulos 03 e 04 revisitam `json` e `csv` em um nível mais profundo de biblioteca, enquanto um capítulo posterior fará o mesmo com `logging`. As aparições anteriores ensinaram formatos de arquivo ou conceitos maiores de design; nesta fase estudamos os módulos, suas APIs e seus trade-offs.

## Estrutura do diretório

```text
standard-library/
├── README.md
├── README.pt-BR.md
├── README.es.md
├── 01-pathlib/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── discover_python_files.py
│       ├── inspect_paths.py
│       ├── path_parts.py
│       └── text_workspace.py
├── 02-datetime/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── date_arithmetic.py
│       ├── duration_seconds.py
│       ├── parse_and_format.py
│       └── utc_conversion.py
├── 03-json/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── examples/
│       ├── decimal_decode.py
│       ├── deterministic_json.py
│       ├── reject_duplicate_keys.py
│       └── strict_numbers.py
└── 04-csv/
    ├── README.md
    ├── README.pt-BR.md
    ├── README.es.md
    └── examples/
        ├── dialect_round_trip.py
        ├── quote_none_escape.py
        ├── sniff_delimiter.py
        └── validate_dict_rows.py
```

Novos diretórios de capítulos serão adicionados conforme a fase avançar.
