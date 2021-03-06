---
layout: post
title:  "How to publish a Python package"
date:   2021-3-5 20:44:37 -0500
categories: tools

---

This blog records the way how I build and publish my first Python package, `SubsetPrivacy` (not released yet). 

My environments:

- macOS Big Sur 11.0.1
- Python 3.6
- Sphinx 3.5.1

# Project structure

A nice start point is this <a class="ui-tooltip" title="Excellent documentation is one of the reason why I prefer Python to R!"><span style="cursor: help;">tutorial</span></a> on how to [packaging Python projects](https://packaging.python.org/tutorials/packaging-projects/). 

It includes 

- The basic structure of an example project
- How to configure metadata for the setup files (with templates)
- Create README and LICENSE (See my previous blog for [how to choose a license]({% post_url 2021-2-3-How-to-choose-an-open-source-license %}))

Now you’ll have a project directory looks like this

```
packaging_tutorial
├── LICENSE
├── README.md
├── example_pkg
│   └── __init__.py
├── pyproject.toml
├── setup.cfg
├── setup.py
└── tests
```

Let's explore how to publish it *before adding any code* :)

Following the instructions of the same tutorial, it tells 

- Generate distributions 
- Upload the package to `Test PyPI` and finally `PyPI`
- Install the package we just uploaded

Congratulations! You’ve published a new Python package! Now, let’s elaborate our project a little bit more. 

## Organize the code

The package I wrote is small — hence no need for sub-packages, I put all of my modules under the `example_pkg` directory. For example,

```
example_pkg
├── __init__.py
├── foo.py
└── bar.py
```

[Here's the documentation for](https://docs.python.org/3/reference/import.html#regular-packages) `__init__.py` . In short, when `example_pkg` is imported, python will automatically execute  this file, which servers as the initialization of the whole project. We can import functions and classes defined in other modules in this file, such as

```python
from .foo import *
from .bar import *
```

Then we when have another python file and 

```python
import example_pkg
```

, the functions in `foo.py` and `bar.py` are available.

**Remark 1:** In the above, we use relative import `from .foo import *` since all the files are under the same directory. Absolute import will be `from example_pkg.foo import *`.

**Remark 2:** Define `__all__` variable in the `foo.py` will influence the behavior of `from .foo import *`, only items listed in the  `__all__` will be imported. Also, if  `__all__`  is not specified, all variables start with `_` or `__` will not be imported. 

**Remark 3:** Test is important! Put the test codes in the parallel folder `tests`. Since I’m not familiar with that, the only recommendation is package [`unittest`](https://docs.python.org/3/library/unittest.html) .

Good, now it’s time to write the documentations!

## Documentations

[`Sphinx`](https://www.sphinx-doc.org/en/master/index.html) makes life easier! It’s the most famous and widely-used tool for documentation generation, specially designed for Python. The quick start given by the official website is somewhat hard for me to understand. After spending some time Googling, I construct my docs with the help of this [tutorial](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html).

1. Install Sphinx using `pip install -U Sphinx`

2. Create and initialize `docs` directory
```bash
$ cd packaging_tutorial
$ mkdir docs
$ cd docs
$ sphinx-quickstart
```
I choose to use a directory "_build" within the root path (here the `docs`).

3. Now the `docs` directory looks like this

   ```
   docs
   ├── _static
   ├── _templates
   ├── _build
   ├── conf.py
   ├── index.rst
   ├── Makefile
   └── make.bat
   ```

   Build html documentations by 

   ```bash
   $ make html
   ```

   and pdf by

   ```bash
   $ make latexpdf
   ```

For `conf.py`, it controls the behavior of building process. Some extensions are almost necessary, 

- Append the root path and code path to the system path

- Add extensions such as 

  ```python
  extensions = [
  "sphinx.ext.intersphinx",
  "sphinx.ext.autodoc",  # auto generate docs for codes
  "sphinx.ext.mathjax",  # render latex
  "sphinx.ext.napoleon",  # for Numpy and Google style documentation
  "nbsphinx",  # enable including jupyter notebook
  ]
  ```

- I override the default theme by readthedocs theme (have to install the theme first through `pip`)

  ```python
  html_theme = "sphinx_rtd_theme"
  ```

Now, feel free to change `index.rst` and add more contents. The website is build based on [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). (Not easy to learn at all!) You can also add extensions like markdown and Jupyter notebook. 

**Remark 4:** I suppose you know how to add documentations for the code, otherwise, here are another two nice references on [Numpy style guide](https://numpydoc.readthedocs.io/en/latest/format.html) and [Google style guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

## Host the docs

[Read the Docs](https://readthedocs.org) is a free docs hosting for open source projects. It’s smooth to host the docs if we already build the docs using `Sphinx` and upload it to the Github. Otherwise, you may manually import the project following [this guide](https://docs.readthedocs.io/en/stable/intro/import-guide.html).

## Ending

Hope it helps you figure out how to build and publish a new Python package. Feel free to reach out if you have any suggestions or questions.