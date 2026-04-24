PROJECT_DIR    ?= svmodule
TESTS_DIR      ?= tests


ruff: venv3
	source venv3/bin/activate && ruff check $(PROJECT_DIR) $(TESTS_DIR)

ruff-fix: venv3
	source venv3/bin/activate && ruff check --fix $(PROJECT_DIR) $(TESTS_DIR)

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
	source venv3/bin/activate && python3 -m build

venv3:
	python3 -m venv venv3
	source venv3/bin/activate && pip install --upgrade pip
	source venv3/bin/activate && \
	    pip install build twine ruff pytest pytest-cov python-lsp-server

clean:
	rm -rf test_*.dot test_*.tcl tests.xml coverage.xml htmlcov
	rm -rf install-test upload-test upload-prod dist-check
	rm -rf venv3 venv3-test-install
	rm -rf dist $(PROJECT_DIR).egg-info
