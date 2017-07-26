============
Git Trivia 1
============

The best place to start learning about how to use git is the `Atlassian tutorial <https://www.atlassian.com/git/tutorials/>`_. More detailed instructions can be found `here <http://git-scm.com/documentation>`_ and `here
<http://git-scm.com/book/en/v2>`_

After that, the next helpful trick is to use `pyscaffold <http://pyscaffold.readthedocs.org/en/latest/features.html>`_ to set up your respository. This creates a lot of boilerplate including a gitignore file and a setup.py file that can run pytest, choose a license and configure for tox and Travis::

  putup my_project --license bsd --with-tox --with-travis

An existing project created with pyscaffold can be updated to the latest version with::

   putup --update my_project

An existing project not created with pyscaffold can be updated to use it with::

   putup --force my_project

.. warning::
   Remember to commit all of your changes prior to doing this, just in case!!!

Once your project is created, you can create a corresponding respository on github or bitbucket and upload the project
