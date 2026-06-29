# CodeSense Backend

FastAPI service scaffold for the CodeSense platform.

## Layout

```text
app/
├── api/       # HTTP routing, versioning, and dependency adapters
├── core/      # Settings, logging, security, and process-wide configuration
├── services/  # Application service interfaces and orchestration boundaries
├── models/    # Persistence-facing models when storage is introduced
├── schemas/   # Pydantic request and response contracts
└── utils/     # Framework-neutral helpers shared across backend modules
```

Keep domain behavior out of route handlers. Routes should validate transport concerns, call services, and return schemas.
