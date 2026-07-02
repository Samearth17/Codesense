"""Dependency providers for request-scoped resources.

Keep dependency wiring here so route modules stay focused on transport concerns
and services remain easy to replace in tests.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING

# Ensure the repo root is on sys.path so we can import from the ml/ package.
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

if TYPE_CHECKING:
    from ml.inference.predictor import CodeSensePredictor

_predictor: CodeSensePredictor | None = None


def _load_predictor() -> CodeSensePredictor:
    """Eagerly load the model. Called once during application lifespan."""
    global _predictor  # noqa: PLW0603
    if _predictor is None:
        from ml.inference.predictor import CodeSensePredictor

        _predictor = CodeSensePredictor()
    return _predictor


def get_predictor() -> CodeSensePredictor:
    """FastAPI dependency that returns the singleton predictor.

    The predictor is initialised during the application lifespan event
    (see ``app.main``) so this will never return ``None`` at request time.
    """
    if _predictor is None:
        return _load_predictor()
    return _predictor
