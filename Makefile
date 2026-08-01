PROJECT_DIR    ?= svmodule
TESTS_DIR      ?= tests

# Packaging and publication are handled by .github/workflows/release.yml,
# which builds on a tag and publishes to TestPyPI then PyPI over OIDC
# trusted publishing. The former upload-pypi / upload-pypi-test /
# install-pypy-test / dist-check targets duplicated that with token
# authentication and have been removed.

.PHONY: ruff ruff-fix ruff-format pytest dist clean


ruff:
	uv run ruff check $(PROJECT_DIR) $(TESTS_DIR)

ruff-fix:
	uv run ruff check --fix --unsafe-fixes $(PROJECT_DIR) $(TESTS_DIR)

ruff-format:
	uv run ruff format $(PROJECT_DIR) $(TESTS_DIR)

pytest:
	uv run pytest

# Local build check before tagging; the release itself is built by the CI.
dist:
	uv build

clean:
	rm -rf test_*.dot test_*.tcl tests.xml coverage.xml htmlcov
	rm -rf build dist $(PROJECT_DIR).egg-info .venv
