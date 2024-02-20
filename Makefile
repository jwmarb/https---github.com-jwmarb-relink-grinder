VENV=env
PYTHON=$(VENV)/Scripts/python
PIP=$(VENV)/Scripts/pip
PY_CACHE=src/__pycache__ $(wildcard src/*/__pycache__)
CWD=$(shell pwd)
LINT_BUILD_FLAGS=--count --select=E9,F63,F7,F82 --show-source --statistics
LINT_ERROR_FLAGS=--count --exit-zero --max-complexity=10 --max-line-length=79 --statistics

TEST_FILES=$(wildcard src/tests/*.py)

# src/tests/test_file.py -> tests/test_file.py -> tests.test_file.py
TESTS=$(patsubst %.py,%, $(patsubst tests/%,tests.%,$(patsubst src/%, %,$(TEST_FILES))))

# Invoked if does not exist
env/Scripts/activate: requirements.txt
	rm -rf $(VENV)
	python -m venv env
	./$(PIP) install -r requirements.txt

run: env/Scripts/activate
	cd src && ../$(PYTHON) $(main).py

clean:
	rm -rf $(PY_CACHE)

setup: requirements.txt
	$(PIP) install -r requirements.txt

test:
	cd src && $(foreach file, $(TESTS),$(CWD)/$(PYTHON) -m $(file);)

lint:
	black ./src --line-length 79
	flake8 ./src $(LINT_BUILD_FLAGS)
	flake8 ./src $(LINT_ERROR_FLAGS)