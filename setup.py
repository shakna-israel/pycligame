#!/usr/bin/env python

from distutils.core import setup

with open("README.md") as file:
    long_description = file.read()

setup(name='pycligame',
      version='0.0.1',
      description='A collection of tools to make generating games easier in Python',
      long_description=long_description,
      author='James Milne',
      author_email='jmilne@graphic-designer.com',
      url='https://github.com/shakna-israel/pycligame',
      packages=['pycligame']
)
