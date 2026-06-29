# CodeSense ML

Independent machine-learning module for feature extraction, training, inference, dataset preparation, and evaluation.

This directory is intentionally decoupled from the FastAPI backend so research workflows and production inference code can evolve without forcing web-service changes.

## Layout

```text
feature_extractors/  # Static-analysis and authorship signal extraction modules
training/            # Training jobs, experiment entry points, and configs
inference/           # Model loading and prediction boundaries
datasets/            # ML-local dataset builders and validation utilities
evaluation/          # Metrics, reports, and benchmark workflows
```
