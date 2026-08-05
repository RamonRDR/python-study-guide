"""Regression tests for repository structure and visual-asset validation."""

from pathlib import Path
import struct
import tempfile
import unittest
from unittest.mock import patch

from scripts import validate_repository_structure

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def write_png(path: Path, width: int, height: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(PNG_SIGNATURE + b"\x00\x00\x00\rIHDR" + struct.pack(">II", width, height) + b"\x08\x06\x00\x00\x00\x00\x00\x00\x00")


def write_svg(path: Path, width: int, height: int, reference: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">Fixture title</title>
  <desc id="desc">Fixture description</desc>
  <image href="{reference}"/>
</svg>
''', encoding="utf-8"
    )


class VisualAssetValidationTests(unittest.TestCase):
    def create_valid_assets(self, root: Path) -> None:
        write_png(root / "assets/banner.png", 1200, 400)
        write_png(root / "assets/logo-mark.png", 384, 384)
        write_png(root / "assets/logo.png", 650, 283)
        write_png(root / "assets/repository-preview.png", 1280, 640)
        write_svg(root / "assets/banner.svg", 1200, 400, "data:image/png;base64,AAAA")
        write_svg(root / "assets/repository-preview.svg", 1280, 640, "logo-mark.png")

    def validate(self, root: Path) -> list[str]:
        with patch.object(validate_repository_structure, "REPOSITORY_ROOT", root):
            return validate_repository_structure.validate_visual_assets()

    def test_valid_visual_assets_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.create_valid_assets(root)
            self.assertEqual(self.validate(root), [])

    def test_png_dimensions_are_read_from_ihdr(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "image.png"
            write_png(path, 321, 123)
            self.assertEqual(validate_repository_structure.read_png_dimensions(path), (321, 123))

    def test_svg_canvas_must_match_rendered_png(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.create_valid_assets(root)
            write_svg(root / "assets/banner.svg", 1000, 400, "data:image/png;base64,AAAA")
            self.assertTrue(any("SVG canvas mismatch" in error for error in self.validate(root)))

    def test_missing_local_svg_reference_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.create_valid_assets(root)
            write_svg(root / "assets/repository-preview.svg", 1280, 640, "missing-logo.png")
            self.assertTrue(any("missing local file" in error for error in self.validate(root)))

    def test_svg_reference_cannot_escape_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory) / "repository"
            self.create_valid_assets(root)
            write_svg(root / "assets/repository-preview.svg", 1280, 640, "../../outside.png")
            self.assertTrue(any("outside the repository" in error for error in self.validate(root)))

    def test_svg_requires_accessible_title_and_description(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            self.create_valid_assets(root)
            (root / "assets/banner.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400"></svg>', encoding="utf-8")
            errors = self.validate(root)
            self.assertTrue(any('role="img"' in error for error in errors))
            self.assertTrue(any("non-empty <title>" in error for error in errors))
            self.assertTrue(any("non-empty <desc>" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
