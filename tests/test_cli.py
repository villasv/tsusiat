import re
from importlib.metadata import version as pkg_version

from typer.testing import CliRunner

from tsusiat.cli import app


def test_help_flag() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0

    def _normalize(text: str) -> str:
        no_spacing = re.sub(r" +", " ", text)
        no_trailing = re.sub(r" +\n", "\n", no_spacing)
        no_leading = re.sub(r"\n\s+", "\n", no_trailing)
        return no_leading

    expected = """
     Usage: root [OPTIONS] COMMAND [ARGS]...

     tsusiat: project timeline scheduling.

    ╭─ Options ────────────────────────────────────────────────────────────────────╮
    │ --version  -V        Show version and exit.                                │
    │ --help               Show this message and exit.                           │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    """

    output = _normalize(result.output)
    expected = _normalize(expected)
    assert output == expected


def test_version_flag() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0

    expected = f"tsusiat {pkg_version('tsusiat')}\n"
    assert result.stdout == expected
