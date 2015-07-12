#!/usr/bin/env python

from setuptools import setup, find_packages

def get_version(filename):
    import re
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']

setupopts = dict(
    name="{{ cookiecutter.dist_name }}",
    version=get_version('automate_{{ cookiecutter.ext_name }}/__init__.py'),
    packages=find_packages(),
    install_requires=["automate>=0.9.2,<=0.10"],
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
                 "Intended Audience :: Education",
                 "Intended Audience :: End Users/Desktop",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Information Technology",
                 "License :: Free for non-commercial use",
                 "Operating System :: Microsoft :: Windows",
                 "Operating System :: POSIX",
                 "Operating System :: POSIX :: Linux",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: Scientific/Engineering",
                 "Topic :: Software Development",
                 "Topic :: Software Development :: Libraries"]
)

if __name__ == "__main__":
    setup(**setupopts)
