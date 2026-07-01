import sys, json, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ml"))

from feature_extractors.extractor import extract_features

HUMAN_DIR = ROOT / "datasets" / "human"
AI_DIR    = ROOT / "datasets" / "ai"
OUTPUT    = ROOT / "datasets" / "features.csv"

human_records = json.loads((HUMAN_DIR / "metadata.json").read_text())
ai_records    = json.loads((AI_DIR    / "metadata.json").read_text())
all_records   = human_records + ai_records

print(f"Human: {len(human_records)} | AI: {len(ai_records)} | Total: {len(all_records)}")

rows = []
errors = 0

for i, record in enumerate(all_records):
    if record["label"] == "human":
        repo_name = record["repo"].replace("/", "__")
        file_path = HUMAN_DIR / repo_name / record["relative_path"]
    else:
        file_path = AI_DIR / record["relative_path"]

    if not file_path.exists():
        errors += 1
        continue

    try:
        code = file_path.read_text(errors="ignore")
        features = extract_features(code)
        features["label"] = record["label"]
        rows.append(features)
    except Exception:
        errors += 1
        continue

    if i % 500 == 0 and i > 0:
        print(f"  {i}/{len(all_records)} processed...")

if rows:
    fieldnames = list(rows[0].keys())
    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

print(f"\n✓ features.csv written")
print(f"  Rows     : {len(rows)}")
print(f"  Features : {len(fieldnames) - 1}")
print(f"  Errors   : {errors}")