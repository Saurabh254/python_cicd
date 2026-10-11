# Python CI/CD Pipeline Reference

A minimal reference repository demonstrating continuous integration and automated code quality workflows for Python projects using GitHub Actions.

> [!NOTE]
> Created for educational and personal learning purposes.

---

## Workflows Included

The repository demonstrates a multi-stage GitHub Actions CI setup in `.github/workflows/`:

- **🧪 Unit Testing (`pull_request.yml`)**: Automated test execution using `pytest` on pull requests.
- **🔍 Static Analysis (`pylint.yml`)**: Code analysis and style enforcement via `pylint`.
- **📐 Type Checking (`mypy.yaml`)**: Static typing validation using `mypy`.
- **📦 Import Formatting (`isort.yaml`)**: Verifies PEP 8 compliant import ordering using `isort`.

---

## Project Structure

```
.
├── .github/workflows/
│   ├── isort.yaml          # Import sorting check
│   ├── mypy.yaml           # Type check action
│   ├── pull_request.yml    # Pytest execution on PRs
│   └── pylint.yml          # Linter pipeline
├── main.py                 # Core application module
└── test_main.py            # Pytest test suite
```

---

## Running Locally

To run the checks locally:

```bash
# Install dependencies
pip install pytest pylint mypy isort

# Run tests
pytest

# Run linter & type checker
pylint main.py
mypy main.py
isort --check --diff main.py
```

---

## License

Educational / Personal Use.
