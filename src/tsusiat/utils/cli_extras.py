import importlib.metadata as importlib_metadata

import typer


def _print_version(value: bool) -> None:
    if not value:
        return

    try:
        v = importlib_metadata.version("tsusiat")
    except importlib_metadata.PackageNotFoundError:
        v = "unknown"

    typer.echo(f"tsusiat {v}")
    raise typer.Exit()


VERSION_OPTION = typer.Option(
    False,
    "--version",
    "-V",
    help="Show version and exit.",
    callback=_print_version,
    is_eager=True,
)
