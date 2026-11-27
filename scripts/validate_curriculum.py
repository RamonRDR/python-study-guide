"""Validate the structural manifest boundary (not full consumer acceptance)."""
import argparse
import sys
from pathlib import Path

from curriculum_manifest import ROOT, load_manifest
from curriculum_inventory import load_inventory


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--manifest", default="curriculum/manifest.json")
    parser.add_argument("--inventory", action="store_true",
                        help="validate complete inventory and bank relationships against the tracked baseline")
    args = parser.parse_args()
    try:
        loader = load_inventory if args.inventory else load_manifest
        data = loader(args.root, args.manifest)
    except (ValueError, OSError) as exc:
        print(f"Manifest validation failed: {exc}", file=sys.stderr)
        return 1
    if args.inventory:
        count = sum(len(module["chapters"]) for module in data["modules"])
        print(f"Validated {len(data['modules'])} modules, {count} curriculum entries "
              "and complete assessment relationships; consumer acceptance is separate.")
    else:
        print(f"Manifest structure and paths valid ({data['association_status']}); "
              "full inventory and consumer acceptance are separate gates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
