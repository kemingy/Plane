install:
	pip install -e .

test:
	py.test

doc:
	cd docs && make html

package:
	python setup.py sdist bdist_wheel

.PHONY: install test doc package