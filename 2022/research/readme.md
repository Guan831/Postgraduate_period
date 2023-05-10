The research for 2022

This program is about analyzing the user's browsing history to deduce what the user might be interested in when searching

This program contains the following three parts

    Vectorization of the content of user browsing records (web addresses) (TF-IDF to BERT)
    
    Clustering analysis of the vector of browsing records
    
    Analysis of the content of the user's search

    In this experiment, the search file mainly implements the call to Google api, and the raw data collation
    In the vectorization folder, the SentenceBertJapanese .py file contains the files that use SentenceBert vectorization and do Clustering
    The training model we use is sentence-bert-base-ja-mean-tokens-v2