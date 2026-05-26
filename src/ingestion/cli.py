"""CLI de ingestão."""

import argparse
from pathlib import Path

from src.ingestion.loader import ingest_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingerir documentos no vault")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    n = ingest_path(args.path)
    print(f"Ingeridos {n} arquivos de {args.path}")


if __name__ == "__main__":
    main()
