from dataclasses import dataclass
import os

from src.store import get_store


@dataclass
class RAGResult:
    answer: str
    sources: list[str]


def _build_prompt(question: str, context: str) -> str:
    return (
        "Responda apenas com base no contexto abaixo. "
        "Se não houver informação suficiente, diga que não sabe.\n\n"
        f"Contexto:\n{context}\n\nPergunta: {question}\nResposta:"
    )


def _call_ollama(prompt: str) -> str | None:
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    model = os.getenv("LLM_MODEL", "qwen2.5:7b")
    try:
        import httpx

        r = httpx.post(
            f"{host}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=120.0,
        )
        r.raise_for_status()
        return r.json().get("response", "").strip()
    except Exception:
        return None


class RAGChain:
    def ask(self, question: str, top_k: int = 5) -> RAGResult:
        chunks = get_store().similarity_search(question, k=top_k)
        if not chunks:
            return RAGResult(
                answer="Não encontrei informação relevante nos seus documentos.",
                sources=[],
            )
        context = "\n\n".join(f"[{c.source_id}] {c.text}" for c in chunks)
        prompt = _build_prompt(question, context)
        llm_answer = _call_ollama(prompt)
        if llm_answer:
            answer = llm_answer
        else:
            answer = (
                "Resposta baseada nos trechos recuperados (modo offline sem Ollama):\n\n"
                + context[:2000]
            )
        return RAGResult(answer=answer, sources=[c.source_id for c in chunks])
