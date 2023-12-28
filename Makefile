usage:
	@echo "...Scriptum..."
	@echo "* test | cover | dist | clean"

test:
	nose2 -v -s unit_tests

cover:
	coverage run -m nose2 -v unit_tests
	coverage report -m --fail-under=95 --include=scriptum/*
	coverage html --include=scriptum/*
	coverage xml --include=scriptum/*

dist:
	python setup.py egg_info --tag-build=.$(shell date +%Y%m%d%H%M%S) sdist

clean:
	rm -rf cover coverage.xml .coverage
	rm -rf dist
	find . -name "*.pyc" -exec rm {} \;


.PHONY: test cover dist clean
