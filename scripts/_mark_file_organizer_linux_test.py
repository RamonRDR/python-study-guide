from pathlib import Path

path = Path("practical-projects/06-file-organizer/tests/test_atomic_move.py")
text = path.read_text(encoding="utf-8")
anchor = '''def test_execute_plan_never_replaces_destination_created_after_preflight(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    source = tmp_path / "notes.txt"
'''
replacement = '''def test_execute_plan_never_replaces_destination_created_after_preflight(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    if not file_organizer._supports_secure_directory_fds():
        pytest.skip("secure directory descriptors are unavailable on this platform")

    source = tmp_path / "notes.txt"
'''
if text.count(anchor) != 1:
    raise SystemExit("expected exactly one Linux-only test anchor")
path.write_text(text.replace(anchor, replacement, 1), encoding="utf-8")
