# Polynomial Arithmetic Backend
Modular back-end for polynomial arithmetic in  𝐺 𝐹 ( 2 𝑚 ) GF(2  m  ) fields, supporting operations like addition, subtraction, multiplication, division, modulo reduction, and inversion. Designed for flexibility with field sizes like  𝑚 = 163 , 233 , 409. Accepts binary/hex input, fully documented, and tested for accuracy.

## Setup the environment

1. Install Python 3.12 or higher
2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

```bash
source .venv/bin/activate # For macos
.venv\Scripts\activate # For windows
```

4. Install the required packages

```bash
pip install -r requirements.txt
```

## Some Commands

### Run backend server

Run the fastapi backend server

```bash
python cli.py run
```

### Clean the code (necessary before creating a pull request)

Clean up the code

```bash
python cli.py clean
```

### Generate empty test files

Generate empty test files in the `tests` and `tests/fixtures` directories for all the files in the `src` directory.

```bash
python cli.py generate-test-files
```

### Import fixtures to `conftest.py`

This command imports all the fixtures in the `tests/fixtures` directory to the `conftest.py` file.

```bash
python cli.py import-fixtures
```

### Run tests

This command runs all the tests in the `tests` directory.

```bash
python cli.py run-tests
```

### Clean unused tests and fixtures

This command deletes all the test files in the `tests` and `tests/fixtures` directories that empty.

```bash
python cli.py clean-unused-tests
```

### Run pre-stage command

This command runs the `import-fixtures`, `clean` and `run-tests` commands in this order.

```bash
python cli.py pre-stage
```

## Contributors

- [Rayan Fakhreddine](https://github.com/Rayan28461)
- [Karl Gerges](https://github.com/Karl-67)