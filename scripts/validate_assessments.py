"""CLI for assessment planning and explicitly supplied versioned catalogs."""
import argparse
from pathlib import Path

from assessment_records import load_index, load_matrix


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--quiz-index")
    parser.add_argument("--exercise-index")
    args = parser.parse_args()
    try:
        chapters = load_matrix(args.root)
        print(f"Validated {len(chapters)} planned curriculum entries.")
        for kind, path in (("quiz", args.quiz_index), ("exercise", args.exercise_index)):
            if path:
                records = load_index(kind, args.root, path, chapters)
                print(f"Validated {len(records)} {kind} records.")
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Assessment validation failed: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
