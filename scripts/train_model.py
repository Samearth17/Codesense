import sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ml"))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap
import xgboost as xgb
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, roc_curve, ConfusionMatrixDisplay
)
from sklearn.preprocessing import LabelEncoder
import pickle

# ── Load data ──────────────────────────────────────────────────────
df = pd.read_csv(ROOT / "datasets" / "features.csv")
print(f"Dataset: {df.shape[0]} rows × {df.shape[1]-1} features")
print(f"Labels : {df['label'].value_counts().to_dict()}")

FEATURES = [c for c in df.columns if c != "label"]
X = df[FEATURES].values
y = (df["label"] == "ai").astype(int).values   # 1=AI, 0=human

# ── Train/test split ───────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\nTrain: {len(X_train)} | Test: {len(X_test)}")

# ── Model ──────────────────────────────────────────────────────────
model = xgb.XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    use_label_encoder=False,
    eval_metric="logloss",
    random_state=42,
    n_jobs=-1,
)

# ── Cross-validation ───────────────────────────────────────────────
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring="roc_auc")
print(f"\n5-Fold CV AUC: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# ── Final training ─────────────────────────────────────────────────
model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    verbose=False,
)

# ── Evaluation ─────────────────────────────────────────────────────
y_pred  = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]
auc     = roc_auc_score(y_test, y_proba)

print(f"\nTest AUC   : {auc:.4f}")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["human", "ai"]))

# ── Plots ──────────────────────────────────────────────────────────
PLOTS = ROOT / "ml" / "plots"
PLOTS.mkdir(exist_ok=True)

# 1. Confusion matrix
fig, ax = plt.subplots(figsize=(5, 4))
ConfusionMatrixDisplay(
    confusion_matrix(y_test, y_pred),
    display_labels=["Human", "AI"]
).plot(ax=ax, colorbar=False, cmap="Blues")
ax.set_title("Confusion Matrix")
plt.tight_layout()
plt.savefig(PLOTS / "confusion_matrix.png", dpi=150)
plt.close()
print("Saved: confusion_matrix.png")

# 2. ROC curve
fpr, tpr, _ = roc_curve(y_test, y_proba)
fig, ax = plt.subplots(figsize=(5, 4))
ax.plot(fpr, tpr, lw=2, label=f"AUC = {auc:.3f}")
ax.plot([0,1],[0,1],"--", color="gray")
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("ROC Curve")
ax.legend()
plt.tight_layout()
plt.savefig(PLOTS / "roc_curve.png", dpi=150)
plt.close()
print("Saved: roc_curve.png")

# 3. Feature importance
importances = model.feature_importances_
feat_df = pd.DataFrame({"feature": FEATURES, "importance": importances})
feat_df = feat_df.sort_values("importance", ascending=True).tail(20)

fig, ax = plt.subplots(figsize=(7, 8))
ax.barh(feat_df["feature"], feat_df["importance"], color="#01696f")
ax.set_xlabel("Importance Score")
ax.set_title("Top Feature Importances (XGBoost)")
plt.tight_layout()
plt.savefig(PLOTS / "feature_importance.png", dpi=150)
plt.close()
print("Saved: feature_importance.png")

# 4. SHAP summary plot
explainer   = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
fig, ax = plt.subplots(figsize=(8, 8))
shap.summary_plot(shap_values, X_test, feature_names=FEATURES, show=False)
plt.tight_layout()
plt.savefig(PLOTS / "shap_summary.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved: shap_summary.png")

# ── Save model + metadata ──────────────────────────────────────────
MODELS = ROOT / "ml" / "models"
MODELS.mkdir(exist_ok=True)

model.save_model(str(MODELS / "codesense_xgb.json"))

meta = {
    "features"     : FEATURES,
    "num_features" : len(FEATURES),
    "cv_auc_mean"  : round(float(cv_scores.mean()), 4),
    "cv_auc_std"   : round(float(cv_scores.std()),  4),
    "test_auc"     : round(auc, 4),
    "train_size"   : len(X_train),
    "test_size"    : len(X_test),
}
(MODELS / "model_meta.json").write_text(json.dumps(meta, indent=2))

print(f"\n✓ Model saved  → ml/models/codesense_xgb.json")
print(f"✓ Meta saved   → ml/models/model_meta.json")
print(f"✓ Plots saved  → ml/plots/")