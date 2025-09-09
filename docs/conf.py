from __future__ import annotations

project = "deltakit-textbook"
copyright = "2025, Riverlane Ltd"
author = "Riverlane Ltd"
version = "0.0.1"

extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_design",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "colon_fence",
]

source_suffix = [".rst", ".md"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = "Deltakit Textbook"
html_theme = "sphinxawesome_theme"
html_permalinks_icon = '<span>#</span>'
html_favicon = "logo/deltakit_favicon.png"

html_theme_options = {
    "logo_light": "logo/deltakit_favicon.png",
    "logo_dark": "logo/deltakit_favicon.png",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
templates_path = ["_templates"]
html_css_files = ["overrides.css"]

copybutton_selector = "div:not(.output) > div.highlight pre"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

nitpick_ignore = [
    ("py:class", "_io.StringIO"),
    ("py:class", "_io.BytesIO"),
]

# Configure MathJax v3
mathjax3_config = {
    "tex": {
        "packages": {"[+]": ["physics"]}  # Add the physics package
    },
    "loader": {
        "load": ["[tex]/physics"]         # Load physics extension
    }
}

always_document_param_types = True
jupyter_execute_notebooks = 'off'
nb_execution_timeout = 60
