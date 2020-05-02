#!/usr/bin/env python
from setuptools import setup

setup(
    name="bigserene_sdk",
    version="0.2",
    description="Bigserene SDK to access Bigserene App Platform",
    author="Chris Lee",
    author_email="chrisl@bigserene.com",
    packages=["bigserene_sdk", "bscli"],
    install_requires=["click==7.0", "pytz==2020.1", "requests==2.21.0", "tqdm==4.45.0"],
    extras_require={"test": ["pytest==4.0.0"]},
    scripts=["bin/bscli"],
)
