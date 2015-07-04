#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements
import re

install_reqs = parse_requirements('requirements.pip')
def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']

setupopts = dict(
    name="{{ cookiecutter.dist_name }}",
    version=get_version('automate_{{ cookiecutter.ext_name }}/__init__.py'),
    packages=find_packages(),

    install_requires=[str(ir.req) for ir in install_reqs],

    # metadata for upload to PyPI
    author="{{ cookiecutter.author_full_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.short_description }}",
    long_description=open('README.rst').read(),
    license="",
    url="http://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.dist_name|lower }}",
    entry_points={'automate.extension': [
            '{{ cookiecutter.ext_name }} = automate_{{cookiecutter.ext_name }}:extension_classes'
    ]},

    classifiers=["Development Status :: 4 - Beta",
                 "Environment :: Console",
                 "Environment :: X11 Applications :: Qt",
                 "Environment :: Win32 (MS Windows)",
                 "Environment :: Web Environment",
                 "Intended Audience :: Education",
                 "Intended Audience :: End Users/Desktop",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Information Technology",
                 "License :: Free for non-commercial use",
                 "Operating System :: Microsoft :: Windows",
                 "Operating System :: POSIX",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: Scientific/Engineering",
                 "Topic :: Software Development",
                 "Topic :: Software Development :: Libraries"]
)

if __name__ == "__main__":
    setup(**setupopts)
