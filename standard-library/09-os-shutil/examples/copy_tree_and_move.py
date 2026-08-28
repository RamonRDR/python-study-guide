import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    source = workspace / "source"
    destination = workspace / "backup"
    archive = workspace / "archive"

    (source / "reports").mkdir(parents=True)
    (source / "reports" / "summary.txt").write_text("ready\n", encoding="utf-8")
    (source / "scratch.tmp").write_text("temporary\n", encoding="utf-8")

    shutil.copytree(source, destination, ignore=shutil.ignore_patterns("*.tmp"))
    archive.mkdir()
    moved_path = Path(shutil.move(destination / "reports" / "summary.txt", archive))

    copied_names = sorted(path.name for path in destination.iterdir())
    print(f"backup entries: {copied_names}")
    print(f"moved file: {moved_path.name}")
    print(f"content: {moved_path.read_text(encoding='utf-8').strip()}")
