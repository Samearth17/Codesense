import json
import sys
from pathlib import Path

import numpy as np
import xgboost as xgb

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "ml"))

from feature_extractors.extractor import extract_features

MODELS_DIR = ROOT / "ml" / "models"
META_PATH = MODELS_DIR / "model_meta.json"
MODEL_PATH = MODELS_DIR / "codesense_xgb.json"

SIGNAL_PRIORITY = [
    "docstring_ratio",
    "type_annotation_ratio",
    "maintainability_index",
    "avg_identifier_length",
    "single_char_var_ratio",
    "comment_density",
    "blank_line_ratio",
    "avg_cyclomatic_complexity",
    "magic_number_count",
    "assertion_count",
    "num_try_except",
    "long_line_ratio",
]


class CodeSensePredictor:
    def __init__(self):
        meta = json.loads(META_PATH.read_text())
        self.feature_names: list[str] = meta["features"]
        self.model = xgb.XGBClassifier()
        self.model.load_model(str(MODEL_PATH))
        print(f"✓ Model loaded ({meta['num_features']} features, AUC {meta['test_auc']})")

    def predict(self, code: str, filename: str = "unnamed.py") -> dict:
        raw = extract_features(code)

        vector = np.array([raw.get(f, 0.0) for f in self.feature_names], dtype=np.float32).reshape(
            1, -1
        )

        proba = self.model.predict_proba(vector)[0]
        ai_confidence = float(proba[1])
        label = "ai" if ai_confidence >= 0.5 else "human"
        top_signals = self._top_signals(raw, label)

        return {
            "label": label,
            "confidence": round(ai_confidence if label == "ai" else 1 - ai_confidence, 4),
            "is_ai": label == "ai",
            "top_signals": top_signals,
            "filename": filename,
            "features": {
                "docstring_ratio": round(raw.get("docstring_ratio", 0), 4),
                "type_annotation_ratio": round(raw.get("type_annotation_ratio", 0), 4),
                "maintainability_index": round(raw.get("maintainability_index", 0), 2),
                "avg_identifier_length": round(raw.get("avg_identifier_length", 0), 2),
                "single_char_var_ratio": round(raw.get("single_char_var_ratio", 0), 4),
                "comment_density": round(raw.get("comment_density", 0), 4),
                "blank_line_ratio": round(raw.get("blank_line_ratio", 0), 4),
                "avg_cyclomatic_complexity": round(raw.get("avg_cyclomatic_complexity", 0), 2),
            },
        }

    def _top_signals(self, features: dict, label: str) -> list[str]:
        signals = []
        for feat in SIGNAL_PRIORITY:
            val = features.get(feat, 0)
            if feat == "docstring_ratio" and val > 0.6 or feat == "type_annotation_ratio" and val > 0.6 or feat == "maintainability_index" and val > 80 or feat == "single_char_var_ratio" and val < 0.03 or feat == "avg_identifier_length" and val > 8 or feat == "comment_density" and val > 0.2 or feat == "assertion_count" and val > 3 or feat == "num_try_except" and val > 2:
                signals.append(feat)
            if len(signals) == 3:
                break
        return signals if signals else ["avg_cyclomatic_complexity"]


_predictor: CodeSensePredictor | None = None


def get_predictor() -> CodeSensePredictor:
    global _predictor
    if _predictor is None:
        _predictor = CodeSensePredictor()
    return _predictor
