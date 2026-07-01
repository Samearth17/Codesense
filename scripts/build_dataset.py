# scripts/build_dataset.py
import sys
from pathlib import Path

# Tell Python: "look inside ml/ for imports"
ROOT = Path(__file__).resolve().parent.parent   # → codesense/
sys.path.insert(0, str(ROOT / "ml"))            # → codesense/ml/

from datasets.builder import DatasetPipeline    # now resolves correctly

pipeline = DatasetPipeline(
    workspace=ROOT / "tmp" / "clones",
    output=ROOT / "datasets" / "human",
)
records = pipeline.run()
print(f"\nDone. {len(records)} files ready.")