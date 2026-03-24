# chatbotbackend

Backend for an educational LLM chatbot built during the GigaSchool LLM Engineer course.

The project exposes a FastAPI endpoint for chat requests, routes user input through a small LLM pipeline, and can use Qdrant as a retrieval layer for RAG-style answers.

## Features

- FastAPI HTTP API with `/health` and `/chat`
- LLM orchestration pipeline with dialog routing
- Qdrant-based document retrieval
- Telegram export parsing and indexing script
- `uv`, `ruff`, `mypy`, and `pre-commit` based developer workflow

## Tech Stack

- Python 3.11+
- FastAPI
- OpenAI-compatible API clients
- Qdrant
- uv
- Ruff
- mypy

## Project Structure

```text
src/
  app.py                  FastAPI entrypoint
  settings.py             Environment-based configuration
  dependencies.py         Dependency injection helpers
  clients/                LLM and Qdrant clients
  pipeline/               Orchestrator, context, graph config, nodes
scripts/
  parse_tg_messages.py    Telegram export parser and Qdrant indexer
docker-compose.yaml       Local Qdrant service
ISSUES.md                 Current backlog and known problems
```

## Requirements

- Python 3.11 or newer
- `uv`
- Docker Desktop or a local Qdrant instance
- Access to an OpenAI-compatible chat model and embedding model

## Quick Start

1. Clone the repository.
2. Copy `.env.example` to `.env`.
3. Fill in your API keys, model names, and Qdrant settings.
4. Create the local environment and install dependencies:

```powershell
uv sync --group lint --group type
```

5. Start Qdrant:

```powershell
docker compose up -d
```

6. Run the API:

```powershell
uv run uvicorn src.app:app --reload --host 0.0.0.0 --port 8080
```

## API

### Health Check

```http
GET /health
```

Response:

```json
{"status":"ok"}
```

### Chat

```http
POST /chat
Content-Type: application/json
```

Example request:

```json
{
  "query": "What is new in AI Talent Hub?",
  "history": [
    {
      "role": "user",
      "content": "Hello"
    },
    {
      "role": "assistant",
      "content": "Hi! How can I help?"
    }
  ]
}
```

## Indexing Telegram Data

To load Telegram export data into Qdrant:

```powershell
uv run python scripts/parse_tg_messages.py --export-path data/your_export.json
```

Note:
`data/` is ignored by git and is intended for local datasets only.

## Development

Run formatting and linting:

```powershell
uv run ruff format .
uv run ruff check . --fix
```

Run type checking:

```powershell
uv run mypy src
```

Optionally install git hooks:

```powershell
uv run pre-commit install
```

## Current Status

This repository is in an early educational MVP stage. The main structure is in place, but there are still known runtime and typing issues in the pipeline implementation.

See `ISSUES.md` for the current backlog.

## License

No license has been added yet.
