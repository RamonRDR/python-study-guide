"""Model a small HTTP routing contract, not an HTTP server."""


def route(method: str, path: str) -> tuple[int, dict, object]:
    headers = {"Content-Type": "application/json"}
    if path != "/lessons":
        return 404, headers, {"error": "not found"}
    if method != "GET":
        return 405, {**headers, "Allow": "GET"}, {"error": "method not allowed"}
    return 200, headers, [{"id": 1}]


if __name__ == "__main__":
    for method, path in (("GET", "/lessons"), ("POST", "/lessons"),
                         ("GET", "/missing")):
        print(route(method, path))
