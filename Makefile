PYTHON = python3
SRC_DIR = .
TEST_DIR = ./tests
TEST_FILES = $(wildcard $(TEST_DIR)/*.py)

test:
	$(PYTHON) -m pytest $(TEST_FILES)

format:
	isort $(SRC_DIR) $(TEST_DIR)
	black $(SRC_DIR) $(TEST_DIR)

check-format:
	black --check $(SRC_DIR) $(TEST_DIR)
	isort --check-only $(SRC_DIR) $(TEST_DIR)
	poetry run flake8 . --extend-exclude=dist,build --show-source --statistics
	poetry run pylint $(SRC_DIR) $(TEST_DIR)
