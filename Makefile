install:
	poetry install
lint:
	poetry run flake8 brain_games --use-flake8-tabs
