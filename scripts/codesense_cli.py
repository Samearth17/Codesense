import json
import sys
from pathlib import Path

import typer
from rich import box
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ml"))

from inference.predictor import get_predictor

cli = typer.Typer(
    name="codesense",
    help="🔍 Detect whether Python code was written by a human or AI",
    add_completion=False,
)

SUPPORTED = {".py"}


def _verdict_panel(result: dict, path: str) -> Panel:
    result["label"]
    confidence = result["confidence"]
    is_ai = result["is_ai"]
    signals = result["top_signals"]
    feats = result["features"]

    verdict = (
        Text("🤖  AI GENERATED", style="bold red")
        if is_ai
        else Text("✅  HUMAN WRITTEN", style="bold green")
    )
    pct = f"{confidence * 100:.1f}%"

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
    table.add_column("Feature", style="dim")
    table.add_column("Value", justify="right")

    table.add_row("Docstring ratio", f"{feats['docstring_ratio']:.2f}")
    table.add_row("Type annotation ratio", f"{feats['type_annotation_ratio']:.2f}")
    table.add_row("Maintainability index", f"{feats['maintainability_index']:.1f}")
    table.add_row("Avg identifier length", f"{feats['avg_identifier_length']:.1f}")
    table.add_row("Single char var ratio", f"{feats['single_char_var_ratio']:.2f}")
    table.add_row("Comment density", f"{feats['comment_density']:.2f}")
    table.add_row("Cyclomatic complexity", f"{feats['avg_cyclomatic_complexity']:.1f}")

    signals_str = ", ".join(signals) if signals else "—"

    content = Text.assemble(
        ("File       : ", "bold"),
        (f"{path}\n", ""),
        ("Verdict    : ", "bold"),
        verdict,
        "\n",
        ("Confidence : ", "bold"),
        (f"{pct}\n", "yellow"),
        ("Top signals: ", "bold"),
        (f"{signals_str}\n\n", "magenta"),
    )

    return Panel(
        Group(content, table),
        title="[bold white]CodeSense[/bold white]",
        border_style="red" if is_ai else "green",
        padding=(1, 2),
    )


@cli.command()
def scan(
    path: Path = typer.Argument(..., help="Python file or directory to scan"),
    recursive: bool = typer.Option(
        False, "--recursive", "-r", help="Scan directory recursively"
    ),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output raw JSON"),
    min_confidence: float = typer.Option(
        0.0, "--min-confidence", help="Only show results above this threshold (0.0-1.0)"
    ),
):
    """Scan a Python file or directory for AI-generated code."""

    predictor = get_predictor()
    console = Console()

    # Collect files
    if path.is_file():
        files = [path] if path.suffix in SUPPORTED else []
    elif path.is_dir():
        pattern = "**/*.py" if recursive else "*.py"
        files = list(path.glob(pattern))
    else:
        typer.echo(f"❌ Path not found: {path}", err=True)
        raise typer.Exit(1)

    if not files:
        typer.echo("No Python files found.", err=True)
        raise typer.Exit(1)

    results = []
    for f in files:
        try:
            code = f.read_text(errors="ignore")
            result = predictor.predict(code, filename=f.name)
            result["path"] = str(f)
            results.append(result)
        except Exception as e:
            typer.echo(f"⚠️  Skipped {f}: {e}", err=True)

    if min_confidence > 0:
        results = [r for r in results if r["confidence"] >= min_confidence]

    if not results:
        typer.echo("No results matched the confidence threshold.")
        raise typer.Exit(0)

    # JSON mode
    if json_output:
        typer.echo(json.dumps(results, indent=2))
        return

    # Single file → detailed panel
    if len(results) == 1:
        console.print(_verdict_panel(results[0], results[0]["path"]))
        return

    # Multiple files → summary table
    table = Table(
        title="CodeSense Scan Results",
        box=box.ROUNDED,
        header_style="bold cyan",
        show_lines=True,
    )
    table.add_column("File", style="dim", max_width=60)
    table.add_column("Verdict", justify="center")
    table.add_column("Confidence", justify="right")
    table.add_column("Top Signal", style="magenta")

    ai_count = 0
    human_count = 0

    for r in results:
        if r["is_ai"]:
            verdict = "[bold red]🤖 AI[/bold red]"
            ai_count += 1
        else:
            verdict = "[bold green]✅ Human[/bold green]"
            human_count += 1

        table.add_row(
            r["path"],
            verdict,
            f"{r['confidence'] * 100:.1f}%",
            r["top_signals"][0] if r["top_signals"] else "—",
        )

    console.print(table)
    console.print(
        f"\n[bold]Summary:[/bold] "
        f"[green]{human_count} human[/green] · "
        f"[red]{ai_count} AI[/red] · "
        f"{len(results)} total"
    )


@cli.command()
def version():
    """Show CodeSense version."""
    typer.echo("CodeSense v1.0.0")


if __name__ == "__main__":
    cli()
