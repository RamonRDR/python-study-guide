from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    notes_dir = workspace / "notes"
    notes_dir.mkdir()

    notes_path = notes_dir / "pathlib.txt"
    notes_path.write_text("Paths are objects.\n", encoding="utf-8")

    print(notes_path.read_text(encoding="utf-8").strip())
