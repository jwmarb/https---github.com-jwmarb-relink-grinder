VENV=env
PYTHON=$(VENV)/Scripts/python
PIP=$(VENV)/Scripts/pip
PY_CACHE=src/__pycache__ $(wildcard src/*/__pycache__)

TEST_FILES=$(wildcard src/tests/*.py)

# src/tests/test_file.py -> tests/test_file.py -> tests.test_file.py
TESTS=$(patsubst %.py,%, $(patsubst tests/%,tests.%,$(patsubst src/%, %,$(TEST_FILES))))

# Invoked if does not exist
env/Scripts/activate: requirements.txt
	python -m venv env
	./$(PIP) install -r requirements.txt

run: env/Scripts/activate
	cd src && ../$(PYTHON) main.py

clean:
	rm -rf $(PY_CACHE)

setup: requirements.txt
	$(PIP) install -r requirements.txt

test:
	$(foreach file, $(TESTS), cd src && ../$(PYTHON) -m $(file) && cd ..;)