# Issue List

This file tracks the current backlog and known issues for the project. It can later be converted into GitHub Issues.

## P0

- [ ] Fix runtime import failure in `src/pipeline/abc_base_node.py`. `Context` is used in annotations at runtime while imported only under `TYPE_CHECKING`.
- [ ] Keep Python version requirements aligned with the actual code. The current implementation uses `StrEnum`, so Python 3.11+ is required.

## P1

- [ ] Fix Telegram parsing bug in `scripts/parse_tg_messages.py`. The script checks `len("text")` instead of the parsed message text.
- [ ] Fix document formatting in `src/pipeline/nodes/generate_answer.py`. There is a broken string encoding and document numbering is hardcoded.
- [ ] Add safer handling when `context.documents` is empty or `None`.
- [ ] Add a startup smoke test for importing the FastAPI app.

## P2

- [ ] Tighten types in `src/pipeline/orchestrator.py` so `next_node` and `output` are not based on nullable assumptions.
- [ ] Validate Qdrant payload access in `src/clients/qdrant.py` before reading `payload["text"]`.
- [ ] Improve prompt quality and routing logic in `src/pipeline/nodes/dialog_type_decision.py`.

## Repository Hygiene

- [ ] Add automated tests for API, retrieval, and pipeline behavior.
- [ ] Consider GitHub Actions for lint and type checks.
- [ ] Decide on a project license.
