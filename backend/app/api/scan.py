"""Route module for code-authorship scanning."""

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import get_predictor
from app.schemas.scan import FeatureSnapshot, ScanRequest, ScanResponse

router = APIRouter(tags=["scan"])


@router.post("/scan", response_model=ScanResponse)
def scan_code(
    request: ScanRequest,
    predictor=Depends(get_predictor),
) -> ScanResponse:
    """Analyze Python source code and return an AI-vs-human authorship estimate."""
    try:
        result = predictor.predict(request.code, request.filename)
        return ScanResponse(
            label=result["label"],
            confidence=result["confidence"],
            is_ai=result["is_ai"],
            top_signals=result["top_signals"],
            filename=result["filename"],
            features=FeatureSnapshot(**result["features"]),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {exc}") from exc
