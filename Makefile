install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 ./python_automata

check: test lint


.PHONY: test
