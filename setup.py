from setuptools import find_packages
from setuptools import setup

setup(
    name='pre_commit_hooks',
    description="Java hooks for pre-commit.",
    version='1.0',

    packages=find_packages('.'),

    entry_points={
        'console_scripts': [
            'eclipse-formatter = pre_commit_hooks.eclipse_formatter:main'
        ],
    },
)
