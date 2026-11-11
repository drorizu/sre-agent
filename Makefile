.PHONY: install install-dev run test test-unit test-integration lint format typecheck coverage clean docker-up docker-down docker-build migrate migration shell

Install application

install: python -m pip install -e .

Install application with development dependencies

install-dev: python -m pip install -e ".[dev,llm]"

Run FastAPI application

run: uvicorn sre_agent.main:app --host 0.0.0.0 --port 8000 --reload

Run all tests

test: pytest

Run unit tests

test-unit: pytest tests/unit -v

Run integration tests

test-integration: pytest tests/integration -v

Run test coverage

coverage: pytest --cov=sre_agent --cov-report=html --cov-report=term-missing

Run linting

lint: ruff check .

Format source code

format: ruff format .

Run static type checking

typecheck: mypy src

Start Docker services

docker-up: docker compose up -d

Stop Docker services

docker-down: docker compose down

Build Docker image

docker-build: docker compose build

Apply database migrations

migrate: alembic upgrade head

Create a new database migration

migration: alembic revision --autogenerate -m "$(message)"

Open application shell

shell: python -c "import sre_agent; print('SRE Agent package loaded')"

Remove generated files

clean: python -c "import shutil; from pathlib import Path; [shutil.rmtree(p, ignore_errors=True) for p in Path('.').rglob('pycache')]; [p.unlink(missing_ok=True) for p in Path('.').rglob('*.pyc')]"
