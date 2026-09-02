from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"expected exactly one anchor in {path}: found {text.count(old)}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


# 1) Verify the recovery pathname still names the created recovery inode.
organizer = ROOT / "practical-projects/06-file-organizer/file_organizer.py"
old_recovery = '''def _recover_pinned_source_at(
    source_fd: int,
    source_name: str,
    *,
    root_fd: int,
) -> str:
    """Persist bytes from the pinned source FD into an exclusive recovery file."""
    source_stat = os.fstat(source_fd)
    mode = stat.S_IMODE(source_stat.st_mode)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC

    recovery_fd: int | None = None
    recovery_name = ""
    for _ in range(16):
        recovery_name = _make_recovery_name(source_name)
        try:
            recovery_fd = os.open(
                recovery_name,
                flags,
                mode,
                dir_fd=root_fd,
            )
        except FileExistsError:
            continue
        break

    if recovery_fd is None:
        raise FileExistsError(
            f"could not allocate recovery entry for planned source: {source_name}"
        )

    original_offset = os.lseek(source_fd, 0, os.SEEK_CUR)
    try:
        os.lseek(source_fd, 0, os.SEEK_SET)
        while True:
            chunk = os.read(source_fd, 1024 * 1024)
            if not chunk:
                break
            view = memoryview(chunk)
            while view:
                written = os.write(recovery_fd, view)
                if written <= 0:
                    raise OSError(
                        "could not persist pinned source recovery data"
                    )
                view = view[written:]
        os.fchmod(recovery_fd, mode)
        os.fsync(recovery_fd)
    finally:
        os.lseek(source_fd, original_offset, os.SEEK_SET)
        os.close(recovery_fd)

    return recovery_name
'''
new_recovery = '''def _recover_pinned_source_at(
    source_fd: int,
    source_name: str,
    *,
    root_fd: int,
) -> str:
    """Persist bytes from the pinned source FD into a proven recovery pathname."""
    source_stat = os.fstat(source_fd)
    mode = stat.S_IMODE(source_stat.st_mode)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC

    recovery_fd: int | None = None
    recovery_name = ""
    for _ in range(16):
        recovery_name = _make_recovery_name(source_name)
        try:
            recovery_fd = os.open(
                recovery_name,
                flags,
                mode,
                dir_fd=root_fd,
            )
        except FileExistsError:
            continue
        break

    if recovery_fd is None:
        raise FileExistsError(
            f"could not allocate recovery entry for planned source: {source_name}"
        )

    recovery_identity = _identity_from_regular_stat(
        os.fstat(recovery_fd),
        filename=recovery_name,
    )
    original_offset = os.lseek(source_fd, 0, os.SEEK_CUR)
    try:
        os.lseek(source_fd, 0, os.SEEK_SET)
        while True:
            chunk = os.read(source_fd, 1024 * 1024)
            if not chunk:
                break
            view = memoryview(chunk)
            while view:
                written = os.write(recovery_fd, view)
                if written <= 0:
                    raise OSError(
                        "could not persist pinned source recovery data"
                    )
                view = view[written:]
        os.fchmod(recovery_fd, mode)
        os.fsync(recovery_fd)

        try:
            recovery_path_identity = _regular_identity_at(
                recovery_name,
                directory_fd=root_fd,
            )
        except OSError as exc:
            raise RuntimeError(
                f"recovery pathname changed during execution: {recovery_name}"
            ) from exc
        if recovery_path_identity != recovery_identity:
            raise RuntimeError(
                f"recovery pathname changed during execution: {recovery_name}"
            )
    finally:
        os.lseek(source_fd, original_offset, os.SEEK_SET)
        os.close(recovery_fd)

    return recovery_name
'''
replace_once(organizer, old_recovery, new_recovery)

# 2) Regression: unlink the recovery pathname during fsync and prove no false retention.
tests = ROOT / "practical-projects/06-file-organizer/tests/test_atomic_move.py"
anchor = '''from file_organizer import execute_plan, plan_organization


def test_execute_plan_never_replaces_destination_created_after_preflight(
'''
insert = '''from file_organizer import execute_plan, plan_organization


def test_recovery_path_removed_during_fsync_is_not_reported_as_retained(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    root_fd = file_organizer._open_source_directory_fd(tmp_path)
    source_fd = os.open(source, os.O_RDONLY)
    original_fsync = os.fsync
    recovery_unlinked = False

    def unlink_recovery_during_fsync(fd: int) -> None:
        nonlocal recovery_unlinked
        original_fsync(fd)
        if fd == source_fd or recovery_unlinked:
            return
        recovery_files = [
            child
            for child in tmp_path.iterdir()
            if child.name.startswith(".fo-recovery-")
        ]
        assert len(recovery_files) == 1
        recovery_files[0].unlink()
        recovery_unlinked = True

    monkeypatch.setattr(file_organizer.os, "fsync", unlink_recovery_during_fsync)

    try:
        with pytest.raises(RuntimeError, match="recovery pathname changed during execution"):
            file_organizer._recover_pinned_source_at(
                source_fd,
                source.name,
                root_fd=root_fd,
            )

        assert recovery_unlinked
        assert not any(
            child.name.startswith(".fo-recovery-") for child in tmp_path.iterdir()
        )
        os.lseek(source_fd, 0, os.SEEK_SET)
        assert os.read(source_fd, 1024) == b"planned source"
    finally:
        os.close(source_fd)
        os.close(root_fd)


def test_execute_plan_never_replaces_destination_created_after_preflight(
'''
replace_once(tests, anchor, insert)

# 3) Documentation in EN / PT-BR / ES.
readme = ROOT / "practical-projects/06-file-organizer/README.md"
old_en = '''A staging pathname is not an inode lock. After the source has been claimed, every failure path rechecks whether the staging entry still matches the pinned source identity. If it does, execution may attempt a no-replace hard link from that proven stage back to the original source name, but restoration is accepted only after the recreated source pathname itself is re-read and verified to have the pinned identity. If the link fails, races to a different object, leaves the source name missing, or the post-link source identity does not match, execution leaves uncertain entries untouched and, before closing the still-pinned source file descriptor, copies the planned source bytes into an exclusive `.fo-recovery-*` regular file. This also covers a final `RENAME_NOREPLACE` failure caused by a destination that appears after the stage was raced. If a replacement stage is successfully renamed and destination identity verification detects the mismatch, the unrelated destination is likewise left intact while the pinned bytes are recovered. Recovery preserves data without claiming that the original inode survived the race.
'''
new_en = '''A staging pathname is not an inode lock. After the source has been claimed, every failure path rechecks whether the staging entry still matches the pinned source identity. If it does, execution may attempt a no-replace hard link from that proven stage back to the original source name, but restoration is accepted only after the recreated source pathname itself is re-read and verified to have the pinned identity. If the link fails, races to a different object, leaves the source name missing, or the post-link source identity does not match, execution leaves uncertain entries untouched and, before closing the still-pinned source file descriptor, copies the planned source bytes into an exclusive `.fo-recovery-*` regular file. That recovery file is not reported as retained merely because its descriptor was written and `fsync()` completed: while the recovery descriptor is still open, execution re-reads the recovery pathname through the anchored root and requires it to name the same regular-file `(st_dev, st_ino)`. A missing, renamed, or replaced recovery pathname raises instead of falsely claiming durable retention, and uncertain third-party entries are not deleted or overwritten. This also covers a final `RENAME_NOREPLACE` failure caused by a destination that appears after the stage was raced. If a replacement stage is successfully renamed and destination identity verification detects the mismatch, the unrelated destination is likewise left intact while the pinned bytes are recovered. Recovery preserves data only when the pathname used to report that preservation is itself proven.
'''
replace_once(readme, old_en, new_en)

readme_pt = ROOT / "practical-projects/06-file-organizer/README.pt-BR.md"
old_pt = '''Um pathname de staging não funciona como lock de inode. Depois que a origem foi claimada, todo caminho de falha revalida se a entrada de staging ainda corresponde à identidade pinada da origem. Se corresponder, a execução pode tentar recriar o nome original por hard link no-replace a partir desse staging comprovado, mas a restauração só é aceita depois que o próprio pathname recriado da origem é relido e verificado com a identidade pinada. Se o link falhar, sofrer corrida para outro objeto, deixar o nome de origem ausente ou a identidade pós-link não corresponder, a execução deixa entradas incertas intactas e, antes de fechar o descritor ainda pinado da origem, copia os bytes planejados para um arquivo regular exclusivo `.fo-recovery-*`. Isso também cobre uma falha final de `RENAME_NOREPLACE` causada por um destino que aparece depois de uma corrida sobre o staging. Se um staging substituto for renomeado com sucesso e a verificação de identidade do destino detectar a divergência, o destino alheio também permanece intacto enquanto os bytes pinados são recuperados. A recuperação preserva os dados sem afirmar que o inode original sobreviveu à corrida.
'''
new_pt = '''Um pathname de staging não funciona como lock de inode. Depois que a origem foi claimada, todo caminho de falha revalida se a entrada de staging ainda corresponde à identidade pinada da origem. Se corresponder, a execução pode tentar recriar o nome original por hard link no-replace a partir desse staging comprovado, mas a restauração só é aceita depois que o próprio pathname recriado da origem é relido e verificado com a identidade pinada. Se o link falhar, sofrer corrida para outro objeto, deixar o nome de origem ausente ou a identidade pós-link não corresponder, a execução deixa entradas incertas intactas e, antes de fechar o descritor ainda pinado da origem, copia os bytes planejados para um arquivo regular exclusivo `.fo-recovery-*`. Esse recovery não é reportado como preservado apenas porque seu descritor foi gravado e o `fsync()` terminou: enquanto o descritor do recovery ainda está aberto, a execução relê o pathname de recuperação pelo root ancorado e exige que ele aponte para o mesmo arquivo regular `(st_dev, st_ino)`. Se o pathname sumir, for renomeado ou substituído, a execução falha em vez de afirmar falsamente que os dados foram retidos, sem excluir nem sobrescrever entradas incertas de terceiros. Isso também cobre uma falha final de `RENAME_NOREPLACE` causada por um destino que aparece depois de uma corrida sobre o staging. Se um staging substituto for renomeado com sucesso e a verificação de identidade do destino detectar a divergência, o destino alheio também permanece intacto enquanto os bytes pinados são recuperados. A recuperação só afirma preservação quando o próprio pathname usado para reportá-la é comprovado.
'''
replace_once(readme_pt, old_pt, new_pt)

readme_es = ROOT / "practical-projects/06-file-organizer/README.es.md"
old_es = '''Un pathname de staging no funciona como lock de inode. Después de reclamar el origen, cada ruta de fallo vuelve a comprobar si la entrada de staging todavía coincide con la identidad fijada del origen. Si coincide, la ejecución puede intentar recrear el nombre original mediante un hard link no-replace desde ese staging comprobado, pero la restauración solo se acepta después de volver a leer el propio pathname recreado del origen y verificar que conserva la identidad fijada. Si el link falla, sufre una carrera hacia otro objeto, deja ausente el nombre de origen o la identidad posterior al link no coincide, la ejecución deja intactas las entradas inciertas y, antes de cerrar el descriptor todavía fijado del origen, copia los bytes planificados a un archivo regular exclusivo `.fo-recovery-*`. Esto también cubre un fallo final de `RENAME_NOREPLACE` causado por un destino que aparece después de una carrera sobre el staging. Si un staging de reemplazo se renombra con éxito y la verificación de identidad del destino detecta la divergencia, el destino ajeno también queda intacto mientras se recuperan los bytes fijados. La recuperación conserva los datos sin afirmar que el inode original haya sobrevivido a la carrera.
'''
new_es = '''Un pathname de staging no funciona como lock de inode. Después de reclamar el origen, cada ruta de fallo vuelve a comprobar si la entrada de staging todavía coincide con la identidad fijada del origen. Si coincide, la ejecución puede intentar recrear el nombre original mediante un hard link no-replace desde ese staging comprobado, pero la restauración solo se acepta después de volver a leer el propio pathname recreado del origen y verificar que conserva la identidad fijada. Si el link falla, sufre una carrera hacia otro objeto, deja ausente el nombre de origen o la identidad posterior al link no coincide, la ejecución deja intactas las entradas inciertas y, antes de cerrar el descriptor todavía fijado del origen, copia los bytes planificados a un archivo regular exclusivo `.fo-recovery-*`. Ese recovery no se informa como conservado solo porque su descriptor se haya escrito y `fsync()` haya terminado: mientras el descriptor de recovery sigue abierto, la ejecución vuelve a leer el pathname de recuperación a través de la raíz anclada y exige que nombre el mismo archivo regular `(st_dev, st_ino)`. Si el pathname desaparece, se renombra o se reemplaza, la ejecución falla en lugar de afirmar falsamente que los datos quedaron retenidos, sin borrar ni sobrescribir entradas inciertas de terceros. Esto también cubre un fallo final de `RENAME_NOREPLACE` causado por un destino que aparece después de una carrera sobre el staging. Si un staging de reemplazo se renombra con éxito y la verificación de identidad del destino detecta la divergencia, el destino ajeno también queda intacto mientras se recuperan los bytes fijados. La recuperación solo afirma conservación cuando el propio pathname usado para informarla queda demostrado.
'''
replace_once(readme_es, old_es, new_es)

print("Review 14 patch applied")
