from pathlib import Path

def filter_file(path: Path, min_lines: int, max_lines: int) -> bool:
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
        lines = content.splitlines()
        return min_lines <= len(lines) <= max_lines
    except Exception:
        return False