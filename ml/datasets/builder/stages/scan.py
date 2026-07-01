from pathlib import Path

def scan_files(repo_path: Path, ignore_dirs: set, extensions: set) -> list[Path]:
    results = []
    for path in repo_path.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignore_dirs for part in path.parts):
            continue
        if path.suffix in extensions:
            results.append(path)
    return results