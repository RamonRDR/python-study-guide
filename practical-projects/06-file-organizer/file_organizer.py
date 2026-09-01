from __future__ import annotations

import os
import secrets
import stat
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


@dataclass(frozen=True, slots=True)
class _FileIdentity:
    """Stable filesystem identity captured before mutation."""

    device: int
    inode: int


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


def _identity_from_regular_stat(
    stat_result: os.stat_result,
    *,
    filename: str,
) -> _FileIdentity:
    if not stat.S_ISREG(stat_result.st_mode):
        raise FileNotFoundError(
            f"planned source is no longer a regular file: {filename}"
        )
    return _FileIdentity(stat_result.st_dev, stat_result.st_ino)


def _identity_from_directory_stat(
    stat_result: os.stat_result,
    *,
    directory_name: str,
) -> _FileIdentity:
    if not stat.S_ISDIR(stat_result.st_mode):
        raise ValueError(
            f"category directory became unsafe during execution: {directory_name}"
        )
    return _FileIdentity(stat_result.st_dev, stat_result.st_ino)


def _capture_path_identity(path: Path) -> _FileIdentity:
    try:
        stat_result = path.lstat()
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"planned source is no longer a regular file: {path.name}"
        ) from exc
    return _identity_from_regular_stat(stat_result, filename=path.name)


def _capture_directory_identity(path: Path) -> _FileIdentity:
    try:
        stat_result = path.lstat()
    except FileNotFoundError as exc:
        raise ValueError(
            f"category directory became unsafe during execution: {path.name}"
        ) from exc
    return _identity_from_directory_stat(stat_result, directory_name=path.name)


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


def _preflight_execution(plan: OrganizationPlan) -> dict[Path, _FileIdentity]:
    root = _require_source_directory(plan.source_directory)
    if root != plan.source_directory:
        raise ValueError("source_directory no longer resolves to the planned directory")

    _validate_category_locations(root)

    source_identities = {
        action.source: _capture_path_identity(action.source) for action in plan.actions
    }

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

    return source_identities


def _supports_secure_directory_fds() -> bool:
    """Return whether the platform can enforce no-follow directory mutation."""
    return (
        hasattr(os, "O_DIRECTORY")
        and hasattr(os, "O_NOFOLLOW")
        and os.open in os.supports_dir_fd
        and os.mkdir in os.supports_dir_fd
        and os.link in os.supports_dir_fd
        and os.unlink in os.supports_dir_fd
        and os.rename in os.supports_dir_fd
        and os.stat in os.supports_dir_fd
        and os.stat in os.supports_follow_symlinks
    )


def _directory_open_flags() -> int:
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    return flags


def _open_source_directory_fd(source_directory: Path) -> int:
    try:
        return os.open(source_directory, _directory_open_flags())
    except OSError as exc:
        raise ValueError("source_directory became unsafe during execution") from exc


def _open_category_directory_fd(root_fd: int, category_name: str) -> int:
    """Create/open one category directory without following a late symlink."""
    try:
        os.mkdir(category_name, dir_fd=root_fd)
    except FileExistsError:
        pass

    try:
        category_fd = os.open(category_name, _directory_open_flags(), dir_fd=root_fd)
    except OSError as exc:
        raise ValueError(
            f"category directory became unsafe during execution: {category_name}"
        ) from exc

    _verify_category_anchor_at(
        root_fd=root_fd,
        category_name=category_name,
        category_fd=category_fd,
    )
    return category_fd


def _regular_identity_at(
    filename: str,
    *,
    directory_fd: int,
) -> _FileIdentity:
    try:
        stat_result = os.stat(
            filename,
            dir_fd=directory_fd,
            follow_symlinks=False,
        )
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"planned source is no longer a regular file: {filename}"
        ) from exc
    return _identity_from_regular_stat(stat_result, filename=filename)


def _verify_source_identity_at(
    source_name: str,
    *,
    source_directory_fd: int,
    expected_identity: _FileIdentity,
) -> None:
    current_identity = _regular_identity_at(
        source_name,
        directory_fd=source_directory_fd,
    )
    if current_identity != expected_identity:
        raise FileNotFoundError(
            f"planned source changed during execution: {source_name}"
        )


def _verify_destination_identity_at(
    destination_name: str,
    *,
    destination_directory_fd: int,
    expected_identity: _FileIdentity,
) -> None:
    try:
        stat_result = os.stat(
            destination_name,
            dir_fd=destination_directory_fd,
            follow_symlinks=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"destination changed during execution: {destination_name}"
        ) from exc

    if not stat.S_ISREG(stat_result.st_mode):
        raise RuntimeError(
            f"destination does not match planned source: {destination_name}"
        )

    destination_identity = _FileIdentity(stat_result.st_dev, stat_result.st_ino)
    if destination_identity != expected_identity:
        raise RuntimeError(
            f"destination does not match planned source: {destination_name}"
        )


def _verify_category_anchor_at(
    *,
    root_fd: int,
    category_name: str,
    category_fd: int,
) -> None:
    """Require the pinned category FD to remain the named child of the root."""
    pinned = os.fstat(category_fd)
    try:
        current = os.stat(
            category_name,
            dir_fd=root_fd,
            follow_symlinks=False,
        )
    except FileNotFoundError as exc:
        raise ValueError(
            f"category directory moved during execution: {category_name}"
        ) from exc

    pinned_identity = _identity_from_directory_stat(
        pinned,
        directory_name=category_name,
    )
    current_identity = _identity_from_directory_stat(
        current,
        directory_name=category_name,
    )
    if pinned_identity != current_identity:
        raise ValueError(
            f"category directory moved during execution: {category_name}"
        )


def _make_stage_name(source_name: str) -> str:
    return f".file-organizer-stage-{secrets.token_hex(16)}-{source_name}"


def _restore_staged_regular_at(
    stage_name: str,
    source_name: str,
    *,
    root_fd: int,
    expected_identity: _FileIdentity,
) -> None:
    """Best-effort no-replace restore of a verified staged regular file."""
    try:
        stage_identity = _regular_identity_at(stage_name, directory_fd=root_fd)
    except FileNotFoundError:
        return
    if stage_identity != expected_identity:
        return

    try:
        os.link(
            stage_name,
            source_name,
            src_dir_fd=root_fd,
            dst_dir_fd=root_fd,
            follow_symlinks=False,
        )
    except FileExistsError:
        return
    try:
        os.unlink(stage_name, dir_fd=root_fd)
    except OSError:
        pass


def _restore_destination_to_source_at(
    destination_name: str,
    source_name: str,
    *,
    root_fd: int,
    destination_directory_fd: int,
    expected_identity: _FileIdentity,
) -> None:
    """Best-effort no-replace restore from a pinned destination to the source."""
    try:
        _verify_destination_identity_at(
            destination_name,
            destination_directory_fd=destination_directory_fd,
            expected_identity=expected_identity,
        )
        os.link(
            destination_name,
            source_name,
            src_dir_fd=destination_directory_fd,
            dst_dir_fd=root_fd,
            follow_symlinks=False,
        )
    except OSError:
        return


def _restore_staged_entry_no_replace_at(
    stage_name: str,
    source_name: str,
    *,
    root_fd: int,
) -> None:
    """Restore a staged non-directory entry without replacing a new source."""
    try:
        os.link(
            stage_name,
            source_name,
            src_dir_fd=root_fd,
            dst_dir_fd=root_fd,
            follow_symlinks=False,
        )
    except OSError:
        return
    try:
        os.unlink(stage_name, dir_fd=root_fd)
    except OSError:
        pass


def _claim_source_at(
    source_name: str,
    *,
    root_fd: int,
    expected_identity: _FileIdentity,
) -> str:
    """Atomically detach the current source entry, then verify what was claimed."""
    stage_name = _make_stage_name(source_name)
    os.rename(
        source_name,
        stage_name,
        src_dir_fd=root_fd,
        dst_dir_fd=root_fd,
    )

    try:
        staged_identity = _regular_identity_at(stage_name, directory_fd=root_fd)
    except FileNotFoundError as exc:
        _restore_staged_entry_no_replace_at(
            stage_name,
            source_name,
            root_fd=root_fd,
        )
        raise FileNotFoundError(
            f"planned source changed during execution: {source_name}"
        ) from exc

    if staged_identity != expected_identity:
        _restore_staged_entry_no_replace_at(
            stage_name,
            source_name,
            root_fd=root_fd,
        )
        raise FileNotFoundError(
            f"planned source changed during execution: {source_name}"
        )

    return stage_name


def _move_file_no_replace_at(
    source_name: str,
    destination_name: str,
    *,
    source_directory_fd: int,
    destination_directory_fd: int,
    category_name: str,
    expected_identity: _FileIdentity,
) -> None:
    """Move one file without deleting an entry that changed after verification."""
    _verify_source_identity_at(
        source_name,
        source_directory_fd=source_directory_fd,
        expected_identity=expected_identity,
    )
    _verify_category_anchor_at(
        root_fd=source_directory_fd,
        category_name=category_name,
        category_fd=destination_directory_fd,
    )

    try:
        os.link(
            source_name,
            destination_name,
            src_dir_fd=source_directory_fd,
            dst_dir_fd=destination_directory_fd,
            follow_symlinks=False,
        )
    except FileExistsError as exc:
        raise FileExistsError(
            f"destination appeared during execution: {destination_name}"
        ) from exc

    _verify_destination_identity_at(
        destination_name,
        destination_directory_fd=destination_directory_fd,
        expected_identity=expected_identity,
    )
    _verify_category_anchor_at(
        root_fd=source_directory_fd,
        category_name=category_name,
        category_fd=destination_directory_fd,
    )

    stage_name = _claim_source_at(
        source_name,
        root_fd=source_directory_fd,
        expected_identity=expected_identity,
    )

    try:
        _verify_category_anchor_at(
            root_fd=source_directory_fd,
            category_name=category_name,
            category_fd=destination_directory_fd,
        )
    except ValueError:
        _restore_staged_regular_at(
            stage_name,
            source_name,
            root_fd=source_directory_fd,
            expected_identity=expected_identity,
        )
        raise

    try:
        os.unlink(stage_name, dir_fd=source_directory_fd)
    except OSError as exc:
        _restore_staged_regular_at(
            stage_name,
            source_name,
            root_fd=source_directory_fd,
            expected_identity=expected_identity,
        )
        raise OSError(
            f"could not finalize source removal safely: {source_name}"
        ) from exc

    try:
        _verify_category_anchor_at(
            root_fd=source_directory_fd,
            category_name=category_name,
            category_fd=destination_directory_fd,
        )
    except ValueError:
        _restore_destination_to_source_at(
            destination_name,
            source_name,
            root_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
            expected_identity=expected_identity,
        )
        raise


def _verify_path_identity(path: Path, expected_identity: _FileIdentity) -> None:
    current_identity = _capture_path_identity(path)
    if current_identity != expected_identity:
        raise FileNotFoundError(
            f"planned source changed during execution: {path.name}"
        )


def _verify_destination_path_identity(
    destination: Path,
    expected_identity: _FileIdentity,
) -> None:
    try:
        stat_result = destination.lstat()
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"destination changed during execution: {destination.name}"
        ) from exc

    if not stat.S_ISREG(stat_result.st_mode):
        raise RuntimeError(
            f"destination does not match planned source: {destination.name}"
        )

    destination_identity = _FileIdentity(stat_result.st_dev, stat_result.st_ino)
    if destination_identity != expected_identity:
        raise RuntimeError(
            f"destination does not match planned source: {destination.name}"
        )


def _stage_source_path(source: Path, expected_identity: _FileIdentity) -> Path:
    """Atomically move a source name to a unique internal staging name."""
    stage = source.with_name(_make_stage_name(source.name))
    os.rename(source, stage)
    try:
        _verify_path_identity(stage, expected_identity)
    except FileNotFoundError:
        try:
            os.link(stage, source, follow_symlinks=False)
        except OSError:
            pass
        else:
            try:
                stage.unlink()
            except OSError:
                pass
        raise
    return stage


def _restore_staged_path(
    stage: Path,
    source: Path,
    expected_identity: _FileIdentity,
) -> None:
    try:
        _verify_path_identity(stage, expected_identity)
        os.link(stage, source, follow_symlinks=False)
    except OSError:
        return
    try:
        stage.unlink()
    except OSError:
        pass


def _move_file_no_replace(
    source: Path,
    destination: Path,
    expected_identity: _FileIdentity,
) -> None:
    """Portable fallback using a staged source detach instead of source unlink."""
    _verify_path_identity(source, expected_identity)
    category_identity = _capture_directory_identity(destination.parent)

    try:
        os.link(source, destination, follow_symlinks=False)
    except FileExistsError as exc:
        raise FileExistsError(
            f"destination appeared during execution: {destination.name}"
        ) from exc

    _verify_destination_path_identity(destination, expected_identity)
    if _capture_directory_identity(destination.parent) != category_identity:
        raise ValueError(
            f"category directory moved during execution: {destination.parent.name}"
        )

    stage = _stage_source_path(source, expected_identity)

    if _capture_directory_identity(destination.parent) != category_identity:
        _restore_staged_path(stage, source, expected_identity)
        raise ValueError(
            f"category directory moved during execution: {destination.parent.name}"
        )

    try:
        stage.unlink()
    except OSError as exc:
        _restore_staged_path(stage, source, expected_identity)
        raise OSError(
            f"could not finalize source removal safely: {source.name}"
        ) from exc

    if _capture_directory_identity(destination.parent) != category_identity:
        try:
            os.link(destination, source, follow_symlinks=False)
        except OSError:
            pass
        raise ValueError(
            f"category directory moved during execution: {destination.parent.name}"
        )


def _execute_plan_with_directory_fds(
    plan: OrganizationPlan,
    source_identities: dict[Path, _FileIdentity],
) -> OrganizationResult:
    """Execute using pinned no-follow directory descriptors when supported."""
    root_fd = _open_source_directory_fd(plan.source_directory)
    category_fds: dict[FileCategory, int] = {}

    try:
        for category in sorted(
            {action.category for action in plan.actions},
            key=lambda item: item.value,
        ):
            category_fds[category] = _open_category_directory_fd(
                root_fd,
                category.value,
            )

        moved: list[Path] = []
        for action in plan.actions:
            _move_file_no_replace_at(
                action.source.name,
                action.destination.name,
                source_directory_fd=root_fd,
                destination_directory_fd=category_fds[action.category],
                category_name=action.category.value,
                expected_identity=source_identities[action.source],
            )
            moved.append(action.destination)

        return OrganizationResult(plan=plan, moved_files=tuple(moved))
    finally:
        for directory_fd in category_fds.values():
            os.close(directory_fd)
        os.close(root_fd)


def _execute_plan_portable(
    plan: OrganizationPlan,
    source_identities: dict[Path, _FileIdentity],
) -> OrganizationResult:
    """Execute on platforms without directory-descriptor no-follow support."""
    for directory in sorted(
        {action.destination.parent for action in plan.actions},
        key=lambda path: (path.name.casefold(), path.name),
    ):
        directory.mkdir(exist_ok=True)
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError(
                f"category directory became unsafe during execution: {directory.name}"
            )

    moved: list[Path] = []
    for action in plan.actions:
        if action.destination.parent.is_symlink():
            raise ValueError(
                "category directory became unsafe during execution: "
                f"{action.destination.parent.name}"
            )
        _move_file_no_replace(
            action.source,
            action.destination,
            source_identities[action.source],
        )
        moved.append(action.destination)

    return OrganizationResult(plan=plan, moved_files=tuple(moved))


def execute_plan(plan: OrganizationPlan) -> OrganizationResult:
    """Execute a previously validated plan after a full collision preflight."""
    if not isinstance(plan, OrganizationPlan):
        raise TypeError("plan must be an OrganizationPlan")

    source_identities = _preflight_execution(plan)

    if _supports_secure_directory_fds():
        return _execute_plan_with_directory_fds(plan, source_identities)
    return _execute_plan_portable(plan, source_identities)
