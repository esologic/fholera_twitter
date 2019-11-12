"""Use this file to install fholera_twitter as a module"""

from distutils.core import setup
from typing import List


def prod_dependencies() -> List[str]:
    """
    Pull the dependencies from the requirements dir
    :return: Each of the newlines, strings of the dependencies
    """
    with open("./requirements/prod.txt", "r") as file:
        return file.read().splitlines()


setup(
    name="fholera_twitter",
    version="0.1.0",
    description="Follow the followers of a given twitter account or accounts.",
    author="Devon Bray",
    author_email="dev@esologic.com",
    package_dir={"fholera_twitter": "./src"},
    packages=["fholera_twitter"],
    install_requires=prod_dependencies(),
)
