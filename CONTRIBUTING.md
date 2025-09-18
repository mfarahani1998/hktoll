# Contributing to hktoll

Thanks for considering a contribution! This project welcomes issues and PRs.

## Development setup

```bash
# 1) Clone
git clone https://github.com/yourname/hktoll.git
cd hktoll

# 2) Create a virtualenv (Python 3.9+)
python3 -m venv .venv
source .venv/bin/activate

# 3) Install in editable mode with dev extras
pip install -U pip
pip install -e ".[dev]"
```

## Running tests and linters

```bash
make test
make lint
make format
```

## Submitting a PR

- Fork the repo, create a feature branch.
- Add/adjust tests to cover your changes.
- Run `make test` and ensure CI passes.
- Open a PR with a clear description and reference any issues.
