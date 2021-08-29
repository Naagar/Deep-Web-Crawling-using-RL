import gensim
# Operating System
import os
# Regular Expression
import re
# nltk packages
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
# Basic Packages
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# PCA Package
from sklearn.decomposition import PCA
stemmer = SnowballStemmer("english")
from nltk.tokenize import word_tokenize, sent_tokenize

# !pip install sentence-transformers
# !pip install huggingface-hub==0.0.12
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# download the stopword for the english
stopWords = pd.read_csv('stopwords.txt').values


# define the function to get the text from the url
def crawler(url):
    webpage = requests.get(url)
    webpagetext = BeautifulSoup(webpage.text, "html.parser")
    all_p = webpagetext.find_all('p')
    text = ""
    for item in all_p:
        text = text + item.get_text()
    return text
wiki_text = crawler(url_wiki)

class MySentences(object):
    def __init__(self, fnamelist):
        self.fnamelist = fnamelist
        # Creating a set of vocabulary
        self.vocabulary = set([])

    def __iter__(self):
        for fname in self.fnamelist:
            for line in open(fname, encoding='latin1'):
                # Find all the words that has letters from 2 - 15. If the words are longer than that ignore.
                words = re.findall(r'(\b[A-Za-z][a-z]{2,15}\b)', line)
                # Stemming a word.
                words = [ stemmer.stem(word.lower()) for word in words if not word.lower() in stopWords]
                for word in words:
                    self.vocabulary.add(word)
                yield words

def get_reward(url, wiki_url):


	# web crawling, get the text for the both link 
	url_text = crawler(url)
	wiki_text = crawler(wiki_url)

	# tokenized the text of  both websites
	tokenized_url = sent_tokenize(url_text)
	tokenized_wiki = sent_tokenize(wiki_text)

	sentences_url = MySentences(tokenized_url) # a memory-friendly iterator
	sentences_wiki = MySentences(tokenized_wiki) # a memory-friendly iterator
	model = SentenceTransformer('bert-base-nli-mean-tokens')

	sentences = [sentences_url, sentences_wiki]
	sentence_embeddings = model.encode(sentences)
	similarity = cosine_similarity( [sentence_embeddings[0]], sentence_embeddings[1:])

	return similarity




# sentences_nvd = MySentences(text_nvd) # a memory-friendly iterator 
# sentences_wiki = MySentences(text_wiki) # a memory-friendly iterator 



# text_nvd = crawler(url_nvd)    # input nvd url for the keyword e.g., Injection, return the text from the nvd website
# text_wiki = crawler(url_wiki)  # input wiki url for the keyword e.g., Injection, return the text from the wiki website

# tokenized_nvd = sent_tokenize(text_nvd)
# tokenized_wiki = sent_tokenize(text_wiki)



# sentences_nvd = MySentences(tokenized_nvd) # a memory-friendly iterator
# sentences_wiki = MySentences(tokenized_wiki) # a memory-friendly iterator

# # # Initialize our model:
# # from sentence_transformers import SentenceTransformer
# # from sklearn.metrics.pairwise import cosine_similarity


# model = SentenceTransformer('bert-base-nli-mean-tokens')

# sentences = [sentences_nvd, sentences_wiki]
# sentence_embeddings = model.encode(sentences)
# # sentence_embeddings.shape ##

# # calculate the similarity for the text
# # Let's calculate cosine similarity for sentence 0:
# similarity = cosine_similarity( 
#     [sentence_embeddings[0]],
#     sentence_embeddings[1:])
# similarity