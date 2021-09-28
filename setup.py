#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


install_deps = ['napari',
                'napari-plugin-engine>=0.1.4',
                'numpy',
                'pandas']

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
    python_requires='>=3.7',
    use_scm_version=True,
    install_requires=install_deps,
    setup_requires=['setuptools_scm', 'pytest-runner'],
    tests_require=['pytest', 'pytest-qt'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Science/Research',
        'Framework :: napari',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'napari.plugin': [
            'napari-spacetx-explorer = napari_spacetx_explorer',
        ],
    },
)
