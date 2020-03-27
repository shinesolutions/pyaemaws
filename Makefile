ci: deps test package install

deps:
	pip install -r requirements.txt
	pip3 install -r requirements.txt

test:
	python -m unittest discover -s tests

coverage:
	coverage run --source=./pyaemaws -m unittest discover
	coverage report

package:
	python3 pyaemaws/setup.py sdist bdist_wheel

install:
	pip3 install dist/pyaemaws-0.0.4-py3-none-any.whl

.PHONY: ci deps test coverage package install
