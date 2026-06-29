# CodeSense

CodeSense is an explainable AI-assisted code authorship analysis platform. It is designed to combine static analysis and machine learning to estimate whether source code is AI-assisted or human-written, without relying on LLM APIs.

This repository currently contains the production architecture scaffold only. Application logic, model implementation, and product workflows will be added in later iterations.

## Repository Layout

```text
codesense/
├── frontend/   # Next.js 15 App Router UI
├── backend/    # FastAPI service boundary and API architecture
├── ml/         # Independent ML experimentation and inference module
├── datasets/   # Versioned dataset manifests and documentation placeholders
├── models/     # Model artifact metadata placeholders
├── docs/       # Architecture, API, roadmap, and ML pipeline notes
├── scripts/    # Project automation entry points
├── tests/      # Cross-service and contract test placeholders
├── docker/     # Docker Compose and deployment support files
└── .github/    # CI workflows
```

## Local Development

Copy environment examples before running services:

```bash
cp frontend/.env.example frontend/.env.local
cp backend/.env.example backend/.env
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Backend:

```bash
cd backend
uv sync
uv run fastapi dev app/main.py
```

Docker Compose:

```bash
docker compose up --build
```

## Quality Gates

- Frontend: ESLint, Prettier, TypeScript
- Backend: Ruff, Pytest, Python 3.12 via uv
- CI: GitHub Actions lint and test workflow

## Architecture Principles

- Clear separation between UI, API, service orchestration, data contracts, and ML modules.
- Dependency injection at service boundaries so implementations can be swapped for tests, local inference, or deployed model runtimes.
- Independent ML package structure so research code can mature without coupling to web request handling.
- Configuration through environment variables and typed settings.
