#!/usr/bin/env python
from setuptools import setup, find_packages


METADATA = dict(
    name='django-documentation',
    version='1.0',

    author='Nicolas Patry',
    author_email='nicolas@kwyk.fr',

    description="""Provides a way to integrate a protected sphinx based
    documentation within your django app.""",
    long_description=open('README.rst').read(),

    url='http://github.com/Narsil/django-documentation',
    download_url='http://github.com/Narsil/django-documentation',

    install_requires=['Sphinx>=1.0.7', ],

    include_package_data=True,

    packages=find_packages(),

    keywords='django documentation sphinx authentification',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public \
License (LGPL)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

if __name__ == '__main__':
    setup(**METADATA)
