# tests/test_dataset_builder.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ml"))

# Now all imports work:
from datasets.builder.stages.filter import filter_file
from datasets.builder.stages.hasher import sha256_file
from datasets.builder.stages.dedup import deduplicate
from datasets.builder.models import FileRecord