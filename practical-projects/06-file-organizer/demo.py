from pathlib import Path
from tempfile import TemporaryDirectory

from file_organizer import execute_plan, plan_organization


def main() -> None:
    """Run a deterministic fictional organization workflow in a temporary folder."""
    with TemporaryDirectory() as temporary_directory:
        workspace = Path(temporary_directory)
        fictional_files = {
            "meeting-notes.txt": "Agenda notes\n",
            "orders.csv": "id,total\n101,50\n",
            "product-photo.png": "fictional image placeholder\n",
            "backup.zip": "fictional archive placeholder\n",
            "automation.py": "print('fictional')\n",
        }
        for name, content in fictional_files.items():
            (workspace / name).write_text(content, encoding="utf-8")

        plan = plan_organization(workspace)
        print(f"planned moves: {plan.planned_count}")
        for action in plan.actions:
            print(
                f"{action.source.name} -> "
                f"{action.destination.parent.name}/{action.destination.name}"
            )

        result = execute_plan(plan)
        print(f"moved files: {result.moved_count}")
        folders = sorted(path.name for path in workspace.iterdir() if path.is_dir())
        print(f"created folders: {', '.join(folders)}")


if __name__ == "__main__":
    main()
