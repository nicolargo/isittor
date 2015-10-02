#!/usr/bin/env python

from setuptools import setup

data_files = [
    ('share/doc/isittor', ['AUTHORS', 'README.md'])
]

def get_requires():
    requires = ['requests>=2.7.0']
    return requires

setup(
    name='isittor',
    version='1.0',
    description="Check if the given <IPaddress> is a Tor exit node.",
    long_description=open('README.md').read(),
    author='Nicolas Hennion',
    author_email='nicolas@nicolargo.com',
    url='https://github.com/nicolargo/isittor',
    license="MIT",
    keywords="cli tor",
    install_requires=get_requires(),
    packages=['isittor'],
    include_package_data=True,
    data_files=data_files,
    entry_points={"console_scripts": ["isittor=isittor:main"]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities'
    ]
)
