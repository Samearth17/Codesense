SEED_REPOS = [
    "TheAlgorithms/Python",
    "psf/requests",
    "pallets/flask",
    "tiangolo/fastapi",
    "django/django",
    "scrapy/scrapy",
    "httpie/cli",
]

IGNORE_DIRS = {
    ".git", "__pycache__", "node_modules", "build",
    "dist", "venv", ".tox", "tests", "test", "docs"
}

LANGUAGE_MAP = {
    ".py": "python"
}

MIN_LINES = 15
MAX_LINES = 400