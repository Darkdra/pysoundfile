import os
import sys
sys.path.insert(0, os.path.abspath(".."))

project = "My Project"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
html_theme = "sphinx_rtd_theme"
extensions.append("myst_parser")
