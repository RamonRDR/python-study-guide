"""Find project markers in real Python comments using the tokenize module."""


from io import StringIO
import re
import tokenize


MARKER_PATTERN = re.compile(
    r"#\s*(TODO|FIXME|NOTE|HACK|XXX)"
    r"(?:\(([^)]+)\))?:\s*(.+)"
)

SAMPLE_SOURCE = """
message = "# TODO: this is text, not a comment"
# TODO(#128): Replace the temporary parser.
# NOTE: Amounts are stored in cents.
value = 10
"""


def find_markers(source: str) -> list[tuple[str, str | None, str]]:
    """Return marker, reference, and message tuples from Python comments."""
    markers: list[tuple[str, str | None, str]] = []

    for token in tokenize.generate_tokens(StringIO(source).readline):
        if token.type != tokenize.COMMENT:
            continue

        match = MARKER_PATTERN.fullmatch(token.string)
        if match:
            marker, reference, message = match.groups()
            markers.append((marker, reference, message))

    return markers


def main() -> None:
    """Run the marker-scanning example."""
    for marker, reference, message in find_markers(SAMPLE_SOURCE):
        reference_text = reference or "none"
        print(f"{marker} | reference={reference_text} | {message}")


if __name__ == "__main__":
    main()
