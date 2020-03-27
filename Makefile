ci: deps test package install

deps:
	pip install -r requirements.txt
	pip3 install -r requirements.txt

test:
	python -m unittest discover -s tests

coverage:
	coverage run --source=./AocAwsHelper -m unittest discover
	coverage report

package:
	python3 AocAwsHelper/setup.py sdist bdist_wheel

install:
	pip3 install dist/AocAwsHelper-0.0.4-py3-none-any.whl

.PHONY: ci deps test coverage package install
