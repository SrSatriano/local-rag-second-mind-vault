# Guia de deploy — Cofre RAG local "Second Mind"

> Versão **1.0.0** · Stack: **Python, FastAPI, ChromaDB, Ollama, Docker**

## 1. Objetivo

Este guia descreve como publicar o projeto em **homologação** e **produção**, incluindo variáveis de ambiente, health checks e procedimento de rollback.

## 2. Pré-requisitos de infraestrutura

Python 3.11+, opcional: Ollama instalado para respostas generativas.

## 3. Homologação (staging)

### 3.1 Preparação

```bash
git clone https://github.com/SrSatriano/local-rag-second-mind-vault.git
cd local-rag-second-mind-vault
cp .env.example .env   # quando existir
```

### 3.2 Instalação

```bash
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

### 3.3 Validação

```bash
pytest tests/ -q
```

Confirme health check (HTTP ou métrica) antes de promover.

## 4. Produção

| Item | Recomendação |
|------|----------------|
| **Segredos** | Secret manager (GitHub Actions secrets, Vault, cloud provider) |
| **Rede** | TLS terminado no reverse proxy ou ingress |
| **Dados** | Backup automático conforme RPO/RTO da equipe |
| **Logs** | Agregação centralizada (Loki, CloudWatch, ELK) |
| **Métricas** | Prometheus/Grafana ou equivalente |

### Variáveis de ambiente

Consulte a tabela no [README](../README.md#configuração). Em produção, rotacione chaves periodicamente.

## 5. Estratégias de deploy

| Estratégia | Quando usar |
|------------|-------------|
| **Rolling** | APIs stateless, zero downtime gradual |
| **Blue/green** | Validação completa antes de trocar tráfego |
| **Canary** | Risco alto; libera % pequena do tráfego |

## 6. Health checks

- **Liveness:** processo responde (não travado).
- **Readiness:** dependências (banco, fila, RPC) disponíveis.

Documente o endpoint ou comando no README do serviço.

## 7. Rollback

1. Identifique a tag estável anterior (ex.: `v1.0.0`).
2. Reverta o deploy para a imagem/binário dessa tag.
3. Execute `pytest tests/ -q` ou smoke tests automatizados.
4. Reprocesse fila morta ou jobs falhos, se aplicável.
5. Abra post-mortem se houve impacto a usuários.

## 8. Checklist pré-go-live

- [ ] Testes CI verdes
- [ ] `.env` de produção fora do Git
- [ ] Backup configurado
- [ ] Alertas de erro e latência ativos
- [ ] Runbook [OPERATIONS.md](OPERATIONS.md) revisado pela equipe
