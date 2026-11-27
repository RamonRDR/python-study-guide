"""Validate the structural manifest boundary (not full consumer acceptance)."""
import argparse
import sys
from pathlib import Path

from curriculum_manifest import ROOT, load_manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--manifest", default="curriculum/manifest.json")
    args = parser.parse_args()
    try:
        data = load_manifest(args.root, args.manifest)
    except (ValueError, OSError) as exc:
        print(f"Manifest validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Manifest structure and paths valid ({data['association_status']}); "
          "full inventory and consumer acceptance are separate gates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
