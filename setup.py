from setuptools import find_packages, setup
from typing import List

r = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Returns list of requirements"""
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if r in requirements:
        requirements.remove(r)

    return requirements


setup(
    name="OCR",
    version="0.0.1",
    packages=find_packages(),
    install_require=get_requirements("requirements.txt"),
)
