import subprocess
from pathlib import Path

def clone_repo(repo: str, target_dir: Path) -> Path:
    repo_name = repo.replace("/", "__")
    dest = target_dir / repo_name
    if dest.exists():
        print(f"  (already cloned, skipping)")
        return dest
    url = f"https://github.com/{repo}.git"
    subprocess.run(
        ["git", "clone", "--depth=1", url, str(dest)],
        check=True, capture_output=True
    )
    return dest