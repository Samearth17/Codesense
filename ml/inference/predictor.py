import json
import sys
from pathlib import Path

import numpy as np
import shap
import xgboost as xgb

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "ml"))

from feature_extractors.extractor import extract_features  # noqa: E402
from vulnerability.scanner import VulnerabilityScanner  # noqa: E402

MODELS_DIR = ROOT / "ml" / "models"
META_PATH = MODELS_DIR / "model_meta.json"
MODEL_PATH = MODELS_DIR / "codesense_xgb.json"


class CodeSensePredictor:
    def __init__(self):
        meta = json.loads(META_PATH.read_text())
        self.feature_names: list[str] = meta["features"]
        self.model = xgb.XGBClassifier()
        self.model.load_model(str(MODEL_PATH))
        self.explainer = shap.TreeExplainer(self.model)
        self.vuln_scanner = VulnerabilityScanner()
        print(f"✓ Model loaded ({meta['num_features']} features, AUC {meta['test_auc']})")

    def predict(self, code: str, filename: str = "unnamed.py") -> dict:
        raw = extract_features(code)
        vuln_results = self.vuln_scanner.scan(code)

        missing_features = sorted(set(self.feature_names) - raw.keys())
        if missing_features:
            print(f"⚠️ Missing model features will be zero-filled: {', '.join(missing_features)}")

        vector = np.array([raw.get(f, 0.0) for f in self.feature_names], dtype=np.float32).reshape(
            1, -1
        )

        proba = self.model.predict_proba(vector)[0]
        ai_confidence = float(proba[1])
        label = "ai" if ai_confidence >= 0.5 else "human"
        top_signals = self._top_signals(vector)

        return {
            "label": label,
            "confidence": round(ai_confidence if label == "ai" else 1 - ai_confidence, 4),
            "is_ai": label == "ai",
            "top_signals": top_signals,
            "filename": filename,
            "vulnerabilities": vuln_results,
            "vulnerability_count": len(vuln_results),
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

    def _top_signals(self, vector: np.ndarray) -> list[str]:
        shap_values = np.asarray(self.explainer.shap_values(vector))
        if shap_values.ndim == 3:
            shap_values = shap_values[0]
            if shap_values.shape[0] == len(self.feature_names):
                shap_values = shap_values[:, -1]
            else:
                shap_values = shap_values[-1]
        elif shap_values.ndim == 2:
            shap_values = shap_values[0]

        if shap_values.shape[0] != len(self.feature_names):
            raise ValueError(
                "SHAP output does not match the model feature schema: "
                f"got {shap_values.shape[0]} values for {len(self.feature_names)} features"
            )

        ranked_indices = np.argsort(np.abs(shap_values))[::-1][:3]
        return [self.feature_names[index] for index in ranked_indices]


_predictor: CodeSensePredictor | None = None


def get_predictor() -> CodeSensePredictor:
    global _predictor
    if _predictor is None:
        _predictor = CodeSensePredictor()
    return _predictor
