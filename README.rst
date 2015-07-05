**********************************
cookiecutter-automate-ext-template
**********************************

`cookiecutter <http://cookiecutter.readthedocs.org/>`_ template for a
`Automate <http://github.com/tuomas2/automate/>`_ extension.

The template sets up a project with:

- a readme explaining how to install and configure the extension,
- a license file with the LICENCE.txt,
- a Python module with an empty Automate extension,
- an empty test suite that can be executed with ``py.test``,
- a ``setup.py`` file for releasing and installing the extension as a Python
  package.


Usage
=====

#. Install `cookiecutter` 1.0.0 or newer::

       pip install cookiecutter

#. Generate a Automate extension project::

       cookiecutter https://github.com/tuomas2/cookiecutter-automate-ext-template.git

#. Create a Git repo from the generated project.

#. Make your Automate extension do something.

#. Release the extension to `PyPI <https://pypi.python.org/>`_.


Further reading
===============

To learn more about creating Automate extensions, please read the docs on
`extension development <http://tuomasairaksinen.fi/automate/docs/extensions.html>`_.