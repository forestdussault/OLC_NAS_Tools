#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="OLC_NAS_Tools",
    version="0.1",  # version must be incremented manually each time
    packages=find_packages(),
    author="Forest Dussault",
    author_email="forest.dussault@inspection.gc.ca",
    url="https://github.com/forestdussault/OLC_NAS_Tools",  # link to the repo
    scripts=['nastools.py'],
)