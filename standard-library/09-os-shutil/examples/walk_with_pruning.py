import os
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    (workspace / "src").mkdir()
    (workspace / "src" / "app.py").write_text("print('ready')\n", encoding="utf-8")
    (workspace / "cache").mkdir()
    (workspace / "cache" / "ignored.bin").write_bytes(b"ignored")

    for root, dirnames, filenames in os.walk(workspace, topdown=True):
        dirnames[:] = sorted(name for name in dirnames if name != "cache")
        filenames.sort()

        relative_root = Path(root).relative_to(workspace)
        label = "." if relative_root == Path(".") else relative_root.as_posix()
        print(f"{label}: {filenames}")
