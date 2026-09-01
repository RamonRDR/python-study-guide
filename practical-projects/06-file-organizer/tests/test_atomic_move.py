import os
from pathlib import Path

import pytest

import file_organizer
from file_organizer import execute_plan, plan_organization


def test_execute_plan_never_replaces_destination_created_after_preflight(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
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
            expected_identity=expected_identity,
        )

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
    monkeypatch.setattr(file_organizer, "_move_file_no_replace_at", racing_move)

    with pytest.raises(FileNotFoundError, match="regular file|changed during execution"):
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

    original_rename = os.rename
    raced = False

    def racing_rename(
        source_path: str | os.PathLike[str],
        destination_path: str | os.PathLike[str],
        *,
        src_dir_fd: int | None = None,
        dst_dir_fd: int | None = None,
    ) -> None:
        nonlocal raced
        if source_path == source.name and src_dir_fd is not None and not raced:
            raced = True
            source.unlink()
            source.write_text("third-party replacement", encoding="utf-8")
        original_rename(
            source_path,
            destination_path,
            src_dir_fd=src_dir_fd,
            dst_dir_fd=dst_dir_fd,
        )

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
    monkeypatch.setattr(file_organizer.os, "rename", racing_rename)

    with pytest.raises(FileNotFoundError, match="changed during execution"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "third-party replacement"
    assert not destination.exists()
    retained = [child for child in tmp_path.iterdir() if child.name.startswith(".fo-stage-")]
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
        if not raced:
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
        if not raced:
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
