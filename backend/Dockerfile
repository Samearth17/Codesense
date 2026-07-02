FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

FROM base AS builder
COPY --from=ghcr.io/astral-sh/uv:0.5.13 /uv /uvx /bin/
COPY backend/pyproject.toml backend/README.md ./
RUN uv sync --no-dev --no-install-project

FROM base AS runner
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
COPY backend/app ./app
COPY ml/inference ./ml/inference
COPY ml/feature_extractors ./ml/feature_extractors
COPY ml/models ./ml/models
COPY ml/pyproject.toml ./ml/pyproject.toml
EXPOSE 8000
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
