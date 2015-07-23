# -*- coding: utf-8 -*-
"""
Created on:    Nov 1, 2013
@author:        vahid
"""

from setuptools import setup, find_packages
import os.path
import re

# reading isass version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'rtl', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

long_description = """
RTL Reshaper
"""

setup(
    name='rtl',
    version=package_version,
    author='Vahid Mardani',
    author_email='vahid.mardani@gmail.com',
    description='Python Right-To_left text reshaper, plus cli',
    long_description=long_description,
    license='MIT',
    install_requires=['python-bidi'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rtl = rtl:main'
        ]
    },
    test_suite = "rtl.tests",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        ],
    )