========
Trivia 1
========

Customizing Sphinx Output
=========================

The easiest way to customize Sphinx output is to modify the conf.py file.

* In the general configuration section you can:

   * Change the project name
   * Update the copyright
   * update the version
   * .. note::
        The variable ``pygments_style`` is set to 'sphinx' in this section automatically. If you want to create a theme that uses a different style, you need to comment this line to allow the theme to control the style. Alternatively, you can set the pygments style to whatever you like using this variable.

* In the html configuration section you can:

   * select a theme for the overall format of your output and set options if any are available. If you use a custom theme, make sure to set the ``html_theme_path`` variable to include the path of the theme
   * customize your sidebars by uncommenting and filling in the ``html_sidebars`` variable. The standard sidebar includes items like

      * 'localtoc.html' which gives a TOC
      * 'relations.html' which gives you the previous and next choices
      * 'sourcelink.html' which gives you the link to the sourcefile
      * 'searchbox.html' which give the search box
      * you can also include custom templates

   * control index generation
   * control footer properties

* More stuff here???
