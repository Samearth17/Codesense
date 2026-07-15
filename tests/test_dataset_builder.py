# tests/test_dataset_builder.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ml"))

# Now all imports work:
