ci: clean deps lint test coverage package install

clean:
	rm -rf *.egg-info build dist pyaemaws/_pycache_/ pyaemaws/*.pyc tests/_pycache_/ tests/*.pyc .coverage

deps:
	pip install --ignore-installed -r requirements.txt
	pip3 install --ignore-installed -r requirements.txt

lint:
	pylint pyaemaws/*.py pyaemaws/*/*.py

test:
	python3 -m unittest discover -s tests

coverage:
	coverage run --source=./pyaemaws -m unittest discover
	# Generate the HTML report regardless of coverage
	coverage html
	# Fail the build if coverage is less than 100%
	coverage report --fail-under=100

package:
	python3 setup.py sdist bdist_wheel

install:
	pip3 install dist/pyaemaws-`yq -r .version conf/info.yaml`-py3-none-any.whl

release:
	rtk release

publish:
	python3 setup.py sdist

publish-test:
	python3 setup.py register -r pypitest && \
		python3 setup.py sdist upload -r pypitest

.PHONY: ci clean deps lint test coverage package install release publish publish-test
