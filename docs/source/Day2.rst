Day 2
=====

CTCF binding prediction with classical machine learning
-------------------------------------------------------

The assignment is to develop a machine-learning model to predict CTCF binding
events from DNA sequences.

The dataset format is:

.. code-block:: text

   chrom,start,end,build_region_index,peak_k562:ctcf
   chr6,70413000,70414000,1670062,True
   chr4,25173000,25174000,1372412,True
   chr17,47890000,47891000,786861,True
   chr11,44656000,44657000,319623,False
   chrX,48430000,48431000,2087452,False

The first three columns are genomic coordinates, and the fifth column is the
binding label. ``True`` indicates a binding event and ``False`` indicates
non-binding.

Tasks
~~~~~

1. Write a Python script that reads DNA sequences from genomic coordinates.
   You may use `twobitreader <https://pythonhosted.org/twobitreader/>`_ with
   the `human hg38 genome <https://hgdownload.cse.ucsc.edu/goldenpath/hg38/bigZips/>`_.
2. Design sequence features. A simple baseline is to treat a 1-kb DNA sequence
   as 1,000 single-base features. You are encouraged to explore k-mer,
   one-hot, motif-aware, or embedding-based features.
3. Train a random forest classifier for CTCF binding prediction.
4. Evaluate the model on the test set.

Deliverable
~~~~~~~~~~~

Submit Python code or a Jupyter notebook that can reproduce feature extraction,
training, evaluation, and the final metric table.
