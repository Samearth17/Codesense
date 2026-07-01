from ..models import FileRecord

def deduplicate(records: list[FileRecord]) -> list[FileRecord]:
    seen: set[str] = set()
    unique = []
    for r in records:
        if r.sha256 not in seen:
            seen.add(r.sha256)
            unique.append(r)
    return unique