.PHONY: test lint format build serve

test:
	pytest -q

lint:
	ruff check src

format:
	ruff check --fix src || true

build:
	python -m build

serve:
	python -m hktoll.server
