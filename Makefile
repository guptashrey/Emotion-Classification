install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py
	black tests/*.py

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv --cov=emoclassify tests/test_emoclassify.py

all: install format lint test