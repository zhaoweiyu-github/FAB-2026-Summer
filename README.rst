Frontiers and Advance of Bioinformatics
=======================================

Course documentation for **Frontiers and Advance of Bioinformatics, Summer
2026**.

The site is built with Sphinx and the Read the Docs theme.  It contains a
day-by-day schedule, assignment briefs, datasets, deliverables, and links to the
main tools used in the course.

Page sites
----------

* GitHub Pages: https://zhaoweiyu-github.github.io/FAB-2026-Summer/
* Read the Docs: https://fab-2026-summer.readthedocs.io/en/latest/
* Local preview: ``docs/build/html/index.html``

Course pages
------------

* Day 1: https://zhaoweiyu-github.github.io/FAB-2026-Summer/Day1.html
* Day 2: https://zhaoweiyu-github.github.io/FAB-2026-Summer/Day2.html
* Day 3: https://zhaoweiyu-github.github.io/FAB-2026-Summer/Day3.html
* Day 4: https://zhaoweiyu-github.github.io/FAB-2026-Summer/Day4.html
* Resources: https://zhaoweiyu-github.github.io/FAB-2026-Summer/resources.html

Build locally
-------------

.. code-block:: console

   python -m pip install -r docs/requirements.txt
   sphinx-build -b html docs/source docs/build/html

The rendered entry point is ``docs/build/html/index.html``.
