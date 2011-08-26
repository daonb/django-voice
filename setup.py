# -*- coding: utf-8 -*-

import sys
import djangovoice
from setuptools import find_packages
from setuptools import setup

readme_file = 'README.rst'
try:
    long_description = file(readme_file).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(
    name='django-voice',
    version=djangovoice.get_version(),
    description="A feedback application for Django 1.3 or later",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django,feedback,discussion',
    author='Gökmen Görgen',
    author_email='gokmen@alageek.com',
    url='https://github.com/alageek/django-voice',
    download_url='https://github.com/alageek/django-voice/downloads',
    license='BSD',
    packages=find_packages(exclude=('demo', 'demo.*')),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)