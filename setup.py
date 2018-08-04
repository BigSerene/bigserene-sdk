#!/usr/bin/env python
from setuptools import setup

setup(
    name="bigserene_sdk",
    version="0.1",
    description="Bigserene SDK to access Bigserene App Platform",
    author="Chris Lee",
    author_email="chrisl@bigseren.com",
    packages=["bigserene_sdk"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
)
