import hashlib
import json
from pathlib import Path

from datasets import load_dataset

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "datasets" / "ai"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Downloading dataset from HuggingFace...")
ds = load_dataset("iamtarun/python_code_instructions_18k_alpaca", split="train")
print(f"Dataset loaded. Total entries: {len(ds)}")

records = []
count = 0

for item in ds:
    if count >= 2000:
        break
    code = item.get("output", "").strip()
    if not code or len(code.splitlines()) < 15:
        continue

    sha = hashlib.sha256(code.encode()).hexdigest()
    filename = f"ai_sample_{count:04d}.py"
    (OUTPUT_DIR / filename).write_text(code, encoding="utf-8")
    records.append(
        {
            "repo": "huggingface/python_code_instructions_18k_alpaca",
            "language": "python",
            "relative_path": filename,
            "lines": len(code.splitlines()),
            "sha256": sha,
            "label": "ai",
        }
    )
    count += 1
    if count % 100 == 0:
        print(f"  {count}/600 files saved...")

(OUTPUT_DIR / "metadata.json").write_text(json.dumps(records, indent=2))
print(f"\n✓ Done! {count} AI samples → datasets/ai/")
