<div align="center">

# Cofre RAG local "Second Mind"

**Cofre RAG local Second Mind**

<p>
  <a href="https://github.com/SrSatriano/local-rag-second-mind-vault"><img src="https://img.shields.io/badge/GitHub-local-rag-second-mind-vault-24292e?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
</p>

<p>
  <img src="https://img.shields.io/badge/versão-1.0.0-0ea5e9?style=flat-square" alt="versão" />
  <img src="https://img.shields.io/badge/licença-MIT-22c55e?style=flat-square" alt="licença" />
  <img src="https://img.shields.io/badge/idioma-pt--BR-blue?style=flat-square" alt="idioma" />
  <img src="https://img.shields.io/badge/CI-GitHub_Actions-8b5cf6?style=flat-square" alt="ci" />
</p>

<p><strong>Perguntas e respostas 100% offline com Ollama — seus documentos nunca saem da máquina.</strong></p>

<p>
  Autor: <a href="https://github.com/SrSatriano">@SrSatriano</a> ·
  Release <strong>1.0.0</strong> (2026-03-26)
</p>

</div>

---

## Índice

1. [Visão geral](#visão-geral)
2. [Problema e solução](#problema-e-solução)
3. [Para quem é](#para-quem-é)
4. [Casos de uso](#casos-de-uso)
5. [Funcionalidades](#funcionalidades)
6. [Stack tecnológica](#stack-tecnológica)
7. [Arquitetura](#arquitetura)
8. [Estrutura do repositório](#estrutura-do-repositório)
9. [Pré-requisitos](#pré-requisitos)
10. [Instalação e execução](#instalação-e-execução)
11. [Configuração](#configuração)
12. [Testes](#testes)
13. [Performance](#performance)
14. [Deploy e operação](#deploy-e-operação)
15. [Limitações conhecidas](#limitações-conhecidas)
16. [Roadmap](#roadmap)
17. [Documentação complementar](#documentação-complementar)
18. [Segurança e licença](#segurança-e-licença)

---

## Visão geral

Este repositório faz parte do **portfólio de engenharia** mantido por [@SrSatriano](https://github.com/SrSatriano). A versão **1.0.0** entrega implementação do núcleo do produto, testes automatizados, pipeline de integração contínua e documentação operacional em **português brasileiro**.

O objetivo é permitir que você clone, execute e evolua o projeto com clareza — do desenvolvimento local ao deploy em produção.

## Problema e solução

| | |
|---|---|
| **Problema** | Enviar documentos confidenciais para APIs na nuvem viola políticas de privacidade. |
| **Solução** | Ingestão local, busca semântica e geração opcional via Ollama com citação de fontes. |

## Para quem é

Advogados, pesquisadores, PMEs e desenvolvedores que precisam de RAG privado.

## Casos de uso

- Base de conhecimento de contratos
- Segunda memória para notas técnicas

## Funcionalidades

- [x] Endpoints REST de ingestão (texto e arquivo)
- [x] Consulta com top-k e lista de fontes
- [x] Modo offline sem LLM (contexto recuperado)
- [x] Integração Ollama configurável por variáveis
- [x] Docker Compose para deploy rápido

## Stack tecnológica

| Camada | Tecnologias |
|--------|-------------|
| **Principal** | Python, FastAPI, ChromaDB, Ollama, Docker |

## Arquitetura

```mermaid
flowchart TB
  ING[Ingestão PDF/MD] --> CH[Chunking]
  CH --> EMB[Embeddings locais]
  EMB --> VDB[(Vector store)]
  API[FastAPI] --> RET[Recuperação + RAG]
  RET --> VDB
  RET --> LLM[Ollama opcional]
```

Detalhamento de componentes, fluxos de dados e decisões de design: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Estrutura do repositório

| Caminho | Descrição |
|---------|-----------|
| `src/api/main.py` | API FastAPI |
| `src/retrieval/chain.py` | Pipeline RAG |
| `src/ingestion/` | Carregadores de documentos |

## Pré-requisitos

Python 3.11+, opcional: Ollama instalado para respostas generativas.

## Instalação e execução

```bash
git clone https://github.com/SrSatriano/local-rag-second-mind-vault.git
cd local-rag-second-mind-vault
```

```bash
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

## Configuração

| Variável | Descrição | Exemplo |
|----------|-----------|--------|
| `OLLAMA_HOST` | URL do Ollama | `http://localhost:11434` |
| `LLM_MODEL` | Modelo local | `qwen2.5:7b` |

> **Importante:** nunca faça commit de arquivos `.env` com segredos reais. Use `.env.example` como referência.

## Testes

Execute a suíte de testes antes de abrir pull requests:

```bash
pytest tests/ -q
```

A pipeline [`.github/workflows/ci.yml`](.github/workflows/ci.yml) repete build e testes em cada push para `main`.

## Performance

| Modelo | Latência média de consulta |
|--------|---------------------------|
| Qwen 7B Q4 | 2–4 s |

Metodologia, hardware de referência e flags de compilação: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Deploy e operação

| Guia | Conteúdo |
|------|----------|
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Homologação, produção e rollback |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Monitoramento, alertas e incidentes |

## Limitações conhecidas

- Vector store em memória na v1.0; use Chroma persistente em produção

## Roadmap

- Embeddings sentence-transformers
- Suporte PDF nativo

## Documentação complementar

| Documento | Descrição |
|-----------|-----------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Arquitetura e decisões técnicas |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Deploy passo a passo |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Runbook operacional |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Como contribuir |
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões |
| [SECURITY.md](SECURITY.md) | Política de segurança |
| [AUTHORS.md](AUTHORS.md) | Créditos |

## Segurança e licença

- Dependências revisadas na release **1.0.0**
- Vulnerabilidades: siga [SECURITY.md](SECURITY.md)
- Licença: [MIT](LICENSE) © SrSatriano 2026

---

<p align="center">Desenvolvido com foco em clareza e engenharia de produção · <a href="https://github.com/SrSatriano/local-rag-second-mind-vault">Ver no GitHub</a></p>
