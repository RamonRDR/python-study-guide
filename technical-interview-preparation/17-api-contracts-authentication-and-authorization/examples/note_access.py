"""Model object-level authorization after a trusted authentication boundary."""


def validate_title(payload: object) -> str:
    if not isinstance(payload, dict) or set(payload) != {"title"}:
        raise ValueError("expected exactly the title field")
    title = payload["title"]
    if not isinstance(title, str) or not 1 <= len(title.strip()) <= 80:
        raise ValueError("title must contain 1 to 80 characters after trimming")
    return title.strip()


def read_note(principal: str | None, note_id: int, notes: dict) -> tuple:
    headers = {"Content-Type": "application/json"}
    # principal is supplied by a trusted authentication layer, not the client.
    if principal is None:
        return 401, {**headers, "WWW-Authenticate": "Bearer"}, {"error": "authentication required"}
    note = notes.get(note_id)
    if note is None:
        return 404, headers, {"error": "not found"}
    owner, text = note
    if principal != owner:
        return 403, headers, {"error": "forbidden"}
    return 200, headers, {"text": text}


if __name__ == "__main__":
    notes = {1: ("learner-a", "draft")}
    print(read_note("learner-a", 1, notes))
    print(read_note("learner-b", 1, notes))
    print(validate_title({"title": "  SQL  "}))
