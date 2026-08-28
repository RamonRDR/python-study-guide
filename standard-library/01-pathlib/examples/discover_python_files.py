from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source_dir = workspace / "src"
    tools_dir = source_dir / "tools"
    tools_dir.mkdir(parents=True)

    (source_dir / "app.py").write_text("print('app')\n", encoding="utf-8")
    (tools_dir / "helper.py").write_text("VALUE = 1\n", encoding="utf-8")
    (tools_dir / "notes.txt").write_text("notes\n", encoding="utf-8")

    for path in sorted(source_dir.rglob("*.py")):
        print(path.relative_to(workspace))
