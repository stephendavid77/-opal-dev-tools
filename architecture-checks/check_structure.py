import sys
import os

# A dictionary that defines forbidden files/directories for each module type.
FORBIDDEN_STRUCTURE_ELEMENTS = {
    "application": [
        "static/css",  # Custom CSS directory
        "config.py",  # Custom config file
        "auth.py",  # Custom auth file
        "database.py",  # Custom database file
    ],
    "shared-library": {
        # Shared libraries should not have application-specific files
        "opal-database": [],
        "opal-auth-backend": [],
        "opal-shared-utils": [],
        "opal-global-ui": [],
        "opal-auth-frontend": [],
    },
}

REQUIRED_FILES = {
    "README.md": "Each project must have a README.md file.",
    "gemini.md": "Each project must have a gemini.md file.",
}

# REQUIRED_SCRIPTS dictionary is removed entirely


def get_project_type(project_path):
    # This is a placeholder. In a real scenario, you might infer this from project structure or a config file.
    if "opal-auth-backend" in project_path or "opal-database" in project_path or "opal-shared-utils" in project_path or "opal-global-ui" in project_path or "opal-auth-frontend" in project_path:
        return "shared-library"
    return "application"


def check_structure():
    print("Checking project structure...")
    project_path = os.getcwd()
    project_type = get_project_type(project_path)

    violations = []

    # Check for forbidden files/directories
    for root, dirs, files in os.walk(project_path):
        for forbidden_element in FORBIDDEN_STRUCTURE_ELEMENTS.get(project_type, []):
            full_path = os.path.join(root, forbidden_element)
            if os.path.exists(full_path):
                violations.append(f"Forbidden file/directory found: {full_path}")

    # Check for required files
    for required_file, message in REQUIRED_FILES.items():
        if not os.path.exists(os.path.join(project_path, required_file)):
            violations.append(message)

    # Check for scripts folder (only existence, not content)
    scripts_path = os.path.join(project_path, "scripts")
    if not os.path.exists(scripts_path):
        violations.append("Each project must have a 'scripts' folder.")

    if violations:
        print("Structure check failed:")
        for violation in violations:
            print(f"- {violation}")
        sys.exit(1)
    else:
        print("Structure check passed.")
        sys.exit(0)


if __name__ == "__main__":
    check_structure()