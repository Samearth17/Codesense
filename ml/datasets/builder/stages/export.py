import shutil
from pathlib import Path

from ..models import FileRecord


def export_files(records: list[FileRecord], output_dir: Path, workspace: Path) -> None:
    for record in records:
        repo_name = record.repo.replace("/", "__")
        source = workspace / repo_name / record.relative_path
        dest = output_dir / repo_name / record.relative_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        if source.exists():
            shutil.copy2(source, dest)
