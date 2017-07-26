========
Trivia 1
========

Configuring Tox
===============

`Tox <http://tox.readthedocs.org>`_ is a system for testing in different environments (eg py27 and py34) that uses virtual environments
to create clean tesing environments with specified software installed. It allows you to test that your
package installs and runs correctly. It coordinates with different testing software including nose and `pytest <http://pytest.org>`_.

The first step to use tox is to create a *tox.ini* file::

   # content of: tox.ini , put in same dir as setup.py
   [tox]
   envlist = py26,py27
   [testenv]
   deps=
       pytest       # install pytest in the venvs
       #-rrequirements.txt	# uncomment to also install packages in requirements.txt
   commands=py.test  # or 'nosetests' or ...
   changedir=test/directory	# run tests in this directory rather than at the top level
   sitepackages=True		# use globally installed packages

Then from a terminal in the top level package directory run the command::

   tox

This will create virtual environments, load package dependencies, install the package and run all tests. In my hands on windows, tox doesn't work well with dependencies like numpy since it cannot be pip installed. My solution was to set sitepackages to True to use the globally installed packages.

More suggestions about how to use tools for open source development from `here <http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/>`_.

Here is a series of `blog posts about testing and code coverage <http://ilovesymposia.com/2014/10/27/continuous-integration-in-python-7-some-helper-tools-and-final-thoughts/>`_.
