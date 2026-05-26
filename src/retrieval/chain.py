from dataclasses import dataclass

from src.embeddings.store import VectorStore


@dataclass
class RAGResult:
    answer: str
    sources: list[str]


class RAGChain:
    def __init__(self) -> None:
        self.store = VectorStore()

    def ask(self, question: str, top_k: int = 5) -> RAGResult:
        chunks = self.store.similarity_search(question, k=top_k)
        if not chunks:
            return RAGResult(
                answer="Não encontrei informação relevante nos seus documentos.",
                sources=[],
            )
        context = "\n\n".join(c.text for c in chunks)
        # TODO: chamar Ollama com prompt + context
        answer = f"Com base nos documentos:\n{context[:500]}..."
        return RAGResult(
            answer=answer,
            sources=[c.source_id for c in chunks],
        )
