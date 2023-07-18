# OpenAI

This file contains all files that use OpenAI.

* openai.ipynb:
    * We use OpenAI to generate embeddings of the text, then use cosine similarity to find the match between the records and taxonomy.

* re_ranking.ipynb:
    * We use tf-idf to select the first 100 documents then we use OpenAI embeddings to re-rank the documents and select top 10 for each query.

* re_ranking_bm25.ipynb:
    * We use bm25 to select the first 100 documents then we use OpenAI embeddings to re-rank the documents and select top 10 for each query.
