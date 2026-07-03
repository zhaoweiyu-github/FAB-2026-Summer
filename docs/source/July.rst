July
====

Weeks 5-6
---------

During Weeks 5 and 6, your assignment is to fine-tune a pre-trained DNA
language model, such as `DNABERT <https://github.com/jerryji1993/DNABERT>`_ or
`DNABERT-2 <https://github.com/MAGICS-LAB/DNABERT_2>`_, for CTCF binding
prediction.

The training and testing datasets follow the same coordinate-label format used
in June:

.. code-block:: text

   chrom,start,end,build_region_index,peak_k562:ctcf
   chr6,70413000,70414000,1670062,True
   chr4,25173000,25174000,1372412,True
   chr17,47890000,47891000,786861,True
   chr11,44656000,44657000,319623,False
   chrX,48430000,48431000,2087452,False

Tasks
~~~~~

1. Read the `DNABERT paper <https://pubmed.ncbi.nlm.nih.gov/33538820/>`_ and
   inspect the model repository to understand pre-training, tokenization, and
   fine-tuning.
2. Convert each genomic interval into the input format required by the selected
   DNA language model.
3. Load a pre-trained checkpoint and fine-tune it for binary CTCF binding
   classification.
4. Because the dataset may be imbalanced, compare cross-entropy with a
   class-weighted loss or focal loss.

Weeks 7-8
---------

Run the best fine-tuning configuration on GPU resources and prepare a concise
comparison against your June baseline.

Your report should include:

1. Tokenization strategy and maximum sequence length.
2. Training configuration, including batch size, learning rate, epochs, and
   checkpoint selection.
3. Evaluation metrics on the held-out test set.
4. A short discussion of where the language model improves or fails compared
   with the random forest baseline.

Deliverable
~~~~~~~~~~~

Submit reproducible fine-tuning code, a README with the run command, and a
result table that includes both the classical model and the language-model
baseline.
