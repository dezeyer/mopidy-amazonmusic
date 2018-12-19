from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='Mopidy-AmazonMusic',
    version=get_version('mopidy_amazonmusic/__init__.py'),
    url='https://github.com/amjadsaadeh/mopidy-amazonmusic',
    license='Apache License, Version 2.0',
    author='Amjad Saadeh',
    author_email='mail@amjadsaadeh.de',
    description='Mopidy extension for Amazon (Prime) Music streaming',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
    ],
    dependency_links=[
        'git+https://github.com/amjadsaadeh/amazonmusic.git',
    ],
    entry_points={
        'mopidy.ext': [
            'amazonmusic = mopidy_amazonmusic:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
