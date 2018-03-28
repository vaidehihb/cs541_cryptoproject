import gensim
from dbConnect import getContent, getCurrencyNames, readCurrencies
from nltk.tokenize import word_tokenize
import time


def createSims(content):
    gen_docs = [[w.lower() for w in word_tokenize(text)] for text in content]
    dictionary = gensim.corpora.Dictionary(gen_docs)
    print type(dictionary)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    sims = gensim.similarities.Similarity('similarity', tf_idf[corpus], num_features=len(dictionary))
    return dictionary, tf_idf, sims


def getSimilarity(query_content, dictionary, tf_idf, sims):
    query_doc = [w.lower() for w in word_tokenize(query_content)]
    query_doc_bow = dictionary.doc2bow(query_doc)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print sims[query_doc_tf_idf]


def getCurrencyPopularity():
    content_raw = getContent()
    content = [unicode(article[0], errors='ignore') for article in content_raw]
    currencies = readCurrencies()
    for c in currencies:
        c[0] = c[0].lower()
    gen_docs = [[w.lower() for w in word_tokenize(text)] for text in content]
    dictionary = gensim.corpora.Dictionary(currencies)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    total_currencies = [[index, 0] for index in range(len(currencies))]
    for article in corpus:
        for currency in article:
            index = currency[0]
            total_currencies[index][1] += 1
    popular_currencies = [currency for currency in total_currencies if currency[1] > 0]
    popular_currencies = sorted(popular_currencies, key=lambda x: x[1], reverse=True)
    popularity_list = []
    for currency in popular_currencies:
        popularity_list.append([currencies[currency[0]], currency[1]])
    return popularity_list[:10]

