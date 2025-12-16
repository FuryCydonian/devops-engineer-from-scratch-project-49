install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff format brain_games

test:
	uv run pytest -s

build-install:
	make build
	make package-reinstall