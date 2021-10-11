from setuptools import find_packages, setup
from db_cicd_github_demo import __version__

setup(
    name="db_cicd_github_demo",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Databricks Labs CICD Templates Sample Project",
    author="",
)
