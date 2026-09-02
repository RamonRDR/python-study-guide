import os
import stat
from pathlib import Path

import pytest

import file_organizer
from file_organizer import execute_plan, plan_organization


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

    def racing_rename_no_replace(
        source_name: str,
        destination_name: str,
        *,
        source_directory_fd: int,
        destination_directory_fd: int,
    ) -> None:
        destination.write_text("late destination", encoding="utf-8")
        original_rename_no_replace(
            source_name,
            destination_name,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
        )

    monkeypatch.setattr(
        file_organizer,
        "_rename_no_replace_at",
        racing_rename_no_replace,
    )

    with pytest.raises(FileExistsError, match="during execution"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "planned source"
    assert destination.read_text(encoding="utf-8") == "late destination"
    assert any(child.name.startswith(".fo-stage-") for child in tmp_path.iterdir())


def test_execute_plan_rejects_category_symlink_created_after_preflight(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)

    outside = tmp_path.parent / f"{tmp_path.name}-outside"
    outside.mkdir()
    category = tmp_path / "documents"
    original_mkdir = os.mkdir
    raced = False

    def racing_mkdir(
        path: str | os.PathLike[str],
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> None:
        nonlocal raced
        if path == "documents" and dir_fd is not None and not raced:
            raced = True
            category.symlink_to(outside, target_is_directory=True)
            raise FileExistsError
        original_mkdir(path, mode, dir_fd=dir_fd)

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
    monkeypatch.setattr(file_organizer.os, "mkdir", racing_mkdir)

    with pytest.raises(ValueError, match="became unsafe during execution"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "planned source"
    assert category.is_symlink()
    assert list(outside.iterdir()) == []


def test_execute_plan_rejects_source_symlink_replacement_during_mutation(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)

    outside = tmp_path.parent / f"{tmp_path.name}-source-target.txt"
    outside.write_text("target data", encoding="utf-8")
    destination = tmp_path / "documents" / "notes.txt"
    original_move = file_organizer._move_file_no_replace_at
    raced = False

    def racing_move(
        source_name: str,
        destination_name: str,
        *,
        source_directory_path: Path,
        source_directory_fd: int,
        destination_directory_fd: int,
        category_name: str,
        source_fd: int,
        expected_identity: file_organizer._FileIdentity,
    ) -> None:
        nonlocal raced
        if not raced:
            raced = True
            source.unlink()
            source.symlink_to(outside)
        original_move(
            source_name,
            destination_name,
            source_directory_path=source_directory_path,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
            category_name=category_name,
            source_fd=source_fd,
            expected_identity=expected_identity,
        )

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
    monkeypatch.setattr(file_organizer, "_move_file_no_replace_at", racing_move)

    with pytest.raises(FileNotFoundError, match="planned source data retained"):
        execute_plan(plan)

    assert source.is_symlink()
    assert outside.read_text(encoding="utf-8") == "target data"
    assert not destination.exists()


def test_source_replacement_during_claim_is_preserved_without_unlink(
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
    raced = False

    def racing_rename_no_replace(
        source_name: str,
        destination_name: str,
        *,
        source_directory_fd: int,
        destination_directory_fd: int,
    ) -> None:
        nonlocal raced
        if (
            source_name == source.name
            and source_directory_fd == destination_directory_fd
            and not raced
        ):
            raced = True
            source.unlink()
            source.write_text("third-party replacement", encoding="utf-8")
        original_rename_no_replace(
            source_name,
            destination_name,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
        )

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
    monkeypatch.setattr(
        file_organizer,
        "_rename_no_replace_at",
        racing_rename_no_replace,
    )

    with pytest.raises(FileNotFoundError, match="planned source data retained"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "third-party replacement"
    assert not destination.exists()
    recovery_files = [
        child for child in tmp_path.iterdir() if child.name.startswith(".fo-recovery-")
    ]
    assert len(recovery_files) == 1
    assert recovery_files[0].read_text(encoding="utf-8") == "planned source"
    retained = [
        child for child in tmp_path.iterdir() if child.name.startswith(".fo-stage-")
    ]
    assert len(retained) == 1
    assert retained[0].read_text(encoding="utf-8") == "third-party replacement"


def test_category_rename_after_fd_open_never_reports_false_destination(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)
    category = tmp_path / "documents"
    detached = tmp_path / "documents-detached"
    original_rename_no_replace = file_organizer._rename_no_replace_at
    raced = False

    def racing_rename_no_replace(
        source_name: str,
        destination_name: str,
        *,
        source_directory_fd: int,
        destination_directory_fd: int,
    ) -> None:
        nonlocal raced
        if source_directory_fd != destination_directory_fd and not raced:
            raced = True
            category.rename(detached)
            category.mkdir()
        original_rename_no_replace(
            source_name,
            destination_name,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
        )

    monkeypatch.setattr(
        file_organizer,
        "_rename_no_replace_at",
        racing_rename_no_replace,
    )

    with pytest.raises(ValueError, match="category directory moved during execution"):
        execute_plan(plan)

    assert not (category / "notes.txt").exists()
    assert (detached / "notes.txt").read_text(encoding="utf-8") == "planned source"


def test_source_root_rename_after_fd_open_never_reports_false_destination(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    workspace = tmp_path / "workspace"
    workspace.mkdir()
    source = workspace / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(workspace)
    detached = tmp_path / "workspace-detached"
    original_rename_no_replace = file_organizer._rename_no_replace_at
    raced = False

    def racing_rename_no_replace(
        source_name: str,
        destination_name: str,
        *,
        source_directory_fd: int,
        destination_directory_fd: int,
    ) -> None:
        nonlocal raced
        if source_directory_fd != destination_directory_fd and not raced:
            raced = True
            workspace.rename(detached)
        original_rename_no_replace(
            source_name,
            destination_name,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
        )

    monkeypatch.setattr(
        file_organizer,
        "_rename_no_replace_at",
        racing_rename_no_replace,
    )

    with pytest.raises(ValueError, match="source_directory moved during execution"):
        execute_plan(plan)

    assert not workspace.exists()
    assert (detached / "documents" / "notes.txt").read_text(encoding="utf-8") == "planned source"


def test_stage_name_is_fixed_length_for_long_source_names() -> None:
    short = file_organizer._make_stage_name("a.txt")
    long = file_organizer._make_stage_name(f"{'x' * 220}.txt")

    assert short.startswith(".fo-stage-")
    assert long.startswith(".fo-stage-")
    assert len(short.encode()) == len(long.encode()) < 64


def test_successful_execution_never_unlinks_a_staging_entry(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)
    original_unlink = os.unlink

    def guarded_unlink(
        path: str | os.PathLike[str],
        *,
        dir_fd: int | None = None,
    ) -> None:
        if os.fspath(path).startswith(".fo-stage-"):
            raise AssertionError("staging entries must not be unlinked")
        original_unlink(path, dir_fd=dir_fd)

    monkeypatch.setattr(file_organizer.os, "unlink", guarded_unlink)

    result = execute_plan(plan)

    assert result.moved_count == 1
    assert not source.exists()
    assert (tmp_path / "documents" / "notes.txt").read_text(encoding="utf-8") == "planned source"


def test_source_pin_uses_nonblocking_open_and_rejects_late_fifo(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")
    if not hasattr(os, "mkfifo") or not hasattr(os, "O_NONBLOCK"):
        pytest.skip("FIFO or O_NONBLOCK is unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)
    original_open = os.open
    raced = False
    observed_flags: list[int] = []

    def racing_open(
        path: str | os.PathLike[str],
        flags: int,
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> int:
        nonlocal raced
        if path == source.name and dir_fd is not None and not raced:
            raced = True
            observed_flags.append(flags)
            source.unlink()
            os.mkfifo(source)
        return original_open(path, flags, mode, dir_fd=dir_fd)

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
    monkeypatch.setattr(file_organizer.os, "open", racing_open)

    with pytest.raises(FileNotFoundError, match="regular file|changed during execution"):
        execute_plan(plan)

    assert observed_flags
    assert observed_flags[0] & os.O_NONBLOCK
    assert stat.S_ISFIFO(source.lstat().st_mode)
    assert not (tmp_path / "documents" / "notes.txt").exists()


def test_execute_plan_rechecks_late_casefold_collision_before_commit(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "Report.TXT"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)
    category = tmp_path / "documents"
    late_destination = category / "report.txt"
    exact_destination = category / "Report.TXT"
    original_claim = file_organizer._claim_source_at
    raced = False

    def racing_claim(
        source_name: str,
        *,
        root_fd: int,
        expected_identity: file_organizer._FileIdentity,
    ) -> str:
        nonlocal raced
        stage_name = original_claim(
            source_name,
            root_fd=root_fd,
            expected_identity=expected_identity,
        )
        if not raced:
            raced = True
            late_destination.write_text("late casefold collision", encoding="utf-8")
        return stage_name

    monkeypatch.setattr(file_organizer, "_claim_source_at", racing_claim)

    with pytest.raises(FileExistsError, match="case-insensitive destination"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "planned source"
    assert late_destination.read_text(encoding="utf-8") == "late casefold collision"
    assert not exact_destination.exists()
    assert any(child.name.startswith(".fo-stage-") for child in tmp_path.iterdir())



def test_staging_replacement_before_final_rename_preserves_pinned_source_data(
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
    raced = False

    def racing_rename_no_replace(
        source_name: str,
        destination_name: str,
        *,
        source_directory_fd: int,
        destination_directory_fd: int,
    ) -> None:
        nonlocal raced
        if source_name.startswith(".fo-stage-") and not raced:
            raced = True
            stage = tmp_path / source_name
            assert stage.name.startswith(".fo-stage-")
            stage.unlink()
            stage.write_text("third-party replacement", encoding="utf-8")
        original_rename_no_replace(
            source_name,
            destination_name,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
        )

    monkeypatch.setattr(
        file_organizer,
        "_rename_no_replace_at",
        racing_rename_no_replace,
    )

    with pytest.raises(RuntimeError, match="planned source data retained"):
        execute_plan(plan)

    assert destination.read_text(encoding="utf-8") == "third-party replacement"
    recovery_files = [
        child
        for child in tmp_path.iterdir()
        if child.name.startswith(".fo-recovery-")
    ]
    assert len(recovery_files) == 1
    assert recovery_files[0].read_text(encoding="utf-8") == "planned source"
    assert not source.exists()





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

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
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


def test_failed_final_rename_after_stage_replacement_recovers_pinned_source_data(
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
    raced = False

    def racing_rename_no_replace(
        source_name: str,
        destination_name: str,
        *,
        source_directory_fd: int,
        destination_directory_fd: int,
    ) -> None:
        nonlocal raced
        if source_name.startswith(".fo-stage-") and not raced:
            raced = True
            stage = tmp_path / source_name
            stage.unlink()
            stage.write_text("third-party stage", encoding="utf-8")
            destination.write_text("late destination", encoding="utf-8")
        original_rename_no_replace(
            source_name,
            destination_name,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
        )

    monkeypatch.setattr(
        file_organizer,
        "_rename_no_replace_at",
        racing_rename_no_replace,
    )

    with pytest.raises(FileExistsError, match="destination appeared during execution"):
        execute_plan(plan)

    assert destination.read_text(encoding="utf-8") == "late destination"
    assert not source.exists()
    stage_files = [
        child for child in tmp_path.iterdir() if child.name.startswith(".fo-stage-")
    ]
    assert len(stage_files) == 1
    assert stage_files[0].read_text(encoding="utf-8") == "third-party stage"
    recovery_files = [
        child
        for child in tmp_path.iterdir()
        if child.name.startswith(".fo-recovery-")
    ]
    assert len(recovery_files) == 1
    assert recovery_files[0].read_text(encoding="utf-8") == "planned source"


def test_secure_execution_reports_readability_precondition_before_categories(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)
    original_open = os.open

    def permission_denied_open(
        path: str | os.PathLike[str],
        flags: int,
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> int:
        if path == source.name and dir_fd is not None:
            raise PermissionError("simulated unreadable source")
        return original_open(path, flags, mode, dir_fd=dir_fd)

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
    monkeypatch.setattr(file_organizer.os, "open", permission_denied_open)

    with pytest.raises(PermissionError, match="must be readable for safe execution"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "planned source"
    assert not (tmp_path / "documents").exists()


def test_category_fd_is_closed_when_anchor_verification_fails(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    root_fd = file_organizer._open_source_directory_fd(tmp_path)
    original_open = os.open
    original_close = os.close
    opened_category_fd: int | None = None
    closed_fds: list[int] = []

    def tracking_open(
        path: str | os.PathLike[str],
        flags: int,
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> int:
        nonlocal opened_category_fd
        fd = original_open(path, flags, mode, dir_fd=dir_fd)
        if path == "documents" and dir_fd == root_fd:
            opened_category_fd = fd
        return fd

    def tracking_close(fd: int) -> None:
        closed_fds.append(fd)
        original_close(fd)

    def failing_anchor(**_: object) -> None:
        raise ValueError("simulated category anchor race")

    monkeypatch.setattr(file_organizer.os, "open", tracking_open)
    monkeypatch.setattr(file_organizer.os, "close", tracking_close)
    monkeypatch.setattr(file_organizer, "_verify_category_anchor_at", failing_anchor)

    try:
        with pytest.raises(ValueError, match="simulated category anchor race"):
            file_organizer._open_category_directory_fd(root_fd, "documents")
    finally:
        original_close(root_fd)

    assert opened_category_fd is not None
    assert opened_category_fd in closed_fds


def test_source_identity_is_accepted_only_after_descriptor_pin(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)
    destination = tmp_path / "documents" / "notes.txt"
    original_pin = file_organizer._pin_planned_sources_at
    raced = False

    def racing_pin(
        plan_value: file_organizer.OrganizationPlan,
        *,
        root_fd: int,
    ) -> dict[Path, file_organizer._PinnedSource]:
        nonlocal raced
        pinned = original_pin(plan_value, root_fd=root_fd)
        if not raced:
            raced = True
            source.unlink()
            source.write_text("third-party replacement", encoding="utf-8")
        return pinned

    monkeypatch.setattr(file_organizer, "_pin_planned_sources_at", racing_pin)

    with pytest.raises(FileNotFoundError, match="planned source data retained"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "third-party replacement"
    assert not destination.exists()
    recovery_files = [
        child for child in tmp_path.iterdir() if child.name.startswith(".fo-recovery-")
    ]
    assert len(recovery_files) == 1
    assert recovery_files[0].read_text(encoding="utf-8") == "planned source"
