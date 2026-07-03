Day 3
=====

DNA language models for CTCF binding prediction
-----------------------------------------------

The assignment is to fine-tune a pre-trained DNA language model, such as
`DNABERT <https://github.com/jerryji1993/DNABERT>`_ or
`DNABERT-2 <https://github.com/MAGICS-LAB/DNABERT_2>`_, for CTCF binding
prediction.

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

Deliverable
~~~~~~~~~~~

Submit reproducible fine-tuning code, a README with the run command, and a
result table comparing the classical model and the language-model baseline.
