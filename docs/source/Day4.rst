Day 4
=====

ChromBERT and final comparative analysis
----------------------------------------

The assignment is to explore
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
4. Track the same metric set used in Day 2 and Day 3.

Final report
~~~~~~~~~~~~

Compare the classical baseline, the DNA language model, and ChromBERT. Discuss
whether cistrome-aware representations help, how class imbalance affects
threshold-dependent metrics, and which model is strongest and easiest to
reproduce.
