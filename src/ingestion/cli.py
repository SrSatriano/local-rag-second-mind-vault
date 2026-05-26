"""CLI de ingestão de documentos."""

import argparse
from pathlib import Path

from src.embeddings.store import VectorStore


def ingest_path(path: Path, store: VectorStore) -> int:
    count = 0
    for file in path.rglob("*"):
        if file.suffix.lower() in {".txt", ".md"}:
            store.add(file.read_text(encoding="utf-8", errors="ignore"), str(file))
            count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingerir documentos no vault")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    store = VectorStore()
    n = ingest_path(args.path, store)
    print(f"Ingeridos {n} arquivos de {args.path}")


if __name__ == "__main__":
    main()
