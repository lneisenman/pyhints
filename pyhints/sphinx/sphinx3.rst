==============================
Using Sphinx with Github Pages
==============================

Sphinx can be used to generate static web sites like this one to be hosted on
Github by putting the html output into a branch called gh-pages. Start by
creating a project with a readme file, a license file and a directory containing
the source code for your sphinx (or other static) website. These will be stored
in the master branch of your github repo. After you build the website you can
use the `ghp-import <https://github.com/davisp/ghp-import>`_ tool to put your
html output into the gh-pages branch and push to github.

First install `ghp-import`

.. code-block:: bash

   pip install ghp-import

Then add content to the website and commit

.. code-block:: bash

   git add .
   git commit -m "added content"
   git push origin master

Now build the website and push to gh-pages.

.. code-block:: bash

    cd project
    make html
    cd ..
    ghp-import project/_build/html
    git push origin gh-pages

This is based on a `tip <http://docs.getpelican.com/en/3.0/tips.html>`_ for
publishing `Pelican <https://blog.getpelican.com/>`_ webpages on Github
