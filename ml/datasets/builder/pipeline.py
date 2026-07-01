# ml/datasets/builder/pipeline.py
import shutil
from pathlib import Path
from .config import SEED_REPOS, LANGUAGE_MAP, IGNORE_DIRS, MIN_LINES, MAX_LINES
from .models import FileRecord
from .stages.clone import clone_repo
from .stages.scan import scan_files
from .stages.filter import filter_file
from .stages.hasher import sha256_file
from .stages.dedup import deduplicate
from .stages.export import export_files
from .stages.manifest import write_manifest


class DatasetPipeline:
    def __init__(self, workspace: Path, output: Path):
        self.workspace = workspace  # tmp clones go here
        self.output = output        # datasets/human/ goes here
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.output.mkdir(parents=True, exist_ok=True)

    def run(self) -> list[FileRecord]:
        all_records: list[FileRecord] = []

        for repo in SEED_REPOS:
            print(f"\n→ Processing {repo}")
            try:
                repo_path = clone_repo(repo, self.workspace)
            except Exception as e:
                print(f"  ✗ Clone failed: {e}")
                continue

            files = scan_files(repo_path, IGNORE_DIRS, set(LANGUAGE_MAP.keys()))
            print(f"  Scanned: {len(files)} files")

            kept = 0
            for f in files:
                if not filter_file(f, MIN_LINES, MAX_LINES):
                    continue
                try:
                    sha = sha256_file(f)
                    record = FileRecord(
                        repo=repo,
                        language=LANGUAGE_MAP[f.suffix],
                        relative_path=str(f.relative_to(repo_path)),
                        lines=len(f.read_text(errors="ignore").splitlines()),
                        sha256=sha,
                    )
                    all_records.append(record)
                    kept += 1
                except Exception:
                    continue
            print(f"  Kept: {kept} files")

        unique = deduplicate(all_records)
        print(f"\n✓ Total unique files: {len(unique)}")

        export_files(unique, self.output, self.workspace)
        write_manifest(unique, self.output)
        print(f"✓ Exported to {self.output}")
        return unique