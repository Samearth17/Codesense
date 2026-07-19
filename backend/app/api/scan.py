"""Route module for code-authorship scanning."""

import ast
from typing import Annotated, Any, NoReturn

import structlog
from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_predictor
from app.schemas.scan import FeatureSnapshot, ScanRequest, ScanResponse, VulnerabilityResult

router = APIRouter(tags=["scan"])
logger = structlog.get_logger(__name__)


def _validate_python_source(code: str) -> None:
    try:
        ast.parse(code)
    except SyntaxError as exc:
        line = exc.lineno or 0
        raise ValueError(f"Invalid Python syntax at line {line}: {exc.msg}") from exc


def _raise_model_unavailable(exc: FileNotFoundError, filename: str | None = None) -> NoReturn:
    logger.exception(
        "scan_model_file_missing",
        filename=filename,
        error=str(exc),
    )
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail={
            "message": (
                "CodeSense model artifacts are unavailable. Please retry after deployment is fixed."
            ),
            "type": "model_unavailable",
        },
    ) from exc


def get_scan_predictor() -> Any:
    try:
        return get_predictor()
    except FileNotFoundError as exc:
        _raise_model_unavailable(exc)


@router.post("/scan", response_model=ScanResponse)
def scan_code(
    request: ScanRequest,
    predictor: Annotated[Any, Depends(get_scan_predictor)],
) -> ScanResponse:
    """Analyze Python source code and return an AI-vs-human authorship estimate."""
    try:
        _validate_python_source(request.code)
        result = predictor.predict(request.code, request.filename)
        return ScanResponse(
            label=result["label"],
            confidence=result["confidence"],
            is_ai=result["is_ai"],
            top_signals=result["top_signals"],
            filename=result["filename"],
            vulnerabilities=[VulnerabilityResult(**item) for item in result["vulnerabilities"]],
            vulnerability_count=result["vulnerability_count"],
            features=FeatureSnapshot(**result["features"]),
        )
    except ValueError as exc:
        logger.warning(
            "scan_validation_failed",
            filename=request.filename,
            error=str(exc),
        )
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "message": str(exc),
                "type": "invalid_python",
            },
        ) from exc
    except FileNotFoundError as exc:
        _raise_model_unavailable(exc, request.filename)
    except RuntimeError as exc:
        logger.exception(
            "scan_runtime_failed",
            filename=request.filename,
            error=str(exc),
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "The analysis runtime failed while processing this file.",
                "type": "analysis_runtime_error",
            },
        ) from exc
    except Exception as exc:
        logger.exception(
            "scan_unexpected_error",
            filename=request.filename,
            error=str(exc),
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Analysis failed unexpectedly. Please try again.",
                "type": "analysis_failed",
            },
        ) from exc
