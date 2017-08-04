=================================
Using Jupyter notebooks in Sphinx
=================================

Jupyter notebooks can be included in Sphinx documents using the
`nbsphinx extension <http://nbsphinx.readthedocs.io/en/0.2.14/index.html>`_ ::

   sudo -H pip3 install nbsphinx

Once installed, nbspinx needs to be added to the `extensions` section of the
`conf.py` file. It is also a good idea to add `**.ipynb_checkpoints` to the
`exclude_patterns` section. ::

   extensions = ['nbsphinx']
   exclude_patterns = ['_build', '**.ipynb_checkpoints']

The program `pandoc <http://pandoc.org/>`_ also needs to be installed for this
to work

Now you can add your .ipynb files to your Sphinx project
