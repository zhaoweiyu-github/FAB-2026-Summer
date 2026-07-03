# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FAB-2026-Summer'
copyright = '2026, ZhangLab'
author = 'ZhangLab'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = None
html_favicon = None
html_static_path = ['_static']
html_css_files = ['course.css']
html_theme_options = {
    'navigation_depth': 3,
    'collapse_navigation': False,
    'sticky_navigation': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
