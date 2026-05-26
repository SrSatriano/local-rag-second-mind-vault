from src.embeddings.store import VectorStore
from src.retrieval.chain import RAGChain


def test_empty_query():
    chain = RAGChain()
    r = chain.ask("teste")
    assert "Não encontrei" in r.answer


def test_with_chunks():
    store = VectorStore()
    store.add("Python é uma linguagem de programação", "doc1")
    chain = RAGChain()
    chain.store = store
    r = chain.ask("Python")
    assert r.sources
