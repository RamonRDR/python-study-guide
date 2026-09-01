from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "practical-projects/06-file-organizer/file_organizer.py"
TESTS = ROOT / "practical-projects/06-file-organizer/tests/test_atomic_move.py"
READMES = {
    ROOT / "practical-projects/06-file-organizer/README.md": (
        "If it does, execution may hard-link that proven stage back to the original source name. If the stage is missing or has been replaced, execution leaves the uncertain stage untouched and, before closing the still-pinned source file descriptor, copies the planned source bytes into an exclusive `.fo-recovery-*` regular file.",
        "If it does, execution may attempt a no-replace hard link from that proven stage back to the original source name, but restoration is accepted only after the recreated source pathname itself is re-read and verified to have the pinned identity. If the link fails, races to a different object, leaves the source name missing, or the post-link source identity does not match, execution leaves uncertain entries untouched and, before closing the still-pinned source file descriptor, copies the planned source bytes into an exclusive `.fo-recovery-*` regular file."
    ),
    ROOT / "practical-projects/06-file-organizer/README.pt-BR.md": (
        "Se corresponder, a execução pode recriar o nome original por hard link a partir desse staging comprovado. Se o staging sumiu ou foi substituído, a execução deixa a entrada incerta intacta e, antes de fechar o descritor ainda pinado da origem, copia os bytes planejados para um arquivo regular exclusivo `.fo-recovery-*`.",
        "Se corresponder, a execução pode tentar recriar o nome original por hard link no-replace a partir desse staging comprovado, mas a restauração só é aceita depois que o próprio pathname recriado da origem é relido e verificado com a identidade pinada. Se o link falhar, sofrer corrida para outro objeto, deixar o nome de origem ausente ou a identidade pós-link não corresponder, a execução deixa entradas incertas intactas e, antes de fechar o descritor ainda pinado da origem, copia os bytes planejados para um arquivo regular exclusivo `.fo-recovery-*`."
    ),
    ROOT / "practical-projects/06-file-organizer/README.es.md": (
        "Si coincide, la ejecución puede recrear el nombre original mediante un hard link desde ese staging comprobado. Si el staging desapareció o fue reemplazado, la ejecución deja intacta la entrada incierta y, antes de cerrar el descriptor todavía fijado del origen, copia los bytes planificados a un archivo regular exclusivo `.fo-recovery-*`.",
        "Si coincide, la ejecución puede intentar recrear el nombre original mediante un hard link no-replace desde ese staging comprobado, pero la restauración solo se acepta después de volver a leer el propio pathname recreado del origen y verificar que conserva la identidad fijada. Si el link falla, sufre una carrera hacia otro objeto, deja ausente el nombre de origen o la identidad posterior al link no coincide, la ejecución deja intactas las entradas inciertas y, antes de cerrar el descriptor todavía fijado del origen, copia los bytes planificados a un archivo regular exclusivo `.fo-recovery-*`."
    ),
}


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"expected exactly one anchor in {path}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


code = CODE.read_text(encoding="utf-8")
old_code = '''def _preserve_stage_at(stage_name: str, source_name: str, *, root_fd: int) -> None:\n    \"\"\"Best-effort restore by linking only; never delete a raced staging entry.\"\"\"\n    try:\n        os.link(\n            stage_name,\n            source_name,\n            src_dir_fd=root_fd,\n            dst_dir_fd=root_fd,\n            follow_symlinks=False,\n        )\n    except OSError:\n        pass\n'''
new_code = '''def _preserve_stage_at(\n    stage_name: str,\n    source_name: str,\n    *,\n    root_fd: int,\n    expected_identity: _FileIdentity | None = None,\n) -> bool:\n    \"\"\"Best-effort restore without deleting raced entries; optionally prove result.\"\"\"\n    try:\n        os.link(\n            stage_name,\n            source_name,\n            src_dir_fd=root_fd,\n            dst_dir_fd=root_fd,\n            follow_symlinks=False,\n        )\n    except OSError:\n        pass\n\n    if expected_identity is None:\n        return False\n\n    try:\n        restored_identity = _regular_identity_at(\n            source_name,\n            directory_fd=root_fd,\n        )\n    except OSError:\n        return False\n    return restored_identity == expected_identity\n'''
if code.count(old_code) != 1:
    raise RuntimeError("preserve-stage helper anchor not found exactly once")
code = code.replace(old_code, new_code, 1)
old_branch = '''    if staged_identity == expected_identity:\n        _preserve_stage_at(stage_name, source_name, root_fd=root_fd)\n        return None\n\n    return _recover_pinned_source_at(\n'''
new_branch = '''    if staged_identity == expected_identity:\n        restored = _preserve_stage_at(\n            stage_name,\n            source_name,\n            root_fd=root_fd,\n            expected_identity=expected_identity,\n        )\n        if restored:\n            return None\n\n    return _recover_pinned_source_at(\n'''
if code.count(old_branch) != 1:
    raise RuntimeError("post-claim recovery branch anchor not found exactly once")
code = code.replace(old_branch, new_branch, 1)
CODE.write_text(code, encoding="utf-8")

for path, (old, new) in READMES.items():
    replace_once(path, old, new)


tests = TESTS.read_text(encoding="utf-8")
anchor = '''def test_failed_final_rename_after_stage_replacement_recovers_pinned_source_data(\n'''
if tests.count(anchor) != 1:
    raise RuntimeError("test insertion anchor not found exactly once")
new_test = r'''

def test_failed_final_rename_stage_changes_during_restore_recovers_pinned_source_data(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)
    destination = tmp_path / "documents" / "notes.txt"
    original_rename_no_replace = file_organizer._rename_no_replace_at
    original_link = os.link
    final_rename_failed = False
    restore_raced = False

    def failing_final_rename(
        source_name: str,
        destination_name: str,
        *,
        source_directory_fd: int,
        destination_directory_fd: int,
    ) -> None:
        nonlocal final_rename_failed
        if source_name.startswith(".fo-stage-") and not final_rename_failed:
            final_rename_failed = True
            destination.write_text("late destination", encoding="utf-8")
        original_rename_no_replace(
            source_name,
            destination_name,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
        )

    def racing_link(
        src: str | os.PathLike[str],
        dst: str | os.PathLike[str],
        *,
        src_dir_fd: int | None = None,
        dst_dir_fd: int | None = None,
        follow_symlinks: bool = True,
    ) -> None:
        nonlocal restore_raced
        if (
            os.fspath(src).startswith(".fo-stage-")
            and os.fspath(dst) == source.name
            and src_dir_fd is not None
            and dst_dir_fd is not None
            and not restore_raced
        ):
            restore_raced = True
            stage = tmp_path / os.fspath(src)
            stage.unlink()
            stage.write_text("third-party stage", encoding="utf-8")
        original_link(
            src,
            dst,
            src_dir_fd=src_dir_fd,
            dst_dir_fd=dst_dir_fd,
            follow_symlinks=follow_symlinks,
        )

    monkeypatch.setattr(file_organizer, "_rename_no_replace_at", failing_final_rename)
    monkeypatch.setattr(file_organizer.os, "link", racing_link)

    with pytest.raises(FileExistsError, match="destination appeared during execution"):
        execute_plan(plan)

    assert final_rename_failed
    assert restore_raced
    assert destination.read_text(encoding="utf-8") == "late destination"
    assert source.read_text(encoding="utf-8") == "third-party stage"
    stage_files = [
        child for child in tmp_path.iterdir() if child.name.startswith(".fo-stage-")
    ]
    assert len(stage_files) == 1
    assert stage_files[0].read_text(encoding="utf-8") == "third-party stage"
    recovery_files = [
        child for child in tmp_path.iterdir() if child.name.startswith(".fo-recovery-")
    ]
    assert len(recovery_files) == 1
    assert recovery_files[0].read_text(encoding="utf-8") == "planned source"


'''
tests = tests.replace(anchor, new_test + anchor, 1)
TESTS.write_text(tests, encoding="utf-8")
