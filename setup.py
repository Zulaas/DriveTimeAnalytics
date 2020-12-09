# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='analyzes drive time for continous miner',
    long_description=readme,
    author='Jan Zimmermann',
    author_email='jan@ueberruhr.de',
    url='https://github.com/Zulaas/DriveTimeAnalytics',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)