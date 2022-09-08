#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'messy',
]

test_requirements = []

setup(
    author="Hidayat Trimarsanto",
    author_email='trimarsanto@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="MESSy panel-sequencing extension",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='messy panel-sequencing',
    name='messy-panelseq',
    packages=find_packages(include=['messy_panelseq', 'messy_panelseq.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/vivaxgen/messy-panelseq',
    version='0.1.0',
    zip_safe=False,
)
