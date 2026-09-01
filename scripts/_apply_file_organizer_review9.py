from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one patch anchor in {path}, found {count}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


IMPLEMENTATION = "practical-projects/06-file-organizer/file_organizer.py"
TESTS = "practical-projects/06-file-organizer/tests/test_file_organizer.py"

validation_old = '''def _validate_category_locations(source_directory: Path) -> None:\n    for category in FileCategory:\n        target = source_directory / category.value\n        if target.is_symlink():\n            raise ValueError(f"category directory cannot be a symlink: {target.name}")\n        if target.exists() and not target.is_dir():\n            raise NotADirectoryError(\n                f"category path exists but is not a directory: {target.name}"\n            )\n'''
validation_new = '''def _is_directory_redirect(path: Path) -> bool:\n    """Return whether a directory entry redirects traversal to another location."""\n    if path.is_symlink():\n        return True\n    is_junction = getattr(path, "is_junction", None)\n    return bool(is_junction is not None and is_junction())\n\n\ndef _validate_category_locations(source_directory: Path) -> None:\n    for category in FileCategory:\n        target = source_directory / category.value\n        if _is_directory_redirect(target):\n            raise ValueError(\n                f"category directory cannot be a symlink or junction: {target.name}"\n            )\n        if target.exists() and not target.is_dir():\n            raise NotADirectoryError(\n                f"category path exists but is not a directory: {target.name}"\n            )\n'''
replace_once(IMPLEMENTATION, validation_old, validation_new)

portable_old = '''        directory.mkdir(exist_ok=True)\n        if directory.is_symlink() or not directory.is_dir():\n            raise ValueError(\n                f"category directory became unsafe during execution: {directory.name}"\n            )\n\n    moved: list[Path] = []\n    for action in plan.actions:\n        if action.destination.parent.is_symlink():\n            raise ValueError(\n                "category directory became unsafe during execution: "\n                f"{action.destination.parent.name}"\n            )\n'''
portable_new = '''        directory.mkdir(exist_ok=True)\n        if _is_directory_redirect(directory) or not directory.is_dir():\n            raise ValueError(\n                f"category directory became unsafe during execution: {directory.name}"\n            )\n\n    moved: list[Path] = []\n    for action in plan.actions:\n        if _is_directory_redirect(action.destination.parent):\n            raise ValueError(\n                "category directory became unsafe during execution: "\n                f"{action.destination.parent.name}"\n            )\n'''
replace_once(IMPLEMENTATION, portable_old, portable_new)

import_old = '''from pathlib import Path\n\nimport pytest\n\nfrom file_organizer import (\n'''
import_new = '''from pathlib import Path\n\nimport pytest\n\nimport file_organizer\nfrom file_organizer import (\n'''
replace_once(TESTS, import_old, import_new)

test_anchor = '''def test_plan_empty_directory_is_valid(tmp_path: Path) -> None:\n'''
tests_new = '''def test_plan_organization_rejects_category_directory_junction(\n    monkeypatch: pytest.MonkeyPatch,\n    tmp_path: Path,\n) -> None:\n    source = tmp_path / "notes.txt"\n    source.write_text("x", encoding="utf-8")\n    documents = tmp_path / "documents"\n    documents.mkdir()\n    original_is_junction = getattr(Path, "is_junction", lambda self: False)\n\n    def fake_is_junction(path: Path) -> bool:\n        return path == documents or original_is_junction(path)\n\n    monkeypatch.setattr(Path, "is_junction", fake_is_junction, raising=False)\n\n    with pytest.raises(ValueError, match="symlink or junction"):\n        plan_organization(tmp_path)\n\n    assert source.read_text(encoding="utf-8") == "x"\n\n\ndef test_windows_portable_execution_rejects_late_category_junction(\n    monkeypatch: pytest.MonkeyPatch,\n    tmp_path: Path,\n) -> None:\n    source = tmp_path / "notes.txt"\n    source.write_text("planned", encoding="utf-8")\n    plan = plan_organization(tmp_path)\n    documents = tmp_path / "documents"\n    identities = {source.resolve(): file_organizer._capture_path_identity(source.resolve())}\n    original_is_junction = getattr(Path, "is_junction", lambda self: False)\n\n    def fake_is_junction(path: Path) -> bool:\n        return path == documents or original_is_junction(path)\n\n    monkeypatch.setattr(Path, "is_junction", fake_is_junction, raising=False)\n    monkeypatch.setattr(file_organizer.os, "name", "nt")\n\n    with pytest.raises(ValueError, match="category directory became unsafe"):\n        file_organizer._execute_plan_portable(plan, identities)\n\n    assert source.read_text(encoding="utf-8") == "planned"\n    assert not (documents / "notes.txt").exists()\n\n\n'''
replace_once(TESTS, test_anchor, tests_new + test_anchor)

DOC_UPDATES = {
    "practical-projects/06-file-organizer/README.md": (
        "The organizer does not follow direct-child symlinks. It also rejects a source directory or category folder that is a symlink.\n",
        "The organizer does not follow direct-child symlinks. It also rejects a source directory or category folder that is a symlink. On Windows, category folders that are NTFS junctions are rejected too: `is_dir()` follows a junction, so accepting one could redirect a planned move outside the workspace.\n",
    ),
    "practical-projects/06-file-organizer/README.pt-BR.md": (
        "O organizador não segue symlinks filhos diretos. Também rejeita diretório de origem ou pasta de categoria que seja symlink.\n",
        "O organizador não segue symlinks filhos diretos. Também rejeita diretório de origem ou pasta de categoria que seja symlink. No Windows, pastas de categoria que sejam junctions NTFS também são rejeitadas: `is_dir()` segue um junction, então aceitá-lo poderia redirecionar uma movimentação planejada para fora do workspace.\n",
    ),
    "practical-projects/06-file-organizer/README.es.md": (
        "El organizador no sigue symlinks hijos directos. También rechaza un directorio de origen o carpeta de categoría que sea symlink.\n",
        "El organizador no sigue symlinks hijos directos. También rechaza un directorio de origen o carpeta de categoría que sea symlink. En Windows, las carpetas de categoría que sean junctions NTFS también se rechazan: `is_dir()` sigue un junction, por lo que aceptarlo podría redirigir un movimiento planificado fuera del workspace.\n",
    ),
}
for path, (old, new) in DOC_UPDATES.items():
    replace_once(path, old, new)
