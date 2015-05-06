#!/usr/bin/env python
"""setup.py."""

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://rxns.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


requires = ['click',
            'munch',
            'pubchempy',
            'pandas',
            'pyyaml',
            ]

setup(
    name='rxns',
    version='0.1.0',
    description='Help plan molecular biology reaction sets including stock solutions and master mixes that your '
                'target reactions depend on.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Gus Dunn',
    author_email='gus.dunn@yale.edu',
    url='https://github.com/xguse/rxns',
    packages=[
        'rxns',
    ],
    package_dir={'rxns': 'rxns'},
    entry_points={
        'console_scripts': [
            'react = rxns.rxns:cli',
            ]
        },
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    keywords='rxns',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
