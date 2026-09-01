import os
import subprocess
from pathlib import Path

import pytest

import file_organizer
from file_organizer import (
    CollisionPolicy,
    FileCategory,
    MoveAction,
    OrganizationPlan,
    OrganizationResult,
    classify_path,
    discover_files,
    execute_plan,
    plan_organization,
)


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("notes.txt", FileCategory.DOCUMENTS),
        ("README.MD", FileCategory.DOCUMENTS),
        ("report.pdf", FileCategory.DOCUMENTS),
        ("records.csv", FileCategory.DATA),
        ("payload.JSON", FileCategory.DATA),
        ("sheet.xlsx", FileCategory.DATA),
        ("photo.png", FileCategory.IMAGES),
        ("photo.JPEG", FileCategory.IMAGES),
        ("vector.svg", FileCategory.IMAGES),
        ("backup.zip", FileCategory.ARCHIVES),
        ("backup.tar.gz", FileCategory.ARCHIVES),
        ("backup.TAR.XZ", FileCategory.ARCHIVES),
        ("script.py", FileCategory.OTHER),
        ("LICENSE", FileCategory.OTHER),
    ],
)
def test_classify_path_by_suffix(name: str, expected: FileCategory) -> None:
    assert classify_path(name) is expected


@pytest.mark.parametrize("value", [None, 42, True, 3.14])
def test_classify_path_rejects_non_path_like_values(value: object) -> None:
    with pytest.raises(TypeError, match="path-like"):
        classify_path(value)  # type: ignore[arg-type]


def test_discover_files_returns_direct_regular_files_in_deterministic_order(tmp_path: Path) -> None:
    (tmp_path / "b.txt").write_text("b", encoding="utf-8")
    (tmp_path / "A.txt").write_text("a", encoding="utf-8")
    (tmp_path / "nested").mkdir()
    (tmp_path / "nested" / "ignored.txt").write_text("x", encoding="utf-8")

    files = discover_files(tmp_path)

    assert tuple(path.name for path in files) == ("A.txt", "b.txt")
    assert all(path.is_absolute() for path in files)


def test_discover_files_ignores_symlinks(tmp_path: Path) -> None:
    target = tmp_path / "target.txt"
    target.write_text("x", encoding="utf-8")
    link = tmp_path / "linked.txt"
    try:
        link.symlink_to(target)
    except OSError:
        pytest.skip("symlinks are not available in this environment")

    assert tuple(path.name for path in discover_files(tmp_path)) == ("target.txt",)


def test_discover_files_accepts_string_directory(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("x", encoding="utf-8")
    assert discover_files(str(tmp_path))[0].name == "a.txt"


def test_discover_files_rejects_missing_directory(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        discover_files(tmp_path / "missing")


def test_discover_files_rejects_regular_file(tmp_path: Path) -> None:
    source = tmp_path / "file.txt"
    source.write_text("x", encoding="utf-8")
    with pytest.raises(NotADirectoryError):
        discover_files(source)


def test_discover_files_rejects_symlink_source_directory(tmp_path: Path) -> None:
    real = tmp_path / "real"
    real.mkdir()
    link = tmp_path / "link"
    try:
        link.symlink_to(real, target_is_directory=True)
    except OSError:
        pytest.skip("symlinks are not available in this environment")

    with pytest.raises(ValueError, match="cannot be a symlink"):
        discover_files(link)


def test_plan_organization_builds_expected_categories_without_mutating(tmp_path: Path) -> None:
    for name in ("notes.txt", "rows.csv", "image.png", "backup.zip", "script.py"):
        (tmp_path / name).write_text("x", encoding="utf-8")

    plan = plan_organization(tmp_path)

    assert plan.planned_count == 5
    assert plan.skipped_collision_count == 0
    assert tuple(action.category for action in plan.actions) == (
        FileCategory.ARCHIVES,
        FileCategory.IMAGES,
        FileCategory.DOCUMENTS,
        FileCategory.DATA,
        FileCategory.OTHER,
    )
    assert all(action.source.exists() for action in plan.actions)
    assert not any((tmp_path / category.value).exists() for category in FileCategory)


def test_plan_organization_preserves_filenames(tmp_path: Path) -> None:
    source = tmp_path / "Quarterly Report.PDF"
    source.write_text("x", encoding="utf-8")
    plan = plan_organization(tmp_path)
    action = plan.actions[0]
    assert action.destination.name == source.name
    assert action.destination.parent.name == "documents"


def test_plan_organization_reports_ignored_symlinks(tmp_path: Path) -> None:
    target = tmp_path / "target.txt"
    target.write_text("x", encoding="utf-8")
    link = tmp_path / "linked.txt"
    try:
        link.symlink_to(target)
    except OSError:
        pytest.skip("symlinks are not available in this environment")

    plan = plan_organization(tmp_path)
    assert plan.ignored_symlink_count == 1
    assert plan.ignored_symlinks[0].name == "linked.txt"
    assert tuple(action.source.name for action in plan.actions) == ("target.txt",)


def test_plan_organization_rejects_raw_collision_policy(tmp_path: Path) -> None:
    with pytest.raises(TypeError, match="CollisionPolicy"):
        plan_organization(tmp_path, collision_policy="skip")  # type: ignore[arg-type]


def test_plan_organization_errors_on_existing_destination(tmp_path: Path) -> None:
    (tmp_path / "report.txt").write_text("new", encoding="utf-8")
    documents = tmp_path / "documents"
    documents.mkdir()
    (documents / "report.txt").write_text("old", encoding="utf-8")

    with pytest.raises(FileExistsError, match="report.txt"):
        plan_organization(tmp_path)


def test_plan_organization_detects_casefold_collision(tmp_path: Path) -> None:
    (tmp_path / "Report.TXT").write_text("new", encoding="utf-8")
    documents = tmp_path / "documents"
    documents.mkdir()
    (documents / "report.txt").write_text("old", encoding="utf-8")

    with pytest.raises(FileExistsError):
        plan_organization(tmp_path)


def test_plan_organization_can_skip_existing_destination(tmp_path: Path) -> None:
    (tmp_path / "report.txt").write_text("new", encoding="utf-8")
    (tmp_path / "data.csv").write_text("data", encoding="utf-8")
    documents = tmp_path / "documents"
    documents.mkdir()
    (documents / "report.txt").write_text("old", encoding="utf-8")

    plan = plan_organization(tmp_path, collision_policy=CollisionPolicy.SKIP)

    assert plan.planned_count == 1
    assert plan.skipped_collision_count == 1
    assert plan.skipped_collisions[0].name == "report.txt"
    assert plan.actions[0].source.name == "data.csv"


def test_plan_organization_rejects_category_path_that_is_a_file(tmp_path: Path) -> None:
    (tmp_path / "documents").write_text("not a directory", encoding="utf-8")
    with pytest.raises(NotADirectoryError, match="documents"):
        plan_organization(tmp_path)


def test_plan_organization_rejects_category_directory_symlink(tmp_path: Path) -> None:
    real = tmp_path / "real-documents"
    real.mkdir()
    link = tmp_path / "documents"
    try:
        link.symlink_to(real, target_is_directory=True)
    except OSError:
        pytest.skip("symlinks are not available in this environment")

    with pytest.raises(ValueError, match="category directory cannot be a symlink"):
        plan_organization(tmp_path)


def test_plan_organization_rejects_category_directory_junction(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    source = tmp_path / "notes.txt"
    source.write_text("x", encoding="utf-8")
    documents = tmp_path / "documents"
    documents.mkdir()
    original_is_junction = getattr(Path, "is_junction", lambda self: False)

    def fake_is_junction(path: Path) -> bool:
        return path == documents or original_is_junction(path)

    monkeypatch.setattr(Path, "is_junction", fake_is_junction, raising=False)

    with pytest.raises(ValueError, match="symlink or junction"):
        plan_organization(tmp_path)

    assert source.read_text(encoding="utf-8") == "x"


def test_windows_portable_execution_rejects_late_category_junction(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    source = tmp_path / "notes.txt"
    source.write_text("planned", encoding="utf-8")
    plan = plan_organization(tmp_path)
    documents = tmp_path / "documents"
    identities = {source.resolve(): file_organizer._capture_path_identity(source.resolve())}
    original_is_junction = getattr(Path, "is_junction", lambda self: False)

    def fake_is_junction(path: Path) -> bool:
        return path == documents or original_is_junction(path)

    monkeypatch.setattr(Path, "is_junction", fake_is_junction, raising=False)
    monkeypatch.setattr(file_organizer.os, "name", "nt")

    with pytest.raises(ValueError, match="category directory became unsafe"):
        file_organizer._execute_plan_portable(plan, identities)

    assert source.read_text(encoding="utf-8") == "planned"
    assert not (documents / "notes.txt").exists()


def test_plan_empty_directory_is_valid(tmp_path: Path) -> None:
    plan = plan_organization(tmp_path)
    assert plan.actions == ()
    assert plan.skipped_collisions == ()
    assert plan.ignored_symlinks == ()


def test_move_action_validates_category_type(tmp_path: Path) -> None:
    source = (tmp_path / "a.txt").absolute()
    destination = (tmp_path / "documents" / "a.txt").absolute()
    with pytest.raises(TypeError, match="FileCategory"):
        MoveAction(source, destination, "documents")  # type: ignore[arg-type]


def test_move_action_requires_absolute_paths(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="absolute"):
        MoveAction(Path("a.txt"), Path("documents/a.txt"), FileCategory.DOCUMENTS)


def test_move_action_requires_preserved_filename(tmp_path: Path) -> None:
    source = (tmp_path / "a.txt").absolute()
    destination = (tmp_path / "documents" / "b.txt").absolute()
    with pytest.raises(ValueError, match="preserve"):
        MoveAction(source, destination, FileCategory.DOCUMENTS)


def test_move_action_requires_category_directory(tmp_path: Path) -> None:
    source = (tmp_path / "a.txt").absolute()
    destination = (tmp_path / "data" / "a.txt").absolute()
    with pytest.raises(ValueError, match="category"):
        MoveAction(source, destination, FileCategory.DOCUMENTS)


def test_organization_plan_requires_sorted_actions(tmp_path: Path) -> None:
    root = tmp_path.resolve()
    first = MoveAction(root / "a.txt", root / "documents" / "a.txt", FileCategory.DOCUMENTS)
    second = MoveAction(root / "b.txt", root / "documents" / "b.txt", FileCategory.DOCUMENTS)
    with pytest.raises(ValueError, match="sorted"):
        OrganizationPlan(root, (second, first), (), ())


def test_organization_plan_requires_sources_inside_root(tmp_path: Path) -> None:
    root = tmp_path.resolve()
    outside = root.parent / "outside.txt"
    action = MoveAction(outside, root / "documents" / "outside.txt", FileCategory.DOCUMENTS)
    with pytest.raises(ValueError, match="direct children"):
        OrganizationPlan(root, (action,), (), ())


def test_organization_plan_requires_destinations_inside_root(tmp_path: Path) -> None:
    root = tmp_path.resolve()
    source = root / "a.txt"
    destination = root.parent / "documents" / "a.txt"
    action = MoveAction(source, destination, FileCategory.DOCUMENTS)
    with pytest.raises(ValueError, match="category folders inside"):
        OrganizationPlan(root, (action,), (), ())


def test_execute_plan_moves_files_and_creates_only_needed_directories(tmp_path: Path) -> None:
    (tmp_path / "notes.txt").write_text("notes", encoding="utf-8")
    (tmp_path / "rows.csv").write_text("a,b\n1,2\n", encoding="utf-8")
    plan = plan_organization(tmp_path)

    result = execute_plan(plan)

    assert result.moved_count == 2
    assert (tmp_path / "documents" / "notes.txt").read_text(encoding="utf-8") == "notes"
    assert (tmp_path / "data" / "rows.csv").exists()
    assert not (tmp_path / "images").exists()
    assert not (tmp_path / "archives").exists()
    assert not (tmp_path / "other").exists()


def test_execute_plan_preserves_skipped_collision_source(tmp_path: Path) -> None:
    source = tmp_path / "report.txt"
    source.write_text("new", encoding="utf-8")
    documents = tmp_path / "documents"
    documents.mkdir()
    (documents / "report.txt").write_text("old", encoding="utf-8")
    plan = plan_organization(tmp_path, collision_policy=CollisionPolicy.SKIP)

    result = execute_plan(plan)

    assert result.moved_count == 0
    assert source.read_text(encoding="utf-8") == "new"
    assert (documents / "report.txt").read_text(encoding="utf-8") == "old"


def test_execute_plan_rejects_non_plan() -> None:
    with pytest.raises(TypeError, match="OrganizationPlan"):
        execute_plan(object())  # type: ignore[arg-type]


def test_execute_plan_preflights_missing_source_before_mutation(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "b.csv"
    first.write_text("a", encoding="utf-8")
    second.write_text("b", encoding="utf-8")
    plan = plan_organization(tmp_path)
    second.unlink()

    with pytest.raises(FileNotFoundError):
        execute_plan(plan)

    assert first.exists()
    assert not (tmp_path / "documents").exists()
    assert not (tmp_path / "data").exists()


def test_execute_plan_binds_current_source_at_execution_start(tmp_path: Path) -> None:
    source = tmp_path / "notes.txt"
    source.write_text("observed during planning", encoding="utf-8")
    plan = plan_organization(tmp_path)

    source.unlink()
    source.write_text("current at execution start", encoding="utf-8")

    result = execute_plan(plan)

    destination = tmp_path / "documents" / "notes.txt"
    assert result.moved_files == (destination,)
    assert destination.read_text(encoding="utf-8") == "current at execution start"
    assert not source.exists()


def test_execute_plan_preflights_new_exact_collision_before_mutation(tmp_path: Path) -> None:
    first = tmp_path / "a.txt"
    second = tmp_path / "b.csv"
    first.write_text("a", encoding="utf-8")
    second.write_text("b", encoding="utf-8")
    plan = plan_organization(tmp_path)
    documents = tmp_path / "documents"
    documents.mkdir()
    (documents / "a.txt").write_text("existing", encoding="utf-8")

    with pytest.raises(FileExistsError, match="appeared after planning"):
        execute_plan(plan)

    assert first.exists()
    assert second.exists()
    assert not (tmp_path / "data").exists()


def test_execute_plan_preflights_new_casefold_collision_before_mutation(tmp_path: Path) -> None:
    source = tmp_path / "Report.TXT"
    source.write_text("new", encoding="utf-8")
    plan = plan_organization(tmp_path)
    documents = tmp_path / "documents"
    documents.mkdir()
    (documents / "report.txt").write_text("old", encoding="utf-8")

    with pytest.raises(FileExistsError):
        execute_plan(plan)
    assert source.exists()


def test_execute_plan_rejects_category_path_replaced_by_file(tmp_path: Path) -> None:
    source = tmp_path / "a.txt"
    source.write_text("x", encoding="utf-8")
    plan = plan_organization(tmp_path)
    (tmp_path / "documents").write_text("block", encoding="utf-8")

    with pytest.raises(NotADirectoryError):
        execute_plan(plan)
    assert source.exists()


def test_execute_plan_rejects_source_replaced_by_symlink(tmp_path: Path) -> None:
    source = tmp_path / "a.txt"
    source.write_text("x", encoding="utf-8")
    plan = plan_organization(tmp_path)
    source.unlink()
    target = tmp_path / "target.txt"
    target.write_text("target", encoding="utf-8")
    try:
        source.symlink_to(target)
    except OSError:
        pytest.skip("symlinks are not available in this environment")

    with pytest.raises(FileNotFoundError):
        execute_plan(plan)
    assert target.read_text(encoding="utf-8") == "target"


def test_execute_empty_plan_creates_nothing(tmp_path: Path) -> None:
    plan = plan_organization(tmp_path)
    result = execute_plan(plan)
    assert result.moved_files == ()
    assert list(tmp_path.iterdir()) == []


def test_organization_result_requires_exact_destinations(tmp_path: Path) -> None:
    source = tmp_path / "a.txt"
    source.write_text("x", encoding="utf-8")
    plan = plan_organization(tmp_path)
    with pytest.raises(ValueError, match="match"):
        OrganizationResult(plan, ())


def test_organization_result_rejects_non_plan(tmp_path: Path) -> None:
    with pytest.raises(TypeError, match="plan"):
        OrganizationResult(object(), ())  # type: ignore[arg-type]


def test_plan_properties_reflect_counts(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("x", encoding="utf-8")
    plan = plan_organization(tmp_path)
    assert plan.planned_count == len(plan.actions) == 1
    assert plan.skipped_collision_count == 0
    assert plan.ignored_symlink_count == 0


def test_classification_does_not_require_file_to_exist() -> None:
    assert classify_path("fictional/path/report.csv") is FileCategory.DATA


def test_plan_does_not_recurse_into_existing_category_directories(tmp_path: Path) -> None:
    documents = tmp_path / "documents"
    documents.mkdir()
    (documents / "already.txt").write_text("x", encoding="utf-8")
    (tmp_path / "new.txt").write_text("y", encoding="utf-8")

    plan = plan_organization(tmp_path)

    assert tuple(action.source.name for action in plan.actions) == ("new.txt",)


def test_execute_plan_keeps_existing_unrelated_category_files(tmp_path: Path) -> None:
    documents = tmp_path / "documents"
    documents.mkdir()
    existing = documents / "existing.txt"
    existing.write_text("old", encoding="utf-8")
    (tmp_path / "new.txt").write_text("new", encoding="utf-8")
    plan = plan_organization(tmp_path)

    execute_plan(plan)

    assert existing.read_text(encoding="utf-8") == "old"
    assert (documents / "new.txt").read_text(encoding="utf-8") == "new"


def test_internal_recovery_artifacts_are_reserved_from_future_plans(tmp_path: Path) -> None:
    (tmp_path / ".fo-stage-deadbeef").write_text("stage", encoding="utf-8")
    (tmp_path / ".fo-recovery-deadbeef").write_text("recovery", encoding="utf-8")
    (tmp_path / "notes.txt").write_text("user", encoding="utf-8")

    plan = plan_organization(tmp_path)

    assert tuple(action.source.name for action in plan.actions) == ("notes.txt",)


@pytest.mark.skipif(os.name != "nt", reason="requires Windows NTFS junction semantics")
def test_windows_real_source_and_category_junctions_are_rejected(tmp_path: Path) -> None:
    outside = tmp_path / "outside"
    outside.mkdir()

    source_junction = tmp_path / "workspace-link"
    subprocess.run(
        ["cmd", "/c", "mklink", "/J", str(source_junction), str(outside)],
        check=True,
        capture_output=True,
        text=True,
    )
    with pytest.raises(ValueError, match="symlink or junction"):
        plan_organization(source_junction)

    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (workspace / "notes.txt").write_text("x", encoding="utf-8")
    category_junction = workspace / "documents"
    subprocess.run(
        ["cmd", "/c", "mklink", "/J", str(category_junction), str(outside)],
        check=True,
        capture_output=True,
        text=True,
    )
    with pytest.raises(ValueError, match="symlink or junction"):
        plan_organization(workspace)
