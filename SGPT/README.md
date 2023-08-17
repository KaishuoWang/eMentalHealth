# SGPT

This folder contains all files for SGPT.

* SGPT_demo.ipynb:
    * Model: SGPT-BE
    * Use cosine similarity to find match between the given query and taxonomy / records

* mental_SGPT.ipynb:
    * Model: SGPT-BE
    * Use cosine similarity to find match between records and taxonomy

* mental_SGPT_ST.ipynb:
    * Model: SGPT-BE, RoBERTa, XLNet, LLaMA, T5
    * Use cosine similarity to find match between records and taxonomy.
    * This file uses sentence-transformer library.

* sgpt_ce.ipynb:
    * Model: SGPT-CE
    * Use cosine similarity to find match between records and taxonomy
    * In this file, we've also added keyword search to limit the number documents we need to search.

* mental-SGPT-tax-records.ipynb
    * Model: SGPT-BE
    * Use SGPT-BE model to generate embeddings of records and taxonomy.
