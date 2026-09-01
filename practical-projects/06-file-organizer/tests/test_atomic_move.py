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
    original_link = os.link

    def racing_link(
        source_path: str | os.PathLike[str],
        destination_path: str | os.PathLike[str],
        *,
        src_dir_fd: int | None = None,
        dst_dir_fd: int | None = None,
        follow_symlinks: bool = True,
    ) -> None:
        destination.write_text("late destination", encoding="utf-8")
        original_link(
            source_path,
            destination_path,
            src_dir_fd=src_dir_fd,
            dst_dir_fd=dst_dir_fd,
            follow_symlinks=follow_symlinks,
        )

    monkeypatch.setattr(file_organizer.os, "link", racing_link)

    with pytest.raises(FileExistsError, match="during execution"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "planned source"
    assert destination.read_text(encoding="utf-8") == "late destination"


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


def test_source_replacement_between_verify_and_removal_is_never_unlinked(
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
    assert destination.read_text(encoding="utf-8") == "planned source"
    assert not any(
        child.name.startswith(".file-organizer-stage-")
        for child in tmp_path.iterdir()
    )


def test_category_rename_after_fd_open_aborts_before_source_removal(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
    source.write_text("planned source", encoding="utf-8")
    plan = plan_organization(tmp_path)

    category = tmp_path / "documents"
    renamed_category = tmp_path / "documents-detached"
    planned_destination = category / "notes.txt"

    original_link = os.link
    raced = False

    def racing_link(
        source_path: str | os.PathLike[str],
        destination_path: str | os.PathLike[str],
        *,
        src_dir_fd: int | None = None,
        dst_dir_fd: int | None = None,
        follow_symlinks: bool = True,
    ) -> None:
        nonlocal raced
        original_link(
            source_path,
            destination_path,
            src_dir_fd=src_dir_fd,
            dst_dir_fd=dst_dir_fd,
            follow_symlinks=follow_symlinks,
        )
        if (
            destination_path == source.name
            and dst_dir_fd is not None
            and src_dir_fd is not None
            and not raced
        ):
            raced = True
            category.rename(renamed_category)
            category.mkdir()

    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)
    monkeypatch.setattr(file_organizer.os, "link", racing_link)

    with pytest.raises(ValueError, match="category directory moved during execution"):
        execute_plan(plan)

    assert source.read_text(encoding="utf-8") == "planned source"
    assert not planned_destination.exists()
    assert (
        renamed_category / "notes.txt"
    ).read_text(encoding="utf-8") == "planned source"
