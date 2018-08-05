#!/usr/bin/env python

import setuptools

with open('requirements.txt') as f:
    required = f.readlines()

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='ipahttp',
    version='0.1',
    author='Andreas Calminder',
    author_email='andreas.calminder@nordnet.se',
    url='https://github.com/nordnet/python-freeipa-json',
    description='Lightweight FreeIPA json/rpc library',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=required,
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ),
)
