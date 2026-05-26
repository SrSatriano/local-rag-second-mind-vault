# Local RAG "Second Mind" Vault

Sistema de Retrieval-Augmented Generation 100% offline. Ingere milhares de PDFs e documentos pessoais, vetoriza localmente e consulta com LLM open-source via Ollama/LM Studio.

## Stack

- Python, LangChain
- Qwen / DeepSeek (Ollama)
- ChromaDB ou Milvus
- Docker

## Diagrama de arquitetura

```
 PDFs/Docs ──► Ingestion ──► Chunker ──► Embeddings (local)
                                              │
                                              ▼
 User Query ──► Retriever ◄── Vector DB (Chroma/Milvus)
                    │
                    ▼
              LLM (Ollama) ──► Answer + Citations
```

Diagrama detalhado: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## Requisitos de hardware

| Modelo | RAM | VRAM (GPU) | Notas |
|--------|-----|------------|-------|
| 7B Q4 | 8 GB | 6 GB | Uso diário leve |
| 14B Q4 | 16 GB | 10 GB | Melhor qualidade |
| 32B+ | 32 GB+ | 24 GB+ | Workstation |

CPU-only funciona com modelos quantizados; latência maior.

## Deploy Docker

```bash
docker compose -f docker/docker-compose.yml up -d
```

Serviços: `ollama`, `chroma`, `api`, `ingest-worker`.

## Quick start (local)

```bash
pip install -r requirements.txt
cp config/example.env .env
python -m src.ingestion.cli ingest ./data/samples
python -m src.api.main
```

Consulta: `POST /query` com `{"question": "...", "top_k": 5}`.

## Privacidade

- Nenhum dado sai da máquina.
- Embeddings e índice persistidos em volume local.
- Opcional: criptografia em repouso (ver `docs/SECURITY.md`).

## Estrutura

| Pasta | Função |
|-------|--------|
| `src/ingestion/` | PDF, DOCX, markdown |
| `src/embeddings/` | Modelos sentence-transformers |
| `src/retrieval/` | RAG chain |
| `src/api/` | FastAPI |
| `docker/` | Compose e imagens |
