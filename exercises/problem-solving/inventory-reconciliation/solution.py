"""Reference solution for inventory-reconciliation."""


def reconcile(expected: list[list], actual: list[list]) -> list[list]:
    expected_totals = {}
    actual_totals = {}
    order = []
    seen = set()
    for rows, totals in ((expected, expected_totals), (actual, actual_totals)):
        for label, quantity in rows:
            totals[label] = totals.get(label, 0) + quantity
            if label not in seen:
                seen.add(label)
                order.append(label)
    result = []
    for label in order:
        before = expected_totals.get(label, 0)
        after = actual_totals.get(label, 0)
        if before != after:
            result.append([label, before, after, after - before])
    return result
