#!/usr/bin/env python3

from setuptools import setup
from pathlib import Path


reqs_path = Path(__file__).parent / 'requirements.txt'
reqs = reqs_path.read_text().splitlines()


setup(
    name='tst',
    version='0.0.1',
    description='Test python snap',
    packages=['tst'],
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'tst = tst:main',
            'tst-sub = tst:sub',
        ],
    },
)
