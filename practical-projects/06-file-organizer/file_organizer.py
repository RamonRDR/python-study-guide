from __future__ import annotations

import ctypes
import errno
import os
import secrets
import stat
import sys
from collections.abc import Callable
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
_RENAME_NOREPLACE = 1
_INTERNAL_PREFIXES = (".fo-stage-", ".fo-recovery-")


def _load_renameat2() -> Callable[..., int] | None:
    """Return Linux renameat2 when libc exposes the no-replace primitive."""
    if not sys.platform.startswith("linux"):
        return None
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        renameat2 = libc.renameat2
    except (OSError, AttributeError):
        return None

    renameat2.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    ]
    renameat2.restype = ctypes.c_int
    return renameat2


_RENAMEAT2 = _load_renameat2()


@dataclass(frozen=True, slots=True)
class _FileIdentity:
    """Stable filesystem identity captured while an object is pinned."""

    device: int
    inode: int


@dataclass(frozen=True, slots=True)
class _PinnedSource:
    """Descriptor and identity accepted together for one planned source."""

    fd: int
    identity: _FileIdentity


def _coerce_path(value: str | PathLike[str], field_name: str) -> Path:
    if isinstance(value, bool) or not isinstance(value, (str, PathLike)):
        raise TypeError(f"{field_name} must be a path-like value")
    try:
        return Path(value)
    except (TypeError, ValueError, OSError) as exc:
        raise TypeError(f"{field_name} must be a valid path-like value") from exc


def _require_source_directory(value: str | PathLike[str]) -> Path:
    path = _coerce_path(value, "source_directory")
    is_junction = getattr(path, "is_junction", None)
    if path.is_symlink() or bool(is_junction is not None and is_junction()):
        raise ValueError("source_directory cannot be a symlink or junction")
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
            f"directory became unsafe during execution: {directory_name}"
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
            f"directory became unsafe during execution: {path.name}"
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
    """Immutable pathname-intent plan produced before filesystem mutation."""

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
        if child.name.startswith(_INTERNAL_PREFIXES):
            continue
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


def _is_directory_redirect(path: Path) -> bool:
    """Return whether a directory entry redirects traversal to another location."""
    if path.is_symlink():
        return True
    is_junction = getattr(path, "is_junction", None)
    return bool(is_junction is not None and is_junction())


def _validate_category_locations(source_directory: Path) -> None:
    for category in FileCategory:
        target = source_directory / category.value
        if _is_directory_redirect(target):
            raise ValueError(
                f"category directory cannot be a symlink or junction: {target.name}"
            )
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
    """Build a deterministic, non-mutating pathname-intent plan."""
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


def _capture_portable_source_identities(
    plan: OrganizationPlan,
) -> dict[Path, _FileIdentity]:
    """Capture best-effort pathname identities for the guarded Windows path."""
    return {
        action.source: _capture_path_identity(action.source) for action in plan.actions
    }


def _supports_secure_directory_fds() -> bool:
    """Return whether Linux can enforce descriptor-anchored no-replace renames."""
    return (
        _RENAMEAT2 is not None
        and hasattr(os, "O_DIRECTORY")
        and hasattr(os, "O_NOFOLLOW")
        and os.open in os.supports_dir_fd
        and os.mkdir in os.supports_dir_fd
        and os.link in os.supports_dir_fd
        and os.rename in os.supports_dir_fd
        and os.stat in os.supports_dir_fd
        and os.stat in os.supports_follow_symlinks
        and os.listdir in os.supports_fd
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


def _verify_root_anchor_at(source_directory: Path, root_fd: int) -> None:
    """Require the pinned root FD to remain reachable at the planned path."""
    pinned = os.fstat(root_fd)
    try:
        current = source_directory.lstat()
    except FileNotFoundError as exc:
        raise ValueError("source_directory moved during execution") from exc

    pinned_identity = _identity_from_directory_stat(
        pinned,
        directory_name=source_directory.name,
    )
    try:
        current_identity = _identity_from_directory_stat(
            current,
            directory_name=source_directory.name,
        )
    except ValueError as exc:
        raise ValueError("source_directory moved during execution") from exc
    if pinned_identity != current_identity:
        raise ValueError("source_directory moved during execution")


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

    try:
        _verify_category_anchor_at(
            root_fd=root_fd,
            category_name=category_name,
            category_fd=category_fd,
        )
    except Exception:
        os.close(category_fd)
        raise
    return category_fd


def _regular_identity_at(filename: str, *, directory_fd: int) -> _FileIdentity:
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


def _open_planned_source_fd_at(
    source_name: str,
    *,
    root_fd: int,
) -> _PinnedSource:
    """Open first, then accept identity from the descriptor pinning the inode."""
    flags = os.O_RDONLY | os.O_NOFOLLOW
    if hasattr(os, "O_NONBLOCK"):
        flags |= os.O_NONBLOCK
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    try:
        source_fd = os.open(source_name, flags, dir_fd=root_fd)
    except PermissionError as exc:
        raise PermissionError(
            f"planned source must be readable for safe execution: {source_name}"
        ) from exc
    except OSError as exc:
        raise FileNotFoundError(
            f"planned source changed during execution: {source_name}"
        ) from exc

    try:
        identity = _identity_from_regular_stat(
            os.fstat(source_fd),
            filename=source_name,
        )
    except Exception:
        os.close(source_fd)
        raise
    return _PinnedSource(fd=source_fd, identity=identity)


def _pin_planned_sources_at(
    plan: OrganizationPlan,
    *,
    root_fd: int,
) -> dict[Path, _PinnedSource]:
    """Pin the current regular file at every planned pathname before mutation.

    OrganizationPlan intentionally stores pathname/category intent, not live file
    descriptors or a durable filesystem-object snapshot. Identity becomes strong
    only when execute_plan opens each pathname and accepts fstat() on that pin.
    """
    pinned: dict[Path, _PinnedSource] = {}
    try:
        for action in plan.actions:
            pinned[action.source] = _open_planned_source_fd_at(
                action.source.name,
                root_fd=root_fd,
            )
    except Exception:
        for source in pinned.values():
            os.close(source.fd)
        raise
    return pinned


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
    if _FileIdentity(stat_result.st_dev, stat_result.st_ino) != expected_identity:
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


def _verify_no_casefold_destination_collision_at(
    destination_name: str,
    *,
    destination_directory_fd: int,
) -> None:
    """Reject a casefold-equivalent entry visible immediately before commit."""
    destination_key = destination_name.casefold()
    try:
        current_names = os.listdir(destination_directory_fd)
    except OSError as exc:
        raise ValueError("category directory became unsafe during execution") from exc

    if any(name.casefold() == destination_key for name in current_names):
        raise FileExistsError(
            f"case-insensitive destination appeared during execution: {destination_name}"
        )


def _verify_no_casefold_destination_collision_path(destination: Path) -> None:
    """Best-effort Windows recheck for a casefold-equivalent destination."""
    destination_key = destination.name.casefold()
    if any(child.name.casefold() == destination_key for child in destination.parent.iterdir()):
        raise FileExistsError(
            f"case-insensitive destination appeared during execution: {destination.name}"
        )


def _make_stage_name(source_name: str) -> str:
    """Return a fixed-length internal name independent of the source filename."""
    del source_name
    return f".fo-stage-{secrets.token_hex(16)}"


def _make_recovery_name(source_name: str) -> str:
    """Return a bounded exclusive name for emergency source-data recovery."""
    del source_name
    return f".fo-recovery-{secrets.token_hex(16)}"


def _recover_pinned_source_at(
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


def _preserve_stage_at(
    stage_name: str,
    source_name: str,
    *,
    root_fd: int,
    expected_identity: _FileIdentity | None = None,
) -> bool:
    """Best-effort restore without deleting raced entries; optionally prove result."""
    try:
        os.link(
            stage_name,
            source_name,
            src_dir_fd=root_fd,
            dst_dir_fd=root_fd,
            follow_symlinks=False,
        )
    except OSError:
        pass

    if expected_identity is None:
        return False

    try:
        restored_identity = _regular_identity_at(
            source_name,
            directory_fd=root_fd,
        )
    except OSError:
        return False
    return restored_identity == expected_identity


def _preserve_claimed_source_after_failure_at(
    stage_name: str,
    source_name: str,
    *,
    root_fd: int,
    source_fd: int,
    expected_identity: _FileIdentity,
) -> str | None:
    """Restore a proven stage or recover pinned bytes when stage identity is uncertain."""
    try:
        staged_identity = _regular_identity_at(stage_name, directory_fd=root_fd)
    except OSError:
        staged_identity = None

    if staged_identity == expected_identity:
        restored = _preserve_stage_at(
            stage_name,
            source_name,
            root_fd=root_fd,
            expected_identity=expected_identity,
        )
        if restored:
            return None

    return _recover_pinned_source_at(
        source_fd,
        source_name,
        root_fd=root_fd,
    )


def _claim_source_at(
    source_name: str,
    *,
    root_fd: int,
    expected_identity: _FileIdentity,
) -> str:
    """Atomically detach the source name and verify the claimed regular file."""
    stage_name = ""
    for _ in range(16):
        stage_name = _make_stage_name(source_name)
        try:
            _rename_no_replace_at(
                source_name,
                stage_name,
                source_directory_fd=root_fd,
                destination_directory_fd=root_fd,
            )
        except FileExistsError:
            continue
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"planned source changed during execution: {source_name}"
            ) from exc
        break
    else:
        raise FileExistsError(
            f"could not allocate staging entry for planned source: {source_name}"
        )

    try:
        staged_identity = _regular_identity_at(stage_name, directory_fd=root_fd)
    except FileNotFoundError as exc:
        _preserve_stage_at(stage_name, source_name, root_fd=root_fd)
        raise FileNotFoundError(
            f"planned source changed during execution: {source_name}"
        ) from exc

    if staged_identity != expected_identity:
        _preserve_stage_at(stage_name, source_name, root_fd=root_fd)
        raise FileNotFoundError(
            f"planned source changed during execution: {source_name}"
        )
    return stage_name


def _rename_no_replace_at(
    source_name: str,
    destination_name: str,
    *,
    source_directory_fd: int,
    destination_directory_fd: int,
) -> None:
    """Atomically rename between pinned directories without replacing destination."""
    if _RENAMEAT2 is None:
        raise NotImplementedError("atomic no-replace rename is unavailable")

    ctypes.set_errno(0)
    result = _RENAMEAT2(
        source_directory_fd,
        os.fsencode(source_name),
        destination_directory_fd,
        os.fsencode(destination_name),
        _RENAME_NOREPLACE,
    )
    if result == 0:
        return

    error_number = ctypes.get_errno()
    if error_number == errno.EEXIST:
        raise FileExistsError(
            error_number,
            "destination appeared during execution",
            destination_name,
        )
    raise OSError(error_number, os.strerror(error_number), destination_name)


def _move_file_no_replace_at(
    source_name: str,
    destination_name: str,
    *,
    source_directory_path: Path,
    source_directory_fd: int,
    destination_directory_fd: int,
    category_name: str,
    source_fd: int,
    expected_identity: _FileIdentity,
) -> None:
    """Commit one move using the source descriptor pinned before mutation."""
    _verify_root_anchor_at(source_directory_path, source_directory_fd)
    _verify_category_anchor_at(
        root_fd=source_directory_fd,
        category_name=category_name,
        category_fd=destination_directory_fd,
    )

    try:
        stage_name = _claim_source_at(
            source_name,
            root_fd=source_directory_fd,
            expected_identity=expected_identity,
        )
    except FileNotFoundError as exc:
        recovery_name = _recover_pinned_source_at(
            source_fd,
            source_name,
            root_fd=source_directory_fd,
        )
        raise FileNotFoundError(
            "planned source changed after it was pinned; "
            f"planned source data retained as {recovery_name}: {source_name}"
        ) from exc

    try:
        _verify_root_anchor_at(source_directory_path, source_directory_fd)
        _verify_category_anchor_at(
            root_fd=source_directory_fd,
            category_name=category_name,
            category_fd=destination_directory_fd,
        )
        staged_identity = _regular_identity_at(
            stage_name,
            directory_fd=source_directory_fd,
        )
        if staged_identity != expected_identity:
            raise FileNotFoundError(
                f"planned source changed during execution: {source_name}"
            )
        _verify_no_casefold_destination_collision_at(
            destination_name,
            destination_directory_fd=destination_directory_fd,
        )
        _rename_no_replace_at(
            stage_name,
            destination_name,
            source_directory_fd=source_directory_fd,
            destination_directory_fd=destination_directory_fd,
        )
    except (FileExistsError, FileNotFoundError, ValueError, OSError) as exc:
        recovery_name = _preserve_claimed_source_after_failure_at(
            stage_name,
            source_name,
            root_fd=source_directory_fd,
            source_fd=source_fd,
            expected_identity=expected_identity,
        )
        if recovery_name is not None:
            exc.add_note(
                "planned source data retained as "
                f"{recovery_name}: {source_name}"
            )
        raise

    try:
        _verify_destination_identity_at(
            destination_name,
            destination_directory_fd=destination_directory_fd,
            expected_identity=expected_identity,
        )
    except RuntimeError as exc:
        recovery_name = _recover_pinned_source_at(
            source_fd,
            source_name,
            root_fd=source_directory_fd,
        )
        raise RuntimeError(
            "destination does not match planned source; "
            f"planned source data retained as {recovery_name}: {destination_name}"
        ) from exc
    _verify_root_anchor_at(source_directory_path, source_directory_fd)
    _verify_category_anchor_at(
        root_fd=source_directory_fd,
        category_name=category_name,
        category_fd=destination_directory_fd,
    )


def _rename_no_replace_path(source: Path, destination: Path) -> None:
    """Portable no-replace rename for Windows; Linux uses descriptor execution."""
    if os.name != "nt":
        raise NotImplementedError(
            "safe execution requires Linux renameat2 or Windows rename semantics"
        )
    try:
        os.rename(source, destination)
    except FileExistsError as exc:
        raise FileExistsError(
            f"destination appeared during execution: {destination.name}"
        ) from exc


def _move_file_no_replace(
    source: Path,
    destination: Path,
    expected_identity: _FileIdentity,
) -> None:
    """Windows fallback using its atomic no-replace rename behavior."""
    _verify_path_identity(source, expected_identity)
    category_identity = _capture_directory_identity(destination.parent)
    _verify_no_casefold_destination_collision_path(destination)
    _rename_no_replace_path(source, destination)
    _verify_destination_path_identity(destination, expected_identity)
    if _capture_directory_identity(destination.parent) != category_identity:
        raise ValueError(
            f"category directory moved during execution: {destination.parent.name}"
        )


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
    if _FileIdentity(stat_result.st_dev, stat_result.st_ino) != expected_identity:
        raise RuntimeError(
            f"destination does not match planned source: {destination.name}"
        )


def _execute_plan_with_directory_fds(
    plan: OrganizationPlan,
) -> OrganizationResult:
    """Execute using sources and directories pinned before Linux mutation."""
    root_fd = _open_source_directory_fd(plan.source_directory)
    pinned_sources: dict[Path, _PinnedSource] = {}
    category_fds: dict[FileCategory, int] = {}

    try:
        _verify_root_anchor_at(plan.source_directory, root_fd)

        # Accept identity only from already-open descriptors. Keeping every
        # descriptor alive prevents accepted inodes from being freed/reused.
        pinned_sources = _pin_planned_sources_at(plan, root_fd=root_fd)

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
            pinned_source = pinned_sources[action.source]
            _move_file_no_replace_at(
                action.source.name,
                action.destination.name,
                source_directory_path=plan.source_directory,
                source_directory_fd=root_fd,
                destination_directory_fd=category_fds[action.category],
                category_name=action.category.value,
                source_fd=pinned_source.fd,
                expected_identity=pinned_source.identity,
            )
            moved.append(action.destination)

        _verify_root_anchor_at(plan.source_directory, root_fd)
        return OrganizationResult(plan=plan, moved_files=tuple(moved))
    finally:
        for directory_fd in category_fds.values():
            os.close(directory_fd)
        for source in pinned_sources.values():
            os.close(source.fd)
        os.close(root_fd)


def _execute_plan_portable(
    plan: OrganizationPlan,
    source_identities: dict[Path, _FileIdentity],
) -> OrganizationResult:
    """Execute on Windows, where os.rename refuses an existing destination."""
    if os.name != "nt":
        raise NotImplementedError(
            "safe execution requires Linux renameat2 or Windows rename semantics"
        )

    for directory in sorted(
        {action.destination.parent for action in plan.actions},
        key=lambda path: (path.name.casefold(), path.name),
    ):
        directory.mkdir(exist_ok=True)
        if _is_directory_redirect(directory) or not directory.is_dir():
            raise ValueError(
                f"category directory became unsafe during execution: {directory.name}"
            )

    moved: list[Path] = []
    for action in plan.actions:
        if _is_directory_redirect(action.destination.parent):
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
    """Execute pathname intent under the strongest supported platform contract.

    A plan does not freeze source-object identity between planning and execution.
    The current regular file at each planned pathname is bound when execution
    starts; changes after that binding are rejected under the platform contract.
    """
    if not isinstance(plan, OrganizationPlan):
        raise TypeError("plan must be an OrganizationPlan")

    _preflight_execution(plan)
    if not plan.actions:
        return OrganizationResult(plan=plan, moved_files=())

    if _supports_secure_directory_fds():
        return _execute_plan_with_directory_fds(plan)

    source_identities = _capture_portable_source_identities(plan)
    return _execute_plan_portable(plan, source_identities)
