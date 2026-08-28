import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    (workspace / "alpha.txt").write_text("alpha\n", encoding="utf-8")
    (workspace / "data").mkdir()
    (workspace / "data" / "values.txt").write_text("1\n2\n", encoding="utf-8")

    with os.scandir(workspace) as entries:
        for entry in sorted(entries, key=lambda item: item.name):
            kind = "dir" if entry.is_dir() else "file"
            print(f"{entry.name}: {kind}")
