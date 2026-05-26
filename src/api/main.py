"""FastAPI — consultas RAG locais."""

from fastapi import FastAPI
from pydantic import BaseModel

from src.retrieval.chain import RAGChain

app = FastAPI(title="Second Mind Vault", version="0.1.0")
chain = RAGChain()


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest) -> QueryResponse:
    result = chain.ask(req.question, top_k=req.top_k)
    return QueryResponse(answer=result.answer, sources=result.sources)
