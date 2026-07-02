from contextlib import asynccontextmanager
from time import perf_counter

import structlog
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api.dependencies import _load_predictor
from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging

logger = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Load the ML model once at startup so the first request isn't slow."""
    _load_predictor()
    yield


def create_app() -> FastAPI:
    """Create the FastAPI application and wire process-level concerns."""
    settings = get_settings()
    configure_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        debug=settings.app_debug,
        lifespan=lifespan,
    )
    if settings.backend_cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.backend_cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    @app.middleware("http")
    async def log_http_requests(request: Request, call_next):
        start_time = perf_counter()
        try:
            response = await call_next(request)
        except Exception:
            duration_ms = round((perf_counter() - start_time) * 1000, 2)
            logger.exception(
                "http_request_failed",
                method=request.method,
                path=request.url.path,
                duration_ms=duration_ms,
            )
            raise

        duration_ms = round((perf_counter() - start_time) * 1000, 2)
        logger.info(
            "http_request_completed",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=duration_ms,
        )
        return response

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    @app.get("/health")
    def health():
        return {"status": "ok", "service": "codesense-backend"}

    return app


app = create_app()
