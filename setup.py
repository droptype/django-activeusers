#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os
import activeusers

setup(
    name='django-activeusers',
    version=activeusers.get_version(),
    description="Just active-visitor tracking for Django",
    long_description=open('README.rst', 'r').read(),
    keywords='django, active, visitors, users, tracking',
    author='Alvin Savoy',
    author_email='none',
    url='http://github.com/asavoy/django-activeusers',
    license='MIT',
    package_dir={'activeusers': 'activeusers'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)
