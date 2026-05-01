PROJECT_DIR    ?= svmodule
TESTS_DIR      ?= tests


ruff:
	uv run ruff check $(PROJECT_DIR) $(TESTS_DIR)

ruff-fix:
	uv run ruff check --fix --unsafe-fixes $(PROJECT_DIR) $(TESTS_DIR)

ruff-format:
	uv run ruff format $(PROJECT_DIR) $(TESTS_DIR)

pytest:
	uv run pytest
	sed -i 's/></>\n</g' tests.xml

upload-pypi: dist-check
	uv run twine upload -u __token__ -p $$PYPI_TOKEN dist/*
	touch $@

install-pypy-test: upload-pypi-test
	rm -rf venv-test-install
	uv venv venv-test-install
	uv run --python venv-test-install pip \
	    install --index-url https://test.pypi.org/simple/ --no-deps $(PROJECT_DIR)
	touch $@

upload-pypi-test: dist-check
	uv run twine upload --verbose -u __token__ -p $$PYPI_TEST_TOKEN \
	    --repository-url https://test.pypi.org/legacy/ dist/*
	touch $@

dist-check: dist
	uv run twine check dist/*
	touch $@

dist:
	uv build

clean:
	rm -rf test_*.dot test_*.tcl tests.xml coverage.xml htmlcov
	rm -rf dist-check upload-pypi upload-pypi-test install-pypy-test
	rm -rf venv-test-install .venv
	rm -rf dist $(PROJECT_DIR).egg-info
