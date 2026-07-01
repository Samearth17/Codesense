from pydantic import BaseModel
from pathlib import Path

class FileRecord(BaseModel):
    repo: str
    language: str
    relative_path: str
    lines: int
    sha256: str
    label: str = "human"