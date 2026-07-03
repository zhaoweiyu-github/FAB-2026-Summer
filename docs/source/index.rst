Functional Annotation Bioinformatics
====================================

.. note::

   Advisor: Prof. Yong Zhang and Prof. Qi Wang.

   Practice: transcription factor binding prediction with machine learning,
   deep language models, and cistrome-aware foundation models.

.. raw:: html

   <section class="course-hero">
     <div>
       <p class="eyebrow">FAB 2026 Summer</p>
       <h2>From genomic coordinates to regulatory prediction.</h2>
       <p>
         A compact research practice course on extracting DNA sequences,
         engineering genomic features, fine-tuning pre-trained models, and
         evaluating transcription regulator binding across imbalanced datasets.
       </p>
     </div>
     <div class="hero-metrics" aria-label="Course overview">
       <span><strong>3</strong> project blocks</span>
       <span><strong>8</strong> summer weeks</span>
       <span><strong>2</strong> model families</span>
     </div>
   </section>

Schedule
--------

.. list-table::
   :header-rows: 1
   :class: schedule-table

   * - Month
     - Focus
     - Main output
   * - :doc:`June <June>`
     - Python, scikit-learn, genome sequence extraction
     - Classical CTCF binding classifier
   * - :doc:`July <July>`
     - DNABERT/DNABERT-2 fine-tuning
     - Deep model for imbalanced CTCF prediction
   * - :doc:`August <August>`
     - ChromBERT and comparative analysis
     - CTCF/EZH2 model report and reproducible code

.. raw:: html

   <div class="course-cards">
     <a class="course-card" href="June.html">
       <span>01</span>
       <strong>Classical machine learning</strong>
       <p>Build the end-to-end baseline: coordinates, sequences, features, random forest, and metrics.</p>
     </a>
     <a class="course-card" href="July.html">
       <span>02</span>
       <strong>DNA language models</strong>
       <p>Read DNABERT papers, load checkpoints, fine-tune, and handle imbalanced labels.</p>
     </a>
     <a class="course-card" href="August.html">
       <span>03</span>
       <strong>Cistrome foundation models</strong>
       <p>Use ChromBERT for CTCF and EZH2, then compare model behavior and practical tradeoffs.</p>
     </a>
   </div>

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Course

   June
   July
   August
   resources
