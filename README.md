# TFIDF-Representation
### TFIDF Representation Assignment of Artificial Intelligence Module in University

The main.py provides tfidf function with the following steps for **preprocessing**:
1. Read the text files from 5 subdirectories in dataset and split the document text into words
2. Remove the stopwords from the text collections, which are frequent words that carry no information. Stopwords list are given in the file stopwords.txt
3. Convert all words into their lower case form. Delete all non-alphabet characters from the text
4. Perform word stemming to remove the word suffix (install the library: nltk in order to run this code for this step)

After preprocessing **TFIDF Representation** is done. The documents are represented as the vector space model. In the vector space model, each document is represented as a vector of words. A collection of documents are represented by a document-by-word matrix A.
Mainly three values are obtained:
1. The frequency of word k in document i
2. The total number of times word k occurs in the dataset called the document frequency
3. Taking into account the length of different documents, we normalize the representation of the document
