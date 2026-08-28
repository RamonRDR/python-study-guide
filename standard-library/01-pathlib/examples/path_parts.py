from pathlib import Path


report_path = Path("reports") / "2026" / "summary.txt"

print(f"Path: {report_path}")
print(f"Name: {report_path.name}")
print(f"Stem: {report_path.stem}")
print(f"Suffix: {report_path.suffix}")
print(f"Parent: {report_path.parent}")
