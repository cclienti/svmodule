PROJECT_DIR    ?= svmodule
TESTS_DIR      ?= tests
PYLINT_SCORE   ?= 8.9


flake8: venv3
	source venv3/bin/activate && flake8 $(PROJECT_DIR) $(TESTS_DIR)

pylint: venv3
	source venv3/bin/activate && \
	    pylint-fail-under --fail_under $(PYLINT_SCORE) $(PROJECT_DIR) $(TESTS_DIR)

pytest: venv3
	source venv3/bin/activate && $@
	sed -i 's/></>\n</g' tests.xml

upload-pypi: install-pypy-test
	source venv3/bin/activate && twine upload -u $$PYPI_PROD_USER -p $$PYPI_PROD_PASSWORD dist/*
	touch $@

install-pypy-test: upload-pypi-test
	rm -rf venv3-test-install
	python3 -m venv venv3-test-install
	source venv3-test-install/bin/activate && pip \
	    install --index-url https://test.pypi.org/simple/ --no-deps $(PROJECT_DIR)
	touch $@

upload-pypi-test: dist-check
	source venv3/bin/activate && \
	    twine upload --verbose -u $$PYPI_TEST_USER -p $$PYPI_TEST_PASSWORD \
	    --repository-url https://test.pypi.org/legacy/ dist/*
	touch $@

dist-check: dist
	source venv3/bin/activate && twine check dist/*
	touch $@

dist: venv3
	source venv3/bin/activate && python3 setup.py sdist bdist_wheel

venv3:
	python3 -m venv venv3
	source venv3/bin/activate && pip install --upgrade pip
	source venv3/bin/activate && \
	    pip install wheel flake8 pylint twine pytest pytest-cov pylint-fail-under

clean:
	rm -rf test_*.dot test_*.tcl tests.xml coverage.xml htmlcov
	rm -rf install-test upload-test upload-prod dist-check
	rm -rf venv3 venv3-test-install
	rm -rf dist $(PROJECT_DIR).egg-info
