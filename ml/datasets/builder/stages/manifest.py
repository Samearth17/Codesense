import json
from pathlib import Path

from ..models import FileRecord


def write_manifest(records: list[FileRecord], output_dir: Path) -> None:
    data = [r.model_dump() for r in records]
    manifest_path = output_dir / "metadata.json"
    manifest_path.write_text(json.dumps(data, indent=2))
    print(f"  Manifest: {len(data)} entries → {manifest_path}")
