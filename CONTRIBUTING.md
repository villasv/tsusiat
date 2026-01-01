# Contributing

## Setup

This project uses **Hatch** for environments and publishing.

- Install Hatch (if you haven't):
  - `pipx install hatch`

- Create the default env (first time):
  - `hatch env create`

## Running

- Run a command inside the default env:
  - `hatch run python -c "import tsusiat; print('ok')"`

## Quality

- Lint:
  - `hatch run ruff check .`

- Format:
  - `hatch run ruff format .`

## Tests

- Run tests with coverage:
  - `hatch run pytest -q --cov=tsusiat --cov-report=term-missing`

## Builds

- Build sdist + wheel:
  - `hatch build`

## Publishing

- Publish to PyPI:
  - `hatch publish`
