from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one match in {path}, found {count}: {old[:80]!r}")
    file_path.write_text(text.replace(old, new), encoding="utf-8")


source = "practical-projects/06-file-organizer/file_organizer.py"
replace_once(
    source,
    '    """Immutable organization plan produced before filesystem mutation."""',
    '    """Immutable pathname-intent plan produced before filesystem mutation."""',
)
replace_once(
    source,
    '    """Build a deterministic, non-mutating plan for direct child files."""',
    '    """Build a deterministic, non-mutating pathname-intent plan."""',
)
replace_once(
    source,
    '    """Pin every source before category creation or source mutation."""',
    '    """Pin the current regular file at every planned pathname before mutation.\n\n    OrganizationPlan intentionally stores pathname/category intent, not live file\n    descriptors or a durable filesystem-object snapshot. Identity becomes strong\n    only when execute_plan opens each pathname and accepts fstat() on that pin.\n    """',
)
replace_once(
    source,
    '    """Execute a plan under the strongest explicitly supported platform contract."""',
    '    """Execute pathname intent under the strongest supported platform contract.\n\n    A plan does not freeze source-object identity between planning and execution.\n    The current regular file at each planned pathname is bound when execution\n    starts; changes after that binding are rejected under the platform contract.\n    """',
)

# Add a platform-neutral regression that makes the plan/execution identity boundary explicit.
test_path = "practical-projects/06-file-organizer/tests/test_file_organizer.py"
anchor = '''def test_execute_plan_preflights_missing_source_before_mutation(tmp_path: Path) -> None:\n    first = tmp_path / "a.txt"\n    second = tmp_path / "b.csv"\n    first.write_text("a", encoding="utf-8")\n    second.write_text("b", encoding="utf-8")\n    plan = plan_organization(tmp_path)\n    second.unlink()\n\n    with pytest.raises(FileNotFoundError):\n        execute_plan(plan)\n\n    assert first.exists()\n    assert not (tmp_path / "documents").exists()\n    assert not (tmp_path / "data").exists()\n\n\n'''
addition = anchor + '''def test_execute_plan_binds_current_source_at_execution_start(tmp_path: Path) -> None:\n    source = tmp_path / "notes.txt"\n    source.write_text("observed during planning", encoding="utf-8")\n    plan = plan_organization(tmp_path)\n\n    source.unlink()\n    source.write_text("current at execution start", encoding="utf-8")\n\n    result = execute_plan(plan)\n\n    destination = tmp_path / "documents" / "notes.txt"\n    assert result.moved_files == (destination,)\n    assert destination.read_text(encoding="utf-8") == "current at execution start"\n    assert not source.exists()\n\n\n'''
replace_once(test_path, anchor, addition)

# English contract wording.
readme = "practical-projects/06-file-organizer/README.md"
replace_once(readme, "14. capture planned-source filesystem identity;", "14. bind each source filesystem identity when execution begins, not during planning;")
replace_once(readme, "17. reject stale source, root, or category assumptions during execution;", "17. reject source changes after execution-time identity binding and reject stale root/category assumptions;")
replace_once(
    readme,
    "The plan is immutable. Creating it does not create directories and does not move files.",
    "The plan is immutable. Creating it does not create directories and does not move files. It records **pathname/category intent**, not an open descriptor or durable snapshot of the filesystem object behind each pathname. If a regular file is replaced at the same planned pathname before `execute_plan()` begins binding sources, the replacement is the current object selected by that pathname intent. Strong object identity starts at execution-time pinning.",
)
replace_once(
    readme,
    "The proposal exists as data before side effects begin, which makes review and testing easier.",
    "The proposal exists as data before side effects begin, which makes review and testing easier. This separation deliberately does **not** promise that a pathname still names the identical filesystem object observed during planning; retaining that guarantee would require keeping live source descriptors inside the plan. Execution instead binds the current regular object at each planned pathname before any category creation or source mutation.",
)
replace_once(
    readme,
    "During secure Linux execution, source identity is accepted **only after the source has been opened** with `O_NOFOLLOW | O_NONBLOCK` when `O_NONBLOCK` is available.",
    "Planning records pathname intent rather than source-object identity. Therefore a regular file replaced at the same pathname **before execution-time pinning** is accepted as the current object selected by the plan. During secure Linux execution, source identity is accepted **only after the current source has been opened** with `O_NOFOLLOW | O_NONBLOCK` when `O_NONBLOCK` is available.",
)
replace_once(readme, "3. open every planned source and accept identity from `fstat()` on that pinned descriptor", "3. open the current regular file at every planned pathname and accept identity from `fstat()` on that pinned descriptor")
replace_once(readme, "6. Linux: pin every planned source before accepting identity and before category mutation;", "6. Linux: bind the current regular file at every planned pathname by pinning it before accepting identity and before category mutation;")

# Portuguese contract wording.
readme = "practical-projects/06-file-organizer/README.pt-BR.md"
replace_once(readme, "14. capturar a identidade das origens planejadas;", "14. vincular a identidade de cada origem quando a execução começa, e não durante o planejamento;")
replace_once(readme, "17. rejeitar premissas obsoletas sobre origem, raiz ou categoria durante a execução;", "17. rejeitar mudanças da origem após o vínculo de identidade da execução e premissas obsoletas sobre raiz/categoria;")
replace_once(
    readme,
    "O plano é imutável. Criá-lo não cria diretórios e não move arquivos.",
    "O plano é imutável. Criá-lo não cria diretórios e não move arquivos. Ele registra **intenção de pathname/categoria**, e não um descriptor aberto ou snapshot durável do objeto de filesystem por trás de cada pathname. Se um arquivo regular for substituído no mesmo pathname planejado antes de `execute_plan()` começar a pinar as origens, a substituição é o objeto atual selecionado por essa intenção de pathname. A identidade forte do objeto começa no pinning da execução.",
)
replace_once(
    readme,
    "A proposta existe como dados antes de os efeitos colaterais começarem, facilitando revisão e testes.",
    "A proposta existe como dados antes de os efeitos colaterais começarem, facilitando revisão e testes. Essa separação deliberadamente **não** promete que um pathname ainda nomeie o mesmo objeto observado durante o planejamento; manter essa garantia exigiria descriptors de origem vivos dentro do plano. Em vez disso, a execução vincula o objeto regular atual em cada pathname planejado antes de criar categorias ou alterar origens.",
)
replace_once(
    readme,
    "Durante a execução segura no Linux, a identidade da origem só é aceita **depois que o arquivo já foi aberto** com `O_NOFOLLOW | O_NONBLOCK` quando `O_NONBLOCK` está disponível.",
    "O planejamento registra intenção de pathname, e não identidade do objeto de origem. Portanto, um arquivo regular substituído no mesmo pathname **antes do pinning da execução** é aceito como o objeto atual selecionado pelo plano. Durante a execução segura no Linux, a identidade da origem só é aceita **depois que o arquivo atual já foi aberto** com `O_NOFOLLOW | O_NONBLOCK` quando `O_NONBLOCK` está disponível.",
)
replace_once(readme, "3. abrir todas as origens planejadas e aceitar identidade pelo `fstat()` do descriptor pinado", "3. abrir o arquivo regular atual em cada pathname planejado e aceitar identidade pelo `fstat()` do descriptor pinado")
replace_once(readme, "6. Linux: pin every planned source before accepting identity and before category mutation;", "6. Linux: vincular o arquivo regular atual em cada pathname planejado, pinando-o antes de aceitar identidade e antes da mutação de categorias;") if False else None
# The Portuguese execution-flow sentence is localized differently; patch it only if present.
pt_text = Path(readme).read_text(encoding="utf-8")
old_pt = "6. Linux: pinar cada origem planejada antes de aceitar identidade e antes da mutação de categorias;"
if old_pt in pt_text:
    replace_once(readme, old_pt, "6. Linux: vincular o arquivo regular atual em cada pathname planejado, pinando-o antes de aceitar identidade e antes da mutação de categorias;")

# Spanish contract wording.
readme = "practical-projects/06-file-organizer/README.es.md"
replace_once(readme, "14. capturar la identidad de los orígenes planificados;", "14. vincular la identidad de cada origen cuando comienza la ejecución, no durante la planificación;")
replace_once(readme, "17. rechazar supuestos obsoletos sobre origen, raíz o categoría durante la ejecución;", "17. rechazar cambios del origen después del vínculo de identidad de ejecución y supuestos obsoletos sobre raíz/categoría;")
replace_once(
    readme,
    "El plan es inmutable. Crearlo no crea directorios ni mueve archivos.",
    "El plan es inmutable. Crearlo no crea directorios ni mueve archivos. Registra **intención de pathname/categoría**, no un descriptor abierto ni un snapshot duradero del objeto de filesystem detrás de cada pathname. Si un archivo regular se reemplaza en el mismo pathname planificado antes de que `execute_plan()` empiece a fijar los orígenes, el reemplazo es el objeto actual seleccionado por esa intención de pathname. La identidad fuerte del objeto comienza con el pinning de ejecución.",
)
replace_once(
    readme,
    "La propuesta existe como datos antes de que comiencen los efectos secundarios, lo que facilita revisión y pruebas.",
    "La propuesta existe como datos antes de que comiencen los efectos secundarios, lo que facilita revisión y pruebas. Esta separación deliberadamente **no** promete que un pathname siga nombrando el mismo objeto observado durante la planificación; conservar esa garantía exigiría mantener descriptores de origen vivos dentro del plan. En su lugar, la ejecución vincula el objeto regular actual en cada pathname planificado antes de crear categorías o mutar orígenes.",
)
replace_once(
    readme,
    "Durante la ejecución segura en Linux, la identidad del origen se acepta **solo después de abrir el archivo** con `O_NOFOLLOW | O_NONBLOCK` cuando `O_NONBLOCK` está disponible.",
    "La planificación registra intención de pathname y no identidad del objeto de origen. Por ello, un archivo regular reemplazado en el mismo pathname **antes del pinning de ejecución** se acepta como el objeto actual seleccionado por el plan. Durante la ejecución segura en Linux, la identidad del origen se acepta **solo después de abrir el archivo actual** con `O_NOFOLLOW | O_NONBLOCK` cuando `O_NONBLOCK` está disponible.",
)
replace_once(readme, "3. abrir todos los orígenes planificados y aceptar identidad mediante `fstat()` del descriptor fijado", "3. abrir el archivo regular actual en cada pathname planificado y aceptar identidad mediante `fstat()` del descriptor fijado")
es_text = Path(readme).read_text(encoding="utf-8")
old_es = "6. Linux: fijar cada origen planificado antes de aceptar identidad y antes de mutar categorías;"
if old_es in es_text:
    replace_once(readme, old_es, "6. Linux: vincular el archivo regular actual en cada pathname planificado, fijándolo antes de aceptar identidad y antes de mutar categorías;")

# Revert unrelated Spanish roadmap rewrites while keeping Project 06 additions.
es = "docs/roadmap.es.md"
replace_once(es, "Los ejemplos ejecutables usan el contrato declarado en [`requirements-external.txt`](../requirements-external.txt).", "Los ejemplos ejecutables de bibliotecas externas usan el contrato declarado en [`requirements-external.txt`](../requirements-external.txt).")
replace_once(es, "- [x] [Analizador CSV](../practical-projects/04-csv-analyzer/README.es.md)", "- [x] [Analizador de CSV](../practical-projects/04-csv-analyzer/README.es.md)")
replace_once(
    es,
    "El Proyecto 01 establece el contrato de la Fase 10 con requisitos explícitos, modelado de datos validado, dinero exacto con `Decimal`, persistencia, demostración determinista, cobertura automatizada con pytest, desafíos de extensión y discusión de portafolio. El Proyecto 02 extiende el contrato con reglas configurables de calificación, agregación ponderada exacta, informes parcial/final explícitos y validación centrada en límites. El Proyecto 03 añade datos de identidad canónicos, normalización Unicode e IDNA, prevención de duplicados, índices secundarios de lookup, actualizaciones seguras de campos indexados, transiciones explícitas del ciclo de vida y cobertura pytest centrada en mutación sin introducir autenticación. El Proyecto 04 añade schemas CSV estrictos, conversión tipada, manejo de fallos estructurales frente a fallos por fila, parsing con éxito parcial, identificadores aceptados duplicados, agregación determinista y filtrado usando mecanismos CSV de la biblioteca estándar de forma explícita. El Proyecto 05 añade ventanas inclusivas de fechas, validación de identidad de origen, métricas de resumen exactas y deterministas, construcción inmutable de informes, renderización TXT/Markdown, escape específico del formato y salida UTF-8. El Proyecto 06 añade descubrimiento superficial determinista, planificación inmutable, categorías por sufijo, políticas explícitas de colisión, fronteras de symlink, identidad `(device, inode)`, anclaje de descriptors de raíz/categorías, nombres de staging acotados y commits atómicos no-replace sensibles a la plataforma con `renameat2(RENAME_NOREPLACE)` en Linux.",
    "El Proyecto 01 establece el contrato de la Fase 10 con requisitos explícitos, modelado de datos validado, dinero exacto con `Decimal`, persistencia, demostración determinista, cobertura automatizada con pytest, desafíos de ampliación y discusión de portafolio. El Proyecto 02 amplía el contrato con reglas de calificación configurables, agregación ponderada exacta, informe parcial/final explícito y validación centrada en límites. El Proyecto 03 añade datos de identidad canónicos, normalización Unicode e IDNA, prevención de duplicados, índices secundarios, actualizaciones seguras y transiciones explícitas del ciclo de vida sin introducir autenticación. El Proyecto 04 añade schemas CSV estrictos, conversión tipada, separación entre fallos estructurales y fallos de fila, parsing con éxito parcial, identificadores aceptados duplicados, agregación determinista y filtros con la mecánica de la biblioteca estándar expuesta explícitamente. El Proyecto 05 añade ventanas inclusivas explícitas de fechas, validación de identidad del origen, métricas exactas y deterministas de resumen, construcción inmutable del informe, renderización TXT/Markdown, escape específico del formato y escritura UTF-8. El Proyecto 06 añade descubrimiento superficial determinista, planificación inmutable, categorías por sufijo, políticas explícitas de colisión, fronteras de symlink, identidad `(device, inode)`, anclaje de descriptors de raíz/categorías, nombres de staging acotados y commits atómicos no-replace sensibles a la plataforma con `renameat2(RENAME_NOREPLACE)` en Linux.",
)
replace_once(es, "- cobertura automatizada para comportamientos importantes;", "- cobertura automatizada del comportamiento importante;")
replace_once(es, "- desafíos de extensión;", "- desafíos de ampliación;")
replace_once(es, "## Gates continuos de calidad", "## Criterios continuos de calidad")
replace_once(es, "- datos seguros para privacidad;", "- datos seguros desde el punto de vista de la privacidad;")
replace_once(es, "- ejemplos Python ejecutables cuando corresponda;", "- ejemplos ejecutables de Python cuando corresponda;")
replace_once(es, "- integridad de navegación interna;", "- integridad de la navegación interna;")
replace_once(es, "- supuestos honestos sobre dependencias y versiones.", "- transparencia sobre dependencias y supuestos de versión.")
replace_once(es, "El roadmap evolucionará a medida que crezca el proyecto, pero los cambios deben preservar la progresión desde conceptos iniciales hasta trabajo práctico integrado.", "El roadmap evolucionará a medida que el proyecto crezca, pero los cambios deben preservar la progresión desde los conceptos iniciales hasta el trabajo práctico integrado.")

# Revert unrelated Portuguese roadmap rewrites while keeping Project 06 additions.
pt = "docs/roadmap.pt-BR.md"
replace_once(pt, "O Capítulo 09 encerra a fase conectando essas bases a estado do ambiente do processo, interfaces path-like, varredura e travessia de diretórios, metadados, cópia, movimento, remoção recursiva, capacidades de plataforma e segurança de archives.", "O Capítulo 09 encerra a fase conectando essas bases ao estado do ambiente do processo, interfaces path-like, varredura e travessia de diretórios, metadados, cópia, movimentação, exclusão recursiva, capacidades de plataforma e segurança de archives.")
replace_once(pt, "Os exemplos executáveis usam o contrato declarado em [`requirements-external.txt`](../requirements-external.txt).", "Os exemplos executáveis de bibliotecas externas usam o contrato declarado em [`requirements-external.txt`](../requirements-external.txt).")
replace_once(pt, "- [x] [Analisador CSV](../practical-projects/04-csv-analyzer/README.pt-BR.md)", "- [x] [Analisador de CSV](../practical-projects/04-csv-analyzer/README.pt-BR.md)")
replace_once(
    pt,
    "O Projeto 01 estabelece o contrato da Fase 10 com requisitos explícitos, modelagem de dados validada, dinheiro exato com `Decimal`, persistência, demonstração determinística, cobertura automatizada com pytest, desafios de extensão e discussão de portfólio. O Projeto 02 estende o contrato com regras configuráveis de notas, agregação ponderada exata, relatórios parcial/final explícitos e validação focada em fronteiras. O Projeto 03 adiciona dados de identidade canônicos, normalização Unicode e IDNA, prevenção de duplicidade, índices secundários de lookup, atualizações seguras de campos indexados, transições explícitas de ciclo de vida e cobertura pytest focada em mutação sem introduzir autenticação. O Projeto 04 adiciona schemas CSV estritos, conversão tipada, tratamento de falhas estruturais versus falhas por linha, parsing com sucesso parcial, identificadores aceitos duplicados, agregação determinística e filtragem usando mecanismos CSV da biblioteca padrão de forma explícita. O Projeto 05 adiciona janelas inclusivas de datas, validação de identidade de origem, métricas de resumo exatas e determinísticas, construção imutável de relatórios, renderização TXT/Markdown, escape específico do formato e saída UTF-8. O Projeto 06 adiciona descoberta rasa determinística, planejamento imutável, categorias por sufixo, políticas explícitas de colisão, fronteiras de symlink, identidade `(device, inode)`, ancoragem de descriptors de raiz/categorias, nomes de staging limitados e commits atômicos no-replace sensíveis à plataforma com `renameat2(RENAME_NOREPLACE)` no Linux.",
    "O Projeto 01 estabelece o contrato da Fase 10 com requisitos explícitos, modelagem de dados validada, dinheiro exato com `Decimal`, persistência, demonstração determinística, cobertura automatizada com pytest, desafios de extensão e discussão de portfólio. O Projeto 02 amplia o contrato com regras de notas configuráveis, agregação ponderada exata, relatório parcial/final explícito e validação focada em fronteiras. O Projeto 03 adiciona dados de identidade canônicos, normalização Unicode e IDNA, prevenção de duplicidade, índices secundários, atualizações seguras e transições explícitas de ciclo de vida sem introduzir autenticação. O Projeto 04 adiciona schemas CSV rígidos, conversão tipada, separação entre falhas estruturais e falhas de linha, parsing com sucesso parcial, identificadores aceitos duplicados, agregação determinística e filtros com a mecânica da biblioteca padrão exposta explicitamente. O Projeto 05 adiciona janelas inclusivas explícitas de datas, validação da identidade da origem, métricas exatas e determinísticas de resumo, construção imutável do relatório, renderização TXT/Markdown, escape específico do formato e escrita UTF-8. O Projeto 06 adiciona descoberta rasa determinística, planejamento imutável, categorias por sufixo, políticas explícitas de colisão, fronteiras de symlink, identidade `(device, inode)`, ancoragem de descriptors de raiz/categorias, nomes de staging limitados e commits atômicos no-replace sensíveis à plataforma com `renameat2(RENAME_NOREPLACE)` no Linux.",
)
replace_once(pt, "- cobertura automatizada para comportamentos importantes;", "- cobertura automatizada dos comportamentos importantes;")
replace_once(pt, "## Gates contínuos de qualidade", "## Critérios contínuos de qualidade")
replace_once(pt, "- dados seguros para privacidade;", "- dados seguros do ponto de vista de privacidade;")
replace_once(pt, "- integridade de navegação interna;", "- integridade da navegação interna;")
replace_once(pt, "- atenção ao PEP 8;", "- atenção à PEP 8;")
replace_once(pt, "- premissas honestas sobre dependências e versões.", "- transparência sobre dependências e pressupostos de versão.")
replace_once(pt, "O roadmap evoluirá conforme o projeto crescer, mas as mudanças devem preservar a progressão de conceitos iniciantes para trabalho prático integrado.", "O roadmap evoluirá à medida que o projeto crescer, mas as mudanças devem preservar a progressão dos conceitos iniciais até o trabalho prático integrado.")

print("Applied Review 11 contract and roadmap-scope fixes.")
