from tempfile import TemporaryDirectory

from expense_tracker import ExpenseTracker


def build_demo_tracker() -> ExpenseTracker:
    tracker = ExpenseTracker()
    tracker.add("2026-08-27", "Groceries", "Food", "45.40")
    tracker.add("2026-08-28", "Bus pass", "Transport", "120.00")
    tracker.add("2026-08-29", "Coffee", "Food", "8.50")
    return tracker


def main() -> None:
    tracker = build_demo_tracker()

    print(f"expenses: {len(tracker.expenses)}")
    print(f"total: {tracker.total():.2f}")
    print(f"food: {tracker.total('food'):.2f}")
    print(f"transport: {tracker.total('transport'):.2f}")

    with TemporaryDirectory() as temp_dir:
        json_path = tracker.save_json(f"{temp_dir}/expenses.json")
        csv_path = tracker.export_csv(f"{temp_dir}/expenses.csv")
        restored = ExpenseTracker.load_json(json_path)

        csv_rows = len(csv_path.read_text(encoding="utf-8").splitlines()) - 1
        print(f"json round-trip: {restored.expenses == tracker.expenses}")
        print(f"csv rows: {csv_rows}")


if __name__ == "__main__":
    main()
