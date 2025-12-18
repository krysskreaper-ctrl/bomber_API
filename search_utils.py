from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

# Keywords that should trigger a match when present in a filename or file content
DRAGON_KEYWORDS = ["dragon36", "dragon", "3.6", "3_6"]


def _contains_keyword(text: str, keywords: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in keywords)


def _read_text_safely(path: Path) -> str:
    """Read text from a file while tolerating encoding errors.

    Binary files may raise exceptions when treated as text; in that case an
    empty string is returned so they do not accidentally report false matches.
    """

    try:
        return path.read_text(errors="ignore")
    except (OSError, UnicodeDecodeError):
        return ""


def find_dragon_files(root: str | Path = ".") -> List[str]:
    """Return file paths under ``root`` that mention dragon-related keywords.

    A match occurs when a filename or its text content contains any value in
    ``DRAGON_KEYWORDS`` (case-insensitive). Paths are returned relative to the
    provided root for readability.
    """

    root_path = Path(root).resolve()
    matches: List[str] = []

    for file_path in root_path.rglob("*"):
        if not file_path.is_file():
            continue

        if _contains_keyword(file_path.name, DRAGON_KEYWORDS):
            matches.append(str(file_path.relative_to(root_path)))
            continue

        content = _read_text_safely(file_path)
        if content and _contains_keyword(content, DRAGON_KEYWORDS):
            matches.append(str(file_path.relative_to(root_path)))

    return matches
