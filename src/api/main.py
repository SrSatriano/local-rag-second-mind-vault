"""FastAPI — Second Mind Vault v1.0"""

from pathlib import Path

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel, Field

from src.ingestion.loader import ingest_text
from src.retrieval.chain import RAGChain
from src.store import get_store

app = FastAPI(title="Second Mind Vault", version="1.0.0")
chain = RAGChain()


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1)
    top_k: int = Field(5, ge=1, le=20)


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


class IngestResponse(BaseModel):
    source_id: str
    chars: int


@app.get("/health")
def health() -> dict:
    store = get_store()
    return {"status": "ok", "documents_indexed": len(store._chunks)}


@app.post("/ingest/text", response_model=IngestResponse)
def ingest_body(payload: dict) -> IngestResponse:
    text = payload.get("text", "")
    source_id = payload.get("source_id", "inline")
    n = ingest_text(text, source_id)
    return IngestResponse(source_id=source_id, chars=n)


@app.post("/ingest/file", response_model=IngestResponse)
async def ingest_file(file: UploadFile = File(...)) -> IngestResponse:
    data = await file.read()
    name = file.filename or "upload"
    if Path(name).suffix.lower() in {".txt", ".md"}:
        text = data.decode("utf-8", errors="ignore")
    else:
        text = data.decode("utf-8", errors="ignore")
    n = ingest_text(text, name)
    return IngestResponse(source_id=name, chars=n)


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest) -> QueryResponse:
    result = chain.ask(req.question, top_k=req.top_k)
    return QueryResponse(answer=result.answer, sources=result.sources)
