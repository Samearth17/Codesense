"""Request and response contracts for the code-scan endpoint."""

from pydantic import BaseModel, Field, field_validator


class ScanRequest(BaseModel):
    """Payload for a code-authorship scan."""

    code: str = Field(
        ...,
        min_length=1,
        max_length=500_000,
        description="Python source code to analyze.",
    )
    filename: str = Field(
        default="unnamed.py",
        min_length=1,
        max_length=255,
        description="Optional filename for context.",
    )

    @field_validator("code")
    @classmethod
    def code_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Code must contain at least one non-whitespace character.")
        return value

    @field_validator("filename")
    @classmethod
    def filename_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Filename must contain at least one non-whitespace character.")
        return value


class FeatureSnapshot(BaseModel):
    """Subset of extracted features surfaced in the API response."""

    docstring_ratio: float
    type_annotation_ratio: float
    maintainability_index: float
    avg_identifier_length: float
    single_char_var_ratio: float
    comment_density: float
    blank_line_ratio: float
    avg_cyclomatic_complexity: float


class VulnerabilityResult(BaseModel):
    """A static-analysis vulnerability finding."""

    rule: str
    severity: str = Field(..., pattern="^(high|medium|low)$")
    line: int = Field(..., ge=1)
    message: str
    ai_pattern: bool


class ScanResponse(BaseModel):
    """Structured result of an authorship analysis."""

    label: str = Field(..., description="'ai' or 'human'.")
    confidence: float = Field(..., ge=0, le=1, description="Confidence in the predicted label.")
    is_ai: bool = Field(..., description="True when the prediction is AI-authored.")
    top_signals: list[str] = Field(
        ...,
        description="Up to 3 feature names that most influenced the prediction.",
    )
    features: FeatureSnapshot = Field(
        ...,
        description="Key code metrics extracted during analysis.",
    )
    filename: str
    vulnerabilities: list[VulnerabilityResult]
    vulnerability_count: int = Field(..., ge=0)
