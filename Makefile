ci: deps test

deps:
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests

.PHONY: ci deps test
