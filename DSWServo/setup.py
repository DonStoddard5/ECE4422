#! /usr/bin/python

from setuptools import setup, find_packages

setup(
    name='DSWServo',
    version='1.0.0',
    description='Python code to control a servo on a Raspberry Pi',
    author='Don Webster',
    author_email='tuj45546@temple.edu',
    packages=find_packages(),
    install_requires=['gpiozero','time']
    )
