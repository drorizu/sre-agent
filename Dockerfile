--------------------------------------------------
SRE Agent - Production Docker Image
--------------------------------------------------

FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

Install build dependencies.

RUN pip install --no-cache-dir --upgrade pip hatchling

Copy project metadata and source code.

COPY pyproject.toml README.md LICENSE ./ COPY src/ ./src/

Build the application wheel.

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels .

--------------------------------------------------
Runtime stage
--------------------------------------------------

FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
PIP_NO_CACHE_DIR=1
PYTHONPATH=/app/src
PORT=8000

WORKDIR /app

Create a dedicated non-root application user.

RUN groupadd --system app &&
useradd --system --gid app --home-dir /app app

Install the built application package.

COPY --from=builder /wheels /wheels

RUN pip install --no-cache-dir --no-index --find-links=/wheels sre-agent &&
rm -rf /wheels

Copy application source.

COPY --chown=app:app src/ ./src/

Switch to the non-root user.

USER app

Expose the application port.

EXPOSE 8000

Container health check.

HEALTHCHECK --interval=30s
--timeout=5s
--start-period=15s
--retries=3
CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)" || exit 1

Start the FastAPI application.

CMD ["uvicorn", "sre_agent.main:app", "--host", "0.0.0.0", "--port", "8000"]
