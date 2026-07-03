FAB-2026-Summer
===============

Course documentation for **Functional Annotation Bioinformatics, Summer 2026**.

The site is built with Sphinx and the Read the Docs theme.  It contains a
month-by-month schedule, assignment briefs, datasets, deliverables, and links to
the main tools used in the course.

Build locally
-------------

.. code-block:: console

   python -m pip install -r docs/requirements.txt
   sphinx-build -b html docs/source docs/build/html

The rendered entry point is ``docs/build/html/index.html``.
