from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected exactly one match, found {count}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def replace_line_prefix(path: str, prefix: str, replacement: str) -> None:
    target = Path(path)
    lines = target.read_text(encoding="utf-8").splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"{path}: expected one line starting {prefix!r}, found {len(matches)}")
    lines[matches[0]] = replacement
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


replace_once(
    "practical-projects/README.md",
    "2. ⏳ Grade Calculator",
    "2. ✅ [Grade Calculator](02-grade-calculator/README.md)",
)
replace_once(
    "practical-projects/README.md",
    "Project 01 establishes the pattern with validated monetary records, exact `Decimal` arithmetic, JSON persistence, CSV export, and a pytest suite.",
    "Project 01 establishes the integration pattern with validated monetary records and persistence. Project 02 extends it with configurable grading policies, exact weighted aggregation, explicit partial/final states, structured reporting, and boundary-focused pytest coverage.",
)
replace_once(
    "practical-projects/README.pt-BR.md",
    "2. ⏳ Calculadora de Notas",
    "2. ✅ [Calculadora de Notas](02-grade-calculator/README.pt-BR.md)",
)
replace_once(
    "practical-projects/README.pt-BR.md",
    "O Projeto 01 estabelece o padrão com registros monetários validados, aritmética exata com `Decimal`, persistência JSON, exportação CSV e uma suíte pytest.",
    "O Projeto 01 estabelece o padrão de integração com registros monetários validados e persistência. O Projeto 02 amplia esse padrão com políticas de notas configuráveis, agregação ponderada exata, estados parcial/final explícitos, relatório estruturado e cobertura pytest focada em fronteiras.",
)
replace_once(
    "practical-projects/README.es.md",
    "2. ⏳ Calculadora de Notas",
    "2. ✅ [Calculadora de Notas](02-grade-calculator/README.es.md)",
)
replace_once(
    "practical-projects/README.es.md",
    "El Proyecto 01 establece el patrón con registros monetarios validados, aritmética exacta con `Decimal`, persistencia JSON, exportación CSV y una suite pytest.",
    "El Proyecto 01 establece el patrón de integración con registros monetarios validados y persistencia. El Proyecto 02 amplía ese patrón con políticas de calificación configurables, agregación ponderada exacta, estados parcial/final explícitos, informe estructurado y cobertura pytest centrada en límites.",
)

replace_once(
    "docs/learning-path.en.md",
    "2. ⏳ Grade Calculator",
    "2. ✅ [Grade Calculator](../practical-projects/02-grade-calculator/README.md)",
)
replace_once(
    "docs/learning-path.en.md",
    "Phase 10 is in progress. Project 01 integrates validated data modeling, exact `Decimal` money, collections, JSON persistence, CSV export, deterministic temporary-file handling, and automated pytest coverage into one complete workflow.",
    "Phase 10 is in progress. Project 01 integrates validated data modeling, exact `Decimal` money, collections, JSON persistence, CSV export, deterministic temporary-file handling, and automated pytest coverage. Project 02 adds configurable grade policies, exact weighted aggregation, explicit progress-versus-final state, structured reporting, and boundary-focused tests.",
)
replace_once(
    "docs/learning-path.pt-BR.md",
    "2. ⏳ Calculadora de Notas",
    "2. ✅ [Calculadora de Notas](../practical-projects/02-grade-calculator/README.pt-BR.md)",
)
replace_once(
    "docs/learning-path.pt-BR.md",
    "A Fase 10 está em andamento. O Projeto 01 integra modelagem de dados validada, dinheiro exato com `Decimal`, coleções, persistência JSON, exportação CSV, manipulação determinística de arquivos temporários e cobertura automatizada com pytest em um fluxo completo.",
    "A Fase 10 está em andamento. O Projeto 01 integra modelagem de dados validada, dinheiro exato com `Decimal`, coleções, persistência JSON, exportação CSV, manipulação determinística de arquivos temporários e cobertura automatizada com pytest. O Projeto 02 adiciona políticas de notas configuráveis, agregação ponderada exata, estado de progresso versus final explícito, relatório estruturado e testes focados em fronteiras.",
)
replace_once(
    "docs/learning-path.es.md",
    "2. ⏳ Calculadora de Notas",
    "2. ✅ [Calculadora de Notas](../practical-projects/02-grade-calculator/README.es.md)",
)
replace_once(
    "docs/learning-path.es.md",
    "La Fase 10 está en progreso. El Proyecto 01 integra modelado de datos validado, dinero exacto con `Decimal`, colecciones, persistencia JSON, exportación CSV, manejo determinista de archivos temporales y cobertura automatizada con pytest en un flujo completo.",
    "La Fase 10 está en progreso. El Proyecto 01 integra modelado de datos validado, dinero exacto con `Decimal`, colecciones, persistencia JSON, exportación CSV, manejo determinista de archivos temporales y cobertura automatizada con pytest. El Proyecto 02 añade políticas de calificación configurables, agregación ponderada exacta, estado de progreso frente a final explícito, informe estructurado y pruebas centradas en límites.",
)

replace_once(
    "docs/roadmap.en.md",
    "- [ ] Grade Calculator",
    "- [x] [Grade Calculator](../practical-projects/02-grade-calculator/README.md)",
)
replace_once(
    "docs/roadmap.en.md",
    "Project 01 establishes the Phase 10 contract with explicit requirements, validated data modeling, exact `Decimal` money, JSON persistence, CSV export, deterministic demonstration, automated pytest coverage, extension challenges, and portfolio discussion.",
    "Project 01 establishes the Phase 10 contract with explicit requirements, validated data modeling, exact `Decimal` money, persistence, deterministic demonstration, automated pytest coverage, extension challenges, and portfolio discussion. Project 02 extends the contract with configurable grading rules, exact weighted aggregation, explicit partial/final reporting, and boundary-focused validation.",
)
replace_once(
    "docs/roadmap.pt-BR.md",
    "- [ ] Calculadora de Notas",
    "- [x] [Calculadora de Notas](../practical-projects/02-grade-calculator/README.pt-BR.md)",
)
replace_once(
    "docs/roadmap.pt-BR.md",
    "O Projeto 01 estabelece o contrato da Fase 10 com requisitos explícitos, modelagem de dados validada, dinheiro exato com `Decimal`, persistência JSON, exportação CSV, demonstração determinística, cobertura automatizada com pytest, desafios de extensão e discussão de portfólio.",
    "O Projeto 01 estabelece o contrato da Fase 10 com requisitos explícitos, modelagem de dados validada, dinheiro exato com `Decimal`, persistência, demonstração determinística, cobertura automatizada com pytest, desafios de extensão e discussão de portfólio. O Projeto 02 amplia o contrato com regras de notas configuráveis, agregação ponderada exata, relatório parcial/final explícito e validação focada em fronteiras.",
)
replace_once(
    "docs/roadmap.es.md",
    "- [ ] Calculadora de Notas",
    "- [x] [Calculadora de Notas](../practical-projects/02-grade-calculator/README.es.md)",
)
replace_once(
    "docs/roadmap.es.md",
    "El Proyecto 01 establece el contrato de la Fase 10 con requisitos explícitos, modelado de datos validado, dinero exacto con `Decimal`, persistencia JSON, exportación CSV, demostración determinista, cobertura automatizada con pytest, desafíos de ampliación y discusión de portafolio.",
    "El Proyecto 01 establece el contrato de la Fase 10 con requisitos explícitos, modelado de datos validado, dinero exacto con `Decimal`, persistencia, demostración determinista, cobertura automatizada con pytest, desafíos de ampliación y discusión de portafolio. El Proyecto 02 amplía el contrato con reglas de calificación configurables, agregación ponderada exacta, informe parcial/final explícito y validación centrada en límites.",
)

old_tree = """├── practical-projects/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   └── 01-expense-tracker/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       ├── demo.py
│       ├── expense_tracker.py
│       └── tests/
│           ├── conftest.py
│           └── test_expense_tracker.py
"""
new_tree = """├── practical-projects/
│   ├── README.md
│   ├── README.pt-BR.md
│   ├── README.es.md
│   ├── 01-expense-tracker/
│   │   ├── README.md
│   │   ├── README.pt-BR.md
│   │   ├── README.es.md
│   │   ├── demo.py
│   │   ├── expense_tracker.py
│   │   └── tests/
│   │       ├── conftest.py
│   │       └── test_expense_tracker.py
│   └── 02-grade-calculator/
│       ├── README.md
│       ├── README.pt-BR.md
│       ├── README.es.md
│       ├── demo.py
│       ├── grade_calculator.py
│       └── tests/
│           ├── conftest.py
│           └── test_grade_calculator.py
"""
for path in (
    "docs/project-structure.en.md",
    "docs/project-structure.pt-BR.md",
    "docs/project-structure.es.md",
):
    replace_once(path, old_tree, new_tree)

replace_line_prefix(
    "docs/project-structure.en.md",
    "- `practical-projects/`:",
    "- `practical-projects/`: Phase 10 practical-project workspace. Project 01, Expense Tracker, integrates validated monetary data, persistence, a deterministic demo, and pytest coverage. Project 02, Grade Calculator, adds configurable grading policies, exact weighted aggregation, explicit progress/final reporting, and boundary-focused tests.",
)
replace_line_prefix(
    "docs/project-structure.pt-BR.md",
    "- `practical-projects/`:",
    "- `practical-projects/`: espaço de Projetos Práticos da Fase 10. O Projeto 01, Controle de Despesas, integra dados monetários validados, persistência, demonstração determinística e cobertura pytest. O Projeto 02, Calculadora de Notas, adiciona políticas de notas configuráveis, agregação ponderada exata, relatório de progresso/final explícito e testes focados em fronteiras.",
)
replace_line_prefix(
    "docs/project-structure.es.md",
    "- `practical-projects/`:",
    "- `practical-projects/`: espacio de Proyectos Prácticos de la Fase 10. El Proyecto 01, Control de Gastos, integra datos monetarios validados, persistencia, demostración determinista y cobertura pytest. El Proyecto 02, Calculadora de Notas, añade políticas de calificación configurables, agregación ponderada exacta, informe de progreso/final explícito y pruebas centradas en límites.",
)

manifest = Path("scripts/example_manifest.txt")
manifest_text = manifest.read_text(encoding="utf-8")
new_demo = "practical-projects/02-grade-calculator/demo.py"
if new_demo in manifest_text:
    raise RuntimeError("Grade Calculator demo is already registered")
old_demo = "practical-projects/01-expense-tracker/demo.py"
if manifest_text.count(old_demo) != 1:
    raise RuntimeError("Expense Tracker demo manifest anchor not found exactly once")
manifest.write_text(
    manifest_text.replace(old_demo, f"{old_demo}\n{new_demo}", 1),
    encoding="utf-8",
)
