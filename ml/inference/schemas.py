from pydantic import BaseModel


class PredictRequest(BaseModel):
    code: str
    filename: str = "unnamed.py"


class FeatureSnapshot(BaseModel):
    docstring_ratio: float
    type_annotation_ratio: float
    maintainability_index: float
    avg_identifier_length: float
    single_char_var_ratio: float
    comment_density: float
    blank_line_ratio: float
    avg_cyclomatic_complexity: float


class PredictResponse(BaseModel):
    label: str
    confidence: float
    is_ai: bool
    top_signals: list[str]
    features: FeatureSnapshot
    filename: str
