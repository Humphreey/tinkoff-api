#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="tinkoff-api",
    version="0.1.1",
    description="Tinkoff API",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha",
    ],
    license="Apache License, Version 2.0",
    author="Alexander Tikhonov",
    author_email="random.gauss@gmail.com",
    url='https://github.com/Fatal1ty/tinkoff-api',
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.6",
    install_requires=[
        "aiohttp>=3.6.2,<3.7",
        "yarl>=1.4.2,<1.5",
        "mashumaro>=1.12,<2.0",
        "ciso8601==2.1.2",
    ]
)
