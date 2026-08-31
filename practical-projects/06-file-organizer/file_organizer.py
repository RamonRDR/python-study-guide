from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum
from os import PathLike
from pathlib import Path


class FileCategory(str, Enum):
    """Destination categories supported by the organizer."""

    DOCUMENTS = "documents"
    DATA = "data"
    IMAGES = "images"
    ARCHIVES = "archives"
    OTHER = "other"


class CollisionPolicy(str, Enum):
    """How planning handles a destination name that already exists."""

    ERROR = "error"
    SKIP = "skip"


_DOCUMENT_SUFFIXES = frozenset({".txt", ".md", ".pdf", ".doc", ".docx", ".odt"})
_DATA_SUFFIXES = frozenset({".csv", ".json", ".xml", ".xls", ".xlsx"})
_IMAGE_SUFFIXES = frozenset({".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"})
_ARCHIVE_SUFFIXES = frozenset({".zip", ".tar", ".gz", ".bz2", ".xz", ".7z"})
_COMPOUND_ARCHIVE_SUFFIXES = (".tar.gz", ".tar.bz2", ".tar.xz")


def _coerce_path(value: str | PathLike[str], field_name: str) -> Path:
    if isinstance(value, bool) or not isinstance(value, (str, PathLike)):
        raise TypeError(f"{field_name} must be a path-like value")
    try:
        return Path(value)
    except (TypeError, ValueError, OSError) as exc:
        raise TypeError(f"{field_name} must be a valid path-like value") from exc


def _require_source_directory(value: str | PathLike[str]) -> Path:
    path = _coerce_path(value, "source_directory")
    if path.is_symlink():
        raise ValueError("source_directory cannot be a symlink")
    if not path.exists():
        raise FileNotFoundError(f"source_directory does not exist: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"source_directory is not a directory: {path}")
    return path.resolve()


def _path_sort_key(path: Path) -> tuple[str, str]:
    return path.name.casefold(), path.name


@dataclass(frozen=True, slots=True)
class MoveAction:
    """One planned move from the source directory into a category folder."""

    source: Path
    destination: Path
    category: FileCategory

    def __post_init__(self) -> None:
        if not isinstance(self.source, Path) or not isinstance(self.destination, Path):
            raise TypeError("source and destination must be Path values")
        if not isinstance(self.category, FileCategory):
            raise TypeError("category must be a FileCategory")
        if not self.source.is_absolute() or not self.destination.is_absolute():
            raise ValueError("source and destination must be absolute paths")
        if self.source == self.destination:
            raise ValueError("source and destination must differ")
        if self.source.name != self.destination.name:
            raise ValueError("destination must preserve the source filename")
        if self.destination.parent.name != self.category.value:
            raise ValueError("destination directory must match the file category")


@dataclass(frozen=True, slots=True)
class OrganizationPlan:
    """Immutable organization plan produced before filesystem mutation."""

    source_directory: Path
    actions: tuple[MoveAction, ...]
    skipped_collisions: tuple[Path, ...]
    ignored_symlinks: tuple[Path, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.source_directory, Path):
            raise TypeError("source_directory must be a Path")
        if not self.source_directory.is_absolute():
            raise ValueError("source_directory must be absolute")
        if not isinstance(self.actions, tuple) or any(
            not isinstance(action, MoveAction) for action in self.actions
        ):
            raise TypeError("actions must be a tuple of MoveAction values")
        for field_name, values in (
            ("skipped_collisions", self.skipped_collisions),
            ("ignored_symlinks", self.ignored_symlinks),
        ):
            if not isinstance(values, tuple) or any(
                not isinstance(path, Path) for path in values
            ):
                raise TypeError(f"{field_name} must be a tuple of Path values")

        for action in self.actions:
            if action.source.parent != self.source_directory:
                raise ValueError("planned sources must be direct children of source_directory")
            if action.destination.parent.parent != self.source_directory:
                raise ValueError(
                    "planned destinations must be category folders inside source_directory"
                )

        for path in (*self.skipped_collisions, *self.ignored_symlinks):
            if not path.is_absolute() or path.parent != self.source_directory:
                raise ValueError(
                    "skipped and ignored paths must be direct children of source_directory"
                )

        expected_actions = tuple(
            sorted(self.actions, key=lambda item: _path_sort_key(item.source))
        )
        if self.actions != expected_actions:
            raise ValueError("actions must be sorted by source filename")

        for field_name, values in (
            ("skipped_collisions", self.skipped_collisions),
            ("ignored_symlinks", self.ignored_symlinks),
        ):
            if values != tuple(sorted(values, key=_path_sort_key)):
                raise ValueError(f"{field_name} must be sorted by filename")

        source_keys = tuple(action.source.name.casefold() for action in self.actions)
        if len(source_keys) != len(set(source_keys)):
            raise ValueError("planned source filenames must be unique case-insensitively")

        destination_keys = tuple(
            (action.category.value, action.destination.name.casefold())
            for action in self.actions
        )
        if len(destination_keys) != len(set(destination_keys)):
            raise ValueError("planned destinations must be unique case-insensitively")

    @property
    def planned_count(self) -> int:
        return len(self.actions)

    @property
    def skipped_collision_count(self) -> int:
        return len(self.skipped_collisions)

    @property
    def ignored_symlink_count(self) -> int:
        return len(self.ignored_symlinks)


@dataclass(frozen=True, slots=True)
class OrganizationResult:
    """Result of successfully executing one complete organization plan."""

    plan: OrganizationPlan
    moved_files: tuple[Path, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.plan, OrganizationPlan):
            raise TypeError("plan must be an OrganizationPlan")
        if not isinstance(self.moved_files, tuple) or any(
            not isinstance(path, Path) for path in self.moved_files
        ):
            raise TypeError("moved_files must be a tuple of Path values")
        expected = tuple(action.destination for action in self.plan.actions)
        if self.moved_files != expected:
            raise ValueError("moved_files must match the plan destinations")

    @property
    def moved_count(self) -> int:
        return len(self.moved_files)


def classify_path(path: str | PathLike[str]) -> FileCategory:
    """Classify a filename by its suffix without reading file contents."""
    value = _coerce_path(path, "path")
    name = value.name.casefold()

    if any(name.endswith(suffix) for suffix in _COMPOUND_ARCHIVE_SUFFIXES):
        return FileCategory.ARCHIVES

    suffix = value.suffix.casefold()
    if suffix in _DOCUMENT_SUFFIXES:
        return FileCategory.DOCUMENTS
    if suffix in _DATA_SUFFIXES:
        return FileCategory.DATA
    if suffix in _IMAGE_SUFFIXES:
        return FileCategory.IMAGES
    if suffix in _ARCHIVE_SUFFIXES:
        return FileCategory.ARCHIVES
    return FileCategory.OTHER


def _scan_source_directory(
    source_directory: Path,
) -> tuple[tuple[Path, ...], tuple[Path, ...]]:
    files: list[Path] = []
    symlinks: list[Path] = []

    for child in sorted(source_directory.iterdir(), key=_path_sort_key):
        if child.is_symlink():
            symlinks.append(child.absolute())
        elif child.is_file():
            files.append(child.absolute())

    return tuple(files), tuple(symlinks)


def discover_files(source_directory: str | PathLike[str]) -> tuple[Path, ...]:
    """Return direct regular-file children in deterministic order."""
    root = _require_source_directory(source_directory)
    files, _ = _scan_source_directory(root)
    return files


def _validate_category_locations(source_directory: Path) -> None:
    for category in FileCategory:
        target = source_directory / category.value
        if target.is_symlink():
            raise ValueError(f"category directory cannot be a symlink: {target.name}")
        if target.exists() and not target.is_dir():
            raise NotADirectoryError(
                f"category path exists but is not a directory: {target.name}"
            )


def _existing_names_casefold(directory: Path) -> set[str]:
    if not directory.exists():
        return set()
    return {child.name.casefold() for child in directory.iterdir()}


def plan_organization(
    source_directory: str | PathLike[str],
    *,
    collision_policy: CollisionPolicy = CollisionPolicy.ERROR,
) -> OrganizationPlan:
    """Build a deterministic, non-mutating plan for direct child files."""
    root = _require_source_directory(source_directory)
    if not isinstance(collision_policy, CollisionPolicy):
        raise TypeError("collision_policy must be a CollisionPolicy")

    _validate_category_locations(root)
    files, symlinks = _scan_source_directory(root)
    existing_by_category = {
        category: _existing_names_casefold(root / category.value)
        for category in FileCategory
    }

    actions: list[MoveAction] = []
    skipped: list[Path] = []
    planned_keys: set[tuple[FileCategory, str]] = set()

    for source in files:
        category = classify_path(source)
        destination = (root / category.value / source.name).absolute()
        key = (category, source.name.casefold())
        collides = (
            source.name.casefold() in existing_by_category[category]
            or key in planned_keys
        )

        if collides:
            if collision_policy is CollisionPolicy.ERROR:
                raise FileExistsError(
                    f"destination already exists for source file: {source.name}"
                )
            skipped.append(source)
            continue

        actions.append(
            MoveAction(
                source=source,
                destination=destination,
                category=category,
            )
        )
        planned_keys.add(key)

    return OrganizationPlan(
        source_directory=root,
        actions=tuple(actions),
        skipped_collisions=tuple(skipped),
        ignored_symlinks=symlinks,
    )


def _preflight_execution(plan: OrganizationPlan) -> None:
    root = _require_source_directory(plan.source_directory)
    if root != plan.source_directory:
        raise ValueError("source_directory no longer resolves to the planned directory")

    _validate_category_locations(root)

    for action in plan.actions:
        if action.source.is_symlink() or not action.source.is_file():
            raise FileNotFoundError(
                f"planned source is no longer a regular file: {action.source.name}"
            )

    for action in plan.actions:
        target_directory = action.destination.parent
        if target_directory.exists():
            current_names = _existing_names_casefold(target_directory)
            if action.destination.name.casefold() in current_names:
                raise FileExistsError(
                    f"destination appeared after planning: {action.destination.name}"
                )
        elif action.destination.exists() or action.destination.is_symlink():
            raise FileExistsError(
                f"destination appeared after planning: {action.destination.name}"
            )


def _move_file_no_replace(source: Path, destination: Path) -> None:
    """Move one regular file without ever replacing an existing destination."""
    try:
        os.link(source, destination, follow_symlinks=False)
    except FileExistsError as exc:
        raise FileExistsError(
            f"destination appeared during execution: {destination.name}"
        ) from exc

    try:
        source.unlink()
    except OSError as exc:
        try:
            destination.unlink()
        except OSError as rollback_exc:
            raise RuntimeError(
                f"move rollback failed for source file: {source.name}"
            ) from rollback_exc
        raise OSError(
            f"could not remove source after creating destination: {source.name}"
        ) from exc


def execute_plan(plan: OrganizationPlan) -> OrganizationResult:
    """Execute a previously validated plan after a full collision preflight."""
    if not isinstance(plan, OrganizationPlan):
        raise TypeError("plan must be an OrganizationPlan")

    _preflight_execution(plan)

    for directory in sorted(
        {action.destination.parent for action in plan.actions},
        key=lambda path: (path.name.casefold(), path.name),
    ):
        directory.mkdir(exist_ok=True)

    moved: list[Path] = []
    for action in plan.actions:
        _move_file_no_replace(action.source, action.destination)
        moved.append(action.destination)

    return OrganizationResult(plan=plan, moved_files=tuple(moved))
