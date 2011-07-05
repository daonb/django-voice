# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1'

LONG_DESCRIPTION = """
============
Django Voice
============

This application lets you solicit feedback and suggestions from
your users, who can then vote and comment on other suggestions.
"""

setup(
    name='django-voice',
    version=version,
    description="django-voice",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django,feedback,discussion',
    author='Gökmen Görgen',
    author_email='gokmen@alageek.com',
    url='https://github.com/gkmngrgn/django-voice',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

