"""Command-line interface for CodeSense scans."""

from __future__ import annotations

import json
from pathlib import Path

import typer
from inference.predictor import get_predictor
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="codesense",
    help="Detect AI-assisted Python code and static vulnerability patterns.",
    add_completion=False,
)


@app.callback()
def main() -> None:
    """CodeSense command group."""


def _python_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if path.suffix == ".py" else []
    if path.is_dir():
        return sorted(item for item in path.rglob("*.py") if item.is_file())
    raise typer.BadParameter(f"Path does not exist: {path}")


@app.command()
def scan(
    path: Path = typer.Argument(  # noqa: B008
        ..., help="Python file or directory to scan"
    ),
    threshold: float = typer.Option(  # noqa: B008
        0.5, min=0, max=1, help="AI confidence threshold"
    ),
    format: str = typer.Option("table", help="Output format: table or json"),  # noqa: B008
    show_vulns: bool = typer.Option(  # noqa: B008
        False, "--show-vulns", help="Show vulnerability findings"
    ),
) -> None:
    """Recursively scan a file or directory and return a CI-friendly exit code."""
    if format not in {"table", "json"}:
        raise typer.BadParameter("format must be 'table' or 'json'")

    files = _python_files(path)
    if not files:
        typer.echo("No Python files found.", err=True)
        raise typer.Exit(1)

    predictor = get_predictor()
    results = []
    for file in files:
        try:
            result = predictor.predict(file.read_text(errors="ignore"), filename=str(file))
            results.append(result)
        except OSError as exc:
            typer.echo(f"Skipped {file}: {exc}", err=True)

    if format == "json":
        typer.echo(json.dumps(results, indent=2))
    else:
        table = Table(title="CodeSense Scan Results")
        table.add_column("Filename", style="cyan")
        table.add_column("AI%", justify="right")
        table.add_column("Label")
        table.add_column("Top signal")
        table.add_column("Vuln count", justify="right")
        for result in results:
            ai_confidence = result["confidence"] if result["is_ai"] else 1 - result["confidence"]
            table.add_row(
                result["filename"],
                f"{ai_confidence * 100:.0f}%",
                result["label"].upper(),
                result["top_signals"][0] if result["top_signals"] else "-",
                str(result["vulnerability_count"]),
            )
        Console().print(table)
        if show_vulns:
            for result in results:
                for finding in result["vulnerabilities"]:
                    typer.echo(
                        f"{result['filename']}:{finding['line']} [{finding['severity']}] "
                        f"{finding['rule']}: {finding['message']}"
                    )

    if any(result["is_ai"] and result["confidence"] >= threshold for result in results):
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
