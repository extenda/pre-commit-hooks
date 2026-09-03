from setuptools import find_packages
from setuptools import setup

setup(
    name='pre_commit_hooks',
    description="Java hooks for pre-commit.",
    # Informational only. The released version is the git tag created by
    # extenda/actions/conventional-release, which is what consumers pin.
    version='0.17.0',

    packages=find_packages('.'),

    # Holds the google-java-format version the hook downloads.
    package_data={'pre_commit_hooks': ['pom.xml']},

    entry_points={
        'console_scripts': [
            'eclipse-formatter = pre_commit_hooks.eclipse_formatter:main',
            'google-java-formatter = ' +
                'pre_commit_hooks.google_java_formatter:main'
        ],
    },
)
