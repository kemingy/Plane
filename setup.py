from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="plane",
    version="0.2.1",
    description="A lib for text preprocessing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Keming Yang",
    author_email="kemingy94@gmail.com",
    license="MIT",
    classifiers=[
        "Topic :: Text Processing",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6",
            "flake8>=3.8",
            "black>=20.8b1",
            "isort>=5.6",
            "autoflake>=1.4",
        ],
    },
    python_requires=">=3",
    packages=find_packages(exclude=["test"]),
    url="https://github.com/kemingy/Plane",
)
