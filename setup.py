# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
        install_requires = f.read().strip().split('\n')


from gad import __version__ as version

setup(
        name='gad',
        version=version,
        description='gad',
        author='ahmed',
        author_email='ahmedgadallah1899@gmail.com',
        packages=find_packages(),
        zip_safe=False,
        include_package_data=True,
        install_requires=install_requires
)

