"""Singleton do vector store da aplicação."""

from src.embeddings.store import VectorStore

_store: VectorStore | None = None


def get_store() -> VectorStore:
    global _store
    if _store is None:
        _store = VectorStore()
    return _store


def reset_store() -> None:
    global _store
    _store = VectorStore()
