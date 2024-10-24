from pathlib import Path
import sys

from scripts.boilerplate.readme import readme_template

INIT_FILE = "__init__.py"
TESTS_FOLDER = "tests"
SOURCE_FOLDER = "src"


def create_package_structure(package_name):
    package_dir = Path.cwd() / package_name
    src_dir = package_dir / SOURCE_FOLDER
    tests_dir = package_dir / TESTS_FOLDER

    _create_root(package_dir, package_name)
    _create_source(src_dir)
    _create_tests(tests_dir)
    _create_readme(package_dir)


def _create_readme(package_dir):
    (package_dir / "README.md").write_text(readme_template(package_name))


def _create_tests(tests_dir):
    tests_dir.mkdir(exist_ok=True)
    (tests_dir / INIT_FILE).write_text("# tests initialization")


def _create_source(src_dir):
    src_dir.mkdir(exist_ok=True)
    (src_dir / INIT_FILE).write_text("# src initialization")


def _create_root(package_dir, package_name):
    package_dir.mkdir(exist_ok=True)
    (package_dir / INIT_FILE).write_text(f"# {package_name} package")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: create_module.py <package_name>")
        sys.exit(1)

    package_name = sys.argv[1]
    create_package_structure(package_name)