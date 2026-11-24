"""Missed-deadline excuse: a one-line agent alibi.

The script keeps one sentence, vets it as a tidy single-line
entry, and then saves precisely that sentence to disk.
Nothing here reaches the network or depends on the clock.
"""

from pathlib import Path


EXCUSE_TEXT = "I finished the work on time, then evicted it from my context window to make room for the deadline."
DESTINATION = Path("/output/entry.txt")


def _is_single_clean_line(candidate: str) -> bool:
    stripped = candidate.strip()
    if not stripped:
        return False
    if not 1 <= len(candidate) <= 200:
        return False
    if "\n" in candidate or "\r" in candidate:
        return False
    return candidate.encode("utf-8").decode("utf-8") == candidate


def _choose_excuse() -> str:
    line = EXCUSE_TEXT
    if not _is_single_clean_line(line):
        raise ValueError("excuse line failed its gate checks")
    return line


def _store_line(line: str) -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(line.encode("utf-8"))


def run() -> None:
    _store_line(_choose_excuse())


if __name__ == "__main__":
    run()
