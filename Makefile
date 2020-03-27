ci: clean deps test coverage package install

clean:
	rm -rf *.egg-info build dist pyaemaws/_pycache_/ pyaemaws/*.pyc tests/_pycache_/ tests/*.pyc .coverage

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

release:
	rtk release

.PHONY: ci clean deps test coverage package install release
