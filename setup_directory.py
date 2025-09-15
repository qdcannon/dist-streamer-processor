import os
import sys
from textwrap import dedent


def create_project(project_name: str):
    base_dir = os.path.abspath(project_name)

    # Create standard dirs
    src_dir = os.path.join(base_dir, "src", project_name)
    tests_dir = os.path.join(base_dir, "tests")

    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(tests_dir, exist_ok=True)

    # ----------------
    # Package files
    # ----------------
    with open(os.path.join(src_dir, "__init__.py"), "w") as f:
        f.write("")

    # Example module
    with open(os.path.join(src_dir, "example.py"), "w") as f:
        f.write(dedent("""\
        def hello():
            return "Hello, world!"
        """))

    # ----------------
    # Project root files
    # ----------------
    with open(os.path.join(base_dir, "README.md"), "w") as f:
        f.write(f"# {project_name}\n\nProject description here.\n")

    with open(os.path.join(base_dir, "pyproject.toml"), "w") as f:
        f.write(dedent(f"""\
        [build-system]
        requires = ["setuptools>=42"]
        build-backend = "setuptools.build_meta"

        [project]
        name = "{project_name}"
        version = "0.1.0"
        description = "My awesome Python project"
        authors = [{{ name = "Your Name", email = "you@example.com" }}]
        dependencies = []
        """))

    with open(os.path.join(base_dir, "setup.cfg"), "w") as f:
        f.write(dedent(f"""\
        [metadata]
        name = {project_name}
        version = 0.1.0

        [options]
        packages = find:
        package_dir =
            =src
        python_requires = >=3.8

        [options.packages.find]
        where = src
        """))

    # ----------------
    # Tests
    # ----------------
    with open(os.path.join(tests_dir, "__init__.py"), "w") as f:
        f.write("")

    with open(os.path.join(tests_dir, "test_example.py"), "w") as f:
        f.write(dedent(f"""\
        from {project_name}.example import hello

        def test_hello():
            assert hello() == "Hello, world!"
        """))

    print(f"✅ Project '{project_name}' created at: {base_dir}")
    print("\nNext steps:")
    print(f"  cd {project_name}")
    print("  pip install -e .")
    print("  pytest tests/")
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python setup_project.py <project_name>")
    else:
        create_project(sys.argv[1])
