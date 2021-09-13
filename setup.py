


from setuptools import find_packages, setup

PACKAGE_NAME = "KeyPass"

setup(
    name=PACKAGE_NAME,
    author="Bryce Boe",
    author_email="",
    python_requires="~=3.6",
    description=(
        "PRAW, an acronym for Python Reddit API Wrapper, is a python package that"
        " allows for simple access to reddit's API."
    ),

    #package_data={"": ["LICENSE.txt"], PACKAGE_NAME: ["*.ini", "images/*.jpg"]},
    #packages=find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),
    packages=find_packages(),
    version=1,
)