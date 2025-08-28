# OpalSuite Development Tools (`opal-dev-tools`) :

This repository serves as the central hub for shared development tools and architectural checks across the entire OpalSuite ecosystem. Its primary purpose is to enforce code quality, consistency, and adherence to architectural standards through `pre-commit` hooks.

## Architectural Checks

`opal-dev-tools` provides a suite of Python-based architectural checks designed to maintain the integrity and consistency of the multi-repository OpalSuite structure. These checks are implemented as `pre-commit` hooks and are automatically applied to all projects that integrate with this repository.

The key checks include:

- **`check_dependencies.py`**: Ensures that projects adhere to defined dependency rules, preventing the use of forbidden libraries and promoting the consumption of centralized shared components.
- **`check_imports.py`**: Verifies import statements within Python modules to prevent direct imports of functionalities that should be accessed via shared services.
- **`check_structure.py`**: Enforces a consistent directory structure, ensuring the presence of required files (e.g., `scripts` folder, `README.md`) and preventing the inclusion of forbidden structural elements.

## Pre-commit Integration (Global Hooks)

This repository is designed to be integrated into other OpalSuite projects as a source for global `pre-commit` hooks. By referencing `opal-dev-tools` in a project's `.pre-commit-config.yaml`, that project automatically inherits a comprehensive set of code quality, linting, security, and architectural checks.

### Global Hooks Provided:

- **Code Formatting:** `black`, `isort`, `prettier`
- **Python Linters:** `flake8`, `mypy`
- **Security Scanners:** `bandit`
- **General Checks:** `trailing-whitespace`, `end-of-file-fixer`, `check-yaml`, `check-added-large-files`
- **Architectural Checks:** `check-dependencies`, `check-imports`, `check-structure`
- **Unit Tests:** `pytest` (runs unit tests before commit)
- **JavaScript/TypeScript Linters:** `eslint`

### Usage in Other Projects

To integrate these global hooks into any OpalSuite project:

1.  **Ensure `pre-commit` is installed:**
    ```bash
    pip install pre-commit
    ```
2.  **Update the project's `.pre-commit-config.yaml`:**
    Replace the contents of the project's `.pre-commit-config.yaml` with a reference to `opal-dev-tools` and the desired hooks. A typical configuration will look like this:

    ```yaml
    repos:
      - repo: https://github.com/stephendavid77/opal-dev-tools
        rev: main # Use a specific commit hash or tag for production stability
        hooks:
          - id: trailing-whitespace
          - id: end-of-file-fixer
          - id: check-yaml
          - id: check-added-large-files
          - id: black
          - id: isort
          - id: flake8
          - id: mypy
          - id: bandit
          - id: eslint
          - id: prettier
          - id: check-dependencies
          - id: check-imports
          - id: check-structure
          - id: pytest
    ```

3.  **Install the hooks in the project:**

    ```bash
    pre-commit install
    ```

4.  **Update hooks periodically:**
    To ensure you have the latest versions of the global hooks, run:
    ```bash
    pre-commit autoupdate
    ```

## Local Development

To develop on `opal-dev-tools` itself:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/stephendavid77/opal-dev-tools.git
    cd opal-dev-tools
    ```
2.  **Install dependencies (for running checks locally):**
    ```bash
    pip install -e .
    ```
3.  **Run checks from the command line (for testing purposes):**
    ```bash
    python -m architecture_checks.check_dependencies
    python -m architecture_checks.check_imports
    python -m architecture_checks.check_structure
    ```
