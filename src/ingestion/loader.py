from pathlib import Path

from src.store import get_store


def ingest_text(text: str, source_id: str) -> int:
    store = get_store()
    store.add(text, source_id)
    return len(text)


def ingest_path(path: Path) -> int:
    count = 0
    store = get_store()
    for file in path.rglob("*"):
        if file.suffix.lower() not in {".txt", ".md"}:
            continue
        content = file.read_text(encoding="utf-8", errors="ignore")
        store.add(content, str(file))
        count += 1
    return count
