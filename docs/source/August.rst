August
======

Weeks 9-10
----------

During Weeks 9 and 10, your assignment is to explore
`ChromBERT <https://github.com/zhanglabtools/ChromBERT>`_, a pre-trained model
developed for transcription regulatory genomics, and adapt it to binding
prediction tasks.

ChromBERT is pre-trained on large-scale human ChIP-seq, DNase-seq, and ATAC-seq
profiles. Instead of using DNA sequence alone, it can model cistrome context and
regulatory relationships across transcription regulators.

Tasks
~~~~~

1. Read the ChromBERT repository and its fine-tuning tutorial.
2. Prepare input datasets for CTCF and EZH2.
3. Fine-tune ChromBERT separately for CTCF and EZH2 binding prediction.
4. Track the same metric set used in the June and July assignments.

Weeks 11-12
-----------

Compare the classical baseline, the DNA language model, and ChromBERT.

Your analysis should discuss:

1. Whether cistrome-aware representations help on CTCF and EZH2.
2. How class imbalance changes threshold-dependent metrics.
3. Which model is easiest to reproduce and which model is strongest.
4. Possible reasons for disagreement between sequence-only and cistrome-aware
   predictions.

Deliverable
~~~~~~~~~~~

Submit a final report, runnable code, and a results directory containing metric
tables, plots, and the commands used for each experiment.
