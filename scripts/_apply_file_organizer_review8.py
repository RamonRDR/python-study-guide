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

category_old = '''    _verify_category_anchor_at(\n        root_fd=root_fd,\n        category_name=category_name,\n        category_fd=category_fd,\n    )\n    return category_fd\n'''
category_new = '''    try:\n        _verify_category_anchor_at(\n            root_fd=root_fd,\n            category_name=category_name,\n            category_fd=category_fd,\n        )\n    except Exception:\n        os.close(category_fd)\n        raise\n    return category_fd\n'''
replace_once(IMPLEMENTATION, category_old, category_new)

permission_old = '''    try:\n        source_fd = os.open(source_name, flags, dir_fd=root_fd)\n    except OSError as exc:\n        raise FileNotFoundError(\n            f"planned source changed during execution: {source_name}"\n        ) from exc\n'''
permission_new = '''    try:\n        source_fd = os.open(source_name, flags, dir_fd=root_fd)\n    except PermissionError as exc:\n        raise PermissionError(\n            f"planned source must be readable for safe execution: {source_name}"\n        ) from exc\n    except OSError as exc:\n        raise FileNotFoundError(\n            f"planned source changed during execution: {source_name}"\n        ) from exc\n'''
replace_once(IMPLEMENTATION, permission_old, permission_new)

prevalidate_old = '''    try:\n        _verify_root_anchor_at(plan.source_directory, root_fd)\n        for category in sorted(\n'''
prevalidate_new = '''    try:\n        _verify_root_anchor_at(plan.source_directory, root_fd)\n\n        # Readability is a deliberate secure-execution prerequisite because\n        # pinned-FD recovery must be able to persist the planned source bytes.\n        for action in plan.actions:\n            validation_fd = _open_planned_source_fd_at(\n                action.source.name,\n                root_fd=root_fd,\n                expected_identity=source_identities[action.source],\n            )\n            os.close(validation_fd)\n\n        for category in sorted(\n'''
replace_once(IMPLEMENTATION, prevalidate_old, prevalidate_new)


test_path = Path(TESTS)
test_text = test_path.read_text(encoding="utf-8")
if "test_secure_execution_reports_readability_precondition_before_categories" not in test_text:
    test_text += '''\n\n\ndef test_secure_execution_reports_readability_precondition_before_categories(\n    monkeypatch: pytest.MonkeyPatch,\n    tmp_path: Path,\n) -> None:\n    if not file_organizer._supports_secure_directory_fds():\n        pytest.skip("secure directory descriptors are unavailable on this platform")\n\n    source = tmp_path / "notes.txt"\n    source.write_text("planned source", encoding="utf-8")\n    plan = plan_organization(tmp_path)\n    original_open = os.open\n\n    def permission_denied_open(\n        path: str | os.PathLike[str],\n        flags: int,\n        mode: int = 0o777,\n        *,\n        dir_fd: int | None = None,\n    ) -> int:\n        if path == source.name and dir_fd is not None:\n            raise PermissionError("simulated unreadable source")\n        return original_open(path, flags, mode, dir_fd=dir_fd)\n\n    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)\n    monkeypatch.setattr(file_organizer.os, "open", permission_denied_open)\n\n    with pytest.raises(PermissionError, match="must be readable for safe execution"):\n        execute_plan(plan)\n\n    assert source.read_text(encoding="utf-8") == "planned source"\n    assert not (tmp_path / "documents").exists()\n\n\ndef test_category_fd_is_closed_when_anchor_verification_fails(\n    monkeypatch: pytest.MonkeyPatch,\n    tmp_path: Path,\n) -> None:\n    if not file_organizer._supports_secure_directory_fds():\n        pytest.skip("secure directory descriptors are unavailable on this platform")\n\n    root_fd = file_organizer._open_source_directory_fd(tmp_path)\n    original_open = os.open\n    original_close = os.close\n    opened_category_fd: int | None = None\n    closed_fds: list[int] = []\n\n    def tracking_open(\n        path: str | os.PathLike[str],\n        flags: int,\n        mode: int = 0o777,\n        *,\n        dir_fd: int | None = None,\n    ) -> int:\n        nonlocal opened_category_fd\n        fd = original_open(path, flags, mode, dir_fd=dir_fd)\n        if path == "documents" and dir_fd == root_fd:\n            opened_category_fd = fd\n        return fd\n\n    def tracking_close(fd: int) -> None:\n        closed_fds.append(fd)\n        original_close(fd)\n\n    def failing_anchor(**_: object) -> None:\n        raise ValueError("simulated category anchor race")\n\n    monkeypatch.setattr(file_organizer.os, "open", tracking_open)\n    monkeypatch.setattr(file_organizer.os, "close", tracking_close)\n    monkeypatch.setattr(file_organizer, "_verify_category_anchor_at", failing_anchor)\n\n    try:\n        with pytest.raises(ValueError, match="simulated category anchor race"):\n            file_organizer._open_category_directory_fd(root_fd, "documents")\n    finally:\n        original_close(root_fd)\n\n    assert opened_category_fd is not None\n    assert opened_category_fd in closed_fds\n'''
    test_path.write_text(test_text, encoding="utf-8")

DOC_UPDATES = {
    "practical-projects/06-file-organizer/README.md": (
        "A staging pathname is not an inode lock. If the final rename consumes a replacement entry and destination identity verification detects the mismatch, execution leaves the unrelated destination intact and, before closing the still-pinned source file descriptor, copies the planned source bytes into an exclusive `.fo-recovery-*` regular file. This preserves recoverable data without claiming that the original inode survived the race.\n",
        "A staging pathname is not an inode lock. If the final rename consumes a replacement entry and destination identity verification detects the mismatch, execution leaves the unrelated destination intact and, before closing the still-pinned source file descriptor, copies the planned source bytes into an exclusive `.fo-recovery-*` regular file. This preserves recoverable data without claiming that the original inode survived the race.\n\nSafe Linux execution therefore deliberately requires read access to each planned regular file. Readability is validated before category directories are created and again when the source inode is pinned for mutation; permission failures are reported as `PermissionError`, not as a false source-identity change.\n",
    ),
    "practical-projects/06-file-organizer/README.pt-BR.md": (
        "Um pathname de staging não funciona como lock de inode. Se o rename final consumir uma entrada substituta e a verificação de identidade do destino detectar a divergência, a execução mantém intacto o destino alheio e, antes de fechar o descritor ainda pinado da origem, copia os bytes planejados para um arquivo regular exclusivo `.fo-recovery-*`. Essa recuperação preserva dados recuperáveis sem afirmar que o inode original sobreviveu à corrida.\n",
        "Um pathname de staging não funciona como lock de inode. Se o rename final consumir uma entrada substituta e a verificação de identidade do destino detectar a divergência, a execução mantém intacto o destino alheio e, antes de fechar o descritor ainda pinado da origem, copia os bytes planejados para um arquivo regular exclusivo `.fo-recovery-*`. Essa recuperação preserva dados recuperáveis sem afirmar que o inode original sobreviveu à corrida.\n\nPor isso, a execução segura no Linux exige deliberadamente permissão de leitura para cada arquivo regular planejado. A legibilidade é validada antes da criação das pastas de categoria e novamente ao pinar o inode da origem para a mutação; falhas de permissão são reportadas como `PermissionError`, e não como uma falsa mudança de identidade da origem.\n",
    ),
    "practical-projects/06-file-organizer/README.es.md": (
        "Un pathname de staging no funciona como lock de inode. Si el rename final consume una entrada de reemplazo y la verificación de identidad del destino detecta la divergencia, la ejecución conserva intacto el destino ajeno y, antes de cerrar el descriptor aún anclado del origen, copia los bytes planificados a un archivo regular exclusivo `.fo-recovery-*`. Esta recuperación conserva datos recuperables sin afirmar que el inode original haya sobrevivido a la carrera.\n",
        "Un pathname de staging no funciona como lock de inode. Si el rename final consume una entrada de reemplazo y la verificación de identidad del destino detecta la divergencia, la ejecución conserva intacto el destino ajeno y, antes de cerrar el descriptor aún anclado del origen, copia los bytes planificados a un archivo regular exclusivo `.fo-recovery-*`. Esta recuperación conserva datos recuperables sin afirmar que el inode original haya sobrevivido a la carrera.\n\nPor ello, la ejecución segura en Linux exige deliberadamente permiso de lectura para cada archivo regular planificado. La legibilidad se valida antes de crear los directorios de categoría y de nuevo al fijar el inode del origen para la mutación; los fallos de permisos se informan como `PermissionError`, no como un falso cambio de identidad del origen.\n",
    ),
}

for path, (old, new) in DOC_UPDATES.items():
    replace_once(path, old, new)
