from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one patch anchor in {path}, found {count}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


IMPLEMENTATION = "practical-projects/06-file-organizer/file_organizer.py"
TESTS = "practical-projects/06-file-organizer/tests/test_atomic_move.py"

helpers_anchor = '''def _preserve_stage_at(stage_name: str, source_name: str, *, root_fd: int) -> None:\n'''
helpers = '''def _make_recovery_name(source_name: str) -> str:\n    """Return a bounded exclusive name for emergency source-data recovery."""\n    del source_name\n    return f".fo-recovery-{secrets.token_hex(16)}"\n\n\ndef _recover_pinned_source_at(\n    source_fd: int,\n    source_name: str,\n    *,\n    root_fd: int,\n) -> str:\n    """Persist bytes from the pinned source FD into an exclusive recovery file."""\n    source_stat = os.fstat(source_fd)\n    mode = stat.S_IMODE(source_stat.st_mode)\n    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL\n    if hasattr(os, "O_CLOEXEC"):\n        flags |= os.O_CLOEXEC\n\n    recovery_fd: int | None = None\n    recovery_name = ""\n    for _ in range(16):\n        recovery_name = _make_recovery_name(source_name)\n        try:\n            recovery_fd = os.open(\n                recovery_name,\n                flags,\n                mode,\n                dir_fd=root_fd,\n            )\n        except FileExistsError:\n            continue\n        break\n\n    if recovery_fd is None:\n        raise FileExistsError(\n            f"could not allocate recovery entry for planned source: {source_name}"\n        )\n\n    original_offset = os.lseek(source_fd, 0, os.SEEK_CUR)\n    try:\n        os.lseek(source_fd, 0, os.SEEK_SET)\n        while True:\n            chunk = os.read(source_fd, 1024 * 1024)\n            if not chunk:\n                break\n            view = memoryview(chunk)\n            while view:\n                written = os.write(recovery_fd, view)\n                if written <= 0:\n                    raise OSError(\n                        "could not persist pinned source recovery data"\n                    )\n                view = view[written:]\n        os.fchmod(recovery_fd, mode)\n        os.fsync(recovery_fd)\n    finally:\n        os.lseek(source_fd, original_offset, os.SEEK_SET)\n        os.close(recovery_fd)\n\n    return recovery_name\n\n\n'''
replace_once(IMPLEMENTATION, helpers_anchor, helpers + helpers_anchor)

verify_anchor = '''        _verify_destination_identity_at(\n            destination_name,\n            destination_directory_fd=destination_directory_fd,\n            expected_identity=expected_identity,\n        )\n        _verify_root_anchor_at(source_directory_path, source_directory_fd)\n'''
verify_replacement = '''        try:\n            _verify_destination_identity_at(\n                destination_name,\n                destination_directory_fd=destination_directory_fd,\n                expected_identity=expected_identity,\n            )\n        except RuntimeError as exc:\n            recovery_name = _recover_pinned_source_at(\n                source_fd,\n                source_name,\n                root_fd=source_directory_fd,\n            )\n            raise RuntimeError(\n                "destination does not match planned source; "\n                f"planned source data retained as {recovery_name}: {destination_name}"\n            ) from exc\n        _verify_root_anchor_at(source_directory_path, source_directory_fd)\n'''
replace_once(IMPLEMENTATION, verify_anchor, verify_replacement)

test_path = Path(TESTS)
test_text = test_path.read_text(encoding="utf-8")
test_name = "test_staging_replacement_before_final_rename_preserves_pinned_source_data"
if test_name not in test_text:
    test_text += '''\n\n\ndef test_staging_replacement_before_final_rename_preserves_pinned_source_data(\n    monkeypatch: pytest.MonkeyPatch,\n    tmp_path: Path,\n) -> None:\n    if not file_organizer._supports_secure_directory_fds():\n        pytest.skip("secure directory descriptors are unavailable on this platform")\n\n    source = tmp_path / "notes.txt"\n    source.write_text("planned source", encoding="utf-8")\n    plan = plan_organization(tmp_path)\n    destination = tmp_path / "documents" / "notes.txt"\n    original_rename_no_replace = file_organizer._rename_no_replace_at\n    raced = False\n\n    def racing_rename_no_replace(\n        source_name: str,\n        destination_name: str,\n        *,\n        source_directory_fd: int,\n        destination_directory_fd: int,\n    ) -> None:\n        nonlocal raced\n        if not raced:\n            raced = True\n            stage = tmp_path / source_name\n            assert stage.name.startswith(".fo-stage-")\n            stage.unlink()\n            stage.write_text("third-party replacement", encoding="utf-8")\n        original_rename_no_replace(\n            source_name,\n            destination_name,\n            source_directory_fd=source_directory_fd,\n            destination_directory_fd=destination_directory_fd,\n        )\n\n    monkeypatch.setattr(\n        file_organizer,\n        "_rename_no_replace_at",\n        racing_rename_no_replace,\n    )\n\n    with pytest.raises(RuntimeError, match="planned source data retained"):\n        execute_plan(plan)\n\n    assert destination.read_text(encoding="utf-8") == "third-party replacement"\n    recovery_files = [\n        child\n        for child in tmp_path.iterdir()\n        if child.name.startswith(".fo-recovery-")\n    ]\n    assert len(recovery_files) == 1\n    assert recovery_files[0].read_text(encoding="utf-8") == "planned source"\n    assert not source.exists()\n'''
    test_path.write_text(test_text, encoding="utf-8")

DOC_UPDATES = {
    "practical-projects/06-file-organizer/README.md": (
        "If execution has already claimed the source into a staging entry and later detects an unsafe condition, it may create a no-replace hard link back to the original source name when possible. It does not blindly delete the staging entry.\n\n",
        "If execution has already claimed the source into a staging entry and later detects an unsafe condition, it may create a no-replace hard link back to the original source name when possible. It does not blindly delete the staging entry.\n\nA staging pathname is not an inode lock. If the final rename consumes a replacement entry and destination identity verification detects the mismatch, execution leaves the unrelated destination intact and, before closing the still-pinned source file descriptor, copies the planned source bytes into an exclusive `.fo-recovery-*` regular file. This preserves recoverable data without claiming that the original inode survived the race.\n\n",
    ),
    "practical-projects/06-file-organizer/README.pt-BR.md": (
        "Se a execução já moveu a origem para staging e depois detecta condição insegura, ela pode criar um hard link no-replace de volta para o nome de origem quando possível. Ela não apaga cegamente o staging.\n\n",
        "Se a execução já moveu a origem para staging e depois detecta condição insegura, ela pode criar um hard link no-replace de volta para o nome de origem quando possível. Ela não apaga cegamente o staging.\n\nUm pathname de staging não funciona como lock de inode. Se o rename final consumir uma entrada substituta e a verificação de identidade do destino detectar a divergência, a execução mantém intacto o destino alheio e, antes de fechar o descritor ainda pinado da origem, copia os bytes planejados para um arquivo regular exclusivo `.fo-recovery-*`. Essa recuperação preserva dados recuperáveis sem afirmar que o inode original sobreviveu à corrida.\n\n",
    ),
    "practical-projects/06-file-organizer/README.es.md": (
        "Si la ejecución ya movió el origen al staging y después detecta una condición insegura, puede crear un hard link no-replace de vuelta al nombre de origen cuando sea posible. No elimina a ciegas el staging.\n\n",
        "Si la ejecución ya movió el origen al staging y después detecta una condición insegura, puede crear un hard link no-replace de vuelta al nombre de origen cuando sea posible. No elimina a ciegas el staging.\n\nUn pathname de staging no funciona como lock de inode. Si el rename final consume una entrada de reemplazo y la verificación de identidad del destino detecta la divergencia, la ejecución conserva intacto el destino ajeno y, antes de cerrar el descriptor aún anclado del origen, copia los bytes planificados a un archivo regular exclusivo `.fo-recovery-*`. Esta recuperación conserva datos recuperables sin afirmar que el inode original haya sobrevivido a la carrera.\n\n",
    ),
}

for path, (old, new) in DOC_UPDATES.items():
    replace_once(path, old, new)
