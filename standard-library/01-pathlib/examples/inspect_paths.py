from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    workspace = Path(temp_dir)
    file_path = workspace / "lesson.txt"
    file_path.write_text("pathlib", encoding="utf-8")

    print(f"File exists: {file_path.exists()}")
    print(f"Is file: {file_path.is_file()}")
    print(f"Workspace is directory: {workspace.is_dir()}")
