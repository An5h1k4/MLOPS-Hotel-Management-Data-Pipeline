from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines() # whatever f will read from requirements.txt will get stored under requirements variable

setup(
    name = "MLOPS-Project-1",
    version = "0.1",
    author = "Anshika",
    packages = find_packages(),
    install_requires = requirements,
)