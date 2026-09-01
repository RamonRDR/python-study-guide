from pathlib import Path

ROOT = Path('.')
CODE = ROOT / 'practical-projects/06-file-organizer/file_organizer.py'
ATOMIC = ROOT / 'practical-projects/06-file-organizer/tests/test_atomic_move.py'
TESTS = ROOT / 'practical-projects/06-file-organizer/tests/test_file_organizer.py'
README_EN = ROOT / 'practical-projects/06-file-organizer/README.md'
README_PT = ROOT / 'practical-projects/06-file-organizer/README.pt-BR.md'
README_ES = ROOT / 'practical-projects/06-file-organizer/README.es.md'


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding='utf-8')
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{path}: expected one anchor, found {count}')
    path.write_text(text.replace(old, new, 1), encoding='utf-8')


def append_once(path: Path, marker: str, addition: str) -> None:
    text = path.read_text(encoding='utf-8')
    if marker in text:
        raise RuntimeError(f'{path}: marker already present: {marker}')
    path.write_text(text.rstrip() + '\n\n\n' + addition.strip() + '\n', encoding='utf-8')


# Core models and reserved internal namespace.
replace_once(CODE, '_RENAME_NOREPLACE = 1\n_AT_FDCWD = -100\n', '_RENAME_NOREPLACE = 1\n_INTERNAL_PREFIXES = (".fo-stage-", ".fo-recovery-")\n')
replace_once(
    CODE,
    '''@dataclass(frozen=True, slots=True)\nclass _FileIdentity:\n    """Stable filesystem identity captured before mutation."""\n\n    device: int\n    inode: int\n''',
    '''@dataclass(frozen=True, slots=True)\nclass _FileIdentity:\n    """Stable filesystem identity captured while an object is pinned."""\n\n    device: int\n    inode: int\n\n\n@dataclass(frozen=True, slots=True)\nclass _PinnedSource:\n    """Descriptor and identity accepted together for one planned source."""\n\n    fd: int\n    identity: _FileIdentity\n''',
)

# Reject Windows junctions at the workspace root too.
replace_once(
    CODE,
    '''def _require_source_directory(value: str | PathLike[str]) -> Path:\n    path = _coerce_path(value, "source_directory")\n    if path.is_symlink():\n        raise ValueError("source_directory cannot be a symlink")\n''',
    '''def _require_source_directory(value: str | PathLike[str]) -> Path:\n    path = _coerce_path(value, "source_directory")\n    is_junction = getattr(path, "is_junction", None)\n    if path.is_symlink() or bool(is_junction is not None and is_junction()):\n        raise ValueError("source_directory cannot be a symlink or junction")\n''',
)

# Never rediscover the organizer's own conservative recovery/staging artifacts.
replace_once(
    CODE,
    '''def _scan_source_directory(\n    source_directory: Path,\n) -> tuple[tuple[Path, ...], tuple[Path, ...]]:\n    files: list[Path] = []\n    symlinks: list[Path] = []\n\n    for child in sorted(source_directory.iterdir(), key=_path_sort_key):\n        if child.is_symlink():\n            symlinks.append(child.absolute())\n        elif child.is_file():\n            files.append(child.absolute())\n''',
    '''def _scan_source_directory(\n    source_directory: Path,\n) -> tuple[tuple[Path, ...], tuple[Path, ...]]:\n    files: list[Path] = []\n    symlinks: list[Path] = []\n\n    for child in sorted(source_directory.iterdir(), key=_path_sort_key):\n        if child.name.startswith(_INTERNAL_PREFIXES):\n            continue\n        if child.is_symlink():\n            symlinks.append(child.absolute())\n        elif child.is_file():\n            files.append(child.absolute())\n''',
)

# Preflight validates paths/collisions only. Linux accepts identity from open FDs;
# Windows keeps a documented best-effort pathname identity capture.
replace_once(
    CODE,
    '''def _preflight_execution(plan: OrganizationPlan) -> dict[Path, _FileIdentity]:\n    root = _require_source_directory(plan.source_directory)\n    if root != plan.source_directory:\n        raise ValueError("source_directory no longer resolves to the planned directory")\n\n    _validate_category_locations(root)\n\n    source_identities = {\n        action.source: _capture_path_identity(action.source) for action in plan.actions\n    }\n\n    for action in plan.actions:\n        target_directory = action.destination.parent\n        if target_directory.exists():\n            current_names = _existing_names_casefold(target_directory)\n            if action.destination.name.casefold() in current_names:\n                raise FileExistsError(\n                    f"destination appeared after planning: {action.destination.name}"\n                )\n        elif action.destination.exists() or action.destination.is_symlink():\n            raise FileExistsError(\n                f"destination appeared after planning: {action.destination.name}"\n            )\n\n    return source_identities\n''',
    '''def _preflight_execution(plan: OrganizationPlan) -> None:\n    root = _require_source_directory(plan.source_directory)\n    if root != plan.source_directory:\n        raise ValueError("source_directory no longer resolves to the planned directory")\n\n    _validate_category_locations(root)\n\n    for action in plan.actions:\n        target_directory = action.destination.parent\n        if target_directory.exists():\n            current_names = _existing_names_casefold(target_directory)\n            if action.destination.name.casefold() in current_names:\n                raise FileExistsError(\n                    f"destination appeared after planning: {action.destination.name}"\n                )\n        elif action.destination.exists() or action.destination.is_symlink():\n            raise FileExistsError(\n                f"destination appeared after planning: {action.destination.name}"\n            )\n\n\ndef _capture_portable_source_identities(\n    plan: OrganizationPlan,\n) -> dict[Path, _FileIdentity]:\n    """Capture best-effort pathname identities for the guarded Windows path."""\n    return {\n        action.source: _capture_path_identity(action.source) for action in plan.actions\n    }\n''',
)

# Remove obsolete pathname verifier and accept identity only from the pinned FD.
replace_once(
    CODE,
    '''def _verify_source_identity_at(\n    source_name: str,\n    *,\n    source_directory_fd: int,\n    expected_identity: _FileIdentity,\n) -> None:\n    current_identity = _regular_identity_at(\n        source_name,\n        directory_fd=source_directory_fd,\n    )\n    if current_identity != expected_identity:\n        raise FileNotFoundError(\n            f"planned source changed during execution: {source_name}"\n        )\n\n\n''',
    '',
)
replace_once(
    CODE,
    '''def _open_planned_source_fd_at(\n    source_name: str,\n    *,\n    root_fd: int,\n    expected_identity: _FileIdentity,\n) -> int:\n    """Pin the planned inode without blocking on a late special-file replacement."""\n    flags = os.O_RDONLY | os.O_NOFOLLOW\n    if hasattr(os, "O_NONBLOCK"):\n        flags |= os.O_NONBLOCK\n    if hasattr(os, "O_CLOEXEC"):\n        flags |= os.O_CLOEXEC\n    try:\n        source_fd = os.open(source_name, flags, dir_fd=root_fd)\n    except PermissionError as exc:\n        raise PermissionError(\n            f"planned source must be readable for safe execution: {source_name}"\n        ) from exc\n    except OSError as exc:\n        raise FileNotFoundError(\n            f"planned source changed during execution: {source_name}"\n        ) from exc\n\n    try:\n        current_identity = _identity_from_regular_stat(\n            os.fstat(source_fd),\n            filename=source_name,\n        )\n        if current_identity != expected_identity:\n            raise FileNotFoundError(\n                f"planned source changed during execution: {source_name}"\n            )\n    except Exception:\n        os.close(source_fd)\n        raise\n    return source_fd\n\n\n''',
    '''def _open_planned_source_fd_at(\n    source_name: str,\n    *,\n    root_fd: int,\n) -> _PinnedSource:\n    """Open first, then accept identity from the descriptor pinning the inode."""\n    flags = os.O_RDONLY | os.O_NOFOLLOW\n    if hasattr(os, "O_NONBLOCK"):\n        flags |= os.O_NONBLOCK\n    if hasattr(os, "O_CLOEXEC"):\n        flags |= os.O_CLOEXEC\n    try:\n        source_fd = os.open(source_name, flags, dir_fd=root_fd)\n    except PermissionError as exc:\n        raise PermissionError(\n            f"planned source must be readable for safe execution: {source_name}"\n        ) from exc\n    except OSError as exc:\n        raise FileNotFoundError(\n            f"planned source changed during execution: {source_name}"\n        ) from exc\n\n    try:\n        identity = _identity_from_regular_stat(\n            os.fstat(source_fd),\n            filename=source_name,\n        )\n    except Exception:\n        os.close(source_fd)\n        raise\n    return _PinnedSource(fd=source_fd, identity=identity)\n\n\ndef _pin_planned_sources_at(\n    plan: OrganizationPlan,\n    *,\n    root_fd: int,\n) -> dict[Path, _PinnedSource]:\n    """Pin every source before category creation or source mutation."""\n    pinned: dict[Path, _PinnedSource] = {}\n    try:\n        for action in plan.actions:\n            pinned[action.source] = _open_planned_source_fd_at(\n                action.source.name,\n                root_fd=root_fd,\n            )\n    except Exception:\n        for source in pinned.values():\n            os.close(source.fd)\n        raise\n    return pinned\n\n\n''',
)

# Source -> stage also uses no-replace semantics with bounded retries.
replace_once(
    CODE,
    '''    stage_name = _make_stage_name(source_name)\n    os.rename(\n        source_name,\n        stage_name,\n        src_dir_fd=root_fd,\n        dst_dir_fd=root_fd,\n    )\n\n    try:\n''',
    '''    stage_name = ""\n    for _ in range(16):\n        stage_name = _make_stage_name(source_name)\n        try:\n            _rename_no_replace_at(\n                source_name,\n                stage_name,\n                source_directory_fd=root_fd,\n                destination_directory_fd=root_fd,\n            )\n        except FileExistsError:\n            continue\n        except FileNotFoundError as exc:\n            raise FileNotFoundError(\n                f"planned source changed during execution: {source_name}"\n            ) from exc\n        break\n    else:\n        raise FileExistsError(\n            f"could not allocate staging entry for planned source: {source_name}"\n        )\n\n    try:\n''',
)

# Move receives the already-pinned FD and recovers its bytes if pathname claim fails.
replace_once(
    CODE,
    '''def _move_file_no_replace_at(\n    source_name: str,\n    destination_name: str,\n    *,\n    source_directory_path: Path,\n    source_directory_fd: int,\n    destination_directory_fd: int,\n    category_name: str,\n    expected_identity: _FileIdentity,\n) -> None:\n    """Commit one move with anchored directories and no replace/unlink window."""\n    _verify_root_anchor_at(source_directory_path, source_directory_fd)\n    _verify_category_anchor_at(\n        root_fd=source_directory_fd,\n        category_name=category_name,\n        category_fd=destination_directory_fd,\n    )\n    source_fd = _open_planned_source_fd_at(\n        source_name,\n        root_fd=source_directory_fd,\n        expected_identity=expected_identity,\n    )\n\n    try:\n        stage_name = _claim_source_at(\n            source_name,\n            root_fd=source_directory_fd,\n            expected_identity=expected_identity,\n        )\n\n        try:\n            _verify_root_anchor_at(source_directory_path, source_directory_fd)\n            _verify_category_anchor_at(\n                root_fd=source_directory_fd,\n                category_name=category_name,\n                category_fd=destination_directory_fd,\n            )\n            staged_identity = _regular_identity_at(\n                stage_name,\n                directory_fd=source_directory_fd,\n            )\n            if staged_identity != expected_identity:\n                raise FileNotFoundError(\n                    f"planned source changed during execution: {source_name}"\n                )\n            _verify_no_casefold_destination_collision_at(\n                destination_name,\n                destination_directory_fd=destination_directory_fd,\n            )\n            _rename_no_replace_at(\n                stage_name,\n                destination_name,\n                source_directory_fd=source_directory_fd,\n                destination_directory_fd=destination_directory_fd,\n            )\n        except (FileExistsError, FileNotFoundError, ValueError, OSError):\n            _preserve_stage_at(stage_name, source_name, root_fd=source_directory_fd)\n            raise\n\n        try:\n            _verify_destination_identity_at(\n                destination_name,\n                destination_directory_fd=destination_directory_fd,\n                expected_identity=expected_identity,\n            )\n        except RuntimeError as exc:\n            recovery_name = _recover_pinned_source_at(\n                source_fd,\n                source_name,\n                root_fd=source_directory_fd,\n            )\n            raise RuntimeError(\n                "destination does not match planned source; "\n                f"planned source data retained as {recovery_name}: {destination_name}"\n            ) from exc\n        _verify_root_anchor_at(source_directory_path, source_directory_fd)\n        _verify_category_anchor_at(\n            root_fd=source_directory_fd,\n            category_name=category_name,\n            category_fd=destination_directory_fd,\n        )\n    finally:\n        os.close(source_fd)\n\n\n''',
    '''def _move_file_no_replace_at(\n    source_name: str,\n    destination_name: str,\n    *,\n    source_directory_path: Path,\n    source_directory_fd: int,\n    destination_directory_fd: int,\n    category_name: str,\n    source_fd: int,\n    expected_identity: _FileIdentity,\n) -> None:\n    """Commit one move using the source descriptor pinned before mutation."""\n    _verify_root_anchor_at(source_directory_path, source_directory_fd)\n    _verify_category_anchor_at(\n        root_fd=source_directory_fd,\n        category_name=category_name,\n        category_fd=destination_directory_fd,\n    )\n\n    try:\n        stage_name = _claim_source_at(\n            source_name,\n            root_fd=source_directory_fd,\n            expected_identity=expected_identity,\n        )\n    except FileNotFoundError as exc:\n        recovery_name = _recover_pinned_source_at(\n            source_fd,\n            source_name,\n            root_fd=source_directory_fd,\n        )\n        raise FileNotFoundError(\n            "planned source changed after it was pinned; "\n            f"planned source data retained as {recovery_name}: {source_name}"\n        ) from exc\n\n    try:\n        _verify_root_anchor_at(source_directory_path, source_directory_fd)\n        _verify_category_anchor_at(\n            root_fd=source_directory_fd,\n            category_name=category_name,\n            category_fd=destination_directory_fd,\n        )\n        staged_identity = _regular_identity_at(\n            stage_name,\n            directory_fd=source_directory_fd,\n        )\n        if staged_identity != expected_identity:\n            raise FileNotFoundError(\n                f"planned source changed during execution: {source_name}"\n            )\n        _verify_no_casefold_destination_collision_at(\n            destination_name,\n            destination_directory_fd=destination_directory_fd,\n        )\n        _rename_no_replace_at(\n            stage_name,\n            destination_name,\n            source_directory_fd=source_directory_fd,\n            destination_directory_fd=destination_directory_fd,\n        )\n    except (FileExistsError, FileNotFoundError, ValueError, OSError):\n        _preserve_stage_at(stage_name, source_name, root_fd=source_directory_fd)\n        raise\n\n    try:\n        _verify_destination_identity_at(\n            destination_name,\n            destination_directory_fd=destination_directory_fd,\n            expected_identity=expected_identity,\n        )\n    except RuntimeError as exc:\n        recovery_name = _recover_pinned_source_at(\n            source_fd,\n            source_name,\n            root_fd=source_directory_fd,\n        )\n        raise RuntimeError(\n            "destination does not match planned source; "\n            f"planned source data retained as {recovery_name}: {destination_name}"\n        ) from exc\n    _verify_root_anchor_at(source_directory_path, source_directory_fd)\n    _verify_category_anchor_at(\n        root_fd=source_directory_fd,\n        category_name=category_name,\n        category_fd=destination_directory_fd,\n    )\n\n\n''',
)

# Linux pins all sources before any category directory is created and keeps them open.
replace_once(
    CODE,
    '''def _execute_plan_with_directory_fds(\n    plan: OrganizationPlan,\n    source_identities: dict[Path, _FileIdentity],\n) -> OrganizationResult:\n    """Execute using pinned no-follow directory descriptors on Linux."""\n    root_fd = _open_source_directory_fd(plan.source_directory)\n    category_fds: dict[FileCategory, int] = {}\n\n    try:\n        _verify_root_anchor_at(plan.source_directory, root_fd)\n\n        # Readability is a deliberate secure-execution prerequisite because\n        # pinned-FD recovery must be able to persist the planned source bytes.\n        for action in plan.actions:\n            validation_fd = _open_planned_source_fd_at(\n                action.source.name,\n                root_fd=root_fd,\n                expected_identity=source_identities[action.source],\n            )\n            os.close(validation_fd)\n\n        for category in sorted(\n            {action.category for action in plan.actions},\n            key=lambda item: item.value,\n        ):\n            category_fds[category] = _open_category_directory_fd(\n                root_fd,\n                category.value,\n            )\n\n        moved: list[Path] = []\n        for action in plan.actions:\n            _move_file_no_replace_at(\n                action.source.name,\n                action.destination.name,\n                source_directory_path=plan.source_directory,\n                source_directory_fd=root_fd,\n                destination_directory_fd=category_fds[action.category],\n                category_name=action.category.value,\n                expected_identity=source_identities[action.source],\n            )\n            moved.append(action.destination)\n\n        _verify_root_anchor_at(plan.source_directory, root_fd)\n        return OrganizationResult(plan=plan, moved_files=tuple(moved))\n    finally:\n        for directory_fd in category_fds.values():\n            os.close(directory_fd)\n        os.close(root_fd)\n\n\n''',
    '''def _execute_plan_with_directory_fds(\n    plan: OrganizationPlan,\n) -> OrganizationResult:\n    """Execute using sources and directories pinned before Linux mutation."""\n    root_fd = _open_source_directory_fd(plan.source_directory)\n    pinned_sources: dict[Path, _PinnedSource] = {}\n    category_fds: dict[FileCategory, int] = {}\n\n    try:\n        _verify_root_anchor_at(plan.source_directory, root_fd)\n\n        # Accept identity only from already-open descriptors. Keeping every\n        # descriptor alive prevents accepted inodes from being freed/reused.\n        pinned_sources = _pin_planned_sources_at(plan, root_fd=root_fd)\n\n        for category in sorted(\n            {action.category for action in plan.actions},\n            key=lambda item: item.value,\n        ):\n            category_fds[category] = _open_category_directory_fd(\n                root_fd,\n                category.value,\n            )\n\n        moved: list[Path] = []\n        for action in plan.actions:\n            pinned_source = pinned_sources[action.source]\n            _move_file_no_replace_at(\n                action.source.name,\n                action.destination.name,\n                source_directory_path=plan.source_directory,\n                source_directory_fd=root_fd,\n                destination_directory_fd=category_fds[action.category],\n                category_name=action.category.value,\n                source_fd=pinned_source.fd,\n                expected_identity=pinned_source.identity,\n            )\n            moved.append(action.destination)\n\n        _verify_root_anchor_at(plan.source_directory, root_fd)\n        return OrganizationResult(plan=plan, moved_files=tuple(moved))\n    finally:\n        for directory_fd in category_fds.values():\n            os.close(directory_fd)\n        for source in pinned_sources.values():\n            os.close(source.fd)\n        os.close(root_fd)\n\n\n''',
)
replace_once(
    CODE,
    '''def execute_plan(plan: OrganizationPlan) -> OrganizationResult:\n    """Execute a previously validated plan after a full collision preflight."""\n    if not isinstance(plan, OrganizationPlan):\n        raise TypeError("plan must be an OrganizationPlan")\n\n    source_identities = _preflight_execution(plan)\n    if not plan.actions:\n        return OrganizationResult(plan=plan, moved_files=())\n\n    if _supports_secure_directory_fds():\n        return _execute_plan_with_directory_fds(plan, source_identities)\n    return _execute_plan_portable(plan, source_identities)\n''',
    '''def execute_plan(plan: OrganizationPlan) -> OrganizationResult:\n    """Execute a plan under the strongest explicitly supported platform contract."""\n    if not isinstance(plan, OrganizationPlan):\n        raise TypeError("plan must be an OrganizationPlan")\n\n    _preflight_execution(plan)\n    if not plan.actions:\n        return OrganizationResult(plan=plan, moved_files=())\n\n    if _supports_secure_directory_fds():\n        return _execute_plan_with_directory_fds(plan)\n\n    source_identities = _capture_portable_source_identities(plan)\n    return _execute_plan_portable(plan, source_identities)\n''',
)

# Update the mutation-race wrapper for the new pinned-FD argument.
replace_once(
    ATOMIC,
    '''    def racing_move(\n        source_name: str,\n        destination_name: str,\n        *,\n        source_directory_path: Path,\n        source_directory_fd: int,\n        destination_directory_fd: int,\n        category_name: str,\n        expected_identity: file_organizer._FileIdentity,\n    ) -> None:\n''',
    '''    def racing_move(\n        source_name: str,\n        destination_name: str,\n        *,\n        source_directory_path: Path,\n        source_directory_fd: int,\n        destination_directory_fd: int,\n        category_name: str,\n        source_fd: int,\n        expected_identity: file_organizer._FileIdentity,\n    ) -> None:\n''',
)
replace_once(
    ATOMIC,
    '''            destination_directory_fd=destination_directory_fd,\n            category_name=category_name,\n            expected_identity=expected_identity,\n        )\n\n    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)\n''',
    '''            destination_directory_fd=destination_directory_fd,\n            category_name=category_name,\n            source_fd=source_fd,\n            expected_identity=expected_identity,\n        )\n\n    monkeypatch.setattr(file_organizer, "_supports_secure_directory_fds", lambda: True)\n''',
)
append_once(
    ATOMIC,
    'test_source_identity_is_accepted_only_after_descriptor_pin',
    '''def test_source_identity_is_accepted_only_after_descriptor_pin(\n    monkeypatch: pytest.MonkeyPatch,\n    tmp_path: Path,\n) -> None:\n    if not file_organizer._supports_secure_directory_fds():\n        pytest.skip("secure directory descriptors are unavailable on this platform")\n\n    source = tmp_path / "notes.txt"\n    source.write_text("planned source", encoding="utf-8")\n    plan = plan_organization(tmp_path)\n    destination = tmp_path / "documents" / "notes.txt"\n    original_pin = file_organizer._pin_planned_sources_at\n    raced = False\n\n    def racing_pin(\n        plan_value: file_organizer.OrganizationPlan,\n        *,\n        root_fd: int,\n    ) -> dict[Path, file_organizer._PinnedSource]:\n        nonlocal raced\n        pinned = original_pin(plan_value, root_fd=root_fd)\n        if not raced:\n            raced = True\n            source.unlink()\n            source.write_text("third-party replacement", encoding="utf-8")\n        return pinned\n\n    monkeypatch.setattr(file_organizer, "_pin_planned_sources_at", racing_pin)\n\n    with pytest.raises(FileNotFoundError, match="planned source data retained"):\n        execute_plan(plan)\n\n    assert source.read_text(encoding="utf-8") == "third-party replacement"\n    assert not destination.exists()\n    recovery_files = [\n        child for child in tmp_path.iterdir() if child.name.startswith(".fo-recovery-")\n    ]\n    assert len(recovery_files) == 1\n    assert recovery_files[0].read_text(encoding="utf-8") == "planned source"\n''',
)

# Real Windows junction and reserved-internal-namespace regressions.
replace_once(TESTS, 'from pathlib import Path\n', 'import os\nimport subprocess\nfrom pathlib import Path\n')
append_once(
    TESTS,
    'test_internal_recovery_artifacts_are_reserved_from_future_plans',
    '''def test_internal_recovery_artifacts_are_reserved_from_future_plans(tmp_path: Path) -> None:\n    (tmp_path / ".fo-stage-deadbeef").write_text("stage", encoding="utf-8")\n    (tmp_path / ".fo-recovery-deadbeef").write_text("recovery", encoding="utf-8")\n    (tmp_path / "notes.txt").write_text("user", encoding="utf-8")\n\n    plan = plan_organization(tmp_path)\n\n    assert tuple(action.source.name for action in plan.actions) == ("notes.txt",)\n\n\n@pytest.mark.skipif(os.name != "nt", reason="requires Windows NTFS junction semantics")\ndef test_windows_real_source_and_category_junctions_are_rejected(tmp_path: Path) -> None:\n    outside = tmp_path / "outside"\n    outside.mkdir()\n\n    source_junction = tmp_path / "workspace-link"\n    subprocess.run(\n        ["cmd", "/c", "mklink", "/J", str(source_junction), str(outside)],\n        check=True,\n        capture_output=True,\n        text=True,\n    )\n    with pytest.raises(ValueError, match="symlink or junction"):\n        plan_organization(source_junction)\n\n    workspace = tmp_path / "workspace"\n    workspace.mkdir()\n    (workspace / "notes.txt").write_text("x", encoding="utf-8")\n    category_junction = workspace / "documents"\n    subprocess.run(\n        ["cmd", "/c", "mklink", "/J", str(category_junction), str(outside)],\n        check=True,\n        capture_output=True,\n        text=True,\n    )\n    with pytest.raises(ValueError, match="symlink or junction"):\n        plan_organization(workspace)\n''',
)

# Documentation EN.
replace_once(
    README_EN,
    'During secure Linux execution, the planned source is opened with `O_NOFOLLOW | O_NONBLOCK` when `O_NONBLOCK` is available. The nonblocking flag prevents a late FIFO replacement from hanging `open()`, while the following `fstat()` still requires a regular file with the planned `(device, inode)` identity. The open descriptor pins the expected inode while the commit runs.',
    'During secure Linux execution, source identity is accepted **only after the source has been opened** with `O_NOFOLLOW | O_NONBLOCK` when `O_NONBLOCK` is available. The following `fstat()` derives `(device, inode)` from that already-open descriptor, and every planned source descriptor stays open until the plan finishes. An accepted inode that is later unlinked therefore cannot be freed and immediately reused while execution still depends on its identity. The nonblocking flag also prevents a late FIFO replacement from hanging `open()`. Descriptor pinning stabilizes object identity, not file contents; concurrent writes to the same inode are outside this project\'s snapshot guarantees.',
)
replace_once(
    README_EN,
    '''1. preflight and capture source identity\n2. open and anchor the source root\n3. open and anchor required category directories\n4. pin the planned source inode with O_NOFOLLOW | O_NONBLOCK\n5. atomically claim source name -> short internal stage\n6. verify stage identity and directory anchors\n7. rescan the pinned category for a casefold-equivalent destination\n8. atomically rename stage -> exact destination with RENAME_NOREPLACE\n9. verify destination identity and anchors\n10. report success''',
    '''1. validate paths and collision preflight\n2. open and anchor the source root\n3. open every planned source and accept identity from `fstat()` on that pinned descriptor\n4. keep all accepted source descriptors open through plan completion\n5. open and anchor required category directories\n6. claim source name -> short internal stage with no-replace semantics\n7. verify stage identity and directory anchors\n8. rescan the pinned category for a casefold-equivalent destination\n9. atomically rename stage -> exact destination with RENAME_NOREPLACE\n10. verify destination identity and anchors\n11. report success''',
)
replace_once(
    README_EN,
    '- **Windows:** the fallback relies on Windows `os.rename()` refusing an existing destination and performs a best-effort casefold recheck plus source/destination/category identity validation around the operation;',
    '- **Windows:** the guarded portable path relies on Windows `os.rename()` refusing an existing destination and performs best-effort casefold, redirect, and identity checks. It does **not** claim the descriptor-pinned adversarial race resistance of the Linux path;',
)
replace_once(
    README_EN,
    '''4. planned-source identity capture;\n5. destination collision preflight;\n6. platform capability selection;\n7. anchored directory setup;\n8. nonblocking source pin and source claim;\n9. mutation-time casefold collision recheck;\n10. atomic exact-name no-replace commit;\n11. destination/anchor verification;\n12. `OrganizationResult` construction.''',
    '''4. destination collision preflight;\n5. platform capability selection;\n6. Linux: pin every planned source before accepting identity and before category mutation;\n7. anchored directory setup;\n8. source claim;\n9. mutation-time casefold collision recheck;\n10. atomic exact-name no-replace commit;\n11. destination/anchor verification;\n12. `OrganizationResult` construction.''',
)
replace_once(
    README_EN,
    'The organizer does not follow direct-child symlinks. It also rejects a source directory or category folder that is a symlink. On Windows, category folders that are NTFS junctions are rejected too: `is_dir()` follows a junction, so accepting one could redirect a planned move outside the workspace.',
    'The organizer does not follow direct-child symlinks. It rejects a source directory or category folder that is a symlink. On Windows, source directories and category folders that are NTFS junctions are rejected too: `is_dir()` follows a junction, so accepting one could redirect discovery or a planned move outside the workspace.',
)
replace_once(
    README_EN,
    'This can intentionally leave an internal recovery entry in unusual race/failure scenarios. That is preferable to deleting unrelated data whose current identity cannot be proven.',
    'This can intentionally leave an internal recovery entry in unusual race/failure scenarios. The `.fo-stage-*` and `.fo-recovery-*` prefixes are reserved internal namespaces and are excluded from later discovery so recovery evidence is not accidentally reorganized. That is preferable to deleting or reclassifying uncertain data whose current identity cannot be proven.',
)

# Documentation PT-BR.
replace_once(
    README_PT,
    'Durante a execução segura no Linux, a origem planejada é aberta com `O_NOFOLLOW | O_NONBLOCK` quando `O_NONBLOCK` está disponível. A flag nonblocking impede que uma substituição tardia por FIFO trave o `open()`, enquanto o `fstat()` seguinte ainda exige um arquivo regular com a identidade `(device, inode)` planejada. O descriptor aberto fixa o inode esperado durante o commit.',
    'Durante a execução segura no Linux, a identidade da origem só é aceita **depois que o arquivo já foi aberto** com `O_NOFOLLOW | O_NONBLOCK` quando `O_NONBLOCK` está disponível. O `fstat()` deriva `(device, inode)` desse descriptor já aberto, e todos os descriptors das origens planejadas permanecem abertos até o fim do plano. Assim, um inode aceito e depois desvinculado não pode ser liberado e imediatamente reutilizado enquanto a execução ainda depende da sua identidade. A flag nonblocking também impede que uma substituição tardia por FIFO trave o `open()`. O pinning estabiliza a identidade do objeto, não o conteúdo; escritas concorrentes no mesmo inode ficam fora das garantias de snapshot deste projeto.',
)
replace_once(
    README_PT,
    '''1. executar preflight e capturar identidade da origem\n2. abrir e ancorar a raiz\n3. abrir e ancorar as categorias necessárias\n4. fixar o inode da origem com O_NOFOLLOW | O_NONBLOCK\n5. reivindicar atomicamente origem -> staging curto\n6. verificar identidade do staging e âncoras\n7. varrer novamente a categoria ancorada por destino equivalente via casefold\n8. renomear atomicamente staging -> destino exato com RENAME_NOREPLACE\n9. verificar identidade do destino e âncoras\n10. reportar sucesso''',
    '''1. validar caminhos e executar o preflight de colisões\n2. abrir e ancorar a raiz\n3. abrir todas as origens planejadas e aceitar identidade pelo `fstat()` do descriptor pinado\n4. manter todos os descriptors aceitos abertos até o fim do plano\n5. abrir e ancorar as categorias necessárias\n6. reivindicar origem -> staging curto com semântica no-replace\n7. verificar identidade do staging e âncoras\n8. varrer novamente a categoria ancorada por destino equivalente via casefold\n9. renomear atomicamente staging -> destino exato com RENAME_NOREPLACE\n10. verificar identidade do destino e âncoras\n11. reportar sucesso''',
)
replace_once(
    README_PT,
    '- **Windows:** o fallback usa o comportamento de `os.rename()` que recusa destino existente e executa uma rechecagem `casefold()` best-effort mais validações de identidade ao redor da operação;',
    '- **Windows:** o caminho portátil protegido usa `os.rename()` recusando destino existente e realiza checagens best-effort de `casefold()`, redirecionamento e identidade. Ele **não** afirma possuir a mesma resistência a corridas adversariais baseada em descriptors pinados do caminho Linux;',
)
replace_once(
    README_PT,
    '''4. captura das identidades das origens planejadas;\n5. preflight de colisões;\n6. seleção da capacidade da plataforma;\n7. preparação dos diretórios ancorados;\n8. pinning nonblocking e claim da origem;\n9. rechecagem de colisão por `casefold()` na mutação;\n10. commit atômico no-replace do nome exato;\n11. verificação do destino e das âncoras;\n12. construção de `OrganizationResult`.''',
    '''4. preflight de colisões;\n5. seleção da capacidade da plataforma;\n6. Linux: pinning de todas as origens antes de aceitar identidade e antes de mutar categorias;\n7. preparação dos diretórios ancorados;\n8. claim da origem;\n9. rechecagem de colisão por `casefold()` na mutação;\n10. commit atômico no-replace do nome exato;\n11. verificação do destino e das âncoras;\n12. construção de `OrganizationResult`.''',
)
replace_once(
    README_PT,
    'O organizador não segue symlinks filhos diretos. Também rejeita diretório de origem ou pasta de categoria que seja symlink. No Windows, pastas de categoria que sejam junctions NTFS também são rejeitadas: `is_dir()` segue um junction, então aceitá-lo poderia redirecionar uma movimentação planejada para fora do workspace.',
    'O organizador não segue symlinks filhos diretos. Também rejeita diretório de origem ou pasta de categoria que seja symlink. No Windows, tanto o diretório de origem quanto as pastas de categoria são rejeitados quando são junctions NTFS: `is_dir()` segue um junction, então aceitá-lo poderia redirecionar descoberta ou movimentação para fora do workspace.',
)
replace_once(
    README_PT,
    'Em cenários raros de corrida/falha, isso pode deixar uma entrada interna de recuperação. É preferível a excluir dados cuja identidade atual não pode ser comprovada.',
    'Em cenários raros de corrida/falha, isso pode deixar uma entrada interna de recuperação. Os prefixos `.fo-stage-*` e `.fo-recovery-*` são namespaces internos reservados e ficam fora de descobertas futuras, evitando que evidências de recuperação sejam reorganizadas por acidente. É preferível a excluir ou reclassificar dados cuja identidade atual não pode ser comprovada.',
)

# Documentation ES.
replace_once(
    README_ES,
    'Durante la ejecución segura en Linux, el origen planificado se abre con `O_NOFOLLOW | O_NONBLOCK` cuando `O_NONBLOCK` está disponible. La flag nonblocking impide que una sustitución tardía por FIFO bloquee `open()`, mientras el `fstat()` posterior sigue exigiendo un archivo regular con la identidad `(device, inode)` planificada. El descriptor abierto fija el inode esperado durante el commit.',
    'Durante la ejecución segura en Linux, la identidad del origen se acepta **solo después de abrir el archivo** con `O_NOFOLLOW | O_NONBLOCK` cuando `O_NONBLOCK` está disponible. El `fstat()` deriva `(device, inode)` de ese descriptor ya abierto, y todos los descriptores de los orígenes planificados permanecen abiertos hasta que termina el plan. Así, un inode aceptado y luego desvinculado no puede liberarse y reutilizarse de inmediato mientras la ejecución todavía depende de su identidad. La flag nonblocking también evita que una sustitución tardía por FIFO bloquee `open()`. El pinning estabiliza la identidad del objeto, no su contenido; las escrituras concurrentes sobre el mismo inode quedan fuera de las garantías de snapshot de este proyecto.',
)
replace_once(
    README_ES,
    '''1. ejecutar preflight y capturar identidad del origen\n2. abrir y anclar la raíz\n3. abrir y anclar las categorías necesarias\n4. fijar el inode del origen con O_NOFOLLOW | O_NONBLOCK\n5. reclamar atómicamente origen -> staging corto\n6. verificar identidad del staging y anclajes\n7. escanear de nuevo la categoría anclada buscando un destino equivalente por casefold\n8. renombrar atómicamente staging -> destino exacto con RENAME_NOREPLACE\n9. verificar identidad del destino y anclajes\n10. informar éxito''',
    '''1. validar rutas y ejecutar el preflight de colisiones\n2. abrir y anclar la raíz\n3. abrir todos los orígenes planificados y aceptar identidad mediante `fstat()` del descriptor fijado\n4. mantener abiertos todos los descriptores aceptados hasta que termine el plan\n5. abrir y anclar las categorías necesarias\n6. reclamar origen -> staging corto con semántica no-replace\n7. verificar identidad del staging y anclajes\n8. escanear de nuevo la categoría anclada buscando un destino equivalente por casefold\n9. renombrar atómicamente staging -> destino exacto con RENAME_NOREPLACE\n10. verificar identidad del destino y anclajes\n11. informar éxito''',
)
replace_once(
    README_ES,
    '- **Windows:** el fallback usa el comportamiento de `os.rename()` que rechaza un destino existente y realiza una nueva comprobación `casefold()` best-effort junto con validaciones de identidad alrededor de la operación;',
    '- **Windows:** la ruta portátil protegida usa `os.rename()` rechazando un destino existente y realiza comprobaciones best-effort de `casefold()`, redirección e identidad. **No** afirma tener la misma resistencia a carreras adversariales basada en descriptores fijados que la ruta Linux;',
)
replace_once(
    README_ES,
    '''4. captura de identidades de los orígenes planificados;\n5. preflight de colisiones;\n6. selección de capacidades de plataforma;\n7. preparación de directorios anclados;\n8. pinning nonblocking y claim del origen;\n9. nueva comprobación de colisión por `casefold()` durante la mutación;\n10. commit atómico no-replace del nombre exacto;\n11. verificación de destino y anclajes;\n12. construcción de `OrganizationResult`.''',
    '''4. preflight de colisiones;\n5. selección de capacidades de plataforma;\n6. Linux: fijar todos los orígenes antes de aceptar identidad y antes de mutar categorías;\n7. preparación de directorios anclados;\n8. claim del origen;\n9. nueva comprobación de colisión por `casefold()` durante la mutación;\n10. commit atómico no-replace del nombre exacto;\n11. verificación de destino y anclajes;\n12. construcción de `OrganizationResult`.''',
)
replace_once(
    README_ES,
    'El organizador no sigue symlinks hijos directos. También rechaza directorio de origen o carpeta de categoría que sea symlink. En Windows, también se rechazan carpetas de categoría que sean junctions NTFS: `is_dir()` sigue un junction, por lo que aceptarlo podría redirigir un movimiento planificado fuera del workspace.',
    'El organizador no sigue symlinks hijos directos. También rechaza directorio de origen o carpeta de categoría que sea symlink. En Windows, tanto el directorio de origen como las carpetas de categoría se rechazan cuando son junctions NTFS: `is_dir()` sigue un junction, por lo que aceptarlo podría redirigir el descubrimiento o un movimiento fuera del workspace.',
)
replace_once(
    README_ES,
    'En escenarios raros de carrera/fallo, esto puede dejar una entrada interna de recuperación. Es preferible a borrar datos cuya identidad actual no puede demostrarse.',
    'En escenarios raros de carrera/fallo, esto puede dejar una entrada interna de recuperación. Los prefijos `.fo-stage-*` y `.fo-recovery-*` son namespaces internos reservados y quedan fuera de descubrimientos futuros para que la evidencia de recuperación no se reorganice por accidente. Es preferible a borrar o reclasificar datos cuya identidad actual no puede demostrarse.',
)

print('Applied File Organizer full-review hardening patch.')
