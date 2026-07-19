from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .predictor import CodeSensePredictor, get_predictor
from .schemas import FeatureSnapshot, PredictRequest, PredictResponse, VulnerabilityResult

predictor: CodeSensePredictor = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global predictor
    predictor = get_predictor()
    yield


app = FastAPI(
    title="CodeSense API",
    description="Detects whether Python code was written by a human or AI",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "service": "CodeSense",
        "version": "1.0.0",
        "status": "running",
        "endpoints": ["/predict", "/health", "/docs"],
    }


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": predictor is not None}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    if len(request.code) > 500_000:
        raise HTTPException(status_code=400, detail="Code too large (max 500KB)")

    try:
        result = predictor.predict(request.code, request.filename)
        return PredictResponse(
            label=result["label"],
            confidence=result["confidence"],
            is_ai=result["is_ai"],
            top_signals=result["top_signals"],
            filename=result["filename"],
            vulnerabilities=[VulnerabilityResult(**item) for item in result["vulnerabilities"]],
            vulnerability_count=result["vulnerability_count"],
            features=FeatureSnapshot(**result["features"]),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
