__author__ = 'John Wang'

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.1',
    packages=['polls'],
    include_package_data=True,
    license='BSD license',
    description='A simple django app to conduct web-based polls',
    long_description=README,
    url='http://www.wzjg520.com/',
    author='john wang',
    author_email='wzjg520@126.com',
    classifiers=[]
)
