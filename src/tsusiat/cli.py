import typer

from tsusiat.utils.cli_extras import VERSION_OPTION

app = typer.Typer(add_completion=False)


@app.callback()
def main(
    version: bool = VERSION_OPTION,
) -> None:
    """tsusiat: project timeline scheduling."""
