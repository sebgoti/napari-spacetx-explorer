#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


install_deps = ['napari',
                'napari-plugin-engine>=0.1.4',
                'imagecodecs']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='napari-spacetx-explorer',
    author='Sebastian Gonzalez-Tirado',
    author_email='sebastian.gonzalez@embl.de',
    license='BSD-3',
    url='https://github.com/sebgoti/napari-spacetx-explorer',
    description='visualizer for spatial omic data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    use_scm_version=True,
    install_requires=install_deps,
    setup_requires=['setuptools_scm', 'pytest-runner'],
    tests_require=['pytest', 'pytest-qt'],
    extras_require={
      "docs": [
        'sphinx>=3.0',
        'sphinxcontrib-apidoc',
        'sphinx_rtd_theme',
        'sphinx-prompt',
        'sphinx-autodoc-typehints',
      ]
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Framework :: napari',
    ],
    entry_points={
        'napari.plugin': [
            'napari-spacetx-explorer = napari_spacetx_explorer',
        ],
    },
)