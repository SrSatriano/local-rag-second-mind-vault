# Arquitetura RAG local

## Pipeline de ingestão

1. **Load** — PyMuPDF / Unstructured para extrair texto.
2. **Split** — chunks de 512 tokens, overlap 64.
3. **Embed** — `sentence-transformers/all-MiniLM-L6-v2` (offline).
4. **Store** — Chroma collection por usuário/projeto.

## Pipeline de consulta

1. Embed da pergunta.
2. Similarity search top-k.
3. Montagem do prompt com citações `[doc_id:chunk]`.
4. Geração via Ollama API `http://localhost:11434`.

## Fallback

Se score < threshold, resposta: "Não encontrei nos seus documentos" — evita alucinação.
