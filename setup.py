from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='plane',
    version='0.0.1',
    description='A lib for text preprocessing',
    long_description=long_description,
    author='Keming Yang',
    author_email='kemingy94@gmail.com',
    url='',
    license='MIT',
    classifiers=[
        'Topic :: Text Processing',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[],
)